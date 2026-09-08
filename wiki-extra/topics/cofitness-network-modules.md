---
title: Cofitness Network Modules
type: Topic
sources:
- id: amr_cofitness_networks
  resource: ../../wiki/summaries/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
- id: discoveries
  resource: ../../wiki/summaries/discoveries.md
  title: discoveries
- id: fitness_modules
  resource: ../../wiki/summaries/fitness_modules__REPORT.md
  title: fitness modules
- id: cofitness_coinheritance
  resource: ../../wiki/summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
- id: aromatic_catabolism_network
  resource: ../../wiki/summaries/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
- id: module_conservation
  resource: ../../wiki/summaries/module_conservation__REPORT.md
  title: module conservation
- id: essential_genome
  resource: ../../wiki/summaries/essential_genome__REPORT.md
  title: essential genome
- id: functional_dark_matter
  resource: ../../wiki/summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: metal_cross_resistance
  resource: ../../wiki/summaries/metal_cross_resistance__REPORT.md
  title: metal cross resistance
- id: conservation_fitness_synthesis
  resource: ../../wiki/summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
- id: respiratory_chain_wiring
  resource: ../../wiki/summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
---
# Cofitness Network Modules

Cofitness network modules are groups of genes whose fitness profiles vary together across experimental conditions. They provide a way to study functional organization that is not limited to operons, annotations, or single-gene effects. This corpus speaks to the topic through broad bacterial Fitness Browser datasets, independent component analysis (ICA), pangenome comparisons, condition-specific pathway studies, and analyses of unknown-function genes. Together, these projects support modules as useful empirical summaries of coordinated phenotypes, while cautioning that a module is not automatically a regulatory unit, a metabolic pathway, or a naturally co-inherited genomic island.

## What the Corpus Shows

**Modules capture structured, condition-dependent phenotypes.** Cofitness measures similarity between genes’ fitness profiles across experimental conditions; it therefore reports shared phenotypic response rather than direct transcriptional control. [^amr_cofitness_networks] In a broad analysis across 32 bacteria, robust ICA and DBSCAN identified 17–52 modules per organism. [^discoveries] Using an absolute component-weight threshold of \(|weight| \geq 0.3\) and a maximum of 50 genes, the analysis identified 1,116 stable modules; 94.2% showed elevated within-module cofitness, with mean within-module \(|r|=0.34\) versus 0.12 in the background. [^fitness_modules] This pattern supports modules as non-random summaries of condition-linked fitness behavior, while the strong genomic-adjacency enrichment of 22.7× indicates that physical organization contributes without fully explaining the signal. [^fitness_modules]

The AMR-focused analysis provides a second scale of evidence. Among 801 antimicrobial-resistance genes with fitness data, 192 (24%) were assigned to ICA modules. [^amr_cofitness_networks] AMR-containing modules had a median of 46 genes versus 27 in non-AMR modules, with Mann–Whitney U p = 1.7×10⁻⁸; 136 module families contained AMR genes, and 208/209 (99%) AMR gene–module assignments belonged to cross-organism conserved families. [^amr_cofitness_networks] Thus, resistance genes often appear embedded in broader condition-associated systems rather than isolated in mechanism-specific neighborhoods. The result is best read as an architecture of shared fitness response, not proof that all member genes are co-regulated.

**The most informative units can be larger than pairwise links.** Pairwise cofitness is widespread: 769/801 AMR genes (96%) had at least one extra-operon partner at \(|r|>0.3\), and the dataset contained 180,370 total cofitness partners, of which 179,375 were extra-operon. [^amr_cofitness_networks] Mean support-network sizes were 233 genes at \(|r|>0.3\), 110 at \(|r|>0.4\), and 71 at \(|r|>0.5\). [^amr_cofitness_networks] These large neighborhoods are useful for discovery, but they also show why an individual edge can be difficult to interpret: many genes may be jointly dispensable under one condition and jointly important under another.

Pangenome analysis suggests that coordinated modules can outperform isolated pairwise associations when the question is whether genes occur together across genomes. Across 9 organisms, 2,253,491 cofit pairs were compared with 22,534,910 prevalence-matched random pairs. [^cofitness_coinheritance] The mean pairwise co-occurrence effect was delta phi = +0.011 across organisms, but the aggregate effect was delta = +0.003 and the across-organism Wilcoxon signed-rank test was not significant (W=9, p=0.13). [^cofitness_coinheritance] By contrast, across 195 ICA modules in 6 organisms, within-module co-occurrence had mean phi=0.229 versus a prevalence-matched null mean of 0.177, yielding delta=+0.053; 51/195 modules (26%) were significant at p<0.05 and 21/195 (11%) remained significant at q<0.05 after false-discovery-rate correction. [^cofitness_coinheritance] The practical implication is that module-level structure can retain a coherent inheritance signal even where pairwise phi is weakened by prevalence ceilings.

**Modules connect physically dispersed genes through shared biochemical objectives.** The ADP1 quinate-catabolism study identified a 51-gene support network around the β-ketoadipate pathway. [^aromatic_catabolism_network] Cofitness assigned 44/51 genes (86%) to four subsystems: 8 aromatic-pathway genes, 21 Complex I genes, 7 iron-acquisition genes, and 2 PQQ-biosynthesis genes; six additional genes were transcriptional regulators and 7 remained unassigned. [^aromatic_catabolism_network] These genes occupy distinct chromosomal regions: the Complex I operon lies at 714–729 kb, the pca/qui pathway at 1,709–1,724 kb, PQQ biosynthesis at 2,461 kb, and iron-acquisition genes at 4 loci. [^aromatic_catabolism_network]

The biochemical interpretation is that a substrate-supported growth phenotype depends on more than the pathway that directly transforms the substrate. Quinate catabolism produces metabolites entering the TCA cycle; quinate dehydrogenase requires PQQ, protocatechuate 3,4-dioxygenase requires non-heme Fe²⁺, and respiratory machinery must reoxidize NADH generated during oxidation. [^aromatic_catabolism_network] Ten of 13 Complex I operon subunits independently produced quinate-specific growth defects even though the respiratory locus is distant from pca/qui. [^aromatic_catabolism_network] This is a strong example of a module-like support network spanning pathway, cofactor, metal, electron-transfer, and regulatory functions. It also illustrates why cofitness can reveal functional coupling beyond genomic neighborhoods: only 0.7% of cofit pairs were adjacent within 5 genes, and excluding adjacent pairs did not change the result pattern. [^cofitness_coinheritance]

**Cross-organism conservation makes some modules portable, but not universally transferable.** Cross-organism alignment of fitness modules found 156 families spanning at least 2 organisms, 28 spanning 5+ organisms, and one spanning 21 of 32 organisms. [^discoveries] A complementary conservation analysis found that module genes had an 86.0% core fraction versus 81.5% for all genes. [^module_conservation] Here, “core” means broadly present in the analyzed pangenome; it should not be conflated with essentiality under every condition. The broader synthesis reported that only 15 essential families were essential in all 48 organisms, whereas 859 ortholog families were universally essential within every organism in which they occurred. [^essential_genome]

The corpus therefore supports a hierarchy of transferability. Module families can preserve a process-level relationship across organisms, but the exact genes, dependencies, and phenotypic consequences remain organism- and condition-specific. This is especially important for dark genes: 6,142 dark genes belonged to ICA fitness modules, but Module-ICA achieved less than 1% strict KEGG KO precision, whereas ortholog transfer achieved 95.8% precision and 91.2% coverage. [^functional_dark_matter][^discoveries] Modules are consequently better suited to proposing process-level functions than to assigning precise molecular identities.

## Tensions and Caveats

The central interpretive conflict is whether network signals represent biological coordination or shared dispensability, ancestry, stress response, annotation boundaries, and experimental design. [conflict--amr_cofitness_networks--amr_strain_variation--aromatic_catabolism_network--d0b6ec8b](../conflicts/conflict--amr_cofitness_networks--amr_strain_variation--aromatic_catabolism_network--d0b6ec8b.md) The AMR analysis explicitly states that shared fitness profiles do not establish direct regulation, while the metal analysis lacked negative controls capable of separating universal cross-resistance from a general-stress response. [^amr_cofitness_networks][^metal_cross_resistance] Pairwise inheritance effects were also heterogeneous: the aggregate delta was +0.003 with Wilcoxon p=0.13, and Korea had no significant modules because its modules were greater than 90% core with prevalence near 1.0. [^cofitness_coinheritance]

Prevalence and phylogeny are load-bearing limitations for pangenome interpretation. Nearly universal genes provide too little presence/absence variation for reliable phi inference, and cofit-pair phi was higher among near genomes than medium-distance genomes, with mean=0.102 versus mean=0.067. [^cofitness_coinheritance] Most organisms lacked genomes in the far phylogenetic stratum, so apparent co-inheritance cannot be cleanly separated from shared ancestry in every comparison. [^cofitness_coinheritance]

Conservation is also not a direct synonym for module importance. The promoted dispute over conservation, essentiality, and laboratory burden contrasts a positive genome-wide conservation gradient with an AMR result in which core and accessory AMR genes had virtually identical baseline fitness distributions: mean fitness −0.024 for both, p = 0.33. [conflict--acinetobacter_adp1_explorer--adp1_triple_essentiality--alphafold_msa_annotation--8af84dcc](../conflicts/conflict--acinetobacter_adp1_explorer--adp1_triple_essentiality--alphafold_msa_annotation--8af84dcc.md) [^conservation_fitness_synthesis] In addition, continuous fitness can contain information about knockout lethality while thresholded RB-TnSeq essentiality agrees poorly with complete-knockout calls: the 0.05-threshold AUC was 0.344 and Cohen’s kappa was -0.081. [conflict--adp1_triple_essentiality--conservation_fitness_synthesis--conservation_vs_fitness--3d504d86](../conflicts/conflict--adp1_triple_essentiality--conservation_fitness_synthesis--conservation_vs_fitness--3d504d86.md) 

Finally, condition-specific modules should not be treated as universal metabolic wiring. In ADP1, the aromatic study reported 1.76× higher Complex I flux on aromatic substrates and 10/13 Complex I subunit defects, whereas a related respiratory analysis predicted zero NDH-2 flux under standard FBA conditions and found no significant cross-species compensation pattern, p = 0.52. [conflict--aromatic_catabolism_network--respiratory_chain_wiring](../conflicts/conflict--aromatic_catabolism_network--respiratory_chain_wiring.md) [^aromatic_catabolism_network][^respiratory_chain_wiring] Models, transferred fitness, and measured growth defects therefore answer related but non-identical questions.

## Where to Go Deeper

- [cofitness-network-architecture](../../wiki/concepts/cofitness-network-architecture.md) — start here for the overall module architecture, thresholds, organism specificity, and shared dispensability.
- [module-level-coinheritance](../../wiki/concepts/module-level-coinheritance.md) — examine why ICA modules provide a stronger pangenome co-occurrence signal than pairwise cofitness.
- [genomic-dispersal-functional-coupling](../../wiki/concepts/genomic-dispersal-functional-coupling.md) — follow the ADP1 example of distributed genes supporting one biochemical objective.
- [fitness-module-detection-sensitivity](../../wiki/concepts/fitness-module-detection-sensitivity.md) — assess how module detection, conservation, and callability affect the apparent enrichment.
- [gene-essentiality](../../wiki/concepts/gene-essentiality.md) — distinguish module membership, graded fitness effects, and binary essentiality.
- [pangenome-conservation-fitness-decoupling](../../wiki/concepts/pangenome-conservation-fitness-decoupling.md) — investigate why conservation and laboratory burden do not always coincide.
- [metabolic-model-gapfilling](../../wiki/concepts/metabolic-model-gapfilling.md) — evaluate the limits of FBA when modules imply respiratory or cofactor dependencies.
- [functional-dark-matter](../../wiki/concepts/functional-dark-matter.md) — see how module membership prioritizes genes whose molecular functions remain unknown.

Key entities: [kescience-fitnessbrowser](../../wiki/entities/kescience-fitnessbrowser.md), [independent-component-analysis](../../wiki/entities/independent-component-analysis.md), [kbase-ke-pangenome](../../wiki/entities/kbase-ke-pangenome.md), [tnseq](../../wiki/entities/tnseq.md), [flux-balance-analysis](../../wiki/entities/flux-balance-analysis.md), [bidirectional-best-hit-orthology](../../wiki/entities/bidirectional-best-hit-orthology.md)

Project reports: [fitness_modules__REPORT](../../wiki/summaries/fitness_modules__REPORT.md), [amr_cofitness_networks__REPORT](../../wiki/summaries/amr_cofitness_networks__REPORT.md), [cofitness_coinheritance__REPORT](../../wiki/summaries/cofitness_coinheritance__REPORT.md), [aromatic_catabolism_network__REPORT](../../wiki/summaries/aromatic_catabolism_network__REPORT.md), [module_conservation__REPORT](../../wiki/summaries/module_conservation__REPORT.md), [conservation_fitness_synthesis__REPORT](../../wiki/summaries/conservation_fitness_synthesis__REPORT.md), discoveries__REPORT

[^amr_cofitness_networks]: [amr cofitness networks](../../wiki/summaries/amr_cofitness_networks__REPORT.md)
[^discoveries]: [discoveries](../../wiki/summaries/discoveries.md)
[^fitness_modules]: [fitness modules](../../wiki/summaries/fitness_modules__REPORT.md)
[^cofitness_coinheritance]: [cofitness coinheritance](../../wiki/summaries/cofitness_coinheritance__REPORT.md)
[^aromatic_catabolism_network]: [aromatic catabolism network](../../wiki/summaries/aromatic_catabolism_network__REPORT.md)
[^module_conservation]: [module conservation](../../wiki/summaries/module_conservation__REPORT.md)
[^essential_genome]: [essential genome](../../wiki/summaries/essential_genome__REPORT.md)
[^functional_dark_matter]: [functional dark matter](../../wiki/summaries/functional_dark_matter__REPORT.md)
[^metal_cross_resistance]: [metal cross resistance](../../wiki/summaries/metal_cross_resistance__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../../wiki/summaries/conservation_fitness_synthesis__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../../wiki/summaries/respiratory_chain_wiring__REPORT.md)
