---
type: "Research direction"
description: "Only 8 of 50 EC-less gapfilled reactions (16%) were resolved, versus 88 of 151 (58.3%) with EC numbers. Do the unresolved ones reflect real, uncharacterized enzyme activities or non-unique gapfill solutions?"
hypothesis: "EC-less reactions that persist across alternative gapfill solutions and have candidate genes with carbon-source-specific fitness defects are real uncharacterized enzymes. The rest are largely artifacts of non-unique gapfilling."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gapfilled reactions and candidate genes exist in the lakehouse, but alternative gapfilling and structure-based prediction must be run."
collections: ["kescience-fitnessbrowser", "kbase-msd-biochemistry", "kbase-uniprot", "kbase-uniref"]
findings: ["annotation_gap_discovery--61f3d4be", "annotation_gap_discovery--ccaed616", "annotation_gap_discovery--41b7c54a"]
conflicts: ["conflict--metabolic-model-gapfilling--c50aa829"]
papers: ["30910961", "39375541"]
builds_on: ["findings/annotation_gap_discovery--61f3d4be", "findings/annotation_gap_discovery--ccaed616", "findings/annotation_gap_discovery--41b7c54a", "conflicts/conflict--metabolic-model-gapfilling--c50aa829"]
projects: ["acinetobacter_adp1_explorer", "annotation_gap_discovery"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Are unresolved EC-less gapfilled reactions real uncharacterized enzymes or gapfilling artifacts?

Only 8 of 50 EC-less gapfilled reactions (16%) were resolved, versus 88 of 151 (58.3%) with EC numbers. Do the unresolved ones reflect real, uncharacterized enzyme activities or non-unique gapfill solutions?

## Hypothesis

EC-less reactions that persist across alternative gapfill solutions and have candidate genes with carbon-source-specific fitness defects are real uncharacterized enzymes. The rest are largely artifacts of non-unique gapfilling.

## Why it matters

It would show whether the unresolved pairs (105 of 201, 52.2% without a convincing candidate) are an enzymology gap or a modelling artifact, directing effort toward discovery or model repair.

## How to test it

For the 50 EC-less reactions, generate alternative gapfill solutions (including gapseq reconstructions) and score each reaction for stability. Test whether stable reactions have candidate genes with fitness defects on the matching carbon source in the Fitness Browser, and run structure- and reactive-site-based prediction on those candidates, comparing recovery against BLAST. Knockout simulation previously could not validate assignments because models need the gapfilled reactions to grow, so use withheld carbon sources instead.

## What would support or refute it

Support: stable, fitness-linked EC-less reactions receive structure-based candidates that BLAST misses, while unstable reactions show no fitness link. Refute: stability and fitness evidence do not separate the groups, or structure-based methods recover no more than BLAST.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gapfilled reactions and candidate genes exist in the lakehouse, but alternative gapfilling and structure-based prediction must be run.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-msd-biochemistry|ModelSEED Biochemistry]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/annotation_gap_discovery--61f3d4be|Dark reactions without EC numbers are far harder to resolve]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--ccaed616|Over half of gapfilled pairs remain without a convincing gene candidate]] (Insufficient literature evidence)
- Finding: [[findings/annotation_gap_discovery--41b7c54a|Knockout simulation could not validate candidate gene assignments]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--metabolic-model-gapfilling--c50aa829|Does flux balance analysis track experimental growth and essentiality, or not?]]

## Closest published work

- [PMID 30910961](https://pubmed.ncbi.nlm.nih.gov/30910961/) Enzyme annotation for orphan and novel reactions using knowledge of substrate reactive sites.
- [PMID 39375541](https://pubmed.ncbi.nlm.nih.gov/39375541/) High-throughput protein characterization by complementation using DNA barcoded fragment libraries.

PMID 30910961 predicts enzymes for orphan reactions from substrate reactive sites and PMID 39375541 characterizes proteins by barcoded complementation, but neither asks whether unresolved gapfilled EC-less reactions are real activities rather than gapfill artifacts.
