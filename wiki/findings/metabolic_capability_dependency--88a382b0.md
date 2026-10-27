---
type: "Finding"
description: "Pathway category strongly predicted dependency class (\u03c7\u00b2=163.6, df=4, p=2.5\u00d710\u207b\u00b3\u2074): carbon source utilization pathways were 24.3% latent (39.8% active), amino acid biosynthesis pathways 6.5% latent (63.5% active), and 'Other' pathways 2.9% latent (86.8% active)."
finding_id: "metabolic_capability_dependency--88a382b0"
result: "observation"
source: "metabolic_capability_dependency"
quantities: [{"value": "24.3%", "what": "carbon source utilization pathways classified latent", "unit": "percent", "denominator": "", "scope": "carbon source utilization pathways"}, {"value": "6.5%", "what": "amino acid biosynthesis pathways classified latent", "unit": "percent", "denominator": "", "scope": "amino acid biosynthesis pathways"}, {"value": "2.9%", "what": "'Other' pathways classified latent", "unit": "percent", "denominator": "", "scope": "'Other' category pathways"}, {"value": "\u03c7\u00b2=163.6", "what": "test of pathway category versus dependency class", "unit": "", "denominator": "", "scope": "df=4, p=2.5\u00d710\u207b\u00b3\u2074"}]
caveat: "Fitness experiments are biased toward laboratory conditions, and lab media may not reflect the conditions under which pathways are expressed, which may inflate the latent fraction."
first_added: "2026-10-27"
source_hash: "1412a5c1aa7711732d548b57744f3324a207e5eba6d0b4052c8882ac9cc593fe"
---
# Carbon utilization pathways are far more often latent than amino acid biosynthesis

Pathway category strongly predicted dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴): carbon source utilization pathways were 24.3% latent (39.8% active), amino acid biosynthesis pathways 6.5% latent (63.5% active), and 'Other' pathways 2.9% latent (86.8% active). [src: metabolic_capability_dependency]

## Key figures

- **24.3%**: carbon source utilization pathways classified latent (scope carbon source utilization pathways) [src: metabolic_capability_dependency]
- **6.5%**: amino acid biosynthesis pathways classified latent (scope amino acid biosynthesis pathways) [src: metabolic_capability_dependency]
- **2.9%**: 'Other' pathways classified latent (scope 'Other' category pathways) [src: metabolic_capability_dependency]
- **χ²=163.6**: test of pathway category versus dependency class (scope df=4, p=2.5×10⁻³⁴) [src: metabolic_capability_dependency]

## Evidence

> Pathway category strongly predicted dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴). Carbon source utilization pathways were most likely to be latent (24.3% latent, 39.8% active), while amino acid biosynthesis pathways were predominantly active (63.5% active, 6.5% latent). "Other" category pathways were rarely latent (2.9% latent, 86.8% active). [src: metabolic_capability_dependency]

From the report [[summaries/metabolic_capability_dependency__REPORT]].

## Caveat

Fitness experiments are biased toward laboratory conditions, and lab media may not reflect the conditions under which pathways are expressed, which may inflate the latent fraction. [src: metabolic_capability_dependency]

> - **Fitness experiments are biased toward laboratory conditions**: lab media may not reflect the full range of conditions under which pathways are expressed, inflating the latent fraction. [src: metabolic_capability_dependency]

## Other caveats in this report

- Across 16 threshold combinations, the latent fraction ranged from 4.7% to 21.1% (SD = 5.9 percentage points), versus 15.8% at default thresholds; the estimated fraction is moderately threshold-sensitive. [src: metabolic_capability_dependency]
- Deoxyribonate and myoinositol were absent from all analyses for lack of SEED matches; phenylalanine and tyrosine entered via phe and tyr abbreviations; alanine was excluded from classification because fewer than 3 SEED-annotated genes met coverage. [src: metabolic_capability_dependency]
- The report interprets the positive clade-level openness association alongside the null pathway-level conservation comparison as mixed evidence for the Black Queen framework, not uniform support. [src: metabolic_capability_dependency]
- The pathway-completeness conservation measure cannot detect partial gene erosion. [src: metabolic_capability_dependency]
- Fitness coverage of only 48 organisms may inflate apparent conservation when other members of their species clades were not fitness-tested. [src: metabolic_capability_dependency]
