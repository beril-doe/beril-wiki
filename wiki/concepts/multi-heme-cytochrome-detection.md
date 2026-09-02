---
type: "Concept"
description: "How corrected multi-signal markers improve iron-reduction comparisons"
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md"]
---
# Correcting Multi-Heme Cytochrome Markers for Iron-Reduction Comparisons

This concept concerns how marker selection changes comparisons of putative iron-reduction capacity across subsurface and soil microbial cohorts. [src: bacillota_b_subsurface_accessory]

## Why Marker Correction Was Needed

The original clay-confined-subsurface analysis used K07811, K17324, and K17323 as iron-reduction markers, but these were identified as TMAO reductase, glycerol ABC ATP-binding, and glycerol ABC permease genes rather than canonical iron-reduction markers. [src: bacillota_b_subsurface_accessory] This mismatch undermined the original interpretation of cohort differences and motivated a corrected detector. [src: bacillota_b_subsurface_accessory] The clay-confined-subsurface report **supports** this diagnosis and explicitly records that the original iron-reduction analysis was corrected because these KOs were misidentified. [src: clay_confined_subsurface]

The corrected workflow used PFAM profile signals—PF02085 and PF22678—together with a count of at least 4 CXXCH heme-binding motifs in gene-cluster protein sequences. [src: bacillota_b_subsurface_accessory] PFAM refers to protein families represented by profile models, while a CXXCH motif is a cysteine-containing sequence pattern associated with c-type heme binding. [src: bacillota_b_subsurface_accessory] A genome was classified as positive when any one of these signals was present. [src: bacillota_b_subsurface_accessory] The new report characterizes this as a corrected triple-signal multi-heme cytochrome detector, retaining PF02085, PF22678, and the CXXCH threshold of ≥4 motifs. [src: clay_confined_subsurface] This **refines** the workflow by making the signal combination explicit without changing the previously reported positivity rule. [src: clay_confined_subsurface]

## Corrected Cohort Results

The corrected detector identified multi-heme cytochrome signal in 5/9 anchor_deep genomes, or 55.6%, compared with 1/9, or 11.1%, under the original marker set. [src: bacillota_b_subsurface_accessory] In anchor_shallow, the corrected detector identified 12/30 genomes, or 40.0%, compared with 15/30, or 50.0%, under the original markers. [src: bacillota_b_subsurface_accessory] In soil_baseline, the corrected detector identified 61/149 genomes, or 40.9%, compared with 30/149, or 20.1%, under the original markers. [src: bacillota_b_subsurface_accessory] The clay report independently reports the same corrected rates—55.6% for anchor_deep (n = 9), 40.0% for anchor_shallow (n = 30), and 40.9% for soil_baseline (n = 149)—and therefore **supports** these corrected counts. [src: clay_confined_subsurface]

Pairwise Fisher exact tests found no significant corrected cohort differences: deep versus shallow had odds ratio 1.88 and p=0.46, deep versus baseline had odds ratio 1.80 and p=0.49, and shallow versus baseline had odds ratio 0.96 and p=1.0. [src: bacillota_b_subsurface_accessory] These results contradict the original shallow-enrichment narrative and refine it to a comparison in which corrected multi-heme cytochrome content is statistically similar across the clay cohorts and soil baseline. [src: bacillota_b_subsurface_accessory] The clay report **supports** this interpretation: all corrected cohort comparisons had Fisher p ≥ 0.46, and it states that the original shallow-greater-than-deep iron-reduction narrative is withdrawn. [src: clay_confined_subsurface]

## Marker Availability and Interpretation

Within the Bacillota_B pangenome, PF02085 produced 4 hits in 4 clusters, PF00034 produced 1 hit in 1 cluster, PF13442 produced 1 hit in 1 cluster, PF22678 produced 1 hit in 1 cluster, and PF14537 produced 0 hits in 0 clusters. [src: bacillota_b_subsurface_accessory] The sparse PFAM signal means that CXXCH motif counting carried most of the corrected iron-reduction signal in this comparison. [src: bacillota_b_subsurface_accessory]

The correction removes statistical support for the original shallow-enrichment interpretation, but it does not establish that all detected multi-heme cytochromes directly mediate iron reduction. [src: bacillota_b_subsurface_accessory] The corrected analysis is therefore best treated as a robust Phase 1 correction of the multi-heme cytochrome comparison rather than a complete functional assignment of iron-reduction activity. [src: bacillota_b_subsurface_accessory] The clay report **supports** this restraint: corrected iron-reduction comparisons were non-significant, with corrected rates of 55.6%, 40.0%, and 40.9% for deep, shallow, and baseline cohorts, respectively. [src: clay_confined_subsurface]

This correction should be distinguished from the clay project’s sulfite-reduction result, which remained supported: 5/9 deep-cohort genomes were positive versus a Mitzscherling rock-attached null rate of 0.2%, with binomial p=4×10⁻¹². [src: bacillota_b_subsurface_accessory] Thus, the porewater-bias interpretation remains supported through sulfite reduction but loses support on the corrected iron-reduction side. [src: bacillota_b_subsurface_accessory] The new report **supports** the underlying porewater interpretation through a sulfate-reduction signal: 5/9 deep genomes were positive versus 0.018 expected among 9 under the Mitzscherling rock-attached null, with binomial p = 4.0×10⁻¹². [src: clay_confined_subsurface]

## Tensions

The existing source describes the retained signal as “sulfite reduction,” whereas the new clay report describes it as dissimilatory “sulfate reduction”; both report 5/9 positives and the same null scale, but the terminology is not identical. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] This **requires** verification against the underlying marker definitions and source tables rather than silently treating the labels as interchangeable.

## Relation to the Source Report

The source report presents this workflow as a reusable marker-correction approach for comparisons in which functional labels were assigned from mismatched or weakly specific genes. [src: bacillota_b_subsurface_accessory] The full cohort construction, detector definitions, marker counts, and statistical results are documented in [[summaries/bacillota_b_subsurface_accessory__REPORT]]. [src: bacillota_b_subsurface_accessory] The corresponding named detection workflow is represented by [[entities/multi-heme-cytochrome-detection]]. [src: bacillota_b_subsurface_accessory] The new clay-confined analysis applies the corrected detector to its deep, shallow, and soil cohorts and documents the resulting non-significant iron-reduction comparisons. [src: clay_confined_subsurface] Its full results are documented in [[summaries/clay_confined_subsurface__REPORT]].

## Open Directions

- Reapply the corrected detector to the clay-project branch and test whether the Bagnoud porewater comparison changes when PF02085, PF22678, and the CXXCH threshold are used instead of K07811, K17324, and K17323. [src: bacillota_b_subsurface_accessory] The new report indicates that this reanalysis has now been performed for the reported cohorts, so the remaining task is to verify marker definitions and compartment annotations in the underlying tables. [src: clay_confined_subsurface]
- Use gene-cluster context, protein-domain annotation, and targeted biochemical or expression data to determine which CXXCH-positive clusters are plausibly involved in iron reduction rather than other electron-transfer processes. [src: bacillota_b_subsurface_accessory]
- Increase the number of rock-attached and porewater genomes, then repeat the corrected Fisher tests to ask whether substrate association explains multi-heme cytochrome distribution. [src: bacillota_b_subsurface_accessory] Add deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge to test whether the cultured-cohort result generalizes beyond porewater isolates. [src: clay_confined_subsurface]
- Compare the corrected detector with independently curated iron-reduction markers and metatranscriptomic or proteomic measurements to test whether marker positivity predicts active iron reduction. [src: bacillota_b_subsurface_accessory]
- Resolve the sulfite-versus-sulfate terminology by auditing the retained marker set and linking genome presence to Bagnoud’s metaproteomic evidence. [src: clay_confined_subsurface]
