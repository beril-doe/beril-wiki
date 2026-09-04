---
type: "Method"
description: "Method for detecting multi-heme cytochrome signals with PFAM and CXXCH evidence"
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md"]
---
# Corrected multi-heme cytochrome detector using PFAM and CXXCH signals

## What this entity is

The corrected multi-heme cytochrome detector is a method that identifies candidate multi-heme cytochrome signals by combining PFAM-domain evidence with counts of CXXCH heme-binding motifs in gene-cluster protein sequences. [src: bacillota_b_subsurface_accessory]

**Canonical name:** Corrected multi-heme cytochrome detector using PFAM and CXXCH signals. [src: bacillota_b_subsurface_accessory]

**Known aliases:** Corrected multi-heme cytochrome detector; triple-signal detector; PFAM/CXXCH detector. [src: bacillota_b_subsurface_accessory]

**Stable external identifier:** No stable external identifier was reported in the source. [src: bacillota_b_subsurface_accessory]

## Method definition

The detector combines PFAM PF02085, PFAM PF22678, and a threshold of at least 4 CXXCH motifs in gene-cluster protein sequences. [src: bacillota_b_subsurface_accessory]

A genome is classified as positive when any one of these signals is present. [src: bacillota_b_subsurface_accessory]

The new clay-confined analysis refines the workflow by describing it as a corrected triple-signal multi-heme cytochrome detector using PFAM PF02085, PFAM PF22678, and CXXCH heme-binding motif counting with a threshold of ≥4 motifs. [src: clay_confined_subsurface]

Within the Bacillota_B pangenome, PF02085 produced 4 hits in 4 clusters, PF00034 produced 1 hit in 1 cluster, PF13442 produced 1 hit in 1 cluster, PF22678 produced 1 hit in 1 cluster, and PF14537 produced 0 hits in 0 clusters. [src: bacillota_b_subsurface_accessory]

Because multi-heme cytochrome PFAMs were sparse, CXXCH motif counting carried most of the corrected iron-reduction signal. [src: bacillota_b_subsurface_accessory]

The clay-confined report further identifies K07811, K17324, and K17323 as misidentified iron-reduction markers: they are TMAO reductase, glycerol ABC transport ATP-binding, and glycerol ABC transport permease, respectively. This **supports** retaining the corrected detector rather than the original marker set. [src: clay_confined_subsurface]

## Findings from the source project

The corrected detector identified positive genomes in 5 of 9 deep-clay genomes, or 55.6%, compared with 1 of 9, or 11.1%, under the original marker set. [src: bacillota_b_subsurface_accessory]

It identified positive genomes in 12 of 30 shallow-clay genomes, or 40.0%, compared with 15 of 30, or 50.0%, under the original marker set. [src: bacillota_b_subsurface_accessory]

It identified positive genomes in 61 of 149 soil-baseline genomes, or 40.9%, compared with 30 of 149, or 20.1%, under the original marker set. [src: bacillota_b_subsurface_accessory]

The clay-confined analysis **supports** these corrected rates, reporting 55.6% for anchor_deep (n = 9), 40.0% for anchor_shallow (n = 30), and 40.9% for soil_baseline (n = 149), versus original rates of 11.1%, 50.0%, and 20.1%, respectively. [src: clay_confined_subsurface]

Corrected pairwise Fisher tests found no significant differences between deep and shallow cohorts, with odds ratio 1.88 and p=0.46; between deep and baseline cohorts, with odds ratio 1.80 and p=0.49; or between shallow and baseline cohorts, with odds ratio 0.96 and p=1.0. [src: bacillota_b_subsurface_accessory]

The corrected detector therefore removes statistical support for the original shallow-enrichment narrative and indicates similar multi-heme cytochrome content across the clay cohorts and soil baseline. [src: bacillota_b_subsurface_accessory]

The new report **supports** withdrawal of the original shallow-greater-than-deep iron-reduction narrative: all corrected cohort comparisons had Fisher p ≥ 0.46. It also states that the corrected iron-reduction comparison does not establish a deep-clay enrichment, while the separate sulfate-reduction finding remains supported. [src: clay_confined_subsurface]

The source characterizes this correction as robust for the multi-heme cytochrome signal, while noting that it remains a Phase 1 correction and does not fully determine whether the original clay-project comparison with the Bagnoud porewater pattern should be retained. [src: bacillota_b_subsurface_accessory]

## Relation to the research corpus

This method provides the marker-correction workflow discussed in [[concepts/functional-marker-validation]]. [src: bacillota_b_subsurface_accessory]

Its application revises the interpretation of deep-clay Bacillota_B specialization described in [[concepts/subsurface-bacillota-specialization]]. [src: bacillota_b_subsurface_accessory]

The cohort-level comparison is part of the within-lineage pangenome analysis summarized in [[concepts/pangenome-integration]]. [src: bacillota_b_subsurface_accessory]

The complete project contexts are available in [[summaries/bacillota_b_subsurface_accessory__REPORT]] and [[summaries/clay_confined_subsurface__REPORT]]. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
