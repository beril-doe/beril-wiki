<!-- tension-hash: 874d5ba826e65347 -->
# Coverage of the Dark-Gene Candidate List: Taxonomic Skew Versus Pangenome-Linkage Gap

Two projects that both mine the Fitness Browser — a public collection of genome-wide bacterial mutant fitness data — for "dark" genes (protein-coding genes with no functional annotation) disagree about where the resulting candidate lists are incomplete, and therefore about what fixing them would require. One locates the gap in *taxonomy*: the organisms sampled are narrow, so candidates over-represent a single phylum. The other locates the gap in *linkage*: a large block of dark genes could not be connected to pangenome context (the set of gene families shared or variable across genomes of related strains) and so was never assessed at all. The distinction matters because the first gap is closed by adding organisms, the second by extending the annotation pipeline to genes already in hand. This tension is recorded on [[concepts/cofitness-network-architecture]].

## Evidence Sides

**Taxonomic coverage is the limiting gap.** The functional-dark-matter analysis found 57,011 dark genes, but the Fitness Browser contained 37/48 Pseudomonadota (the phylum containing most classical Gram-negative model bacteria) and no Archaea, Actinobacteria, or Epsilonproteobacteria among the top 500 candidates. [src: functional_dark_matter] On this reading the candidate list is a census of one lineage's unknowns, and whole domains and phyla are absent by construction rather than by any measured shortfall in their dark-gene content.

**Pangenome linkage is the limiting gap.** The truly-dark analysis adds a 17,479-gene pangenome-linkage gap and estimates approximately 2,841 additional truly dark genes among them at the 16.3% linked rate; this is an estimate, not an observed count. [src: truly_dark_genes] On this reading the missing candidates are already inside the same organism set — unassessed, not unsampled — and the 2,841 figure is an inference from the rate observed on linked genes, so it carries no direct observation of those genes' status.

## Possible Reconciliations

- *Hypothesis: the two gaps are orthogonal and additive.* Taxonomic skew would bias which lineages contribute candidates, while the linkage gap would deplete the list within every lineage present; neither claim then constrains the other, and both corrections are needed. Neither project measures the other's quantity, so this remains untested.
- *Hypothesis: the linkage gap is itself taxonomically structured.* If pangenome links are preferentially available for the well-sampled Pseudomonadota, the 17,479 unlinked genes [src: truly_dark_genes] would be enriched in exactly the under-represented groups [src: functional_dark_matter], making the two gaps one gap seen from two directions.
- *Hypothesis: the disagreement is about denominators, not biology.* One side counts organisms and top-ranked candidates, the other counts genes and an estimated rate; the claims may be jointly true and simply not comparable as stated.

## Resolving Work

- Cross-tabulate the 17,479 unlinked dark genes by source organism and phylum [src: truly_dark_genes] against the 37/48 Pseudomonadota composition [src: functional_dark_matter] — is the linkage gap concentrated in the under-sampled groups?
- Reannotate the 17,479 unlinked genes directly rather than by rate extrapolation, converting the estimated ~2,841 into an observed count [src: truly_dark_genes].
- Recompute the top 500 candidate ranking after adding any Archaeal, Actinobacterial, or Epsilonproteobacterial fitness datasets [src: functional_dark_matter] — does phylum representation shift?
- Test whether the 16.3% linked truly-dark rate [src: truly_dark_genes] is stable across phyla, since a lineage-dependent rate invalidates a single-rate extrapolation.
