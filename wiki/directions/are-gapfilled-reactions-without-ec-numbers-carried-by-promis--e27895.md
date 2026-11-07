---
type: "Research direction"
description: "Why were only a minority of gapfilled reactions with no EC number resolved to a gene, compared with most reactions that have one: are their enzymes unknown families, or known families acting on unusual substrates?"
hypothesis: "Most unresolved EC-less reactions are catalysed by members of characterised enzyme families acting on a similar substrate, and the matching carbon-source fitness phenotypes point to those family members."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Reactions, fitness data and annotations are in the lakehouse, but the similarity search over reactions needs new computation."
collections: ["kbase-msd-biochemistry", "kescience-fitnessbrowser", "kbase-uniprot", "kbase-ke-pangenome"]
findings: ["annotation_gap_discovery--61f3d4be", "annotation_gap_discovery--ccaed616"]
conflicts: []
papers: ["30910961", "25968644"]
builds_on: ["findings/annotation_gap_discovery--61f3d4be", "findings/annotation_gap_discovery--ccaed616"]
projects: ["annotation_gap_discovery"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Are gapfilled reactions without EC numbers carried by promiscuous enzymes of known families?

Why were only a minority of gapfilled reactions with no EC number resolved to a gene, compared with most reactions that have one: are their enzymes unknown families, or known families acting on unusual substrates?

## Hypothesis

Most unresolved EC-less reactions are catalysed by members of characterised enzyme families acting on a similar substrate, and the matching carbon-source fitness phenotypes point to those family members.

## Why it matters

Over half of gapfilled pairs lack a convincing gene candidate, so many models carry reactions with no known enzyme. If promiscuity explains them, annotation can use substrate similarity and existing families. If not, they point to new enzyme families needing discovery.

## How to test it

For the 50 EC-less reactions, use reactive-site similarity in ModelSEED Biochemistry to find the nearest EC-bearing reactions and predict candidate families. Check whether genes of those families in the same organism show fitness defects on the matching carbon source more often than randomly chosen genes of similar family size. Test the best candidates in vitro.

## What would support or refute it

Candidate-family genes enriched for fitness defects on the matching carbon source, and activity in vitro, would support promiscuity. No enrichment over random genes, and no activity, would favour unknown families.

## Data

Approach: analysis then experiment. Readiness: needs compute. Reactions, fitness data and annotations are in the lakehouse, but the similarity search over reactions needs new computation.

- Collection: [[data/kbase-msd-biochemistry|ModelSEED Biochemistry]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/annotation_gap_discovery--61f3d4be|Dark reactions without EC numbers are far harder to resolve]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--ccaed616|Over half of gapfilled pairs remain without a convincing gene candidate]] (Insufficient literature evidence)

## Closest published work

- [PMID 30910961](https://pubmed.ncbi.nlm.nih.gov/30910961/) Enzyme annotation for orphan and novel reactions using knowledge of substrate reactive sites.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

PMID 30910961 annotates orphan reactions from reactive-site knowledge and PMID 25968644 supplies the fitness method; neither checks predictions against matched-substrate fitness for gapfilled reactions across many organisms.
