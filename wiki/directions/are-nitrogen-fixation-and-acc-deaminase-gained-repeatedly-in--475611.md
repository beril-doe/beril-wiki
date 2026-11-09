---
type: "Research direction"
description: "Within genera that contain both plant-associated and non-plant genomes, do nitrogen fixation and ACC deaminase arise independently several times on plant-associated branches?"
hypothesis: "Nitrogen fixation and ACC deaminase, which stayed linked to plant association within genera, show repeated independent gains on plant-associated branches, whereas markers that lost association within genera reflect deep shared ancestry. The type III secretion system, whose within-genus support was weaker and would be lost under a stricter correction, serves as a borderline comparison."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Presence data exist but only a minority of plant-associated species have tree data, so genus trees must be built."
collections: ["kbase-ke-pangenome"]
findings: ["plant_microbiome_ecotypes--223dadd3", "plant_microbiome_ecotypes--8106ac12", "plant_microbiome_ecotypes--64143b61"]
conflicts: ["conflict--ecotype-environment-gene-content--aa91ad15"]
papers: ["29255260", "22792073", "35536128", "32040377"]
builds_on: ["findings/plant_microbiome_ecotypes--223dadd3", "findings/plant_microbiome_ecotypes--8106ac12", "findings/plant_microbiome_ecotypes--64143b61", "conflicts/conflict--ecotype-environment-gene-content--aa91ad15"]
projects: ["plant_microbiome_ecotypes", "prophage_ecology"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Are nitrogen fixation and ACC deaminase gained repeatedly in plant-associated lineages within genera?

Within genera that contain both plant-associated and non-plant genomes, do nitrogen fixation and ACC deaminase arise independently several times on plant-associated branches?

## Hypothesis

Nitrogen fixation and ACC deaminase, which stayed linked to plant association within genera, show repeated independent gains on plant-associated branches, whereas markers that lost association within genera reflect deep shared ancestry. The type III secretion system, whose within-genus support was weaker and would be lost under a stricter correction, serves as a borderline comparison.

## Why it matters

Most plant-enriched markers lost their association when comparisons were kept within genera, yet two held up clearly. Repeated gains would mark them as real plant adaptation, and would clarify why plant-associated genera carry more mobile elements even though beneficial clusters are mostly core.

## How to test it

In the Pangenome Collection, for genera containing both plant-associated and non-plant genomes, reconstruct gains and losses of nitrogen fixation, ACC deaminase, the type III secretion system and non-surviving markers on genus phylogenies. Count independent gains and test whether gains are concentrated on plant-associated branches. Check whether gains sit near mobile-element genes.

## What would support or refute it

Support: the two clearly surviving markers show multiple independent gains on plant-associated branches and non-surviving markers do not. Refutation: gains are single and ancestral, or equally frequent on non-plant branches.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Presence data exist but only a minority of plant-associated species have tree data, so genus trees must be built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/plant_microbiome_ecotypes--223dadd3|Only three plant markers survive strict within-genus permutation]] (Insufficient literature evidence)
- Finding: [[findings/plant_microbiome_ecotypes--8106ac12|Nearly all top plant-enriched gene families persist after phylum and genome-size control]] (Insufficient literature evidence)
- Finding: [[findings/plant_microbiome_ecotypes--64143b61|Two Xanthomonas species segregate by plant host across subclades]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--aa91ad15|Core-Dominated Beneficial Clusters vs. Elevated Mobilome Burden in Plant-Associated Genera]]

## Closest published work

- [PMID 29255260](https://pubmed.ncbi.nlm.nih.gov/29255260/) Genomic features of bacterial adaptation to plants.
- [PMID 22792073](https://pubmed.ncbi.nlm.nih.gov/22792073/) Comparative genomics of plant-associated Pseudomonas spp.: insights into diversity and inheritance of traits involved in multitrophic interactions.
- [PMID 35536128](https://pubmed.ncbi.nlm.nih.gov/35536128/) Cruciferous Weed Isolates of Xanthomonas campestris Yield Insight into Pathovar Genomic Relationships and Genetic Determinants of Host and Tissue Specificity.
- [PMID 32040377](https://pubmed.ncbi.nlm.nih.gov/32040377/) Genomic Acquisitions in Emerging Populations of Xanthomonas vasicola pv. vasculorum Infecting Corn in the United States and Argentina.

PMID 29255260 and PMID 22792073 describe genomic features of plant adaptation using broader comparisons. This direction tests whether gains are repeated within genera, which separates adaptation from inherited ancestry.
