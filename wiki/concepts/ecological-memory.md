---
type: Concept
description: Prior exposure preserves community differences after environmental conditions
  change.
sources:
- id: lignin_community_enrichment
  resource: ../summaries/lignin_community_enrichment__REPORT.md
  title: lignin community enrichment
title: Ecological memory preserves community differences across changing environments
---
# Ecological memory preserves community differences across changing environments

Ecological memory is the persistence of community-composition differences caused by prior environmental exposure after communities encounter the same current conditions. The lignin-enrichment experiment provides a quantitative bacterial example: Round-1 carbon history explained more Round-2 community variation than the current Round-2 carbon source, and communities with different histories did not converge under identical conditions. [^lignin_community_enrichment]

## Core Evidence

The study analyzed 21 samples across 7 groups, with 3 replicates per group, using bacterial 16S V3–V4 and fungal ITS2 amplicon data, 97% OTU clustering, Bray–Curtis distances, PCoA, and PERMANOVA, a permutation-based test of community-composition differences. [^lignin_community_enrichment] The Round-2 factorial PERMANOVA included 12 samples and found that Round-1 history explained 58.9% of community variance (F=14.31, R²=0.589, p=0.002), whereas the current Round-2 carbon source explained 32.7% (F=4.85, R²=0.327, p=0.018). [^lignin_community_enrichment]

The history effect was also reflected in the relative distance structure: history/Round-2 distance ratios were 1.15 for Round-2 lignin and 1.59 for Round-2 lignin plus labile carbon, indicating stronger historical than current-condition effects in these comparisons. [^lignin_community_enrichment] Under identical Round-2 conditions, the mean Bray–Curtis distance was 0.507 for L-L versus LC-L and 0.486 for L-LC versus LC-LC, compared with 0.441 for L-L versus L-LC and 0.306 for LC-L versus LC-LC. [^lignin_community_enrichment] The reported memory index was ~0.50, meaning that communities with different histories retained approximately half of the maximum possible divergence under the same current condition. [^lignin_community_enrichment]

Taxonomic composition showed the same historical structuring. Lignin-history groups L-L and L-LC were Pseudomonas-dominated at 52–53%, whereas lignin-plus-labile-history groups LC-L and LC-LC were Acinetobacter-dominant at 31–34%, with Pseudomonas at 24–26% and Enterobacter at 2.7–18.1%. [^lignin_community_enrichment] OTU retention was 81% from L to L-L and 91% from LC to LC-LC, indicating that core taxa were maintained across the passage series. [^lignin_community_enrichment]

## Interpretation

These results support the interpretation that an initial carbon regime can alter which taxa persist or become dominant, thereby constraining later community responses when the environment changes. [^lignin_community_enrichment] The stronger effect of Round-1 history than of current carbon source supports [condition-specific-fitness](condition-specific-fitness.md), because the observed legacy depended on the earlier selective regime as well as on the present one. [^lignin_community_enrichment]

The initial enrichment created a strong ecological filter: lignin-only treatment increased Pseudomonas to 39.3% and Acinetobacter to 25.2%, while Shannon diversity declined from 6.46 to 3.16 and observed OTUs declined from 1,594 to 163. [^lignin_community_enrichment] Adding labile carbon instead increased Acinetobacter to 41.7% and Aeromonas to 20.2%, while Pseudomonas decreased to 23.0%, showing that the first carbon regime established distinct starting states for subsequent passage. [^lignin_community_enrichment]

The bacterial memory result is stronger than the fungal result in this experiment. [^lignin_community_enrichment] Fungal Round-2 history was not statistically detectable (R²=0.142, p=0.090), while fungal within-group Bray–Curtis distances reached 0.99–1.00 for several Round-2 groups compared with 0.09 for 16S. [^lignin_community_enrichment] The fungal evidence is therefore preliminary and does not establish a comparable fungal memory effect. [^lignin_community_enrichment] This marker-specific contrast motivates integration with [multi-omics-integration](multi-omics-integration.md), while the bacterial result provides a tractable target for linking persistent community composition to gene content through [pangenome-integration](pangenome-integration.md). [^lignin_community_enrichment]

## Scope and Limitations

The bacterial history effect was detected in a design with n=3 per group, while the Round-2 factorial analysis used n=12; the smaller per-group replication limits pairwise inference even though the factorial history effect was significant. [^lignin_community_enrichment] Pairwise Mann–Whitney U tests had a minimum achievable p-value of 0.10 because there were only 10 possible permutations for 3-versus-3 comparisons, and pairwise PERMANOVA had a permutation floor of approximately p~0.10. [^lignin_community_enrichment]

PERMDISP, a test of differences in within-group dispersion, was significant for 16S (p=0.0004) and ITS (p=0.0001), so the PERMANOVA signals reflect both differences in group location and differences in dispersion. [^lignin_community_enrichment] The experiment used 97% vsearch OTUs rather than amplicon sequence variants, so closely related organisms may have been merged. [^lignin_community_enrichment] The reported memory effect is consequently a strong bacterial community-composition result, but its taxonomic and mechanistic basis requires further testing. [^lignin_community_enrichment]

## Open Directions

- Increase replication to n>=5 per group and repeat the Round-1/Round-2 factorial design to test whether the history effect and the ~0.50 memory index remain stable. [^lignin_community_enrichment]
- Use DADA2 amplicon sequence variants, phylogenetic diversity, and UniFrac distances on the existing 16S data to determine whether ecological memory persists beyond 97% OTU definitions. [^lignin_community_enrichment]
- Cross-reference persistent Pseudomonas, Acinetobacter, and Comamonas lineages with [kbase_ke_pangenome](../entities/kbase-ke-pangenome.md) and test whether retained gene-content differences explain the L-versus-LC legacy. [^lignin_community_enrichment]
- Infer or measure beta-ketoadipate and protocatechuate pathway content in the retained bacterial taxa to test whether functional lignin-associated capacity predicts persistence across passages. [^lignin_community_enrichment]
- Add intermediate passage time points and fit community trajectories to distinguish rapid restructuring from gradual historical persistence. [^lignin_community_enrichment]
- Increase ITS sequencing depth, use UNITE-based taxonomy, and repeat the history experiment to test whether the absent fungal memory signal reflects biology or poor replicate structure. [^lignin_community_enrichment]

## Related Evidence

- [lignin_community_enrichment__REPORT](../summaries/lignin_community_enrichment__REPORT.md) — source summary for the bacterial history effect, taxonomic persistence, fungal contrast, and study limitations. [^lignin_community_enrichment]
- [condition-specific-fitness](condition-specific-fitness.md) — connects historical community divergence to selection under distinct carbon regimes. [^lignin_community_enrichment]
- [multi-omics-integration](multi-omics-integration.md) — frames the incomplete bacterial–fungal concordance analysis and its marker-specific limitations. [^lignin_community_enrichment]
- [pangenome-integration](pangenome-integration.md) — provides the proposed route for testing whether persistent community members carry distinct pathway content. [^lignin_community_enrichment]

[^lignin_community_enrichment]: [lignin community enrichment](../summaries/lignin_community_enrichment__REPORT.md)
