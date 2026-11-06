---
type: "Finding"
description: "The flux balance analysis model captures 1.76\u00d7 higher Complex I flux on aromatic substrates (0.55 vs 0.31), but predicts 0% essentiality, seeing the increased demand but not the bottleneck."
finding_id: "aromatic_catabolism_network--7d6bd2aa"
result: "null result"
source: "aromatic_catabolism_network"
quantities: [{"value": "1.76\u00d7", "what": "predicted Complex I flux increase on aromatic substrates", "unit": "fold", "denominator": "", "scope": "flux balance analysis model"}, {"value": "0.55 vs 0.31", "what": "predicted Complex I flux on aromatic substrates vs the comparison", "unit": "", "denominator": "", "scope": "flux balance analysis model"}, {"value": "0%", "what": "predicted essentiality", "unit": "", "denominator": "", "scope": "flux balance analysis model"}]
caveat: "The report argues the model's linear programming framework does not capture the threshold effect of losing any subunit of the multisubunit Complex I, which eliminates function entirely."
first_added: "2026-10-27"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# Flux balance model sees higher Complex I demand but predicts no essentiality

The flux balance analysis model captures 1.76× higher Complex I flux on aromatic substrates (0.55 vs 0.31), but predicts 0% essentiality, seeing the increased demand but not the bottleneck. [src: aromatic_catabolism_network]

## Key figures

- **1.76× fold**: predicted Complex I flux increase on aromatic substrates (scope flux balance analysis model) [src: aromatic_catabolism_network]
- **0.55 vs 0.31**: predicted Complex I flux on aromatic substrates vs the comparison (scope flux balance analysis model) [src: aromatic_catabolism_network]
- **0%**: predicted essentiality (scope flux balance analysis model) [src: aromatic_catabolism_network]

## Evidence

> The FBA model captures 1.76× higher Complex I flux on aromatic substrates (0.55 vs 0.31), but predicts 0% essentiality — it sees the increased demand but not the bottleneck. [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

The report argues the model's linear programming framework does not capture the threshold effect of losing any subunit of the multisubunit Complex I, which eliminates function entirely. [src: aromatic_catabolism_network]

> In reality, Complex I operates as a single multi-subunit complex — loss of any subunit eliminates function entirely, creating a threshold effect that FBA's linear programming framework doesn't capture. [src: aromatic_catabolism_network]

## Other caveats in this report

- NDH-2 compensation is proposed as a likely explanation for ADP1's apparent quinate specificity, not directly established here. [src: aromatic_catabolism_network]
- The report identifies growth-rate optimization and alternative flux routes as reasons the flux balance analysis model may miss a bottleneck. [src: aromatic_catabolism_network]
- The report interprets cross-species fitness as a high-TCA-flux rather than strictly aromatic Complex I dependency; its NDH-2 explanation remains inferential. [src: aromatic_catabolism_network]
- Co-fitness correlations rely on only eight growth conditions, limiting assignment resolution. [src: aromatic_catabolism_network]
- Cross-species ortholog-transferred fitness mixes organisms with different respiratory chains; the report lacks a definitive single-organism aromatic-substrate Complex I test. [src: aromatic_catabolism_network]
