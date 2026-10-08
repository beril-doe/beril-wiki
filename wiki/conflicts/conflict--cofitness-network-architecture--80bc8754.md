<!-- tension-hash: 80bc875463e3cae1 -->
# Process-Level Inference versus Gene-Level Functional Identity

Projects in the corpus that infer gene function from fitness data report outputs at different levels. Gene-level identity means assigning a specific KEGG Orthology (KO) term, a curated orthologous-gene function identifier, to a gene. Process-level inference places a gene within a biological process or yields a candidate role. One project scores fitness-based module methods against strict KO assignment and finds they fall short, while ortholog transfer scores highly [src: fitness_modules]. Other projects present dark-gene inferences as hypotheses rather than direct assignments [src: functional_dark_matter; truly_dark_genes], and donor inference as exploratory [src: gene_function_ecological_agora]. This matters for how the cofitness architecture in [[concepts/cofitness-network-architecture]] can be used. The open question is whether cofitness-derived signals should be read as weak gene-identity predictors or as a separate class of process-level evidence that no single benchmark captures.

## Evidence Sides

**Gene-level identity benchmark: process methods score near zero on strict KO precision**

Module-ICA (independent component analysis, which groups genes into co-varying fitness modules) and cofitness voting (assigning function from genes with correlated fitness profiles) each had <1% strict KEGG KO precision [src: fitness_modules]. Ortholog transfer, which carries annotations across sequence-homologous genes, achieved 95.8% precision, 91.2% coverage, and 0.934 F1 (a summary score combining prediction accuracy measures) [src: fitness_modules].

**Process and hypothesis-level outputs: inferences are framed as candidates, not assignments**

Functional-dark-matter results from GapMind (a pathway-gap annotation tool) and protein-domain analysis do not give direct gene-to-step assignments [src: functional_dark_matter; truly_dark_genes]. Neither do truly-dark-gene clues from eggNOG (an orthology-based annotation resource) or from phenotypes [src: functional_dark_matter; truly_dark_genes]. Both identify hypotheses [src: functional_dark_matter; truly_dark_genes]. The Agora's M26 tree-based donor inference, which infers the source lineage of acquired genes from phylogenetic trees, is described as exploratory rather than donor identification [src: gene_function_ecological_agora].

## Possible Reconciliations

- *Hypothesis:* The two sides measure different targets. Strict KO precision tests molecular-function identity. Process-level methods may carry valid information that this metric cannot score.
- *Hypothesis:* Process-level signals become gene-level evidence only when combined with independent sequence evidence, such as orthology or domains. Each alone stays at hypothesis level.
- *Hypothesis:* The low KO precision of Module-ICA and cofitness voting reflects real limits of fitness-based inference. If so, process framings in dark-gene and Agora work describe how far these methods actually reach, not a separate valid layer.

## Resolving Work

- **Data:** Fitness Browser genes with curated pathway membership but no strict KO. **Method:** score Module-ICA and cofitness voting with a process-level metric, such as pathway or module membership, instead of strict KO match. **Question:** do these methods perform better at the process level than at the KO level?
- **Data:** dark genes with GapMind or domain hypotheses. **Method:** targeted mutant phenotyping on predicted substrates or conditions. **Question:** what fraction of hypothesis-level calls resolve into direct gene-to-step assignments?
- **Data:** genes with both ortholog-transfer annotations and module membership. **Method:** stratify ortholog-transfer accuracy by module agreement. **Question:** does process-level concordance add precision beyond orthology?
- **Data:** M26 tree-based donor inferences. **Method:** compare against independent synteny (conserved gene order across genomes) or mobile-element evidence (genetic elements that move between genomic locations or organisms) for the same acquisitions. **Question:** can exploratory donor inference reach donor identification?
