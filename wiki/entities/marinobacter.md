---
type: "Organism"
description: "Marinobacter, a bacterial genus studied through annotation and fitness analyses."
sources: ["summaries/annotation_gap_discovery__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md"]
---
# Marinobacter

## Identity

**Canonical name:** Marinobacter. [src: annotation_gap_discovery]

**Known alias:** Marino. [src: annotation_gap_discovery]

**Stable external identifier:** Not reported in the source document. [src: annotation_gap_discovery]

## Key Facts

Marinobacter had 12 annotation gaps in the integrated evidence pipeline, of which 8 were resolved, giving an exact resolution rate of 66.7%. [src: annotation_gap_discovery]

This resolution rate placed Marinobacter among the organisms with the highest annotation-gap resolution in the study, whose organism-level rates ranged from 20% to 71.4%. [src: annotation_gap_discovery]

The study analyzed 14 organisms selected for rich carbon-source random-barcode transposon sequencing (RB-TnSeq), a method that measures genome-wide mutant fitness using barcoded transposon libraries. [src: annotation_gap_discovery]

The integrated pipeline combined metabolic-model gapfilling, Fitness Browser phenotypes, pangenome annotations, GapMind pathway evidence, and BLAST homology to assign candidate genes to gapfilled reactions. [src: annotation_gap_discovery]

Across all organisms, the pipeline resolved 96 of 201 gapfilled enzymatic reaction-organism pairs, or 47.8%, while 105 pairs, or 52.2%, remained unresolved. [src: annotation_gap_discovery]

The functional-dark-matter analysis **refines** this gapfilling evidence by reporting 49 organism–pathway gaps for Marinobacter, where these gaps are GapMind pathway co-occurrences rather than the 12 annotation gaps counted in the earlier integrated pipeline. [src: functional_dark_matter]

Marinobacter contributed 9 of the top 100 phenotype-bearing dark-gene candidates in the six-axis prioritization, which combined fitness importance, conservation, inference quality, pangenome distribution, biogeographic signal, and experimental tractability. [src: functional_dark_matter]

The conservation-weighted covering-set analysis included a Marinobacter stress experiment among the 10 organism–condition experiments selected to address 242 of the top 500 dark genes, or 45.3%. [src: functional_dark_matter]

In the cross-species conservation analysis, Marinobacter adhaerens showed one of the strongest essential-core enrichment signals, with an odds ratio of 3.08. [src: conservation_vs_fitness]

This result **supports** the existing fitness-based links by indicating that, in this organism, genes inferred as essential were preferentially found in core pangenome clusters; across the analyzed organisms, the median odds ratio was 1.56. [src: conservation_vs_fitness]

## Relation to the Research Corpus

Marinobacter is discussed in [[summaries/annotation_gap_discovery__REPORT]], which reports its 8 resolved gaps out of 12 total gaps. [src: annotation_gap_discovery]

Its result contributes evidence to [[concepts/metabolic-model-gapfilling]] by showing that integrated evidence can resolve a substantial fraction of gapfilled reaction-organism pairs. [src: annotation_gap_discovery]

The 49 GapMind pathway gaps **support and extend** Marinobacter’s relevance to [[concepts/metabolic-model-gapfilling]], while the different counting frameworks should not be treated as a reconciled single gap total. [src: functional_dark_matter]

Its result also relates to [[concepts/pangenome-integration]] and [[concepts/condition-specific-fitness]] because the pipeline used pangenome conservation and carbon-source fitness evidence in candidate-gene prioritization. [src: annotation_gap_discovery]

The dark-gene ranking **supports** these links by prioritizing Marinobacter candidates with integrated fitness, conservation, pangenome, and tractability evidence, and by selecting a Marinobacter stress experiment for broad experimental coverage. [src: functional_dark_matter]

The essential-core enrichment **supports and extends** [[concepts/gene-essentiality]] and [[concepts/pangenome-integration]] by connecting Marinobacter fitness measurements to species-level gene conservation. [src: conservation_vs_fitness]

Further details are in [[summaries/functional_dark_matter__REPORT]] and [[summaries/conservation_vs_fitness__REPORT]].
