---
type: "Finding"
description: "Taxonomy-based inference of prophage burden across 6,365 NMDC metagenomic samples (87.2% median matching coverage) yielded 57 significant module-abiotic correlations at FDR < 0.05."
finding_id: "prophage_ecology--967ce72a"
result: "inference"
source: "prophage_ecology"
quantities: [{"value": "6,365", "what": "NMDC metagenomic samples analyzed", "unit": "samples", "denominator": "", "scope": ""}, {"value": "87.2%", "what": "median matching coverage of taxonomy-based inference", "unit": "", "denominator": "", "scope": "NMDC samples"}, {"value": "57", "what": "significant module-abiotic correlations", "unit": "correlations", "denominator": "", "scope": "FDR < 0.05"}]
caveat: "Taxonomy-based inference assumes genus-level conservation of prophage content, which may not hold for recently acquired or lost prophages, and the approach has not been independently validated for prophage genes."
first_added: "2026-11-09"
source_hash: "58e5dfbe672d830cc749b46434bc92ecb328e31d5cb5f793a987c72994a7e0ed"
---
# Inferred prophage burden correlates with abiotic variables across NMDC metagenomes

Taxonomy-based inference of prophage burden across 6,365 NMDC metagenomic samples (87.2% median matching coverage) yielded 57 significant module-abiotic correlations at FDR < 0.05. [src: prophage_ecology]

## Key figures

- **6,365 samples**: NMDC metagenomic samples analyzed [src: prophage_ecology]
- **87.2%**: median matching coverage of taxonomy-based inference (scope NMDC samples) [src: prophage_ecology]
- **57 correlations**: significant module-abiotic correlations (scope FDR < 0.05) [src: prophage_ecology]

## Evidence

> Taxonomy-based inference of prophage burden across 6,365 NMDC metagenomic samples (87.2% median matching coverage) reveals 57 significant module-abiotic correlations (FDR < 0.05). The strongest correlations: [src: prophage_ecology]

From the report [[summaries/prophage_ecology__REPORT]].

## Caveat

Taxonomy-based inference assumes genus-level conservation of prophage content, which may not hold for recently acquired or lost prophages, and the approach has not been independently validated for prophage genes. [src: prophage_ecology]

> 4. **NMDC inference is indirect**: Taxonomy-based prophage burden inference assumes genus-level conservation of prophage content, which may not hold for recently acquired or lost prophages. This approach was validated for the PHB granule ecology project but has not been independently validated for prophage genes. [src: prophage_ecology]

## Other caveats in this report

- The authors caution that near-universal modules may include domesticated, defective prophage remnants; head, tail, and anti-defense may better indicate more complete elements. [src: prophage_ecology]
- Packaging, lysis, integration, and lysogenic regulation were NMDC-significant but not pangenome-enriched beyond phylogenetic expectation; masking by near-universal prevalence is the authors’ interpretation. [src: prophage_ecology]
- Metagenomic prophage burden was inferred from genus-level pangenome scores through GTDB metadata and genus matching, rather than directly measured in the NMDC samples. [src: prophage_ecology]
- The report proposes, but does not directly test, a pH-sensitive lysogeny explanation for the positive pH correlations (rho=0.519 for packaging; 0.474 overall). [src: prophage_ecology]
- The co-occurrence results support the module definitions for the core backbone—packaging, lysis, and lysogenic regulation—less strongly for the accessory integration and anti-defense functions. [src: prophage_ecology]
