---
type: "Finding"
description: "In the reported PERMANOVA of prophage module composition, the F-statistics were 212.99 for genome size quartile, 30.04 for environment and 6.17 for family-level phylogeny, each with p=0.01."
finding_id: "prophage_ecology--9f2125cc"
result: "observation"
source: "prophage_ecology"
quantities: [{"value": "212.99", "what": "PERMANOVA F-statistic for genome size quartile", "unit": "", "denominator": "", "scope": "p=0.01"}, {"value": "30.04", "what": "PERMANOVA F-statistic for environment", "unit": "", "denominator": "", "scope": "p=0.01"}, {"value": "6.17", "what": "PERMANOVA F-statistic for phylogeny (family)", "unit": "", "denominator": "", "scope": "p=0.01"}]
caveat: "Each predictor was tested independently; partial PERMANOVA to quantify the unique variance explained by environment after controlling for phylogeny and genome size simultaneously had not been implemented."
first_added: "2026-11-09"
source_hash: "58e5dfbe672d830cc749b46434bc92ecb328e31d5cb5f793a987c72994a7e0ed"
---
# Genome size dwarfs environment and phylogeny as predictor of prophage module composition

In the reported PERMANOVA of prophage module composition, the F-statistics were 212.99 for genome size quartile, 30.04 for environment and 6.17 for family-level phylogeny, each with p=0.01. [src: prophage_ecology]

## Key figures

- **212.99**: PERMANOVA F-statistic for genome size quartile (scope p=0.01) [src: prophage_ecology]
- **30.04**: PERMANOVA F-statistic for environment (scope p=0.01) [src: prophage_ecology]
- **6.17**: PERMANOVA F-statistic for phylogeny (family) (scope p=0.01) [src: prophage_ecology]

## Evidence

> | Genome size quartile | **212.99** | 0.01 | 4 | | Environment | **30.04** | 0.01 | 10 | | Phylogeny (family) | **6.17** | 0.01 | 294 | [src: prophage_ecology]

From the report [[summaries/prophage_ecology__REPORT]].

## Caveat

Each predictor was tested independently; partial PERMANOVA to quantify the unique variance explained by environment after controlling for phylogeny and genome size simultaneously had not been implemented. [src: prophage_ecology]

> 2. **Partial PERMANOVA**: Implement sequential/partial PERMANOVA to formally quantify the unique variance explained by environment after controlling for phylogeny and genome size simultaneously, rather than testing each predictor independently. [src: prophage_ecology]

## Other caveats in this report

- The authors caution that near-universal modules may include domesticated, defective prophage remnants; head, tail, and anti-defense may better indicate more complete elements. [src: prophage_ecology]
- Packaging, lysis, integration, and lysogenic regulation were NMDC-significant but not pangenome-enriched beyond phylogenetic expectation; masking by near-universal prevalence is the authors’ interpretation. [src: prophage_ecology]
- Metagenomic prophage burden was inferred from genus-level pangenome scores through GTDB metadata and genus matching, rather than directly measured in the NMDC samples. [src: prophage_ecology]
- The report proposes, but does not directly test, a pH-sensitive lysogeny explanation for the positive pH correlations (rho=0.519 for packaging; 0.474 overall). [src: prophage_ecology]
- The co-occurrence results support the module definitions for the core backbone—packaging, lysis, and lysogenic regulation—less strongly for the accessory integration and anti-defense functions. [src: prophage_ecology]
