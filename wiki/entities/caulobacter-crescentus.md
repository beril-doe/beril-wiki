---
type: "Organism"
description: "Model alphaproteobacterium studied for envelope and lipid A-loss adaptation"
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Caulobacter crescentus

## What this entity is

**Canonical name:** *Caulobacter crescentus* [src: caulobacter_fur_lipida_loss]

**Known alias:** *C. crescentus* [src: caulobacter_fur_lipida_loss]

**Stable external identifier:** No stable external identifier was reported in this document. [src: caulobacter_fur_lipida_loss]

*Caulobacter crescentus* is the alphaproteobacterial model in which combined loss of [[entities/fur]] and [[entities/sspb]] permits viability after deletion of [[entities/lpxc]], a lipid A-biosynthesis gene. [src: caulobacter_fur_lipida_loss]

## Findings in the lipid A-loss study

The 4584-vs-4580 contrast, representing Δ*fur* Δ*sspB* Δ*rsaA* versus Δ*rsaA*, correlated with Leaden 2018's Δ*fur* signal across 93 differentially expressed genes with Spearman ρ = 0.315, p = 2.08e-03, and 71% sign concordance. [src: caulobacter_fur_lipida_loss]

Of those 93 genes, 53 were buffered in the present data, with logFC approximately 0 despite Leaden values of -5 to -9; the buffered set was dominated by the cbb3/cyd/*fix*-NOPQ micro-aerobic respiratory operon, including CCNA_01466-01476, *ccoNOPQ*, *cydCDA*, and *fixG/H/I*. [src: caulobacter_fur_lipida_loss]

The study therefore supports [[entities/fur]] derepression in *C. crescentus*, while the mechanistic importance of the Δ*sspB*-buffered respiratory program for Δ*lpxc* rescue remains a hypothesis. [src: caulobacter_fur_lipida_loss]

The *C. crescentus* RB-TnSeq compendium in [[entities/kescience-fitnessbrowser]] covered 198 experiments, including 22 envelope-stress experiments and zero iron-limitation experiments. [src: caulobacter_fur_lipida_loss]

Among 3943 genes, 1311 had phenotype-bearing genes in the genome-wide envelope-stress background, or 33.25%. [src: caulobacter_fur_lipida_loss]

The 32-gene concordant-strong Fur signature contained 17 phenotype-bearing genes, or 53.1%, corresponding to 1.60× enrichment with hypergeometric p = 0.016, whereas the 26-gene SspB-buffered set contained 9 phenotype-bearing genes, or 34.6%, corresponding to 1.04× enrichment with p = 0.515. [src: caulobacter_fur_lipida_loss]

ChvT (CCNA_03108) had envelope-stress |*t*| = 43.7, while other Fur-derepressed TBDTs included CCNA_02910, CCNA_00210, CCNA_02048, and CCNA_00028 with |*t*| values of 9-28. [src: caulobacter_fur_lipida_loss]

Published [[entities/chvi]]-induced regulons contained 488 genes in the tested universe and partitioned into 20 unique-to-early genes, 10 genes induced in both phases, and 49 late-consequence genes, for a disjoint total of 79 induced genes. [src: caulobacter_fur_lipida_loss]

The both-phases group included ChvI itself, CCNA_00237, which had logFC +1.45 in the 4584-vs-4580 contrast, supporting ChvI autoregulation. [src: caulobacter_fur_lipida_loss]

The late-consequence group included LolA-family CCNA_03820 at +2.89, Pal-like CCNA_00784 at +2.08, a *zot*-like membrane perturber, *osrP*, and multiple TBDTs. [src: caulobacter_fur_lipida_loss]

The sphingolipid-biosynthesis pathway was constitutive rather than induced: 0/6 biosynthesis genes were UP, *spt* was DOWN by -0.64 with FDR 0.002, and *sphk* was DOWN by -0.40 with FDR 0.02. [src: caulobacter_fur_lipida_loss]

This constitutive sphingolipid-substitution route is linked to [[entities/sphingolipid-biosynthesis]] and is contrasted with the lipid A-loss pathways identified in the comparator species. [src: caulobacter_fur_lipida_loss]

CtpA/CCNA_03113 showed logFC +0.58 with pvalue = 0.048 and FDR = 0.109 in 4599-vs-4584, was not detected in the outer-membrane proteome, and was rejected at the preregistered bar. [src: caulobacter_fur_lipida_loss]

No canonical Lpt component was DOWN at the transcript level; the MsbA-like CCNA_00307 was UP by +0.89 with FDR 0.01, and LptC-related CCNA_03716 was UP by +0.56 with FDR 0.005. [src: caulobacter_fur_lipida_loss]

At the protein level, LptD changed by log2(4672/4659) = -0.47 and by log2(4672/4580) = -0.62, while LptE changed by -0.78 and -0.68, respectively. [src: caulobacter_fur_lipida_loss]

The sphingolipid transporter CCNA_01226 (*lptC2*) showed transcript -0.60 with FDR 0.034 but protein log2(4672/4659) = +1.08, corresponding to a net protein change of +0.66 log2, or approximately 1.58×, versus the wild-type baseline. [src: caulobacter_fur_lipida_loss]

The peptidoglycan-remodeling set contained 53 loci, of which 28 unique loci met the H4 threshold; 25 were transcript-significant in 4599-vs-4584 at FDR<0.05 and 6 had outer-membrane-proteome |log2|>1. [src: caulobacter_fur_lipida_loss]

The response contained 20 DOWN loci, 5 UP transcript hits, and 3 UP protein hits. [src: caulobacter_fur_lipida_loss]

Specific induced activities included SdpA/CCNA_01252 at +4.8 log2 protein, Pal/CCNA_00784 at +2.08 transcript and +2.84 protein, PleA, PbpX, and CCNA_01754. [src: caulobacter_fur_lipida_loss]

Basal division and elongation machinery was broadly reduced, including FtsI, PbpZ at -1.08 transcript, PbpC at -1.15 protein, a D,D-transpeptidase at -1.27 protein, *murD*, *mviN/murJ*, multiple LdpD/E/F M23-family endopeptidases, *amiC*, *ripA*, and membrane-bound transglycosylase A at -2.47 log2 protein. [src: caulobacter_fur_lipida_loss]

Pal was induced at both transcript and protein levels and was also among the late-cohort ChvI genes; the report interprets [[entities/tol-pal-system]] upregulation as consistent with increased lipid-remodeling demand after loss of outer-leaflet lipid A. [src: caulobacter_fur_lipida_loss]

## Metabolic context

A related GapMind pilot, a computational pathway-completeness method, included *Caulobacter vibrioides* (“Caulo”) among seven organisms and found 18/18 amino-acid biosynthesis pathways complete, or 100%, in that organism. This **supports** the interpretation that the Caulobacter model has broad biosynthetic capacity, but the result is computational, concerns *C. vibrioides* as named in that report, and does not establish that any pathway is essential for viability in *C. crescentus*. [src: essential_metabolome]

The pathway-capability analysis **refines** this comparison by including *C. crescentus* among seven Tier 1 organisms matched between Fitness Browser fitness data and GapMind predictions; only 7 of the 48 Fitness Browser organisms had matching GapMind genome data. [src: pathway_capability_dependency] It classified 161 organism–pathway pairs across those seven organisms by combining pathway completeness with gene-level fitness evidence, demonstrating that genomic capability and experimentally observed dependency are distinct rather than interchangeable. [src: pathway_capability_dependency]

The pilot also found fumarate and succinate, acetate, propionate, and L-lactate, all amino acids, deoxyribose and deoxyribonate, and putrescine conserved as carbon sources across all 7 organisms. This **refines** the envelope-focused picture with a small-sample metabolic comparison rather than evidence for a specific lipid A-loss mechanism. [src: essential_metabolome]

The newer analysis further **supports** a condition-dependent interpretation of metabolic fitness: all 66 aggregate Latent Capability pairs became fitness-important under at least one condition type, although its median-based condition-specific threshold can cause reclassification by construction and requires independent calibration. [src: pathway_capability_dependency]

## Comparative context and limitations

NCBI annotation found that *spt* and *cerR* were restricted to *C. crescentus* across *C. crescentus*, [[entities/acinetobacter-baumannii]], [[entities/neisseria-meningitidis]], and [[entities/moraxella-catarrhalis]], with pattern 1000. [src: caulobacter_fur_lipida_loss]

[[entities/chvg]] and [[entities/chvi]] also showed pattern 1000, supporting restriction of the ChvG–ChvI circuit to *C. crescentus* among the tested species. [src: caulobacter_fur_lipida_loss]

The original [[entities/kescience-paperblast]] screen returned 0 hits for LpxA versus 11 NCBI hits, 0 versus 15 for LpxC, 0 versus 15 for LpxD, 0 versus 15 for LpxB, and 0 versus 18 for LpxK, which the report characterized as an approximately 80% false-negative rate for the tested *C. crescentus* lipid A genes. [src: caulobacter_fur_lipida_loss]

The study had single-replicate outer-membrane proteomics, so the *lptC2* protein induction, Pal–Tol upregulation, LptD/LptE decline, and CCNA_01217 increase require replicated proteomics before publication-level claims can be made. [src: caulobacter_fur_lipida_loss]

The study also lacked iron-limitation experiments in its 198-experiment fitness compendium, leaving the iron-axis component of the rescue mechanism unresolved. [src: caulobacter_fur_lipida_loss]

The metabolic comparison likewise has limited scope: only 7 organisms were mapped successfully from an underlying collection of 45, and GapMind predictions are computational and may miss non-canonical or divergent pathways. The newer pathway analysis also covered only 80 pathways—18 amino acid biosynthesis pathways and 62 carbon-source utilization pathways—and used KEGG-based mapping, which can miss genes lacking KEGG annotations. These limitations **refine** rather than resolve questions about condition-specific metabolic essentiality in *C. crescentus*. [src: essential_metabolome] [src: pathway_capability_dependency]

## Related pages

- [[summaries/caulobacter_fur_lipida_loss__REPORT]]
- [[summaries/essential_metabolome__REPORT]]
- [[summaries/pathway_capability_dependency__REPORT]]
- [[concepts/multi-omics-integration]]
- [[concepts/condition-specific-fitness]]
- [[concepts/gene-essentiality]]
- [[concepts/cross-tenant-data-bridging]]
- [[concepts/metabolic-model-gapfilling]]
- [[entities/fur]]
- [[entities/chvi]]
- [[entities/chvg]]
- [[entities/lpxc]]
- [[entities/lipid-a-biosynthesis]]
- [[entities/sphingolipid-biosynthesis]]
- [[entities/tol-pal-system]]
- [[entities/kescience-fitnessbrowser]]
- [[entities/kescience-paperblast]]
