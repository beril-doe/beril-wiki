---
title: Schema-Dependent Functional Inference
type: Topic
sources:
- id: cog_analysis
  resource: ../../wiki/summaries/cog_analysis__REPORT.md
  title: cog analysis
- id: discoveries
  resource: ../../wiki/summaries/discoveries.md
  title: discoveries
- id: plant_microbiome_ecotypes
  resource: ../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: ecotype_functional_differentiation
  resource: ../../wiki/summaries/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
- id: webofmicrobes_explorer
  resource: ../../wiki/summaries/webofmicrobes_explorer__REPORT.md
  title: webofmicrobes explorer
- id: fitness_effects_conservation
  resource: ../../wiki/summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: core_gene_tradeoffs
  resource: ../../wiki/summaries/core_gene_tradeoffs__REPORT.md
  title: core gene tradeoffs
---
# Schema-Dependent Functional Inference

Schema-dependent functional inference is the process of translating genes, pathways, metabolites, phenotypes, and ecological observations into categories that can be compared biologically. The corpus shows that these categories are not neutral containers: ontology choice, annotation system, identifier mapping, composite-label handling, feature namespace, and cohort representation can change what counts as a signal. This topic therefore asks not only whether a biological pattern is statistically detectable, but whether the pattern remains interpretable when the schema used to measure it changes.

## Literature Context

Published work has established that functional inference is inseparable from the resources and software used to represent biological sequence data. eggNOG 5.0 provides hierarchical orthology, functional, and phylogenetic annotations across 5,090 organisms and 2,502 viruses, making large-scale comparison possible while also exposing the importance of orthology boundaries and annotation depth ([PMID 30418610](https://pubmed.ncbi.nlm.nih.gov/30418610/)). More broadly, the literature frames microbiome functional analysis as an exercise in adapting and combining tools originally developed for other purposes, rather than applying a single universally neutral pipeline ([PMID 33422152](https://pubmed.ncbi.nlm.nih.gov/33422152/)). Recent reviews likewise emphasize interoperability among bioinformatics tools, digital resources, and emerging data types as a central challenge for interpreting complex microbial datasets ([PMID 41297621](https://pubmed.ncbi.nlm.nih.gov/41297621/)).

This literature is consistent with the corpus’s finding that annotation coverage, identifier mapping, ontology choice, and marker definition alter the measurable biological question. The corpus extends the resource-centered perspective by quantifying how sharply conclusions can change: eggNOG and Bakta differed in coverage across COG, KEGG, Pfam, GO, product descriptions, and UniRef50, while their union rescued additional gene clusters. Its examples of regex-based versus MetaCyc pathway categorization, and of generic KOs versus validated lanthanide-related markers, provide concrete demonstrations that a statistically coherent result can still be schema-dependent. MEGARes 2.0 similarly illustrates the value of purpose-built, curated classification for antimicrobial, biocide, and metal-resistance determinants, supporting the corpus’s caution that broad identifiers should be treated as candidate evidence rather than definitive functional assignments ([PMID 31722416](https://pubmed.ncbi.nlm.nih.gov/31722416/)). The corpus’s treatment of composite COG labels extends this point beyond database selection: preserving multi-label assignments can retain biological relationships that exclusive or split-category representations may erase.

The corpus also sits within an emerging shift from isolated annotation databases toward integrated, metadata-aware infrastructures. Microbiome Datahub is described as an open-access platform combining environmental metadata, taxonomy, and functional annotation for metagenome-assembled genome datasets ([PMID 41840729](https://pubmed.ncbi.nlm.nih.gov/41840729/)). Consistent with that direction, the corpus shows that ecological comparison depends on sampling process, cohort representation, measurement scale, and feature namespace—not annotation alone. Its cross-cohort metabolomics and MetaPhlAn3/Kaiju projection examples extend published concerns into an explicit portability problem: pooled or high-confidence models may encode cohort or namespace structure rather than transferable biology. The particularly novel contribution is therefore not simply the claim that tools differ, which is established, but the integration of ontology sensitivity, composite annotations, statistical effect-size interpretation, and cross-cohort transfer into one evidential framework. In tension with analyses that may treat functional labels as stable inputs, the corpus argues that reproducible functional inference requires testing whether biological conclusions survive deliberate changes in schema and representation.

## What the Corpus Shows

**The representation defines the measurable biological question.**  
A biological object can occupy different measurable spaces depending on how it is annotated or categorized. In the 32-species COG comparison, COG annotations covered approximately 70% of genes, and the analysis used eggNOG v6 annotations that may differ from original COG assignments. [^cog_analysis] Thus, an apparent absence of a function may mean that the gene was unassigned, assigned under another database convention, or genuinely lacked the function; the analysis cannot distinguish these possibilities without independent evidence. [^cog_analysis]

The broader annotation comparison makes this dependence explicit. Across 132.5M gene clusters, eggNOG had higher COG coverage at 51% versus 8.2% for Bakta, higher KEGG coverage at 38.5% versus 17.3%, and higher Pfam coverage at 63% versus 7.7%; Bakta had higher GO coverage at 15% versus 7.4%, product-description coverage at 71.2% versus 70.4%, and unique UniRef50 links covering 79.2%. [^discoveries] Their union increased any-functional-annotation coverage to 77.3%, while Bakta rescued 11.2M clusters among 39.2M missed by eggNOG. [^discoveries] These results mean that “functional absence” is partly a property of annotation coverage and identifier linkage, not necessarily of biology. [^discoveries]

This concern extends to ecological and taxonomic comparisons. Pangenome-derived plant genera and MGnify rhizosphere genera had only 11.7% Jaccard overlap because isolation metadata and metagenomic detection measured different phenomena. [^plant_microbiome_ecotypes] A comparison can therefore fail before statistical testing if apparently equivalent feature sets were generated by different sampling processes.

**Ontology and category definitions can create or erase biological themes.**  
In an inflammatory-bowel-disease pathway analysis, a regex-based category scheme identified 3 of 52 CD-up pathways in 7 themes and produced a structurally degenerate result. [^discoveries] A MetaCyc hierarchy assigned 262/409 pathways to at least one of 12 IBD themes and supported iron/heme acquisition with OR=8.1, FDR=7e-6, and 15/52 CD-up pathways. [^discoveries] Here, a curator-validated hierarchy means an ontology whose parent-child relationships and pathway membership are biologically curated, whereas a regex scheme assigns categories from textual name matching. [^discoveries] The difference shows that a conclusion about pathway-level biology can be a consequence of category construction rather than a stable property of the underlying pathway results. [^discoveries]

Marker definitions are similarly consequential. An eggNOG preferred-name query for `lanM` produced 505 additional hits with zero overlap with 62 Bakta-validated Lanmodulin genomes. [^discoveries] eggNOG KO K02030 produced 46,369 nonspecific hits, while only 418 of 5,092 genomes with any xoxF marker hit both eggNOG K00114 and Bakta lanthanide-dependent methanol-dehydrogenase products. [^discoveries] These results support treating generic KOs, preferred names, and product descriptions as candidate evidence rather than definitive functional markers. [^discoveries]

**Multi-label and composite annotations preserve relationships that exclusive categories lose.**  
A composite COG annotation is an assignment containing multiple functional letters. The corpus retained such assignments as single biological categories rather than splitting them into independent counts. [^cog_analysis] This matters because a gene assigned LV can represent linked mobile and defense functions, whereas splitting it into L and V may imply two unrelated observations. [^cog_analysis]

Across 32 species spanning 9 phyla and 357,623 genes, the LV composite showed +0.34% enrichment in novel or singleton genes, with 76% consistency across species. [^cog_analysis] The result was interpreted as consistent with multifunctional modules such as mobile defense islands, while acknowledging that annotation conventions may contribute to the pattern. [^cog_analysis] Preserving the composite therefore gives an intermediate resolution: more informative than one undifferentiated label, but less presumptive than treating every component as independent evidence. [^cog_analysis]

The same principle appears in ecotype comparisons. Within-species gene-content ecotypes differed in both adaptive and housekeeping COG categories, but adaptive categories had a mean effect size of 0.0136 versus 0.0064 for housekeeping categories, a 2.13x ratio, with p = 2.53 x 10^-6 for the distributional comparison. [^ecotype_functional_differentiation] Effect size describes the magnitude of a difference, whereas statistical significance tests whether the observation is unlikely under a specified null hypothesis. [^ecotype_functional_differentiation] Because housekeeping categories were also significant in 33 of 48 tests, or 68.8%, the schema supports a stronger adaptive contrast in magnitude, not an absolute adaptive-versus-housekeeping separation. [^ecotype_functional_differentiation]

**Statistical strength does not rescue an unstable schema.**  
The ecotype-functional analysis covered 257 chi-square or Fisher’s exact tests across 12 species and 23 COG categories; 170 tests, or 66.1%, were significant after Benjamini–Hochberg false-discovery-rate correction at q < 0.05. [^ecotype_functional_differentiation] Yet the report characterizes the effect sizes as small and notes that significance may partly reflect the sample size of 1,820 genomes. [^ecotype_functional_differentiation] The largest mean effect sizes were instead observed for S, unknown function, at 0.0392, and L, replication, recombination, and repair, at 0.0337, outside the predefined adaptive set. [^ecotype_functional_differentiation] A schema that predefines adaptive and housekeeping groups can therefore organize interpretation, but it should not be mistaken for a complete partition of biological importance.

Functional labels also interact with evolutionary classes. Novel or singleton genes were enriched in COG L by +10.88% and COG V by +2.83%, while core genes were depleted in translation J by -4.65%, nucleotide metabolism F by -2.09%, coenzyme metabolism H by -2.06%, amino-acid metabolism E by -1.81%, and energy production C by -1.75%. [^cog_analysis] These are core-versus-novel comparisons, not within-species ecotype contrasts, so transferring the interpretation from one schema or comparison to another would overstate the evidence. [^cog_analysis]

**Portability depends on compatible representation, not only classifier quality.**  
Cross-cohort analyses show that a model can perform well in pooled data while learning the cohort or measurement schema. Pooling HMP2 and Franzosa metabolomics on 122 m/z-bridge metabolites produced K=4 clustering that separated completely by cohort rather than diagnosis; the first principal component explained 79% of variance, and leave-one-study-out adjusted Rand index was 0.000 for metabolomics versus 0.113 for taxonomic ecotypes. [^discoveries] Relative-abundance features transferred more robustly because they were unitless and compositional, whereas absolute-intensity metabolomics required explicit correction such as ComBat, surrogate variable analysis, RUV, or quantile normalization. [^discoveries]

Namespace changes can also alter biological assignments. Linear discriminant analysis projection across MetaPhlAn3 and Kaiju namespaces produced Kuehl proportions of 27/42/31% across ecotypes, whereas centered log-ratio plus principal-component Gaussian-mixture projection assigned all 26 Kuehl samples to E3 at confidence greater than 0.97; Kuehl detected only 54% of the training species. [^discoveries] The apparent confidence was therefore compatible with missing feature coverage rather than reliable ecological classification. [^discoveries] Similarly, among 257 identified Web of Microbes compounds, 69, or 26.8%, had definitive ModelSEED links, while formula-only matching yielded 107 compounds expanding to 900 candidate molecules. [^webofmicrobes_explorer] Match confidence and namespace harmonization are consequently part of the biological inference, not merely implementation details. [^webofmicrobes_explorer]

## Tensions and Caveats

A central tension is whether observed functional differentiation reflects adaptive biology or lineage structure. All 12 species with valid ecotype clusters had at least one differentiated COG category, but approximately 38% of gene clusters had COG annotations, and the analysis lacked within-species phylogenetic controls. [^ecotype_functional_differentiation] The result supports non-random functional structure while leaving its ecological attribution unresolved. [^ecotype_functional_differentiation] This is the key issue in [conflict--bacdive_phenotype_metal_tolerance--ecotype_analysis--ecotype_functional_differentiation--d8143c37](../conflicts/conflict--bacdive_phenotype_metal_tolerance--ecotype_analysis--ecotype_functional_differentiation--d8143c37.md) and [conflict--ecotype_analysis--ecotype_env_reanalysis--ecotype_functional_differentiation--57f3758f](../conflicts/conflict--ecotype_analysis--ecotype_env_reanalysis--ecotype_functional_differentiation--57f3758f.md).

A second tension concerns whether conserved or “core” functions can be inferred to be uniformly important or low-cost. Across approximately 194,000 genes from 43 bacteria, essential genes were 82% core whereas always-neutral genes were 66% core, but the association was weak overall. [^fitness_effects_conservation] Core genes also had heavier fitness-effect tails in both negative and positive directions, and core genes were more burdensome in some categories while non-core genes were more burdensome in Cell Wall functions. [^core_gene_tradeoffs] These findings prevent “core,” “housekeeping,” “essential,” and “low burden” from being used as interchangeable labels; the disagreement is anchored in [conflict--acinetobacter_adp1_explorer--adp1_triple_essentiality--alphafold_msa_annotation--8af84dcc](../conflicts/conflict--acinetobacter_adp1_explorer--adp1_triple_essentiality--alphafold_msa_annotation--8af84dcc.md) and [conflict--adp1_deletion_phenotypes--core_gene_tradeoffs--costly_dispensable_genes--470fcab9](../conflicts/conflict--adp1_deletion_phenotypes--core_gene_tradeoffs--costly_dispensable_genes--470fcab9.md).

Finally, model agreement is endpoint-dependent. In FW300-N2E3, GapMind showed 13/13 concordance and Fitness Browser 21/21, whereas BacDive showed 3/7 concordance. [^webofmicrobes_explorer] Such results support useful agreement in particular organisms, media, and endpoints, but they do not establish that predicted capability equals utilization, dependency, production, or activity. [^webofmicrobes_explorer] The broader model-versus-phenotype limitation is represented by [conflict--acinetobacter_adp1_explorer--adp1_triple_essentiality--annotation_gap_discovery--8f009ad9](../conflicts/conflict--acinetobacter_adp1_explorer--adp1_triple_essentiality--annotation_gap_discovery--8f009ad9.md).

## Where to Go Deeper

- [ontology-and-category-schema-sensitivity](../../wiki/concepts/ontology-and-category-schema-sensitivity.md) — start here for direct examples of pathway, marker, ontology, and identifier choices changing biological conclusions.
- [composite-functional-annotation](../../wiki/concepts/composite-functional-annotation.md) — examine why multi-label COG assignments should sometimes remain intact.
- [adaptive-versus-housekeeping-functional-differentiation](../../wiki/concepts/adaptive-versus-housekeeping-functional-differentiation.md) — follow the distinction between statistical significance and biological effect size in ecotype comparisons.
- [cross-cohort-microbiome-portability](../../wiki/concepts/cross-cohort-microbiome-portability.md) — assess how feature namespaces, measurement scales, and annotation coverage affect transfer across cohorts.

Key entities: [cog-functional-categories](../../wiki/entities/cog-functional-categories.md), [eggnog](../../wiki/entities/eggnog.md), [gapmind](../../wiki/entities/gapmind.md), [kbase-ke-pangenome](../../wiki/entities/kbase-ke-pangenome.md), [kescience-fitnessbrowser](../../wiki/entities/kescience-fitnessbrowser.md), [tnseq](../../wiki/entities/tnseq.md).

Project reports: discoveries__REPORT, [cog_analysis__REPORT](../../wiki/summaries/cog_analysis__REPORT.md), [ecotype_functional_differentiation__REPORT](../../wiki/summaries/ecotype_functional_differentiation__REPORT.md), [plant_microbiome_ecotypes__REPORT](../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md), [webofmicrobes_explorer__REPORT](../../wiki/summaries/webofmicrobes_explorer__REPORT.md), [fitness_effects_conservation__REPORT](../../wiki/summaries/fitness_effects_conservation__REPORT.md).

[^cog_analysis]: [cog analysis](../../wiki/summaries/cog_analysis__REPORT.md)
[^discoveries]: [discoveries](../../wiki/summaries/discoveries.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md)
[^ecotype_functional_differentiation]: [ecotype functional differentiation](../../wiki/summaries/ecotype_functional_differentiation__REPORT.md)
[^webofmicrobes_explorer]: [webofmicrobes explorer](../../wiki/summaries/webofmicrobes_explorer__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../../wiki/summaries/fitness_effects_conservation__REPORT.md)
[^core_gene_tradeoffs]: [core gene tradeoffs](../../wiki/summaries/core_gene_tradeoffs__REPORT.md)
