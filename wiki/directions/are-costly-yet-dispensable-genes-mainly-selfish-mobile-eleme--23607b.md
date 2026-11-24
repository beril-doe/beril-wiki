---
type: "Research direction"
description: "Do costly but non-conserved genes in Fitness Browser bacteria persist because they are selfish mobile elements that have not yet been purged, rather than degrading metabolic pathways?"
hypothesis: "Costly+dispensable genes that are not mobile-element-annotated sit near annotated mobile elements or have atypical GC far more often than costly+conserved genes. Their burden should also stay when the one-experiment cost rule is replaced by a rule requiring replication across several experiments."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Fitness and pangenome tables appear in the catalog, but linking genes to pangenome clusters and computing neighbourhoods requires new compute."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.seedannotation", "kescience.fitnessbrowser.experiment", "kbase.ke_pangenome.gene_cluster"]
findings: ["costly_dispensable_genes--31cecf6a", "costly_dispensable_genes--e1254d2a", "costly_dispensable_genes--f3a85492"]
conflicts: []
papers: ["22448042", "29769716", "36097170", "40728316"]
builds_on: ["findings/costly_dispensable_genes--31cecf6a", "findings/costly_dispensable_genes--e1254d2a", "findings/costly_dispensable_genes--f3a85492"]
projects: ["costly_dispensable_genes"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Are costly yet dispensable genes mainly selfish mobile elements still awaiting loss?

Do costly but non-conserved genes in Fitness Browser bacteria persist because they are selfish mobile elements that have not yet been purged, rather than degrading metabolic pathways?

## Hypothesis

Costly+dispensable genes that are not mobile-element-annotated sit near annotated mobile elements or have atypical GC far more often than costly+conserved genes. Their burden should also stay when the one-experiment cost rule is replaced by a rule requiring replication across several experiments.

## Why it matters

It would show that horizontal gene transfer expansion, not adaptive loss of metabolic functions, is the main source of costly accessory genes. That would redirect how gene loss theories are applied to pangenomes.

## How to test it

For Fitness Browser organisms, classify genes as costly if they show a fitness gain in at least 2 independent experiments, then as conserved or dispensable using pangenome core status. Compare keyword-based and neighbourhood-based mobile-element signals (distance to transposase, integrase and phage genes; GC deviation) using the Fitness Browser gene and SEED annotations and the pangenome gene cluster core flags. Repeat with the original single-experiment rule.

## What would support or refute it

Support: the enrichment holds under the replicated cost rule and extends to unannotated genes by neighbourhood. Refute: the enrichment vanishes under the replicated rule, or unannotated costly genes are not near mobile elements, suggesting noise or metabolic decay.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Fitness and pangenome tables appear in the catalog, but linking genes to pangenome clusters and computing neighbourhoods requires new compute.

## Builds on

- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--e1254d2a|Costly non-conserved genes are mostly mobile-element debris from horizontal transfer]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--f3a85492|SEED phage and transposable element category enriched among costly dispensable genes]] (Candidate novel)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 40728316](https://pubmed.ncbi.nlm.nih.gov/40728316/) Adaptive pangenomic remodeling in the Azolla cyanobiont amid a transient microbiome.

Black Queen work (22448042) and pangenome essentiality (36097170) address gene loss, but neither tests whether costly dispensable genes are mobile-element debris; this direction tests that with a replicated cost definition.
