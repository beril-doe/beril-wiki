---
type: "Finding"
description: "The pre-registered null of uniform coverage across classes is not rejected: a \u03c7\u00b2 test on the 8 enigma_isolate_call callables by class gives \u03c7\u00b2=5.07, p=0.53 (df=6), and adding the single measured-fitness lauric acid (Fatty acids 1/10) does not change the verdict."
finding_id: "enigma_carbon_census_1--f8b7ca8b"
result: "null result"
source: "enigma_carbon_census_1"
quantities: [{"value": "\u03c7\u00b2=5.07", "what": "chi-square statistic for uniform coverage across classes", "unit": "", "denominator": "8 isolate-call callables", "scope": "df=6"}, {"value": "p=0.53", "what": "p-value of the uniform-coverage test", "unit": "", "denominator": "", "scope": "df=6"}, {"value": "5/25", "what": "Shikimates callable compounds", "unit": "compounds", "denominator": "25 Shikimates compounds", "scope": "largest class share in the test"}]
caveat: "With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the directional pattern is confounded with annotation coverage rather than a clean biological degradability gradient."
first_added: "2026-10-27"
source_hash: "62204d5c4271f61cef9bd5c3aee8b1410bebd0a60d508276d2875691a7194f49"
---
# Uniform class coverage of isolate-callable compounds not rejected, by an underpowered test

The pre-registered null of uniform coverage across classes is not rejected: a χ² test on the 8 enigma_isolate_call callables by class gives χ²=5.07, p=0.53 (df=6), and adding the single measured-fitness lauric acid (Fatty acids 1/10) does not change the verdict. [src: enigma_carbon_census_1]

## Key figures

- **χ²=5.07**: chi-square statistic for uniform coverage across classes (denominator 8 isolate-call callables; scope df=6) [src: enigma_carbon_census_1]
- **p=0.53**: p-value of the uniform-coverage test (scope df=6) [src: enigma_carbon_census_1]
- **5/25 compounds**: Shikimates callable compounds (denominator 25 Shikimates compounds; scope largest class share in the test) [src: enigma_carbon_census_1]

## Evidence

> But the **pre-registered null (uniform coverage across classes) is not rejected**: a χ² test on the 8 `enigma_isolate_call` callables by class (Shikimates 5/25, Alkaloids 2/26, Terpenoids 1/17, Fatty acids 0/10, Polyketides 0/2, AA/Peptides 0/2, mixed 0/1) gives **χ²=5.07, p=0.53 (df=6)**; adding the single measured-fitness lauric acid (Fatty acids 1/10) does not change the verdict. [src: enigma_carbon_census_1]

From the report [[summaries/enigma_carbon_census_1__REPORT]].

## Caveat

With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the directional pattern is confounded with annotation coverage rather than a clean biological degradability gradient. [src: enigma_carbon_census_1]

> With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the directional pattern is further **confounded with annotation coverage** (which classes KEGG/ModelSEED/genome_depot annotate) rather than a clean biological degradability gradient. [src: enigma_carbon_census_1]

## Other caveats in this report

- Lauric acid's measured-fitness organism is a reference bacterium, not an ENIGMA isolate. [src: enigma_carbon_census_1]
- Resource darkness is not evidence of biological absence; a shallow PubMed title screen yielded zero literature rescues. [src: enigma_carbon_census_1]
- Xanthine's R02107 reaction reflects purine nitrogen acquisition, not carbon catabolism; the effective carbon-callable count is 8 rather than 9. [src: enigma_carbon_census_1]
- Because rare capacities compress the φ coefficient, the reanalysis used Haldane-corrected odds ratios with 95% confidence intervals and Jaccard indices from saved 2×2 counts. [src: enigma_carbon_census_1]
- The 34 all-high-certainty terephthalic-acid calls reflect a single-reaction-signature artifact, not stronger evidence. [src: enigma_carbon_census_1]
