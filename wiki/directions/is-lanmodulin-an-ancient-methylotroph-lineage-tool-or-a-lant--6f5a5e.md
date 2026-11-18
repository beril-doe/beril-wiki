---
type: "Research direction"
description: "Why is lanmodulin confined to three alpha-Proteobacterial methylotroph families, and what does it do in the genomes that carry it without the lanthanide-dependent methanol enzyme?"
hypothesis: "Lanmodulin was gained in a few ancestral lineages and then lost repeatedly. Carriers without xoxF keep it for lanthanide buffering or storage, so its presence is not tied to the dehydrogenase."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Annotation, gene-to-cluster and taxonomy tables are in the catalog, but a gene tree and neighbourhood analysis must be built, and gene position columns were not shown by the catalog."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.gene_genecluster_junction", "kbase.ke_pangenome.gene", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["lanthanide_methylotrophy_atlas--d54adcf1", "lanthanide_methylotrophy_atlas--6543a6a6"]
conflicts: []
papers: ["30351021", "35814700", "37259003", "34737731"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--d54adcf1", "findings/lanthanide_methylotrophy_atlas--6543a6a6"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Is lanmodulin an ancient methylotroph-lineage tool or a lanthanide store used without xoxF?

Why is lanmodulin confined to three alpha-Proteobacterial methylotroph families, and what does it do in the genomes that carry it without the lanthanide-dependent methanol enzyme?

## Hypothesis

Lanmodulin was gained in a few ancestral lineages and then lost repeatedly. Carriers without xoxF keep it for lanthanide buffering or storage, so its presence is not tied to the dehydrogenase.

## Why it matters

It would separate a lanthanide-handling protein from the enzyme it was assumed to serve. Lanmodulin presence could then not be used to predict lanthanide-dependent metabolism, and engineered lanmodulin variants would not mimic a natural role.

## How to test it

Build a gene tree of lanmodulin across the genomes that carry a validated copy (62 genomes from 10 species, all within Beijerinckiaceae, Acetobacteraceae or Hyphomicrobiaceae) and compare it with the species tree to count gains and losses. Compare the genes next to lanmodulin in genomes with and without xoxF (xoxF co-occurred in 49 of the 62). Then grow a lanmodulin-carrying strain that lacks xoxF in metal-limited medium with and without lanthanum, comparing wild type with a lanmodulin deletion for lanthanide uptake and survival.

## What would support or refute it

Support: few gains followed by repeated losses, neighbouring genes unrelated to methanol oxidation in carriers lacking xoxF, and a deletion effect on lanthanide handling. Refute: lanmodulin always sits beside xoxF-linked genes, or its deletion has no effect without xoxF.

## Data

Approach: analysis then experiment. Readiness: needs compute. Annotation, gene-to-cluster and taxonomy tables are in the catalog, but a gene tree and neighbourhood analysis must be built, and gene position columns were not shown by the catalog.

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--d54adcf1|Bakta-validated lanmodulin is confined to alpha-Proteobacterial methylotroph families]] (Insufficient literature evidence)
- Finding: [[findings/lanthanide_methylotrophy_atlas--6543a6a6|Lanmodulin–xoxF co-occurrence falls just short of preregistered threshold]] (Insufficient literature evidence)

## Closest published work

- [PMID 30351021](https://pubmed.ncbi.nlm.nih.gov/30351021/) Lanmodulin: A Highly Selective Lanthanide-Binding Protein from a Lanthanide-Utilizing Bacterium.
- [PMID 35814700](https://pubmed.ncbi.nlm.nih.gov/35814700/) A Periplasmic Lanthanide Mediator, Lanmodulin, in Methylobacterium aquaticum Strain 22A.
- [PMID 37259003](https://pubmed.ncbi.nlm.nih.gov/37259003/) Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer.
- [PMID 34737731](https://pubmed.ncbi.nlm.nih.gov/34737731/) Comprehensive Comparative Genomics and Phenotyping of Methylobacterium Species.

PMIDs 30351021 and 35814700 characterize lanmodulin in Methylobacterium and PMID 34737731 compares Methylobacterium genomes. None traces gain and loss of lanmodulin or tests its role where xoxF is absent.
