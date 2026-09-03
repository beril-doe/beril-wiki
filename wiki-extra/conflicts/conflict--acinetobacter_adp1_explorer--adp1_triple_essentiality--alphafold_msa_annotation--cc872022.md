<!-- tension-hash: 1878bf802935e572 -->
# Conservation, essentiality, and functional prediction do not align

The disagreement is whether conservation and essentiality provide a reliable general guide to gene importance, pathway capability, and metabolic prediction. [[concepts/gene-essentiality]] Several analyses find strong enrichment of essential or functionally important genes among core genes, while others identify neutral or lineage-restricted exceptions, pathway-level reversals, and substantial failures of computational prediction. The tension may reflect real biology, but it may also arise from different organism sets, definitions, denominators, and measurement systems.

## Evidence Sides

**Conservation predicts essentiality and functional importance.**  
The two conservation–essentiality integrations report essential-gene core fractions of 82% (and 82.2% under strongest-effect grouping) across approximately 194,000 genes from 43 bacteria, versus 86.1% among 148,826 genes from 33 organisms. [src: fitness_effects_conservation] [src: conservation_vs_fitness] Essential genes were 86.1% core versus 81.2% for non-essential genes. [src: conservation_vs_fitness] Module genes were 86.0% core versus 81.5% for all genes. [src: module_conservation] Broad metal-important genes were 87.4% core versus 76.9% baseline, while metal+stress genes were 94.3% core. [src: metal_fitness_atlas] [src: metal_specificity] These patterns support a broad association between conservation, essentiality, and functional importance.

**Exceptions and measurement systems weaken or reverse that association.**  
Core enrichment coexists with 66% core status among always-neutral genes, 24.4% positive-fitness core genes versus 19.9% accessory genes, and function-specific reversals. [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] Persistent hypothetical genes had a higher essential fraction than annotation-lag genes, 18.0% versus 13.4%, despite being less core and having narrower ortholog breadth. [src: truly_dark_genes] DvH heavy-metal genes were 71.2% core and not significantly enriched after correction, while metal-specific genes were 84.8% core pooled and general sick genes were 90.2% core. [src: field_vs_lab_fitness] [src: metal_specificity] At the pathway level, latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, with p=0.94; a newer analysis instead found Active Dependencies at mean core completeness 0.986 versus 0.975 for Latent Capabilities in only 7 matched model organisms. [src: metabolic_capability_dependency] [src: pathway_capability_dependency] Prediction methods also disagree: FBA had 42.5% baseline accuracy across 574 organism–carbon-source combinations, lacked mappings for 30/51 aromatic-network genes, and predicted 0% Complex I essentiality despite 1.76× higher aromatic flux. [src: annotation_gap_discovery] [src: discoveries]

## Possible Reconciliations

- **Hypothesis—sampling and denominator effects:** The 82% and 86.1% estimates may differ because of datasets, organism filters, pangenome mappings, and denominators. Clades with only 2 genomes can have trivially high core fractions; the main *Escherichia coli* clade was absent, and Keio mapped to a small clade at only 26.1% coverage. [src: fitness_effects_conservation] [src: conservation_vs_fitness]
- **Hypothesis—definition and threshold effects:** “Essential,” “metal-important,” “active dependency,” and “core” may describe different operational categories. [src: counter_ion_effects] [src: metal_specificity]
- **Hypothesis—measurement rather than biological contradiction:** ICA, FBA, pathway matching, and knockout assays observe different targets. Essential genes are invisible to insertion-based ICA, and production matches cannot establish uptake, pathway completeness, or gene essentiality. [src: module_conservation] [src: webofmicrobes_explorer]

## Resolving Work

- Recompute core fractions using identical genomes, clade filters, pangenome mappings, and denominators; test whether the reported estimates still differ.
- Stratify essentiality and metal effects by organism, assay, threshold, gene length, annotation status, and stress history.
- Compare FBA, knockout, ortholog-transfer, and ICA predictions on the same genes and carbon sources to separate target differences from accuracy differences.
- Experimentally test uptake, pathway completeness, and essentiality for computationally matched compounds and apparently complete pathways.
- Reanalyze pathway conservation and dependency with matched organism sets and explicitly compare gene-level, pathway-level, and flux-level measures.
