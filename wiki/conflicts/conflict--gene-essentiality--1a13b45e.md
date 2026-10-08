<!-- tension-hash: 1a13b45e4288ee34 -->
# How Well Do Computational Predictors Recover Gene Essentiality and Function?

Projects in this corpus disagree about how far computational predictors can stand in for measured gene essentiality or function. In one organism, flux balance analysis (FBA, a constraint-based metabolic-modeling method) showed moderate concordance with knockout outcomes [src: adp1_triple_essentiality]. Across many organisms and carbon sources, baseline FBA accuracy was low [src: annotation_gap_discovery], and FBA lacked mappings for many genes in one gene network [src: discoveries]. A parallel split appears in function prediction, where a co-regulation method performs very differently from ortholog transfer [src: fitness_modules]. This matters for [[concepts/gene-essentiality]] because the corpus treats modeling, annotation and conservation as predictors rather than definitions of essentiality. How much weight each predictor deserves depends on which result generalizes.

## Evidence Sides

**Side A: some computational predictors perform well against their own evaluation targets**

- In *Acinetobacter baylyi* ADP1, FBA showed moderate concordance with experimental knockout phenotypes [src: adp1_triple_essentiality].
- Module-ICA (independent component analysis applied to fitness data to define co-regulated gene modules) is backed by strong cofitness, meaning correlated mutant fitness across experiments [src: fitness_modules].
- Ortholog transfer (assigning function to a gene from its characterized orthologs) reached 95.8% strict KO precision, where precision is the fraction of predictions that are correct and KO is a KEGG Orthology functional assignment [src: fitness_modules].

**Side B: computational predictors fail broadly or systematically**

- Annotation-gap analysis found 42.5% baseline FBA accuracy across 574 organism–carbon-source combinations [src: annotation_gap_discovery].
- FBA lacked mappings for 30/51 aromatic-network genes [src: discoveries].
- FBA predicted 0% Complex I (the first enzyme complex of the respiratory chain) essentiality despite 1.76× higher aromatic flux [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules].
- Module-ICA had <1% strict KO precision despite strong cofitness [src: fitness_modules].

## Possible Reconciliations

- **Hypothesis 1: different prediction targets.** The tension record itself frames the gap this way. Knockout concordance, growth or no-growth on a carbon source, and molecular-function (KO) assignment are different targets. On this view the results do not form a biological contradiction [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules].
- **Hypothesis 2: model and annotation coverage.** FBA may agree with knockouts for genes that the model maps. It may fail where genes have no reaction mappings, as with the 30/51 unmapped aromatic-network genes [src: discoveries]. If so, aggregate accuracy would reflect annotation completeness rather than the method's validity.
- **Hypothesis 3: single-organism versus multi-organism scope.** The moderate ADP1 concordance comes from a single organism [src: adp1_triple_essentiality]. The 42.5% figure spans 574 combinations [src: annotation_gap_discovery]. Organism-specific model curation could account for the difference. This remains untested here.

## Resolving Work

- Stratify ADP1 knockout concordance by whether each gene has an FBA reaction mapping. This asks whether concordance collapses for unmapped genes.
- Rescore the multi-organism FBA comparison against gene-level knockout or TnSeq (transposon sequencing) essentiality instead of carbon-source growth. This asks whether low growth-prediction accuracy coexists with moderate gene-level concordance.
- Assign reactions, where annotation allows, to the 30/51 aromatic-network genes lacking FBA mappings [src: discoveries], then rerun FBA. This asks whether the 0% Complex I essentiality prediction, made despite 1.76× higher aromatic flux, changes [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules].
- Evaluate Module-ICA against process-level labels such as pathway membership instead of strict KO identity. This asks whether its strong cofitness signal predicts biological process even where strict KO precision is <1% [src: fitness_modules].
