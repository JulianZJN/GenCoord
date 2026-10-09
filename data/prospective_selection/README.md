# Prospective selection evidence

## Result-to-source map

- `analysis/summary.json`: final quality and exclusive-card timing, paired intervals, per-choice and per-checkpoint results, writing-task sensitivity, invocation rates, transmission and attempt accounting.
- `analysis/source_aggregates.json`: all quality policies averaged within each test description; `assigned` gives the number of role/checkpoint executions behind each average.
- `descriptions/cal_texts.jsonl`, `cal_labels.jsonl`: 256 calibration descriptions and labels.
- `descriptions/test_texts.jsonl`, `test_labels.jsonl`: 640 test descriptions and labels.
- The complete delivered execution contract and result report are under the root `evidence/selection_experiment/` directory. The current supplement S13 supplies the reader-facing design and results.

## Corpus and provenance

The reported corpus contains 32 execution-check, 256 calibration, and 640 test descriptions. Eight writing tasks share the `gpt-6-astra` service. Task cards, not the previous wording or model-error cases, supplied the writing prompts. Independent language-model tasks performed two blinded review rounds before scoring, with authorship, target labels and model results withheld. The 896 calibration/test descriptions were assigned by a predetermined hash within writing-task and semantic-choice strata. The two delivered text files contain the calibration/test material; the 32 check descriptions are documented by the execution report, not reconstructed here. The writing tasks are not eight human authors. Two high-overlap description pairs are recorded in the result report.

## Frozen rule and complete prespecified findings

The threshold is the 52nd smallest calibration margin, 0.009421091709274076. Strictly lower margins invoke Factor. Calibration routes 51/256, quality routes97/640, and timing routes8/64. Labels participate in the prespecified calibration error-count gate (40 errors against a minimum12), not threshold fitting.

Primary ranking and success effects use97.5% intervals. Secondary intervals use95%. The predeclared noninferiority tolerance against full Factor was−2 percentage points. The quality contrast is−7.526pp,95%[−9.870,−5.208], so that criterion is not met. Full Factor remains the highest-quality policy; the routed policy raises retrieval quality at an intermediate cost.

The quantile rule is a computation-budget rule, not a1% error-risk guarantee. The retained retrieval group has71 errors/543 descriptions. Random and maximum-score comparisons are batch quota-matched controls using unlabeled test prescoring within public templates. Their prescan cost is reported separately; production retrieval still encodes each query fresh.

## Executions and timing

Quality:17,920 assignments,17,726 formed and fulfilled,2,103 fulfilled wrong-task outcomes. Independent exclusive-card timing:1,024 assignments,1,008 formed,1,007 fulfilled; one full-Factor execution has a completion loss. There are no resampled/model-generated experiments in this writing revision.

Costs distinguish protocol request/response bytes from actual IPC, which includes candidate/vector/logging payload. `quality[*].cost_totals_all_attempts`, `timing[*].cost_totals_all_attempts`, `batch_mask_costs`, `attempt_inventory`, `recovery`, and the source timing distributions preserve those details. Quality timings across parallel workers are not the reported same-card operating points. The raw attempt logs themselves are not reconstructed from the supplied summaries.

## Checkpoint and language sensitivity

`per_seed`, `per_seed_effects`, `per_cell`, `per_cell_seed`, `per_cell_ranking_retained_risk`, `writer_task_points`, `leave_one_writer_task_out`, and `repair_damage_by_margin_gate` supply every recorded disaggregation. These are the original archived analyses; this manuscript revision does not recompute bootstrap intervals or create a new selector agreement/risk-coverage analysis.
