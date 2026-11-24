---
type: "Organism"
description: "The soil Pseudomonas strain FW300-N2E3 (Fitness Browser pseudo3_N2E3) whose metabolite production, fitness, pathway predictions and co-inheritance were integrated across databases."
sources: ["summaries/cofitness_coinheritance__REPORT.md", "summaries/discoveries.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
aliases: ["FW300-N2E3", "Pseudomonas FW300-N2E3", "Pseudomonas fluorescens N2E3", "Pseudomonas sp. FW300-N2E3", "pseudo3_N2E3"]
---
# Pseudomonas fluorescens FW300-N2E3

This page covers the soil Pseudomonas strain FW300-N2E3 (Fitness Browser pseudo3_N2E3), whose metabolite production, fitness, pathway predictions and co-inheritance were integrated across databases. In Web of Microbes (WoM) it is an exact strain match to pseudo3_N2E3, with 5,854 genes and 211 experiments. [src: discoveries, webofmicrobes_explorer] The reports note that the high cross-database concordance is largely inevitable by construction. [src: discoveries]

## Key facts

- It was isolated from groundwater at the Oak Ridge Field Research Center (ENIGMA SFA), where it lives in complex microbial communities. [src: fw300_metabolic_consistency]
- The two directly matched WoM Pseudomonas strains are ENIGMA groundwater isolates. [src: webofmicrobes_explorer]
- The extracted pseudo3_N2E3 co-inheritance dataset had 40 genomes, 5,513 clusters and 507,828 cofit pairs, without a phylogenetic tree. [src: cofitness_coinheritance]

## Metabolite production and cross-database concordance

Of 58 WoM metabolites (27 Emerged, 31 Increased), 21 could be cross-referenced against at least one other database. [src: fw300_metabolic_consistency] Among these, 17/21 (81%) were fully concordant, 4/21 (19%) partially concordant, none fully discordant, and the mean concordance score was 0.94. [src: fw300_metabolic_consistency] A separate report counted 37/41 concordant comparisons overall (90.2%). [src: discoveries]

The discoveries digest says this concordance is largely inevitable. Fitness Browser (FB) always shows growth for metabolites used as sole C/N sources, and GapMind predicts complete pathways for common amino acids. [src: discoveries] The 94% mean decomposes into FB 21/21 = 100% (structural), GapMind 13/13 = 100% (structural) and BacDive 3/7 = 43% (informative). [src: discoveries] All 13 metabolites mapped to GapMind had complete predictions and growth in FB. [src: discoveries] The matched metabolites were common amino acids and organic acids with well-characterized pathways. [src: discoveries] A binomial test found BacDive utilization of WoM-produced metabolites (43%) not significantly different from the species baseline (27.5%), p=0.40. [src: discoveries] See [[concepts/cross-database-concordance-of-metabolite-evidence]].

A third report's curated matching found 19 metabolites produced in WoM and tested as FB carbon or nitrogen sources: 5 de novo products (E) and 14 amplified (I). [src: webofmicrobes_explorer] This 19 differs from the 21 above, and the claims do not say why. See [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments]].

## Fitness

Across 21 WoM metabolites with matching FB experiments, the strain had significant fitness effects (|fit| > 1, |t| > 4) for 601 unique genes, with 4,764 gene-condition hits. [src: fw300_metabolic_consistency] The top 18 genes significant across all 21 conditions were amino acid biosynthesis enzymes, including homoserine O-acetyltransferase, ATP (adenosine triphosphate) phosphoribosyltransferase, dihydroxy-acid dehydratase, isopropylmalate dehydrogenase, shikimate dehydrogenase and imidazoleglycerol-phosphate dehydratase. [src: discoveries] The report says these are essential on any minimal medium. [src: discoveries] It identifies the ~370 genes significant in only 1-2 conditions as the truly substrate-specific ones. [src: discoveries] See [[concepts/housekeeping-versus-substrate-specific-fitness-genes]].

## Tryptophan overflow

The strain increases tryptophan in WoM, has 231 genes with significant fitness on tryptophan in FB, and has a GapMind-predicted complete biosynthesis pathway. [src: discoveries, fw300_metabolic_consistency] Yet 0/52 P. fluorescens strains in BacDive use tryptophan as a carbon source in one report, and 0 of 50 in another. [src: discoveries, fw300_metabolic_consistency] The reports propose a tryptophan overflow hypothesis from these four lines. [src: fw300_metabolic_consistency] The digest argues this makes a compelling case for cross-feeding or signaling rather than catabolism. [src: discoveries] See [[concepts/metabolite-production-versus-utilization-discordance]] and [[entities/tryptophan]].

## Co-inheritance of cofit genes

For pseudo3_N2E3, 31,959 cofit pairs had mean phi 0.458 versus 0.433 for random pairs (delta +0.026, p 6.6e-16). [src: cofitness_coinheritance] The module analysis listed 40 modules, 4 (10%) significant, mean phi 0.444 and null mean 0.409. [src: cofitness_coinheritance] Species with more gene-content diversity (Ddia6719, pseudo3_N2E3) show the largest positive deltas. [src: cofitness_coinheritance] Its ANI (average nucleotide identity) is 99.66%, and it also shows a positive delta (+0.026). [src: cofitness_coinheritance] See [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]].

## Role in the metal fitness atlas

Multiple P. fluorescens strains inflate apparent conservation through phylogenetic non-independence. [src: metal_fitness_atlas] Removing 4 duplicate FW300 strains while keeping pseudo3_N2E3 reduces the analysis from 22 to 18 organisms. [src: metal_fitness_atlas] It is the only atlas organism with a negligible negative core-fraction delta (-0.003, p=0.70). [src: metal_fitness_atlas] Oak Ridge FW300 Pseudomonas strains came from Cr-contaminated groundwater but have never been tested against chromate. [src: metal_fitness_atlas]

## Proposed work

The WoM explorer report proposes identifying fitness-important genes on self-produced carbon sources in pseudo3_N2E3 and pseudo13_GW456_L13, to test whether metabolic output predicts gene essentiality. [src: webofmicrobes_explorer]
