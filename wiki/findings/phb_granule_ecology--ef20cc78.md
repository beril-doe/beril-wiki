---
type: "Finding"
description: "The report concludes that the apparent PHB\u2013niche-breadth association (H1b) is substantially confounded by genome size and cannot independently support the feast/famine hypothesis."
finding_id: "phb_granule_ecology--ef20cc78"
result: "null result"
source: "phb_granule_ecology"
quantities: []
caveat: "Adjusting for genome size changed the PHB\u2013breadth correlation from rho = 0.106 (p = 1.77e-06) to partial rho = -0.047 (p = 0.037), a 56.3% effect-size reduction with sign reversal, while PHB+ genomes were larger (median 4.34 Mbp vs 2.44 Mbp)."
first_added: "2026-10-27"
source_hash: "256700c607287ee65c24d87e88b02331582e76de9afbe656fd2ea6cd80350324"
---
# PHB–niche-breadth association is confounded by genome size

The report concludes that the apparent PHB–niche-breadth association (H1b) is substantially confounded by genome size and cannot independently support the feast/famine hypothesis. [src: phb_granule_ecology]

## Evidence

> This means H1b (niche breadth) is substantially confounded by genome size and cannot be interpreted as independent evidence for the feast/famine hypothesis. Larger genomes encode more metabolic pathways generally, and PHB is one of many pathways enriched in larger-genome species. [src: phb_granule_ecology]

From the report [[summaries/phb_granule_ecology__REPORT]].

## Caveat

Adjusting for genome size changed the PHB–breadth correlation from rho = 0.106 (p = 1.77e-06) to partial rho = -0.047 (p = 0.037), a 56.3% effect-size reduction with sign reversal, while PHB+ genomes were larger (median 4.34 Mbp vs 2.44 Mbp). [src: phb_granule_ecology]

> However, PHB+ species also have substantially larger genomes (median 4.34 Mbp vs 2.44 Mbp for PHB-, rank-biserial r = -0.592, p ~ 0), and genome size itself correlates with niche breadth (rho = 0.302, p = 1.5e-43). After controlling for genome size via partial Spearman correlation, **the PHB-niche breadth association largely disappears**: partial rho = **-0.047** (p = 0.037), a **56.3% reduction** in effect size with a sign reversal compared to the raw correlation (rho = 0.106, p = 1.77e-06). [src: phb_granule_ecology]

## Other caveats in this report

- The 46.5% precursors-only category is not PHB-specific because phaA (K00626) and phaB (K00023) are pleiotropic; phaR (K18080) was absent from eggNOG annotations for all 27K species, possibly owing to annotation coverage or misassignment. [src: phb_granule_ecology]
- Family-level environmental interpretation is limited by sparse metadata: the other_unknown category covers 30/41 enriched and 26/62 depleted families. [src: phb_granule_ecology]
- Abiotic correlation effect sizes were modest (|rho| < 0.12), and the report notes that NMDC point-in-time abiotic measurements are not direct measurements of temporal variability; depth and temperature interpretations are inferential. [src: phb_granule_ecology]
- PHA synthase class analysis failed to resolve classes: all 11,792 phaC clusters were classified as other_pfam because the eggNOG PFAMs column used domain names (Abhydrolase_1, PhaC_N) rather than expected Pfam accession IDs (PF00561, PF07167). [src: phb_granule_ecology]
- Environment metadata covered 293,050 genomes spanning all 27,690 species; environment classes were harmonized from NCBI isolation_source, env_broad_scale, env_local_scale, and host fields into 11 categories. [src: phb_granule_ecology]
