---
type: "Dataset"
description: "Per-gene KO call table in the KBase Data Lakehouse covering only 57% of NEON workflows, with habitat-biased coverage."
sources: ["summaries/neon_mag_functional_discovery__REPORT.md", "summaries/pitfalls.md"]
aliases: ["annotation_kegg_orthology"]
---
# nmdc_results.annotation_kegg_orthology

`nmdc_results.annotation_kegg_orthology` (also called annotation_kegg_orthology) is a per-gene table of KEGG ortholog (KO) calls in the KBase Data Lakehouse. In the NEON data it covers only 57% of workflows, and the missing workflows are concentrated in particular habitats and genera. [src: neon_mag_functional_discovery, pitfalls] Treat it as a biased source for per-gene analysis. The evidence comes from one project's re-analysis, repeated in the central pitfalls digest. See [[summaries/neon_mag_functional_discovery__REPORT]] and [[summaries/pitfalls]].

## Key facts

- The table holds 1.83 B rows. It does not cover every MetagenomeAnnotation workflow that has a row in `nmdc_metadata.functional_annotation_agg`. [src: pitfalls]
- Only 1,799 of 3,137 NEON MetagenomeAnnotation workflows (57%) have any rows in it. [src: neon_mag_functional_discovery, pitfalls]
- The neon_mag_functional_discovery report used its per-gene KO calls to build per-MAG (metagenome assembled genome) KO sets through the `members_id` join. [src: neon_mag_functional_discovery]
- `workflow_execution_set_mags_list.members_id` is an `array<string>` of contig IDs (identifiers) per MAG. The table's `gene_id` has the structure `<contig_id>_<start>_<end>`. [src: neon_mag_functional_discovery]
- Equi-joining on the extracted contig portion links per-gene KO calls to specific MAGs. This is the basis of the NB04b per-MAG re-analysis. [src: neon_mag_functional_discovery] See also [[concepts/join-key-validity-and-identifier-format-mismatches]].

## Habitat-biased coverage

The 43% gap is non-random. It correlates strongly with habitat and genus. [src: pitfalls] Coverage falls from aquatic to soil genera. It reaches 0% for novel soil genera. The NB04b survival counts below are the cohort outcomes the report lists beside each coverage figure. [src: neon_mag_functional_discovery]

| Cohort | Per-gene KO coverage | NB04b cohort outcome |
|---|---|---|
| Surface-water cyanobacteria (Planktothrix, Dolichospermum, Rubrivivax) | 100% | All 27 MAGs survived [src: neon_mag_functional_discovery, pitfalls] |
| Benthic generalists (Ferruginibacter, Flavobacterium, UBA953) | ~85% | 16 / 19 survived [src: neon_mag_functional_discovery, pitfalls] |
| Soil acidobacteria (Sulfotelmatobacter, Palsa-465, Palsa-1447) | ~30% | 12 / 40 survived [src: neon_mag_functional_discovery, pitfalls] |
| Soil cultured genera (Mycobacterium, Bradyrhizobium, Acidoferrum) | ~10% | 5 / 65 survived [src: neon_mag_functional_discovery, pitfalls] |
| Soil unculturable / novel (Acidocella, BOG-234, Pseudolabrys, Pseudonocardia, Reyranella) | 0% | 0 / 28 survived [src: neon_mag_functional_discovery, pitfalls] |

The per-MAG re-analysis was limited by this gap. [src: neon_mag_functional_discovery]

## Guidance and unknowns

- Prefer `functional_annotation_agg` in `nmdc_metadata` for sample-level or workflow-level KO, COG (clusters of orthologous groups) or Pfam analysis. It covers essentially every workflow that has any annotation output. [src: pitfalls]
- Use `functional_annotation_agg` for habitat-versus-chemistry analysis, PCoA (principal coordinates analysis) and PERMANOVA (permutational multivariate analysis of variance), where per-gene resolution is not needed. [src: pitfalls]
- Do not assume `pfam_annotation_gff` fills the gap left by this table. [src: pitfalls] That table has 2.68 B rows, and `annotation_enzyme_commission` has 1.23 B rows. Neither covers every workflow. [src: pitfalls]
- The report could not tell whether `pfam_annotation_gff` and `annotation_enzyme_commission` fill the soil-genera gap. Bounded SQL (structured query language) could not query their per-workflow coverage. [src: neon_mag_functional_discovery]
- Bounded queries for a single `workflow_run_id` time out at scan-only cost. The tables have 2–3 B rows, and `workflow_run_id` does not partition-prune cleanly. [src: pitfalls]

Related concepts: annotation and environmental metadata table gaps in the data lakehouse, [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].
