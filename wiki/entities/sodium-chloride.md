---
type: "Compound"
description: "Sodium chloride used as a stress comparator in metal-fitness analysis"
sources: ["summaries/counter_ion_effects__REPORT.md"]
---
# Sodium chloride

## Identity

Sodium chloride is the canonical name for the compound abbreviated **NaCl** in the report. [src: counter_ion_effects]

- **Known alias:** NaCl. [src: counter_ion_effects]
- **Stable external identifier:** No stable external identifier is reported in this document. [src: counter_ion_effects]

## Evidence from counter-ion analysis

The analysis included 71 NaCl experiments, 4,648 NaCl-important genes, and 25 organisms. [src: counter_ion_effects]

Across 19 organisms and 14 metals, 4,304 of 10,821 metal-important gene records, or 39.8%, were also NaCl-important. [src: counter_ion_effects]

After excluding the *Synechococcus elongatus* outlier, the overlap was 3,739 of 10,183 records, or 36.7%. [src: counter_ion_effects]

NaCl-important genes overlapped with metal-important genes for every metal, with overlap ranging from 9.2% for molybdenum to 57.6% for manganese. [src: counter_ion_effects]

The report interprets the shared NaCl–metal signal as shared cellular-stress biology involving cell-envelope integrity, DNA repair, and ion homeostasis, rather than chloride contamination from metal salts; these mechanistic categories were not tested by formal functional-enrichment analyses. [src: counter_ion_effects]

NaCl is not a pure chloride control because it supplies both sodium and chloride and produces osmotic stress. [src: counter_ion_effects]

## Counter-ion interpretation

Chloride concentration did not explain the observed overlap: zinc sulfate, which delivers 0 mM chloride, had 44.6% NaCl overlap, compared with 41.3% for cobalt, 41.0% for copper, and 39.3% for nickel. [src: counter_ion_effects]

Metals delivered with chloride had a mean NaCl overlap of 41.6%, compared with 37.8% for metals delivered without chloride. [src: counter_ion_effects]

In [[entities/desulfovibrio-vulgaris-hildenborough]], whole-genome Pearson correlations between NaCl and metal-fitness profiles ranged from zinc at r=0.715 to iron at r=0.086; zinc sulfate had zero chloride and nevertheless ranked first. [src: counter_ion_effects]

The report therefore rejected the hypothesis that chloride dose is the primary driver of NaCl–metal overlap, while noting that the comparison does not isolate sodium, chloride, and osmotic effects. [src: counter_ion_effects]

## Relation to fitness concepts

The NaCl overlap supports [[concepts/condition-specific-fitness]] by showing that metal-fitness profiles contain both shared-stress and metal-specific condition responses. [src: counter_ion_effects]

The DvH NaCl–metal correlation hierarchy provides evidence relevant to [[concepts/cofitness-network-architecture]], including a proposed decomposition of shared and condition-specific fitness modules. [src: counter_ion_effects]

The corrected Metal Fitness Atlas analysis remained robust after removing shared-stress genes, linking NaCl stress to [[concepts/gene-essentiality]] without attributing the atlas core-enrichment result to NaCl-responsive genes. [src: counter_ion_effects]

## Limitations and follow-up tests

The 39.8% overlap depends on the NaCl-importance threshold, defined as fit < -1 or n_sick ≥ 1. [src: counter_ion_effects]

The *S. elongatus* estimate is especially sensitive because that organism had 12 NaCl experiments spanning 0.5–250 mM, whereas other organisms had 1–6 NaCl experiments. [src: counter_ion_effects]

The report proposes KCl or choline chloride controls, matched CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ experiments, and DvH NaCl dose-response experiments at 0.1, 1, 10, 100, and 500 mM to separate counter-ion effects from broader stress responses. [src: counter_ion_effects]

## Source

- [[summaries/counter_ion_effects__REPORT]] — analysis of counter-ion effects on metal-fitness measurements. [src: counter_ion_effects]
