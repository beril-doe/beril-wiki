<!-- tension-hash: d921d3c1b9c46a6d -->
# Which Taxonomic Rank Reveals Functional Signal: Coarse Ranks Versus Fine Resolution

Projects that test genotype-to-function links at more than one taxonomic rank (the hierarchy levels species, genus, family, order and class) disagree on which rank is informative. A multi-rank analysis found a photosynthesis effect present only at a coarse rank and a mycolic-acid effect attenuated at family rank relative to a sub-clade restriction [src: gene_function_ecological_agora, discoveries]. Community-ecology analyses instead frame genus-level aggregation as potentially masking finer-scale effects [src: enigma_contamination_functional_potential, enigma_sso_asv_ecology]. This matters for [[concepts/taxonomic-resolution-dependent-functional-inference]], because aggregation controls which genotype-to-function relationships can be detected [src: enigma_contamination_functional_potential]. If the informative rank depends on the trait or the dataset, no single default aggregation level can be assumed.

## Evidence Sides

**Side A: signal can appear only at a coarse rank, or weaken at an intermediate one.**
In the multi-rank atlas analysis, the photosystem II (PSII, the water-oxidizing complex of oxygenic photosynthesis) effect was absent at genus, family and order rank and present only at class rank [src: gene_function_ecological_agora, discoveries]. The project attributed this to dilution: pooling genera that lack the full paralog repertoire (the set of duplicated gene copies) blurs the signal at intermediate ranks [src: gene_function_ecological_agora, discoveries]. The mycolic-acid (long-chain cell-envelope lipid) effect at family rank was attenuated relative to a sub-clade restriction [src: gene_function_ecological_agora, discoveries]. The project report itself states that the PSII rank-gradient requires a clearer explanation [src: gene_function_ecological_agora]. The dilution account is therefore the authors' interpretation, not an established mechanism.

**Side B: genus-level aggregation may mask finer-scale effects.**
The enigma_contamination_functional_potential and enigma_sso_asv_ecology projects both frame genus-level aggregation as potentially masking finer-scale effects [src: enigma_contamination_functional_potential, enigma_sso_asv_ecology]. This is framed as a potential effect, not as a measured loss of signal [src: enigma_contamination_functional_potential, enigma_sso_asv_ecology].

These positions should not be averaged into a single preferred rank [src: gene_function_ecological_agora].

## Possible Reconciliations

- **Hypothesis 1: trait-specific informative rank.** Each function may have its own informative rank, set by how its gene repertoire is distributed across the tree. Under this view the PSII class-rank result and the genus-masking concern need not conflict, because they concern different traits.
- **Hypothesis 2: data-type dependence.** Tree-scale pangenome analyses (a pangenome being the full gene set across a clade's genomes) and community-abundance analyses may suffer from different aggregation artifacts. In community data, aggregation determines how community taxa are bridged to pangenome clades [src: enigma_contamination_functional_potential]. In tree-scale data, pooling genera that lack the full paralog repertoire was proposed to dilute signal [src: gene_function_ecological_agora, discoveries].
- **Hypothesis 3: non-monotonic signal.** Signal may not change steadily with rank. It could be diluted at intermediate ranks and recovered at a broader rank, which would make "finer is better" and "coarser is better" both incomplete.

## Resolving Work

- Use the per-(rank × clade × KO) species-with-KO fractions (KO: KEGG Orthology gene-function group) from the agora leaf-consistency analysis to test whether paralog-repertoire completeness explains where the PSII effect appears and disappears across genus, family, order and class.
- Re-run the ENIGMA contamination models at ranks above and below genus to test whether genus aggregation actually masks associations, or only reduces mapped coverage (the fraction of community abundance linked to the functional-feature construction).
- Analyse the enigma_sso_asv_ecology community data at amplicon-sequence-variant (ASV, exact-sequence taxon) resolution versus genus aggregation to test whether finer resolution reveals functional gradients that genus pooling hides.
- Repeat the mycolic-acid test across sub-clade, family and order levels to test whether attenuation follows the dilution pattern proposed for PSII.
