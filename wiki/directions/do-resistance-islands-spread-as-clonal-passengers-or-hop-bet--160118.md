---
type: "Research direction"
description: "Within a species, are tightly co-occurring resistance gene islands concentrated in particular strain lineages, or scattered across lineages like horizontally transferred cassettes? Is that pattern different from single acquired resistance genes?"
hypothesis: "Resistance islands are less lineage-restricted than size-matched sets of independently occurring acquired resistance genes, because they move as a unit on mobile elements. Core, near-universal resistance genes are excluded from the comparison."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Island calls and genome-level resistance gene tables exist, but gain counting on within-species trees and matched null sets need new computation; the largest species (e.g. E. coli) were excluded by size."
collections: ["kbase-ke-pangenome"]
findings: ["amr_strain_variation--065d36b5", "amr_strain_variation--e349ed14", "amr_strain_variation--6ebb7e8b", "amr_strain_variation--f9cc56e8"]
conflicts: []
papers: ["33602143", "20375036", "30068738", "30953542", "39233522"]
builds_on: ["findings/amr_strain_variation--065d36b5", "findings/amr_strain_variation--e349ed14", "findings/amr_strain_variation--6ebb7e8b", "findings/amr_strain_variation--f9cc56e8"]
projects: ["amr_strain_variation"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do resistance islands spread as clonal passengers or hop between bacterial lineages?

Within a species, are tightly co-occurring resistance gene islands concentrated in particular strain lineages, or scattered across lineages like horizontally transferred cassettes? Is that pattern different from single acquired resistance genes?

## Hypothesis

Resistance islands are less lineage-restricted than size-matched sets of independently occurring acquired resistance genes, because they move as a unit on mobile elements. Core, near-universal resistance genes are excluded from the comparison.

## Why it matters

More than half of species carry such islands, yet it is unknown whether they are inherited with the strain or repeatedly gained. The answer decides whether surveillance should track strain lineages or the islands themselves, and excluding near-universal core genes removes a partly artefactual contribution to earlier lineage-signal differences.

## How to test it

In the species with at most 500 genomes, take the detected islands and compare their distribution on the within-species genome-distance tree with that of random sets of non-core resistance genes matched on size and prevalence. Count how many separate times each island appears to have been gained along the tree. Check whether the same island appears in several species in the Pangenome Collection, and compare island-carrying species to those without islands.

## What would support or refute it

Support: islands show more independent gains and weaker clustering by lineage than matched acquired gene sets, and recur across species. Refute: islands are as lineage-restricted as, or more than, matched gene sets, which implies mostly clonal inheritance.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Island calls and genome-level resistance gene tables exist, but gain counting on within-species trees and matched null sets need new computation; the largest species (e.g. E. coli) were excluded by size.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_strain_variation--065d36b5|Tightly co-occurring resistance islands are detected in over half of species]] (Insufficient literature evidence)
- Finding: [[findings/amr_strain_variation--e349ed14|Putatively acquired AMR genes show stronger phylogenetic signal than core genes]] (Candidate novel)
- Finding: [[findings/amr_strain_variation--6ebb7e8b|Over half of species show significant ANI–AMR phylogenetic signal]] (Insufficient literature evidence)
- Finding: [[findings/amr_strain_variation--f9cc56e8|Most within-species AMR gene occurrences are rare or variable, rarely fixed]] (Insufficient literature evidence)

## Closest published work

- [PMID 33602143](https://pubmed.ncbi.nlm.nih.gov/33602143/) Genomic islands mediate environmental adaptation and the spread of antibiotic resistance in multiresistant Enterococci - evidence from genomic sequences.
- [PMID 20375036](https://pubmed.ncbi.nlm.nih.gov/20375036/) Evolution of AbaR-type genomic resistance islands in multiply antibiotic-resistant Acinetobacter baumannii.
- [PMID 30068738](https://pubmed.ncbi.nlm.nih.gov/30068738/) Mobile Genetic Elements Associated with Antimicrobial Resistance.
- [PMID 30953542](https://pubmed.ncbi.nlm.nih.gov/30953542/) Culture-enriched human gut microbiomes reveal core and accessory resistance genes.
- [PMID 39233522](https://pubmed.ncbi.nlm.nih.gov/39233522/) Comparative Genomic Analyses of E. coli ST2178 Strains Originated from Wild Birds in Pakistan.

PMID 33602143 and PMID 20375036 follow resistance islands in single genera or species, and PMID 39233522 shows resistance genes tracking mobile elements in one E. coli lineage; none compares island lineage-restriction with matched acquired genes across hundreds of species.
