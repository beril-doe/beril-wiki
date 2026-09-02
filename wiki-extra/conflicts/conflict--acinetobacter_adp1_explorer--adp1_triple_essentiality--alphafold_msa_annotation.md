<!-- tension-hash: 1878bf802935e572 -->
# Conservation–Essentiality Signals Split Across Datasets and Measurement Methods

[[concepts/gene-essentiality]] brings together several disagreements about whether conserved, core, essential, and functionally important genes should coincide. The central estimates differ, but so do organism sets, pangenome mappings, thresholds, pathway definitions, and measurement methods. The tension matters because a single conservation–essentiality gradient could conceal lineage-restricted essential genes, annotation gaps, stress-specific effects, and failures of computational prediction.

## Evidence Sides

**Conservation and essentiality are positively associated.**  
One integration reported an essential-gene core fraction of 82% (and 82.2% under strongest-effect grouping) across approximately 194,000 genes from 43 bacteria, while another reported 86.1% among 148,826 genes from 33 organisms. [src: fitness_effects_conservation] [src: conservation_vs_fitness] In the direct linkage, essential genes were 86.1% core versus 81.2% for non-essential genes. [src: conservation_vs_fitness] Module genes were 86.0% core versus 81.5% for all genes. [src: module_conservation] Broad metal-important genes were 87.4% core versus 76.9% baseline, and metal+stress genes were 94.3% core. [src: metal_fitness_atlas] [src: metal_specificity]

**The association is conditional, and some measurements reverse or weaken it.**  
Always-neutral genes were 66% core, positive-fitness core genes were 24.4% versus 19.9% accessory genes, and function-specific reversals were observed. [src: acinetobacter_adp1_explorer] [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] [src: fitness_effects_conservation] Persistent hypothetical genes had a higher essential fraction than annotation-lag genes, 18.0% versus 13.4%, despite being less core and having narrower ortholog breadth. [src: truly_dark_genes] DvH heavy-metal genes were 71.2% core and not significantly enriched after correction; metal-specific genes were 84.8% core pooled, while general sick genes were 90.2% core. [src: field_vs_lab_fitness] [src: metal_specificity]

**Computational and pathway measurements do not consistently reproduce gene-level essentiality.**  
Latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, with p=0.94. [src: metabolic_capability_dependency] Conversely, Active Dependencies had mean core completeness 0.986 versus 0.975 for Latent Capabilities in only 7 matched model organisms. [src: pathway_capability_dependency] ADP1 showed moderate FBA–knockout concordance, while annotation-gap analysis found 42.5% baseline FBA accuracy across 574 organism–carbon-source combinations. [src: adp1_triple_essentiality] [src: annotation_gap_discovery] Module-ICA had <1% strict KO precision versus 95.8% for ortholog transfer. [src: discoveries] [src: fitness_modules]

## Possible Reconciliations

- **Hypothesis — denominator and sampling effects:** the 82%, 82.2%, and 86.1% estimates may differ because of organism filters, pangenome mappings, clade sizes, and denominators; the estimates should not be averaged. Clades with only 2 genomes can have trivially high core fractions, while the main *Escherichia coli* clade was absent and Keio mapped at only 26.1% coverage. [src: conservation_vs_fitness]
- **Hypothesis — biological scope:** pathway conservation, gene essentiality, metal importance, and stress sickness may describe different conditional functions rather than one universal property.
- **Hypothesis — measurement visibility:** essential genes are invisible to insertion-based ICA, and FBA, knockout assays, ortholog transfer, and module inference target different quantities.
- **Hypothesis — annotation and lineage restriction:** essentiality can persist in lineage-restricted genes, while short-gene measurement and annotation biases alter apparent conservation.

## Resolving Work

- Recompute both conservation–essentiality estimates on the same organism set, genome filters, pangenome mapping, and denominator; test whether 82%, 82.2%, and 86.1% remain distinct.
- Stratify essential and non-essential genes by clade size, coverage, gene length, annotation status, and ortholog breadth; test whether the 86.1% versus 81.2% contrast survives matched sampling.
- Compare insertion, knockout, FBA, ortholog-transfer, and module-ICA predictions against the same experimentally tested genes under identical carbon and stress conditions.
- Reanalyze metal-important, heavy-metal, osmotic-stress, and metal+stress genes with common thresholds and organism sets; test whether the 2.7× discrepancy and enrichment differences persist.
- Complete pathway and uptake validation experimentally across the 7 mapped organisms; test whether pathway completeness predicts measured capability and essentiality.
