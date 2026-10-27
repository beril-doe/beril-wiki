---
type: "Finding"
description: "In Desulfovibrio vulgaris Hildenborough, field-stress (q=0.026), field-core (q=0.026) and lab-nutrient (q=0.037) genes are significantly enriched in the core genome after BH-FDR correction, while heavy-metals and lab-antibiotic genes trend below baseline but are not significant."
finding_id: "field_vs_lab_fitness--571f3f78"
result: "observation"
source: "field_vs_lab_fitness"
quantities: [{"value": "0.026", "what": "BH-FDR q for core enrichment of field-stress genes", "unit": "", "denominator": "", "scope": "non-essential DvH genes"}, {"value": "0.026", "what": "BH-FDR q for core enrichment of field-core genes", "unit": "", "denominator": "", "scope": "non-essential DvH genes"}, {"value": "0.037", "what": "BH-FDR q for core enrichment of lab-nutrient genes", "unit": "", "denominator": "", "scope": "non-essential DvH genes"}]
caveat: "Lab-nutrient genes are also significantly enriched (81.4%, q=0.037) and the field-specific vs lab-specific gene comparison is not significant (Fisher exact OR=0.32, p=0.27, n=50-52 per group), which limits an ecological-specificity reading."
first_added: "2026-10-27"
source_hash: "8bf50c605e80b6db78122bc45bdfce5cb3ef8bc17821932e2e7ab7fb94e5622c"
---
# Field-stress, field-core and lab-nutrient genes are enriched in the core genome

In Desulfovibrio vulgaris Hildenborough, field-stress (q=0.026), field-core (q=0.026) and lab-nutrient (q=0.037) genes are significantly enriched in the core genome after BH-FDR correction, while heavy-metals and lab-antibiotic genes trend below baseline but are not significant. [src: field_vs_lab_fitness]

## Key figures

- **0.026**: BH-FDR q for core enrichment of field-stress genes (scope non-essential DvH genes) [src: field_vs_lab_fitness]
- **0.026**: BH-FDR q for core enrichment of field-core genes (scope non-essential DvH genes) [src: field_vs_lab_fitness]
- **0.037**: BH-FDR q for core enrichment of lab-nutrient genes (scope non-essential DvH genes) [src: field_vs_lab_fitness]

## Evidence

> Field-stress (q=0.026), field-core (q=0.026), and lab-nutrient (q=0.037) genes are significantly enriched in the core genome after BH-FDR correction. Heavy-metals and lab-antibiotic genes trend below baseline but are not significant. [src: field_vs_lab_fitness]

From the report [[summaries/field_vs_lab_fitness__REPORT]].

## Caveat

Lab-nutrient genes are also significantly enriched (81.4%, q=0.037) and the field-specific vs lab-specific gene comparison is not significant (Fisher exact OR=0.32, p=0.27, n=50-52 per group), which limits an ecological-specificity reading. [src: field_vs_lab_fitness]

> However, lab-nutrient genes are also significantly enriched (81.4%, q=0.037), and the field-specific vs lab-specific gene comparison is not significant (Fisher exact OR=0.32, p=0.27, n=50-52 per group). [src: field_vs_lab_fitness]

## Other caveats in this report

- ENIGMA CORAL has 4,346 field samples across 596 Oak Ridge locations and 213,044 ASVs, but these do not provide DvH gene-level fitness. [src: field_vs_lab_fitness]
- The 678 essential genes (80.1% core) were excluded because no transposon mutants and hence no fitness data were available. [src: field_vs_lab_fitness]
- Accessory resistance and mobile-element involvement are interpretations, not directly demonstrated mechanisms. [src: field_vs_lab_fitness]
- The proposed mechanistic explanation for the metal-class contrast is tentative. [src: field_vs_lab_fitness]
- The report interprets antibiotic and metal resistance as accessory-enriched, although its class comparisons versus baseline were not statistically significant. [src: field_vs_lab_fitness]
