---
type: "Research direction"
description: "Some genes cost fitness in the lab and are dispensable, yet a share still have condition-specific fitness effects. Are such genes found in a larger fraction of their species' genomes than costly dispensable genes without such effects?"
hypothesis: "Among costly dispensable genes, those with condition-specific fitness effects are present in a larger fraction of genomes within their species than those without, a pattern that would be consistent with, though not proof of, slower gene loss."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "The costly dispensable classes and their condition-specific phenotypes already exist and the pangenome links are established."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["costly_dispensable_genes--7f8211ca", "costly_dispensable_genes--f3a85492", "costly_dispensable_genes--31cecf6a"]
conflicts: ["conflict--essentiality-assay-discordance--3eeac603"]
papers: ["22448042", "22761588", "28344773", "36097170"]
builds_on: ["findings/costly_dispensable_genes--7f8211ca", "findings/costly_dispensable_genes--f3a85492", "findings/costly_dispensable_genes--31cecf6a", "conflicts/conflict--essentiality-assay-discordance--3eeac603"]
projects: ["conservation_fitness_synthesis", "core_gene_tradeoffs", "costly_dispensable_genes"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do costly dispensable genes with condition-specific fitness effects persist in more genomes?

Some genes cost fitness in the lab and are dispensable, yet a share still have condition-specific fitness effects. Are such genes found in a larger fraction of their species' genomes than costly dispensable genes without such effects?

## Hypothesis

Among costly dispensable genes, those with condition-specific fitness effects are present in a larger fraction of genomes within their species than those without, a pattern that would be consistent with, though not proof of, slower gene loss.

## Why it matters

It would link lab fitness trade-offs to how widely costly genes are retained, giving a data-based test of the Black Queen idea that costly genes are shed unless they sometimes matter.

## How to test it

In the Fitness Browser, classify genes as costly dispensable with or without condition-specific fitness effects. Map them to the Pangenome Collection and compare within-species prevalence, controlling for gene length, mobile-element annotation and organism. Repeat after excluding genes annotated as transposase, integrase or phage, which dominate the costly dispensable class.

## What would support or refute it

Support: genes with condition-specific effects have higher within-species prevalence even after removing mobile-element genes. Refute: prevalence is the same in both groups. Because the comparison is cross-sectional, support would motivate, not establish, a slower loss rate.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. The costly dispensable classes and their condition-specific phenotypes already exist and the pangenome links are established.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/costly_dispensable_genes--7f8211ca|Costly dispensable genes are not inert: some have condition-specific phenotypes]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--f3a85492|Mobile-element and virulence SEED categories enriched versus costly conserved genes]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--essentiality-assay-discordance--3eeac603|Do costly, conserved genes show natural selection, or only lab-inferred selection signatures?]]

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 28344773](https://pubmed.ncbi.nlm.nih.gov/28344773/) Escherichia coli ST131: a multidrug-resistant clone primed for global domination.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.

PMID 22448042 and PMID 22761588 predict loss of costly dispensable genes but do not test whether condition-specific fitness effects relate to retention in measured fitness data.
