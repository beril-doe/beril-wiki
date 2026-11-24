---
type: "Organism"
description: "Alphaproteobacterium used as the model in which Δlpxc (lipid A loss) is viable on a Δfur background with anionic sphingolipids."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/lab_field_ecology__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
aliases: ["C. crescentus", "Caulo", "Caulobacter", "Caulobacter NA1000"]
---
# Caulobacter crescentus

Caulobacter crescentus is the model in which Δlpxc (lipid A loss) is viable on a Δfur background with anionic sphingolipids. [src: caulobacter_fur_lipida_loss] The report combines its evidence into a multi-layer model for Δfur ΔsspB-permitted Δlpxc viability. [src: caulobacter_fur_lipida_loss] It describes its regulatory and proteomic evidence as the first showing that a shared-component sphingolipid/LPS transport model operates in a Caulobacter Δlpxc strain. [src: caulobacter_fur_lipida_loss] Other reports add GapMind, field-abundance and Fitness Browser data.

## Key facts

- Zik et al. 2022 (PMID, PubMed identifier, 35649364), authored by the project's data provider K.R. Ryan, is the foundational paper on Caulobacter crescentus lipid A loss. [src: caulobacter_fur_lipida_loss]
- Zik et al. established that Δlpxc viability in C. crescentus requires both Δfur and anionic sphingolipid CPG, with Fur-regulated processes rather than iron status per se underlying viability. [src: caulobacter_fur_lipida_loss]
- The Fitness Browser organisms studied in one project include Caulobacter crescentus, alongside Desulfovibrio vulgaris Hildenborough, Shewanella oneidensis MR-1, Pseudomonas putida, Pseudomonas stutzeri, Sinorhizobium meliloti and Azospirillum brasilense. [src: pathway_capability_dependency] See [[entities/sinorhizobium-meliloti]] and [[entities/azospirillum-brasilense]].
- The Tier 1 Fitness Browser analysis includes Caulobacter crescentus, abbreviated Caulo, with available GapMind pathway data. [src: pathway_capability_dependency]

## Lipid A loss model

The report supports a multi-layer model for Δfur ΔsspB-permitted Δlpxc viability. [src: caulobacter_fur_lipida_loss] See [[summaries/caulobacter_fur_lipida_loss__REPORT]] and [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]].

- In the report's data, 53 of the 93 Leaden Δfur DEGs are buffered at logFC ~0 in 4584-vs-4580 despite -5 to -9 in Leaden. The buffered set is dominated by the cbb3 / cyd / fix-NOPQ micro-aerobic respiratory operon (CCNA_01466-01476, ccoNOPQ, cydCDA, fixG/H/I). [src: caulobacter_fur_lipida_loss] See [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]].
- The report claims the first regulatory and proteomic evidence that the shared-component sphingolipid/LPS (lipopolysaccharide) transport model operates in a Caulobacter Δlpxc strain. [src: caulobacter_fur_lipida_loss]
- The dual-release-switch model predicts Δlpxc should not be viable on a Δfur background with sspB intact, because the cbb3/fix respiratory chain would shut down. [src: caulobacter_fur_lipida_loss]
- It also predicts Δlpxc should not be viable on a ΔsspB background with fur intact, because Fur would repress transport machinery needed for sphingolipid trafficking. [src: caulobacter_fur_lipida_loss]
- The report asserts that Caulobacter lacks the alternative rescue routes and that sphingolipid substitution is its only viable path. [src: caulobacter_fur_lipida_loss] See [[concepts/alternative-routes-to-tolerating-lipid-a-or-lps-loss-across-gram-negatives]].

## Amino acid pathways

In the GapMind analysis, Caulobacter vibrioides (Caulo) has 18/18 amino acid pathways complete (100%). [src: essential_metabolome] Its genome, GCF_000022005.1, has 694 GapMind predictions and is present in the collection. [src: essential_metabolome] See [[concepts/conservation-of-amino-acid-biosynthesis-pathways-across-bacteria]] and [[summaries/essential_metabolome__REPORT]].

## Field ecology

Caulobacter was detected at 82% of Oak Ridge sites. [src: lab_field_ecology] It was less abundant at high-uranium sites (Spearman rho -0.411, p-value 1.0e-5, false discovery rate (FDR) q 1.1e-4). [src: lab_field_ecology] The report interprets Caulobacter and Sphingomonas as sensitive indicators of uranium contamination, and Herbaspirillum and Bacteroides as possible tolerant colonizers. [src: lab_field_ecology] See [[entities/uranium]], [[entities/sphingomonas]], [[summaries/lab_field_ecology__REPORT]] and [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].
