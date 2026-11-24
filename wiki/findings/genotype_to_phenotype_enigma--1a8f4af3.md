---
type: "Finding"
description: "Worldwide, the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9\u00b0C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster."
finding_id: "genotype_to_phenotype_enigma--1a8f4af3"
result: "observation"
source: "genotype_to_phenotype_enigma"
quantities: [{"value": "1.35", "what": "pH units more acidic", "unit": "pH units", "denominator": "", "scope": "worldwide"}, {"value": "6.9\u00b0C", "what": "warmer", "unit": "\u00b0C", "denominator": "", "scope": "worldwide"}]
caveat: "Spearman co-occurrence suggests shared/exclusive niches but does not prove direct interaction."
first_added: "2026-11-24"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Oak Ridge co-occurrence clusters separate along a global pH gradient

Worldwide, the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9°C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster. [src: genotype_to_phenotype_enigma]

## Key figures

- **1.35 pH units**: pH units more acidic (scope worldwide) [src: genotype_to_phenotype_enigma]
- **6.9°C °C**: warmer (scope worldwide) [src: genotype_to_phenotype_enigma]

## Evidence

> the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9°C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster worldwide. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

Spearman co-occurrence suggests shared/exclusive niches but does not prove direct interaction. [src: genotype_to_phenotype_enigma]

> **Co-occurrence is correlation, not causation**: Spearman co-occurrence suggests shared/exclusive niches but does not prove direct interaction. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- The bacterial growth model's SHAP features are weakly concordant with Fitness Browser (1.19× enrichment), because gene presence across genera and gene essentiality within one strain address different biological questions. [src: genotype_to_phenotype_enigma]
- Transfer learning from clinical phenotype databases may be biased for ENIGMA subsurface field isolates. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains to the KBase Data Lakehouse pangenome through ncbi_strain_identifiers caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The ENIGMA short strain name MT20, representing Rhodanobacter glycinis, matched unrelated Streptococcus pneumoniae, with name collisions injecting 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma]
- The report documents the strain-name collision pitfall in docs/pitfalls.md and says it affects any project linking ENIGMA strains to the pangenome by name. [src: genotype_to_phenotype_enigma]
