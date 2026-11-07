---
type: "Finding"
description: "Among the 311 discordant phaC-positive species, 60.1% carry phaC as accessory genome versus 32.3% across all phaC-carrying species, which the report says supports horizontal acquisition."
finding_id: "phb_granule_ecology--f9008fe7"
result: "inference"
source: "phb_granule_ecology"
quantities: [{"value": "60.1%", "what": "discordant phaC-positive species carrying phaC as accessory genome", "unit": "% of species", "denominator": "311 discordant phaC-positive species", "scope": ""}, {"value": "32.3%", "what": "accessory rate across all phaC-carrying species", "unit": "%", "denominator": "", "scope": "all phaC-carrying species"}]
caveat: "Core is defined as a gene cluster present in >90% of genomes within a species, and the elevated accessory rate is indirect pangenome-scale evidence for horizontal transfer, not direct proof."
first_added: "2026-10-27"
source_hash: "256700c607287ee65c24d87e88b02331582e76de9afbe656fd2ea6cd80350324"
---
# Phylogenetically discordant phaC carriers are enriched for accessory-genome phaC

Among the 311 discordant phaC-positive species, 60.1% carry phaC as accessory genome versus 32.3% across all phaC-carrying species, which the report says supports horizontal acquisition. [src: phb_granule_ecology]

## Key figures

- **60.1% % of species**: discordant phaC-positive species carrying phaC as accessory genome (denominator 311 discordant phaC-positive species) [src: phb_granule_ecology]
- **32.3%**: accessory rate across all phaC-carrying species (scope all phaC-carrying species) [src: phb_granule_ecology]

## Evidence

> Among the 311 discordant phaC-positive species, **60.1% carry phaC as accessory genome** (not present in all strains), compared to 32.3% accessory rate across all phaC-carrying species — nearly double. This strongly supports horizontal acquisition: recently transferred genes have not yet been fixed in the core genome. [src: phb_granule_ecology]

From the report [[summaries/phb_granule_ecology__REPORT]].

## Caveat

Core is defined as a gene cluster present in >90% of genomes within a species, and the elevated accessory rate is indirect pangenome-scale evidence for horizontal transfer, not direct proof. [src: phb_granule_ecology]

> The HGT analysis leveraged core/accessory classification from the pangenome: a gene cluster present in >90% of genomes within a species is "core," otherwise "accessory." The significantly elevated accessory rate in phylogenetically discordant species (60.1% vs 32.3%) provides pangenome-scale evidence for ongoing horizontal transfer of phaC, consistent with earlier single-species case studies (Kalia et al. 2007; Catone et al. 2014). [src: phb_granule_ecology]

## Other caveats in this report

- The 46.5% precursors-only category is not PHB-specific because phaA (K00626) and phaB (K00023) are pleiotropic; phaR (K18080) was absent from eggNOG annotations for all 27K species, possibly owing to annotation coverage or misassignment. [src: phb_granule_ecology]
- PHB+ genomes were larger (median 4.34 Mbp vs 2.44 Mbp; rank-biserial r = -0.592, p ~ 0), genome size correlated with niche breadth (rho = 0.302, p = 1.5e-43), and adjustment changed the PHB–breadth correlation from rho = 0.106 (p = 1.77e-06) to partial rho = -0.047 (p = 0.037), reported as a 56.3% effect-size reduction with sign reversal. [src: phb_granule_ecology]
- Family-level environmental interpretation is limited by sparse metadata: the other_unknown category covers 30/41 enriched and 26/62 depleted families. [src: phb_granule_ecology]
- Abiotic correlation effect sizes were modest (|rho| < 0.12), and the report notes that NMDC point-in-time abiotic measurements are not direct measurements of temporal variability; depth and temperature interpretations are inferential. [src: phb_granule_ecology]
- PHA synthase class analysis failed to resolve classes: all 11,792 phaC clusters were classified as other_pfam because the eggNOG PFAMs column used domain names (Abhydrolase_1, PhaC_N) rather than expected Pfam accession IDs (PF00561, PF07167). [src: phb_granule_ecology]
