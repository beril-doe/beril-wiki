---
type: "Finding"
description: "With 8 positive and 16 negative results, the utilization comparison is underpowered (Mann-Whitney p=0.14, d=-0.57)."
finding_id: "bacdive_metal_validation--2a7f4c05"
result: "null result"
source: "bacdive_metal_validation"
quantities: [{"value": "8", "what": "positive utilization results", "unit": "results", "denominator": "", "scope": ""}, {"value": "16", "what": "negative utilization results", "unit": "results", "denominator": "", "scope": ""}, {"value": "0.14", "what": "Mann-Whitney p-value", "unit": "", "denominator": "", "scope": "positive versus negative utilizers"}, {"value": "-0.57", "what": "Cohen's d", "unit": "", "denominator": "", "scope": ""}]
caveat: "Positive utilizers had lower predicted scores, a surprising direction that is not significant and should not be over-interpreted given the tiny sample size."
first_added: "2026-10-27"
source_hash: "6b482275a5774daed2242605f701225afa538da071ebfacdff398459a8d660a0"
---
# Metal utilization tests show no significant link to predicted score

With 8 positive and 16 negative results, the utilization comparison is underpowered (Mann-Whitney p=0.14, d=-0.57). [src: bacdive_metal_validation]

## Key figures

- **8 results**: positive utilization results [src: bacdive_metal_validation]
- **16 results**: negative utilization results [src: bacdive_metal_validation]
- **0.14**: Mann-Whitney p-value (scope positive versus negative utilizers) [src: bacdive_metal_validation]
- **-0.57**: Cohen's d [src: bacdive_metal_validation]

## Evidence

> With 8 positive and 16 negative results, the comparison is underpowered (Mann-Whitney p=0.14, d=-0.57). [src: bacdive_metal_validation]

From the report [[summaries/bacdive_metal_validation__REPORT]].

## Caveat

Positive utilizers had lower predicted scores, a surprising direction that is not significant and should not be over-interpreted given the tiny sample size. [src: bacdive_metal_validation]

> The negative direction (positive utilizers had *lower* metal scores) is surprising but not significant and should not be over-interpreted given the tiny sample size. [src: bacdive_metal_validation]

## Other caveats in this report

- With n=10 heavy-metal isolates versus ~5,000 baseline isolates, the estimated minimum detectable effect at 80% power was approximately d=0.93. [src: bacdive_metal_validation]
- The observed d=1.00 was only slightly above the reported detection threshold. [src: bacdive_metal_validation]
- The plan referenced n=31 heavy-metal isolates, but only 10 matched scored pangenome species after bridging. [src: bacdive_metal_validation]
- The report attributes an 88% core estimate for metal-tolerance genes to the separate metal_specificity project; this is secondhand evidence here. [src: bacdive_metal_validation]
- The report proposes that within-species core-gene enrichment can coexist with between-species differences in total metal-tolerance gene content; this is an interpretation, not a separate test in this report. [src: bacdive_metal_validation]
