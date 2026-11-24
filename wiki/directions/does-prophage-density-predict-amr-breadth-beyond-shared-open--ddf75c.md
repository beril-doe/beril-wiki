---
type: "Research direction"
description: "Species with denser prophages carry broader AMR repertoires, yet the association reverses at very close range. Does prophage density add information beyond pangenome openness and environment?"
hypothesis: "Prophage density predicts AMR breadth less within genera than across species. Once openness and environmental diversity are controlled, the association shrinks sharply, which would favor shared open-pangenome effects over phage-driven transfer."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "AMR, annotation, pangenome and environment tables are listed, but the species-level aggregation and gene-neighborhood analysis need new computation."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.bakta_amr", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.pangenome", "kbase.ke_pangenome.alphaearth_embeddings_all_years"]
findings: ["prophage_amr_comobilization--78c6cbde", "prophage_amr_comobilization--6abb4f27", "amr_pangenome_atlas--ccd6e57f", "cog_analysis--e7589648"]
conflicts: ["conflict--core-versus-accessory-partitioning-of-gene-functions-and-trait-genes--5cc5b57d"]
papers: ["30576310", "30453138", "26078016", "33980677", "34135355"]
builds_on: ["findings/prophage_amr_comobilization--78c6cbde", "findings/prophage_amr_comobilization--6abb4f27", "findings/amr_pangenome_atlas--ccd6e57f", "findings/cog_analysis--e7589648", "conflicts/conflict--core-versus-accessory-partitioning-of-gene-functions-and-trait-genes--5cc5b57d"]
projects: ["amr_pangenome_atlas", "cog_analysis", "pgp_pangenome_ecology", "plant_microbiome_ecotypes", "prophage_amr_comobilization"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Does prophage density predict AMR breadth beyond shared open-pangenome effects?

Species with denser prophages carry broader AMR repertoires, yet the association reverses at very close range. Does prophage density add information beyond pangenome openness and environment?

## Hypothesis

Prophage density predicts AMR breadth less within genera than across species. Once openness and environmental diversity are controlled, the association shrinks sharply, which would favor shared open-pangenome effects over phage-driven transfer.

## Why it matters

It would show whether prophages are a general route for resistance spread or both traits just accumulate in open, ecologically diverse species. That affects how surveillance uses prophage content.

## How to test it

Per species, compute prophage-like gene density from Bakta annotation keywords (the catalog did not show dedicated prophage calls), AMR breadth from the Bakta AMR table, openness from cluster counts and environmental diversity from AlphaEarth embeddings. Fit nested models with genus as a grouping term and compare the prophage term. Also repeat the gene-distance analysis separately for core and accessory AMR clusters.

## What would support or refute it

Support: the prophage term stays large within genera after controls. Refute: it drops near zero once openness and environment enter.

## Data

Approach: lakehouse analysis. Readiness: needs compute. AMR, annotation, pangenome and environment tables are listed, but the species-level aggregation and gene-neighborhood analysis need new computation.

## Builds on

- Finding: [[findings/prophage_amr_comobilization--78c6cbde|Tenfold higher prophage density predicts much broader AMR repertoires]] (Candidate novel)
- Finding: [[findings/prophage_amr_comobilization--6abb4f27|Prophage proximity and accessory AMR status reverse at very close range]] (Candidate novel)
- Finding: [[findings/amr_pangenome_atlas--ccd6e57f|Environmental diversity strongly predicts AMR count per species]] (Candidate novel)
- Finding: [[findings/cog_analysis--e7589648|Mobile elements dominate novel genes across all species]] (Candidate novel)
- Conflict: [[conflicts/conflict--core-versus-accessory-partitioning-of-gene-functions-and-trait-genes--5cc5b57d|Horizontal Gene Transfer versus Vertical Core Inheritance: A Tension in Reading Core/Accessory Status of Trait Genes]]

## Closest published work

- [PMID 30576310](https://pubmed.ncbi.nlm.nih.gov/30576310/) Genetic exchanges are more frequent in bacteria encoding capsules.
- [PMID 30453138](https://pubmed.ncbi.nlm.nih.gov/30453138/) A metagenomic analysis framework for characterization of antibiotic resistomes in river environment: Application to an urban river in Beijing.
- [PMID 26078016](https://pubmed.ncbi.nlm.nih.gov/26078016/) Fluoroquinolone induction of phage-mediated gene transfer in multidrug-resistant Salmonella.
- [PMID 33980677](https://pubmed.ncbi.nlm.nih.gov/33980677/) Staphylococcus epidermidis Phages Transduce Antimicrobial Resistance Plasmids and Mobilize Chromosomal Islands.
- [PMID 34135355](https://pubmed.ncbi.nlm.nih.gov/34135355/) AMRFinderPlus and the Reference Gene Catalog facilitate examination of the genomic links among antimicrobial resistance, stress response, and virulence.

30576310 links prophages and resistance to capsules and larger pangenomes. 30453138, 26078016 and 33980677 show phage-associated transfer. None separates prophage density from openness and environment.
