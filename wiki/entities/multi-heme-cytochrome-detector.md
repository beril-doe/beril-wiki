---
type: "Method"
description: "Triple-signal detection of multi-heme cytochromes (PFAM PF02085, PF22678 and CXXCH motif counting) used as an iron-reduction marker."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
aliases: ["CXXCH motif counting", "Multi-heme cytochrome iron-reduction detector", "multi-heme cytochrome triple-signal detector", "triple-signal multi-heme cytochrome detection"]
---
# Multi-heme cytochrome detector

The multi-heme cytochrome detector is a triple-signal method that combines two PFAM families with a CXXCH motif count to flag multi-heme cytochrome iron-reduction (IR) potential. [src: bacillota_b_subsurface_accessory] It was used to correct the clay project's IR analysis, where it changed the per-cohort IR rates substantially. [src: discoveries]

## Key facts

- **Background.** KEGG has no canonical KO (KEGG ortholog) for the Geobacter omcS or Shewanella mtr operon multi-heme outer-surface cytochromes. The clay project's original analysis unknowingly substituted unrelated genes. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
- **Signal 1.** PFAM PF02085 (Cytochrom_CIII, multi-heme c-type). [src: bacillota_b_subsurface_accessory]
- **Signal 2.** PFAM PF22678 (Cytochrom_c_NrfB-like, multi-heme nitrite reductase). [src: bacillota_b_subsurface_accessory]
- **Signal 3.** A CXXCH heme-binding motif count of at least 4 in `gene_cluster.faa_sequence`. The report calls this a canonical method since Methé et al. 2003 on Geobacter. [src: bacillota_b_subsurface_accessory]
- **Decision rule.** A genome scores positive if any of the three signals is present. [src: bacillota_b_subsurface_accessory]

## Contribution of each signal

The PFAMs are sparse in Bacillota_B, with only about 6 clusters across all four PFAMs examined. The CXXCH motif counting therefore carried most of the IR signal in the NB06 notebook. This is why the corrected IR rates (40–56%) are far higher than PFAM-only detection would give. [src: bacillota_b_subsurface_accessory]

## Effect on clay cohort rates

The corrected detector raised the rate for anchor_deep and soil_baseline and lowered it for anchor_shallow. [src: clay_confined_subsurface]

| Cohort | n | Original marker | Corrected detector |
|---|---|---|---|
| anchor_deep | 9 | 11.1% | 55.6% [src: clay_confined_subsurface] |
| anchor_shallow | 30 | 50.0% | 40.0% [src: clay_confined_subsurface] |
| soil_baseline | 149 | 20.1% | 40.9% [src: clay_confined_subsurface] |

The discoveries digest gives the same results rounded: anchor_deep 56% (was 11%), anchor_shallow 40% (was 50%), soil_baseline 41% (was 20%). [src: discoveries] The clay project's corrected analysis uses the same three signals. [src: clay_confined_subsurface]

## Proposed reuse

The bacillota_b_subsurface_accessory report proposes this triple-signal pattern as a reusable KBase Data Lakehouse method for cases where KEGG KO assignment is unreliable. [src: bacillota_b_subsurface_accessory] The report says it applies across the pangenome whenever iron-reduction or extracellular-electron-transfer questions arise. [src: bacillota_b_subsurface_accessory] This is a proposal from one re-analysis.

## Related pages

See [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction]], [[concepts/iron-and-sulfate-reduction-signatures-in-clay-subsurface-porewater-versus-rock-attached-communities]], [[summaries/bacillota_b_subsurface_accessory__REPORT]] and [[summaries/clay_confined_subsurface__REPORT]].
