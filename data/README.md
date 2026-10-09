# Data guide

All numerical results retain their original precision. CSV files use UTF-8; an empty cell and JSON `null` indicate unavailable or inapplicable data. They are distinct from an observed false or zero value. Identifiers and protocol field names are kept stable so paired trials can be joined.

## Outcomes

| Field | Meaning |
|---|---|
| `C`, `formation`, `planning_complete` | A complete commitment has been formed and admitted. |
| `H` | The material handoff was verified. This is a historical event, so later consumption does not erase it. |
| `T_decl` | The terminal outcome specified by the delivered commitment was verified. |
| `F` | The committed work was fulfilled, using the handoff and declared completion checks. |
| `G`, `success` | The unchanged original task was completed, including its required assignment. |
| `M` | The raw receiver continuation matches the delivered request before admission. It is a protocol check, distinct from later physical fulfillment. |
| `fulfilled_wrong_task` | Fulfillment is true and original-task success is false. |
| `unformed` | No admitted commitment. |
| `handoff_failure`, `completion_failure` | Loss after formation at the indicated execution stage. |
| `assigned` | All trials allocated to the configuration, including unsuccessful or unformed trials. |
| `*_pct` | A percentage on the explicitly stated assigned population. |
| `*_state` | Availability status: `measured`, `source_null`, or `missing_record`. |

The stages belong to different experiments. In particular, the main selector comparison reports assignment correctness before execution. Its task-success field `G` is a different endpoint; the manuscript's selection accuracy must be reconstructed from the selected assignment, not substituted by `G`.

## Identifiers and repeated measurements

`record_id` and `assigned_id` identify trials. `cluster_id`, `semantic_cluster_id`, and `pair_id` identify the paired task units in their respective experiments. `source_group`, `source_id`, and the legacy field `mother_id` identify a source description. A `cell` is a template--assignment combination. `role` gives the role permutation, and `seed`, `repeat`, or `api_repeat` identify training checkpoints or repeated calls. These repeated measurements do not create new independent descriptions or task clusters.

## Costs

`TTC_ms` and `time_to_commitment_ms` are milliseconds to commitment formation or a stopped formation attempt. `TTC_s` is the corresponding quantity in seconds. World execution occurs later. `T_episode` fields include the complete executed episode under the associated experiment's timing definition. `formation_service_ms` measures formation service time. `model_calls` and `logical_calls` count generation calls; `encoder_calls` counts embedding queries separately. Technical HTTP attempts are reported separately from logical calls. The 64 DeepSeek timing pairs follow one fixed alternating order; 51 pairs were measured in a first session and the remaining 13 in a second session the next day, with each pair measured back to back.

`peer_application_bytes`, `wire_bytes`, and peer directional byte columns concern messages delivered between agents. API request/response bytes and IPC bytes are separate fields. Local structured-surface payload counts the request; the local free-form ledger counts peer dialogue. The private-structure ledger includes requests and acknowledgments. The prompted two-protocol ledger counts all delivered peer messages, including control messages. These ledgers retain their published definitions rather than being silently merged.

Input-token totals include protocol examples and context encoding. The API charge columns are estimates based on fixed token rates and available usage, not provider invoices. Missing usage remains missing. `billed_tokens` is a token count, not a monetary charge. The charge basis is recorded in English without changing the amounts.

## File groups and appendix navigation

| Appendix | Sources |
|---|---|
| S1--S4: protocol, tasks, training, and information | `task_templates.csv`, `training_runs.csv`, `workcell_*`, `runtime_trace*`, `private_information.csv` |
| S5: local surfaces and horizon | `representation_cost.csv`, `horizon_summary.json`, `horizon_family.csv`, `heldout_failure_analysis.json`, `cost_contrasts/` |
| S6: prompted protocols and feedback | `coordination_extension/111D/`, `coordination_extension/111BC/C_*` |
| S7: private task structure | `final_evidence/private_*` |
| S8: formation backends and fixed-sender receivers | `backend_comparison.csv`, `composition_reference.csv`, `final_evidence/a1_*` |
| S9: online natural descriptions | `online_descriptions/` |
| S10: planning descriptions | `naturalized_private_fact_*`, `final_evidence/naturalized_*` |
| S11: prospective selection and hosted selectors | `prospective_selection/`, `coordination_extension/111A/`, `coordination_extension/timing/` |
| S12: protocol diagnostics | `request_intervention.csv`, `counterfactual_traces.json`, `workcell_*`, `final_evidence/api_*`, `coordination_extension/111BC/B_*` |
| S13: structural cues | `visibility_*`, `final_evidence/stage_order_analysis.json` |

Legacy file names and raw method identifiers are stable join keys. The English method names used in the paper are defined below and in the local data guides.

## Method aliases

| Raw identifier | Manuscript name |
|---|---|
| `D2` / `D1` | Direct with learned / deterministic receiver |
| `F2` / `F1` | Factor with learned / deterministic receiver |
| `T1` | TF--IDF retrieval |
| `L1` | Supervised lexical classifier |
| `R1` | Embedding retrieval |
| `O1` | Privileged true-assignment reference |
| `R_ALL` | Embedding retrieval for all descriptions |
| `F_FIRST` | Factor for all descriptions |
| `RF_MARGIN` | Retrieval with low-margin decisions routed to Factor |
| `S_ALL` | Hosted DeepSeek selector for all descriptions |
| `RS_MARGIN` / `fresh_RS_MARGIN` | Retrieval with low-margin decisions routed to DeepSeek |
| `SHORT_DSL` | Short DSL protocol |
| `NL_DIALOGUE_WITH_STRUCTURED_COMMIT` | Dialogue with structured commitment submission |

Machine directory values have been replaced by anonymous source identifiers. These replacements affect provenance text only; numerical observations, null values, trial identifiers, prompts, and delivered dialogue are preserved. The accompanying `CSV_FIELDS.json` lists the columns actually present in each CSV. The appendix supplies the operational definitions for each experimental family.
