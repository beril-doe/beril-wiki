---
type: "Concept"
description: "EC-less reactions form a major barrier to gene-function resolution."
sources: ["summaries/annotation_gap_discovery__REPORT.md"]
---
# EC-Less Reactions Are a Distinct Annotation-Resolution Barrier

An EC number is an enzyme-classification identifier used to connect a metabolic reaction to candidate gene functions. In the annotation-gap study, reactions without EC numbers formed a distinct class of annotation problem because the available homology and functional-annotation evidence was harder to connect to stoichiometry-defined reactions. [src: annotation_gap_discovery]

## Key Evidence

Among 201 gapfilled enzymatic reaction-organism pairs, 50 (24.9%) lacked an EC number in ModelSEED and were designated “dark reactions.” [src: annotation_gap_discovery] Only 8 of these 50 (16%) received candidate assignments, compared with 88 of 151 (58.3%) reactions with known EC numbers. [src: annotation_gap_discovery]

The study resolved 96 of 201 pairs (47.8%) through an evidence-triangulation pipeline combining gapfilling, Fitness Browser phenotypes, pangenome annotations, GapMind pathway evidence, and BLAST homology. [src: annotation_gap_discovery] The unresolved set contained 105 pairs (52.2%), including most of the EC-less reactions. [src: annotation_gap_discovery] This pattern supports the interpretation that missing enzyme classification is not merely a cosmetic annotation defect but a measurable barrier to transferring evidence across databases and analytical steps. [src: annotation_gap_discovery]

## Why EC-Less Reactions Resist Resolution

The pipeline used EC numbers to connect gapfilled reactions to Fitness Browser gene annotations, alternative Bakta annotations, GapMind pathway evidence, and Swiss-Prot exemplar sequences. [src: annotation_gap_discovery] NB03 matched gapfilled reaction EC numbers to Fitness Browser gene annotations through pangenome gene clusters and resolved 51 of 201 pairs (25.4%) with 107 gene candidates. [src: annotation_gap_discovery] NB04 queried Bakta annotations for alternative EC numbers and product-name matches, added 22 newly resolved pairs (10.9%), and produced 1,459 Bakta EC candidate entries. [src: annotation_gap_discovery] NB06 downloaded 328 Swiss-Prot exemplar sequences for 75 of 84 unique ECs, identified 154 DIAMOND hits, and contributed to the final 96 resolved pairs through evidence triangulation. [src: annotation_gap_discovery]

For an EC-less reaction, the reaction stoichiometry remains available, but the standard enzyme-classification key used to retrieve homologs and compare annotations is absent. [src: annotation_gap_discovery] The study therefore treated the EC-less category as a limitation of evidence linkage rather than as evidence that the underlying reaction lacks a gene in the organism. [src: annotation_gap_discovery]

## Relation to Functional Dark Matter

The EC-less category overlaps operationally with the broader problem of [[concepts/functional-dark-matter]], but the two problems are not identical. [src: annotation_gap_discovery] EC-less reactions are defined by missing enzyme-classification identifiers in ModelSEED, whereas functional dark matter concerns genes or proteins whose functions remain poorly characterized or unassigned. [src: annotation_gap_discovery] The study found that EC-less reactions were difficult to resolve even within a workflow that included BLAST, pangenome conservation, fitness evidence, and pathway evidence. [src: annotation_gap_discovery]

This finding refines [[concepts/structural-annotation-gap]] by showing that a missing reaction-to-enzyme identifier can block downstream evidence integration even when sequence and phenotype data exist. [src: annotation_gap_discovery] It also supports [[concepts/evidence-triangulation-for-functional-annotation]]: multiple evidence streams improved overall resolution, but their integration remained constrained when reactions lacked a common functional anchor. [src: annotation_gap_discovery]

## Relation to Metabolic-Model Gapfilling

The EC-less barrier arose within a gapfilling workflow in which conditional gapfilling addressed 38 false-negative organism–carbon-source cases and added 219 reactions: 201 enzymatic, 14 transport, and 12 exchange. [src: annotation_gap_discovery] The models used default ModelSEED gapfilling, which minimizes the number of added reactions but does not guarantee biological optimality, and multiple valid gapfilling solutions may exist for a false-negative case. [src: annotation_gap_discovery]

Consequently, an EC-less reaction combines two uncertainties: uncertainty about whether the selected gapfilled reaction is the biologically correct solution and uncertainty about which gene performs that reaction. [src: annotation_gap_discovery] This interaction strengthens the case for treating [[concepts/metabolic-model-gapfilling]] and EC-less annotation as linked but separable validation problems. [src: annotation_gap_discovery]

## Interpretation and Limits

The evidence for an EC-less resolution barrier is strong within this dataset because resolution was directly compared between 50 EC-less and 151 EC-annotated reaction pairs. [src: annotation_gap_discovery] The result should not be interpreted as a universal estimate for all metabolic databases or organisms because the dataset contained 14 organisms, 12 of which were Proteobacteria, and because the models were based on automated RAST annotations with systematic errors. [src: annotation_gap_discovery]

GapMind provided only partial support for resolving these gaps because it covers approximately 80 carbon and amino acid pathways rather than full metabolism, and its available BERDL output reports pathway-level step counts rather than individual step identities. [src: annotation_gap_discovery] The study also reported that baseline FBA achieved 42.5% overall accuracy across 574 organism–carbon-source combinations and produced 330 false positives, indicating that model permissiveness could complicate interpretation of any reaction selected by gapfilling. [src: annotation_gap_discovery]

The central implication is therefore prioritization rather than abandonment: EC-less reactions should receive dedicated functional-characterization workflows, while their candidate assignments should not be treated as equivalent to assignments supported by established EC-linked evidence. [src: annotation_gap_discovery]

## Open Directions

- Use the 50 EC-less reactions and their 201 reaction-organism records to compare alternative stoichiometric gapfilling solutions with gapseq reconstructions, asking which reactions remain stable across reconstruction methods. [src: annotation_gap_discovery]
- Combine sequence profiles, structure-based searches, and targeted biochemical assays for the 42 unresolved EC-less reaction-organism pairs, asking whether enzyme families can be assigned without an existing EC identifier. [src: annotation_gap_discovery]
- Reanalyze the 50 EC-less reactions with the 23 available GPR insertions and targeted gene-knockout or CRISPRi experiments, asking whether phenotype changes distinguish competing candidate genes without relying on circular model growth requirements. [src: annotation_gap_discovery]
- Expand the EC-less analysis from the 14-organism dataset to all 48 Fitness Browser organisms, asking whether the 16% EC-less resolution rate is reproduced across broader phylogenetic and annotation coverage. [src: annotation_gap_discovery]
- Integrate the 104 GapMind-gapfill pathway pairings with reaction-level annotation and additional pathway databases, asking whether step-level evidence can recover EC-less functions outside the approximately 80 pathways covered by GapMind. [src: annotation_gap_discovery]
