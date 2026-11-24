---
type: "Finding"
description: "SHAP features are mechanistically coherent (ribose transporter predicts ribose growth, protocatechuate cycloisomerase predicts aromatic catabolism) but weakly concordant with Fitness Browser (1.19\u00d7 enrichment)."
finding_id: "genotype_to_phenotype_enigma--c8d74adf"
result: "observation"
source: "genotype_to_phenotype_enigma"
quantities: [{"value": "1.19\u00d7", "what": "Fitness Browser concordance enrichment", "unit": "", "denominator": "", "scope": ""}]
caveat: "This is a weak positive: the model's features are barely more fitness-significant than random genes under matched conditions."
first_added: "2026-11-24"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# SHAP features are coherent but only weakly concordant with Fitness Browser

SHAP features are mechanistically coherent (ribose transporter predicts ribose growth, protocatechuate cycloisomerase predicts aromatic catabolism) but weakly concordant with Fitness Browser (1.19× enrichment). [src: genotype_to_phenotype_enigma]

## Key figures

- **1.19×**: Fitness Browser concordance enrichment [src: genotype_to_phenotype_enigma]

## Evidence

> **SHAP features are mechanistically coherent** (ribose transporter predicts ribose growth, protocatechuate cycloisomerase predicts aromatic catabolism) but weakly concordant with Fitness Browser (1.19× enrichment) because gene presence across genera and gene essentiality within one strain are different biological questions. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

This is a weak positive: the model's features are barely more fitness-significant than random genes under matched conditions. [src: genotype_to_phenotype_enigma]

> This is a weak positive: the model's features are barely more fitness-significant than random genes under matched conditions. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- The bacterial growth model's SHAP features are weakly concordant with Fitness Browser (1.19× enrichment), because gene presence across genera and gene essentiality within one strain address different biological questions. [src: genotype_to_phenotype_enigma]
- Transfer learning from clinical phenotype databases may be biased for ENIGMA subsurface field isolates. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains to the KBase Data Lakehouse pangenome through ncbi_strain_identifiers caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The ENIGMA short strain name MT20, representing Rhodanobacter glycinis, matched unrelated Streptococcus pneumoniae, with name collisions injecting 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma]
- The report documents the strain-name collision pitfall in docs/pitfalls.md and says it affects any project linking ENIGMA strains to the pangenome by name. [src: genotype_to_phenotype_enigma]
