<!-- tension-hash: 4b4aa6edd14a0749 -->
# Does COG-Level Functional Structure Hold Up or Wash Out Across Analyses?

The COG comparison reports consistent functional partitioning between core and novel genes, while the ENIGMA community analysis does not detect a robust contamination-associated shift in coarse COG proxies at genus resolution. Here COG means Clusters of Orthologous Groups, a scheme that sorts genes into broad functional categories. [src: cog_analysis] [src: enigma_contamination_functional_potential] The disagreement matters for [[concepts/taxonomic-resolution-dependent-functional-inference]] because it bears on a practical question: is coarse COG-category structure a dependable signal in general, or only under certain analytical framings? The TENSION text itself says this is not a direct contradiction, because the two studies test different signals. [src: cog_analysis] [src: enigma_contamination_functional_potential] This page records both sides without choosing between them.

## Evidence Sides

**Side A: consistent functional partitioning by gene novelty**
The COG comparison found consistent core-versus-novel functional partitioning across 32 species. [src: cog_analysis] The signal tested is broad evolutionary partitioning by gene novelty. [src: cog_analysis]

**Side B: no robust contamination-associated shift at genus resolution**
The ENIGMA analysis did not find a robust contamination-associated shift in coarse COG proxies at genus resolution. [src: enigma_contamination_functional_potential] The signal tested is a site-level ecological association. It is measured after taxonomic bridging, meaning community taxa are linked to pangenome clades. [src: enigma_contamination_functional_potential] This is a null result for that association. It is not evidence that no shift exists.

## Possible Reconciliations

- **Hypothesis: different signals.** Partitioning by gene novelty within genomes and association with site contamination across communities may be independent properties. If so, finding one does not predict finding the other. [src: cog_analysis] [src: enigma_contamination_functional_potential]
- **Hypothesis: resolution and bridging attenuate the signal.** Aggregation determines how community taxa are bridged to clades and how much abundance is retained for functional scoring, so community-level results may reflect representation rather than biological shifts. [src: enigma_contamination_functional_potential] Whether this explains the null result is untested here.
- **Hypothesis: functional redundancy.** Contamination might change which taxa are present while aggregated COG summaries stay stable, because different taxa supply overlapping functions. The ENIGMA data do not directly demonstrate this. [src: enigma_contamination_functional_potential]

## Resolving Work

- **Novelty partitioning inside ENIGMA communities:** Apply the core-versus-novel COG partitioning to genomes bridged from ENIGMA communities. This asks whether the Side A pattern is present in the very taxa where Side B found no site-level shift.
- **Contamination test at finer resolution:** Rerun the contamination association at finer-than-genus taxonomic resolution, using coverage-aware models (models that account for mapped coverage, the fraction of community abundance linked to the functional features). This asks whether the genus-resolution null depends on the chosen resolution and its mapped coverage.
- **Accessory-fraction scores:** Stratify ENIGMA functional scores into core-derived and novel-derived COG fractions, then test each against contamination. This asks whether a shift is confined to novel-gene categories that whole-genome proxies would mask.
- **Redundancy test:** Test, across ENIGMA sites, whether community membership varies with contamination and whether aggregated COG profiles do. This asks whether functional redundancy could explain the absence of a robust shift in COG proxies.
