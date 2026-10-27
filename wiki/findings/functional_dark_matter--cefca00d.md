---
type: "Finding"
description: "Among 7,491 dark genes, the hypothesis that stress-condition genes are more accessory than carbon/nitrogen genes was not supported: stress genes were 23.0% accessory versus 25.5% for carbon/nitrogen (Fisher's exact OR=1.15, p=0.013), the opposite direction."
finding_id: "functional_dark_matter--cefca00d"
result: "null result"
source: "functional_dark_matter"
quantities: [{"value": "23.0%", "what": "stress-condition dark genes that are accessory", "unit": "percent", "denominator": "", "scope": "n=7,491 dark genes"}, {"value": "25.5%", "what": "carbon/nitrogen dark genes that are accessory", "unit": "percent", "denominator": "", "scope": "n=7,491 dark genes"}, {"value": "1.15", "what": "Fisher's exact odds ratio", "unit": "", "denominator": "", "scope": ""}, {"value": "0.013", "what": "Fisher's exact p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "Not all 48 organisms were tested under the same conditions; organisms with more conditions (e.g., MR-1 with 121) produce more specific phenotypes, biasing prioritization."
first_added: "2026-10-23"
source_hash: "1ea00a93830c52ac6d4c47418f8d718cf6b5aa2d81462a64855a8308888da1d0"
---
# Stress-condition dark genes are not more accessory than carbon/nitrogen genes

Among 7,491 dark genes, the hypothesis that stress-condition genes are more accessory than carbon/nitrogen genes was not supported: stress genes were 23.0% accessory versus 25.5% for carbon/nitrogen (Fisher's exact OR=1.15, p=0.013), the opposite direction. [src: functional_dark_matter]

## Key figures

- **23.0%**: stress-condition dark genes that are accessory (scope n=7,491 dark genes) [src: functional_dark_matter]
- **25.5%**: carbon/nitrogen dark genes that are accessory (scope n=7,491 dark genes) [src: functional_dark_matter]
- **1.15**: Fisher's exact odds ratio [src: functional_dark_matter]
- **0.013**: Fisher's exact p-value [src: functional_dark_matter]

## Evidence

> - **H1b (Conservation signal)**: **Not supported.** Formal testing (Fisher's exact, n=7,491 dark genes; NB06) showed the opposite of the predicted pattern: stress-condition dark genes are 23.0% accessory, while carbon/nitrogen dark genes are 25.5% accessory (OR=1.15, p=0.013). The hypothesis that stress genes should be more accessory than carbon/nitrogen genes is rejected. This suggests that the relationship between condition specificity and pangenome conservation is more complex than a simple stress=accessory, metabolism=core dichotomy. [src: functional_dark_matter]

From the report [[summaries/functional_dark_matter__REPORT]].

## Caveat

Not all 48 organisms were tested under the same conditions; organisms with more conditions (e.g., MR-1 with 121) produce more specific phenotypes, biasing prioritization. [src: functional_dark_matter]

> 5. **Condition coverage unevenness**: Not all 48 organisms were tested under the same conditions. Organisms with more conditions (e.g., MR-1 with 121) produce more specific phenotypes, biasing them toward higher prioritization scores. [src: functional_dark_matter]

## Other caveats in this report

- The fraction of hypothetical genes ranges from >35% to <15% across species; the report attributes this variation to annotation depth rather than true functional content. [src: functional_dark_matter]
- The pathway-gap result is organism-level co-occurrence, not direct gene-to-gap enzymatic matching. [src: functional_dark_matter]
- Dark-gene gap filling remains a hypothesis requiring enzyme-number matching, structure prediction, or experiments. [src: functional_dark_matter]
- Marinobacter has 49 gapped pathways, and D. desulfuricans ME-23 and P. stutzeri have 45 each; their dark genes are proposed, not established, as possible missing-step enzymes. [src: functional_dark_matter]
- The report interprets carbon-source and motility concordance as possible conserved unannotated functions, and OG05812 as a possible stress-associated regulatory protease; these are functional hypotheses. [src: functional_dark_matter]
