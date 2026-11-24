---
type: "Concept"
description: "How small matched groups, culture-collection bias, taxonomy-bridge loss and tiny phenotype subsets limit validation of genome- or fitness-based metal-tolerance predictions against isolate isolation-environment metadata."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/pitfalls.md"]
---
# Validating metal-tolerance predictions against culture-collection metadata

This page covers how small matched groups, culture-collection bias, taxonomy-bridge loss and tiny phenotype subsets limit validation of metal-tolerance predictions against isolate isolation-environment metadata. In the BacDive heavy-metal comparison, the observed d=1.00 barely exceeded the detection threshold for the n=10 group. [src: bacdive_metal_validation] The metal-utilization phenotype test was inconclusive [src: bacdive_metal_validation], and the Fitness Browser (FB) species-scale test found no correlation. [src: metal_cross_resistance] See also [[concepts/isolation-environment-validation-of-genome-predicted-metal-tolerance]].

## Small groups after matching

Matching shrinks the groups. [[entities/bacdive]] has 31 strains tagged cat3=#Heavy metal contamination, but only 10 match pangenome species with metal tolerance scores. [src: pitfalls, bacdive_metal_validation] The report therefore recommends computing post-matching sample sizes and power before interpreting results. [src: pitfalls]

With n=10 heavy metal isolates against ~5,000 environmental baseline isolates, the minimum detectable effect size at 80% power is approximately d=0.93. [src: bacdive_metal_validation] The observed d=1.00 barely exceeds this threshold, so power was just enough. [src: bacdive_metal_validation] The effect-size estimate is imprecise, and a larger heavy metal contamination dataset would be needed to estimate it precisely. [src: bacdive_metal_validation] Contamination-isolate samples are also small in Bacillota and Bacteroidota, where the signal is not significant (p=0.285 and p=0.456). [src: bacdive_metal_validation]

## Relation to the Oak Ridge result

The earlier lab_field_ecology project found a suggestive but nonsignificant correlation between FB lab metal tolerance and field abundance at Oak Ridge (rho=0.50, p=0.095, n=11 genera). [src: bacdive_metal_validation] The BacDive report calls its own analysis stronger evidence for the same hypothesis at larger scale (n=10 for heavy metal, n=176 for all contamination, d=+0.43-1.00). [src: bacdive_metal_validation] It attributes the difference in significance to the power gained from BacDive's larger sample. [src: bacdive_metal_validation] The two analyses use different populations and tests, so this is the report's interpretation and not a direct comparison. See [[concepts/laboratory-fitness-as-a-predictor-of-field-abundance]].

## Fitness Browser scale: a null result

In metal_cross_resistance, multi-metal tolerance scores did not correlate with BacDive isolation from metal environments at the FB species scale (Spearman rho ~ -0.02, p > 0.8). [src: metal_cross_resistance] The validation set excluded 2 organisms without tier classification data (azobra and BFirm, with <3 metals). [src: metal_cross_resistance] It also collapsed multiple FB strains of a species into one entry, for example 5 P. fluorescens strains sharing the same BacDive pool. [src: metal_cross_resistance] The effective sample size was 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance] That report states that a prior project showed metal-tolerance prediction needs pangenome-scale analysis (42K strains, Cohen's d = +1.0) to reach power. [src: metal_cross_resistance] It also says organism-scale validation (n = 26) lacks the power of the [[entities/metal-fitness-atlas]] at pangenome scale. [src: metal_cross_resistance] It states that a proper test would apply the Metal Fitness Atlas KEGG/PFAM mapping approach to the cross-resistance gene signatures across 27K species. [src: metal_cross_resistance] It proposes predicting multi-metal tolerance across those species and validating against BacDive polymetallic isolation environments. [src: metal_cross_resistance]

## Taxonomy-bridge loss and fuzzy matching

The BacDive-to-GTDB bridge left 55,107 strains (56.6%) unmatched because no GTDB species was available. [src: bacdive_metal_validation] The report attributes this mainly to GTDB using different species boundaries than LPSN/DSMZ. [src: bacdive_metal_validation] Matching by genus+species substring is imprecise for genus-only identifications such as "Acidovorax sp.", and these fuzzy matches need caution. [src: metal_cross_resistance] See [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases]] and [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]].

## Culture-collection bias

BacDive holds culturable, described strains and not the full diversity of environmental bacteria. Metal-tolerant extremophiles may be under-represented. [src: bacdive_metal_validation]

## Tiny phenotype subsets

Only 24 BacDive metal utilization test records (iron, manganese, arsenate, chromate, cobalt, zinc) matched strains with metal tolerance scores. [src: bacdive_metal_validation] With 8 positive and 16 negative results, the comparison was underpowered (Mann-Whitney p=0.14, d=-0.57). [src: bacdive_metal_validation] Positive utilizers had lower metal scores. The report calls this direction surprising and warns against over-interpreting it. [src: bacdive_metal_validation] It judges the phenotype validation inconclusive. [src: bacdive_metal_validation] It suggests the BacDive API (application programming interface) may hold further tolerance data, such as MIC data and growth inhibition, that are absent from the current metabolite_utilization table. [src: bacdive_metal_validation]

## Open Directions

- Re-run the heavy-metal comparison with a larger contamination set, or with a better species bridge, to narrow the interval on d=1.00 (gap: n=10, at the detection limit).
- Predict multi-metal tolerance across 27K species with the KEGG/PFAM mapping approach and validate it against BacDive polymetallic isolation environments. This closes the n=20 power gap.
- Pull MIC and growth-inhibition records from the BacDive API to replace the 24-record utilization subset.
- Measure how many of the 55,107 unmatched strains a synonym-aware bridge would recover, and whether the recovered strains differ in isolation environment.
