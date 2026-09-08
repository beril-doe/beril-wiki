---
type: Summary
description: Experimental prioritization and validation framework for bacterial functional
  dark matter
doc_type: short
full_text: ../sources/functional_dark_matter__REPORT.md
title: Functional Dark Matter — Experimentally Prioritized Novel Genetic Systems
sources:
- id: functional_dark_matter
  resource: ../sources/functional_dark_matter__REPORT.md
  title: functional dark matter
---
# Functional Dark Matter — Experimentally Prioritized Novel Genetic Systems

## Overview

This report integrates Fitness Browser fitness profiles, essentiality, pangenome links, fitness modules, gene domains, environmental metadata, GapMind pathway analysis, cross-organism concordance, synteny, co-fitness, and Bakta reannotation to prioritize experimentally actionable bacterial genes of unknown function. Across 48 organisms, it identifies 57,011 dark genes among 228,709 genes, ranks candidates through evidence-weighted and conservation-weighted routes, and converts gene-level evidence into organism-level experimental campaigns. [^functional_dark_matter]

## Key Findings

### Scale and evidence coverage

Of 228,709 genes across 48 Fitness Browser organisms, 57,011 (24.9%) lack functional annotation as hypothetical proteins, DUFs, or uncharacterized genes. Of these, 7,787 show strong fitness effects (|fitness| ≥ 2 in at least one condition) and 9,557 are essential because no viable transposon mutants were recovered; together, 17,344 genes have experimentally measurable phenotypes. Dark genes range from more than 35% to less than 15% of an organism’s genes, a pattern interpreted as annotation-depth variation rather than established differences in functional content. [^functional_dark_matter]

Among the 57,011 dark genes, 39,532 (69.3%) have pangenome links, 12,686 are accessory, 511 are both accessory and strongly fitness-active, and 6,142 belong to independent-component-analysis (ICA) fitness modules, which group genes with coordinated fitness profiles. Stress conditions, including metals, oxidative stress, and osmotic stress, dominate strong dark-gene phenotypes, followed by carbon-source and nitrogen-source utilization. [^functional_dark_matter]

### Metabolic gaps and pathway hypotheses

GapMind identified 1,256 organism–pathway pairs across 44 Fitness Browser-linked species in which nearly complete pathways had `steps_missing_low` scores and co-occurred with strongly fitness-active dark genes. The most frequent gaps included fucose utilization in 32 organisms, rhamnose utilization in 31, sorbitol utilization in 30, myoinositol utilization in 28, gluconate utilization in 26, and asparagine biosynthesis in 24. Marinobacter had 49 gapped pathways, while *Desulfovibrio desulfuricans* ME-23 and *Pseudomonas stutzeri* had 45 each. [^functional_dark_matter]

These GapMind results are organism-level co-occurrences, not direct gene-to-enzyme assignments. Supplementary domain matching identified 42,239 gene–pathway candidates across 3,186 unique dark genes, including 5,398 high-confidence EC-prefix matches, 4,687 medium-confidence Pfam-family matches, and 32,154 low-confidence keyword matches. Confirming individual assignments requires EC matching, structure prediction, enzymology, or other experimental validation. [^functional_dark_matter]

### Conserved phenotypes and phylogenetic breadth

Cross-organism fitness concordance identified 65 ortholog groups present in at least three organisms whose dark-gene orthologs showed measurable effects under the same condition classes. The strongest examples included carbon-source groups OG11386, OG15006, and OG14628; stress-associated groups OG05812, OG05815, and OG03384; and motility-associated groups OG10428 and OG10455. Several groups had concordance of 1.00, including OG11386 across 8 organisms and OG15006 across 7 organisms. [^functional_dark_matter]

Phylogenetic analysis mapped 30,756 dark-gene clusters across 27,690 species. The initial eggNOG ortholog-group breadth classification assigned 30,721 of 30,756 clusters (99.9%) to universal breadth, making it poorly discriminative; species counts ranged from 1 to 33, with median 1 and mean 2.2. A species-count scoring variant had Spearman ρ = 0.982 with the original ranking, but top-50 overlap was 62% and top-100 overlap was 58%. [^functional_dark_matter]

Full GTDB r214 pangenome analysis expanded conservation coverage from 32,791 (57.5%) to 37,997 (66.6%) dark genes by querying 93.5M gene-cluster annotations and propagating ortholog-group identifiers to recover 5,206 additional dark genes. Species counts ranged from 1 to 27,482, with median 135 and mean 2,128; phylum counts ranged from 1 to 142. Among 11,774 root ortholog groups, 55.9% were kingdom-level, 11.0% class-level, 10.5% family-level, 6.9% genus-level, 6.5% mobile, 4.8% phylum-level, 3.9% order-level, and 0.5% species-level. [^functional_dark_matter]

The conservation-by-ignorance classification assigned 6.0% of dark genes to strong testable hypotheses, 52.5% to weak leads, and 41.5% to true knowledge gaps. The highest-ranked knowledge gaps included COG0468 with 27,427 species across 142 phyla, COG0443 with 27,279 species, and COG0491 with 27,393 species. A conservation-weighted covering set selected 42 organisms covering 95.6% of importance-weighted priority across 28,584 high-priority dark genes. [^functional_dark_matter]

### Environmental and lab–field concordance

Within-species carrier-versus-non-carrier analyses tested 151 accessory dark-gene clusters across 31 species; 10 of 137 clusters with environmental-category tests showed significant enrichment at FDR < 0.05, and 1 of 67 showed significant AlphaEarth embedding divergence. A pre-registered lab–field mapping found 29 of 47 testable clusters concordant (61.7%); pH-associated genes had 100% concordance across 4 tests and nitrogen-source genes had 78% concordance across 9 tests. [^functional_dark_matter]

The top biogeographic signals included *Pseudomonas putida* PP_0025 with odds ratio 27.5 and FDR 7e-6, *P. putida* PP_3434 with odds ratio 28.6 and FDR 7e-6, and *P. putida* N2C3 AO356_11255 with odds ratio 44.0 and FDR 0.093. The AO356_11255 carriers were enriched in soil, freshwater, and wastewater environments relative to non-carriers, matching its nitrogen-utilization fitness phenotype. [^functional_dark_matter]

The one-sided binomial test for 29/47 concordant clusters gave p = 0.072, with Wilson score 95% CI [0.474, 0.742], while Fisher’s combined probability across 47 individual tests gave p = 0.031. NMDC, the National Microbiome Data Collaborative dataset, independently mapped 5 of 6 carrier genera to 47 taxon columns across 6,365 metagenomic samples and confirmed all 4 testable pre-registered abiotic predictions: nitrogen-source carriers correlated with total nitrogen (ρ = +0.109, n = 1,231, FDR = 2.3e-4) and ammonium nitrogen (ρ = +0.231, n = 1,230, FDR = 8.0e-16), pH carriers correlated with pH (ρ = +0.157, n = 4,366, FDR = 7.4e-25), and anaerobic carriers correlated negatively with dissolved oxygen (ρ = -0.298, n = 272, FDR = 1.5e-6). [^functional_dark_matter]

NMDC trait-feature analysis confirmed all 7 pre-registered trait-condition predictions at FDR < 10⁻²¹, including nitrogen-source carriers with nitrogen fixation (ρ = 0.60) and nitrate denitrification (ρ = 0.52), and carbon-source carriers with aerobic chemoheterotrophy (ρ = 0.73) and fermentation (ρ = 0.59). However, 441 of 449 exploratory tests also reached FDR < 0.05, and the report attributes this high rate largely to compositional coupling because abundant genera contribute to both carrier abundance and community trait scores. [^functional_dark_matter]

### Candidate prioritization and experimental design

A six-axis score combining fitness importance, cross-organism conservation, inference quality, pangenome distribution, biogeographic signal, and experimental tractability ranked 17,344 phenotype-bearing dark genes. The top 100 candidates span 22 organisms, with Shewanella MR-1 contributing 25, *P. putida* N2C3 18, and Marinobacter 9; 82/100 have high-confidence functional hypotheses supported by at least 3 evidence types, and 85/100 have module-based predictions. Scores range from 0.624 to 0.715. [^functional_dark_matter]

The highest-ranked fitness-active candidate was *P. putida* N2C3 AO356_11255, with |fit| = 3.4 under nitrogen conditions, a D-alanyl-D-alanine carboxypeptidase prediction, an EamA domain, and a lab–field odds ratio of 44. The next candidates included MR-1 202463 with |fit| = 6.4 under stress and a YGGT domain, and the MR-1 K03306 paralog trio 199738, 203545, and 202450, with nitrogen-associated fitness effects of 5.5, 4.0, and 3.9 respectively. [^functional_dark_matter]

A greedy set-cover analysis found that 10 organism–condition experiments would address 242 of the top 500 dark genes (45.3%). The first three MR-1 experiments—stress, nitrogen source, and carbon source—would address 111 candidates (20.8%); the full 10-experiment sequence included MR-1 stress, MR-1 nitrogen source, MR-1 carbon source, *P. putida* N2C3 stress, *Sinorhizobium meliloti* carbon source, *S. meliloti* stress, *P. stutzeri* RCH2 stress, Marinobacter stress, *P. fluorescens* GW456-L13 carbon source, and *P. putida* carbon source. [^functional_dark_matter]

Essential dark genes require a separate strategy because standard RB-TnSeq, randomly barcoded transposon sequencing, yields no viable knockout fitness profiles for them. Of 9,557 essential dark genes, the top candidates were ranked using gene-neighbor context, cross-organism conservation, phylogenetic breadth, domain annotations, and CRISPRi tractability. Among 57,011 dark genes, 30,190 (52.9%) shared a predicted operon with an annotated gene, while 97.2% had at least one annotated neighbor within a five-gene window; the report cautions that the latter rate is expected given the 75% genome-wide annotation rate. [^functional_dark_matter]

The highest-ranked essential candidates were *Escherichia coli* Keio 14796 with score 0.875 and a YbeY domain, MR-1 200382 with score 0.874 and RimP_N/DUF150_C domains, and *Klebsiella oxytoca* BWI76_RS08540 with score 0.865 and OmpA/TIGR02802 domains. The recommended approach is CRISPRi, CRISPR interference for transcriptional knockdown, including Mobile-CRISPRi for less-established organisms, followed by growth measurements under standard and stress conditions. [^functional_dark_matter]

Cross-species synteny tested 21,011 dark-gene–operon-partner pairs and found 17,058 conserved in at least one other organism and 10,150 conserved in at least 3 organisms. Independent co-fitness analysis tested 32,075 non-essential operon pairs and found 2,899 with co-fitness evidence, including 1,129 mutual top-5 pairs; 998 pairs were double-validated by conserved synteny and strong co-fitness. [^functional_dark_matter]

The darkness spectrum classified all 57,011 dark genes into T1 Void (4,273), T2 Twilight (12,282), T3 Dusk (16,103), T4 Penumbra (22,500), and T5 Dawn (1,853). A weighted covering set selected 42 organisms from 28 genera to cover 95% of scored priority, with 32 organisms sufficient for 80% coverage; 14,450 genes were hypothesis-bearing and 2,038 were classified as darkest and requiring broad screens. [^functional_dark_matter]

### Reannotation and experimental coverage

Bakta v1.12.0 with DB v6.0 reclassified 33,105 of 39,532 pangenome-linked dark genes (83.7%) as not hypothetical, representing 58.1% of all dark genes. All 100 top candidates received Bakta product descriptions, and 5 dark genes received AMRFinderPlus annotations, including mercury-resistance transport, a yersiniabactin transporter, an acid-resistance protein, a heat-resistance membrane protein, and an S8-family peptidase. A further 6,427 genes remained hypothetical in both Fitness Browser and Bakta but gained UniRef50 links for 79.4%, UniParc/UniRef100 links for 69.1%, and RefSeq links for 62.4%. [^functional_dark_matter]

The Fitness Browser collection is taxonomically uneven: 37/48 organisms are Pseudomonadota, and the top 500 candidates include 417 from Gammaproteobacteria, 71 from Alphaproteobacteria, 17 from Deltaproteobacteria, 12 from Bacteroidetes, 10 from Betaproteobacteria, 5 from Firmicutes, 2 from Cyanobacteria, and 0 from Archaea, Actinobacteria, or Epsilonproteobacteria. An extended pool of 73 organisms, including 25 non-Fitness-Browser organisms, produced a 50-organism set covering 98.7% of ortholog groups across 6 phyla; the selected non-Fitness-Browser organisms included *Pseudomonas aeruginosa* PAO1, *Vibrio cholerae* N16961, *Burkholderia cenocepacia* K56-2, *Mycobacterium tuberculosis* H37Rv, and *Campylobacter jejuni*. [^functional_dark_matter]

## Caveats and Limitations

Environmental metadata are sparse: AlphaEarth embeddings cover only 28% of genomes (83K/293K), and NCBI isolation-source metadata are inconsistent. NMDC validation is genus-level, only 5 of 6 carrier genera were matched, and common genera such as *Pseudomonas*, *Klebsiella*, and *Bacteroides* may generate broad correlations with abiotic variables independent of specific dark-gene functions. [^functional_dark_matter]

The 57,011 dark-gene count likely overestimates true functional darkness because annotations may exist in databases or releases not checked. Module predictions, which cover 6,142 dark genes in the integrated census and are reported as 6,691 in a later project-specific accounting, are guilt-by-association inferences rather than direct experimental validation. [^functional_dark_matter]

Fitness Browser condition coverage is uneven, and MR-1 has 121 historical conditions; organisms with deeper condition coverage can therefore produce more specific phenotypes and receive higher prioritization scores. The GapMind analysis is limited to amino-acid biosynthesis and carbon-utilization pathways, identifies organism-level co-occurrence rather than direct gene-to-step assignments, and does not address signaling, regulation, or structural functions comprehensively. [^functional_dark_matter]

Essential genes are penalized in fitness-centric scoring because they lack viable transposon mutants, no `genefitness` rows, and no differential fitness magnitudes; the separate essential-gene prioritization partly corrects this bias but relies on neighborhood and domain inference. The neighborhood heuristic uses a five-gene window, same-strand orientation, and gaps of no more than 300 bp, whereas tools such as DOOR, STRING, and EFI-GNT use broader taxonomic and multimodal evidence. [^functional_dark_matter]

The NMDC trait correlations are vulnerable to compositional coupling: 441/449 exploratory tests were significant despite only 7/7 pre-registered trait directions being the meaningful directional metric. A full sample-label permutation test remains future work. Likewise, the 29/47 lab–field concordance rate has a one-sided binomial p = 0.072, and equivalent annotated-accessory-gene controls were not run through the complete biogeographic pipeline. [^functional_dark_matter]

The prioritization weights are expert-assigned and exact ranks are sensitive to them. Overall rank correlations remained ρ > 0.93 across six alternative configurations, but only 64% of the original fitness-active top 50 remained under conservation-dominant or drop-tractability settings, while essential-gene top-50 retention was 36% when tractability was dropped and 48% when neighbor context was dropped. [^functional_dark_matter]

The Fitness Browser’s 77% Pseudomonadota composition limits cross-phylum inference. The extended covering set improves coverage from 4 to 6 phyla, but non-Fitness-Browser ortholog-group coverage is estimated at the genus level and may overestimate individual-organism coverage; these organisms also lack Fitness Browser condition profiles and therefore support broad screens rather than condition-specific experiments. [^functional_dark_matter]

## Slots Into

- [gene-essentiality](../concepts/gene-essentiality.md) — essential dark genes, neighborhood-based inference, CRISPRi prioritization, and the 9,557-gene essentiality analysis.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — strong fitness phenotypes, condition classes, cross-organism concordance, and targeted RB-TnSeq experiments.
- [pangenome-integration](../concepts/pangenome-integration.md) — pangenome links, full GTDB r214 conservation, ortholog-group propagation, taxonomic tiers, and covering-set optimization.
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — GapMind pathway gaps and domain-compatible candidate gene–pathway matches.
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — carrier-versus-non-carrier environmental enrichment, AlphaEarth divergence, and lab–field concordance.
- [multi-omics-integration](../concepts/multi-omics-integration.md) — NMDC abiotic and trait-feature validation and proposed proteomic and metabolomic follow-up.
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — fitness modules, co-fitness validation, conserved neighborhoods, and double-validated operon predictions.
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — integration of Fitness Browser, pangenome, GTDB, GapMind, NMDC, and Bakta evidence into one catalog.

[^functional_dark_matter]: [functional dark matter](../sources/functional_dark_matter__REPORT.md)
