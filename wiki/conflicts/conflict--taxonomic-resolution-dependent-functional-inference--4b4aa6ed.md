<!-- tension-hash: 4b4aa6edd14a0749 -->
# Tension: Pangenome-Wide COG Partitioning Is Consistent, Yet No Contamination-Associated COG Shift Appears at Genus Resolution

Two projects in this corpus apply Clusters of Orthologous Groups (COG) categories — a coarse scheme that bins genes into broad functional classes — and reach opposite-feeling results. A pangenome comparison reports consistent core-versus-novel functional partitioning across 32 species [src: cog_analysis], while a community analysis of contamination gradients reports no robust contamination-associated shift in coarse COG proxies at genus resolution [src: enigma_contamination_functional_potential]. The disagreement matters because taxonomic resolution controls which genotype-to-function relationships can be detected: aggregation determines both how community taxa are bridged to pangenome clades and how much abundance is retained for functional scoring [src: enigma_contamination_functional_potential]. Read together, the two results raise the question of whether a partitioning that is consistent within genomes should be expected to surface as a community-level association at all, or whether the scale and the bridging step decide what a COG summary can detect. This is the conflict abstracted from [[concepts/taxonomic-resolution-dependent-functional-inference]].

## Evidence Sides

**Side A — COG partitioning is consistent across pangenomes.** The COG comparison found consistent core-versus-novel functional partitioning across 32 species [src: cog_analysis]. The signal being tested is broad evolutionary partitioning by gene novelty: which functional categories concentrate in conserved core genes versus in newly acquired or singleton gene content [src: cog_analysis].

**Side B — no robust contamination-associated COG shift at genus resolution.** The ENIGMA analysis did not find a robust contamination-associated shift in coarse COG proxies at genus resolution [src: enigma_contamination_functional_potential]. This is a null result and is recorded as one: no direction of shift is claimed, and the finding is specific to genus-level resolution and to coarse COG proxies rather than to COG categories generally [src: enigma_contamination_functional_potential].

## Possible Reconciliations

- **Different-signal hypothesis.** The two results may not be a direct contradiction at all, because the studies test different signals: broad evolutionary partitioning by gene novelty versus a site-level ecological association after taxonomic bridging — the step that links observed community taxa to pangenome clades [src: cog_analysis] [src: enigma_contamination_functional_potential].
- **Representation hypothesis.** Mapped coverage — the fraction of community abundance linked to the functional-feature construction — can make community-level associations reflect representation rather than biological shifts; on this hypothesis the genus-resolution result tracks representation rather than biology [src: enigma_contamination_functional_potential].
- **Functional-redundancy hypothesis.** Environmental selection may change community membership while aggregated functional summaries remain stable, because different taxa supply overlapping functions; this is stated as a compatible hypothesis, and this dataset does not directly demonstrate redundancy [src: enigma_contamination_functional_potential].

## Resolving Work

- Re-run the contamination association at finer taxonomic resolution than genus, on the same community samples, asking whether the null at genus resolution survives when aggregation no longer collapses clade-level differences [src: enigma_contamination_functional_potential].
- Stratify the same community models by mapped coverage and test whether the null persists in the highest-coverage strata, separating representation effects from absence of a biological shift [src: enigma_contamination_functional_potential].
- Score community genes by core-versus-novel status rather than by coarse COG proxy alone, and test whether the pangenome-derived partitioning axis tracks contamination where the COG proxy does not [src: cog_analysis] [src: enigma_contamination_functional_potential].
- Check whether the species analyzed in the pangenome comparison are represented among the bridged community clades at all, to establish whether the two studies even share organisms before their results are compared [src: cog_analysis] [src: enigma_contamination_functional_potential].
- Test redundancy directly by asking whether taxon turnover along the gradient is accompanied by conserved category-level composition, which would convert the redundancy hypothesis into a measured claim [src: enigma_contamination_functional_potential].
