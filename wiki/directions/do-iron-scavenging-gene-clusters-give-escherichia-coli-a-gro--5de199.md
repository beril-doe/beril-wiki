---
type: "Research direction"
description: "Do Escherichia coli strains carrying iron-siderophore and genotoxin gene clusters out-compete otherwise similar strains without them when iron is restricted, as in inflamed gut, and does that edge vanish when iron is supplied?"
hypothesis: "Strains with siderophore clusters such as yersiniabactin or enterobactin gain a growth advantage over matched non-carrying strains in iron-restricted gut-like medium, and the advantage disappears with added iron. Cluster carriage predicts this better than an adherent-invasive label does."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Genome scoring can run on lakehouse genomes, but the competition assays need new wet-lab work; the existing enrichment is against the full gene-cluster catalog and is inflated by background rarity."
collections: ["kbase-genomes", "kbase-ke-pangenome"]
findings: ["ibd_phage_targeting--446eca8c", "ibd_phage_targeting--6d9fa20c"]
conflicts: []
papers: ["35359974", "28130329", "41606218"]
builds_on: ["findings/ibd_phage_targeting--446eca8c", "findings/ibd_phage_targeting--6d9fa20c"]
projects: ["ibd_phage_targeting"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Do iron-scavenging gene clusters give Escherichia coli a growth edge when iron is scarce?

Do Escherichia coli strains carrying iron-siderophore and genotoxin gene clusters out-compete otherwise similar strains without them when iron is restricted, as in inflamed gut, and does that edge vanish when iron is supplied?

## Hypothesis

Strains with siderophore clusters such as yersiniabactin or enterobactin gain a growth advantage over matched non-carrying strains in iron-restricted gut-like medium, and the advantage disappears with added iron. Cluster carriage predicts this better than an adherent-invasive label does.

## Why it matters

Only 8 of 23 Crohn's patients in the UC Davis cohort carried detectable E. coli, so adherent-invasive E. coli may not describe most patients. The iron and genotoxin clusters were strongly enriched among the core gene clusters, but against the full catalog rather than a matched set. A direct growth test would show whether these clusters confer a real ecological advantage, which bears on which strains phage or iron-directed therapy should target.

## How to test it

From E. coli genomes in KBase Genomes and the Pangenome Collection, score each genome for iron-siderophore and genotoxin cluster carriage and for adherent-invasive markers. Select pairs that differ in one class but not the other. Run pairwise anaerobic competition assays in gut-like medium across an iron series, including an iron-chelated condition, and count each strain by barcode or marker PCR.

## What would support or refute it

Support: cluster carriers win in iron-restricted medium, the advantage shrinks or disappears with added iron, and it holds regardless of the adherent-invasive label. Refutation: competition outcome tracks the adherent-invasive label or neither trait, or iron level makes no difference.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Genome scoring can run on lakehouse genomes, but the competition assays need new wet-lab work; the existing enrichment is against the full gene-cluster catalog and is inflated by background rarity.

- Collection: [[data/kbase-genomes|KBase Genomes]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/ibd_phage_targeting--446eca8c|Tier-A core gene clusters are enriched for iron-siderophore and genotoxin themes]] (Insufficient literature evidence)
- Finding: [[findings/ibd_phage_targeting--6d9fa20c|E. coli is rarer in this Crohn's cohort than AIEC literature implies]] (Extends retrieved work)

## Closest published work

- [PMID 35359974](https://pubmed.ncbi.nlm.nih.gov/35359974/) Prevalence, Abundance, and Virulence of Adherent-Invasive Escherichia coli in Ulcerative Colitis, Colorectal Cancer, and Coeliac Disease.
- [PMID 28130329](https://pubmed.ncbi.nlm.nih.gov/28130329/) Bacteriophages Targeting Adherent Invasive Escherichia coli Strains as a Promising New Treatment for Crohn's Disease.
- [PMID 41606218](https://pubmed.ncbi.nlm.nih.gov/41606218/) From niche to niche: investigating microbial communities and their specialised metabolite gene clusters in human microbiomes.

PMID 35359974 measures how common adherent-invasive E. coli is and PMID 28130329 targets it with phage; neither asks whether siderophore and genotoxin cluster carriage gives a competitive edge under varying iron.
