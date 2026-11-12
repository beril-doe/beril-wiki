---
type: "Research direction"
description: "Do gapfilled reactions that have no enzyme number, and that are rarely resolved to a gene, reflect known enzymes acting on non-native substrates rather than undiscovered enzyme families?"
hypothesis: "For these reactions, fitness-supported candidate genes encode enzymes whose annotated reactions are chemically more similar to the gapfilled reaction than random genes from the same organism are."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Reactions, fitness and annotation tables are in the catalog; the gapfilled reaction list and the similarity scoring between candidate and gapfilled reactions must be rebuilt and computed."
databases: ["kbase.msd_biochemistry", "kescience.fitnessbrowser"]
tables: ["kbase.msd_biochemistry.reaction", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.besthitkegg", "kescience.fitnessbrowser.seedannotation"]
findings: ["annotation_gap_discovery--61f3d4be", "annotation_gap_discovery--ccaed616", "annotation_gap_discovery--41b7c54a"]
conflicts: ["conflict--metabolic-model-gapfilling--c50aa829"]
papers: ["30910961", "25968644"]
builds_on: ["findings/annotation_gap_discovery--61f3d4be", "findings/annotation_gap_discovery--ccaed616", "findings/annotation_gap_discovery--41b7c54a", "conflicts/conflict--metabolic-model-gapfilling--c50aa829"]
projects: ["acinetobacter_adp1_explorer", "annotation_gap_discovery"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Are gapfilled reactions without enzyme numbers done by known enzymes with broad substrate range?

Do gapfilled reactions that have no enzyme number, and that are rarely resolved to a gene, reflect known enzymes acting on non-native substrates rather than undiscovered enzyme families?

## Hypothesis

For these reactions, fitness-supported candidate genes encode enzymes whose annotated reactions are chemically more similar to the gapfilled reaction than random genes from the same organism are.

## Why it matters

Of the 50 reactions without enzyme numbers, only 8 were resolved, against 88 of 151 for reactions with them. If promiscuity explains the gap, model repair should search known enzymes broadly. If not, truly new families are probably needed.

## How to test it

For each gapfilled reaction without an enzyme number, collect genes whose mutants show fitness effects on the carbon source that required the reaction, across the Fitness Browser organisms. Take each candidate's annotated reaction from its best-hit pathway and functional annotations, and score chemical similarity to the gapfilled reaction by comparing substrates, products and reaction definitions from the biochemistry reaction table (similarity is computed here, as the catalog did not show a precomputed similarity table among the tables listed). Compare with matched-count random genes and with reactions that have enzyme numbers. Test top candidates with purified-protein assays on the predicted substrate.

## What would support or refute it

Support: candidate enzymes are more similar to the gapfilled reaction than random genes, and some candidates turn the substrate over in assays. Refute: similarity is indistinguishable from random and assays are negative, pointing to unknown families.

## Data

Approach: analysis then experiment. Readiness: needs compute. Reactions, fitness and annotation tables are in the catalog; the gapfilled reaction list and the similarity scoring between candidate and gapfilled reactions must be rebuilt and computed.

## Builds on

- Finding: [[findings/annotation_gap_discovery--61f3d4be|Dark reactions without EC numbers are far harder to resolve]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--ccaed616|Over half of gapfilled pairs remain without a convincing gene candidate]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--41b7c54a|Knockout simulation could not validate candidate gene assignments]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--metabolic-model-gapfilling--c50aa829|Does flux balance analysis track experimental growth and essentiality, or not?]]

## Closest published work

- [PMID 30910961](https://pubmed.ncbi.nlm.nih.gov/30910961/) Enzyme annotation for orphan and novel reactions using knowledge of substrate reactive sites.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

PMID 30910961 annotates orphan and novel reactions from substrate reactive sites, and PMID 25968644 provides the fitness method. Neither tests whether fitness-linked candidates for specific unresolved gapfilled reactions are promiscuous known enzymes.
