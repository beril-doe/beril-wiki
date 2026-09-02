---
type: "Dataset"
description: "National Ecological Observatory Network (NEON), a dataset distinct from NMDC."
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/nmdc_context_audit__REPORT.md"]
---
# National Ecological Observatory Network

## What this entity is

**Canonical name:** National Ecological Observatory Network (NEON). [src: euk_in_prok_correlates]

**Known alias:** NEON. [src: euk_in_prok_correlates]

**Stable external identifier:** Not reported in this document. [src: euk_in_prok_correlates]

NEON is the dominant soil metagenome study represented in the analysis of eukaryotic signal in NMDC prokaryote-targeted metagenomes. [src: euk_in_prok_correlates]

The NMDC context audit **refines** this usage distinction: `kbase.nmdc_neon` represents NEON, not the National Microbiome Data Collaborative (NMDC), making it a namesake collision rather than an NMDC resource. NEON is an NSF program, whereas NMDC is associated with DOE-BER. [src: nmdc_context_audit]

## Key facts from the document

The batch-controlled NEON analysis included 1,186 runs from one sampling program with a constant protocol and batch. [src: euk_in_prok_correlates]

Within NEON, local vegetation (`env_local_scale`, with 11 levels) was associated with eukaryotic fraction, with Kruskal–Wallis H=119.1 and p=7.6×10⁻²¹. [src: euk_in_prok_correlates]

Median eukaryotic fractions were 23% in sedge/forb herbaceous soil, 14% in emergent wetland, 13% in dwarf scrub, and 2% in evergreen forest, while deciduous forest, cropland, and pasture were approximately 0. [src: euk_in_prok_correlates]

Geography also differed across 47 NEON sites, with Kruskal–Wallis H=310.4 and p=2.4×10⁻⁴⁶. [src: euk_in_prok_correlates]

The highest median eukaryotic fractions occurred at Arctic tundra sites: Utqiaġvik had 30%, Caribou-Poker Creeks had 22%, and Toolik had 17%, compared with 2–8% in temperate forests. [src: euk_in_prok_correlates]

A model using local environment and geography achieved within-study five-fold R²=+0.17 ± 0.06 in NEON, contrasting with cross-study out-of-study R²=−0.30. [src: euk_in_prok_correlates]

The NEON result supports the interpretation that environmental metadata can predict eukaryotic signal when batch is held approximately constant, while remaining subject to possible sub-batch confounding within the study. [src: euk_in_prok_correlates]

NEON had zero non-null sequencing-depth values, so the reported negative association between measured sequencing depth and eukaryotic fraction was a cross-study statistic and was not part of the batch-controlled within-study result. [src: euk_in_prok_correlates]

The report cautions that `env_local_scale` and geography within NEON may track sub-batches such as sampling campaigns, making this analysis the best available control rather than a randomized design. [src: euk_in_prok_correlates]

The audit’s identification of `kbase.nmdc_neon` **supports** treating NEON provenance and authority separately from NMDC when selecting or attributing resources; its inferred risk of misattribution is a provenance hazard, not a directly observed user error. [src: nmdc_context_audit]

## Related pages

The NEON findings are summarized in [[summaries/euk_in_prok_correlates__REPORT]]. [src: euk_in_prok_correlates]

The resource-provenance distinction is summarized in [[summaries/nmdc_context_audit__REPORT]]. [src: nmdc_context_audit]

They contribute to [[concepts/environment-embedding-geography]], which addresses how environmental metadata and geography relate to biological signals. [src: euk_in_prok_correlates]

They also inform [[concepts/cross-tenant-data-bridging]], because the analysis connected NMDC workflow results with biosample and study metadata. [src: euk_in_prok_correlates]
