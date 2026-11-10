---
type: "Finding"
description: "Ortholog-transferred fitness data from the Fitness Browser (12,241 entries, 2,005 genes, 13 conditions) shows Complex I orthologs have significantly worse fitness on aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001)."
finding_id: "aromatic_catabolism_network--3128e9e3"
result: "observation"
source: "aromatic_catabolism_network"
quantities: [{"value": "-1.35", "what": "mean Complex I ortholog fitness on aromatic conditions", "unit": "", "denominator": "", "scope": "Fitness Browser ortholog-transferred data"}, {"value": "-0.77", "what": "mean Complex I ortholog fitness on comparison conditions", "unit": "", "denominator": "", "scope": "Fitness Browser ortholog-transferred data"}, {"value": "12,241", "what": "ortholog-transferred fitness entries", "unit": "entries", "denominator": "", "scope": "2,005 genes, 13 conditions"}]
caveat: "The report interprets the cross-species data as a high-TCA-flux dependency (aromatics, acetate, succinate) with NDH-2 sufficing on glucose and lactate, which remains inferential."
first_added: "2026-10-27"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# Complex I orthologs show worse fitness on aromatic conditions across species

Ortholog-transferred fitness data from the Fitness Browser (12,241 entries, 2,005 genes, 13 conditions) shows Complex I orthologs have significantly worse fitness on aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001). [src: aromatic_catabolism_network]

## Key figures

- **-1.35**: mean Complex I ortholog fitness on aromatic conditions (scope Fitness Browser ortholog-transferred data) [src: aromatic_catabolism_network]
- **-0.77**: mean Complex I ortholog fitness on comparison conditions (scope Fitness Browser ortholog-transferred data) [src: aromatic_catabolism_network]
- **12,241 entries**: ortholog-transferred fitness entries (scope 2,005 genes, 13 conditions) [src: aromatic_catabolism_network]

## Evidence

> Ortholog-transferred fitness data from the Fitness Browser (12,241 entries, 2,005 genes, 13 conditions) shows Complex I orthologs have significantly worse fitness on aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001). [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

The report interprets the cross-species data as a high-TCA-flux dependency (aromatics, acetate, succinate) with NDH-2 sufficing on glucose and lactate, which remains inferential. [src: aromatic_catabolism_network]

> Our cross-species data supports this: Complex I is dispensable on glucose and lactate (where NDH-2 suffices) but essential on substrates that generate high TCA cycle flux (aromatics, acetate, succinate). [src: aromatic_catabolism_network]

## Other caveats in this report

- NDH-2 compensation is proposed as a likely explanation for ADP1's apparent quinate specificity, not directly established here. [src: aromatic_catabolism_network]
- The report identifies growth-rate optimization and alternative flux routes as reasons the flux balance analysis model may miss a bottleneck. [src: aromatic_catabolism_network]
- The report argues that the model's linear framework misses the threshold effect of disabling a multisubunit Complex I. [src: aromatic_catabolism_network]
- Co-fitness correlations rely on only eight growth conditions, limiting assignment resolution. [src: aromatic_catabolism_network]
- Cross-species ortholog-transferred fitness mixes organisms with different respiratory chains; the report lacks a definitive single-organism aromatic-substrate Complex I test. [src: aromatic_catabolism_network]
