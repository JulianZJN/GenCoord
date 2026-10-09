#!/usr/bin/env python3
"""95% cluster-bootstrap intervals for the headline cost effects (10,000 draws).

local_surface_timing_records.csv: 40-cluster local 0.8B surface timing sample (Table 1).
deepseek_protocol_timing_records.csv: 64 interleaved DeepSeek timing pairs (Table 2).
Resampling unit: semantic cluster; all roles, checkpoints, and repeats of a cluster stay together.
"""
import csv, json, random, statistics as st, collections

def q(v):
    v = sorted(v); return [round(v[249], 4), round(v[9749], 4)]

# Local 0.8B surfaces
loc = collections.defaultdict(lambda: collections.defaultdict(list))
for r in csv.DictReader(open("local_surface_timing_records.csv")):
    loc[r["method"]][r["semantic_cluster_id"]].append(
        (float(r["wire_bytes"]), float(r["time_to_commitment_ms"]), float(r["output_tokens"])))
keys = sorted(loc["Short DSL"])
def local_stats(sample):
    agg = {}
    for m in ("Short DSL", "JSON", "Controlled free-form"):
        rows = [x for c in sample for x in loc[m][c]]
        agg[m] = (st.mean(x[0] for x in rows), st.median(x[1] for x in rows), st.mean(x[2] for x in rows))
    s, j, f = agg["Short DSL"], agg["JSON"], agg["Controlled free-form"]
    return {"wire_reduction_vs_free_form": 1 - s[0] / f[0],
            "median_ttc_reduction_vs_free_form": 1 - s[1] / f[1],
            "output_token_ratio_json": j[2] / s[2], "output_token_ratio_free_form": f[2] / s[2],
            "median_ttc_ratio_json": j[1] / s[1], "median_ttc_ratio_free_form": f[1] / s[1]}

# DeepSeek protocol timing (paired by pair_id, resampled by cluster)
pairs = collections.defaultdict(dict)
for r in csv.DictReader(open("deepseek_protocol_timing_records.csv")):
    if r["arm"] in ("SHORT_DSL", "NL_DIALOGUE_WITH_STRUCTURED_COMMIT"):
        pairs[r["pair_id"]][r["arm"]] = (float(r["TTC_s"]), r["cluster_id"])
ds = collections.defaultdict(list)
for v in pairs.values():
    if len(v) == 2:
        ds[v["SHORT_DSL"][1]].append((v["SHORT_DSL"][0], v["NL_DIALOGUE_WITH_STRUCTURED_COMMIT"][0]))
dkeys = sorted(ds)
def ds_stats(sample):
    rows = [x for c in sample for x in ds[c]]
    s = [a for a, _ in rows]; n = [b for _, b in rows]
    return {"mean_ttc_reduction": 1 - st.mean(s) / st.mean(n),
            "median_ttc_reduction": 1 - st.median(s) / st.median(n)}

out = {"local_0.8B": {"clusters": len(keys), "point": {k: round(v, 4) for k, v in local_stats(keys).items()}},
       "deepseek": {"clusters": len(dkeys), "pairs": sum(len(v) for v in ds.values()),
                    "point": {k: round(v, 4) for k, v in ds_stats(dkeys).items()}}}
for name, fn, ks, seed in (("local_0.8B", local_stats, keys, 20261008), ("deepseek", ds_stats, dkeys, 20261007)):
    random.seed(seed); boot = collections.defaultdict(list)
    for _ in range(10000):
        for k, v in fn(random.choices(ks, k=len(ks))).items():
            boot[k].append(v)
    out[name]["ci95"] = {k: q(v) for k, v in boot.items()}
    out[name]["seed"] = seed
json.dump(out, open("cost_intervals.json", "w"), indent=2)
print(json.dumps(out, indent=2))
