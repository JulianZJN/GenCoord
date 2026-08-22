# Ancillary data

`source_data/` contains the compact canonical data released with the GenCoord
preprint.  `scripts/build_e1e2_tables.py` deterministically regenerates the
three E1/E2 LaTeX table fragments used by `supplement.tex`.

From the submission-source root:

```sh
python3 anc/scripts/build_e1e2_tables.py \
  --analysis anc/source_data/e1e2_analysis.json \
  --training anc/source_data/e1e2_training_budget.json \
  --tables-dir tables \
  --data-dir anc/source_data
```

Runtime dependencies named in the Supplement are governed by their upstream
licenses and terms.  Editable authoring files and raw Minecraft texture assets
are not part of this arXiv ancillary release.
