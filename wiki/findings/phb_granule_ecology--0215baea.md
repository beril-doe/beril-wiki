---
type: "Finding"
description: "No PHB was reported for Campylobacterota (0/271), Gemmatimonadota (0/102), Nanoarchaeota (0/135), or Marinisomatota (0/90), and Patescibacteria was near zero at 0.4% (4/981)."
finding_id: "phb_granule_ecology--0215baea"
result: "null result"
source: "phb_granule_ecology"
quantities: [{"value": "0/271", "what": "Campylobacterota species with PHB", "unit": "species", "denominator": "", "scope": ""}, {"value": "0/102", "what": "Gemmatimonadota species with PHB", "unit": "species", "denominator": "", "scope": ""}, {"value": "0/135", "what": "Nanoarchaeota species with PHB", "unit": "species", "denominator": "", "scope": ""}, {"value": "0.4%", "what": "Patescibacteria PHB prevalence", "unit": "% of species", "denominator": "981 species", "scope": ""}]
caveat: "The analyzed genomes include complete genomes and metagenome-assembled genomes, which may have variable gene detection rates."
first_added: "2026-10-27"
source_hash: "256700c607287ee65c24d87e88b02331582e76de9afbe656fd2ea6cd80350324"
---
# Several major phyla have no detected PHB

No PHB was reported for Campylobacterota (0/271), Gemmatimonadota (0/102), Nanoarchaeota (0/135), or Marinisomatota (0/90), and Patescibacteria was near zero at 0.4% (4/981). [src: phb_granule_ecology]

## Key figures

- **0/271 species**: Campylobacterota species with PHB [src: phb_granule_ecology]
- **0/102 species**: Gemmatimonadota species with PHB [src: phb_granule_ecology]
- **0/135 species**: Nanoarchaeota species with PHB [src: phb_granule_ecology]
- **0.4% % of species**: Patescibacteria PHB prevalence (denominator 981 species) [src: phb_granule_ecology]

## Evidence

> Several major phyla are entirely devoid of PHB: Campylobacterota (0/271), Gemmatimonadota (0/102), Nanoarchaeota (0/135), and Marinisomatota (0/90). Patescibacteria is near-zero at 0.4% (4/981), consistent with its reduced genome sizes and limited metabolic capacity. [src: phb_granule_ecology]

From the report [[summaries/phb_granule_ecology__REPORT]].

## Caveat

The analyzed genomes include complete genomes and metagenome-assembled genomes, which may have variable gene detection rates. [src: phb_granule_ecology]

> includes both complete genomes and MAGs, which may have variable gene detection rates. [src: phb_granule_ecology]

## Other caveats in this report

- The 46.5% precursors-only category is not PHB-specific because phaA (K00626) and phaB (K00023) are pleiotropic; phaR (K18080) was absent from eggNOG annotations for all 27K species, possibly owing to annotation coverage or misassignment. [src: phb_granule_ecology]
- PHB+ genomes were larger (median 4.34 Mbp vs 2.44 Mbp; rank-biserial r = -0.592, p ~ 0), genome size correlated with niche breadth (rho = 0.302, p = 1.5e-43), and adjustment changed the PHB–breadth correlation from rho = 0.106 (p = 1.77e-06) to partial rho = -0.047 (p = 0.037), reported as a 56.3% effect-size reduction with sign reversal. [src: phb_granule_ecology]
- Family-level environmental interpretation is limited by sparse metadata: the other_unknown category covers 30/41 enriched and 26/62 depleted families. [src: phb_granule_ecology]
- Abiotic correlation effect sizes were modest (|rho| < 0.12), and the report notes that NMDC point-in-time abiotic measurements are not direct measurements of temporal variability; depth and temperature interpretations are inferential. [src: phb_granule_ecology]
- PHA synthase class analysis failed to resolve classes: all 11,792 phaC clusters were classified as other_pfam because the eggNOG PFAMs column used domain names (Abhydrolase_1, PhaC_N) rather than expected Pfam accession IDs (PF00561, PF07167). [src: phb_granule_ecology]
