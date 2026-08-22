<div align="center">

# GenCoord

### Skill-Path Commitments under Private Information

**Turning distributed private facts into verified joint action.**

<p>
  <a href="docs/GenCoord_preprint.pdf"><b>Paper</b></a>
  &nbsp;·&nbsp;
  <a href="paper/"><b>LaTeX source</b></a>
  &nbsp;·&nbsp;
  <a href="docs/REPRODUCIBILITY.md"><b>Reproducibility</b></a>
  &nbsp;·&nbsp;
  <a href="paper/anc/source_data/"><b>Compact evidence</b></a>
  &nbsp;·&nbsp;
  <a href="#citation"><b>Citation</b></a>
</p>

<p>
  <a href="docs/GenCoord_preprint.pdf"><img src="https://img.shields.io/badge/paper-preprint-b31b1b.svg?style=flat-square" alt="Paper preprint"></a>
  <a href="paper/"><img src="https://img.shields.io/badge/source-LaTeX-008080.svg?style=flat-square" alt="LaTeX source"></a>
  <a href="docs/REPRODUCIBILITY.md"><img src="https://img.shields.io/badge/artifact-compact%20evidence-6f42c1.svg?style=flat-square" alt="Compact evidence artifact"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-mixed%20rights-555555.svg?style=flat-square" alt="Mixed-rights license"></a>
</p>

**Peng He**<sup>1,&#42;</sup>, **Junning Zhu**<sup>2,&#42;</sup>, **Haohan Yuan**<sup>3</sup>, **Jianpeng Liang**<sup>4</sup>  
<sup>&#42; Equal contribution</sup>

<table>
  <tr>
    <td width="25%" align="center" valign="middle">
      <a href="https://www.tsinghua.edu.cn/">
        <img src="assets/affiliations/tsinghua.png" width="150" alt="Tsinghua University">
      </a>
    </td>
    <td width="25%" align="center" valign="middle">
      <a href="https://www.bnbu.edu.cn/">
        <img src="assets/affiliations/bnbu.svg" width="180" alt="Beijing Normal-Hong Kong Baptist University">
      </a>
    </td>
    <td width="25%" align="center" valign="middle">
      <a href="https://www.charlotte.edu/">
        <img src="assets/affiliations/unc_charlotte.png" width="190" alt="University of North Carolina at Charlotte">
      </a>
    </td>
    <td width="25%" align="center" valign="middle">
      <a href="https://ucsd.edu/">
        <img src="assets/affiliations/uc_san_diego.png" width="200" alt="University of California San Diego">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center"><sub><sup>1</sup> Tsinghua University<br>Beijing, China</sub></td>
    <td align="center"><sub><sup>2</sup> <b>Beijing Normal-Hong Kong Baptist University (BNBU)</b><br>Zhuhai, China</sub></td>
    <td align="center"><sub><sup>3</sup> UNC Charlotte<br>Charlotte, United States</sub></td>
    <td align="center"><sub><sup>4</sup> UC San Diego<br>San Diego, United States</sub></td>
  </tr>
</table>

</div>

<p align="center">
  <img src="assets/teaser.png" width="100%" alt="GenCoord resolves sender-local and peer-local task consequences into a shared executable commitment before grounded Minecraft execution.">
</p>
<p align="center">
  <sub><b>GenCoord in one view.</b> Private task consequences cross the agent boundary through a typed commitment, then enter one shared grounded execution and verification stack.</sub>
</p>

> **TL;DR.** GenCoord communicates the **executable consequence** of a private fact—not the full private state—as a typed, multi-step `SELF+REQ` commitment that is resolved across agents and verified through grounded execution.

<p align="center">
  <code>private fact → β(z) → SELF + REQ → resolved commitment → grounded skills → verified terminal state</code>
</p>

## Overview

Embodied teams often face a simple structural problem: the fact that determines a joint route may be visible to only one endpoint of a coordination edge. One agent may know the goal, while another alone knows which transformation its workcell can perform. Neither local view is sufficient to determine the actor, handoff item, destination, and continuation.

GenCoord makes that execution-relevant binding explicit. A local Qwen3.5-0.8B model proposes role-local paths in a compact `SELF+REQ` schema; bounded `ACCEPT` / `REJECT` / `COUNTER` feedback resolves peer-local capability ambiguity. The resulting commitment is parsed, schema-checked, canonically materialized, compiled to Mineflayer skills, executed, and verified by handoff and terminal state.

| Private information | Executable commitment | Grounded closure |
| --- | --- | --- |
| Route-determining facts remain local until their task consequence must cross an agent boundary. | One typed, multi-step `SELF+REQ` object binds actor, handoff item, destination, and continuation. | The same resolved object passes through check, materialization, compilation, execution, and verification. |

## Results at a glance

| Paired capability feedback | Multi-step commitment horizon | Communication surface |
| :---: | :---: | :---: |
| **50% → 100%** | **91.3% → 98.1%** | **−92.8% peer traffic** |
| Terminal success with correct bounded feedback, consistently across three independently trained seeds. | Held-out-template success, while model decisions fall from **2.91 → 1.98 per episode** (**−32%**). | At **128/128** matched closed-loop semantic clusters; median time-to-commitment also falls by **68.2%** versus controlled free-form. |

Counterfactual interventions hold the world, call schedule, and executor fixed while changing the injected task consequence; requester revision and receiver execution follow the intervention in both directions.

## Artifact scope

This repository is a **paper-source and compact-evidence release**. It is designed to make the manuscript, figures, reported source values, and deterministic E1/E2 table construction inspectable without overstating the release as a full runtime reproduction package.

| Component | Release status | What it supports |
| --- | --- | --- |
| Main paper, supplement, references, and venue-support source | **Released** | Rebuild and inspect the manuscript. |
| Final publication figures and generated LaTeX table fragments | **Released** | Trace the visual and tabular paper artifacts. |
| Compact canonical evidence and source ledger | **Released** | Inspect reported values and selected paired comparisons. |
| Deterministic E1/E2 table builder | **Released** | Rebuild the released CSV and LaTeX fragments. |
| Full Minecraft runtime, raw episode directories, checkpoints, and training pipeline | **Not in this release** | Not required for source-value inspection; full end-to-end reproduction is outside this artifact boundary. |
| Raw Minecraft texture assets and editable PowerPoint / Draw.io files | **Not in this release** | Authoring and third-party assets are excluded. |

The precise evidence boundary is documented in [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

## Quick start

```bash
git clone https://github.com/JulianZJN/GenCoord.git
cd GenCoord

# Rebuild the manuscript
make main
make supplement
make combined

# Rebuild and verify the released compact evidence
make evidence
make verify-evidence
```

<details>
<summary><b>Build requirements and expected outputs</b></summary>

- A recent TeX Live distribution with PDFLaTeX and BibTeX.
- Python 3.9 or newer; the evidence builder uses only the Python standard library.
- `pdfunite` only for the combined preprint target.

Expected outputs:

```text
paper/main.pdf
paper/supplement.pdf
build/GenCoord_preprint.pdf
```

The current release builds a 9-page main paper, a 16-page supplement, and a 25-page combined preprint.

</details>

The arXiv-oriented source order is recorded in [`paper/00README.json`](paper/00README.json).

## Reproducibility

The compact evidence builder validates the expected schema, experimental conditions, episode counts, semantic-cluster unit, training seeds, parse and grounding validity, fallback count, and selected paired-comparison deltas before writing the released outputs.

```bash
make evidence
```

Generated manuscript fragments include:

```text
paper/tables/e1e2_outcome_table.tex
paper/tables/e1e2_field_table.tex
paper/tables/e1e2_training_table.tex
```

After cloning the repository, the deterministic consistency check is:

```bash
make verify-evidence
```

It rebuilds the outputs and fails if tracked table or compact-data files change. See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) for the exact command, generated files, and evidence boundary.

## Repository structure

```text
.
├── README.md
├── CITATION.cff
├── Makefile
├── assets/
│   ├── teaser.png
│   └── affiliations/
├── docs/
│   ├── GenCoord_preprint.pdf
│   └── REPRODUCIBILITY.md
└── paper/
    ├── main.tex
    ├── supplement.tex
    ├── references.bib
    ├── figures/
    ├── tables/
    └── anc/
        ├── scripts/build_e1e2_tables.py
        └── source_data/
```

## Citation

The arXiv identifier will be added after the public record is assigned. Until then, use the metadata in [`CITATION.cff`](CITATION.cff):

```bibtex
@misc{he2026gencoord,
  title        = {GenCoord: Skill-Path Commitments under Private Information},
  author       = {Peng He and Junning Zhu and Haohan Yuan and Jianpeng Liang},
  year         = {2026},
  note         = {Preprint}
}
```

## Acknowledgements and licensing

GenCoord uses Minecraft as an embodied evaluation environment and compiles validated commitments to Mineflayer skills. Minecraft, Mineflayer, institutional marks, and bundled venue-support files remain governed by their respective owners and licenses. University marks identify author affiliations only and do not imply institutional endorsement. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`assets/affiliations/SOURCES.md`](assets/affiliations/SOURCES.md).

This is a mixed-rights research release:

- Original project code and build glue listed in [`LICENSE`](LICENSE) are available under the [MIT License](LICENSES/MIT.txt).
- The manuscript, author-owned figures, and compact evidence remain copyright of the GenCoord authors, with all rights reserved pending final publication rights.
- Institutional marks, venue-support files, Minecraft-related material, and other third-party content remain governed by their respective owners.

The exact path-level scope is defined in [`LICENSE`](LICENSE).
