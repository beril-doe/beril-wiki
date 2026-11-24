---
type: "Organism"
description: "Alphaproteobacterium with all 18 amino acid pathways complete in GapMind."
sources: ["summaries/amr_fitness_cost__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/discoveries.md", "summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
aliases: ["S. meliloti", "Smeli"]
---
# Sinorhizobium meliloti

Sinorhizobium meliloti (also S. meliloti, Smeli) is an alphaproteobacterium. It has all 18 amino acid pathways complete in GapMind. [src: essential_metabolome] It is one of the Fitness Browser organisms used in several projects, and it ranks first for conservation-weighted dark-gene prioritization. [src: discoveries, functional_dark_matter, pathway_capability_dependency]

## Key facts

- GapMind reports 18/18 amino acid pathways complete (100%) for Smeli. [src: essential_metabolome] See [[concepts/conservation-of-amino-acid-biosynthesis-pathways-across-bacteria]].
- The genome is GCF_000006965.1, with 1,735 GapMind predictions, and it is present in the collection. [src: essential_metabolome]
- It is one of seven Fitness Browser organisms in the Tier 1 pathway analysis, which required available GapMind pathway data. [src: pathway_capability_dependency] The others include [[entities/caulobacter-crescentus]] and [[entities/azospirillum-brasilense]]. [src: pathway_capability_dependency]

## Genome sampling and AMR

The AMR (antimicrobial resistance) fitness-cost report names S. meliloti, with 241 genomes, as a well-sampled species for conservation analysis. [src: amr_fitness_cost] See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]].

## Co-fitness and co-inheritance

The extracted Smeli dataset had 241 genomes, 6,004 clusters and 528,699 cofit pairs, and it included a phylogenetic tree. [src: cofitness_coinheritance] For 230,516 cofit pairs, mean phi was 0.029, against 0.026 for random pairs. The delta was +0.002 and the two-sided p-value was <1e-17. [src: cofitness_coinheritance] See [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]].

## Dark-gene prioritization

S. meliloti ranks first in the conservation-weighted covering set (Route B), with 1,630 ortholog groups (OGs) and 195 kingdom-level gaps. [src: discoveries, functional_dark_matter] The reason given is its broader coverage of conserved unknowns. [src: discoveries] The functional dark matter report says its dark genes span the most kingdom-level true knowledge gaps. These are broadly conserved genes with zero functional evidence. Its tractability is 0.6. [src: functional_dark_matter]

The next two organisms in Route B are P. putida, with 1,043 OGs and 172 kingdom gaps, and MR-1, with 805 OGs and 105 kingdom gaps. [src: functional_dark_matter] B. thetaiotaomicron has a higher raw count, 1,382 genes and 267 kingdom gaps. It is deprioritized by its 0.3 tractability. [src: functional_dark_matter]

In Route A, S. meliloti is third, with 570 genes and tractability 0.6. It covers a distinct lineage, Alphaproteobacteria, with 316 T4 Penumbra and 90 T5 Dawn genes. [src: functional_dark_matter] See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]] and [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]].
