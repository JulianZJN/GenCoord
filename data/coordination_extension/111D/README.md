# Prompted communication protocols

`quality_records.csv` contains 1,536 allocated trials: 128 task clusters, two roles, three repetitions, and two protocols. Each protocol has 768 trials. `pair_id` joins the two protocols for a common task, role, and repetition. `role_summary.csv` aggregates by protocol and role. The ten complete conversations are the first ten dialogue records in identifier order, with actual delivered text preserved.

`D_timing_records.csv` contains 64 fresh trials per protocol. It shares the trial definitions but uses `record_id` in place of `assigned_id`, and adds seconds and charge columns. The cost files join to the main trial files by identifier. Quality-pool and fresh-timing usage are distinct samples.

## Trial columns

| Column | Definition |
|---|---|
| `assigned_id`, `record_id` | Allocated trial identifier. |
| `cluster_id` | Semantic task cluster. |
| `template_id`, `family_id` | Task template and semantic family. |
| `role`, `repeat` | Role permutation and repeated-call index. |
| `arm` | Short DSL or dialogue with structured commitment. |
| `pair_id` | Common pairing key across protocols. |
| `result_available` | A complete stored outcome exists. |
| `attempt_number` | Index of the selected completed technical attempt. |
| `status` | Stored outcome status. |
| `C`, `formation` | An executable commitment was formed. |
| `H` | Verified historical material handoff. |
| `T_decl` | Verified terminal state of the declared work. |
| `F` | Fulfillment of the declared plan, including transfer and completion. |
| `G`, `success` | Completion of the original task. |
| `syntax_admitted` | Stored syntactic-admission result. |
| `world_dispatch_intent` | An execution request was stored. |
| `world_started` | World execution actually started, when known. |
| `physical_attempts` | Stored count of physical attempts, when supplied. |
| `TTC_ms`, `TTC_s` | Time to commitment or stopping, in milliseconds or seconds. |
| `peer_application_bytes` | UTF-8 bytes actually delivered between agents, including control messages. |
| `peer_sender_to_receiver_bytes` | Delivered bytes from supplier to receiver. |
| `peer_receiver_to_sender_bytes` | Delivered bytes in the return direction. |
| `logical_calls` | Initiated logical generation calls. |
| `http_attempts` | Provider HTTP attempts, including retries when known. |
| `input_tokens`, `output_tokens` | Stored provider token usage. |
| `billed_tokens` | Sum of known input and output tokens; null if either is unknown. |
| `api_request_bytes`, `api_response_bytes` | Provider request/response body bytes, distinct from peer messages. |
| `length_capped_calls` | Calls stopped by the generation-token cap. |
| `failure_stage` | Broad stage classification derived from stored outcomes. |
| `failed_endpoints` | Endpoints explicitly false; null endpoints are not added to this list. |
| `error_type` | Stored exception type, when present. |
| `api_usd`, `api_usd_low`, `api_usd_high` | Fixed-rate usage estimate and available bounds. |
| `invoice_usd` | Provider invoice amount, null when no invoice was supplied. |
| `api_usd_basis` | Text describing the usage estimate. |

An empty CSV cell means unavailable or inapplicable, whereas `false` means an observed negative result. Post-formation world fields may be null after a formation stop. The rates per million tokens are USD 0.30 for uncached or cache-created input, USD 0.006 for cache-read input, and USD 1.20 for output. Means use available entries; unknown usage is not zero.

The `turns` array in each conversation contains `turn` (index), `speaker`, `recipient`, `text` (delivered text), `utf8_bytes`, `protocol_valid`, `commitment_closed`, and `protocol_reason`. Proposal IDs inside these messages are part of the protocol and remain unchanged.
