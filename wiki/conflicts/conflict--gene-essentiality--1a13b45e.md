<!-- tension-hash: 1a13b45e4288ee34 -->
# Does Model-Based Prediction of Gene Essentiality Hold Up? Single-Organism Concordance Against Corpus-Scale Accuracy and Coverage Gaps

Projects in this corpus disagree about how much weight metabolic models and correlation-based modules deserve as predictors of gene essentiality. One project reports that flux balance analysis (FBA — constraint-based simulation of metabolic fluxes from a genome-scale model) shows moderate agreement with knockout data in a single curated organism [src: adp1_triple_essentiality]; another reports 42.5% baseline FBA accuracy across 574 organism–carbon-source combinations, with whole subsystems left unmapped by the model [src: annotation_gap_discovery]. A third contrasts a module-based predictor at <1% strict knockout (KO) precision against 95.8% for ortholog transfer [src: fitness_modules]. The disagreement matters because it determines whether model-derived essentiality calls can substitute for direct perturbation on [[concepts/gene-essentiality]], or only supplement it.

## Evidence Sides

**FBA is a usable essentiality predictor in a well-characterized organism.** *Acinetobacter baylyi* ADP1 showed moderate FBA–knockout concordance, i.e. model-predicted essential genes overlapped experimentally measured knockout phenotypes at an intermediate level rather than agreeing or failing outright [src: adp1_triple_essentiality]. This is single-organism evidence, from an organism with a mature model and experimental knockout collection.

**Across many organisms and carbon sources, baseline FBA accuracy is low and structurally incomplete.** Annotation-gap analysis found 42.5% baseline FBA accuracy across 574 organism–carbon-source combinations [src: annotation_gap_discovery]. A coverage failure compounds the accuracy failure: FBA lacked reaction mappings for 30 of 51 aromatic-network genes [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules]. A gene the model cannot represent cannot be called essential by it, so part of this deficit is missing model structure rather than a measured absence of phenotype.

**The module-versus-ortholog precision gap is a target mismatch, not a contradiction.** Module-ICA (independent component analysis over fitness profiles, grouping genes by co-regulation) achieved <1% strict KO precision despite strong cofitness, against 95.8% for ortholog transfer (assigning function from a sequence-orthologous gene) [src: fitness_modules]. These are different prediction targets rather than a biological contradiction [src: discoveries].

## Possible Reconciliations

- **Hypothesis: the split is model-curation depth, not method validity.** ADP1's moderate concordance may reflect a curated model [src: adp1_triple_essentiality], while the 42.5% figure reflects draft models across 574 combinations [src: annotation_gap_discovery]. Untested here.
- **Hypothesis: the failure is coverage-limited rather than accuracy-limited.** If genes the model cannot map dominate the error, accuracy would rise on the mapped subnetwork alone [src: annotation_gap_discovery]. Untested here.
- **Hypothesis: the Module-ICA/ortholog gap is fully explained by target mismatch**, so the <1% and 95.8% figures should never be compared on one axis [src: fitness_modules] [src: discoveries].

## Resolving Work

- Re-run the 574 organism–carbon-source FBA sweep after curating models to ADP1-level depth; does accuracy move away from 42.5%, and by how much per curation step? [src: annotation_gap_discovery] [src: adp1_triple_essentiality]
- Stratify FBA accuracy by whether each gene carries a reaction mapping, using the aromatic-network gene set as the test case; is the deficit concentrated in the unmapped genes? [src: annotation_gap_discovery]
- Cross-check the unmapped aromatic-network genes against direct RB-TnSeq (random barcode transposon sequencing) fitness measurements; are model-silent genes phenotypically silent too? [src: annotation_gap_discovery]
- Score Module-ICA on a process-membership benchmark rather than strict KO identity, and score ortholog transfer on the same benchmark; does the <1% vs 95.8% ordering persist? [src: fitness_modules]
- Apply the ADP1 concordance protocol to a second organism with knockout data; does moderate concordance generalize beyond one curated model? [src: adp1_triple_essentiality]
