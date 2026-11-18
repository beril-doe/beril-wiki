---
type: "Research direction"
description: "Do putatively acquired resistance genes track strain relatedness because they pass down clonal lineages, or because they are gained repeatedly in related strains?"
hypothesis: "Acquired resistance genes show more independent gain events per gene than non-resistance accessory genes of matched prevalence, so their stronger relatedness signal does not mean clonal inheritance."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Trees exist for only some species in the catalog (343 listed), and ancestral reconstruction for every gene cluster has to be computed."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.phylogenetic_tree", "kbase.ke_pangenome.bakta_amr", "kbase.ke_pangenome.gene_genecluster_junction", "kbase.ke_pangenome.genome"]
findings: ["amr_strain_variation--e349ed14", "amr_strain_variation--6ebb7e8b", "amr_strain_variation--065d36b5"]
conflicts: []
papers: ["30953542", "20805406", "35801696", "39472795"]
builds_on: ["findings/amr_strain_variation--e349ed14", "findings/amr_strain_variation--6ebb7e8b", "findings/amr_strain_variation--065d36b5"]
projects: ["amr_strain_variation"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Is acquired resistance spread by repeated gene gain rather than clonal inheritance?

Do putatively acquired resistance genes track strain relatedness because they pass down clonal lineages, or because they are gained repeatedly in related strains?

## Hypothesis

Acquired resistance genes show more independent gain events per gene than non-resistance accessory genes of matched prevalence, so their stronger relatedness signal does not mean clonal inheritance.

## Why it matters

The higher relatedness signal for acquired than for intrinsic resistance genes was partly an effect of how the measure handles near-universal core genes, which barely vary between strains. A gain-event comparison between genes of similar prevalence would give a mechanism that this effect cannot.

## How to test it

For species that have within-species trees, reconstruct gains and losses of each resistance gene cluster and of non-resistance accessory clusters matched on prevalence. Compare the number of independent gains per gene. Repeat in species with the most genomes.

## What would support or refute it

Support: more independent gains per resistance gene than matched non-resistance genes. Refute: gain counts equal to or lower than matched genes, meaning clonal inheritance explains the pattern.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Trees exist for only some species in the catalog (343 listed), and ancestral reconstruction for every gene cluster has to be computed.

## Builds on

- Finding: [[findings/amr_strain_variation--e349ed14|Putatively acquired AMR genes show stronger phylogenetic signal than core genes]] (Candidate novel)
- Finding: [[findings/amr_strain_variation--6ebb7e8b|Over half of species show significant ANI–AMR phylogenetic signal]] (Insufficient literature evidence)
- Finding: [[findings/amr_strain_variation--065d36b5|Tightly co-occurring resistance islands are detected in over half of species]] (Insufficient literature evidence)

## Closest published work

- [PMID 30953542](https://pubmed.ncbi.nlm.nih.gov/30953542/) Culture-enriched human gut microbiomes reveal core and accessory resistance genes.
- [PMID 20805406](https://pubmed.ncbi.nlm.nih.gov/20805406/) Mobility of plasmids.
- [PMID 35801696](https://pubmed.ncbi.nlm.nih.gov/35801696/) Core genes can have higher recombination rates than accessory genes within global microbial populations.
- [PMID 39472795](https://pubmed.ncbi.nlm.nih.gov/39472795/) Large-scale genomic analysis of Elizabethkingia anophelis.

PMID 30953542 separates core and accessory resistance genes, and PMID 35801696 reports recombination rates in core versus accessory genes; neither counts independent gains of resistance genes.
