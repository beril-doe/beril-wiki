---
type: "Finding"
description: "At phylum rank the natural_expansion class has producer z mean +0.55 \u03c3, with 95% CI [0.43, 0.67] and n = 457."
finding_id: "gene_function_ecological_agora--804b4e91"
result: "observation"
source: "gene_function_ecological_agora"
quantities: [{"value": "+0.55 \u03c3", "what": "producer z mean at phylum rank", "unit": "\u03c3", "denominator": "", "scope": "natural_expansion class"}, {"value": "[0.43, 0.67]", "what": "95% CI at phylum rank", "unit": "", "denominator": "", "scope": ""}, {"value": "457", "what": "n at phylum rank", "unit": "", "denominator": "", "scope": ""}]
caveat: "The natural_expansion validation is circular because it is selected for paralog count \u2265 3 and tested against a null designed to detect paralog expansion."
first_added: "2026-11-24"
source_hash: "ec22f37a485c95d0e067c1984020af5580f9f103cae1582742ed63f035a74a69"
---
# Paralog-expansion positive control signal grows with taxonomic rank

At phylum rank the natural_expansion class has producer z mean +0.55 σ, with 95% CI [0.43, 0.67] and n = 457. [src: gene_function_ecological_agora]

## Key figures

- **+0.55 σ**: producer z mean at phylum rank (scope natural_expansion class) [src: gene_function_ecological_agora]
- **[0.43, 0.67]**: 95% CI at phylum rank [src: gene_function_ecological_agora]
- **457**: n at phylum rank [src: gene_function_ecological_agora]

## Evidence

> | Rank | Producer z mean | 95% CI | n | |---|---|---|---| | genus | +0.13 σ | [0.08, 0.18] | 975 | | family | +0.19 σ | [0.13, 0.26] | 802 | | order | +0.31 σ | [0.22, 0.39] | 654 | | class | +0.50 σ | [0.38, 0.61] | 482 | | phylum | +0.55 σ | [0.43, 0.67] | 457 | [src: gene_function_ecological_agora]

From the report [[summaries/gene_function_ecological_agora__REPORT]].

## Caveat

The natural_expansion validation is circular because it is selected for paralog count ≥ 3 and tested against a null designed to detect paralog expansion. [src: gene_function_ecological_agora]

> natural_expansion is selected for paralog count ≥ 3 and tested against a null designed to detect paralog expansion. [src: gene_function_ecological_agora]

## Other caveats in this report

- The report rejects the reviewer's revision-count family-wise-error framing because M1–M26 are pre-registration corrections, not 26 alternative tests. [src: gene_function_ecological_agora]
- The Cyanobacteria PSII table describes BacDive coverage as thin (n=4). [src: gene_function_ecological_agora]
- The synthesis narrows the mycolic-acid innovation claim to Mycobacteriaceae sub-clades such as M. tuberculosis / M. leprae complexes, treating family-rank d=0.31 as a population-mixture average. [src: gene_function_ecological_agora]
- The NB08c diagnostic identified parent-rank dispersion permutation null as the wrong metric, replaced by Sankoff parsimony with recipient-rank gain attribution. [src: gene_function_ecological_agora]
- The report regards class rank as biologically appropriate for PSII per Cardona 2018 because PSII evolved before Cyanobacteria diversification, making the genus null expected. [src: gene_function_ecological_agora]
