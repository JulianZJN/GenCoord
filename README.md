<div align="center">

# GenCoord

### Skill-Path Commitments under Private Information

[![Paper PDF](https://img.shields.io/badge/Paper-PDF-b31b1b.svg)](docs/GenCoord_preprint.pdf)
[![LaTeX source](https://img.shields.io/badge/Source-LaTeX-008080.svg)](paper/main.tex)
[![Reproducibility](https://img.shields.io/badge/Artifact-Compact%20Evidence-6f42c1.svg)](docs/REPRODUCIBILITY.md)

**Peng He\***<sup>1</sup>, **Junning Zhu\***<sup>2</sup>, Haohan Yuan<sup>3</sup>, and Jianpeng Liang<sup>4</sup>  
<sup>\*</sup>Equal contribution

<table>
  <tr>
    <td align="center"><a href="https://www.tsinghua.edu.cn/"><img src="assets/affiliations/tsinghua.png" height="48" alt="Tsinghua University"></a></td>
    <td align="center"><a href="https://www.bnbu.edu.cn/"><img src="assets/affiliations/bnbu.svg" height="48" alt="Beijing Normal-Hong Kong Baptist University"></a></td>
    <td align="center"><a href="https://www.charlotte.edu/"><img src="assets/affiliations/unc_charlotte.png" height="48" alt="University of North Carolina at Charlotte"></a></td>
    <td align="center"><a href="https://ucsd.edu/"><img src="assets/affiliations/uc_san_diego.png" height="48" alt="University of California San Diego"></a></td>
  </tr>
  <tr>
    <td align="center"><sup>1</sup>Tsinghua University</td>
    <td align="center"><sup>2</sup>BNBU</td>
    <td align="center"><sup>3</sup>UNC Charlotte</td>
    <td align="center"><sup>4</sup>UC San Diego</td>
  </tr>
</table>

</div>

<p align="center">
  <img src="assets/teaser.png" width="100%" alt="GenCoord resolves sender-local and peer-local task consequences into a shared executable commitment before grounded Minecraft execution.">
</p>

GenCoord studies embodied coordination when the facts that determine a joint plan are split across agents. It represents the executable consequence of those private facts as a typed, multi-step `SELF+REQ` skill-path commitment. The commitment is resolved across the agent boundary, checked and canonically materialized, compiled to Mineflayer skills, and verified through handoff and terminal state.

## Key results

| Question | Result |
| --- | --- |
| Can bounded capability feedback close paired local ambiguity? | **50% → 100%** terminal success across three independently trained seeds. |
| Do multi-step commitments reduce online replanning? | **91.3% → 98.1%** held-out-template success and **2.91 → 1.98** model decisions per episode (**−32%**). |
| Can communication be compressed without reducing closed-loop quality? | Short DSL, JSON, and controlled free-form each complete **128/128** held-out semantic clusters; Short DSL reduces peer traffic by **92.8%** and median time-to-commitment by **68.2%** versus controlled free-form. |

## Release scope

This repository is the public paper-source and compact-evidence release.

| Included | Status |
| --- | --- |
| Main-paper and supplementary LaTeX source | Included |
| Final publication figures and generated table fragments | Included |
| Compact canonical evidence used by the paper | Included |
| Deterministic E1/E2 table builder | Included |
| Full Minecraft runtime and model-training pipeline | **Not included in this release** |
| Raw Minecraft texture assets and editable PowerPoint/Draw.io authoring files | **Not included in this release** |

The bundled evidence supports rebuilding the released paper tables and auditing their source values. It does not by itself reproduce model training or the full Minecraft execution environment.

## Repository layout

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

## Build the paper

Requirements:

- a recent TeX Live distribution with PDFLaTeX and BibTeX;
- Python 3.9 or newer for the compact evidence builder;
- `pdfunite` only if a combined main-plus-supplement PDF is desired.

```bash
git clone https://github.com/JulianZJN/GenCoord.git
cd GenCoord

make main        # paper/main.pdf
make supplement  # paper/supplement.pdf
make combined    # build/GenCoord_preprint.pdf
```

The arXiv-oriented source order is also recorded in [`paper/00README.json`](paper/00README.json).

## Rebuild the released evidence tables

The table builder uses only the Python standard library:

```bash
make evidence
```

For the exact command, expected outputs, and evidence boundary, see [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

## Citation

The arXiv identifier will be added after the public record is assigned. Until then, please cite the preprint metadata in [`CITATION.cff`](CITATION.cff):

```bibtex
@misc{he2026gencoord,
  title        = {GenCoord: Skill-Path Commitments under Private Information},
  author       = {Peng He and Junning Zhu and Haohan Yuan and Jianpeng Liang},
  year         = {2026},
  note         = {Preprint}
}
```

## Acknowledgements and third-party material

GenCoord uses Minecraft as an embodied evaluation environment and compiles validated commitments to Mineflayer skills. Minecraft, Mineflayer, institutional marks, and the bundled venue-support files remain governed by their respective owners and licenses. The university marks identify author affiliations only and do not imply institutional endorsement. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`assets/affiliations/SOURCES.md`](assets/affiliations/SOURCES.md).

## License

This is a mixed-rights research release:

- the original table builder and build glue are available under the [MIT License](LICENSES/MIT.txt);
- the manuscript, author-owned figures, and compact evidence remain copyright of the GenCoord authors, with all rights reserved pending final publication rights;
- institutional marks, venue-support files, Minecraft-related material, and other third-party content remain governed by their respective owners.

The exact path-level scope is defined in [`LICENSE`](LICENSE). No rights to institutional marks or third-party material are granted by the project license.
