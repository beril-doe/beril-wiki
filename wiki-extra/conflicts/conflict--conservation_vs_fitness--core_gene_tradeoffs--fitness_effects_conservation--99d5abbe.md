<!-- tension-hash: 7da469dc247e65ad -->
# Core Status: Biological Conservation or Sampling Artifact?

The disagreement is whether higher core-gene representation among essential genes reflects genuine biological conservation or an analysis boundary shaped by clade size, genome availability, phenotype observability, and functional heterogeneity. The tension matters because core status is being used to connect essentiality, conservation, fitness, and ecological interpretation, yet the cited analyses do not necessarily measure the same gene universe or biological contrast. [[concepts/pangenome-core-boundary-and-clade-size-bias]]

## Evidence Sides

**Essential genes are more conserved within sampled clades.** The analysis supports essential genes being more conserved within sampled clades, with 86.1% of essential genes classified as core versus 81.2% of non-essential genes and a median odds ratio of 1.56. [src: conservation_vs_fitness] This supports interpreting core status as a signal of biological conservation within the sampled clades. [[concepts/pangenome-core-boundary-and-clade-size-bias]]

**Core enrichment is shaped by clade sampling and exclusion.** Clades containing only 2 genomes can produce trivially high core fractions, and the main Escherichia coli clade was unavailable because it contained too many genomes. [src: conservation_vs_fitness] The resulting estimate is therefore shaped by both undersampling and exclusion of overlarge or poorly joinable clades. [src: conservation_vs_fitness] [[concepts/pangenome-core-boundary-and-clade-size-bias]]

**The conservation boundary is analysis-dependent.** The 86.1%-versus-81.2% enrichment differs from the 82%-versus-66% essential-to-always-neutral gradient in the broader analysis. [src: conservation_vs_fitness; fitness_effects_conservation] These values arise from different organism sets, phenotype categories, and integration procedures. [src: conservation_vs_fitness; fitness_effects_conservation] [[concepts/pangenome-core-boundary-and-clade-size-bias]]

**Module and burden results do not define one universal rule.** Module genes were 86.0% core versus 81.5% of all genes, but zero essential genes appeared in modules because essential genes lack usable transposon-insertion fitness data. [src: module_conservation] Core genes were more burdensome in several functional categories, whereas non-core Cell Wall genes were more burdensome. [src: core_gene_tradeoffs] Thus, module enrichment and burden cannot be directly treated as the same essential-versus-non-essential comparison or as a single genome-wide burden rule. [[concepts/pangenome-core-boundary-and-clade-size-bias]]

**Openness measures a different level of variation.** The openness analysis reports null correlations concerning species-level environment and phylogeny effect sizes, whereas the conservation analyses compare gene categories within sampled clades. [src: pangenome_openness; conservation_vs_fitness; fitness_effects_conservation] Whether this reflects a coarse metric, category-specific adaptation, or limited power remains unresolved. [src: pangenome_openness]

## Possible Reconciliations

- **Hypothesis — sampling scope:** Essential genes may genuinely be more conserved within adequately sampled clades, while small, excluded, or poorly joinable clades distort the apparent magnitude.
- **Hypothesis — definitional scope:** The 86.1%-versus-81.2% comparison and the 82%-versus-66% gradient may both be valid because they use different organism sets, phenotype categories, and integration procedures.
- **Hypothesis — observability:** The absence of essential genes from modules may reflect missing usable transposon-insertion fitness data rather than true biological absence.
- **Hypothesis — functional heterogeneity:** Core conservation and fitness burden may vary by functional category, allowing core genes to be more burdensome overall while non-core Cell Wall genes are more burdensome.

## Resolving Work

- Recompute core fractions after matched clade-size filtering and rarefaction; test whether the 86.1% versus 81.2% contrast and median odds ratio of 1.56 persist.
- Add genomes from under-sampled clades and, where possible, the main Escherichia coli clade; test whether core fractions change with sampling depth and clade inclusion.
- Harmonize organism sets, phenotype categories, and integration procedures; determine whether the 86.1%-versus-81.2% and 82%-versus-66% estimates converge under identical definitions.
- Generate usable fitness measurements for essential genes or use an independent essentiality assay; test whether module enrichment remains 86.0% versus 81.5% after comparable observability.
- Stratify conservation, burden, and openness analyses by functional category and phylogenetic scale; test whether category-specific effects explain the burden reversal and null openness correlations.
