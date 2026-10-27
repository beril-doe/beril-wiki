---
type: "Finding"
description: "KO-based binary-growth prediction varies by condition: amino acids reach AUC 0.775, tryptophan 0.933, nucleosides 0.780 and carbon sources 0.695, while metals, antibiotics and nitrogen are not predictable from KO content alone; 95 of 343 tested conditions exceed AUC 0.75."
finding_id: "genotype_to_phenotype_enigma--602fd76d"
result: "observation"
source: "genotype_to_phenotype_enigma"
quantities: [{"value": "0.775", "what": "AUC for binary growth on amino acids", "unit": "AUC", "denominator": "", "scope": "KO presence/absence features"}, {"value": "0.933", "what": "AUC for binary growth on tryptophan", "unit": "AUC", "denominator": "", "scope": "KO presence/absence features"}, {"value": "0.695", "what": "AUC for binary growth on carbon sources", "unit": "AUC", "denominator": "", "scope": "KO presence/absence features"}, {"value": "95 of 343", "what": "tested conditions with AUC > 0.75", "unit": "conditions", "denominator": "343 tested conditions", "scope": ""}]
caveat: "The model predicts growth through combinations of prevalence-variable KOs that act as genus-level proxies rather than individually mechanistically causal genes, with per-strain Fitness Browser enrichment ranging from 1.72x (Cup4G11) to 0.83x (pseudo1_N1B4)."
first_added: "2026-10-27"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Binary growth is predictable from gene content only for some condition classes

KO-based binary-growth prediction varies by condition: amino acids reach AUC 0.775, tryptophan 0.933, nucleosides 0.780 and carbon sources 0.695, while metals, antibiotics and nitrogen are not predictable from KO content alone; 95 of 343 tested conditions exceed AUC 0.75. [src: genotype_to_phenotype_enigma]

## Key figures

- **0.775 AUC**: AUC for binary growth on amino acids (scope KO presence/absence features) [src: genotype_to_phenotype_enigma]
- **0.933 AUC**: AUC for binary growth on tryptophan (scope KO presence/absence features) [src: genotype_to_phenotype_enigma]
- **0.695 AUC**: AUC for binary growth on carbon sources (scope KO presence/absence features) [src: genotype_to_phenotype_enigma]
- **95 of 343 conditions**: tested conditions with AUC > 0.75 (denominator 343 tested conditions) [src: genotype_to_phenotype_enigma]

## Evidence

> - **Binary growth IS predictable** on amino acids (AUC 0.775, tryptophan 0.933) and nucleosides (0.780) from KO presence/absence; moderately predictable on carbon sources (0.695); **not predictable** on metals, antibiotics, or nitrogen from KO content alone. 95 of 343 tested conditions achieve AUC > 0.75. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

The model predicts growth through combinations of prevalence-variable KOs that act as genus-level proxies rather than individually mechanistically causal genes, with per-strain Fitness Browser enrichment ranging from 1.72x (Cup4G11) to 0.83x (pseudo1_N1B4). [src: genotype_to_phenotype_enigma]

> Per-strain enrichment ranges from 1.72x (Cup4G11) to 0.83x (pseudo1_N1B4, no enrichment). The model predicts growth correctly (AUC 0.78 for amino acids) through *combinations* of prevalence-variable KOs that act as genus-level proxies, not through individually mechanistically causal genes. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- Ribose transporter and protocatechuate cycloisomerase are interpretable feature examples, but concordance with Fitness Browser is weak at 1.19× enrichment; cross-genus gene presence and within-strain essentiality address different questions. [src: genotype_to_phenotype_enigma]
- GTDB-based profiles classify global Pseudomonas genomes as 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic, whereas ENIGMA Pseudomonas are in environmental Pseudomonas_E. Rhodanobacter is reported as 55% aquatic, 10% contaminated, and 0% clinical. Transfer from clinical phenotype databases may be biased. [src: genotype_to_phenotype_enigma]
- Different pH-dependent growth profiles and predictive genomic features for the two clusters are proposed expectations, not reported validation results. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains by `ncbi_strain_identifiers` caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The MT20 collision linked Rhodanobacter glycinis to unrelated Streptococcus pneumoniae and introduced 1,751 spurious clinical genomes. GTDB-Tk taxonomy and genus checks reduced verified linkages from 32 to 20 while eliminating false matches. [src: genotype_to_phenotype_enigma]
