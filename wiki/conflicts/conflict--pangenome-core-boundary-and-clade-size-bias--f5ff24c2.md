<!-- tension-hash: f5ff24c292366585 -->
# Does Pangenome Openness Fail to Predict Ecology, or Is the Metric Simply Too Coarse?

Two lines of evidence in this corpus speak to whether pangenome structure — how open or closed a species' gene repertoire is — carries ecological signal; the question sits on [[concepts/pangenome-core-boundary-and-clade-size-bias]]. One line reports a null: species-level openness does not correlate with whether environment or phylogeny dominates gene content. [src: pangenome_openness] The other compares gene categories — core genes, shared across the genomes of a sampled clade, versus auxiliary genes, present in only some of them — and finds a conservation gradient that is statistically robust but only weakly predictive of fitness importance. [src: fitness_effects_conservation] The two are not logically contradictory, but they leave unsettled what the core/auxiliary classification can be asked to do, and at which unit of analysis. Whether openness fails to predict ecological dominance because the metric is too coarse, because relevant adaptation is concentrated in particular functional categories, or because of limited power remains unresolved. [src: pangenome_openness]

## Evidence Sides

**Openness carries no ecological signal (null result, species level).** The openness analysis reports null correlations between openness and species-level environment and phylogeny effect sizes. [src: pangenome_openness] This is a null result and stays null: it is an absence of detected relationship, not a demonstrated independence. The report itself leaves three rival explanations open — that the openness metric is too coarse, that relevant adaptation is concentrated in particular functional categories, or that power is limited — and marks the question as unresolved. [src: pangenome_openness]

**Conservation tracks fitness importance within clades, weakly.** The within-clade conservation analyses compare gene categories inside sampled clades rather than across species. [src: pangenome_openness; conservation_vs_fitness; fitness_effects_conservation] Design choices about which and how many genomes represent a clade can make the core boundary more or less discriminative. [src: conservation_vs_fitness] The gradient linking conservation to fitness importance is statistically robust but only weakly predictive. [src: fitness_effects_conservation] The tension text characterizes the openness null as refining rather than contradicting these findings: the null concerns species-level environment and phylogeny effect sizes, while the conservation work operates on a different unit of analysis entirely. [src: pangenome_openness; conservation_vs_fitness; fitness_effects_conservation]

## Possible Reconciliations

- **Scale-mismatch hypothesis.** Openness is a species-level summary statistic while conservation categories are gene-level within-clade labels; the hypothesis is that ecological signal exists at gene level and is averaged away when compressed into a single openness value. [src: pangenome_openness; conservation_vs_fitness; fitness_effects_conservation]
- **Functional-concentration hypothesis.** Adaptation may be concentrated in particular functional categories, so a category-blind openness metric would detect nothing even where signal exists. [src: pangenome_openness]
- **Limited-power hypothesis.** The null may reflect insufficient statistical power at the species level rather than a true absence of relationship. [src: pangenome_openness]

## Resolving Work

- Recompute the openness-versus-effect-size correlations after stratifying genes by functional category, asking whether any category shows the association that the pooled metric does not. [src: pangenome_openness]
- Run a power analysis on the species-level openness comparison to determine what effect size the existing sample could have detected, distinguishing a true null from an underpowered one. [src: pangenome_openness]
- Apply the within-clade conservation categorization to the same species used in the openness analysis, testing whether gene-level conservation predicts environment-versus-phylogeny dominance where species-level openness does not. [src: pangenome_openness; conservation_vs_fitness; fitness_effects_conservation]
- Decompose openness into components (rate of new-gene accumulation, singleton fraction) and test each separately against environment and phylogeny effect sizes, asking whether the composite metric masks a component-level signal. [src: pangenome_openness]
