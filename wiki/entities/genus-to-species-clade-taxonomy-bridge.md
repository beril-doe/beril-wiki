---
type: "Method"
description: "Genus-normalized mapping from ENIGMA taxa to GTDB pangenome clades with strict, relaxed and species-proxy modes."
sources: ["summaries/discoveries.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/pitfalls.md"]
aliases: ["taxonomy bridge"]
---
# Genus-to-species-clade taxonomy bridge

This page covers the genus-normalized mapping from ENIGMA taxa to GTDB pangenome clades, with strict, relaxed and species-proxy modes. Genus-only taxonomy leaves many genera ambiguous [src: enigma_contamination_functional_potential], and the stricter species-proxy mode loses most mapped abundance. [src: discoveries, enigma_contamination_functional_potential] See [[summaries/enigma_contamination_functional_potential__REPORT]], [[summaries/discoveries]] and [[summaries/pitfalls]] for the source summaries.

## Key facts

- The ENIGMA table `enigma_coral.ddt_brick0000454` provides taxonomy only through Genus, with no species or strain rows. [src: discoveries, enigma_contamination_functional_potential]
- Species-level bridge testing is therefore not directly possible in this dataset slice. [src: enigma_contamination_functional_potential]
- NB02 built the genus-normalized bridge to pangenome clades. [src: enigma_contamination_functional_potential]
- Functional features were computed independently for strict, relaxed and species-proxy modes. [src: enigma_contamination_functional_potential]
- The report presents this as a reproducible ENIGMA-to-KBase Data Lakehouse workflow with mapped-coverage diagnostics and a species-proxy sensitivity mode. [src: enigma_contamination_functional_potential]

## Coverage and bridge size

Upstream diagnostics found 530 mapped genera and 862 unmapped genera. [src: enigma_contamination_functional_potential] The bridge table has 8,242 rows because genus-to-clade expansion is many-to-many. [src: enigma_contamination_functional_potential] The strict mode has 530 clades and the relaxed mode has 7,380 clades. [src: enigma_contamination_functional_potential] Functional features comprise 3,630 rows across the three modes: strict_single_clade, relaxed_all_clades and species_proxy_unique_genus. [src: enigma_contamination_functional_potential]

## Ambiguity

Of the 530 mapped genera, 380 are ambiguous multi-clade genera and 150 map to a unique clade. [src: enigma_contamination_functional_potential] The clade-count distribution has a long right tail, with a maximum of 433 clades per genus. [src: enigma_contamination_functional_potential] The most ambiguous genera, by clade count, are:

| Genus | Clades |
|---|---|
| pseudomonas | 433 [src: enigma_contamination_functional_potential] |
| streptomyces | 378 [src: enigma_contamination_functional_potential] |
| prevotella | 358 [src: enigma_contamination_functional_potential] |
| streptococcus | 214 [src: enigma_contamination_functional_potential] |
| mycobacterium | 186 [src: enigma_contamination_functional_potential] |

See also [[entities/pseudomonas]] and [[entities/streptomyces]].

## Species-proxy mode

Because ENIGMA taxonomy stops at genus, NB02 added `species_proxy_unique_genus` mode. It keeps only genera that map to exactly one GTDB species clade. [src: enigma_contamination_functional_potential] This retained 150 clades from unique genus-to-single-clade mappings. [src: discoveries, enigma_contamination_functional_potential]

The cost is large. Mean mapped abundance fraction was 0.031 in species-proxy mode and 0.343 in strict/relaxed modes. [src: discoveries, enigma_contamination_functional_potential] The ranges were 0.0002 to 0.543 for species-proxy and 0.031 to 0.854 for strict/relaxed. [src: enigma_contamination_functional_potential]

Within species-proxy mode, the site_defense_score trend was positive but not significant (rho = 0.169, [[entities/spearman-rank-correlation|Spearman]] p = 0.081). [src: enigma_contamination_functional_potential] No high-coverage subset test was feasible at mapped_abundance_fraction >= 0.25, because retained coverage was low. [src: enigma_contamination_functional_potential] The report suggests that, at current ENIGMA taxonomy granularity, stricter resolution sharply reduces analyzable signal without yet strengthening inference. [src: enigma_contamination_functional_potential]

## Pitfall

Attempting species-level bridge logic directly on genus-only taxonomy either fails or silently reuses genus-level mappings while appearing higher resolution. [src: pitfalls] The recommended response is to check the available taxonomy levels first. If species or strain labels are absent, use an explicit species-proxy mode and report the mapped-coverage loss. The other option is a data source with species or strain resolution, such as metagenomes or an ASV (amplicon sequence variant) reclassification pipeline. [src: pitfalls]

## Output tables

- `data/bridge_quality_summary.tsv` has 6 rows of mapped, unmapped and ambiguity summary metrics. [src: enigma_contamination_functional_potential]
- `data/bridge_clade_count_distribution.tsv` has 71 rows giving species-clade counts per mapped genus. [src: enigma_contamination_functional_potential]
- `data/bridge_top_ambiguous_genera.tsv` has 20 rows listing the most ambiguous mapped genera. [src: enigma_contamination_functional_potential]

## Related pages

[[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]], [[entities/enigma]], [[entities/gtdb]].
