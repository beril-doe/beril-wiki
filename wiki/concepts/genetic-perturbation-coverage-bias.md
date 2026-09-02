---
type: "Concept"
description: "Perturbation datasets overrepresent conserved and well-annotated genes"
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md"]
---
# Perturbation-Collection Coverage Bias

Perturbation collections can overrepresent genes that are conserved, annotated, and successfully recoverable as mutants, while underrepresenting less-conserved or poorly annotated genes. [src: adp1_deletion_phenotypes]

This pattern matters for interpreting [[concepts/gene-essentiality]] and [[concepts/condition-specific-fitness]]: apparent functional coverage may reflect which genes enter the perturbation collection rather than the full genomic distribution of gene functions. [src: adp1_deletion_phenotypes]

## Evidence from the ADP1 deletion collection

The analysis compared a complete growth matrix of 2,034 genes across 8 carbon sources with TnSeq, or transposon sequencing, essentiality classifications and pangenome annotations. [src: adp1_deletion_phenotypes]

Among 2,593 TnSeq-dispensable genes, 272 (10.5%) lacked growth data from the deletion collection, whereas 2,321 had growth data. [src: adp1_deletion_phenotypes]

The genes missing from the deletion collection had a mean length of 813 bp, compared with 981 bp for present dispensable genes. [src: adp1_deletion_phenotypes]

Missing genes were RAST annotated at 91% versus 100% for present dispensable genes and KO annotated at 49% versus 59%. [src: adp1_deletion_phenotypes]

The missing genes were also less likely to be pangenome-core: 76.5% were core compared with 93.3% of present dispensable genes, a difference with p = 1.4×10⁻²⁰. [src: adp1_deletion_phenotypes]

These results support the interpretation that deletion-collection coverage is biased toward more conserved genes, as measured by species-level pangenome core status, and toward genes with stronger functional annotation. [src: adp1_deletion_phenotypes]

## Annotation bias and uncertain genes

Hypothetical proteins were enriched among genes missing from the deletion collection: 25 were completely unannotated, with q = 2.4×10⁻²⁵, and 48 were annotated as “hypothetical protein,” with q = 3.0×10⁻⁴. [src: adp1_deletion_phenotypes]

The 313 uncertain-class genes had a mean length of 361 bp, 42% annotation coverage, and 31% pangenome-core status, a profile the report considers consistent with gene fragments or pseudogenes rather than true essential genes. [src: adp1_deletion_phenotypes]

This annotation pattern connects coverage bias to [[concepts/functional-dark-matter]]: poorly characterized genes are not merely difficult to interpret after perturbation, but may also be less likely to have usable perturbation phenotypes in the first place. [src: adp1_deletion_phenotypes]

## Consequences for inference

The deletion matrix excludes 499 essential genes and 316 genes with incomplete data, so its condition-specific fitness landscape is biased toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]

The report therefore supports using perturbation results together with pangenome and annotation data, rather than treating the assayed gene set as an unbiased sample of the genome. [src: adp1_deletion_phenotypes]

The conservation comparison is informative but limited because core/accessory status came from BERDL’s species-level *Acinetobacter baylyi* pangenome and may have less resolution than a population-level analysis. [src: adp1_deletion_phenotypes]

This limitation refines [[concepts/pangenome-integration]]: pangenome status can diagnose collection bias, but its interpretation depends on the taxonomic and population scale of the reference pangenome. [src: adp1_deletion_phenotypes]

## Tensions

The observed association between perturbation coverage, annotation, and pangenome-core status could reflect biological conservation, technical difficulty in constructing or measuring mutants, misclassified gene fragments, or some combination of these factors. [src: adp1_deletion_phenotypes]

The report does not establish which mechanism causes the missing-data pattern, so the association should not be interpreted as proof that evolutionary conservation directly determines deletion-mutant recovery. [src: adp1_deletion_phenotypes]

## Source

The underlying analysis is summarized in [[summaries/adp1_deletion_phenotypes__REPORT]]. [src: adp1_deletion_phenotypes]

## Open Directions

- Re-sequence and re-annotate the 272 TnSeq-dispensable genes lacking deletion-collection growth data, then test whether annotation updates explain their missing perturbation phenotypes. [src: adp1_deletion_phenotypes]
- Compare deletion-mutant construction success and phenotype completeness against gene length, annotation status, pangenome frequency, and pseudogene indicators using a multivariable logistic model to separate technical and evolutionary predictors of coverage. [src: adp1_deletion_phenotypes]
- Replace the species-level core/accessory labels with population-level pangenome frequencies and test whether the coverage association remains after controlling for gene fragments and uncertain classifications. [src: adp1_deletion_phenotypes]
- Add the 316 genes with incomplete data and the 499 excluded essential genes where technically possible, then repeat condition-specific fitness analyses to quantify how collection composition changes the inferred essentiality landscape. [src: adp1_deletion_phenotypes]
