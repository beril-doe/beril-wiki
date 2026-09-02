---
type: "Concept"
description: "Why pangenome prevalence does not predict AMR fitness cost"
sources: ["summaries/amr_fitness_cost__REPORT.md"]
---
# Decoupling between pangenome conservation and fitness cost

Pangenome conservation and measured fitness cost are distinct properties: an AMR gene's prevalence across sampled genomes does not, in this dataset, predict the relative fitness effect of disrupting it. The evidence comes from integrating [[entities/kescience-fitnessbrowser]] measurements with pangenome conservation labels, as described in the [[summaries/amr_fitness_cost__REPORT]]. [src: amr_fitness_cost]

## Core–accessory AMR genes show similar fitness distributions

Core, or intrinsic, AMR genes (N=638) and accessory, or acquired, AMR genes (N=163) had virtually identical mean fitness values of −0.024, with Cohen's d = 0.002 and Mann-Whitney U p = 0.33. [src: amr_fitness_cost] This **supports** a decoupling between pangenome conservation status and baseline AMR fitness cost: being broadly conserved did not correspond to a measurably different disruption phenotype from being accessory in the analyzed data. [src: amr_fitness_cost]

The broader stratification analysis likewise found no conservation difference (p = 0.33), no Tier 1-versus-Tier 2 difference (p = 0.26), and no antibiotic-versus-metal resistance-type difference (p = 0.87). [src: amr_fitness_cost] These null results refine [[concepts/environmental-resistome]] by separating the persistence or distribution of resistance genes from the metabolic burden measured when those genes are disrupted. [src: amr_fitness_cost]

## Mechanism predicts distribution, not measured cost

Resistance mechanism was strongly associated with pangenome conservation status (χ² = 69.3, p = 1.4×10⁻¹³): 44% of metal-resistance genes were accessory, compared with 13% of efflux genes and 16% of enzymatic-inactivation genes. [src: amr_fitness_cost] Thus, mechanism **supports** prediction of where an AMR gene occurs in the pangenome, but it did not predict baseline fitness cost: efflux (N=254), enzymatic inactivation (N=304), metal resistance (N=144), and unknown (N=74) mechanisms showed no significant baseline-cost difference (Kruskal-Wallis H = 0.65, p = 0.89). [src: amr_fitness_cost]

This separation indicates that evolutionary or ecological processes shaping gene prevalence need not produce corresponding differences in laboratory knockout fitness. The report proposes, as an interpretation rather than a directly measured process, that horizontal transfer may preferentially retain cost-optimized genes or that compensation may reduce costs after acquisition. [src: amr_fitness_cost]

## Scope and limitations of the decoupling

The comparison used Fitness Browser data from 25 lab-adapted organisms, so the null result may not represent newly acquired resistance or wild populations. [src: amr_fitness_cost] The analysis also classified a gene as core using a ≥95% prevalence threshold, while the median number of GTDB genomes per Fitness Browser species was 9, with a range of 2–399. [src: amr_fitness_cost] Consequently, a gene present in all 9 sampled genomes could be labeled core despite having lower prevalence under broader sampling, making the core–accessory null result especially cautious for species with fewer than 20 genomes. [src: amr_fitness_cost]

The finding therefore does not establish that conservation is unrelated to fitness under every ecological or genetic context; it shows that the available pangenome labels did not explain the measured baseline knockout-fitness distributions in this dataset. [src: amr_fitness_cost] This qualification connects the concept to [[concepts/pangenome-integration]] and [[concepts/condition-specific-fitness]], where denser sampling and condition-specific measurements could reveal relationships hidden by broad conservation categories or averaged fitness values. [src: amr_fitness_cost]

## Tensions

The data contain an apparent tension: mechanism strongly predicted conservation status, yet mechanism did not predict baseline fitness cost. [src: amr_fitness_cost] This is not a statistical contradiction because conservation status and knockout fitness are different response variables, but it means that a mechanism-associated distribution pattern cannot be treated as evidence for a mechanism-associated fitness burden. [src: amr_fitness_cost]

## Open Directions

- Use the 144 metal-resistance genes with fitness measurements and compare their standard-condition costs with responses in the metal fitness atlas, using metal-specific fitness analyses to ask whether genes that appear costly under standard conditions are protective under metal stress. [src: amr_fitness_cost]
- Recalculate core/accessory labels from expanded GTDB sampling and test the association with fitness using prevalence thresholds and species-stratified models, asking whether the null result persists when the median sample of 9 genomes is replaced by broader within-species coverage. [src: amr_fitness_cost]
- Analyze mechanism effects within organisms with many AMR genes, including Cup4G11 (77) and BFirm (50), using genetic-background-controlled comparisons to ask whether conservation–cost relationships emerge within species. [src: amr_fitness_cost]
- Extend the analysis from 25 Fitness Browser organisms to all 293K BERDL genomes by predicting AMR cost from gene-cluster conservation patterns, then test whether predicted cost varies with pangenome prevalence outside the lab-adapted strains. [src: amr_fitness_cost]
