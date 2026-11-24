---
type: "Dataset"
description: "NMDC-rehosted NEON soil, surface-water and benthic-sediment metagenome studies, including the dominant 1,186-run soil study and its MAGs."
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md", "summaries/nmdc_context_audit__REPORT.md"]
aliases: ["NEON", "NEON metagenomes", "NEON soil metagenome study", "NMDC NEON cohort"]
---
# NMDC NEON metagenome studies

NMDC NEON metagenome studies are the soil, surface-water and benthic-sediment metagenome studies from the National Ecological Observatory Network (NEON) that NMDC rehosts. Evidence comes from three projects: a batch-controlled analysis of the dominant soil study, a MAG-focused analysis of all three studies, and a context audit that separates NEON from NMDC. The within-study eukaryote finding is demonstrated for one soil study only, and the cross-study generalization test is under-powered. [src: euk_in_prok_correlates]

## Key facts

- The NEON analysis uses three NMDC-rehosted studies: soil nmdc:sty-11-34xj1150 (n=6,489), surface water nmdc:sty-11-hht5sb92 (n=234) and benthic sediment nmdc:sty-11-pzmd0x14 (n=736). [src: neon_mag_functional_discovery]
- Together they contain 7,298 metagenome assembled genomes (MAGs), of which 1,609 pass MQ+HQ quality. [src: neon_mag_functional_discovery]
- Of those 1,609 MAGs, only 40 are archaeal, all from soil, including 4 HQ MAGs. [src: neon_mag_functional_discovery]
- 14 of the 1,609 are credibly eukaryotic, under the criterion eukaryotic_evaluation_completeness ≥ 50%. [src: neon_mag_functional_discovery]
- The cohort is bacterial and archaeal metagenomes only. No metatranscriptomic, metaproteomic, metabolomic, lipidomic or NOM data are associated with the three studies, so multi-omics framing is not feasible. [src: neon_mag_functional_discovery]

## Naming: NEON is not NMDC

NEON is the NSF (National Science Foundation) National Ecological Observatory Network. Its agency and sampling design differ from NMDC's. [src: nmdc_context_audit] The audit classes kbase.nmdc_neon as a namesake collision that belongs to NEON (NSF), not NMDC. [src: nmdc_context_audit] It warns that the acronym collision would corrupt agency attribution. [src: nmdc_context_audit] The audit lists the table as last committed 2026-07-02 and fresh. [src: nmdc_context_audit] It characterizes the namesake with the tables neon_mag_catalog, sample_data and study_sample. [src: nmdc_context_audit] See [[concepts/provenance-overloading-of-dataset-labels-in-the-data-lakehouse]].

## The dominant soil study and eukaryotic fraction

The batch-controlled analysis restricts to one dominant NEON soil metagenome study. It has 1,186 runs, one sampling program and a constant protocol and batch. [src: euk_in_prok_correlates] Within it, eukaryotic fraction varies with local vegetation (env_local_scale, 11 levels; Kruskal H=119.1, p=7.6×10⁻²¹). [src: euk_in_prok_correlates] It also varies across 47 sites (Kruskal H=310.4, p=2.4×10⁻⁴⁶). [src: euk_in_prok_correlates]

Fractions are highest at Arctic tundra sites: Utqiaġvik 30%, Caribou-Poker Creeks 22% and Toolik 17%. Temperate forests sit at 2–8%. [src: euk_in_prok_correlates]

Local environment plus geography predict eukaryotic fraction within the study, with 5-fold R² = +0.17 ± 0.06. This contrasts with the cross-study out-of-study R² = −0.30. [src: euk_in_prok_correlates] See [[concepts/within-study-environmental-drivers-of-eukaryotic-dna-in-soil-metagenomes]].

## Caveats

- Sampling depth is not measured in this soil study (zero non-null depth values). The report's depth association is therefore cross-study and not part of the batch-controlled result. [src: euk_in_prok_correlates]
- NMDC read-based taxonomy spans only about 9 studies, and one soil study contributes about 43% of runs. The cross-study generalization test is under-powered. The within-study result is shown for one soil study only and may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

## Data tables used

The MAG analysis drew on nmdc metadata tables for study, biosample, MAG, workflow, and per-workflow KO (KEGG ortholog), COG (clusters of orthologous groups) and Pfam data. [src: neon_mag_functional_discovery]

## Related

[[entities/nmdc-integrated-collections]], [[summaries/euk_in_prok_correlates__REPORT]], [[summaries/neon_mag_functional_discovery__REPORT]], [[summaries/nmdc_context_audit__REPORT]].
