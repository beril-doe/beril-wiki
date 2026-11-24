---
type: "Concept"
description: "How many non-pathway genes (cofactor, respiration, iron, regulators) a substrate-specific catabolism requires, and how co-fitness assigns them to subsystems; stops at the aromatic case in one organism."
sources: ["summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/pitfalls.md"]
---
# Support-gene networks around catabolic pathways

This page covers one case: the support-gene network around quinate catabolism in *Acinetobacter baylyi* ADP1 (see [[entities/acinetobacter-baylyi-adp1]]). In this organism, 51 quinate-specific genes form a metabolic dependency network around the β-ketoadipate pathway. [src: aromatic_catabolism_network] Co-fitness analysis assigns 44 of the 51 genes (86%) to four functional subsystems plus transcriptional regulators. [src: aromatic_catabolism_network] The evidence comes from one organism and one substrate, and from a growth matrix of only 8 conditions. [src: aromatic_catabolism_network] It is therefore suggestive, not a general rule.

## Literature Context

The candidate papers establish the pathway core that the hub's support network surrounds, but they do not address the support genes themselves. The β-ketoadipate pathway is described as a route that funnels protocatechuate and catechol into succinyl-CoA and acetyl-CoA, and it is well characterized in bacteria but less so in fungi [PMID 37399977](https://pubmed.ncbi.nlm.nih.gov/37399977/). A genomic survey of 13 lignin-oxidising bacteria found that ten of the eleven genomes with aromatic degradation clusters contain the central β-ketoadipate pathway, which makes it the most common route for aromatic metabolism in lignin-degrading bacteria [PMID 32088760](https://pubmed.ncbi.nlm.nih.gov/32088760/). In Sinorhizobium meliloti, protocatechuate catabolism genes sit in two transcriptional units, pcaDCHGB and pcaIJF. They are controlled by the LysR-type regulator PcaQ and the IclR-type regulator PcaR [PMID 16885292](https://pubmed.ncbi.nlm.nih.gov/16885292/). In Rhodococcus opacus, knockouts confirmed two degradation routes of the pathway for five aromatic compounds [PMID 30059786](https://pubmed.ncbi.nlm.nih.gov/30059786/).

Several papers hint at wider dependencies beyond the core enzymes. In Aspergillus niger, deletion of NRRL3_00837 abolished growth on protocatechuic acid, yet the recombinant protein did not affect the in vitro conversion to β-ketoadipate, so its function is unknown [PMID 37399977](https://pubmed.ncbi.nlm.nih.gov/37399977/). This is a fungal precedent for a required non-pathway gene. In adaptively evolved R. opacus, mutations in several redox-related genes were shared across mutants. One mutant had 56% lower superoxide dismutase activity than wild type, which suggests that redox reactions matter for aromatic utilization [PMID 30059786](https://pubmed.ncbi.nlm.nih.gov/30059786/). In Pseudomonas putida KT2440 grown on vanillin, 662 proteins changed in abundance versus glucose. These included enzymes of the β-ketoadipate pathway and central energy metabolism, which is proteome-level evidence of broad rewiring [PMID 25026441](https://pubmed.ncbi.nlm.nih.gov/25026441/). Benzoate-grown P. aeruginosa also showed metabolic reconfiguration relative to glucose [PMID 35276454](https://pubmed.ncbi.nlm.nih.gov/35276454/). These are abundance or expression measurements, not fitness measurements.

Against this background, the corpus's central finding is that 51 quinate-specific genes surround the 8 core pathway genes in Acinetobacter baylyi ADP1. Co-fitness assigns 44 of the 51 to Complex I, the aromatic pathway, iron acquisition, PQQ biosynthesis and regulators. This **extends** the literature. The regulator category is consistent with the pca regulators in S. meliloti [PMID 16885292](https://pubmed.ncbi.nlm.nih.gov/16885292/). The redox and energy-metabolism emphasis, with Complex I as the largest group at 21 genes, is consistent in direction with the redox signals in R. opacus [PMID 30059786](https://pubmed.ncbi.nlm.nih.gov/30059786/) and the energy-metabolism changes in P. putida [PMID 25026441](https://pubmed.ncbi.nlm.nih.gov/25026441/). The corpus's genome-wide, fitness-based quantification of the support genes, including the 7:1 support-to-pathway ratio, has no counterpart among these candidates, so it is novel here. The candidates give no evidence on the PQQ or iron dependencies, and none tests the proposed high-NADH-flux interpretation.

The corpus's own limits remain. The evidence comes from one organism, one substrate and a matrix of only 8 conditions. The 7:1 ratio therefore cannot be called general on the basis of these papers, which span other species and use different methods.

## Size of the support network

The β-ketoadipate pathway has 8 core genes, but 51 genes show quinate-specific growth defects, reported as a 7:1 support-to-pathway ratio. [src: discoveries] It also states that the support requirement exceeds the pathway by 7:1. [src: aromatic_catabolism_network] The two figures (7:1 and over 8×) are the report's own wording. They are not reconciled here.

## How co-fitness assigns genes

Co-fitness analysis assigns 44 of 51 genes (86%) to four subsystems plus regulators. [src: aromatic_catabolism_network] The cross-project digest lists the support genes as Complex I (21 genes, NADH reoxidation), iron acquisition (7 genes, Fe²⁺ for the ring-cleavage dioxygenase) and PQQ (pyrroloquinoline quinone) biosynthesis (2 genes, cofactor for quinate dehydrogenase). [src: discoveries]

| Subsystem | Genes | Role |
|---|---|---|
| Complex I | 21 | NADH reoxidation; the TCA (tricarboxylic acid) cycle generates excess NADH (reduced nicotinamide adenine dinucleotide) from aromatic catabolism [src: aromatic_catabolism_network] |
| Aromatic pathway | 8 | quinate → protocatechuate → β-ketoadipate → TCA cycle [src: aromatic_catabolism_network] |
| Iron acquisition | 7 | Fe²⁺ supply for protocatechuate 3,4-dioxygenase ring cleavage [src: aromatic_catabolism_network] |
| PQQ biosynthesis | 2 | PQQ cofactor for quinoprotein quinate dehydrogenase [src: aromatic_catabolism_network] |
| Regulation | 6 | transcriptional control of aromatic degradation operons [src: aromatic_catabolism_network] |
| Unassigned | 7 | low co-fitness with all subsystems [src: aromatic_catabolism_network] |

Within-category co-fitness is far higher than between-category co-fitness. The Complex I mean is r = 0.992 and the aromatic pathway mean is r = 0.961. [src: aromatic_catabolism_network] The report reads the Complex I value as nearly identical phenotypic profiles, consistent with single-operon co-regulation. [src: aromatic_catabolism_network]

## Biochemical reasons for each subsystem

- Quinate dehydrogenase (quiA) is a PQQ-dependent quinoprotein. This explains the dependence on the PQQ genes pqqC and pqqD. [src: aromatic_catabolism_network] See [[entities/pyrroloquinoline-quinone-biosynthesis]].
- Protocatechuate 3,4-dioxygenase (pcaGH) is a non-heme Fe²⁺-dependent ring-cleavage enzyme. This explains 7 iron acquisition genes: siderophore biosynthesis, ExbD/TolR transport, a ferrichrome receptor and a TonB-dependent receptor. [src: aromatic_catabolism_network] See [[entities/protocatechuate-3-4-dioxygenase]].
- Complex I is the largest dependency. It covers 21 of 51 genes (41%). [src: aromatic_catabolism_network] See [[entities/respiratory-complex-i-nadh-ubiquinone-oxidoreductase]] and [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].

The report claims the first whole-genome quantification of the PQQ and iron dependencies. [src: aromatic_catabolism_network] It says the PQQ-gene result extends a cited transcriptomic observation to the functional level. [src: aromatic_catabolism_network] The cross-project digest interprets the network as a "high-NADH-flux bottleneck network" rather than an aromatic-chemistry-specific one. [src: discoveries] This is an interpretation. The report proposes testing it directly. [src: aromatic_catabolism_network]

## Recovering uncharacterized genes

Of 23 genes first categorized as Other or Unknown, 16 were assigned to support subsystems with medium or high confidence. [src: aromatic_catabolism_network] Co-fitness recovered pcaC (4-carboxymuconolactone decarboxylase), which keyword matching had miscategorized. [src: aromatic_catabolism_network] The pitfalls digest gives r=0.978 with the aromatic pathway for pcaC. [src: pitfalls] The DUF proteins ACIAD3137 and ACIAD2176 correlate with Complex I genes at r > 0.98. They are candidate Complex I accessory factors. [src: aromatic_catabolism_network] The report proposes protein-protein interaction studies or Complex I co-purification to test whether they are physical accessory factors or indirect regulatory connections. [src: aromatic_catabolism_network] See [[entities/aciad3137-and-aciad2176]] and [[entities/cofitness-analysis]].

## Caveats

- The analysis uses only 8 conditions, which limits gene–gene resolution. [src: aromatic_catabolism_network] The matrix has about 5 independent dimensions. [src: aromatic_catabolism_network] More conditions would sharpen subsystem boundaries. [src: aromatic_catabolism_network]
- The 11 Complex I assignments beyond the core nuo operon rest on phenotypic correlation alone. Some may be indirect connections rather than physical association. [src: aromatic_catabolism_network]

## Open Directions

- Run co-purification with Complex I for ACIAD3137 and ACIAD2176 to separate physical accessory roles from indirect connections.
- Add benzoate, catechol and vanillate, plus iron limitation and respiratory inhibitors. This would refine subsystem boundaries and test the NADH-flux hypothesis directly.
- Repeat the support-gene count for other substrates and organisms. This would show whether the 7:1 ratio is general or specific to ADP1 and quinate.
