# Local and hosted decision timing

The timing data include 128 observations for each of four selection strategies. Fields retain their original units, including millisecond decision durations and USD usage estimates. Strategy identifiers follow the assignment-selection guide in `../111A/README.md`. Where a file also contains protocol timing records, distinguish the `study` or task-family field before aggregating. The interleaved final two-protocol timing sample used in the paper is provided directly in `../111D/D_timing_records.csv` and `../../cost_contrasts/deepseek_protocol_timing_records.csv`.

Missing times or charges remain null. An API cost is a fixed-token-rate estimate; an invoice field is null when no invoice was provided. For the paper's selection table, use assignment correctness before world execution and the decision-time rows for that strategy, rather than the downstream task-success column.
