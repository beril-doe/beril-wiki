---
type: "Finding"
description: "Comparing SHAP importance between the n=7 anchor model and the full 46K-pair corpus, the report concludes that with 7 strains the model uses condition class (45.9%) and genome-scale features (25.3%), whereas with 46K pairs condition-specific catabolic genes emerge."
finding_id: "genotype_to_phenotype_enigma--ad8903f3"
result: "inference"
source: "genotype_to_phenotype_enigma"
quantities: [{"value": "45.9%", "what": "SHAP share of condition class in the n=7 anchor model", "unit": "% of total SHAP", "denominator": "", "scope": "n=7 anchor model"}, {"value": "25.3%", "what": "SHAP share of genome-scale features in the n=7 anchor model", "unit": "% of total SHAP", "denominator": "", "scope": "n=7 anchor model"}]
caveat: "The n=7 analysis uses leave-one-strain-out on 4 Pseudomonas_E strains and one each of Cupriavidus, Acidovorax and Pedobacter, so it does not test cross-genus generalization or per-condition prediction quality."
first_added: "2026-10-27"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Condition-specific catabolic genes emerge only with large training sets

Comparing SHAP importance between the n=7 anchor model and the full 46K-pair corpus, the report concludes that with 7 strains the model uses condition class (45.9%) and genome-scale features (25.3%), whereas with 46K pairs condition-specific catabolic genes emerge. [src: genotype_to_phenotype_enigma]

## Key figures

- **45.9% % of total SHAP**: SHAP share of condition class in the n=7 anchor model (scope n=7 anchor model) [src: genotype_to_phenotype_enigma]
- **25.3% % of total SHAP**: SHAP share of genome-scale features in the n=7 anchor model (scope n=7 anchor model) [src: genotype_to_phenotype_enigma]

## Evidence

> Comparing SHAP feature importance between the n=7 anchor model (NB06) and the full 46K-pair corpus (NB07) reveals a qualitative shift: with 7 strains, the model uses condition class (45.9%) and genome-scale features (25.3%); with 46K pairs, **condition-specific catabolic genes emerge** — ribose transporter (K10440), proline transporter (K03762), protocatechuate cycloisomerase (K01857), AraC regulators (K13633). This quantifies the data requirement for mechanistic prediction. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

The n=7 analysis uses leave-one-strain-out on 4 Pseudomonas_E strains and one each of Cupriavidus, Acidovorax and Pedobacter, so it does not test cross-genus generalization or per-condition prediction quality. [src: genotype_to_phenotype_enigma]

> **Limitation**: This analysis uses leave-one-strain-out on 7 strains (4 Pseudomonas_E, 1 each Cupriavidus, Acidovorax, Pedobacter). It does NOT test cross-genus generalization (e.g., train on Pseudomonas, predict Pedobacter), does NOT analyze per-condition prediction quality, and does NOT use condition-specific features. The model effectively learns "big genomes grow on amino acids" — biologically real but not the condition-specific prediction needed for practical use. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- Ribose transporter and protocatechuate cycloisomerase are interpretable feature examples, but concordance with Fitness Browser is weak at 1.19× enrichment; cross-genus gene presence and within-strain essentiality address different questions. [src: genotype_to_phenotype_enigma]
- GTDB-based profiles classify global Pseudomonas genomes as 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic, whereas ENIGMA Pseudomonas are in environmental Pseudomonas_E. Rhodanobacter is reported as 55% aquatic, 10% contaminated, and 0% clinical. Transfer from clinical phenotype databases may be biased. [src: genotype_to_phenotype_enigma]
- Different pH-dependent growth profiles and predictive genomic features for the two clusters are proposed expectations, not reported validation results. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains by `ncbi_strain_identifiers` caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The MT20 collision linked Rhodanobacter glycinis to unrelated Streptococcus pneumoniae and introduced 1,751 spurious clinical genomes. GTDB-Tk taxonomy and genus checks reduced verified linkages from 32 to 20 while eliminating false matches. [src: genotype_to_phenotype_enigma]
