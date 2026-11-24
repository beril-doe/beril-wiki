---
type: "Research direction"
description: "Do differences between annotation sources in cofitness enrichment reflect resolution or just coverage?"
hypothesis: "On a shared gene set and test count, Pfam recovers the lipoprotein and toluene-tolerance terms that old KEGG found, and adds more specific terms than InterProScan GO."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Domain tables are in the catalog; the cofitness networks and enrichment need computing."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.genedomain", "kescience.fitnessbrowser.gene"]
findings: ["fitness_modules--86f7465d"]
conflicts: ["conflict--annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis--25579b23"]
papers: ["29769716", "34597405"]
builds_on: ["findings/fitness_modules--86f7465d", "conflicts/conflict--annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis--25579b23"]
projects: ["amr_cofitness_networks", "fitness_modules"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Does Pfam give more mechanism-specific enrichment than legacy KEGG in cofitness networks?

Do differences between annotation sources in cofitness enrichment reflect resolution or just coverage?

## Hypothesis

On a shared gene set and test count, Pfam recovers the lipoprotein and toluene-tolerance terms that old KEGG found, and adds more specific terms than InterProScan GO.

## Why it matters

It would guide which annotation source to use for function inference from fitness data.

## How to test it

For antimicrobial resistance cofitness neighbourhoods in Fitness Browser organisms, run enrichment with Pfam domains, old KEGG and InterProScan GO using the same genes, background and threshold. Compare terms recovered and test against permuted random gene sets to measure Pfam overcounting.

## What would support or refute it

Support: Pfam recovers KEGG terms plus new specific ones with a low permuted rate. Refute: Pfam misses them or inflates hits in random sets.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Domain tables are in the catalog; the cofitness networks and enrichment need computing.

## Builds on

- Finding: [[findings/fitness_modules--86f7465d|PFam domains and a lower overlap threshold greatly raised module annotation]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis--25579b23|Tension: Broad Pfam Coverage Versus Legacy Annotation Specificity in Cofitness Analysis]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 34597405](https://pubmed.ncbi.nlm.nih.gov/34597405/) eggNOG-mapper v2: Functional Annotation, Orthology Assignments, and Domain Prediction at the Metagenomic Scale.

29769716 supplies fitness data for unknown genes but does not compare annotation sources for enrichment.
