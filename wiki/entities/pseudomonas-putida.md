---
type: "Organism"
description: "Fitness Browser organism (Putida) with null pairwise co-inheritance delta."
sources: ["summaries/cofitness_coinheritance__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md", "summaries/thermodynamic_impact__REPORT.md"]
aliases: ["KT2440", "P. putida", "P. putida KT2440", "Putida"]
---
# Pseudomonas putida

This page covers the Fitness Browser organism Pseudomonas putida KT2440 ("Putida"). Its co-fitness pairs show no excess co-inheritance over random pairs. [src: cofitness_coinheritance] The page collects what separate reports measured on it. Most results come from single-organism tables.

## Key facts

- KT2440 is a workhorse for bioremediation and metabolic engineering. [src: metal_fitness_atlas]
- GapMind analysis lists 18/18 amino acid pathways complete (100%). [src: essential_metabolome]
- Its genome is GCF_000007565.2, with 1,041 GapMind predictions. [src: essential_metabolome]
- It is one of 7 Tier 1 Fitness Browser organisms with GapMind pathway data. [src: pathway_capability_dependency]

## Co-fitness and co-inheritance

The extracted dataset held 128 genomes, 5,409 clusters and 458,688 cofit pairs, with a phylogenetic tree. [src: cofitness_coinheritance] For 205,323 cofit pairs, mean phi was 0.171, against 0.171 for random pairs. The delta was -0.000 and the two-sided p-value 0.41, a null result. [src: cofitness_coinheritance] The module analysis listed 38 modules. Of these, 6 (16%) were significant, with mean phi 0.266 against a null mean of 0.202. [src: cofitness_coinheritance] See [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]] and [[summaries/cofitness_coinheritance__REPORT]].

## Metals

Putida has fitness matrices but zero metal experiments. It is the only Fitness Browser organism with no metal data. [src: metal_fitness_atlas] It has the 5th-highest metal gene repertoire score among Fitness Browser organisms (0.707). [src: metal_fitness_atlas] The metal fitness atlas report proposes testing Co, Ni, Cu, Zn, Al, Cr and U. The test would link the atlas to the P. putida engineering literature and validate or refute the 5th-highest metal gene repertoire score (0.707). [src: metal_fitness_atlas] See [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]].

## Aromatic and carbon metabolism

The report describes KT2440 as a well-studied aromatic degrader. It channels diverse aromatic compounds through the β-ketoadipate pathway. [src: respiratory_chain_wiring] The report states that its P. putida aromatic fitness data align with published knowledge of Pseudomonas aromatic catabolism. [src: respiratory_chain_wiring] See [[entities/ketoadipate-pathway]]. Belda et al. (2016) documented 92 catabolic pathways in the re-annotated genome. [src: pseudomonas_carbon_ecology] Nikel & de Lorenzo (2018) emphasized broad carbon source use across sugars, organic acids and aromatics. [src: pseudomonas_carbon_ecology]

The 62 GapMind carbon pathways miss genus-specific capabilities. These include toluene, naphthalene and benzoate degradation, which are central to P. putida ecology. [src: pseudomonas_carbon_ecology] The report hypothesizes that aromatic pathways likely carry stronger environmental signal. [src: pseudomonas_carbon_ecology] See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].

## Dark-gene prioritisation

The dark gene roadmap ranks P. putida after P. putida N2C3 (35 candidates), with 24 candidates. [src: functional_dark_matter] In the conservation-weighted covering set, it follows Sinorhizobium meliloti, with 1,043 ortholog groups (OGs) and 172 kingdom gaps. [src: functional_dark_matter] In Route B it is second, with tractability 0.8. The report credits high tractability combined with deep coverage of conserved unknowns. [src: functional_dark_matter]

PP_3434 has a nitrogen phenotype, |fit| 3.1, human_clinical, odds ratio 28.6 and FDR 7e-6. [src: functional_dark_matter] PP_0642 has a nitrogen phenotype, |fit| 2.8, human_clinical, odds ratio 11.6, FDR 0.001 and universal breadth. [src: functional_dark_matter] PP_3105 has a stress phenotype, |fit| 3.7, carrier environment human_assoc, odds ratio inf and FDR 0.004. [src: functional_dark_matter]

## Metabolic model and thermodynamics

The KT2440 model is Proteobacteria with the GramNeg template, 1,350 genes, 1,494 reactions and growth 0.1667. [src: thermodynamic_impact]
