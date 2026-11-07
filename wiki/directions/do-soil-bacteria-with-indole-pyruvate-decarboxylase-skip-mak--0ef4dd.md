---
type: "Research direction"
description: "The link between tryptophan synthesis and the auxin gene ipdC reverses in soil and rhizosphere species, although a tyrosine control also predicts ipdC. Does soil life let ipdC carriers rely on plant-supplied tryptophan?"
hypothesis: "Among soil ipdC carriers, incomplete tryptophan synthesis is common. Those strains make auxin from supplied tryptophan and grow poorly without it, while non-soil carriers synthesise their own."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The genomic comparison uses existing data, but growth and auxin assays on soil isolates need new measurements. Only 214 of 11,272 species carry ipdC, which limits the genomic step."
collections: ["kbase-ke-pangenome"]
findings: ["pgp_pangenome_ecology--6ad3c804", "pgp_pangenome_ecology--ac2bd4ee"]
conflicts: []
papers: ["18757531", "25811953", "2034209"]
builds_on: ["findings/pgp_pangenome_ecology--6ad3c804", "findings/pgp_pangenome_ecology--ac2bd4ee"]
projects: ["pgp_pangenome_ecology"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do soil bacteria with indole-pyruvate decarboxylase skip making their own tryptophan?

The link between tryptophan synthesis and the auxin gene ipdC reverses in soil and rhizosphere species, although a tyrosine control also predicts ipdC. Does soil life let ipdC carriers rely on plant-supplied tryptophan?

## Hypothesis

Among soil ipdC carriers, incomplete tryptophan synthesis is common. Those strains make auxin from supplied tryptophan and grow poorly without it, while non-soil carriers synthesise their own.

## Why it matters

It would identify a nutritional dependency behind a plant-growth trait and guide inoculant choice by what the plant supplies.

## How to test it

In the Pangenome Collection, compare tryptophan pathway completeness in ipdC carriers from soil versus other habitats, controlling for overall pathway completeness and genome size, since the tyrosine control also predicted ipdC. Then grow selected incomplete and complete soil carriers in minimal medium with and without tryptophan, and measure growth and indole-3-acetic acid output.

## What would support or refute it

Support: soil carriers more often lack complete synthesis, and the incomplete ones need tryptophan for growth and auxin. Refute: the reversal vanishes once general completeness is controlled, or incomplete strains grow without tryptophan.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The genomic comparison uses existing data, but growth and auxin assays on soil isolates need new measurements. Only 214 of 11,272 species carry ipdC, which limits the genomic step.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/pgp_pangenome_ecology--6ad3c804|Tryptophan–ipdC association reverses in soil species]] (Candidate novel)
- Finding: [[findings/pgp_pangenome_ecology--ac2bd4ee|Negative-control pathway also predicts ipdC, undermining tryptophan specificity]] (Insufficient literature evidence)

## Closest published work

- [PMID 18757531](https://pubmed.ncbi.nlm.nih.gov/18757531/) Aromatic amino acid-dependent expression of indole-3-pyruvate decarboxylase is regulated by TyrR in Enterobacter cloacae UW5.
- [PMID 25811953](https://pubmed.ncbi.nlm.nih.gov/25811953/) The TyrR transcription factor regulates the divergent akr-ipdC operons of Enterobacter cloacae UW5.
- [PMID 2034209](https://pubmed.ncbi.nlm.nih.gov/2034209/) Molecular cloning of the gene for indolepyruvate decarboxylase from Enterobacter cloacae.

PMID 18757531 and PMID 25811953 show tryptophan-dependent regulation of ipdC in a single Enterobacter strain. Neither examines habitat or whether synthesis is lost.
