---
type: "Finding"
description: "Per-condition analysis reveals that the largest Complex I defects relative to background are on acetate (-1.55) and succinate (-1.39), non-aromatic substrates that also generate high NADH flux through the TCA cycle, qualifying an aromatic-specific interpretation."
finding_id: "aromatic_catabolism_network--3a51f6c6"
result: "correction"
source: "aromatic_catabolism_network"
quantities: [{"value": "-1.55", "what": "Complex I defect relative to background on acetate", "unit": "", "denominator": "", "scope": "ortholog-transferred Fitness Browser data"}, {"value": "-1.39", "what": "Complex I defect relative to background on succinate", "unit": "", "denominator": "", "scope": "ortholog-transferred Fitness Browser data"}]
caveat: "Ortholog-transferred fitness data mixes signals from multiple Fitness Browser organisms with different respiratory chain architectures, and a direct single-organism Complex I fitness measurement on aromatic substrates would be more definitive."
first_added: "2026-10-27"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# Complex I defects are largest on non-aromatic acetate and succinate

Per-condition analysis reveals that the largest Complex I defects relative to background are on acetate (-1.55) and succinate (-1.39), non-aromatic substrates that also generate high NADH flux through the TCA cycle, qualifying an aromatic-specific interpretation. [src: aromatic_catabolism_network]

## Key figures

- **-1.55**: Complex I defect relative to background on acetate (scope ortholog-transferred Fitness Browser data) [src: aromatic_catabolism_network]
- **-1.39**: Complex I defect relative to background on succinate (scope ortholog-transferred Fitness Browser data) [src: aromatic_catabolism_network]

## Evidence

> However, per-condition analysis reveals that the largest Complex I defects relative to background are on acetate (-1.55) and succinate (-1.39) — non-aromatic substrates that also generate high NADH flux through the TCA cycle. [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

Ortholog-transferred fitness data mixes signals from multiple Fitness Browser organisms with different respiratory chain architectures, and a direct single-organism Complex I fitness measurement on aromatic substrates would be more definitive. [src: aromatic_catabolism_network]

> - Ortholog-transferred fitness data mixes signals from multiple FB organisms with different respiratory chain architectures. Direct Complex I fitness measurements on aromatic substrates in a single organism would be more definitive. [src: aromatic_catabolism_network]

## Other caveats in this report

- NDH-2 compensation is proposed as a likely explanation for ADP1's apparent quinate specificity, not directly established here. [src: aromatic_catabolism_network]
- The report identifies growth-rate optimization and alternative flux routes as reasons the flux balance analysis model may miss a bottleneck. [src: aromatic_catabolism_network]
- The report argues that the model's linear framework misses the threshold effect of disabling a multisubunit Complex I. [src: aromatic_catabolism_network]
- The report interprets cross-species fitness as a high-TCA-flux rather than strictly aromatic Complex I dependency; its NDH-2 explanation remains inferential. [src: aromatic_catabolism_network]
- Co-fitness correlations rely on only eight growth conditions, limiting assignment resolution. [src: aromatic_catabolism_network]
