---
type: Concept
description: Limits of inferring reaction-level genes from pathway-level metabolic
  evidence
sources:
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
title: Pathway-Level Evidence Does Not Map Directly to Reaction-Level Gene Assignments
---
# Pathway-Level Evidence Does Not Map Directly to Reaction-Level Gene Assignments

[annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md) shows that pathway-completeness evidence can indicate that metabolism is incomplete without identifying the specific reaction or gene responsible. [^annotation_gap_discovery] The independent [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md) analysis **supports** this boundary: GapMind classified 17 of 18 amino-acid biosynthesis pathways as complete in all 7 mapped organisms, yet its apparent *Desulfovibrio vulgaris* serine gap remained a computational pathway-level result rather than an identified missing gene. [^essential_metabolome] The [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md) further **supports** the distinction by separating complete pathways with experimentally important genes from complete pathways without aggregate fitness defects; pathway capability therefore cannot be treated as reaction-specific dependency. [^pathway_capability_dependency] Its broader analysis classified 267 of 1,695 complete pathway-organism pairs (15.8%) as latent capabilities, based on low aggregate fitness effects and few essential genes, demonstrating that pathway completeness can coexist with fitness neutrality under tested conditions. [^metabolic_capability_dependency]

## Evidence Resolution Mismatch

The study compared ModelSEED gapfilling, which adds individual reactions to enable predicted growth, with GapMind, which evaluates whether pathway steps are present or missing. [^annotation_gap_discovery] Among 104 GapMind–gapfill pathway pairings, GapMind frequently reported `not_present` or `steps_missing` for carbon sources whose ModelSEED models required gapfilling, but exact concordance was limited because the available BERDL records represented pathway-level step counts rather than the identities of individual missing steps. [^annotation_gap_discovery]

This mismatch means that a GapMind result can support the hypothesis that a pathway is incomplete while leaving several reaction-level explanations possible. [^annotation_gap_discovery] A pathway-level deficit therefore cannot, by itself, assign a particular gene to a particular gapfilled reaction. [^annotation_gap_discovery] The essential-metabolome result **refines** this interpretation: even a nearly complete pathway profile—17 of 18 pathways complete across all 7 organisms, with serine incomplete only for DvH—does not establish the responsible reaction or prove that the pathway gap reflects biological auxotrophy. [^essential_metabolome]

The capability–dependency analysis **supports** the same resolution boundary: among 161 organism–pathway pairs, 24 were classified as “Incomplete but Important,” meaning that mapped genes were fitness-important despite GapMind-incomplete pathways, while 66 complete pathways were “Latent Capability” because their genes showed no significant defects under standard conditions. [^pathway_capability_dependency] These categories demonstrate that pathway completeness and gene-level fitness evidence constrain one another but do not uniquely identify the missing or responsible reaction. [^pathway_capability_dependency] The newer analysis **refines** this result by showing that pathway category strongly predicted dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴), while its latent/active labels still summarize pathway-level aggregates rather than identifying a particular missing step. [^metabolic_capability_dependency]

## Reaction-Level Assignment Required Additional Evidence

The annotation-gap pipeline evaluated 201 gapfilled enzymatic reaction–organism pairs and resolved 96 (47.8%) with confidence-scored candidate genes, while 105 (52.2%) remained unresolved. [^annotation_gap_discovery] Its evidence streams included Fitness Browser phenotypes, pangenome conservation, Bakta annotations, GapMind pathway evidence, and BLAST homology rather than GapMind evidence alone. [^annotation_gap_discovery]

The full pipeline resolved 96 pairs (47.8%), compared with 86 (42.8%) without NB03 EC matching, 80 (39.8%) without NB04 Bakta annotations, and 73 (36.3%) without NB06 BLAST. [^annotation_gap_discovery] The individual streams resolved 51 pairs (25.4%) for NB03 alone, 22 (10.9%) for NB04 alone, and 70 (34.8%) for BLAST alone, showing that reaction-level assignments depended on combining complementary evidence. [^annotation_gap_discovery]

This result **supports** [evidence-triangulation-for-functional-annotation](evidence-triangulation-for-functional-annotation.md): pathway evidence is useful as one constraint, but reaction-to-gene assignment requires evidence that distinguishes among candidate steps and homologs. [^annotation_gap_discovery] It also **refines** [metabolic-model-gapfilling](metabolic-model-gapfilling.md) by showing that a gapfilled reaction is a model-level requirement, not automatically a uniquely identified biological function. [^annotation_gap_discovery]

The metabolic capability–dependency study **supports** this requirement for independent evidence: its pathway membership used SEED subsystem annotations as a proxy for GapMind pathway membership, and it notes that direct GapMind per-step gene assignments would improve precision. [^metabolic_capability_dependency] Thus, even when capability, conservation, and fitness are analyzed together, the evidence remains insufficient for a unique reaction-to-gene assignment unless step-level or other discriminating evidence is available. [^metabolic_capability_dependency]

## Why the Mapping Is Difficult

GapMind covers approximately 80 carbon and amino acid pathways rather than full metabolism, so many gapfilled reactions fall outside its coverage. [^annotation_gap_discovery] Even when a pathway is covered, the available result format reports pathway-level completeness rather than a direct reaction-to-gene mapping. [^annotation_gap_discovery] The essential-metabolome pilot **supports** this coverage caution: only 7 of the 45 organisms represented in the underlying essential-gene collection mapped successfully, and *Escherichia coli* K-12 had 0 GapMind predictions in the queried pangenome collection. [^essential_metabolome] Thus, the 17-of-18 pathway result is evidence within a restricted mapped sample, not evidence that pathway-level calls are broadly available or universally complete. [^essential_metabolome]

The capability–dependency analysis **refines** this limitation by showing that its broader GapMind survey covered 80 pathways—18 amino acid biosynthesis and 62 carbon-source utilization pathways—but that only 7 of 48 Fitness Browser organisms had matching GapMind genome data. [^pathway_capability_dependency] Its Fitness Browser-to-GapMind mapping used KEGG annotations and could miss genes lacking KEGG annotations or carrying incorrect annotations, providing another route by which pathway evidence can fail to resolve reaction-level identity. [^pathway_capability_dependency] The new analysis likewise warns that SEED-proxy mapping can introduce false positives because related subsystem annotations may not represent direct GapMind pathway membership. [^metabolic_capability_dependency]

The study also found that 50 of 201 gapfilled reactions (24.9%) lacked an EC number in ModelSEED and were designated dark reactions. [^annotation_gap_discovery] Only 8 of these 50 reactions (16%) were resolved, compared with 88 of 151 (58.3%) reactions with known EC numbers. [^annotation_gap_discovery] Because dark-reaction functions were represented by stoichiometry rather than enzyme classification, sequence-homology and functional-annotation cross-referencing were more difficult. [^annotation_gap_discovery] This **supports** [ec-less-reaction-annotation](ec-less-reaction-annotation.md) and [structural-annotation-gap](structural-annotation-gap.md) as related explanations for why pathway-level evidence often cannot close reaction-level annotation gaps. [^annotation_gap_discovery]

Gapfilling itself is non-unique: multiple valid reaction sets may explain a false-negative growth prediction, and the study used default ModelSEED gapfilling, which minimizes the number of added reactions without guaranteeing biological optimality. [^annotation_gap_discovery] Consequently, a pathway-level signal may be compatible with more than one gapfilling solution before gene-level evidence is considered. [^annotation_gap_discovery]

## Interpreting Concordance

Agreement between a GapMind pathway deficit and a ModelSEED gapfill should be interpreted as concordant support for a metabolic capability problem, not as proof that the gapfilled reaction is the missing pathway step. [^annotation_gap_discovery] The report explicitly noted that exact concordance was limited because GapMind pathway results did not identify individual step identities in the available data. [^annotation_gap_discovery]

The essential-metabolome report **supports** this evidence grading: its DvH serine result was based on GapMind predictions categorized as complete or likely_complete, but the report treated possible serine auxotrophy as a hypothesis because divergent, non-canonical, or unannotated pathway genes could have been missed. [^essential_metabolome] It further notes that rich-media RB-TnSeq—random-barcode transposon sequencing—can obscure biosynthetic essentiality through nutrient supplementation, so pathway completeness and measured gene essentiality cannot be equated. [^essential_metabolome]

The capability–dependency analysis **supports** the condition dependence of this interpretation: all 66 aggregate Latent Capability pairs became fitness-important under at least one condition type, especially nitrogen limitation, stress, or carbon limitation. [^pathway_capability_dependency] However, its median-based condition-specific threshold can cause reclassification by construction, so these results do not independently establish reaction-specific biological dependency. [^pathway_capability_dependency] The new analysis **supports** this caution: the latent fraction was 15.8% overall, but sensitivity analysis across 16 threshold combinations produced latent fractions from 4.7% to 21.1%, with SD = 5.9 percentage points. [^metabolic_capability_dependency]

The strongest reaction-level assignments arose when pathway or model evidence could be combined with more discriminating evidence streams. [^annotation_gap_discovery] For example, NB03 matched gapfilled reaction EC numbers to Fitness Browser gene annotations through pangenome gene clusters and resolved 51 of 201 pairs (25.4%) with 107 gene candidates, while NB06 identified 154 BLAST hits and contributed to the final 96 resolved pairs. [^annotation_gap_discovery] These results **support** [environmental-resistome](environmental-resistome.md) as a broader example of the distinction between inferred capability and directly supported gene identity. [^annotation_gap_discovery]

## Implication for Evidence Grading

A GapMind `not_present` or `steps_missing` result should be graded as pathway-level evidence unless the underlying step identity is independently recoverable. [^annotation_gap_discovery] A reaction-level gene assignment should require additional evidence such as EC matching, annotation alternatives, pangenome conservation, phenotype-fitness association, or sequence homology. [^annotation_gap_discovery] The study’s 47.8% overall resolution rate and 52.2% unresolved fraction show that integrated evidence can resolve a substantial subset while leaving pathway-to-reaction ambiguity for the remainder. [^annotation_gap_discovery]

## Open Directions

- Reprocess the 104 GapMind–gapfill pathway pairings against step-level GapMind outputs and ask how many pathway-level concordances become exact reaction-level matches. [^annotation_gap_discovery]
- Integrate GapMind step identities with the 201 gapfilled enzymatic reaction–organism pairs, pangenome clusters, and BLAST candidates, then test whether step-level evidence increases the 96 (47.8%) resolved-pair count without increasing unsupported assignments. [^annotation_gap_discovery]
- Stratify the 105 (52.2%) unresolved pairs by GapMind coverage and EC-number status, using contingency or regression analysis to ask whether missing pathway coverage or EC-less reactions explains more of the unresolved set. [^annotation_gap_discovery]
- Apply alternative gapfilling solutions to the 38 false-negative cases and compare their reaction sets with GapMind step deficits, asking whether non-uniqueness is responsible for pathway–reaction discordance. [^annotation_gap_discovery]
- Experimentally test high-confidence reaction–gene candidates with targeted gene knockout or CRISPRi and compare the results with pathway-level GapMind predictions, asking whether pathway agreement predicts reaction-specific fitness effects. [^annotation_gap_discovery]
- For the DvH serine gap, inspect GapMind `steps_missing` predictions and annotations, then test growth on serine-free minimal medium and complement candidate genes; this would distinguish a genuine auxotrophy from pathway-detection failure. [^essential_metabolome]
- Recalibrate the condition-specific capability–dependency threshold against known essentials from [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md), then test whether reclassified pathways yield reproducible reaction-level assignments across independent fitness conditions. [^pathway_capability_dependency]
- Replace SEED-proxy pathway membership with direct GapMind per-step gene assignments for the 1,695 complete pathway-organism pairs, then test whether pathway–fitness classes become more predictive of reaction-level candidates without increasing false-positive assignments. [^metabolic_capability_dependency]

[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
