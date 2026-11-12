---
type: "Research direction"
description: "Gene content predicted growth for amino acids, tryptophan, nucleosides and carbon sources, but not for metals, antibiotics or nitrogen sources. Is predictability set by how many genes, and how conserved, a condition requires, given that the predictive gene groups act as genus-level proxies rather than individually established causal genes?"
hypothesis: "Condition classes served by a few dedicated, widely shared genes (biosynthesis of amino acids and nucleosides) are predictable from gene content. Classes that depend on many diffuse, lineage-specific genes (metals, antibiotics) are not. The predictive gene groups are combinations of variable-prevalence genes that stand in for genus, so any link to fitness genes is expected to be partial."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Fitness data, pangenome conservation and the growth panel are in the lakehouse, but the per-class gene counts and within-genus comparisons must be computed and aligned across organisms."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome", "enigma-coral"]
findings: ["genotype_to_phenotype_enigma--602fd76d", "genotype_to_phenotype_enigma--ccab2bff"]
conflicts: []
papers: ["29769716", "25968644", "36097170"]
builds_on: ["findings/genotype_to_phenotype_enigma--602fd76d", "findings/genotype_to_phenotype_enigma--ccab2bff"]
projects: ["genotype_to_phenotype_enigma"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does growth predictability from gene content track how many genes a condition class needs?

Gene content predicted growth for amino acids, tryptophan, nucleosides and carbon sources, but not for metals, antibiotics or nitrogen sources. Is predictability set by how many genes, and how conserved, a condition requires, given that the predictive gene groups act as genus-level proxies rather than individually established causal genes?

## Hypothesis

Condition classes served by a few dedicated, widely shared genes (biosynthesis of amino acids and nucleosides) are predictable from gene content. Classes that depend on many diffuse, lineage-specific genes (metals, antibiotics) are not. The predictive gene groups are combinations of variable-prevalence genes that stand in for genus, so any link to fitness genes is expected to be partial.

## Why it matters

It would explain which phenotypes can be read from genomes and which need direct measurement. It would also tell experimenters where genome-based prediction can replace growth assays, while showing how far the predictive gene groups reflect mechanism rather than lineage.

## How to test it

For the Oak Ridge isolate growth panel in ENIGMA CORAL and the 343 tested conditions, use Fitness Browser data for the organisms the model work names (for example Cupriavidus Cup4G11 and Pseudomonas N1B4). For each condition class count genes with strong fitness effects and the share of them that are core in the Pangenome Collection. Test whether these two numbers explain which classes were predictable, including the 95 conditions that were. Treat the predictive gene groups as genus-level proxies: for each class also measure how much the predictive groups overlap the fitness genes, noting that this overlap ranged from 1.72 times chance in Cup4G11 to 0.83 times in N1B4, and check whether class predictability still tracks gene number when the comparison is restricted to within-genus variation. Order the classes before looking at prediction results.

## What would support or refute it

Support: classes with few, conserved fitness genes are predictable and classes with many, accessory fitness genes are not, across classes and across organisms, with the relation surviving within genera. Refute: predictability is unrelated to gene number and conservation, or the relation disappears within genera, which would point to lineage structure or measurement noise rather than gene requirements.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Fitness data, pangenome conservation and the growth panel are in the lakehouse, but the per-class gene counts and within-genus comparisons must be computed and aligned across organisms.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--602fd76d|Binary growth is predictable from gene content only for some condition classes]] (Insufficient literature evidence)
- Finding: [[findings/genotype_to_phenotype_enigma--ccab2bff|Continuous growth parameters are not predictable across genera from gene content]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.

PMID 29769716 and PMID 25968644 provide genome-wide mutant fitness across diverse bacteria, and PMID 36097170 shows essentiality is strain-dependent in a bacterial pan-genome. None asks why some condition classes are predictable from gene content and others are not.
