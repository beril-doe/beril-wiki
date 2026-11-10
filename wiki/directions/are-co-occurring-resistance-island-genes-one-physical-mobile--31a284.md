---
type: "Research direction"
description: "Do the tightly co-occurring members of resistance islands sit next to each other on the chromosome or plasmid, or are they scattered loci that merely travel together across strains?"
hypothesis: "Island members that co-occur across distantly related strains are physically contiguous, consistent with one mobile element, whereas members that co-occur only loosely are scattered, so tight co-occurrence mostly reflects linkage and not co-selection of separate genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Island calls and strain-level presence/absence exist, but gene positions must be retrieved and joined to the island members and lineage-stratified tests run."
collections: ["kbase-ke-pangenome"]
findings: ["amr_strain_variation--065d36b5", "amr_strain_variation--f9cc56e8", "amr_strain_variation--e349ed14"]
conflicts: []
papers: ["33602143", "20375036", "30068738", "36466658"]
builds_on: ["findings/amr_strain_variation--065d36b5", "findings/amr_strain_variation--f9cc56e8", "findings/amr_strain_variation--e349ed14"]
projects: ["amr_strain_variation"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Are co-occurring resistance island genes one physical mobile unit or separate co-selected loci?

Do the tightly co-occurring members of resistance islands sit next to each other on the chromosome or plasmid, or are they scattered loci that merely travel together across strains?

## Hypothesis

Island members that co-occur across distantly related strains are physically contiguous, consistent with one mobile element, whereas members that co-occur only loosely are scattered, so tight co-occurrence mostly reflects linkage and not co-selection of separate genes.

## Why it matters

More than half of species carry resistance islands with very tight co-occurrence, but co-occurrence alone does not show co-selection. Knowing whether tightness reflects physical linkage tells us which resistance genes spread as one package and which are assembled by selection.

## How to test it

In the Pangenome Collection, for the 705 species with islands, retrieve gene positions on contigs for island members and measure how often members are adjacent versus separated. Relate adjacency to how consistently the members co-occur across distant strain clusters, and to how many independent lineages carry the full island versus partial sets. Compare against matched random gene sets of the same size and prevalence.

## What would support or refute it

Support: tight co-occurrence across many unrelated lineages goes with physical contiguity, and loosely co-occurring members are scattered. Refutation: scattered members also co-occur as tightly as contiguous ones, which would point to co-selection of separate loci, or co-occurrence is high only within clades.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Island calls and strain-level presence/absence exist, but gene positions must be retrieved and joined to the island members and lineage-stratified tests run.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_strain_variation--065d36b5|Tightly co-occurring resistance islands are detected in over half of species]] (Insufficient literature evidence)
- Finding: [[findings/amr_strain_variation--f9cc56e8|Most within-species AMR gene occurrences are rare or variable, rarely fixed]] (Insufficient literature evidence)
- Finding: [[findings/amr_strain_variation--e349ed14|Putatively acquired AMR genes show stronger phylogenetic signal than core genes]] (Candidate novel)

## Closest published work

- [PMID 33602143](https://pubmed.ncbi.nlm.nih.gov/33602143/) Genomic islands mediate environmental adaptation and the spread of antibiotic resistance in multiresistant Enterococci - evidence from genomic sequences.
- [PMID 20375036](https://pubmed.ncbi.nlm.nih.gov/20375036/) Evolution of AbaR-type genomic resistance islands in multiply antibiotic-resistant Acinetobacter baumannii.
- [PMID 30068738](https://pubmed.ncbi.nlm.nih.gov/30068738/) Mobile Genetic Elements Associated with Antimicrobial Resistance.
- [PMID 36466658](https://pubmed.ncbi.nlm.nih.gov/36466658/) Pan-genomic analysis of Corynebacterium amycolatum gives insights into molecular mechanisms underpinning the transition to a pathogenic phenotype.

PMID 33602143 and PMID 20375036 describe resistance islands in single species. This direction asks, across hundreds of species, whether tight co-occurrence reflects physical linkage on one element or co-selection of separate loci.
