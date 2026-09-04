<!-- tension-hash: 76471e081a5f592d -->
# Fitness-network signals: biological coordination or measurement artifact?

The central disagreement is whether cofitness, metal cross-resistance, conservation, and functional-network patterns reveal genuine biological coordination or instead reflect shared dispensability, ancestry, stress responses, annotation boundaries, and experimental design. The tension is concentrated in [[concepts/cofitness-network-architecture]] and related analyses: some results support modules and coordinated cellular processes, while null models and measurement limitations prevent a single interpretation.

## Evidence Sides

**Biological coupling and selection produce real signals.** Flagellar motility, chemotaxis, and amino-acid biosynthesis enrichment may reflect genuine co-regulation, and all tested metal pairs were positive. [src: amr_cofitness_networks] The counter-ion study reports 4,304/10,821 shared NaCl–metal records, while zinc sulfate had 44.6% overlap despite 0 mM chloride. [src: counter_ion_effects] ICA modules had delta phi=+0.053 overall and accessory modules +0.108. [src: cofitness_coinheritance] Laboratory burden also aligned with conservation: 28,017 genes were costly in the laboratory and conserved in the pangenome versus 5,526 costly and dispensable genes. [src: conservation_fitness_synthesis] Across 801 AMR genes and 25 organisms, pooled knockout fitness shift was +0.086 [+0.074, +0.098], and the cost was mechanism-independent (KW p=0.89), conservation-independent (p=0.33), and tier-independent (p=0.26). [src: discoveries]

**The signals may be confounded or lack broad generality.** The null matched conservation class rather than mean fitness and does not resolve whether enrichment reflects co-regulation or shared dispensability. [src: amr_cofitness_networks] No negative controls were included in the metal analysis, so universal cross-resistance cannot be distinguished from a general-stress response. [src: metal_cross_resistance] Pairwise cofit pairs had mean delta phi +0.011, but aggregate delta was +0.003 with Wilcoxon p=0.13. [src: cofitness_coinheritance] Accessory-versus-core differences were only near significant (p=0.051), and Korea had no significant modules because all were >90% core with prevalence near 1.0. [src: cofitness_coinheritance] Only 5% of mapped modules were accessory. [src: module_conservation] Near genomes had mean phi=0.102 versus 0.067 for medium-distance genomes, and most organisms lacked a far stratum. [src: cofitness_coinheritance]

**Functional identity and essentiality are measured inconsistently.** Module-ICA and cofitness voting had <1% strict KEGG KO precision, whereas ortholog transfer achieved 95.8% precision, 91.2% coverage, and 0.934 F1. [src: fitness_modules] Fifteen families were essential in all 48 organisms, while 4,799 were variably essential and 7,084 essential genes had no detectable ortholog in another Fitness Browser organism. [src: essential_genome] Truly dark genes were 18.0% essential versus 13.4% for annotation-lag genes, but short genes and insertion bias complicate interpretation. [src: truly_dark_genes] Conservative BBH orthology can miss divergent homologs, so orphan status is not proof of novelty. [src: essential_genome]

## Possible Reconciliations

- **Hypothesis—unit of analysis:** Modules may capture coordinated biology that pairwise correlations dilute, while the small accessory-module fraction limits generalization.
- **Hypothesis—ancestry and stress:** Metal associations may combine phylogenetic similarity and shared cellular stress biology with genuine cross-resistance.
- **Hypothesis—operational definitions:** Essential, dark, orphan, and functionally assigned genes may describe different measurement boundaries rather than contradictory biological classes.
- **Hypothesis—environmental scope:** Laboratory cost may indicate potential selection relevance without directly measuring purifying selection in natural environments. [src: conservation_fitness_synthesis]

## Resolving Work

- Add negative controls and matched metal concentrations, then use PGLS or independent contrasts to test cross-resistance beyond ancestry and general stress.
- Refit pairwise and module-level associations with phylogenetically corrected models and balanced evolutionary-distance strata.
- Validate network-derived functions using targeted knockouts, complementation, expression measurements, and direct pathway assays.
- Reassess orphan essentials with sensitive homology searches and synteny to distinguish novel genes from missed divergent homologs.
- Compare laboratory fitness and conservation against ecologically matched population data to test whether costly, conserved genes experience natural selection.
