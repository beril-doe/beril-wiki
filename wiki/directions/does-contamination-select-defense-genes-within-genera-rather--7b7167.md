---
type: "Research direction"
description: "At the contaminated Oak Ridge site, is the defense signal carried by shifts within genera, which genus-level summaries would miss?"
hypothesis: "Within a genus, populations from more contaminated wells carry more defense-gene content than populations from cleaner wells. Pooling by genus hides this, which would explain the absent association in the preplanned genus-level test."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Community data in the lakehouse stop at genus level with no strain labels, so within-genus comparison needs new metagenomes; the pangenome step is only a pilot."
collections: ["enigma-coral", "kbase-ke-pangenome"]
findings: ["enigma_contamination_functional_potential--a97faeef", "enigma_contamination_functional_potential--606b2ef6", "enigma_contamination_functional_potential--f4cd1747"]
conflicts: []
papers: ["35107332", "26583008", "30523276"]
builds_on: ["findings/enigma_contamination_functional_potential--a97faeef", "findings/enigma_contamination_functional_potential--606b2ef6", "findings/enigma_contamination_functional_potential--f4cd1747"]
projects: ["enigma_contamination_functional_potential"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does contamination select defense genes within genera rather than between genera?

At the contaminated Oak Ridge site, is the defense signal carried by shifts within genera, which genus-level summaries would miss?

## Hypothesis

Within a genus, populations from more contaminated wells carry more defense-gene content than populations from cleaner wells. Pooling by genus hides this, which would explain the absent association in the preplanned genus-level test.

## Why it matters

It would show whether pollutant stress favors phage and mobile-element defense, and whether genus-level community functional proxies are the wrong scale for such questions.

## How to test it

Step 1, lakehouse: in the Pangenome Collection, compare defense-category gene content of Rhodanobacter genomes from contaminated aquifers with other genomes of the genus, using any isolation-source labels available. The earlier work reported expanded defense gene sets in contaminated-site Rhodanobacter. Step 2, experiment: ENIGMA CORAL names taxa only to genus, so collect shotgun metagenomes from wells spanning the contamination gradient, assemble and bin them, and compare defense genes within the same genus across wells. Include genera the current bridge did not map to the pangenome.

## What would support or refute it

Supported if defense content within the same genus rises with local contamination across several genera. Refuted if within-genus populations show no trend, leaving only the covariate-adjusted relaxed-mapping result, which depended on coverage and covariate choice.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Community data in the lakehouse stop at genus level with no strain labels, so within-genus comparison needs new metagenomes; the pangenome step is only a pilot.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/enigma_contamination_functional_potential--a97faeef|Covariate-adjusted models give a positive defense-contamination signal in relaxed mapping]] (Candidate novel)
- Finding: [[findings/enigma_contamination_functional_potential--606b2ef6|Confirmatory defense null holds across alternative contamination index definitions]] (In tension with retrieved work)
- Finding: [[findings/enigma_contamination_functional_potential--f4cd1747|No significant defense–contamination association in relaxed mapping]] (Insufficient literature evidence)

## Closest published work

- [PMID 35107332](https://pubmed.ncbi.nlm.nih.gov/35107332/) Genomic Features and Pervasive Negative Selection in Rhodanobacter Strains Isolated from Nitrate and Heavy Metal Contaminated Aquifer.
- [PMID 26583008](https://pubmed.ncbi.nlm.nih.gov/26583008/) Comparative metagenomics reveals impact of contaminants on groundwater microbiomes.
- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.

PMID 35107332 found expanded defense gene sets in contaminated-site Rhodanobacter, and PMID 26583008 compared two wells. This direction tests the gradient across many wells, within genera.
