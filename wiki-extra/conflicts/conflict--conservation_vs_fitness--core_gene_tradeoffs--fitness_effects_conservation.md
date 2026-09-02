<!-- tension-hash: 7da469dc247e65ad -->
# Core Status: Biological Conservation or Sampling-Dependent Estimate?

The disagreement concerns whether core-gene status primarily measures biological conservation or instead reflects the composition and observability of the sampled pangenome. The issue matters because essentiality, functional burden, module membership, and ecological interpretation appear to align in some analyses but diverge in others. The evidence therefore challenges any single interpretation of the core boundary across [[concepts/pangenome-core-boundary-and-clade-size-bias]].

## Evidence Sides

**Side 1 — Core status reflects biological conservation**

The analysis supports essential genes being more conserved within sampled clades: 86.1% of essential genes were classified as core versus 81.2% of non-essential genes, with a median odds ratio of 1.56. [src: conservation_vs_fitness] A broader analysis also reports an essential-to-always-neutral gradient of 82%-versus-66%. [src: conservation_vs_fitness; fitness_effects_conservation] These results support a relationship between fitness importance and conservation, although they arise from different analyses.

The module analysis provides a related enrichment: module genes were 86.0% core versus 81.5% of all genes. [src: module_conservation] The [[concepts/core-gene-tradeoffs]] finding further indicates that core genes were more burdensome in several functional categories, suggesting that conservation can coexist with functional cost. [src: core_gene_tradeoffs]

**Side 2 — The estimated boundary is sampling- and analysis-dependent**

Clades containing only 2 genomes can produce trivially high core fractions, while the main Escherichia coli clade was unavailable because it contained too many genomes. [src: conservation_vs_fitness] Thus, the essential-gene enrichment is shaped by both undersampling and exclusion of overlarge or poorly joinable clades. [src: conservation_vs_fitness] The 86.1%-versus-81.2% result also differs from the 82%-versus-66% gradient because the analyses used different organism sets, phenotype categories, and integration procedures. [src: conservation_vs_fitness; fitness_effects_conservation]

Module membership cannot resolve the comparison: zero essential genes appeared in modules because essential genes lack usable transposon-insertion fitness data. [src: module_conservation] Core enrichment therefore cannot be compared directly across the same observable gene universe. In addition, non-core Cell Wall genes were more burdensome, producing a functional reversal rather than a single genome-wide burden rule. [src: core_gene_tradeoffs] Finally, null correlations between openness and ecological dominance concern species-level environment and phylogeny effect sizes, not within-clade gene-category conservation. [src: pangenome_openness; conservation_vs_fitness; fitness_effects_conservation]

## Possible Reconciliations

- **Sampling hypothesis:** Essential genes may genuinely be more conserved, while small clades inflate core fractions and excluded large clades alter the estimate.
- **Analysis-scope hypothesis:** The 86.1%-versus-81.2% and 82%-versus-66% values may both be valid for their respective organism sets, phenotype categories, and integration procedures.
- **Observability hypothesis:** Module enrichment may reflect genes with usable transposon-insertion fitness data rather than the full essential-gene universe.
- **Functional-scope hypothesis:** Conservation and burden may follow different rules across functional categories, including the Cell Wall reversal.
- **Metric hypothesis:** Openness may be too coarse to capture adaptation concentrated in particular functional categories; limited power also remains possible. [src: pangenome_openness]

## Resolving Work

- Recompute essential-versus-non-essential core fractions after matching organism sets, clade sizes, and phenotype categories; test whether the enrichment remains.
- Perform leave-one-clade-out and downsampling analyses, including simulated 2-genome clades, to quantify undersampling and excluded-clade effects.
- Integrate essentiality and module data using an assay that supplies fitness measurements for essential genes; test whether module enrichment persists in a common gene universe.
- Stratify core and non-core burden by functional category, especially Cell Wall, to determine whether the reversal explains aggregate results.
- Reanalyze openness with category-specific adaptation measures and phylogeny-aware power calculations; test whether null correlations reflect metric coarseness or insufficient power.
