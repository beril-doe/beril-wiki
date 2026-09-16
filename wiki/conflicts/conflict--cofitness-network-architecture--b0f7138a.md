<!-- tension-hash: b0f7138a36d17bb8 -->
# Do Dark-Gene Co-fitness Results Extend to Essential Genes and Under-sampled Lineages?

This page records a tension from [[concepts/cofitness-network-architecture]]: the functional-dark-matter work presents co-fitness as a route to function for genes of unknown function, but its own coverage and scope statements limit where that route applies. Co-fitness means correlated fitness profiles across conditions in RB-TnSeq (random barcode transposon sequencing) experiments. The disagreement matters because it decides whether co-fitness evidence can be used for essential dark genes and for lineages outside the Fitness Browser's taxonomic sample. 57,011 dark genes were found [src: functional_dark_matter], but 32,075 co-fitness-tested pairs are described in two incompatible ways [src: functional_dark_matter].

## Evidence Sides

**Side 1: co-fitness as a broad inference route, including essential genes**

The functional-dark-matter analysis found 57,011 dark genes [src: functional_dark_matter]. One section of that report describes its 32,075 co-fitness-tested pairs as providing the strongest functional inference for essential genes that lack direct fitness data [src: functional_dark_matter].

**Side 2: co-fitness restricted in scope and in coverage**

Finding 12 of the same report specifies the 32,075 pairs as non-essential operon pairs (an operon being a set of adjacent genes transcribed as one unit) and states that co-fitness is unavailable for essential genes [src: functional_dark_matter]. The tested-pair scope and the claimed applicability therefore conflict [src: functional_dark_matter].

Coverage is also skewed. The Fitness Browser contained 37/48 Pseudomonadota and no Archaea, Actinobacteria, or Epsilonproteobacteria among the top 500 candidates [src: functional_dark_matter].

The truly-dark analysis adds a 17,479-gene pangenome-linkage gap. A pangenome is the full gene set across genomes of a species. The analysis estimates approximately 2,841 additional truly dark genes among those 17,479 at the 16.3% linked rate. This is an estimate, not an observed count [src: truly_dark_genes].

## Possible Reconciliations

- **Hypothesis A:** "strongest functional inference for essential genes" may refer to operon-neighbour inference, with co-fitness of non-essential partners used only as indirect support. If so, the Finding 12 scope is correct and the other section overstates applicability. Neither reading is established by the TENSION text.
- **Hypothesis B:** the coverage skew may reflect only which organisms the Fitness Browser sampled, not where dark-gene biology is concentrated. Under this hypothesis, conclusions would remain untested outside Pseudomonadota, and their validity within Pseudomonadota would still need its own test.
- **Hypothesis C:** the 16.3% linked rate may or may not transfer to the 17,479 unlinked genes. Until those genes are assessed, the approximately 2,841 figure remains an estimate, not an observed count [src: truly_dark_genes].

## Resolving Work

- **Pair-level audit:** take the 32,075 tested pairs from the functional-dark-matter outputs, join each member to essentiality calls, and ask whether any pair contains an essential gene. This would establish the tested-pair scope, though not whether indirect inference reaches essential genes.
- **Unlinked-gene reannotation:** reannotate the 17,479 unlinked dark genes directly, without a pangenome link. Ask whether the observed truly dark count matches the approximately 2,841 estimate.
- **Eligible-pool audit:** tabulate, by phylum, the full dark-gene pool and organism coverage from which the top 500 candidates were drawn. Ask whether the 37/48 Pseudomonadota share tracks the sampled organism composition or the ranking criteria.
- **Gap-filling lineages:** add fitness data for Archaea, Actinobacteria, or Epsilonproteobacteria. Then test whether co-fitness partners of dark genes behave as they do in Pseudomonadota.
