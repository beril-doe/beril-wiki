---
type: Summary
description: Rational microbiome formulation design for excluding Pseudomonas aeruginosa
doc_type: short
full_text: ../sources/cf_formulation_design__REPORT.md
title: Rational Design of Protective Microbiome Formulations for Competitive Exclusion
  of *Pseudomonas aeruginosa* in Cystic Fibrosis Airways
sources:
- id: cf_formulation_design
  resource: ../sources/cf_formulation_design__REPORT.md
  title: cf formulation design
---
# Rational Design of Protective Microbiome Formulations for Competitive Exclusion of *Pseudomonas aeruginosa* in Cystic Fibrosis Airways

## Overview

This report integrates planktonic inhibition assays, carbon-utilization profiling, growth kinetics, patient metagenomics and metatranscriptomics, pairwise interaction data, and pangenome analysis to design commensal communities that suppress *Pseudomonas aeruginosa* (PA) in cystic-fibrosis airways through metabolic competition and direct antagonism. The study analyzed 4,949 isolates from 175 patient samples, including 220 inhibition-tested isolates, 430 isolates profiled on 21 substrates, 32 isolates with growth kinetics, and 499 pangenome genomes across six species. [^cf_formulation_design]

## Key Findings

### Metabolic competition and inhibition

PA14 preferentially used amino acids under synthetic cystic-fibrosis sputum conditions, with endpoint OD values of 0.60 for proline, 0.56 for histidine, 0.46 for ornithine, 0.40 for glutamate, 0.36 for aspartate, 0.36 for isoleucine, and 0.35 for arginine; glucose supported OD 0.22, while threonine, methionine, cysteine, serine, and glycine each supported essentially no growth at <0.07. [^cf_formulation_design]

Across the 142-isolate cohort with both inhibition and carbon-utilization data, metabolic overlap with PA14 significantly predicted planktonic inhibition (r = 0.384, p = 2.3×10⁻⁶). A multivariate metabolic model explained R² = 0.274 of inhibition variance, increasing to R² = 0.360 after adding genus-level taxonomy; five-fold cross-validation yielded CV R² = 0.145 ± 0.142, indicating that the out-of-sample predictive power was lower than the training fit. [^cf_formulation_design]

The results support metabolic competition as a real but incomplete mechanism: approximately 73% of inhibition variance remained unexplained by metabolism alone, while genus contributed an additional 8.6% of explained variance and likely captured species-specific direct-antagonism mechanisms. Positive residuals identified *Streptococcus salivarius* ASMA-737 (+74.1%), *Gemella sanguinis* ASMA-3044 (+62.2%), and *Neisseria mucosa* ASMA-3643 (+57.2%) as candidate dual-mechanism inhibitors. [^cf_formulation_design]

### Growth kinetics and patient ecology

PA14 was generally the fastest grower on preferred substrates: commensals exceeded its maximum growth rate in only 13.8% of substrate comparisons, but commensals began growing earlier in 43.1% of comparisons. Growth kinetic parameters were moderately correlated with endpoint OD (r ≈ 0.40), and adding kinetics to the metabolic model increased the fit to R² = 0.311 for the 29 isolates with all three assay types. [^cf_formulation_design]

Among 134 species detected in patient metagenomes, the engraftability score, defined as prevalence × log(activity ratio), was highest for *N. mucosa* at 1.595; *Rothia dentocariosa* scored 0.422 and *S. salivarius* scored 0.172, both above the median among inhibition-tested species. [^cf_formulation_design]

### Formulation optimization

Strict safety-filter optimization identified a five-species core consisting of *N. mucosa*, *S. salivarius*, *Micrococcus luteus*, *R. dentocariosa*, and *G. sanguinis*. The best strict-safe formulations were: k=1, *N. mucosa*, with 18% niche coverage, 88% inhibition, and engraftability 1.595; k=2, *R. dentocariosa* + *N. mucosa*, with 18% coverage, 84% inhibition, and engraftability 0.820; k=3, *M. luteus* + *N. mucosa* + *S. salivarius*, with 100% coverage, 75% inhibition, and engraftability 0.140; k=4, *R. dentocariosa* + *M. luteus* + *N. mucosa* + *S. salivarius*, with 100% coverage, 76% inhibition, and engraftability 0.185; and k=5, the five-species core, with 100% coverage, 78% inhibition, and engraftability 0.188. [^cf_formulation_design]

The k=3 formulation was the minimum size achieving complete PA14 niche coverage because *M. luteus* grew on 9 of PA14's 11 preferred substrates. Exhaustive enumeration of C(97,3) = 147,440 possible triples produced 127,598 valid unique-species formulations, and the same k=3 combination was the global optimum with composite score 0.562. [^cf_formulation_design]

Bootstrap resampling over 1,000 replicates produced 95% composite-score confidence intervals of [0.753, 0.753] for k=1, [0.514, 0.588] for k=2, [0.551, 0.562] for k=3, [0.534, 0.578] for k=4, and [0.520, 0.587] for k=5; the k=2 through k=5 intervals overlapped, so formulation sizes were not statistically distinguishable on the composite score. [^cf_formulation_design]

The report recommends k=2 (*R. dentocariosa* + *N. mucosa*) as the primary clinical candidate because both species are lung-adapted, provide 84% mean inhibition, and have combined engraftability 0.820, nearly 6× higher than the k=3 formulation's 0.140. The k=3 formulation is an aspirational second-line candidate contingent on demonstrating *M. luteus* engraftment in vivo. [^cf_formulation_design]

Core-species profiles were: *N. mucosa*, 88% best inhibition, engraftability 1.595, 15 pangenome genomes, 16/18 conserved amino-acid pathways, and 5 lung genomes (33%); *S. salivarius*, 98%, 0.172, 153 genomes, 18/18 pathways, and 5 lung genomes (4%); *R. dentocariosa*, 79%, 0.422, 29 genomes, 14/18 pathways, and 10 lung genomes (38%); *G. sanguinis*, 85%, 0.202, 7 genomes, 7/18 pathways, and 1 lung genome; and *M. luteus*, 38%, 0.000, 295 genomes, 18/18 pathways, and 0 lung genomes. [^cf_formulation_design]

### Prebiotics and pangenome conservation

PA14 outgrew the average commensal on every one of the 22 tested substrates, and no tested amino acid or simple sugar provided a clear commensal growth advantage; the most selective substrates had commensal-to-PA14 ratios of only 0.77–0.96. [^cf_formulation_design]

Genomic pathway comparison identified six pathways complete in at least one core commensal species but absent or nearly absent in PA14: myoinositol, xylitol, xylose, arabinose, fucose, and rhamnose. PA pathway completeness was 0% for myoinositol, xylitol, xylose, and arabinose, and 1% for fucose and rhamnose; corresponding selectivity values were 1.00 for the first four and 0.99 for the latter two. Patient metatranscriptomics additionally identified 47 KEGG pathways with a >2× commensal-to-PA expression ratio. [^cf_formulation_design]

The proposed prebiotic strategy therefore shifts from amino-acid competition to sugar alcohols and pentoses: xylitol is predicted to support *S. salivarius*, myoinositol to support *R. dentocariosa*, and xylose and arabinose to support *N. mucosa* and *G. sanguinis*. These predictions require experimental validation before use. [^cf_formulation_design]

GapMind pathway conservation across 499 genomes supported species-level robustness. *M. luteus* had 18/18 amino-acid pathways and 39/39 carbon pathways conserved at >95%; *S. salivarius* had 18/18 and 32/35; *R. dentocariosa* had 14/18 and 39/41; *N. mucosa* had 16/16 and 27/27; and *G. sanguinis* had 7/18 and 37/39, respectively. [^cf_formulation_design]

### Pairwise interactions and PA diversity

Pairwise competition data showed mean synergy scores of +5.3% for *N. mucosa* + ASMA-2260, +1.4% for ASMA-3913 + ASMA-2260, −2.2% for *N. mucosa* + ASMA-2464, −14.2% for ASMA-3913 + ASMA-2464, and −19.8% for ASMA-1478 + ASMA-1197. Overall mean synergy was −5.8%, but the analysis included only 8 comparisons across 5 unique pairs, so additive formulation scoring remains provisional. [^cf_formulation_design]

Across 1,796 lung or respiratory PA genomes, amino-acid catabolic pathways were 97.4% conserved, and proline utilization was complete in 97% of lung isolates. Lung PA showed losses in sugar pathways, including sorbitol (−0.165), mannitol (−0.204), and gluconate (−0.185), consistent with metabolic streamlining toward amino-acid dependence. [^cf_formulation_design]

The PA amino-acid target set was invariant across virulence backgrounds: amino-acid catabolic pathways did not differ significantly between ExoU+ and ExoS+ PA, with GapMind score differences <0.03 and zero FDR-significant pathways. CF PA was 94% ExoS+ and 5% ExoU+ among 291 CF genomes, whereas PA14 is ExoU+; 96.4% of PA genomes carried both Pel and Psl operons, and only 3.5% were Pel-only. [^cf_formulation_design]

Among 643 annotated PROTECT PA genomes, 304 (47%) were PAO1-like, 48 (7%) were PA14-like, and 291 (45%) were intermediate; among classifiable isolates, 86% were PAO1-like. The PROTECT isolates were distributed across the broader lung-PA diversity in a Pfam-based tree of 165 genomes rather than clustering in one lineage. [^cf_formulation_design]

## Caveats and Limitations

The inhibition assays were planktonic and used PA14, whereas PA in cystic-fibrosis lungs primarily occupies structured biofilms. The carbon panel contained 22 tested substrates and omitted mucins, lipids, iron, polyamines, and the sugar alcohols identified genomically. [^cf_formulation_design]

The metabolic model was based on 142 isolates covering 62 of 211 species (29%), and growth kinetics were available for only 32 isolates; the core cohort was enriched for deeply characterized taxa, including *Rothia*, *Streptococcus*, *Neisseria*, and *Gemella*. [^cf_formulation_design]

Pairwise interaction data covered only 3 A × 3 B isolate combinations, and the complete 10-pair interaction matrix for the five-species core has not been measured. Moreover, `fact_pairwise_interaction` was identical to `fact_carbon_utilization`, with correlation = 1.0 and mean difference = 0.0, so endpoint OD data cannot assess per-substrate co-culture effects; current interaction conclusions rely on the RFU-based competition assay. [^cf_formulation_design]

Engraftability was inferred from patient prevalence and transcriptional activity rather than measured after administration. Only 21 lung genomes across 5 species were available for lung-adaptation comparisons, and *M. luteus* had zero lung genomes and zero detected patient engraftability despite its central role in achieving 100% niche coverage. [^cf_formulation_design]

PA14-based inhibition measurements have not been validated against PAO1 or ExoS+ clinical strains, although the pangenome analysis found no amino-acid pathway differences between ExoU+ and ExoS+ PA. The report therefore prioritizes testing PAO1 and 3–5 mucoid clinical PA isolates. [^cf_formulation_design]

The primary *N. mucosa* conservation analysis used a 15-genome clade even though the PROTECT reference mapped to an 8-genome clade; the 8-genome sensitivity check showed stronger conservation, with 18/18 amino-acid pathways at >95% versus 16/18 in the 15-genome clade, 37/62 carbon pathways versus 27/62, and 1 respiratory genome. [^cf_formulation_design]

## Slots Into

- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — links substrate-specific growth, lag advantage, inhibition, engraftability, and PA lung adaptation to condition-dependent competitive fitness. [^cf_formulation_design]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — integrates inhibition, carbon utilization, growth kinetics, metagenomics, metatranscriptomics, and pangenome pathway predictions in formulation design. [^cf_formulation_design]
- [pangenome-integration](../concepts/pangenome-integration.md) — uses 499 commensal genomes and 1,796 lung PA genomes to assess pathway conservation, lung adaptation, and formulation robustness. [^cf_formulation_design]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — applies GapMind pathway completeness comparisons to identify metabolic gaps between PA14 and candidate commensals, including selective prebiotic targets. [^cf_formulation_design]
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — contributes pairwise inhibition and synergy measurements showing near-additive *N. mucosa* interactions and antagonistic pairs. [^cf_formulation_design]

[^cf_formulation_design]: [cf formulation design](../sources/cf_formulation_design__REPORT.md)
