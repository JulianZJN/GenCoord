# Round 4 materials

| File | Content |
|---|---|
| `local_surface_timing_records.csv` | Per-episode records of the local 0.8B surface timing sample behind Table 1: 3 surfaces × 40 clusters × 2 roles × 3 checkpoints = 720 rows. Columns: method, checkpoint seed, cluster, role, template, family, model calls, input/output tokens, peer wire bytes, time to commitment (ms), whether the selected binding is correct. Means and medians reproduce Table 1 exactly (Short DSL 76.275 B, 2265.6 ms median TTC, 78.6 output tokens; JSON 303.425 B, 7067.4 ms, 267.6; controlled free-form 1061.05 B, 7132.3 ms, 265.8). |
| `deepseek_protocol_timing_records.csv` | The 128 interleaved DeepSeek timing records behind Table 2 (64 per protocol), same file as in the round-2 data package. |
| `cost_intervals.py` | Cluster-bootstrap script (10,000 draws, resampling semantic clusters) for the headline cost effects. |
| `cost_intervals.json` | Its output: point estimates and 95% intervals. |

Wire accounting in the local file: Short DSL and JSON count the delivered request; controlled free-form counts every dialogue message in both directions. The DeepSeek ledger counts every delivered message in both directions, including the Short DSL receiver's acknowledgment (mean 16.0 B).
