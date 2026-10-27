---
type: "Finding"
description: "The report concludes that gene length is a much stronger predictor of core status than fitness effects from either field or lab conditions, and that neither fitness dimension alone is informative (CV-AUC near 0.5)."
finding_id: "field_vs_lab_fitness--d31622df"
result: "inference"
source: "field_vs_lab_fitness"
quantities: [{"value": "near 0.5", "what": "cross-validated AUC for predicting core status from field or lab fitness alone", "unit": "CV-AUC", "denominator": "", "scope": "DvH"}]
caveat: "Gene length is confounded with both fitness measurement quality (short genes get fewer transposon insertions) and core status (core genes tend to be longer)."
first_added: "2026-10-27"
source_hash: "8bf50c605e80b6db78122bc45bdfce5cb3ef8bc17821932e2e7ab7fb94e5622c"
---
# Gene length is judged a stronger predictor of core status than fitness

The report concludes that gene length is a much stronger predictor of core status than fitness effects from either field or lab conditions, and that neither fitness dimension alone is informative (CV-AUC near 0.5). [src: field_vs_lab_fitness]

## Key figures

- **near 0.5 CV-AUC**: cross-validated AUC for predicting core status from field or lab fitness alone (scope DvH) [src: field_vs_lab_fitness]

## Evidence

> Gene length is a much stronger predictor of core status than fitness effects from either field or lab conditions. Neither fitness dimension alone is informative (CV-AUC near 0.5). [src: field_vs_lab_fitness]

From the report [[summaries/field_vs_lab_fitness__REPORT]].

## Caveat

Gene length is confounded with both fitness measurement quality (short genes get fewer transposon insertions) and core status (core genes tend to be longer). [src: field_vs_lab_fitness]

> - Gene length is confounded with both fitness measurement quality (short genes get fewer transposon insertions) and core status (core genes tend to be longer) [src: field_vs_lab_fitness]

## Other caveats in this report

- ENIGMA CORAL has 4,346 field samples across 596 Oak Ridge locations and 213,044 ASVs, but these do not provide DvH gene-level fitness. [src: field_vs_lab_fitness]
- The 678 essential genes (80.1% core) were excluded because no transposon mutants and hence no fitness data were available. [src: field_vs_lab_fitness]
- The lab-nutrient enrichment and nonsignificant field-versus-lab-specific comparison limit the ecological-specificity hypothesis. [src: field_vs_lab_fitness]
- Accessory resistance and mobile-element involvement are interpretations, not directly demonstrated mechanisms. [src: field_vs_lab_fitness]
- The proposed mechanistic explanation for the metal-class contrast is tentative. [src: field_vs_lab_fitness]
