#!/usr/bin/env python3
"""Build the v15 Supplement's E1/E2 table rows from canonical analysis.

The script intentionally accepts only the four v15 conditions.  This keeps the
reader-facing Supplement limited to E1 (feedback-content intervention) and E2
(three-seed centralized full-information completion).
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


EXPECTED_CONDITIONS = (
    "A_ONLY",
    "CORRECT_FEEDBACK",
    "COUNTERFACTUAL_FEEDBACK",
    "CENTRALIZED_FULL_INFO",
)

LABELS = {
    "A_ONLY": "Requester-local (A-only)",
    "CORRECT_FEEDBACK": "Correct bounded feedback",
    "COUNTERFACTUAL_FEEDBACK": "Counterfactual feedback",
    "CENTRALIZED_FULL_INFO": "Centralized full information",
}

INTERFACES = {
    "A_ONLY": "0 B cross-boundary payload",
    "CORRECT_FEEDBACK": "response: mean 103 B",
    "COUNTERFACTUAL_FEEDBACK": "injected response: mean 103 B",
    "CENTRALIZED_FULL_INFO": "state aggregation: mean 956 B",
}

FIELD_LABELS = {
    "craft_actor": "Craft actor",
    "handoff_item": "Handoff item",
    "handoff_count": "Handoff count",
    "peer_suffix": "Peer suffix",
    "goal_item": "Goal item",
    "goal_count": "Goal count",
}


def pct(value: float) -> str:
    return f"{100.0 * value:.1f}\\%"


def ci_text(values: list[float]) -> str:
    lo, hi = values
    return f"$[{100.0 * lo:.0f},{100.0 * hi:.0f}]$"


def tex_escape(text: str) -> str:
    return text.replace("&", r"\&").replace("_", r"\_")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_tabularx_fragment(
    path: Path,
    column_spec: str,
    headers: list[str],
    rows: list[str],
) -> None:
    """Write a complete table body so tabularx can measure it reliably."""
    header = " & ".join(f"\\thead{{{label}}}" for label in headers) + r" \\"
    content = [
        rf"\begin{{tabularx}}{{\textwidth}}{{@{{}}{column_spec}@{{}}}}",
        r"  \toprule",
        f"  {header}",
        r"  \midrule",
        *(f"  {row}" for row in rows),
        r"  \bottomrule",
        r"\end{tabularx}",
    ]
    write_text(path, "\n".join(content) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--analysis", type=Path, required=True)
    parser.add_argument("--training", type=Path, required=True)
    parser.add_argument("--tables-dir", type=Path, required=True)
    parser.add_argument("--data-dir", type=Path, required=True)
    args = parser.parse_args()

    analysis = json.loads(args.analysis.read_text(encoding="utf-8"))
    training = json.loads(args.training.read_text(encoding="utf-8"))

    assert analysis["schema_version"] == "gcp-feedback-intervention-analysis-v0.1"
    assert analysis["episodes"] == 960
    assert analysis["statistical_unit"] == "semantic_cluster"
    assert analysis["training_seeds"] == [2026080601, 2026080602, 2026080603]
    assert set(analysis["conditions"]) == set(EXPECTED_CONDITIONS)
    assert analysis["counterfactual_field_fidelity"]["missing_prediction"] == 0

    outcome_rows: list[dict[str, object]] = []
    outcome_tex: list[str] = []
    for key in EXPECTED_CONDITIONS:
        row = analysis["conditions"][key]
        assert row["episodes"] == 240
        assert row["semantic_clusters"] == 40
        assert row["fallback_episodes"] == 0
        assert row["raw_parse_valid"] == 1.0
        assert row["grounded_valid"] == 1.0
        assert row["planning_complete"] == 1.0

        success = row["terminal_success_cluster_mean"]
        strict = row["strict_clusters_all_replicates_success"]
        calls = row["cost"]["model_calls"]["mean"]
        ci = row["terminal_success_cluster_bootstrap_ci95"]
        outcome_rows.append(
            {
                "condition": key,
                "training_seeds": 3,
                "semantic_clusters": 40,
                "episodes": 240,
                "terminal_success": success,
                "ci95_low": ci[0],
                "ci95_high": ci[1],
                "strict_clusters": strict,
                "mean_model_calls": calls,
                "measured_boundary_component": INTERFACES[key],
            }
        )
        outcome_tex.append(
            f"{LABELS[key]} & 3 & 240 & {pct(success)} & {ci_text(ci)} & "
            f"{strict}/40 & {calls:.1f} & {INTERFACES[key]} \\\\"
        )

    write_csv(args.data_dir / "e1e2_conditions.csv", outcome_rows)
    write_text(args.tables_dir / "e1e2_outcome_rows.tex", "\n".join(outcome_tex) + "\n")
    write_tabularx_fragment(
        args.tables_dir / "e1e2_outcome_table.tex",
        "Z r r r c r r Z",
        ["Condition", "Seeds", "Epis.", "Success", "95\\% CI", "Strict", "Calls", "Measured boundary component"],
        outcome_tex,
    )

    legacy_keys = {
        "A_ONLY": "C_A_ONLY",
        "CORRECT_FEEDBACK": "C_MESSAGE_PASSING",
        "COUNTERFACTUAL_FEEDBACK": "C_COUNTERFACTUAL_FEEDBACK",
        "CENTRALIZED_FULL_INFO": "C_CENTRALIZED",
    }
    compact_private_rows = []
    for row in outcome_rows:
        compact_private_rows.append(
            {
                "condition": legacy_keys[str(row["condition"])],
                "training_seeds": row["training_seeds"],
                "semantic_clusters": row["semantic_clusters"],
                "episodes": row["episodes"],
                "terminal_success_pct": 100.0 * float(row["terminal_success"]),
                "seed_success_sd": 0.0,
                "strict_clusters_success": row["strict_clusters"],
                "mean_calls": row["mean_model_calls"],
                "mean_wire_bytes": (
                    analysis["conditions"][str(row["condition"])]["cost"]["wire_bytes"]["mean"]
                ),
                "ci95_low_pct": 100.0 * float(row["ci95_low"]),
                "ci95_high_pct": 100.0 * float(row["ci95_high"]),
            }
        )
    write_csv(args.data_dir / "private_information.csv", compact_private_rows)

    fidelity_rows: list[dict[str, object]] = []
    fidelity_tex: list[str] = []
    fields = analysis["counterfactual_field_fidelity"]["fields"]
    for key in FIELD_LABELS:
        row = fields[key]
        assert row["eligible"] == 240
        fidelity_rows.append(
            {
                "field": key,
                "eligible": row["eligible"],
                "matches_injected": row["matches_injected"],
                "matches_true": row["matches_true"],
            }
        )
        behavior = "rewritten" if row["matches_true"] == 0 else "invariant"
        fidelity_tex.append(
            f"{FIELD_LABELS[key]} & {row['matches_injected']}/240 & "
            f"{row['matches_true']}/240 & {behavior} \\\\"
        )

    write_csv(args.data_dir / "e1e2_field_fidelity.csv", fidelity_rows)
    write_text(args.tables_dir / "e1e2_field_rows.tex", "\n".join(fidelity_tex) + "\n")
    write_tabularx_fragment(
        args.tables_dir / "e1e2_field_table.tex",
        "Z r r Z",
        ["Field", "Matches injected", "Matches true world", "Observed behavior"],
        fidelity_tex,
    )

    distributed = training["distributed_data"]
    centralized = training["centralized_data"]
    central_contract = training["centralized_contract"]
    dist_contract = training["distributed_contract"]
    assert distributed["rows"] == 640
    assert centralized["rows"] == 320
    assert central_contract["optimizer_updates"] == 80
    assert training["centralized_matched_budget"]["reference"]["optimizer_updates"] == 80
    training_rows = [
        {
            "model": "Distributed requester",
            "view": "320 initial local + 320 after-response local",
            "rows": 640,
            "epochs": dist_contract["epochs"],
            "optimizer_updates": 80,
            "token_exposure": training["centralized_matched_budget"]["reference"]["token_exposure"],
            "training_seeds": 3,
        },
        {
            "model": "Centralized full information",
            "view": "merged current local views",
            "rows": 320,
            "epochs": central_contract["epochs"],
            "optimizer_updates": central_contract["optimizer_updates"],
            "token_exposure": central_contract["token_exposure"],
            "training_seeds": 3,
        },
    ]
    write_csv(args.data_dir / "e1e2_training.csv", training_rows)
    training_tex = [
        "Distributed requester & 320 initial local + 320 after-response local & 640 & 2 & 80 & 868,720 & 3 \\\\",
        "Centralized full information & merged current local views & 320 & 4 & 80 & 970,080 & 3 \\\\",
    ]
    write_text(args.tables_dir / "e1e2_training_rows.tex", "\n".join(training_tex) + "\n")
    write_tabularx_fragment(
        args.tables_dir / "e1e2_training_table.tex",
        "Z Z r r r r r",
        ["Model", "Visible information", "Rows", "Epochs", "Updates", "Train-token occurrences", "Seeds"],
        training_tex,
    )

    comparisons = analysis["paired_comparisons"]
    expected_deltas = {
        "correct_minus_a_only": 0.5,
        "correct_minus_counterfactual": 1.0,
        "centralized_minus_correct": 0.0,
    }
    for key, expected in expected_deltas.items():
        assert comparisons[key]["mean_delta_left_minus_right"] == expected

    sensitivity = analysis["pair_block_sensitivity"]
    assert sensitivity["status"] == "SENSITIVITY_ANALYSIS"
    assert sensitivity["pairing_fields"] == ["private_goal", "world_variant"]
    for key, expected in expected_deltas.items():
        row = sensitivity["comparisons"][key]
        assert row["pair_blocks"] == 20
        assert row["mean_delta_left_minus_right"] == expected

    summary = {
        "schema_version": "gencoord-supplement-e1e2-v15",
        "source_schema": analysis["schema_version"],
        "conditions": list(EXPECTED_CONDITIONS),
        "training_seeds": analysis["training_seeds"],
        "semantic_clusters": 40,
        "role_permutations": 2,
        "episodes_per_condition": 240,
        "total_episodes": 960,
        "counterfactual_control_traces": 240,
        "pair_block_sensitivity": sensitivity,
    }
    write_text(args.data_dir / "e1e2_supplement_summary.json", json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    main()
