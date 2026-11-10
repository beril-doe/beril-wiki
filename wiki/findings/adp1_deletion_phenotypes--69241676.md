---
type: "Finding"
description: "625 genes (31%) have a condition specificity score \u2265 1.0, meaning their growth importance is concentrated on one carbon source, and the top condition-specific genes for each carbon source correspond to the expected metabolic pathways."
finding_id: "adp1_deletion_phenotypes--69241676"
result: "observation"
source: "adp1_deletion_phenotypes"
quantities: [{"value": "625", "what": "genes with condition specificity score \u2265 1.0", "unit": "genes", "denominator": "", "scope": ""}, {"value": "31%", "what": "share of genes with high condition specificity", "unit": "%", "denominator": "", "scope": ""}]
caveat: "Growth ratios are single-timepoint measurements with unknown technical noise, and the condition specificity analysis assumes that variation across conditions reflects biology, not measurement error."
first_added: "2026-10-27"
source_hash: "7d40ea0a5c21fdf6e9852ab3cc9628a50905fba2ddb532cd9dc5aa24117bb6f0"
---
# A third of genes concentrate growth importance on one carbon source

625 genes (31%) have a condition specificity score ≥ 1.0, meaning their growth importance is concentrated on one carbon source, and the top condition-specific genes for each carbon source correspond to the expected metabolic pathways. [src: adp1_deletion_phenotypes]

## Key figures

- **625 genes**: genes with condition specificity score ≥ 1.0 [src: adp1_deletion_phenotypes]
- **31%**: share of genes with high condition specificity [src: adp1_deletion_phenotypes]

## Evidence

> 625 genes (31%) have a condition specificity score ≥ 1.0, meaning their growth importance is concentrated on one carbon source. The top condition-specific genes for each carbon source correspond precisely to the expected metabolic pathways: [src: adp1_deletion_phenotypes]

From the report [[summaries/adp1_deletion_phenotypes__REPORT]].

## Caveat

Growth ratios are single-timepoint measurements with unknown technical noise, and the condition specificity analysis assumes that variation across conditions reflects biology, not measurement error. [src: adp1_deletion_phenotypes]

> - Growth ratios are single-timepoint measurements with unknown technical noise. The condition specificity analysis assumes that variation across conditions reflects biology, not measurement error. [src: adp1_deletion_phenotypes]

## Other caveats in this report

- The report contrasts its lack of discrete ADP1 modules, apart from the 24-gene quinate module, with published E. coli chemical-genetic modules; differing perturbation methods or organismal architecture are proposed, not established, explanations. [src: adp1_deletion_phenotypes]
- This analysis uses single-gene deletions rather than transposon sequencing; the report compares its 625 condition-specific genes with findings from RB-TnSeq. [src: adp1_deletion_phenotypes]
- The 2,034-gene complete matrix excludes 499 essential genes and 316 genes with incomplete data, biasing analysis toward dispensable genes with successful deletions. [src: adp1_deletion_phenotypes]
- Only eight conditions were tested; the approximately five inferred independent dimensions may increase with a broader panel. [src: adp1_deletion_phenotypes]
- The species-level A. baylyi pangenome assignment may have less resolution than a population-level analysis. [src: adp1_deletion_phenotypes]
