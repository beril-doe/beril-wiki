---
type: "Dataset"
description: "refdata collections of SPIRE and JGI GEM MAGs and IMG/VR and MetaVR viral sequences."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/ibd_phage_targeting__REPORT.md"]
aliases: ["GEM-MAGs", "IMG-VR", "IMG/VR", "MetaVR", "SPIRE", "refdata"]
---
# Reference MAG and viral collections

Reference MAG and viral collections (refdata) hold SPIRE and JGI GEM metagenome assembled genomes (MAGs), and IMG/VR and MetaVR viral sequences. [src: berdl_data_atlas] The phage-targeting report treats IMG/VR as an unused external resource. [src: ibd_phage_targeting] See [[summaries/berdl_data_atlas__REPORT]] and [[summaries/ibd_phage_targeting__REPORT]].

## Key facts

The collections `refdata_jgi_gem_mags`, `refdata_spire` and `refdata_jgi_virus` supply reference MAGs and viral sequence catalogs through the tables `genome_metadata`, `imgvr_sequence_info` and `metavr_main`. [src: berdl_data_atlas]

- SPIRE MAGs: 1,158,553 in refdata. [src: berdl_data_atlas]
- JGI GEM-MAGs: 52,515 in refdata. [src: berdl_data_atlas]
- MetaVR viral sequence records: 24,435,662. [src: berdl_data_atlas]
- IMG/VR viral sequence records: 15,677,623. [src: berdl_data_atlas]

For platform-wide depth by entity class, see [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]].

## Use in phage-targeting work

The ibd_phage_targeting report describes IMG/VR as containing ~3M UViGs. It says IMG/VR covers gut-anaerobe phage-discovery space that the platform's internal `ref_phage_biology` literature curation does not. [src: ibd_phage_targeting] That report names INPHARED and IMG/VR external database queries as the highest-priority phage-targetability follow-up. [src: ibd_phage_targeting] It also excludes them from its scope, which was limited to the platform's internal data, even though it calls them the highest-priority external-data extension before clinical translation. [src: ibd_phage_targeting]

HMP2 viromics has no CRISPR-spacer-derived phage-host predictions. Phage discovery for Tier-A hosts would need an IMG/VR cross-reference. [src: ibd_phage_targeting] See [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]].

The two reports give different IMG/VR figures: ~3M UViGs in the phage-targeting report and 15,677,623 records in the atlas report. Neither claim states how they relate, so each stands on its own. [src: ibd_phage_targeting, berdl_data_atlas]
