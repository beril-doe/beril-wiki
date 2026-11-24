---
type: "Research direction"
description: "Is the scaling of AMR breadth with prophage density caused by phage-linked transfer, or by a shared tendency of some species to take up foreign DNA?"
hypothesis: "Prophage density predicts AMR breadth through a shared taxon-level propensity for gene uptake, not phage-mediated transfer, so AMR genes are no more often next to complete prophages than matched non-AMR accessory genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "AMR, cluster and annotation tables are in the catalog; the matched-control distance analysis is not yet run."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.bakta_amr", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.pangenome", "kbase.ke_pangenome.bakta_annotations"]
findings: ["prophage_amr_comobilization--78c6cbde", "prophage_amr_comobilization--6abb4f27", "amr_pangenome_atlas--012985a7"]
conflicts: []
papers: ["30576310", "26078016", "30453138", "33980677", "30068738"]
builds_on: ["findings/prophage_amr_comobilization--78c6cbde", "findings/prophage_amr_comobilization--6abb4f27", "findings/amr_pangenome_atlas--012985a7"]
projects: ["amr_pangenome_atlas", "prophage_amr_comobilization"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Does prophage load drive AMR breadth, or do open pangenomes accumulate both independently?

Is the scaling of AMR breadth with prophage density caused by phage-linked transfer, or by a shared tendency of some species to take up foreign DNA?

## Hypothesis

Prophage density predicts AMR breadth through a shared taxon-level propensity for gene uptake, not phage-mediated transfer, so AMR genes are no more often next to complete prophages than matched non-AMR accessory genes.

## Why it matters

It would separate phage-borne spread of resistance from a general permissiveness to foreign DNA, which implies different interventions.

## How to test it

Per species, use AMR gene calls and prophage annotations from the pangenome. Compare AMR-to-prophage distance with distance for accessory genes matched on cluster frequency, at several distance cut-offs including very close range. Add pangenome openness, which had near zero overall correlation with AMR count, as a covariate. Fit within-phylum models.

## What would support or refute it

Support: after matching, AMR genes are not closer to prophages and the scaling falls once uptake propensity is included. Refute: AMR genes are closer to complete prophages than matched accessory genes in many species, including at close range.

## Data

Approach: lakehouse analysis. Readiness: needs compute. AMR, cluster and annotation tables are in the catalog; the matched-control distance analysis is not yet run.

## Builds on

- Finding: [[findings/prophage_amr_comobilization--78c6cbde|Tenfold higher prophage density predicts much broader AMR repertoires]] (Candidate novel)
- Finding: [[findings/prophage_amr_comobilization--6abb4f27|Prophage proximity and accessory AMR status reverse at very close range]] (Candidate novel)
- Finding: [[findings/amr_pangenome_atlas--012985a7|Pangenome openness does not correlate with AMR count overall]] (Candidate novel)

## Closest published work

- [PMID 30576310](https://pubmed.ncbi.nlm.nih.gov/30576310/) Genetic exchanges are more frequent in bacteria encoding capsules.
- [PMID 26078016](https://pubmed.ncbi.nlm.nih.gov/26078016/) Fluoroquinolone induction of phage-mediated gene transfer in multidrug-resistant Salmonella.
- [PMID 30453138](https://pubmed.ncbi.nlm.nih.gov/30453138/) A metagenomic analysis framework for characterization of antibiotic resistomes in river environment: Application to an urban river in Beijing.
- [PMID 33980677](https://pubmed.ncbi.nlm.nih.gov/33980677/) Staphylococcus epidermidis Phages Transduce Antimicrobial Resistance Plasmids and Mobilize Chromosomal Islands.
- [PMID 30068738](https://pubmed.ncbi.nlm.nih.gov/30068738/) Mobile Genetic Elements Associated with Antimicrobial Resistance.

30576310 and 30453138 link resistance genes to prophages and capsules; this adds matched accessory controls and the close-range reversal.
