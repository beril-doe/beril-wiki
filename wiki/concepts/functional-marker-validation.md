---
type: "Concept"
description: "Test functional markers against sequence evidence before ecological interpretation"
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md"]
---
# Validating Functional Markers Before Ecological Inference

Ecological conclusions based on gene markers are only as strong as the correspondence between the marker and the function it is intended to represent. The [[summaries/bacillota_b_subsurface_accessory__REPORT]] demonstrates this problem by revisiting a clay-project iron-reduction comparison after finding that its original marker KOs did not represent canonical iron-reduction functions. [src: bacillota_b_subsurface_accessory]

## Core Principle

A functional marker should be validated at the sequence or domain level, checked for biological specificity, and tested for availability across the comparison cohorts before its presence is converted into an ecological inference. [src: bacillota_b_subsurface_accessory]

The clay analysis shows why this validation must precede interpretation: the original marker set used K07811, K17324, and K17323, which the report identifies as TMAO reductase, glycerol ABC ATP-binding, and glycerol ABC permease genes rather than canonical iron-reduction markers. [src: bacillota_b_subsurface_accessory]

This workflow refines [[concepts/multi-heme-cytochrome-detection]] by treating marker choice as an empirical validation problem rather than assuming that an annotation or KO label is an adequate ecological proxy. [src: bacillota_b_subsurface_accessory]

## Evidence From the Corrected Clay Comparison

The corrected detector combined PFAM PF02085 and PFAM PF22678—PFAM is a protein-family domain resource—with a CXXCH heme-binding motif count of ≥4 in gene-cluster protein sequences; a genome was called positive if any of these signals was present. [src: bacillota_b_subsurface_accessory]

Under the corrected detector, anchor_deep contained 5/9 positive genomes, or 55.6%, compared with 1/9, or 11.1%, under the original marker set. [src: bacillota_b_subsurface_accessory]

Anchor_shallow contained 12/30 positives, or 40.0%, under the corrected detector, compared with 15/30, or 50.0%, under the original marker set. [src: bacillota_b_subsurface_accessory]

Soil_baseline contained 61/149 positives, or 40.9%, under the corrected detector, compared with 30/149, or 20.1%, under the original marker set. [src: bacillota_b_subsurface_accessory]

The corrected pairwise Fisher tests—a test of association in contingency tables—found no significant cohort differences: deep versus shallow had odds ratio 1.88 and p=0.46; deep versus baseline had odds ratio 1.80 and p=0.49; and shallow versus baseline had odds ratio 0.96 and p=1.0. [src: bacillota_b_subsurface_accessory]

These results contradict the original shallow-enrichment narrative: after marker correction, the report finds that the iron-reduction contrast loses statistical support and that corrected multi-heme cytochrome content is similar across the clay cohorts and soil baseline. [src: bacillota_b_subsurface_accessory]

## Marker Availability Is Part of Interpretation

Within Bacillota_B, PF02085 had 4 hits in 4 clusters, PF00034 had 1 hit in 1 cluster, PF13442 had 1 hit in 1 cluster, PF22678 had 1 hit in 1 cluster, and PF14537 had 0 hits in 0 clusters. [src: bacillota_b_subsurface_accessory]

Because the multi-heme cytochrome PFAM signals were sparse, CXXCH motif counting carried most of the corrected iron-reduction signal. [src: bacillota_b_subsurface_accessory]

This supports [[concepts/multi-heme-cytochrome-detection]]’s emphasis on combining domain and motif evidence, while also showing that a composite detector can depend disproportionately on one signal when marker availability is uneven. [src: bacillota_b_subsurface_accessory]

## Ecological Inference Should Preserve Marker Uncertainty

The corrected analysis does not eliminate every ecological inference from the clay project. Its sulfite-reduction-side finding remains supported: 5/9 deep-cohort genomes were positive versus a Mitzscherling rock-attached null rate of 0.2%, with binomial p=4×10⁻¹². [src: bacillota_b_subsurface_accessory]

The report therefore treats the porewater-bias interpretation as supported through sulfite reduction but unsupported on the corrected iron-reduction side. [src: bacillota_b_subsurface_accessory]

This distinction supports evidence triangulation: an ecological pattern should be retained only for the function whose marker set remains biologically defensible and statistically supported. [src: bacillota_b_subsurface_accessory]

The broader Bacillota_B comparison also illustrates why marker validation should be separated from enrichment discovery. The study identified 547 significantly enriched eggNOG orthologous groups, but manual inspection found that keyword categorization had placed relevant anaerobic-respiration and electron-transfer functions in an “other” category, including COG1977 molybdopterin metabolism, a DsrE/DsrF/DsrH-like family, and a 4Fe–4S dicluster associated with 2-oxoglutarate:ferredoxin oxidoreductase. [src: bacillota_b_subsurface_accessory]

Manual reclassification suggested that the true anaerobic-respiration-related total was closer to 80–100 of the 547 enriched OGs, showing that both false marker assignment and incomplete functional categorization can distort ecological interpretation. [src: bacillota_b_subsurface_accessory]

This finding connects marker validation to [[concepts/evidence-triangulation-for-functional-annotation]] and [[concepts/ec-less-reaction-annotation]]: sequence evidence, domain evidence, motif evidence, and ecological statistics should be evaluated together rather than treated as interchangeable evidence. [src: bacillota_b_subsurface_accessory]

## Tensions

The original analysis supported a shallow-enrichment narrative for iron reduction, whereas the corrected detector found no significant deep-versus-shallow, deep-versus-baseline, or shallow-versus-baseline difference. [src: bacillota_b_subsurface_accessory]

The disagreement is attributable to marker definition rather than to a silent reconciliation of the numerical results: K07811, K17324, and K17323 were replaced by PFAM and motif-based signals, and the resulting cohort counts and tests changed. [src: bacillota_b_subsurface_accessory]

The correction is considered robust for the multi-heme cytochrome signal but remains a Phase 1 correction that does not fully determine whether the original clay-project comparison with the Bagnoud porewater pattern should be retained. [src: bacillota_b_subsurface_accessory]

## Practical Validation Sequence

1. Identify the biochemical function that the ecological claim requires, rather than beginning with an inherited KO list. [src: bacillota_b_subsurface_accessory]
2. Verify each candidate marker against protein-family domains, motifs, gene-cluster context, and known alternative functions. [src: bacillota_b_subsurface_accessory]
3. Quantify marker availability separately for every cohort before interpreting prevalence differences. [src: bacillota_b_subsurface_accessory]
4. Recompute cohort contrasts with the corrected detector and report exact counts, effect sizes, and significance values. [src: bacillota_b_subsurface_accessory]
5. Preserve supported and unsupported functional inferences separately when only part of a multi-function ecological narrative survives correction. [src: bacillota_b_subsurface_accessory]

## Open Directions

- Apply the corrected multi-heme cytochrome detector to the full clay-project branch and test whether the Bagnoud porewater comparison changes when PFAM, motif, and cluster-context evidence are evaluated together. [src: bacillota_b_subsurface_accessory]
- Reclassify the 462 “other_or_unannotated” enriched OGs with an LLM-based or manual functional scan, then test whether the estimated 80–100 anaerobic-respiration-related OGs resolve into reproducible marker sets. [src: bacillota_b_subsurface_accessory]
- Decompose corrected marker prevalence by genus and cohort, using the 10-genome anchor and 62-genome baseline design, to test whether apparent ecological signals are lineage markers. [src: bacillota_b_subsurface_accessory]
- Benchmark the same marker-validation workflow in other phylum-matched subsurface comparisons to determine whether marker correction repeatedly changes ecological conclusions. [src: bacillota_b_subsurface_accessory]
