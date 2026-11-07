---
type: "Finding"
description: "Across 27,690 species with classified primary environments, phaC prevalence was plant-associated 44.0% (625 species), soil 43.6% (1,484), wastewater/engineered 34.5% (1,124), freshwater 25.5% (3,263), sediment 20.1% (1,020), marine 18.7% (3,010), human associated 11.1% (1,237), human clinical 7.4% (2,472), and animal associated 3.3% (3,711)."
finding_id: "phb_granule_ecology--5e2bc604"
result: "observation"
source: "phb_granule_ecology"
quantities: [{"value": "44.0%", "what": "phaC prevalence in plant-associated species", "unit": "% of species", "denominator": "625 species", "scope": "GTDB species with classified primary environment"}, {"value": "43.6%", "what": "phaC prevalence in soil species", "unit": "% of species", "denominator": "1,484 species", "scope": "GTDB species with classified primary environment"}, {"value": "7.4%", "what": "phaC prevalence in human clinical species", "unit": "% of species", "denominator": "2,472 species", "scope": "GTDB species with classified primary environment"}, {"value": "3.3%", "what": "phaC prevalence in animal-associated species", "unit": "% of species", "denominator": "3,711 species", "scope": "GTDB species with classified primary environment"}]
caveat: "For 34.9% of species, the primary environment is other_unknown."
first_added: "2026-10-27"
source_hash: "256700c607287ee65c24d87e88b02331582e76de9afbe656fd2ea6cd80350324"
---
# phaC prevalence falls steeply from plant and soil to animal-associated species

Across 27,690 species with classified primary environments, phaC prevalence was plant-associated 44.0% (625 species), soil 43.6% (1,484), wastewater/engineered 34.5% (1,124), freshwater 25.5% (3,263), sediment 20.1% (1,020), marine 18.7% (3,010), human associated 11.1% (1,237), human clinical 7.4% (2,472), and animal associated 3.3% (3,711). [src: phb_granule_ecology]

## Key figures

- **44.0% % of species**: phaC prevalence in plant-associated species (denominator 625 species; scope GTDB species with classified primary environment) [src: phb_granule_ecology]
- **43.6% % of species**: phaC prevalence in soil species (denominator 1,484 species; scope GTDB species with classified primary environment) [src: phb_granule_ecology]
- **7.4% % of species**: phaC prevalence in human clinical species (denominator 2,472 species; scope GTDB species with classified primary environment) [src: phb_granule_ecology]
- **3.3% % of species**: phaC prevalence in animal-associated species (denominator 3,711 species; scope GTDB species with classified primary environment) [src: phb_granule_ecology]

## Evidence

> PHB prevalence varies dramatically by environment type across 27,690 species with classified primary environments: | Environment | n species | % phaC | Expected variability | |-------------|-----------|--------|---------------------| | Plant-associated | 625 | 44.0% | High | | Soil | 1,484 | 43.6% | High | | Wastewater/engineered | 1,124 | 34.5% | High | | Freshwater | 3,263 | 25.5% | Moderate | | Sediment | 1,020 | 20.1% | Moderate | | Marine | 3,010 | 18.7% | Low | | Human associated | 1,237 | 11.1% | Low | | Human clinical | 2,472 | 7.4% | Low | | Animal associated | 3,711 | 3.3% | Low | [src: phb_granule_ecology]

From the report [[summaries/phb_granule_ecology__REPORT]].

## Caveat

For 34.9% of species, the primary environment is other_unknown. [src: phb_granule_ecology]

> 34.9% of species have "other_unknown" as primary environment. [src: phb_granule_ecology]

## Other caveats in this report

- The 46.5% precursors-only category is not PHB-specific because phaA (K00626) and phaB (K00023) are pleiotropic; phaR (K18080) was absent from eggNOG annotations for all 27K species, possibly owing to annotation coverage or misassignment. [src: phb_granule_ecology]
- PHB+ genomes were larger (median 4.34 Mbp vs 2.44 Mbp; rank-biserial r = -0.592, p ~ 0), genome size correlated with niche breadth (rho = 0.302, p = 1.5e-43), and adjustment changed the PHB–breadth correlation from rho = 0.106 (p = 1.77e-06) to partial rho = -0.047 (p = 0.037), reported as a 56.3% effect-size reduction with sign reversal. [src: phb_granule_ecology]
- Family-level environmental interpretation is limited by sparse metadata: the other_unknown category covers 30/41 enriched and 26/62 depleted families. [src: phb_granule_ecology]
- Abiotic correlation effect sizes were modest (|rho| < 0.12), and the report notes that NMDC point-in-time abiotic measurements are not direct measurements of temporal variability; depth and temperature interpretations are inferential. [src: phb_granule_ecology]
- PHA synthase class analysis failed to resolve classes: all 11,792 phaC clusters were classified as other_pfam because the eggNOG PFAMs column used domain names (Abhydrolase_1, PhaC_N) rather than expected Pfam accession IDs (PF00561, PF07167). [src: phb_granule_ecology]
