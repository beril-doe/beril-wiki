---
type: "Research direction"
description: "If lung P. aeruginosa has lost sugar catabolism but kept amino acid catabolism, does it rely more on amino acids in lung-like conditions, making commensals that compete for those amino acids more effective against lung isolates than against non-lung isolates?"
hypothesis: "Lung lineages lose sugar pathways independently of clade membership while amino acid catabolism stays conserved, so lung and CF isolates grow more on amino acids than non-lung isolates do. Commensal competition for cysteine, threonine and methionine then inhibits lung isolates more than non-lung isolates."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Genome analyses use existing data, but inhibition has not been measured against ExoS+ or non-lung strains."
collections: ["kbase-ke-pangenome"]
findings: ["cf_formulation_design--460ed03a", "cf_formulation_design--1799127b", "cf_formulation_design--8bf20af1", "cf_formulation_design--951bde52"]
conflicts: []
papers: ["25409940", "31214142", "17873029", "19936230", "27881418", "35174108"]
builds_on: ["findings/cf_formulation_design--460ed03a", "findings/cf_formulation_design--1799127b", "findings/cf_formulation_design--8bf20af1", "findings/cf_formulation_design--951bde52"]
projects: ["cf_formulation_design"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Does lung adaptation make P. aeruginosa depend on amino acids that commensals can contest?

If lung P. aeruginosa has lost sugar catabolism but kept amino acid catabolism, does it rely more on amino acids in lung-like conditions, making commensals that compete for those amino acids more effective against lung isolates than against non-lung isolates?

## Hypothesis

Lung lineages lose sugar pathways independently of clade membership while amino acid catabolism stays conserved, so lung and CF isolates grow more on amino acids than non-lung isolates do. Commensal competition for cysteine, threonine and methionine then inhibits lung isolates more than non-lung isolates.

## Why it matters

It would turn a genome-scale streamlining inference into a testable vulnerability, and show whether the commensal-inhibition design, built on the ExoU+ PA14 strain, transfers to the ExoS+ strains that dominate CF.

## How to test it

Analysis: across the 6,760 P. aeruginosa genomes in kbase-ke-pangenome (1,796 lung or CF among 5,199 with metadata), use phylogenetically controlled models to test whether lower sugar-pathway scores (sorbitol -0.165, mannitol -0.204, gluconate -0.185) recur across independent lung lineages rather than tracking clade, and whether amino acid pathways stay at 97%+ conservation. Experiment: in defined media with a single sugar or a single amino acid as carbon source, grow ExoS+ CF isolates, non-lung isolates and PA14 alone and with M. luteus, N. mucosa and S. salivarius. Measure inhibition by substrate class, focusing on the selective substrates (commensal-to-PA14 ratios 0.77 to 0.96).

## What would support or refute it

Support: independent recurrent sugar-pathway loss in lung lineages, and stronger commensal inhibition of lung isolates on amino acid media. Refute: lower scores explained by clade membership, or equal inhibition across isolate origins. The relaxed-selection reading is an evolutionary interpretation, not a measured loss, and PA14 was the only strain in the inhibition assays so far.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Genome analyses use existing data, but inhibition has not been measured against ExoS+ or non-lung strains.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/cf_formulation_design--460ed03a|Lung P. aeruginosa genomes score lower on sugar pathways than non-lung genomes]] (Extends retrieved work)
- Finding: [[findings/cf_formulation_design--1799127b|Cystic fibrosis P. aeruginosa is mostly ExoS+, unlike the PA14 assay strain]] (Extends retrieved work)
- Finding: [[findings/cf_formulation_design--8bf20af1|No tested substrate gives commensals a clear advantage over PA14]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--951bde52|Metabolic overlap with PA14 predicts inhibition, but only modestly]] (Insufficient literature evidence)

## Closest published work

- [PMID 25409940](https://pubmed.ncbi.nlm.nih.gov/25409940/) Impact of glycerol-3-phosphate dehydrogenase on virulence factor production by Pseudomonas aeruginosa.
- [PMID 31214142](https://pubmed.ncbi.nlm.nih.gov/31214142/) Catabolism of Nucleic Acids by a Cystic Fibrosis Pseudomonas aeruginosa Isolate: An Adaptive Pathway to Cystic Fibrosis Sputum Environment.
- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 19936230](https://pubmed.ncbi.nlm.nih.gov/19936230/) Pseudomonas aeruginosa population structure revisited.
- [PMID 27881418](https://pubmed.ncbi.nlm.nih.gov/27881418/) Environmental Pseudomonads Inhibit Cystic Fibrosis Patient-Derived Pseudomonas aeruginosa.
- [PMID 35174108](https://pubmed.ncbi.nlm.nih.gov/35174108/) Commensal Bacteria in the Cystic Fibrosis Airway Microbiome Reduce P. aeruginosa Induced Inflammation.

PMID 25409940 and 31214142 describe individual CF isolates' metabolic adaptation, PMID 19936230 reports ExoS+ dominance in CF, and PMID 17873029 covers CF sputum carbon preferences; none links genome-wide carbon pathway scores to commensal inhibition by substrate class.
