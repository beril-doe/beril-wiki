<!-- tension-hash: 630f704f88730b94 -->
# Conservation, Essentiality, and Fitness Burden — Does Evolutionary Retention Predict Laboratory Cost?
The corpus contains a recurring disagreement over whether genes retained broadly across genomes should also impose measurable laboratory fitness costs when deleted. Conservation and essentiality analyses report a positive association, but AMR-specific results find no baseline burden difference between core and accessory genes. The disagreement matters because conservation, essentiality, and laboratory fitness may reflect different environments, phenotype definitions, and observable gene sets rather than a single biological axis. See [[concepts/gene-essentiality]], [[concepts/pangenome-conservation-fitness-decoupling]], and [[concepts/laboratory-fitness-versus-natural-selection]].

## Evidence Sides

**Conservation and essentiality are positively associated**

The broader synthesis reported 82% of essential genes as core across approximately 194,000 genes from 43 bacteria, while the newer integration reported 86.1% among 148,826 genes from 33 organisms. [src: fitness_effects_conservation] [src: conservation_vs_fitness] In the latter analysis, essential genes were 86.1% core versus 81.2% for non-essential genes, with a median odds ratio of 1.56. [src: conservation_vs_fitness] The broader comparison also found 82% core among essential or broadly fitness-affecting genes versus 66% among always-neutral genes. [src: fitness_effects_conservation] Module genes were similarly enriched for core status, at 86.0% versus 81.5% for all genes. [src: module_conservation] These results support a genome-wide conservation–fitness-importance gradient, although clade size, organism composition, pangenome mappings, and denominator choices affect its magnitude. [src: conservation_vs_fitness] [src: conservation_fitness_synthesis]

**Baseline laboratory burden does not necessarily track conservation**

The AMR analysis found virtually identical baseline fitness distributions for core and accessory AMR genes: mean fitness −0.024 for both, with p = 0.33. [src: amr_fitness_cost] It also found that mechanism strongly predicted conservation status but did not predict baseline fitness cost. [src: amr_fitness_cost] At the genome-wide level, 24.4% of core genes were burdensome when deleted, yet always-neutral genes were 66% core, indicating that evolutionary retention and laboratory deletion burden are not interchangeable. [src: conservation_fitness_synthesis] Functional reversals further limit a universal rule: non-core Cell Wall genes were more burdensome than core genes. [src: core_gene_tradeoffs] Pathway-level results also diverged: latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, with p=0.94, while another analysis found Active Dependencies at mean core completeness 0.986 versus 0.975 for Latent Capabilities in only 7 matched model organisms. [src: metabolic_capability_dependency] [src: pathway_capability_dependency]

## Possible Reconciliations

- **Hypothesis — environmental mismatch:** laboratory assays measure restricted conditions, whereas pangenome conservation integrates selection across broader environments and ecological interactions. [src: conservation_fitness_synthesis]
- **Hypothesis — phenotype scope:** the AMR result concerns baseline fitness in a resistance subset, while genome-wide analyses include essentiality, conditional phenotypes, and effect breadth. [src: amr_fitness_cost] [src: fitness_effects_conservation]
- **Hypothesis — sampling and observability:** clades containing only 2 genomes can have trivially high core fractions, and essential genes are invisible to insertion-based modules. [src: conservation_vs_fitness] [src: module_conservation]
- **Hypothesis — category-specific biology:** conservation and burden may reverse in particular functional classes, as observed for Cell Wall genes. [src: core_gene_tradeoffs]

## Resolving Work

- Build a matched gene panel across the same organisms, AMR mechanisms, core definitions, and knockout conditions; test whether core status predicts baseline and condition-specific fitness within each category.
- Recalculate core fractions after excluding clades containing only 2 genomes and separately restoring or weighting poorly represented clades; test the stability of the 86.1% versus 81.2% comparison.
- Compare laboratory fitness with field or environmental fitness proxies using paired genes and conditions; ask whether costly conserved genes gain advantages outside standard laboratory media.
- Stratify analyses by essentiality definition, effect breadth, functional category, and assay callability; test whether the conservation gradient persists after accounting for insertional measurement bias.
