---
type: "Finding"
description: "Reported phaC prevalence varies by phylum: Pseudomonadota 60.9% (4,544/7,456), Myxococcota 52.9% (83/157), Halobacteriota 34.4% (89/259), Thermoproteota 27.9% (65/233), Desulfobacterota 21.9% (70/319), and Actinomycetota 18.5% (587/3,172)."
finding_id: "phb_granule_ecology--1de7b86b"
result: "observation"
source: "phb_granule_ecology"
quantities: [{"value": "60.9%", "what": "phaC prevalence in Pseudomonadota", "unit": "% of species", "denominator": "7,456 species", "scope": ""}, {"value": "52.9%", "what": "phaC prevalence in Myxococcota", "unit": "% of species", "denominator": "157 species", "scope": ""}, {"value": "34.4%", "what": "phaC prevalence in Halobacteriota", "unit": "% of species", "denominator": "259 species", "scope": ""}, {"value": "18.5%", "what": "phaC prevalence in Actinomycetota", "unit": "% of species", "denominator": "3,172 species", "scope": ""}]
caveat: "The report's statement that five phyla account for 85.5% of the 6,067 phaC-carrying species is internally inconsistent with its own phylum-level counts, and this numerical contradiction remains unresolved."
first_added: "2026-10-27"
source_hash: "256700c607287ee65c24d87e88b02331582e76de9afbe656fd2ea6cd80350324"
---
# phaC is concentrated in Pseudomonadota, with wide variation among phyla

Reported phaC prevalence varies by phylum: Pseudomonadota 60.9% (4,544/7,456), Myxococcota 52.9% (83/157), Halobacteriota 34.4% (89/259), Thermoproteota 27.9% (65/233), Desulfobacterota 21.9% (70/319), and Actinomycetota 18.5% (587/3,172). [src: phb_granule_ecology]

## Key figures

- **60.9% % of species**: phaC prevalence in Pseudomonadota (denominator 7,456 species) [src: phb_granule_ecology]
- **52.9% % of species**: phaC prevalence in Myxococcota (denominator 157 species) [src: phb_granule_ecology]
- **34.4% % of species**: phaC prevalence in Halobacteriota (denominator 259 species) [src: phb_granule_ecology]
- **18.5% % of species**: phaC prevalence in Actinomycetota (denominator 3,172 species) [src: phb_granule_ecology]

## Evidence

> - **Pseudomonadota** dominates with 60.9% prevalence (4,544/7,456 species) - **Myxococcota**: 52.9% (83/157) - **Halobacteriota**: 34.4% (89/259) - **Thermoproteota**: 27.9% (65/233) - **Desulfobacterota**: 21.9% (70/319) - **Actinomycetota**: 18.5% (587/3,172) [src: phb_granule_ecology]

From the report [[summaries/phb_granule_ecology__REPORT]].

## Caveat

The report's statement that five phyla account for 85.5% of the 6,067 phaC-carrying species is internally inconsistent with its own phylum-level counts, and this numerical contradiction remains unresolved. [src: phb_granule_ecology]

> The 6,067 phaC-carrying species span 95 of 142 GTDB phyla but are concentrated in a few lineages. Pseudomonadota alone accounts for 74.9% of all phaC-carrying species (4,544/6,067), driven by high prevalence across Alpha- and Gammaproteobacteria orders. The five most PHB-enriched phyla (Pseudomonadota, Myxococcota, Halobacteriota, Thermoproteota, Desulfobacterota) together account for 85.5% of phaC+ species despite comprising only 30.4% of total species diversity. [src: phb_granule_ecology]

## Other caveats in this report

- The 46.5% precursors-only category is not PHB-specific because phaA (K00626) and phaB (K00023) are pleiotropic; phaR (K18080) was absent from eggNOG annotations for all 27K species, possibly owing to annotation coverage or misassignment. [src: phb_granule_ecology]
- PHB+ genomes were larger (median 4.34 Mbp vs 2.44 Mbp; rank-biserial r = -0.592, p ~ 0), genome size correlated with niche breadth (rho = 0.302, p = 1.5e-43), and adjustment changed the PHB–breadth correlation from rho = 0.106 (p = 1.77e-06) to partial rho = -0.047 (p = 0.037), reported as a 56.3% effect-size reduction with sign reversal. [src: phb_granule_ecology]
- Family-level environmental interpretation is limited by sparse metadata: the other_unknown category covers 30/41 enriched and 26/62 depleted families. [src: phb_granule_ecology]
- Abiotic correlation effect sizes were modest (|rho| < 0.12), and the report notes that NMDC point-in-time abiotic measurements are not direct measurements of temporal variability; depth and temperature interpretations are inferential. [src: phb_granule_ecology]
- PHA synthase class analysis failed to resolve classes: all 11,792 phaC clusters were classified as other_pfam because the eggNOG PFAMs column used domain names (Abhydrolase_1, PhaC_N) rather than expected Pfam accession IDs (PF00561, PF07167). [src: phb_granule_ecology]
