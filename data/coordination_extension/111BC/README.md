# Structured feedback and diagnostic data

The feedback tables contain 40 independent mode pairs, two processing modes, two roles, three API repetitions, and three conditions, for 1,440 allocated trials. Each condition has 480 trials. `CONTROLLED_REVISION` supplies the initial proposal; `TRUE` and `ALT` specify correct and alternative feedback. `E2E_TRUE` includes initial proposal generation and revision.

`C_records.csv` gives one row per trial. `pair_id`, `goal`, `mode`, `role`, `api_repeat`, and `world_variant` identify its conditions. `record_present` records availability. `C`, `H`, `T_decl`, `F`, `product`, and `G` report formation, handoff, declared terminal outcome, fulfillment, requested-product completion, and original-task success. These checks are distinct; a delivered product can be associated with an incorrect actor assignment.

`raw_follow_exact`, `raw_follow_actor`, `raw_follow_handoff`, and `raw_follow_suffix` assess whether the raw revised proposal follows the delivered feedback in its complete object, processing actor, transferred item, or continuation. Each corresponding `_state` field distinguishes `measured`, `source_null`, and `missing_record`.

`C_context_outcomes.csv` pivots the conditions into prefixes `true_`, `alternative_`, and `e2e_`, with the same endpoint meanings. `C_pair_counts.csv` summarizes each endpoint by mode pair and condition. `assigned` is normally 12 per pair-condition; `successes`, `failures`, `NA`, and `missing_records` remain separate. `full_denominator_fraction` is successes divided by assigned trials.

The raw mode label `FINISHED_RECEIVER` denotes the assignment in which the requester crafts and hands over the finished item. `RAW_PROCESSOR` denotes the assignment in which the peer crafts from handed-over material. These are task-assigned modes, not physical ability restrictions. Correct, alternative, and full-interaction results remain distinct.

`C_api_costs.csv` gives token-rate estimates for available usage, with null invoice amounts when no invoice is supplied. `C_author_reported_interval.json` is the supplied paired interval for correct versus alternative feedback. Files beginning with `B_` contain the fault-injection diagnostic: original condition labels, checked layers, stage signatures, and outcome counts. Failure-code strings are the evaluator's protocol labels.
