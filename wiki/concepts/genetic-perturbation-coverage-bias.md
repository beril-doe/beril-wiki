---
type: Concept
description: Biases in which genes receive usable genetic perturbation phenotypes
sources:
- id: adp1_deletion_phenotypes
  resource: ../summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: core_gene_tradeoffs
  resource: ../summaries/core_gene_tradeoffs__REPORT.md
  title: core gene tradeoffs
- id: fitness_effects_conservation
  resource: ../summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: costly_dispensable_genes
  resource: ../summaries/costly_dispensable_genes__REPORT.md
  title: costly dispensable genes
title: Perturbation-Collection Coverage Bias
---
# Perturbation-Collection Coverage Bias

Perturbation collections can overrepresent genes that are conserved, annotated, and successfully recoverable as mutants, while underrepresenting less-conserved or poorly annotated genes. [^adp1_deletion_phenotypes] The broader Fitness Browser comparison supports this concern: across approximately 194,000 genes from 43 bacteria, essential genes were 82% core whereas always-neutral genes were 66% core, although fitness importance was only a weak predictor of conservation. [^fitness_effects_conservation]

This pattern matters for interpreting [gene-essentiality](gene-essentiality.md) and [condition-specific-fitness](condition-specific-fitness.md): apparent functional coverage may reflect which genes enter the perturbation collection rather than the full genomic distribution of gene functions. [^adp1_deletion_phenotypes] Evidence that core genes can themselves be conditionally burdensome **refines** this interpretation: core status is not equivalent to uniformly low burden or universal essentiality. In the broader Fitness Browser analysis, core genes were more burdensome than non-core genes in several functional categories, and 25,271 genes were classified as condition-dependent trade-offs; these findings are based on laboratory fitness and conservation patterns rather than direct measurement of natural selection. [^core_gene_tradeoffs] The new comparison further **supports** this refinement: core genes showed heavier tails in both negative and positive fitness effects, and 24.4% were ever beneficial versus 19.9% of auxiliary genes. [^fitness_effects_conservation]

## Evidence from the ADP1 deletion collection

The analysis compared a complete growth matrix of 2,034 genes across 8 carbon sources with TnSeq, or transposon sequencing, essentiality classifications and pangenome annotations. [^adp1_deletion_phenotypes]

Among 2,593 TnSeq-dispensable genes, 272 (10.5%) lacked growth data from the deletion collection, whereas 2,321 had growth data. [^adp1_deletion_phenotypes] The genes missing from the deletion collection had a mean length of 813 bp, compared with 981 bp for present dispensable genes. [^adp1_deletion_phenotypes] Missing genes were RAST annotated at 91% versus 100% for present dispensable genes and KO annotated at 49% versus 59%. [^adp1_deletion_phenotypes] The missing genes were also less likely to be pangenome-core: 76.5% were core compared with 93.3% of present dispensable genes, a difference with p = 1.4×10⁻²⁰. [^adp1_deletion_phenotypes]

These results support the interpretation that deletion-collection coverage is biased toward more conserved genes, as measured by species-level pangenome core status, and toward genes with stronger functional annotation. [^adp1_deletion_phenotypes] The broader conservation–fitness gradient **supports** the direction of this association while showing that it is not deterministic: genes affecting 20+ experiments were 79% core, compared with 66% for genes with 0 experiments, with Spearman rho=0.086 and p=8.1e-230. [^fitness_effects_conservation] The core-gene trade-off analysis **refines** the meaning of this bias by showing that conserved genes can have strong condition-specific fitness effects rather than forming a uniformly inert or universally essential class. [^core_gene_tradeoffs]

The cross-organism costly–dispensable analysis **supports** the annotation and conservation concern: among 142,190 genes from 43 bacteria, costly+dispensable genes had SEED annotation rates of 50.8% versus 74.9% for costly+conserved genes and KEGG annotation rates of 20.0% versus 42.7%; 44.5% were orphans with no ortholog group, compared with 13.1% of costly+conserved genes. [^costly_dispensable_genes] It also **refines** the interpretation by showing that the poorly annotated, narrowly distributed group is enriched for mobile-element signatures rather than being simply a random collection of uncharacterized genes: mobile-element keywords were 7.45x more likely in costly+dispensable than costly+conserved genes (OR=7.45, p=4.6e-71). [^costly_dispensable_genes] This result characterizes the genes most vulnerable to coverage or interpretation bias but does not itself measure mutant-recovery probability. [^costly_dispensable_genes]

## Annotation bias and uncertain genes

Hypothetical proteins were enriched among genes missing from the deletion collection: 25 were completely unannotated, with q = 2.4×10⁻²⁵, and 48 were annotated as “hypothetical protein,” with q = 3.0×10⁻⁴. [^adp1_deletion_phenotypes]

The 313 uncertain-class genes had a mean length of 361 bp, 42% annotation coverage, and 31% pangenome-core status, a profile the report considers consistent with gene fragments or pseudogenes rather than true essential genes. [^adp1_deletion_phenotypes]

This annotation pattern connects coverage bias to [functional-dark-matter](functional-dark-matter.md): poorly characterized genes are not merely difficult to interpret after perturbation, but may also be less likely to have usable perturbation phenotypes in the first place. [^adp1_deletion_phenotypes] The Fitness Browser analysis **supports** retaining this caution: novel singleton genes showed near-zero mean fitness under the tested laboratory conditions, but the report notes that apparent neutrality may reflect poor transposon coverage rather than biological inactivity. [^fitness_effects_conservation] The costly–dispensable analysis **refines** this caution: 24.2% of costly+dispensable genes were singletons, while no costly+conserved genes were singletons, but within the dispensable category costly genes were only slightly more likely than neutral genes to be singletons (OR=1.09, p=0.02); the report also notes that the first comparison is partly structural because core genes cannot be singletons by definition. [^costly_dispensable_genes]

## Consequences for inference

The deletion matrix excludes 499 essential genes and 316 genes with incomplete data, so its condition-specific fitness landscape is biased toward dispensable genes with successful deletion mutants. [^adp1_deletion_phenotypes]

The report therefore supports using perturbation results together with pangenome and annotation data, rather than treating the assayed gene set as an unbiased sample of the genome. [^adp1_deletion_phenotypes] This **supports** separating collection coverage from biological interpretation of fitness: the core-gene analysis found 28,017 Costly + Conserved genes, indicating that conservation and laboratory burden can coexist, although the result does not directly measure selection in nature. [^core_gene_tradeoffs] The broader analysis **refines** this consequence by finding that strong condition-specific effects were enriched among core genes, with 77.3% of genes tagged with strong specific phenotypes core versus 70.3% without them. [^fitness_effects_conservation] Likewise, 14.1% of costly+dispensable genes had condition-specific phenotypes, compared with 16.7% of costly+conserved genes and 2.7% of neutral+dispensable genes, suggesting that some poorly conserved genes can remain phenotypically informative under particular laboratory conditions. [^costly_dispensable_genes]

The conservation comparison is informative but limited because core/accessory status came from BERDL’s species-level *Acinetobacter baylyi* pangenome and may have less resolution than a population-level analysis. [^adp1_deletion_phenotypes] This limitation refines [pangenome-integration](pangenome-integration.md): pangenome status can diagnose collection bias, but its interpretation depends on the taxonomic and population scale of the reference pangenome. [^adp1_deletion_phenotypes] The Fitness Browser comparison adds a distinct generalizability limitation: its measurements were biased toward rich media and standard stresses, covered 43 bacteria primarily from Proteobacteria, and used single-gene knockouts that did not capture epistatic interactions. [^fitness_effects_conservation]

## Tensions

The observed association between perturbation coverage, annotation, and pangenome-core status could reflect biological conservation, technical difficulty in constructing or measuring mutants, misclassified gene fragments, or some combination of these factors. [^adp1_deletion_phenotypes] The report does not establish which mechanism causes the missing-data pattern, so the association should not be interpreted as proof that evolutionary conservation directly determines deletion-mutant recovery. [^adp1_deletion_phenotypes]

The ADP1 collection indicates that successful coverage is enriched among core genes, whereas the broader trade-off analysis shows that core genes can carry substantial laboratory burden and condition-specific costs. This is not a direct contradiction because the studies measure different outcomes, but it creates a boundary on interpretation: core enrichment in a collection cannot by itself establish either low burden or universal essentiality. [^adp1_deletion_phenotypes][^core_gene_tradeoffs] The Fitness Browser result that singleton genes were near-neutral under tested conditions creates a related interpretive tension: neutrality may represent genuine lack of measured effect or inadequate transposon coverage, and the analysis does not distinguish these explanations. [^fitness_effects_conservation]

The costly–dispensable analysis adds a related boundary rather than resolving this tension: its classification of burden used max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and the result is sensitive to fitness-data noise; its 90% identity DIAMOND threshold may also miss recently acquired genes with low sequence similarity. [^costly_dispensable_genes] Thus, mobile-element enrichment and poor annotation narrow the biological interpretation of costly non-conserved genes toward horizontally acquired DNA, but do not establish that such genes are systematically absent from perturbation collections. [^costly_dispensable_genes]

## Source

The underlying analysis is summarized in [adp1_deletion_phenotypes__REPORT](../summaries/adp1_deletion_phenotypes__REPORT.md). [^adp1_deletion_phenotypes]

The integrated conservation–fitness evidence is summarized in [core_gene_tradeoffs__REPORT](../summaries/core_gene_tradeoffs__REPORT.md). [^core_gene_tradeoffs]

The broader Fitness Browser comparison is summarized in [fitness_effects_conservation__REPORT](../summaries/fitness_effects_conservation__REPORT.md). [^fitness_effects_conservation]

The costly–dispensable gene analysis is summarized in [costly_dispensable_genes__REPORT](../summaries/costly_dispensable_genes__REPORT.md). [^costly_dispensable_genes]

## Open Directions

- Re-sequence and re-annotate the 272 TnSeq-dispensable genes lacking deletion-collection growth data, then test whether annotation updates explain their missing perturbation phenotypes. [^adp1_deletion_phenotypes]
- Compare deletion-mutant construction success and phenotype completeness against gene length, annotation status, pangenome frequency, and pseudogene indicators using a multivariable logistic model to separate technical and evolutionary predictors of coverage. [^adp1_deletion_phenotypes]
- Replace the species-level core/accessory labels with population-level pangenome frequencies and test whether the coverage association remains after controlling for gene fragments and uncertain classifications. [^adp1_deletion_phenotypes]
- Add the 316 genes with incomplete data and the 499 excluded essential genes where technically possible, then repeat condition-specific fitness analyses to quantify how collection composition changes the inferred essentiality landscape. [^adp1_deletion_phenotypes]
- Stratify coverage analyses by functional category and condition, then test whether the observed core-gene burden pattern persists after accounting for which genes are recoverable in the deletion collection. [^core_gene_tradeoffs]
- Reassess singleton neutrality with coverage-aware models and perturbation assays spanning non-rich-media conditions, testing whether missing transposon coverage or unmeasured ecological conditions explain the apparent lack of fitness effects. [^fitness_effects_conservation]
- Test whether the costly+dispensable mobile-element and annotation profile predicts failed mutant construction or incomplete phenotype coverage after controlling for gene length, orthology breadth, and organism. [^costly_dispensable_genes]

[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../summaries/adp1_deletion_phenotypes__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../summaries/fitness_effects_conservation__REPORT.md)
[^core_gene_tradeoffs]: [core gene tradeoffs](../summaries/core_gene_tradeoffs__REPORT.md)
[^costly_dispensable_genes]: [costly dispensable genes](../summaries/costly_dispensable_genes__REPORT.md)
