---
type: "Finding"
description: "All 27,702 species in the pangenome carry prophage-associated gene clusters (4,005,537 in total, identified via eggNOG annotations); packaging (100%), lysis (99.9%) and lysogenic regulation (100%) are near-universal, while head morphogenesis (56.1%), tail (55.6%) and anti-defense (64.3%) are structurally variable, and 34.9% of species carry all 7 modules."
finding_id: "prophage_ecology--d880eadf"
result: "observation"
source: "prophage_ecology"
quantities: [{"value": "27,702", "what": "species carrying prophage-associated gene clusters", "unit": "species", "denominator": "", "scope": "pangenome species surveyed"}, {"value": "4,005,537", "what": "total prophage gene clusters identified via eggNOG annotations", "unit": "gene clusters", "denominator": "", "scope": ""}, {"value": "56.1%", "what": "prevalence of head morphogenesis module (B)", "unit": "", "denominator": "species", "scope": ""}, {"value": "34.9%", "what": "species carrying all 7 modules", "unit": "", "denominator": "species", "scope": ""}]
caveat: "The all-species result is not an intact-prophage prevalence estimate, since individual prophage-associated gene clusters, including domesticated remnants, were counted, which likely explains why it far exceeds Touchon et al.'s (2016) estimate that ~46% of bacterial genomes harbor prophages."
first_added: "2026-11-09"
source_hash: "58e5dfbe672d830cc749b46434bc92ecb328e31d5cb5f793a987c72994a7e0ed"
---
# Prophage-associated gene clusters occur in every surveyed species, with modules varying

All 27,702 species in the pangenome carry prophage-associated gene clusters (4,005,537 in total, identified via eggNOG annotations); packaging (100%), lysis (99.9%) and lysogenic regulation (100%) are near-universal, while head morphogenesis (56.1%), tail (55.6%) and anti-defense (64.3%) are structurally variable, and 34.9% of species carry all 7 modules. [src: prophage_ecology]

## Key figures

- **27,702 species**: species carrying prophage-associated gene clusters (scope pangenome species surveyed) [src: prophage_ecology]
- **4,005,537 gene clusters**: total prophage gene clusters identified via eggNOG annotations [src: prophage_ecology]
- **56.1%**: prevalence of head morphogenesis module (B) (denominator species) [src: prophage_ecology]
- **34.9%**: species carrying all 7 modules (denominator species) [src: prophage_ecology]

## Evidence

> All 27,702 species in the BERDL pangenome carry prophage-associated gene clusters, with 4,005,537 total prophage gene clusters identified via eggNOG annotations. Three modules are near-universal: packaging (A, 100%), lysis (D, 99.9%), and lysogenic regulation (F, 100%). The structurally variable modules — head morphogenesis (B, 56.1%), tail (C, 55.6%), and anti-defense (G, 64.3%) — show the most phylogenetic and environmental variation. 34.9% of species carry all 7 modules. [src: prophage_ecology]

From the report [[summaries/prophage_ecology__REPORT]].

## Caveat

The all-species result is not an intact-prophage prevalence estimate, since individual prophage-associated gene clusters, including domesticated remnants, were counted, which likely explains why it far exceeds Touchon et al.'s (2016) estimate that ~46% of bacterial genomes harbor prophages. [src: prophage_ecology]

> The finding that **all 27,702 species carry prophage annotations** far exceeds Touchon et al.'s (2016) estimate that ~46% of bacterial genomes harbor prophages. This discrepancy likely reflects our broader definition: we identify individual prophage-associated gene clusters (including domesticated remnants), not intact prophages. [src: prophage_ecology]

## Other caveats in this report

- The authors caution that near-universal modules may include domesticated, defective prophage remnants; head, tail, and anti-defense may better indicate more complete elements. [src: prophage_ecology]
- Packaging, lysis, integration, and lysogenic regulation were NMDC-significant but not pangenome-enriched beyond phylogenetic expectation; masking by near-universal prevalence is the authors’ interpretation. [src: prophage_ecology]
- Metagenomic prophage burden was inferred from genus-level pangenome scores through GTDB metadata and genus matching, rather than directly measured in the NMDC samples. [src: prophage_ecology]
- The report proposes, but does not directly test, a pH-sensitive lysogeny explanation for the positive pH correlations (rho=0.519 for packaging; 0.474 overall). [src: prophage_ecology]
- The co-occurrence results support the module definitions for the core backbone—packaging, lysis, and lysogenic regulation—less strongly for the accessory integration and anti-defense functions. [src: prophage_ecology]
