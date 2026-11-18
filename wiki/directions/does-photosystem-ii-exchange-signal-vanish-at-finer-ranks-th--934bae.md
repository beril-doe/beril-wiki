---
type: "Research direction"
description: "Why is photosystem II gene exchange between photic-aquatic habitats and other lineages detectable at class rank in Cyanobacteria but not at genus rank, and does the answer depend on how many genera carry the full gene set?"
hypothesis: "The finer-rank loss is dilution: most genera lack part of the photosystem II gene repertoire, so pooling them blurs the signal. Restricted to genera carrying the full repertoire, the photic-aquatic enrichment should reappear at genus and family rank."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Annotations, taxonomy and habitat labels appear in the catalog; per-genus repertoire tables and rank-wise comparisons must be computed."
databases: ["kbase.ke_pangenome", "kescience.mgnify"]
tables: ["kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.ncbi_env", "kescience.mgnify.genome"]
findings: ["gene_function_ecological_agora--4ca87c61"]
conflicts: ["conflict--taxonomic-resolution-dependent-functional-inference--d921d3c1"]
papers: ["30411862", "32556852", "37232518"]
builds_on: ["findings/gene_function_ecological_agora--4ca87c61", "conflicts/conflict--taxonomic-resolution-dependent-functional-inference--d921d3c1"]
projects: ["enigma_contamination_functional_potential", "enigma_sso_asv_ecology", "gene_function_ecological_agora"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does photosystem II exchange signal vanish at finer ranks through dilution by gene-poor genera?

Why is photosystem II gene exchange between photic-aquatic habitats and other lineages detectable at class rank in Cyanobacteria but not at genus rank, and does the answer depend on how many genera carry the full gene set?

## Hypothesis

The finer-rank loss is dilution: most genera lack part of the photosystem II gene repertoire, so pooling them blurs the signal. Restricted to genera carrying the full repertoire, the photic-aquatic enrichment should reappear at genus and family rank.

## Why it matters

It would show whether rank-dependent verdicts about gene flow are a real feature of evolution or a bookkeeping effect, and so which taxonomic rank should be used for such questions.

## How to test it

For Cyanobacteria genomes, tabulate presence of photosystem II genes per genus from genome annotations, split genera into full-repertoire and partial-repertoire groups, and compare photic-aquatic isolation-source enrichment within each group at genus, family, order and class rank. Add environmental biome labels from the metagenome-genome collection as an independent habitat source.

## What would support or refute it

Support: enrichment is clear in full-repertoire genera at finer ranks and absent in partial-repertoire ones. Refutation: enrichment stays absent at finer ranks even among full-repertoire genera, which would make the class-rank signal a coarse-grouping effect.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Annotations, taxonomy and habitat labels appear in the catalog; per-genus repertoire tables and rank-wise comparisons must be computed.

## Builds on

- Finding: [[findings/gene_function_ecological_agora--4ca87c61|Photosystem II innovation is exchange-type, but only at Cyanobacteriia class rank]] (Candidate novel)
- Conflict: [[conflicts/conflict--taxonomic-resolution-dependent-functional-inference--d921d3c1|Which Taxonomic Rank Reveals Functional Signal: Coarse Ranks Versus Fine Resolution]]

## Closest published work

- [PMID 30411862](https://pubmed.ncbi.nlm.nih.gov/30411862/) Early Archean origin of Photosystem II.
- [PMID 32556852](https://pubmed.ncbi.nlm.nih.gov/32556852/) The diversity and distribution of D1 proteins in cyanobacteria.
- [PMID 37232518](https://pubmed.ncbi.nlm.nih.gov/37232518/) Empirical Evidence That Complexity Limits Horizontal Gene Transfer.

PMID 30411862 dates the origin of photosystem II and PMID 32556852 maps D1 protein diversity in cyanobacteria, but neither tests whether the rank at which exchange appears depends on repertoire completeness.
