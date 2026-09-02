---
type: "Method"
description: "DIAMOND sequence-comparison method for fitness, pangenome, and annotation linking"
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md"]
---
# DIAMOND

## What this entity is

**Canonical name:** DIAMOND. [src: amr_pangenome_atlas]

**Known aliases:** No aliases were reported in this document. [src: amr_pangenome_atlas]

**Stable external identifier:** None was reported in this document. [src: amr_pangenome_atlas]

DIAMOND is a sequence-comparison method used to link pangenome genes with [[entities/kescience-fitnessbrowser]] fitness measurements. [src: amr_pangenome_atlas]

## Fitness and pangenome linking

The report used a DIAMOND-based Fitness Browser pangenome link table containing 177,863 links at 100% sequence identity. [src: amr_pangenome_atlas]

Using these links, the analysis identified 178 AMR genes across 37 Fitness Browser organisms and 29,386 fitness measurements. [src: amr_pangenome_atlas]

The report also contains a separate generated-data table listing fitness data for 162 AMR genes in 36 Fitness Browser organisms, and it does not reconcile this discrepancy with the counts of 178 AMR genes and 37 organisms reported elsewhere. [src: amr_pangenome_atlas]

The 100% identity threshold was conservative because it avoided paralog confusion, but it could miss closely related variants, including alleles differing by a single synonymous substitution, and therefore undercount fitness effects. [src: amr_pangenome_atlas]

The DIAMOND-linked fitness analysis found a median fitness of -0.007 for AMR genes versus -0.012 for the non-AMR baseline, with a Mann–Whitney p-value of 3.7e-6. [src: amr_pangenome_atlas]

Beta-lactamases had a nearly neutral median fitness of -0.001, whereas singleton AMR genes had a median fitness of -0.019. [src: amr_pangenome_atlas]

Because the linked organisms were predominantly environmental strains, the report interpreted these results as consistent with well-integrated intrinsic resistance genes rather than evidence that recently acquired mobile resistance is cost-free in clinical pathogens. [src: amr_pangenome_atlas]

A cross-species conservation analysis **supports** DIAMOND's fitness-linking role: its Phase 1 gene-to-cluster table contained 177,863 links, with 100.0% median protein identity and 94.2% median gene coverage; 44 of 48 Fitness Browser organisms mapped to pangenome species clades and 33 were retained for essentiality analysis. [src: conservation_vs_fitness] The analysis also **refines** the conservative-threshold interpretation by showing that coverage, not identity alone, determined downstream usability: ten organisms were excluded because they had <90% DIAMOND coverage. [src: conservation_vs_fitness]

The costly+dispensable-gene analysis **refines** these threshold-specific findings rather than directly contradicting them: its Fitness Browser–pangenome linking used a 90% identity DIAMOND threshold, and the report cautions that this may miss recently acquired genes with low sequence similarity. [src: costly_dispensable_genes] Thus, DIAMOND identity and coverage settings were analysis-specific, with explicit tradeoffs between avoiding paralog confusion and retaining divergent accessory genes. [src: costly_dispensable_genes]

## Cross-study annotation-gap use

The annotation-gap study **extends** DIAMOND's fitness-linking role by using DIAMOND v2.1.16 blastp against Swiss-Prot exemplar sequences to identify candidate genes for gapfilled reactions. [src: annotation_gap_discovery] The search used `--evalue 1e-5 --max-target-seqs 20 --id 25 --query-cover 50 --outfmt 6` and identified 154 hits from 328 reviewed bacterial sequences representing 75/84 unique ECs. [src: annotation_gap_discovery]

DIAMOND was the strongest single evidence stream in that study, resolving 70 of 201 reaction-organism pairs (34.8%); the complete evidence pipeline resolved 96 (47.8%), so triangulation **supported and strengthened** DIAMOND-only assignments by adding 13 percentage points over BLAST alone. [src: annotation_gap_discovery] High-confidence calls required at least 30% identity, at least 70% coverage, and e-value at most 1e-10, while medium-confidence calls required at least 25% identity, at least 50% coverage, and e-value at most 1e-5. [src: annotation_gap_discovery]

The new result **refines** the conservative-threshold interpretation above: DIAMOND homology was highly informative, but 105 of 201 pairs remained unresolved and sequence evidence alone did not exceed 35% resolution. [src: annotation_gap_discovery]

## Related pages

The DIAMOND-based cross-reference contributes to [[concepts/condition-specific-fitness]] by connecting AMR gene identity with measured fitness under laboratory conditions. [src: amr_pangenome_atlas]

It also contributes to [[concepts/pangenome-integration]] by linking pangenome gene representatives to Fitness Browser measurements. [src: amr_pangenome_atlas, conservation_vs_fitness]

Its annotation-gap application contributes to [[concepts/metabolic-model-gapfilling]] and [[concepts/multi-omics-integration]] by supplying sequence-homology evidence for candidate genes alongside model, pathway, pangenome, and fitness evidence. [src: annotation_gap_discovery]

See the full source summaries at [[summaries/amr_pangenome_atlas__REPORT]], [[summaries/annotation_gap_discovery__REPORT]], [[summaries/conservation_vs_fitness__REPORT]], and [[summaries/costly_dispensable_genes__REPORT]]. [src: amr_pangenome_atlas, annotation_gap_discovery, conservation_vs_fitness, costly_dispensable_genes]
