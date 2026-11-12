---
type: "Research direction"
description: "Plant-growth genes are mostly core (29.7% accessory versus 53.2% genome-wide) and acdS is strongly enriched in soil species even with phylum controls. Yet they co-occur with transposases. Were they gained long ago and are now inherited vertically, so that mobility is old rather than ongoing?"
hypothesis: "Gains of acdS, pqqC and hcnC cluster at deep taxonomic depths (phylum or above), unlike recent-skewed classes such as CRISPR-Cas, and recent genus-level gains are rare and confined to the accessory minority."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The depth method exists for the atlas, but it has not been applied to these gene families and must be run."
collections: ["kbase-ke-pangenome", "kbase-uniref"]
findings: ["pgp_pangenome_ecology--45e0cc45", "pgp_pangenome_ecology--6ef7f988", "gene_function_ecological_agora--c0bd8a1a"]
conflicts: ["conflict--horizontal-gene-transfer-driven-innovation--9137941d"]
papers: ["24905353", "41724873", "34946069", "29925415"]
builds_on: ["findings/pgp_pangenome_ecology--45e0cc45", "findings/pgp_pangenome_ecology--6ef7f988", "findings/gene_function_ecological_agora--c0bd8a1a", "conflicts/conflict--horizontal-gene-transfer-driven-innovation--9137941d"]
projects: ["gene_function_ecological_agora", "pgp_pangenome_ecology", "plant_microbiome_ecotypes"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Were plant-growth genes acquired anciently and since inherited vertically, unlike recent mobile gains?

Plant-growth genes are mostly core (29.7% accessory versus 53.2% genome-wide) and acdS is strongly enriched in soil species even with phylum controls. Yet they co-occur with transposases. Were they gained long ago and are now inherited vertically, so that mobility is old rather than ongoing?

## Hypothesis

Gains of acdS, pqqC and hcnC cluster at deep taxonomic depths (phylum or above), unlike recent-skewed classes such as CRISPR-Cas, and recent genus-level gains are rare and confined to the accessory minority.

## Why it matters

It would separate when plant-growth traits were acquired from whether they move now, and so whether inoculant traits can be predicted from taxonomy or must be screened strain by strain.

## How to test it

Apply the gene-gain depth estimation used for the gene-function atlas to the plant-growth gene families in the Pangenome Collection and UniRef Clusters. Compare the share of genus-level (recent) and phylum-or-above (ancient) gains with the atlas classes at the two extremes: CRISPR-Cas (58.7% recent, 2.4% ancient) and strict tRNA synthetases (24.7% recent, 10.7% ancient). Split by soil/rhizosphere versus other lineages, using pqqD (27.5% singletons) as an outlier reference.

## What would support or refute it

Support: ancient gains outweigh recent gains for the core copies, and recent gains appear only among accessory copies. Refutation: plant-growth genes show recent-skewed gain profiles like CRISPR-Cas, so their core status reflects recent spread or sampling rather than ancient acquisition. The atlas estimates gain location and depth, not donor-recipient flow, and results are limited accordingly.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The depth method exists for the atlas, but it has not been applied to these gene families and must be run.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/pgp_pangenome_ecology--45e0cc45|Plant-growth genes are mostly core, rejecting the accessory/HGT hypothesis]] (Extends retrieved work)
- Finding: [[findings/pgp_pangenome_ecology--6ef7f988|ACC deaminase gene strongly enriched in soil species, surviving phylum controls]] (Extends retrieved work)
- Finding: [[findings/gene_function_ecological_agora--c0bd8a1a|Function classes have distinct gene-acquisition depth profiles, CRISPR-Cas most recent-skewed]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--horizontal-gene-transfer-driven-innovation--9137941d|Plant-Growth-Promoting Traits: Vertically Inherited Core Genes or Transposase-Linked Mobile Cargo?]]

## Closest published work

- [PMID 24905353](https://pubmed.ncbi.nlm.nih.gov/24905353/) New insights into 1-aminocyclopropane-1-carboxylate (ACC) deaminase phylogeny, evolution and ecological significance.
- [PMID 41724873](https://pubmed.ncbi.nlm.nih.gov/41724873/) Comparative genomic analyses reveal key traits for biocontrol and the promotion of plant growth in Paenibacillus strains.
- [PMID 34946069](https://pubmed.ncbi.nlm.nih.gov/34946069/) Pseudomonas 1-Aminocyclopropane-1-carboxylate (ACC) Deaminase and Its Role in Beneficial Plant-Microbe Interactions.
- [PMID 29925415](https://pubmed.ncbi.nlm.nih.gov/29925415/) 1-Aminocyclopropane-1-carboxylate deaminase producers associated to maize and other Poaceae species.

PMID 24905353 concludes ACC deaminase genes are mostly vertically inherited with some transfer, and PMID 41724873 suggests transfer in mobile regions for some plant-growth genes. Neither dates acquisitions or compares gain depth across several plant-growth genes.
