---
type: "Research direction"
description: "Do particular functional groups of genes (transport, secondary metabolism, defense, mobile elements) track environment within bacterial species, even though whole-genome gene content mostly does not?"
hypothesis: "A small set of functional groups shows a clear environment association after removing evolutionary relatedness. Randomly chosen gene sets of the same size and frequency show none, so the near-zero whole-genome signal is a dilution effect, not an absence of habitat adaptation."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gene-cluster presence/absence, annotations and isolation-source metadata exist, but the per-category, per-species distance correlations with matched random nulls need new computation."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples"]
findings: ["ecotype_analysis--9366534f", "ecotype_analysis--aa4707c1", "ecotype_env_reanalysis--82307b2c", "env_embedding_explorer--7dd94f0f"]
conflicts: ["conflict--ecotype-environment-gene-content--744fe541", "conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca"]
papers: ["29975997", "33602135", "23332119", "31227022"]
builds_on: ["findings/ecotype_analysis--9366534f", "findings/ecotype_analysis--aa4707c1", "findings/ecotype_env_reanalysis--82307b2c", "findings/env_embedding_explorer--7dd94f0f", "conflicts/conflict--ecotype-environment-gene-content--744fe541", "conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca"]
projects: ["ecotype_analysis", "ecotype_env_reanalysis", "ecotype_functional_differentiation", "env_embedding_explorer", "prophage_ecology", "soil_metal_functional_genomics"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Is environment's effect on gene content hidden in a few functions?

Do particular functional groups of genes (transport, secondary metabolism, defense, mobile elements) track environment within bacterial species, even though whole-genome gene content mostly does not?

## Hypothesis

A small set of functional groups shows a clear environment association after removing evolutionary relatedness. Randomly chosen gene sets of the same size and frequency show none, so the near-zero whole-genome signal is a dilution effect, not an absence of habitat adaptation.

## Why it matters

The corpus mostly finds that environment barely predicts gene content, including no difference between free-living and host-associated bacteria, the opposite of what papers on reef and fungal communities report. A functional-group signal would show the weak whole-genome result hides targeted adaptation. A flat result across all groups would point to the environmental descriptors instead.

## How to test it

For the species in the ecotype correlation analysis, split accessory gene clusters by functional category. For each category and species, compute the association between environmental distance and gene-content distance while controlling for evolutionary distance. Build a null from random gene sets matched in size and prevalence. Repeat with organism-proximal isolation-source categories in place of collection coordinates, in free-living and host-associated species separately.

## What would support or refute it

Support: some categories (e.g. transport, defense) exceed the matched random gene sets in many species, and the effect is stronger with isolation-source categories than with coordinates. Refute: every category falls within the random-set range under both descriptors, which would place the weakness in the biology.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gene-cluster presence/absence, annotations and isolation-source metadata exist, but the per-category, per-species distance correlations with matched random nulls need new computation.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/ecotype_analysis--9366534f|Environment effects on gene content are not significant in most species]] (Extends retrieved work)
- Finding: [[findings/ecotype_analysis--aa4707c1|No significant difference in environment effects between free-living and host-associated bacteria]] (In tension with retrieved work)
- Finding: [[findings/ecotype_env_reanalysis--82307b2c|Environmental species show no stronger environment–gene-content correlation than human-associated species]] (Insufficient literature evidence)
- Finding: [[findings/env_embedding_explorer--7dd94f0f|Prior weak embedding-gene content link may reflect clinical dilution, untested here]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--744fe541|Broad Environmental Null versus Subsystem-Specific Environmental Signals in Gene Content]]
- Conflict: [[conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca|Weak Genome-Wide Environmental Signal: Locus-Specific Adaptation or Measurement Limits?]]

## Closest published work

- [PMID 29975997](https://pubmed.ncbi.nlm.nih.gov/29975997/) Pan-Genomics of Lactobacillus plantarum Revealed Group-Specific Genomic Profiles without Habitat Association.
- [PMID 33602135](https://pubmed.ncbi.nlm.nih.gov/33602135/) Comparative genomics reveals broad genetic diversity, extensive recombination and nascent ecological adaptation in Micrococcus luteus.
- [PMID 23332119](https://pubmed.ncbi.nlm.nih.gov/23332119/) Horizontal gene transfer and the evolution of bacterial and archaeal population structure.
- [PMID 31227022](https://pubmed.ncbi.nlm.nih.gov/31227022/) Microbial indicators of environmental perturbations in coral reef ecosystems.

PMIDs 29975997 and 33602135 report weak or nascent habitat association for single species, and PMID 23332119 argues habitat structures gene transfer; none compares functional categories against matched random gene sets across many species.
