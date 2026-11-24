---
type: "Concept"
description: "Whether a genomically complete metabolic pathway is actually needed for growth, comparing GapMind pathway-completeness predictions with measured growth and RB-TnSeq fitness, including pathway-to-gene mapping and coverage limits; stops at pangenome-level evolutionary inference."
sources: ["summaries/discoveries.md", "summaries/essential_metabolome__REPORT.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Metabolic capability versus fitness dependency

A genome that encodes a complete pathway does not necessarily depend on it. [src: pathway_capability_dependency] This page compares GapMind pathway-completeness predictions with Fitness Browser (FB) growth and random barcode transposon sequencing (RB-TnSeq) fitness. The main evidence is one analysis of 7 organisms. [src: pathway_capability_dependency] Latent Capability, meaning a complete pathway with no significant fitness defect under standard conditions, is the largest class at 41.0% (66/161) of pairs. [src: pathway_capability_dependency] Condition-specific reanalysis moves all 66 into fitness-important status under at least one condition type. [src: pathway_capability_dependency] A single-organism check found perfect agreement with growth. [src: fw300_metabolic_consistency] Mapping and coverage limits restrict both results. See also [[concepts/latent-metabolic-capability-versus-fitness-dependency]] and [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].

## Capability is not dependency

The pathway_capability_dependency report concludes that genomic capability and metabolic dependency are distinct, because a complete pathway does not guarantee dependence under any given condition. [src: pathway_capability_dependency] It classifies pathways by two tests. Completeness means GapMind predicts the pathway complete in >50% of conspecific genomes. [src: pathway_capability_dependency] Fitness importance means the composite importance score exceeds a data-driven median threshold. [src: pathway_capability_dependency] The score weights essentiality at 40%, fitness breadth at 30% and fitness magnitude at 30%. [src: pathway_capability_dependency]

The classes are Active Dependency (complete and important), Latent Capability (complete but not important), Incomplete but Important, and Missing. [src: pathway_capability_dependency] The data cover 161 organism-pathway pairs from 7 FB organisms and 23 GapMind pathways. [src: pathway_capability_dependency]

| Class | Pairs | Share |
|---|---|---|
| Active Dependency | 57 | 35.4% [src: pathway_capability_dependency] |
| Latent Capability | 66 | 41.0% [src: pathway_capability_dependency] |
| Incomplete but Important | 24 | 14.9% [src: pathway_capability_dependency] |
| Missing | 14 | 8.7% [src: pathway_capability_dependency] |

The report reads the 41% Latent Capability rate as suggesting that nearly half of complete pathways are conditionally dispensable. [src: pathway_capability_dependency] Condition-type stratification splits fitness effects into nitrogen source, carbon source, stress and other conditions. [src: pathway_capability_dependency] Under it, all 66 Latent Capability pairs become fitness-important under at least one condition type. [src: pathway_capability_dependency] Nitrogen limitation, stress and carbon limitation most often trigger the reclassification. [src: pathway_capability_dependency] Nitrogen limitation and stress are the most frequent triggers. This fits the expectation that amino acid biosynthesis pathways are critical when nutrients are scarce but dispensable in rich media. [src: pathway_capability_dependency] The report therefore calls these pathways conditionally active rather than genomic baggage. [src: pathway_capability_dependency] The discoveries digest reads this as validating the core_gene_tradeoffs finding that laboratory fitness underestimates natural selection on metabolic genes. [src: discoveries]

Two caveats limit this. The median threshold splits pathways about 50/50 by construction. [src: pathway_capability_dependency] The "all become important" result may partly reflect inevitable threshold crossing when a median threshold is applied to enough condition subsets. [src: pathway_capability_dependency] Calibrating against an independent set, such as known essentials from essential_metabolome, would give a more defensible threshold. [src: pathway_capability_dependency]

Incomplete but Important pairs are pathways that GapMind scores incomplete but whose mapped genes matter for fitness. The report suggests annotation gaps or salvage routes as the explanation. [src: pathway_capability_dependency]

## Agreement in one organism

In Pseudomonas FW300-N2E3, GapMind predicted complete pathways for all 13 metabolites that could be mapped: lactate, valine, alanine, arginine, aspartate, glutamic acid, glycine, phenylalanine, proline, trehalose, tryptophan, malate and lysine. [src: fw300_metabolic_consistency] All 13 also showed growth in FB experiments. [src: fw300_metabolic_consistency] The report takes this perfect agreement as validating GapMind for this organism. [src: fw300_metabolic_consistency] It cites Price et al. (2022) for high GapMind accuracy against fitness data. [src: fw300_metabolic_consistency] It also states that GapMind 2024 improved amino acid biosynthesis annotations and that pangenome-level predictions in the KBase Data Lakehouse inherit this accuracy. [src: fw300_metabolic_consistency]

For tryptophan, the report notes that GapMind predicts a complete biosynthesis pathway in FW300-N2E3. It separately notes that 0 of 50 *P. fluorescens* strains in BacDive can use tryptophan as a carbon source. [src: fw300_metabolic_consistency] These are different phenotypes (biosynthesis versus carbon-source use) and the BacDive strains are not FW300-N2E3, so this does not contradict the growth concordance above.

## Pathway-to-gene mapping

The pathway_capability_dependency report maps FB genes to GapMind pathways through FB-native KEGG annotations. The chain is besthitkegg to keggmember to EC (Enzyme Commission) to KEGG map to GapMind pathway. It does not use the pangenome link table. [src: pathway_capability_dependency] Genes with missing or incorrect KEGG annotations are missed. This may underestimate the true number of genes per pathway. [src: pathway_capability_dependency]

The metabolic_capability_dependency report computed pathway fitness metrics for 48 FB organisms across proteobacteria, firmicutes and other phyla. [src: metabolic_capability_dependency] It used SEED subsystem annotations as a proxy to map GapMind pathway members to FB genes. [src: metabolic_capability_dependency] This introduces false positives from related subsystems. They dilute the fitness signal and may misclassify pathways that differ in conservation. [src: metabolic_capability_dependency]

The SEED proxy also left gaps:

- Deoxyribonate and myoinositol had no matching SEED roles and are absent from all analyses. [src: metabolic_capability_dependency]
- Phenylalanine and tyrosine lacked SEED coverage under their full names. They are included through the phe and tyr abbreviations. [src: metabolic_capability_dependency]
- Alanine was excluded from classification for all organisms, because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [src: metabolic_capability_dependency]

The report proposes using GapMind's per-step gene assignments instead. This would improve mapping precision and reduce false positives. [src: metabolic_capability_dependency] The FW300-N2E3 report likewise deferred its planned NB04 analysis. That analysis would map fitness genes to GapMind steps. It would show whether tryptophan fitness genes are biosynthetic, catabolic or regulatory, and so separate overflow metabolism from active catabolism. [src: fw300_metabolic_consistency]

## Coverage limits

- Only 7 of the 48 FB organisms have matching GapMind genome data. [src: pathway_capability_dependency] These are model organisms with near-complete core genomes, which compresses the conservation validation signal. [src: pathway_capability_dependency]
- Fitness coverage of 48 organisms is a small fraction of the 293,000 genomes with pathway predictions, so results may not generalize across taxa. [src: metabolic_capability_dependency]
- An attempt to link FB organisms to GapMind species clades through NCBI taxonomy IDs returned zero matches. The column held boolean strings, not numeric taxids. [src: metabolic_capability_dependency] Downstream analyses therefore use organism-level aggregates, which may reduce the precision of the H2a conservation comparison. [src: metabolic_capability_dependency]
- The report does not assess cofactor biosynthesis, lipid metabolism or secondary metabolism. [src: pathway_capability_dependency]
- Laboratory media may not reflect the conditions under which pathways are expressed. This may inflate the latent fraction. [src: metabolic_capability_dependency]
- The essential_metabolome report used RB-TnSeq data from rich media. [src: essential_metabolome] Nutrient supplementation may make biosynthetic genes look non-essential. [src: essential_metabolome] That report cannot separate essentiality for biosynthesis from essentiality for viability. [src: essential_metabolome] It leaves open whether complete pathways are essential for viability [src: essential_metabolome] and which pathways are essential only under specific conditions. [src: essential_metabolome]

## Tensions

- Under the default threshold, 41.0% of pairs are Latent Capability. [src: pathway_capability_dependency] Under stratification, all 66 become important somewhere. [src: pathway_capability_dependency] The report warns that the second may partly be a threshold artifact. [src: pathway_capability_dependency]

## Open Directions

- Redo the pathway-to-fitness mapping with GapMind per-step gene assignments. Compare Latent Capability and Incomplete but Important counts against the SEED and KEGG proxies, to measure the false-positive dilution.
- Calibrate the importance threshold against known essentials from essential_metabolome. Then test whether the Latent Capability fraction survives a non-median cutoff.
- Run the deferred NB04 analysis on FW300-N2E3 tryptophan genes, to classify them as biosynthetic, catabolic or regulatory.
- Fix the taxonomy join between FB organisms and GapMind clades, to enable clade-level conservation comparisons. See [[concepts/join-key-validity-and-identifier-format-mismatches]].
- Extend the analysis beyond the 7 organisms with GapMind data, to test generalization across taxa.
