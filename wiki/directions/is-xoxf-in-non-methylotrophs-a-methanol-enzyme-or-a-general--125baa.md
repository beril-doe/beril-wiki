---
type: "Research direction"
description: "In xoxF-carrying genomes outside classic methylotroph families, is the enzyme part of a methanol-oxidation pathway or a broader alcohol and aldehyde oxidizer?"
hypothesis: "Outside known methylotroph families, most xoxF carriers lack the downstream genes for formaldehyde and formate oxidation, so xoxF abundance reflects general alcohol oxidation rather than methylotrophy."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Both annotation sources and taxonomy for the full genome collection are listed, and the pathway scoring must be built from them."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.gene_genecluster_junction", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["lanthanide_methylotrophy_atlas--6465f1d3", "lanthanide_methylotrophy_atlas--4129a02d"]
conflicts: []
papers: ["41636527", "42678158", "41023737", "29997591"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--6465f1d3", "findings/lanthanide_methylotrophy_atlas--4129a02d"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Is xoxF in non-methylotrophs a methanol enzyme or a general alcohol oxidizer?

In xoxF-carrying genomes outside classic methylotroph families, is the enzyme part of a methanol-oxidation pathway or a broader alcohol and aldehyde oxidizer?

## Hypothesis

Outside known methylotroph families, most xoxF carriers lack the downstream genes for formaldehyde and formate oxidation, so xoxF abundance reflects general alcohol oxidation rather than methylotrophy.

## Why it matters

The large lead of xoxF over the calcium-dependent enzyme is usually read as lanthanide-based methylotrophy dominating. If most carriers are not methylotrophs, that reading and the estimate of how common lanthanide-dependent methanol oxidation is would both change.

## How to test it

For every xoxF carrier in the 293,059-genome collection, score methylotrophy support: partner periplasmic genes, formaldehyde and formate oxidation, and C1 assimilation. Summarize by family and compare known methylotroph families with the rest, reporting each annotation source separately because they disagree for some markers. Then test growth on methanol and on other alcohols with and without lanthanum for a few non-methylotroph carriers, for example in Acidobacteriota.

## What would support or refute it

Support: most carriers outside methylotroph families lack downstream genes, and isolates oxidize other alcohols lanthanide-dependently but not methanol. Refute: downstream pathway genes are present in most carriers, and isolates grow on methanol with lanthanum.

## Data

Approach: analysis then experiment. Readiness: needs compute. Both annotation sources and taxonomy for the full genome collection are listed, and the pathway scoring must be built from them.

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--6465f1d3|Lanthanide-dependent xoxF vastly outnumbers calcium-dependent mxaF across a large genome collection]] (Extends retrieved work)
- Finding: [[findings/lanthanide_methylotrophy_atlas--4129a02d|xoxF dominance holds under several phylogeny-aware corrections, strongest in the mixed model]] (Insufficient literature evidence)

## Closest published work

- [PMID 41636527](https://pubmed.ncbi.nlm.nih.gov/41636527/) Beneath the surface: expanding the known repertoire of methylotrophic metabolism.
- [PMID 42678158](https://pubmed.ncbi.nlm.nih.gov/42678158/) xoxF-linked methanol oxidation signals recur across wetland metagenomes.
- [PMID 41023737](https://pubmed.ncbi.nlm.nih.gov/41023737/) Diversity and distribution of the lanthanome in aerobic methane-oxidising bacteria.
- [PMID 29997591](https://pubmed.ncbi.nlm.nih.gov/29997591/) Lanthanide-Dependent Methanol Dehydrogenases of XoxF4 and XoxF5 Clades Are Differentially Distributed Among Methylotrophic Bacteria and They Reveal Different Biochemical Properties.

PMID 41636527 and PMID 42678158 explore wider methylotrophic metabolism and xoxF signals in wetlands, and PMID 41023737 covers methane oxidizers. None tests whether xoxF carriers across a large genome set carry full methylotrophy pathways.
