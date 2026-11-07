---
type: "Research direction"
description: "Is the lack of a complete serine biosynthesis pathway in Desulfovibrio vulgaris Hildenborough a real serine requirement, or does the organism make serine through a route the pathway predictor does not recognise?"
hypothesis: "Desulfovibrio vulgaris grows without added serine by making it from glycine and one-carbon units through a non-canonical route, so the predicted gap is a blind spot in the predictor and not an auxotrophy."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Fitness data and pathway calls are in the lakehouse, but the growth and isotope-tracing experiment has not been done."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["essential_metabolome--04b688de", "essential_metabolome--a8599193"]
conflicts: []
papers: ["29324779", "15077118", "32576650"]
builds_on: ["findings/essential_metabolome--04b688de", "findings/essential_metabolome--a8599193"]
projects: ["essential_metabolome"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Does Desulfovibrio vulgaris make serine by a route that pathway predictors miss?

Is the lack of a complete serine biosynthesis pathway in Desulfovibrio vulgaris Hildenborough a real serine requirement, or does the organism make serine through a route the pathway predictor does not recognise?

## Hypothesis

Desulfovibrio vulgaris grows without added serine by making it from glycine and one-carbon units through a non-canonical route, so the predicted gap is a blind spot in the predictor and not an auxotrophy.

## Why it matters

The organism was the only one of seven with no complete serine pathway call, and the remaining diversity in amino acid pathways was read as ecological adaptation. If the gap is a missed route, that reading is weaker and pathway predictors have a systematic blind spot in sulfate reducers. If it is real, it is a rare natural serine auxotrophy.

## How to test it

Grow Desulfovibrio vulgaris Hildenborough in defined serine-free medium with and without glycine and a one-carbon source. Trace labelled glycine into serine. In parallel, read mutant fitness for the serine hydroxymethyltransferase gene and for any partial serine pathway genes in the Fitness Browser, and compare with the other six organisms that have complete calls.

## What would support or refute it

Growth and labelled serine without added serine, plus a fitness cost for the glycine-to-serine gene, would support a missed route. No growth without serine, and no fitness cost for any candidate gene, would support a true auxotrophy and refute the hypothesis.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Fitness data and pathway calls are in the lakehouse, but the growth and isotope-tracing experiment has not been done.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/essential_metabolome--04b688de|Desulfovibrio vulgaris alone lacks a complete serine biosynthesis prediction]] (Insufficient literature evidence)
- Finding: [[findings/essential_metabolome--a8599193|Pathway completeness is near-universal rather than strictly universal in this sample]] (Insufficient literature evidence)

## Closest published work

- [PMID 29324779](https://pubmed.ncbi.nlm.nih.gov/29324779/) Filling gaps in bacterial amino acid biosynthesis pathways with high-throughput genetics.
- [PMID 15077118](https://pubmed.ncbi.nlm.nih.gov/15077118/) The genome sequence of the anaerobic, sulfate-reducing bacterium Desulfovibrio vulgaris Hildenborough.
- [PMID 32576650](https://pubmed.ncbi.nlm.nih.gov/32576650/) GapMind: Automated Annotation of Amino Acid Biosynthesis.

PMID 29324779 used high-throughput genetics to fill amino acid pathway gaps predicted by automated tools, and PMID 15077118 gives the genome; neither says whether this organism makes serine without a canonical pathway.
