# Reproducibility scope

This repository releases the paper source, final figures, compact canonical evidence, and a deterministic builder for the E1/E2 supplementary tables.

## Rebuild the E1/E2 tables

From the repository root:

```bash
python3 paper/anc/scripts/build_e1e2_tables.py \
  --analysis paper/anc/source_data/e1e2_analysis.json \
  --training paper/anc/source_data/e1e2_training_budget.json \
  --tables-dir paper/tables \
  --data-dir paper/anc/source_data
```

Equivalently:

```bash
make evidence
```

The builder uses only Python's standard library. It checks the expected schema, conditions, episode counts, semantic-cluster unit, training seeds, parse and grounding validity, fallback count, and selected paired-comparison deltas before writing the released CSV and LaTeX fragments.

Generated paper fragments:

- `paper/tables/e1e2_outcome_table.tex`
- `paper/tables/e1e2_field_table.tex`
- `paper/tables/e1e2_training_table.tex`
- `paper/tables/e1e2_outcome_rows.tex`
- `paper/tables/e1e2_field_rows.tex`
- `paper/tables/e1e2_training_rows.tex`

Generated compact data include:

- `paper/anc/source_data/e1e2_conditions.csv`
- `paper/anc/source_data/e1e2_field_fidelity.csv`
- `paper/anc/source_data/e1e2_training.csv`
- `paper/anc/source_data/private_information.csv`

After initializing the directory as a Git repository, the deterministic check is:

```bash
make verify-evidence
```

It rebuilds the outputs and fails if tracked table or compact-data files change.

## Build the manuscript

```bash
make main
make supplement
make combined
```

Expected document structure:

- main paper: 9 pages, including references;
- supplementary material: 16 pages;
- combined preprint: 25 pages.

## Evidence boundary

The compact evidence supports table reconstruction and source-value inspection. This release does **not** include the full Minecraft runtime, raw episode directories, training checkpoints, complete training pipeline, or editable figure-authoring files. Consequently, it should not be described as a full end-to-end training or environment reproduction package.
