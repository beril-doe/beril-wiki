---
type: "Finding"
description: "Partial Spearman correlation reduced the effect from rho = 0.106 (p = 1.77e-06) to rho = -0.047 (p = 0.037) \u2014 a 56.3% reduction with sign reversal, indicating that genome size is the primary driver of the apparent niche breadth association."
finding_id: "phb_granule_ecology--2bce1246"
result: "correction"
source: "phb_granule_ecology"
quantities: [{"value": "0.106", "what": "raw Spearman rho between PHB and niche breadth", "unit": "", "denominator": "", "scope": ""}, {"value": "-0.047", "what": "partial rho after controlling for genome size", "unit": "", "denominator": "", "scope": ""}, {"value": "56.3%", "what": "reduction in effect size", "unit": "%", "denominator": "", "scope": ""}]
caveat: "Only 28% of genomes (83K/293K) have AlphaEarth embeddings, potentially skewing the niche breadth analysis toward better-sampled lineages."
first_added: "2026-11-24"
source_hash: "256700c607287ee65c24d87e88b02331582e76de9afbe656fd2ea6cd80350324"
---
# Genome size, not PHB, explains the apparent niche-breadth association

Partial Spearman correlation reduced the effect from rho = 0.106 (p = 1.77e-06) to rho = -0.047 (p = 0.037) — a 56.3% reduction with sign reversal, indicating that genome size is the primary driver of the apparent niche breadth association. [src: phb_granule_ecology]

## Key figures

- **0.106**: raw Spearman rho between PHB and niche breadth [src: phb_granule_ecology]
- **-0.047**: partial rho after controlling for genome size [src: phb_granule_ecology]
- **56.3%**: reduction in effect size [src: phb_granule_ecology]

## Evidence

> Partial Spearman correlation reduced the effect from rho = 0.106 (p = 1.77e-06) to rho = -0.047 (p = 0.037) — a 56.3% reduction with sign reversal, indicating that genome size is the primary driver of the apparent niche breadth association. [src: phb_granule_ecology]

From the report [[summaries/phb_granule_ecology__REPORT]].

## Caveat

Only 28% of genomes (83K/293K) have AlphaEarth embeddings, potentially skewing the niche breadth analysis toward better-sampled lineages. [src: phb_granule_ecology]

> 4. **AlphaEarth coverage bias**: Only 28% of genomes (83K/293K) have AlphaEarth embeddings, potentially skewing the niche breadth analysis toward better-sampled lineages. [src: phb_granule_ecology]

## Other caveats in this report

- The report attributes the 46.5% precursors-only category to pleiotropic phaA and phaB functions beyond PHB synthesis. [src: phb_granule_ecology]
- The report concludes that H1b, the PHB–niche breadth association, is substantially confounded by genome size and cannot independently support the feast/famine hypothesis. [src: phb_granule_ecology]
- Interpretation of PHB family environmental patterns is limited by the dominant "other_unknown" category (30/41 enriched, 26/62 depleted), reflecting sparse species environmental metadata. [src: phb_granule_ecology]
- NMDC abiotic correlations had modest effect sizes (|rho| < 0.12), likely because measurements were point-in-time snapshots rather than measures of temporal variability. [src: phb_granule_ecology]
- PHA synthase class analysis assigned all 11,792 phaC clusters to other_pfam because eggNOG supplied domain names Abhydrolase_1 and PhaC_N rather than the expected Pfam accession IDs PF00561 and PF07167. [src: phb_granule_ecology]
