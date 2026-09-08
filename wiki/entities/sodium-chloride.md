---
type: Compound
description: Sodium chloride used as a stress comparator in metal-fitness analysis
sources:
- id: counter_ion_effects
  resource: ../summaries/counter_ion_effects__REPORT.md
  title: counter ion effects
title: Sodium chloride
---
# Sodium chloride

## Identity

Sodium chloride is the canonical name for the compound abbreviated **NaCl** in the report. [^counter_ion_effects]

- **Known alias:** NaCl. [^counter_ion_effects]
- **Stable external identifier:** No stable external identifier is reported in this document. [^counter_ion_effects]

## Evidence from counter-ion analysis

The analysis included 71 NaCl experiments, 4,648 NaCl-important genes, and 25 organisms. [^counter_ion_effects]

Across 19 organisms and 14 metals, 4,304 of 10,821 metal-important gene records, or 39.8%, were also NaCl-important. [^counter_ion_effects]

After excluding the *Synechococcus elongatus* outlier, the overlap was 3,739 of 10,183 records, or 36.7%. [^counter_ion_effects]

NaCl-important genes overlapped with metal-important genes for every metal, with overlap ranging from 9.2% for molybdenum to 57.6% for manganese. [^counter_ion_effects]

The report interprets the shared NaCl–metal signal as shared cellular-stress biology involving cell-envelope integrity, DNA repair, and ion homeostasis, rather than chloride contamination from metal salts; these mechanistic categories were not tested by formal functional-enrichment analyses. [^counter_ion_effects]

NaCl is not a pure chloride control because it supplies both sodium and chloride and produces osmotic stress. [^counter_ion_effects]

## Counter-ion interpretation

Chloride concentration did not explain the observed overlap: zinc sulfate, which delivers 0 mM chloride, had 44.6% NaCl overlap, compared with 41.3% for cobalt, 41.0% for copper, and 39.3% for nickel. [^counter_ion_effects]

Metals delivered with chloride had a mean NaCl overlap of 41.6%, compared with 37.8% for metals delivered without chloride. [^counter_ion_effects]

In [desulfovibrio-vulgaris-hildenborough](desulfovibrio-vulgaris-hildenborough.md), whole-genome Pearson correlations between NaCl and metal-fitness profiles ranged from zinc at r=0.715 to iron at r=0.086; zinc sulfate had zero chloride and nevertheless ranked first. [^counter_ion_effects]

The report therefore rejected the hypothesis that chloride dose is the primary driver of NaCl–metal overlap, while noting that the comparison does not isolate sodium, chloride, and osmotic effects. [^counter_ion_effects]

## Relation to fitness concepts

The NaCl overlap supports [condition-specific-fitness](../concepts/condition-specific-fitness.md) by showing that metal-fitness profiles contain both shared-stress and metal-specific condition responses. [^counter_ion_effects]

The DvH NaCl–metal correlation hierarchy provides evidence relevant to [cofitness-network-architecture](../concepts/cofitness-network-architecture.md), including a proposed decomposition of shared and condition-specific fitness modules. [^counter_ion_effects]

The corrected Metal Fitness Atlas analysis remained robust after removing shared-stress genes, linking NaCl stress to [gene-essentiality](../concepts/gene-essentiality.md) without attributing the atlas core-enrichment result to NaCl-responsive genes. [^counter_ion_effects]

## Limitations and follow-up tests

The 39.8% overlap depends on the NaCl-importance threshold, defined as fit < -1 or n_sick ≥ 1. [^counter_ion_effects]

The *S. elongatus* estimate is especially sensitive because that organism had 12 NaCl experiments spanning 0.5–250 mM, whereas other organisms had 1–6 NaCl experiments. [^counter_ion_effects]

The report proposes KCl or choline chloride controls, matched CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ experiments, and DvH NaCl dose-response experiments at 0.1, 1, 10, 100, and 500 mM to separate counter-ion effects from broader stress responses. [^counter_ion_effects]

## Source

- [counter_ion_effects__REPORT](../summaries/counter_ion_effects__REPORT.md) — analysis of counter-ion effects on metal-fitness measurements. [^counter_ion_effects]

[^counter_ion_effects]: [counter ion effects](../summaries/counter_ion_effects__REPORT.md)
