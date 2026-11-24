---
type: "Research direction"
description: "Why are tryptophan-complete soil species less likely to carry ipdC, and does exudate-supplied tryptophan explain it?"
hypothesis: "Soil species that lack tryptophan synthesis but carry ipdC also carry tryptophan uptake genes or TyrR, so ipdC use depends on scavenged tryptophan."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The catalog shows the pangenome pathway, annotation and environment tables, and the covariate model still has to be run."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["pgp_pangenome_ecology--e6a258a2", "pgp_pangenome_ecology--7e9e60f9"]
conflicts: []
papers: ["18757531", "40130845", "38743630"]
builds_on: ["findings/pgp_pangenome_ecology--e6a258a2", "findings/pgp_pangenome_ecology--7e9e60f9"]
projects: ["pgp_pangenome_ecology"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Does tryptophan completeness predict ipdC carriage in soil species through root-exudate tryptophan supply?

Why are tryptophan-complete soil species less likely to carry ipdC, and does exudate-supplied tryptophan explain it?

## Hypothesis

Soil species that lack tryptophan synthesis but carry ipdC also carry tryptophan uptake genes or TyrR, so ipdC use depends on scavenged tryptophan.

## Why it matters

It would link auxotrophy to plant-growth-promoting traits. Dependence on host-supplied amino acids would then help explain which soil bacteria make auxin.

## How to test it

In the pangenome, split species by tryptophan completeness and environment. Test ipdC carriage against tryptophan transporter genes and TyrR, adding genome size and total complete pathways as covariates. Repeat within genera to control for lineage.

## What would support or refute it

Support: trp-incomplete ipdC carriers are enriched for uptake genes or TyrR beyond what genome size predicts. Refute: no enrichment, or a reversal that disappears when genome size or lineage is controlled. The soil reversal is hypothesis-generating, and ipdC is carried by few species.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The catalog shows the pangenome pathway, annotation and environment tables, and the covariate model still has to be run.

## Builds on

- Finding: [[findings/pgp_pangenome_ecology--e6a258a2|Tryptophan-ipdC association reverses within soil species]] (Candidate novel)
- Finding: [[findings/pgp_pangenome_ecology--7e9e60f9|nifH shows no association with ipdC]] (Candidate novel)

## Closest published work

- [PMID 18757531](https://pubmed.ncbi.nlm.nih.gov/18757531/) Aromatic amino acid-dependent expression of indole-3-pyruvate decarboxylase is regulated by TyrR in Enterobacter cloacae UW5.
- [PMID 40130845](https://pubmed.ncbi.nlm.nih.gov/40130845/) Indole-3-acetic acid (IAA) protects Azospirillum brasilense from indole-induced stress.
- [PMID 38743630](https://pubmed.ncbi.nlm.nih.gov/38743630/) Bacterial lifestyle shapes pangenomes.

18757531 shows tryptophan induces ipdC through TyrR in one strain, and 40130845 covers ipdC physiology. Neither tests species-level links between tryptophan supply and ipdC.
