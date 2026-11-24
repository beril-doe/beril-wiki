---
type: "Finding"
description: "Binary bacterial growth from KO presence/absence is predictable on amino acids (AUC 0.775, tryptophan 0.933) and nucleosides (0.780), and moderately on carbon sources (0.695)."
finding_id: "genotype_to_phenotype_enigma--fa81ccd3"
result: "observation"
source: "genotype_to_phenotype_enigma"
quantities: [{"value": "0.775", "what": "AUC for binary growth on amino acids", "unit": "AUC", "denominator": "", "scope": "KO presence/absence"}, {"value": "0.933", "what": "AUC for tryptophan", "unit": "AUC", "denominator": "", "scope": ""}, {"value": "0.780", "what": "AUC on nucleosides", "unit": "AUC", "denominator": "", "scope": ""}, {"value": "0.695", "what": "AUC on carbon sources", "unit": "AUC", "denominator": "", "scope": ""}]
caveat: "~76% of ENIGMA conditions (metals, antibiotics, nitrogen, stress) have neither GapMind pathway coverage nor CSP training data."
first_added: "2026-11-24"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Binary growth is predictable from KO content on amino acids and nucleosides

Binary bacterial growth from KO presence/absence is predictable on amino acids (AUC 0.775, tryptophan 0.933) and nucleosides (0.780), and moderately on carbon sources (0.695). [src: genotype_to_phenotype_enigma]

## Key figures

- **0.775 AUC**: AUC for binary growth on amino acids (scope KO presence/absence) [src: genotype_to_phenotype_enigma]
- **0.933 AUC**: AUC for tryptophan [src: genotype_to_phenotype_enigma]
- **0.780 AUC**: AUC on nucleosides [src: genotype_to_phenotype_enigma]
- **0.695 AUC**: AUC on carbon sources [src: genotype_to_phenotype_enigma]

## Evidence

> **Binary growth IS predictable** on amino acids (AUC 0.775, tryptophan 0.933) and nucleosides (0.780) from KO presence/absence; moderately predictable on carbon sources (0.695); **not predictable** on metals, antibiotics, or nitrogen from KO content alone. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

~76% of ENIGMA conditions (metals, antibiotics, nitrogen, stress) have neither GapMind pathway coverage nor CSP training data. [src: genotype_to_phenotype_enigma]

> **The coverage gap**: ~76% of ENIGMA conditions (metals, antibiotics, nitrogen, stress) have neither GapMind pathway coverage nor CSP training data. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- The bacterial growth model's SHAP features are weakly concordant with Fitness Browser (1.19× enrichment), because gene presence across genera and gene essentiality within one strain address different biological questions. [src: genotype_to_phenotype_enigma]
- Transfer learning from clinical phenotype databases may be biased for ENIGMA subsurface field isolates. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains to the KBase Data Lakehouse pangenome through ncbi_strain_identifiers caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The ENIGMA short strain name MT20, representing Rhodanobacter glycinis, matched unrelated Streptococcus pneumoniae, with name collisions injecting 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma]
- The report documents the strain-name collision pitfall in docs/pitfalls.md and says it affects any project linking ENIGMA strains to the pangenome by name. [src: genotype_to_phenotype_enigma]
