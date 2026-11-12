---
type: "Research direction"
description: "In many species, resistance genes fall into groups that almost always occur together across genomes, and acquired genes follow the family tree more closely than intrinsic ones. Are these co-occurring groups gained once in a lineage and then inherited, or regained many times independently?"
hypothesis: "Most co-occurring groups arise from a single gain per clade followed by inheritance, so independent gains are few. Groups in species with weak lineage signal show many more independent gains."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Group calls and genome-level presence exist; ancestral reconstruction on core trees must still be run, and tree coverage limits which species qualify."
collections: ["kbase-ke-pangenome"]
findings: ["amr_strain_variation--065d36b5", "amr_strain_variation--e349ed14", "amr_strain_variation--f9cc56e8"]
conflicts: []
papers: ["33602143", "20375036", "20805406", "30953542"]
builds_on: ["findings/amr_strain_variation--065d36b5", "findings/amr_strain_variation--e349ed14", "findings/amr_strain_variation--f9cc56e8"]
projects: ["amr_strain_variation"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Are co-occurring resistance gene groups gained once per lineage, or repeatedly?

In many species, resistance genes fall into groups that almost always occur together across genomes, and acquired genes follow the family tree more closely than intrinsic ones. Are these co-occurring groups gained once in a lineage and then inherited, or regained many times independently?

## Hypothesis

Most co-occurring groups arise from a single gain per clade followed by inheritance, so independent gains are few. Groups in species with weak lineage signal show many more independent gains.

## Why it matters

The groups are defined only by co-occurrence, so the finding itself cannot say whether they are linked on one mobile element. A tree-based gain count would show whether co-occurrence mostly reflects shared ancestry or repeated transfer. That determines whether surveillance should follow strains or movable elements.

## How to test it

For species in the Pangenome Collection that have a core-genome tree and detected co-occurring groups, reconstruct presence of each group along the tree and count independent gains and losses per group. Compare species with strong lineage signal against those with weak signal. As a baseline, compare each group with size-matched sets of acquired resistance genes that do not co-occur tightly. Species without tree data cannot be included.

## What would support or refute it

Support: most groups show one gain per clade, and strong-lineage-signal species have fewer independent gains than weak-signal species. Refute: groups show many independent gains regardless of lineage signal, or no more gains than the matched baseline sets, pointing to repeated transfer or to co-occurrence that is not specific to these groups.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Group calls and genome-level presence exist; ancestral reconstruction on core trees must still be run, and tree coverage limits which species qualify.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_strain_variation--065d36b5|Tightly co-occurring resistance islands are detected in over half of species]] (Insufficient literature evidence)
- Finding: [[findings/amr_strain_variation--e349ed14|Putatively acquired AMR genes show stronger phylogenetic signal than core genes]] (Candidate novel)
- Finding: [[findings/amr_strain_variation--f9cc56e8|Most within-species AMR gene occurrences are rare or variable, rarely fixed]] (Insufficient literature evidence)

## Closest published work

- [PMID 33602143](https://pubmed.ncbi.nlm.nih.gov/33602143/) Genomic islands mediate environmental adaptation and the spread of antibiotic resistance in multiresistant Enterococci - evidence from genomic sequences.
- [PMID 20375036](https://pubmed.ncbi.nlm.nih.gov/20375036/) Evolution of AbaR-type genomic resistance islands in multiply antibiotic-resistant Acinetobacter baumannii.
- [PMID 20805406](https://pubmed.ncbi.nlm.nih.gov/20805406/) Mobility of plasmids.
- [PMID 30953542](https://pubmed.ncbi.nlm.nih.gov/30953542/) Culture-enriched human gut microbiomes reveal core and accessory resistance genes.

PMID 33602143 and PMID 20375036 describe resistance islands in single species or lineages, and PMID 20805406 relates plasmid mobility to host relatedness; none counts independent gains of co-occurring resistance gene groups across many species.
