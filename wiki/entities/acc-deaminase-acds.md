---
type: "Gene_Or_Pathway"
description: "Plant growth-promoting enzyme that modulates plant ethylene signaling and marks root- and soil-associated bacteria."
sources: ["summaries/discoveries.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
aliases: ["ACC deaminase", "acdS"]
---
# ACC deaminase (acdS)

ACC deaminase (acdS) is a plant growth-promoting (PGP) enzyme. Its gene, acdS, modulates plant ethylene signaling at the root interface. [src: discoveries] It shows the strongest compartment-specific enrichment of any single marker in root-associated species. [src: discoveries] It is also enriched in soil/rhizosphere species, and it stays significant in plant-association tests that account for genus and use permutation. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes] ACC stands for 1-aminocyclopropane-1-carboxylate.

## Key facts

- acdS shows the strongest compartment-specific enrichment of any single marker gene, with an odds ratio (OR) of 69.3 in root-associated species. [src: discoveries]
- The enzyme is described as acting on plant ethylene signaling at the root interface. [src: discoveries]
- In the report, acdS stands for ethylene reduction through ACC deaminase. [src: pgp_pangenome_ecology]

## Enrichment in soil, rhizosphere and roots

Across 27K GTDB species, acdS is strongly enriched in soil/rhizosphere environments, with OR = 7.0. [src: discoveries] Prevalence was 15.8% in soil/rhizosphere species versus 2.6% in other environments (OR 7.02, q-value 5.1e-62). [src: pgp_pangenome_ecology] The enrichment survived phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61). [src: pgp_pangenome_ecology] It also held in a strict rhizosphere-only sensitivity analysis, restricted to genomes with "rhizosphere" or "root nodule" in their isolation source (OR = 10.6, q = 7.6e-38). [src: pgp_pangenome_ecology]

In the plant_microbiome_ecotypes report, root species were enriched in ACC deaminase with OR=69, which the report links to ethylene modulation in root colonization. [src: plant_microbiome_ecotypes] The soil figure (OR = 7.0) and the root figure come from different comparisons, so I state each on its own.

The pgp_pangenome_ecology report relates the soil enrichment to Manter et al. (2023), who used direct acdS sequencing to show greater soil abundance of ACCD+ bacteria. [src: pgp_pangenome_ecology] It also cites the ecological model of Glick (1998) and Ravanbakhsh et al. (2017), in which ACC deaminase is specifically advantageous in ethylene-rich root environments. [src: pgp_pangenome_ecology] See [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere]] and [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]].

## Robustness of the plant association

In the genus-cluster-robust plant-association GLM (generalized linear model), ACC deaminase had OR=8.01. [src: plant_microbiome_ecotypes] The table row for acc_deaminase gives coef 2.08, OR 8.01, 95% CI [4.19, 15.32] and a BH-FDR (Benjamini-Hochberg false discovery rate) q of 2.1×10⁻⁹. [src: plant_microbiome_ecotypes] It survived the within-genus plant-label shuffle with perm p < 0.001. [src: plant_microbiome_ecotypes] It is one of three markers in the strongest species-level tier, alongside nitrogen fixation and T3SS (type III secretion system). [src: plant_microbiome_ecotypes] The report says these three are carried by specific plant-associated species within genera where non-plant species do not reliably have them. [src: plant_microbiome_ecotypes] See bacterial nitrogen fixation nif genes and [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

The report assigns medium confidence to ACC deaminase stress relief as a mechanism hypothesis for the beneficial plant-microbiome cohort. [src: plant_microbiome_ecotypes] This is a hypothesis, not a measured mechanism.

## Co-occurrence with pqqC

Across 27K GTDB species, pqqC (phosphate solubilization) and acdS co-occur at OR = 7.24, far stronger than any other PGP gene pair. [src: discoveries] The pgp_pangenome_ecology report gives n = 286 co-occurring species and q = 1.2e-83 for this pair. [src: pgp_pangenome_ecology] In that report, pqqC represents phosphate solubilization through PQQ (pyrroloquinoline quinone) cofactor biosynthesis. [src: pgp_pangenome_ecology] The report finds the pqqC–acdS module strongly rhizosphere-enriched (acdS OR = 7.0). [src: pgp_pangenome_ecology] See [[entities/pyrroloquinoline-quinone-biosynthesis]] and [[concepts/co-occurrence-of-plant-growth-promoting-genes-and-trait-guilds]].

## Pangenome placement and inheritance

acdS clusters were 70.4% core, 13.4% auxiliary and 16.2% singleton (q vs baseline 7.9e-25). [src: pgp_pangenome_ecology] Separately, the report relates its results to Nascimento et al. (2014), whose phylogenetic analysis found predominantly vertical acdS inheritance despite some horizontal transfer events. [src: pgp_pangenome_ecology] It notes that Nascimento et al. documented some acdS horizontal transfer in Proteobacteria. [src: pgp_pangenome_ecology] See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

The plant_microbiome_ecotypes per-marker analysis gives a transposase co-occurrence OR of 6.43 for ACC deaminase markers. Among the markers it names, PGP markers show the strongest horizontal gene transfer (HGT) signal. [src: plant_microbiome_ecotypes] This is a different measure from the pangenome core fraction. See [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]].

## Tensions

- The pangenome report cites Nascimento et al. (2014) for predominantly vertical acdS inheritance despite some horizontal transfer [src: pgp_pangenome_ecology], and reports acdS clusters as 70.4% core. [src: pgp_pangenome_ecology] The plant-microbiome HGT analysis finds ACC deaminase markers co-occurring with transposases (OR=6.43). [src: plant_microbiome_ecotypes] The reports do not reconcile these views.
