<!-- tension-hash: 76471e081a5f592d -->
# What Do Cofitness and Comparative Signals Actually Establish?

The corpus contains a recurring disagreement over whether cofitness, conservation, essentiality, resistance, and ecological associations reveal biological coupling or instead reflect shared stress, ancestry, measurement boundaries, and laboratory-specific effects. The tension matters because the same signals can support strong claims about modules, gene function, and natural selection—or only generate hypotheses requiring phylogenetically controlled and experimentally validated tests. The overview is summarized on [[concepts/cofitness-network-architecture]].

## Evidence Sides

### **Side 1: Cofitness and co-inheritance indicate genuine biological coupling**

Flagellar motility, chemotaxis, and amino-acid biosynthesis enrichment may reflect genuine co-regulation, although the matched null followed conservation class rather than mean fitness. [src: amr_cofitness_networks] Pairwise cofit pairs had mean delta phi +0.011 across organisms, while ICA modules had delta phi=+0.053 overall and accessory modules +0.108. [src: cofitness_coinheritance] Metal pairs were all positive, and the counter-ion study reports 4,304/10,821 shared NaCl–metal records. [src: metal_cross_resistance] Twenty-seven of 28 defense pairings were significant, with R-M Type II × Gabija particularly strong. [src: phage_defense_arsenal]

### **Side 2: Shared stress, ancestry, and laboratory context can produce the same signals**

No negative controls were included in the metal-pair analysis, so universal cross-resistance cannot be distinguished from a general-stress response. [src: metal_cross_resistance] Near genomes had mean phi=0.102 versus 0.067 for medium-distance genomes, and most organisms lacked a far stratum. [src: cofitness_coinheritance] Multi-metal tolerance did not correlate with BacDive isolation from metal environments (Spearman rho approximately -0.02, p > 0.8); after matching and collapsing strains, only 20 independent species remained. [src: metal_cross_resistance] Pairwise cofit aggregation was delta +0.003 with Wilcoxon p=0.13, and Korea had no significant modules because all were >90% core with prevalence near 1.0. [src: cofitness_coinheritance]

### **Side 3: Comparative and functional results support robust gene-level interpretation**

Ortholog transfer achieved 95.8% precision, 91.2% coverage, and 0.934 F1. [src: fitness_modules] Fifteen families were essential in all 48 organisms, while 4,799 were variably essential. [src: essential_genome] Truly dark genes were 18.0% essential versus 13.4% for annotation-lag genes. [src: truly_dark_genes] Laboratory cost also aligned with conservation: 28,017 genes were costly in the laboratory and conserved in the pangenome versus 5,526 costly and dispensable genes. [src: conservation_fitness_synthesis]

### **Side 4: Measurement boundaries and model disagreement limit those interpretations**

Module-ICA and cofitness voting had <1% strict KEGG KO precision, while dark-gene and phenotype analyses identify hypotheses rather than direct gene-to-step assignments. [src: fitness_modules] Zero essential genes appeared in ICA modules, despite essential-genome analyses identifying universally and variably essential families. [src: module_conservation; essential_genome] In ADP1, FBA predicted 0% Complex I essentiality while 10/13 subunits produced quinate-specific defects, and 30/51 network genes lacked FBA reaction mappings. [src: aromatic_catabolism_network] The corrected test found aromatic deficits of -0.297 with validated NDH-2 versus -0.156 without, p=0.52. [src: discoveries]

## Possible Reconciliations

- **Hypothesis—measurement scope:** Modules may capture coordinated processes, whereas essentiality and orthology operate at gene or family level.
- **Hypothesis—ancestry and stress:** Positive cofitness or metal overlap may combine real coupling with phylogenetic relatedness and general-stress physiology.
- **Hypothesis—environmental transfer:** Laboratory burden may be evidence for, but not direct measurement of, purifying selection in natural environments.
- **Hypothesis—model incompleteness:** FBA failures may reflect missing reaction mappings or compensatory pathways rather than false phenotype data.

## Resolving Work

- Reanalyze cofitness, metal, and defense associations with PGLS or independent contrasts; test whether signals persist after phylogenetic correction.
- Add matched negative controls and concentration-matched metal experiments; distinguish general stress from metal-specific cross-resistance.
- Validate predicted modules and dark-gene functions with targeted knockouts, complementation, expression measurements, and pathway-level phenotyping.
- Rebuild FBA models with the 30/51 unmapped network genes and test Complex I and NDH-2 predictions across strains and substrates.
