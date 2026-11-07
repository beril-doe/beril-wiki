---
type: "Finding"
description: "Within all four genome-size quartiles, phaC prevalence was higher in high-variability than low-variability environments: Q1 (0.4\u20131.8 Mbp) 10.7% vs 2.5% (4.4x, p = 1.18 x 10^-11); Q2 (1.8\u20132.5 Mbp) 18.5% vs 4.0% (4.6x, p = 3.25 x 10^-47); Q3 (2.5\u20133.7 Mbp) 34.3% vs 10.9% (3.1x, p = 4.17 x 10^-70); Q4 (3.7\u201314.0 Mbp) 50.9% vs 37.4% (1.4x, p = 3.21 x 10^-14)."
finding_id: "phb_granule_ecology--589de302"
result: "observation"
source: "phb_granule_ecology"
quantities: [{"value": "4.4x", "what": "fold enrichment of phaC+ in high- vs low-variability environments", "unit": "fold", "denominator": "", "scope": "Q1, 0.4\u20131.8 Mbp, 10.7% vs 2.5%"}, {"value": "4.6x", "what": "fold enrichment in Q2", "unit": "fold", "denominator": "", "scope": "Q2, 1.8\u20132.5 Mbp, 18.5% vs 4.0%"}, {"value": "3.1x", "what": "fold enrichment in Q3", "unit": "fold", "denominator": "", "scope": "Q3, 2.5\u20133.7 Mbp, 34.3% vs 10.9%"}, {"value": "1.4x", "what": "fold enrichment in Q4", "unit": "fold", "denominator": "", "scope": "Q4, 3.7\u201314.0 Mbp, 50.9% vs 37.4%"}]
caveat: "Shared ancestry remains a potential confound; phylogenetic logistic regression is proposed as a further test."
first_added: "2026-10-27"
source_hash: "256700c607287ee65c24d87e88b02331582e76de9afbe656fd2ea6cd80350324"
---
# Environmental PHB enrichment persists within every genome-size quartile

Within all four genome-size quartiles, phaC prevalence was higher in high-variability than low-variability environments: Q1 (0.4–1.8 Mbp) 10.7% vs 2.5% (4.4x, p = 1.18 x 10^-11); Q2 (1.8–2.5 Mbp) 18.5% vs 4.0% (4.6x, p = 3.25 x 10^-47); Q3 (2.5–3.7 Mbp) 34.3% vs 10.9% (3.1x, p = 4.17 x 10^-70); Q4 (3.7–14.0 Mbp) 50.9% vs 37.4% (1.4x, p = 3.21 x 10^-14). [src: phb_granule_ecology]

## Key figures

- **4.4x fold**: fold enrichment of phaC+ in high- vs low-variability environments (scope Q1, 0.4–1.8 Mbp, 10.7% vs 2.5%) [src: phb_granule_ecology]
- **4.6x fold**: fold enrichment in Q2 (scope Q2, 1.8–2.5 Mbp, 18.5% vs 4.0%) [src: phb_granule_ecology]
- **3.1x fold**: fold enrichment in Q3 (scope Q3, 2.5–3.7 Mbp, 34.3% vs 10.9%) [src: phb_granule_ecology]
- **1.4x fold**: fold enrichment in Q4 (scope Q4, 3.7–14.0 Mbp, 50.9% vs 37.4%) [src: phb_granule_ecology]

## Evidence

> Critically, however, **the PHB-environment association (H1a) holds robustly within all four genome size quartiles**: | Genome size quartile | Range (Mbp) | High var % phaC+ | Low var % phaC+ | Fold enrichment | p-value | |---------------------|-------------|-------------------|-----------------|-----------------|---------| | Q1 (smallest) | 0.4 – 1.8 | 10.7% | 2.5% | 4.4x | 1.18 x 10^-11 | | Q2 | 1.8 – 2.5 | 18.5% | 4.0% | 4.6x | 3.25 x 10^-47 | | Q3 | 2.5 – 3.7 | 34.3% | 10.9% | 3.1x | 4.17 x 10^-70 | | Q4 (largest) | 3.7 – 14.0 | 50.9% | 37.4% | 1.4x | 3.21 x 10^-14 | [src: phb_granule_ecology]

From the report [[summaries/phb_granule_ecology__REPORT]].

## Caveat

Shared ancestry remains a potential confound; phylogenetic logistic regression is proposed as a further test. [src: phb_granule_ecology]

> phylogenetically controlled analyses (e.g., phylogenetic logistic regression) would further strengthen the findings by accounting for shared ancestry. [src: phb_granule_ecology]

## Other caveats in this report

- The 46.5% precursors-only category is not PHB-specific because phaA (K00626) and phaB (K00023) are pleiotropic; phaR (K18080) was absent from eggNOG annotations for all 27K species, possibly owing to annotation coverage or misassignment. [src: phb_granule_ecology]
- PHB+ genomes were larger (median 4.34 Mbp vs 2.44 Mbp; rank-biserial r = -0.592, p ~ 0), genome size correlated with niche breadth (rho = 0.302, p = 1.5e-43), and adjustment changed the PHB–breadth correlation from rho = 0.106 (p = 1.77e-06) to partial rho = -0.047 (p = 0.037), reported as a 56.3% effect-size reduction with sign reversal. [src: phb_granule_ecology]
- Family-level environmental interpretation is limited by sparse metadata: the other_unknown category covers 30/41 enriched and 26/62 depleted families. [src: phb_granule_ecology]
- Abiotic correlation effect sizes were modest (|rho| < 0.12), and the report notes that NMDC point-in-time abiotic measurements are not direct measurements of temporal variability; depth and temperature interpretations are inferential. [src: phb_granule_ecology]
- PHA synthase class analysis failed to resolve classes: all 11,792 phaC clusters were classified as other_pfam because the eggNOG PFAMs column used domain names (Abhydrolase_1, PhaC_N) rather than expected Pfam accession IDs (PF00561, PF07167). [src: phb_granule_ecology]
