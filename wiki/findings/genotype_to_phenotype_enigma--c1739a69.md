---
type: "Finding"
description: "Binary bacterial growth on metals, antibiotics, or nitrogen is not predictable from KO content alone."
finding_id: "genotype_to_phenotype_enigma--c1739a69"
result: "null result"
source: "genotype_to_phenotype_enigma"
quantities: []
caveat: "In the full ENIGMA/CSP model, metals have AUC 0.605 across 232 pairs but are trivially predicted because of a 98% growth rate."
first_added: "2026-11-24"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Metals, antibiotics and nitrogen growth not predictable from KO content

Binary bacterial growth on metals, antibiotics, or nitrogen is not predictable from KO content alone. [src: genotype_to_phenotype_enigma]

## Evidence

> **not predictable** on metals, antibiotics, or nitrogen from KO content alone. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

In the full ENIGMA/CSP model, metals have AUC 0.605 across 232 pairs but are trivially predicted because of a 98% growth rate. [src: genotype_to_phenotype_enigma]

> | Metals | 0.605 | 232 | Trivially "predicted" (98% growth rate) | [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- The bacterial growth model's SHAP features are weakly concordant with Fitness Browser (1.19× enrichment), because gene presence across genera and gene essentiality within one strain address different biological questions. [src: genotype_to_phenotype_enigma]
- Transfer learning from clinical phenotype databases may be biased for ENIGMA subsurface field isolates. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains to the KBase Data Lakehouse pangenome through ncbi_strain_identifiers caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The ENIGMA short strain name MT20, representing Rhodanobacter glycinis, matched unrelated Streptococcus pneumoniae, with name collisions injecting 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma]
- The report documents the strain-name collision pitfall in docs/pitfalls.md and says it affects any project linking ENIGMA strains to the pangenome by name. [src: genotype_to_phenotype_enigma]
