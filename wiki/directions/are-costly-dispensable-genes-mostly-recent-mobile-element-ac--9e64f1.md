---
type: "Research direction"
description: "Do costly genes that are not conserved represent recently acquired horizontally transferred elements rather than decaying metabolic pathways?"
hypothesis: "Costly-dispensable genes are enriched for mobile-element context, such as neighbouring integrases, sparse distribution across genomes and singleton status, beyond what keyword annotation shows, and their loss rate exceeds that of costly-conserved genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "All tables appear in the catalog, but genomic-context and domain analyses have not been run."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.genefitness", "kescience.fitnessbrowser.gene", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.interproscan_domains", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.gene_genecluster_junction"]
findings: ["costly_dispensable_genes--31cecf6a", "costly_dispensable_genes--e1254d2a", "costly_dispensable_genes--f3a85492", "fitness_effects_conservation--30f6d224"]
conflicts: []
papers: ["22448042", "29769716", "36097170", "40728316"]
builds_on: ["findings/costly_dispensable_genes--31cecf6a", "findings/costly_dispensable_genes--e1254d2a", "findings/costly_dispensable_genes--f3a85492", "findings/fitness_effects_conservation--30f6d224"]
projects: ["costly_dispensable_genes", "fitness_effects_conservation"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Are costly dispensable genes mostly recent mobile-element acquisitions still on their way to loss?

Do costly genes that are not conserved represent recently acquired horizontally transferred elements rather than decaying metabolic pathways?

## Hypothesis

Costly-dispensable genes are enriched for mobile-element context, such as neighbouring integrases, sparse distribution across genomes and singleton status, beyond what keyword annotation shows, and their loss rate exceeds that of costly-conserved genes.

## Why it matters

It would show that most laboratory-detected burden reflects selfish elements in transit, not streamlining of metabolism, and would redirect studies of genome reduction.

## How to test it

Take costly-dispensable and costly-conserved genes from the Fitness Browser, link to pangenome clusters, and compare genomic neighbourhood, domain content (InterPro), singleton status and the fraction of species genomes carrying each cluster. Check unannotated genes by domain search for transposase or phage signatures.

## What would support or refute it

Support: costly-dispensable genes sit near mobile-element genes and are patchy across genomes, including among unannotated genes. Refute: after domain search, a large share are ordinary metabolic genes with no mobile context.

## Data

Approach: lakehouse analysis. Readiness: needs compute. All tables appear in the catalog, but genomic-context and domain analyses have not been run.

## Builds on

- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--e1254d2a|Costly non-conserved genes are mostly mobile-element debris from horizontal transfer]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--f3a85492|SEED phage and transposable element category enriched among costly dispensable genes]] (Candidate novel)
- Finding: [[findings/fitness_effects_conservation--30f6d224|Singleton genes are not systematically detrimental]] (Candidate novel)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 40728316](https://pubmed.ncbi.nlm.nih.gov/40728316/) Adaptive pangenomic remodeling in the Azolla cyanobiont amid a transient microbiome.

22448042 and 36097170 address gene loss and pangenome-dependent essentiality, but none tests the mobile-element origin of costly non-conserved genes.
