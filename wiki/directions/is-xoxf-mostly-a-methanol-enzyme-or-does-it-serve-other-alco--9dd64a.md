---
type: "Research direction"
description: "If xoxF outnumbers mxaF so strongly, do most carriers actually run a full methanol-to-formaldehyde-to-energy route, or does xoxF mainly act on other alcohols or aldehydes in bacteria that are not methylotrophs?"
hypothesis: "A large share of xoxF carriers across phyla lack the downstream one-carbon pathways needed to use methanol, so the xoxF-over-mxaF excess reflects broad alcohol oxidation, not methylotrophy."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The genome classification can be done on lakehouse data, but substrate preference requires enzyme assays."
collections: ["kbase-ke-pangenome", "kbase-uniprot"]
findings: ["lanthanide_methylotrophy_atlas--6465f1d3", "lanthanide_methylotrophy_atlas--4129a02d"]
conflicts: []
papers: ["29997591", "41636527", "29404411", "26858104"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--6465f1d3", "findings/lanthanide_methylotrophy_atlas--4129a02d"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Is xoxF mostly a methanol enzyme, or does it serve other alcohols in non-methylotrophs?

If xoxF outnumbers mxaF so strongly, do most carriers actually run a full methanol-to-formaldehyde-to-energy route, or does xoxF mainly act on other alcohols or aldehydes in bacteria that are not methylotrophs?

## Hypothesis

A large share of xoxF carriers across phyla lack the downstream one-carbon pathways needed to use methanol, so the xoxF-over-mxaF excess reflects broad alcohol oxidation, not methylotrophy.

## Why it matters

It would redefine the xoxF count as a measure of lanthanide-dependent alcohol chemistry, and change how xoxF abundance in soils and wetlands is read as methanol cycling.

## How to test it

In the Pangenome Collection, classify xoxF-carrying genomes by presence of formaldehyde-oxidation and one-carbon assimilation genes, per phylum and with both annotation sources combined. Then, for non-methylotroph carriers in soil lineages such as Acidobacteriota, measure enzyme activity of purified XoxF against methanol, ethanol and other alcohols with and without lanthanides.

## What would support or refute it

Support: many carriers lack the downstream route and the enzyme prefers longer alcohols. Refutation: nearly all carriers have a complete one-carbon route and the enzyme is most active on methanol.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The genome classification can be done on lakehouse data, but substrate preference requires enzyme assays.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--6465f1d3|Lanthanide-dependent xoxF vastly outnumbers calcium-dependent mxaF across a large genome collection]] (Extends retrieved work)
- Finding: [[findings/lanthanide_methylotrophy_atlas--4129a02d|xoxF dominance holds under several phylogeny-aware corrections, strongest in the mixed model]] (Insufficient literature evidence)

## Closest published work

- [PMID 29997591](https://pubmed.ncbi.nlm.nih.gov/29997591/) Lanthanide-Dependent Methanol Dehydrogenases of XoxF4 and XoxF5 Clades Are Differentially Distributed Among Methylotrophic Bacteria and They Reveal Different Biochemical Properties.
- [PMID 41636527](https://pubmed.ncbi.nlm.nih.gov/41636527/) Beneath the surface: expanding the known repertoire of methylotrophic metabolism.
- [PMID 29404411](https://pubmed.ncbi.nlm.nih.gov/29404411/) Lanthanide-Dependent Regulation of Methylotrophy in Methylobacteriumaquaticum Strain 22A.
- [PMID 26858104](https://pubmed.ncbi.nlm.nih.gov/26858104/) XoxF Acts as the Predominant Methanol Dehydrogenase in the Type I Methanotroph Methylomicrobium buryatense.

PMID 29404411 and 26858104 show xoxF as the main methanol dehydrogenase in particular methylotrophs and PMID 41636527 reviews wider methylotrophic metabolism; this tests whether the genome-wide excess is methanol-related at all.
