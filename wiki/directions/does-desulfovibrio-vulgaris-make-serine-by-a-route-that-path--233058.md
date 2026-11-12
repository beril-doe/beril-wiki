---
type: "Research direction"
description: "Desulfovibrio vulgaris Hildenborough is the only one of seven organisms predicted to lack complete serine synthesis. Does it make serine by a non-canonical route, and which genes carry it?"
hypothesis: "D. vulgaris grows without serine by making it from glycine or threonine, so mutants of the glycine-to-serine enzyme lose fitness in serine-free defined medium while homologs of the canonical phosphoglycerate route have little effect."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The decisive test needs serine-free growth and labeled-glycine tracing, which are new measurements; fitness and annotation tables for this organism are in the catalog, but whether serine-free defined-medium experiments exist was not shown."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.besthitkegg", "kbase.ke_pangenome.gapmind_pathways"]
findings: ["essential_metabolome--04b688de", "essential_metabolome--6a696123"]
conflicts: ["conflict--cross-condition-metabolic-comparability--e6421a5b"]
papers: ["29324779", "15077118"]
builds_on: ["findings/essential_metabolome--04b688de", "findings/essential_metabolome--6a696123", "conflicts/conflict--cross-condition-metabolic-comparability--e6421a5b"]
projects: ["essential_metabolome", "webofmicrobes_explorer"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Does Desulfovibrio vulgaris make serine by a route that pathway predictors miss?

Desulfovibrio vulgaris Hildenborough is the only one of seven organisms predicted to lack complete serine synthesis. Does it make serine by a non-canonical route, and which genes carry it?

## Hypothesis

D. vulgaris grows without serine by making it from glycine or threonine, so mutants of the glycine-to-serine enzyme lose fitness in serine-free defined medium while homologs of the canonical phosphoglycerate route have little effect.

## Why it matters

A true serine requirement would be an unusual auxotrophy for a free-living sulfate reducer. A hidden route would show a systematic blind spot of automated pathway prediction in anaerobes.

## How to test it

From mutant fitness data for D. vulgaris in defined media with and without serine or glycine, compare fitness of glycine hydroxymethyltransferase, threonine aldolase and phosphoglycerate-route homologs, and list any genes with strong serine-dependent effects. Then grow the wild type in serine-free defined medium, with labeled glycine to trace serine formation, and complement top candidate genes.

## What would support or refute it

Support: growth without serine, and strong fitness loss of the glycine-route gene only in serine-free medium. Refute: no growth without serine, which would confirm auxotrophy, or growth with no fitness effect in any candidate, which would point to an unannotated route.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The decisive test needs serine-free growth and labeled-glycine tracing, which are new measurements; fitness and annotation tables for this organism are in the catalog, but whether serine-free defined-medium experiments exist was not shown.

## Builds on

- Finding: [[findings/essential_metabolome--04b688de|Desulfovibrio vulgaris alone lacks a complete serine biosynthesis prediction]] (Insufficient literature evidence)
- Finding: [[findings/essential_metabolome--6a696123|Nearly all amino-acid biosynthesis pathways predicted complete across seven organisms]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cross-condition-metabolic-comparability--e6421a5b|Does Pathway Completeness and Metabolite Production Evidence Speak to Condition-Specific Metabolic Requirement or Use?]]

## Closest published work

- [PMID 29324779](https://pubmed.ncbi.nlm.nih.gov/29324779/) Filling gaps in bacterial amino acid biosynthesis pathways with high-throughput genetics.
- [PMID 15077118](https://pubmed.ncbi.nlm.nih.gov/15077118/) The genome sequence of the anaerobic, sulfate-reducing bacterium Desulfovibrio vulgaris Hildenborough.

PMID 29324779 fills predicted amino acid pathway gaps with high-throughput genetics and covers D. vulgaris, and PMID 15077118 is its genome. Neither says whether this organism has a serine gap or how it would be bridged.
