---
type: "Research direction"
description: "Why does tryptophan pathway completeness predict carrying the auxin-synthesis gene ipdC in non-soil species but the reverse in soil and rhizosphere species?"
hypothesis: "In soil, ipdC carriers are often tryptophan auxotrophs that obtain tryptophan from plant exudates and use ipdC to make auxin from it, while carriers elsewhere make their own tryptophan. The reversal should persist when compared with genome-wide metabolic completeness, which the tyrosine control did not do."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Pathway predictions, annotations and isolation sources are in the catalog; genus-matched comparisons need computing, and the growth test needs new measurements. Only a small share of species carry ipdC."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.ncbi_env"]
findings: ["pgp_pangenome_ecology--6ad3c804", "pgp_pangenome_ecology--ac2bd4ee"]
conflicts: []
papers: ["18757531", "2034209", "25811953", "24905353"]
builds_on: ["findings/pgp_pangenome_ecology--6ad3c804", "findings/pgp_pangenome_ecology--ac2bd4ee"]
projects: ["pgp_pangenome_ecology"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Do soil bacteria with the auxin gene ipdC give up tryptophan synthesis?

Why does tryptophan pathway completeness predict carrying the auxin-synthesis gene ipdC in non-soil species but the reverse in soil and rhizosphere species?

## Hypothesis

In soil, ipdC carriers are often tryptophan auxotrophs that obtain tryptophan from plant exudates and use ipdC to make auxin from it, while carriers elsewhere make their own tryptophan. The reversal should persist when compared with genome-wide metabolic completeness, which the tyrosine control did not do.

## Why it matters

It would reveal a gene-loss route to dependence on plants in rhizosphere bacteria, and would guide the choice of inoculants that depend on plant-derived tryptophan.

## How to test it

Within genera containing both ipdC carriers and non-carriers, compare tryptophan pathway completeness against that of amino-acid pathways in general, separately for soil-sourced and other genomes. Check whether carriers lacking tryptophan synthesis also carry tryptophan uptake transporters. Then grow auxotrophic and prototrophic ipdC carriers on defined medium with and without tryptophan and measure auxin output.

## What would support or refute it

Support: soil carriers specifically lack tryptophan synthesis beyond their general pathway loss, retain uptake, and make auxin only when given tryptophan. Refutation: the reversal disappears once general pathway completeness is accounted for, as the tyrosine control suggests, or auxotrophic carriers produce no auxin.

## Data

Approach: analysis then experiment. Readiness: needs compute. Pathway predictions, annotations and isolation sources are in the catalog; genus-matched comparisons need computing, and the growth test needs new measurements. Only a small share of species carry ipdC.

## Builds on

- Finding: [[findings/pgp_pangenome_ecology--6ad3c804|Tryptophan–ipdC association reverses in soil species]] (Candidate novel)
- Finding: [[findings/pgp_pangenome_ecology--ac2bd4ee|Negative-control pathway also predicts ipdC, undermining tryptophan specificity]] (Insufficient literature evidence)

## Closest published work

- [PMID 18757531](https://pubmed.ncbi.nlm.nih.gov/18757531/) Aromatic amino acid-dependent expression of indole-3-pyruvate decarboxylase is regulated by TyrR in Enterobacter cloacae UW5.
- [PMID 2034209](https://pubmed.ncbi.nlm.nih.gov/2034209/) Molecular cloning of the gene for indolepyruvate decarboxylase from Enterobacter cloacae.
- [PMID 25811953](https://pubmed.ncbi.nlm.nih.gov/25811953/) The TyrR transcription factor regulates the divergent akr-ipdC operons of Enterobacter cloacae UW5.
- [PMID 24905353](https://pubmed.ncbi.nlm.nih.gov/24905353/) New insights into 1-aminocyclopropane-1-carboxylate (ACC) deaminase phylogeny, evolution and ecological significance.

PMID 18757531 and PMID 25811953 show tryptophan regulates ipdC expression in Enterobacter cloacae and PMID 2034209 cloned the gene, but none asks whether soil carriers have lost their own tryptophan synthesis.
