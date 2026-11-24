---
type: "Organism"
description: "Sulfate-reducing bacterium and the most extensively profiled organism in the metal and NaCl fitness comparisons."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/essential_metabolome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
aliases: ["DvH", "Nitratidesulfovibrio vulgaris Hildenborough"]
---
# Desulfovibrio vulgaris Hildenborough

Desulfovibrio vulgaris Hildenborough (DvH; also Nitratidesulfovibrio vulgaris Hildenborough) is an anaerobic sulfate-reducing bacterium. [src: essential_metabolome] It is the most extensively profiled organism in the metal and sodium chloride (NaCl) fitness comparisons, with 13 metals and 6 NaCl experiments in one report. [src: counter_ion_effects] It also supplies many candidates in a screen for truly dark genes, 13 of the top 100. [src: truly_dark_genes]

## Key facts

- DvH uses sulfate as terminal electron acceptor in anaerobic respiration [src: essential_metabolome] and uses the organic acids lactate, formate, and pyruvate. [src: essential_metabolome]
- Its niches include anaerobic sediments, biofilms, and intestinal tracts. [src: essential_metabolome]
- The Fitness Browser collection holds DvH RB-TnSeq data for 757 experiments and 2,741 genes. [src: field_vs_lab_fitness] See [[entities/fitness-browser]].
- Trotter et al. (2023) generated the comprehensive barcoded transposon library used in the field-versus-lab analysis. [src: field_vs_lab_fitness]
- The ENIGMA CORAL database on the KBase Data Lakehouse contains no DvH data. [src: field_vs_lab_fitness]

## Metal and NaCl fitness

DvH is the most metal-profiled organism in the metal fitness atlas, with 149 experiments across 13 metals. [src: metal_fitness_atlas] It has 1,366 metal-important genes, 49.8% of its genome across 13 metals. [src: metal_fitness_atlas] In the metal cross-resistance report, DvH gave the richest single-organism view, and molybdenum was the most independent metal. [src: metal_cross_resistance]

In the atlas independent component analysis (ICA) of fitness modules, DvH leads with 47 responsive modules across 12 metals. [src: metal_fitness_atlas] See [[concepts/metal-responsive-ica-fitness-modules]].

### Metal–NaCl correlation hierarchy

In DvH, whole-genome fitness correlations between each metal and NaCl form a hierarchy: Zn > Mn > Cu > Co > Hg > Ni > Al > Mo > U > Se > Cr > W > Fe. [src: counter_ion_effects] The per-metal values are whole-genome Pearson r [src: counter_ion_effects]: zinc 0.715 [src: counter_ion_effects], manganese 0.545 [src: counter_ion_effects], copper 0.532 [src: counter_ion_effects], cobalt 0.498 [src: counter_ion_effects], mercury 0.478 [src: counter_ion_effects], nickel 0.446 [src: counter_ion_effects], aluminum 0.420 [src: counter_ion_effects], molybdenum 0.396 [src: counter_ion_effects], uranium 0.350 [src: counter_ion_effects], selenium 0.342 [src: counter_ion_effects], chromium 0.318 [src: counter_ion_effects], tungsten 0.298 [src: counter_ion_effects] and iron 0.086. [src: counter_ion_effects] The discoveries digest reports the same ordering with values rounded to two decimals. [src: discoveries] The per-metal correlations are in a 13-row table. [src: counter_ion_effects]

The report reads this as a gradient from general to pathway-specific toxicity. Metals that broadly displace essential cofactors (Zn, Mn, Cu, Co) share more genes with NaCl stress than metals that target specific pathways: Mo and W (molybdopterin enzymes) and Fe (iron-sulfur clusters). [src: counter_ion_effects] The metal cross-resistance report cites this as following toxicity mechanism, not counter ion identity. [src: metal_cross_resistance] See [[concepts/counter-ion-confounding-in-metal-fitness-assays]].

### Shared-stress versus metal-specific genes

DvH had 495 unique metal-important genes: 73 shared-stress (14.7%) and 422 metal-specific (85.3%). [src: counter_ion_effects] Shared-stress genes were important across a mean of 4.1 metals per gene, against 2.5 for metal-specific genes. [src: counter_ion_effects] This is consistent with broad cellular vulnerability. [src: counter_ion_effects] In the SEED annotation system, 90.5% of metal-specific genes had annotations, against 78.1% of shared-stress genes. [src: counter_ion_effects] The report suggests that the metal-specific set includes characterized Ni/Fe-hydrogenase, nitrogenase regulators and metal transporters, while shared-stress genes include more uncharacterized general stress proteins. [src: counter_ion_effects] This is a suggestion, not a tested result. See [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]].

## Dark-gene candidates

Among the top 100 truly dark gene candidates, which span 19 organisms, Methanococcus_S2 contributes 29, DvH 13, Methanococcus_JJ 13 and MR-1 8. [src: truly_dark_genes] One DvH candidate, DvH/206658, has score 9 and a stress phenotype (|f| = 5.4). Its eggNOG annotation suggests trehalose synthase despite the hypothetical annotation, which could indicate a mis-annotation or a novel variant. [src: truly_dark_genes] See [[concepts/condition-specific-fitness-of-dark-genes]].

## Field versus lab fitness and conservation

The 757 DvH experiments were classified into 6 condition categories. [src: field_vs_lab_fitness] The broad split is 337 field experiments (44.5%) and 420 lab experiments (55.5%). [src: field_vs_lab_fitness] Among 2,725 non-essential genes with both fitness data and pangenome links, 76.3% are core. [src: field_vs_lab_fitness] Field-stress-important genes are more conserved than baseline (83.6% core, odds ratio (OR) 1.58, false discovery rate (FDR) q=0.026). [src: field_vs_lab_fitness] See [[concepts/field-relevant-versus-laboratory-fitness-as-a-predictor-of-gene-conservation]].

The report cites Shi et al. (2021). That study showed that pre-existing genetic variation in DvH influences chromate tolerance, and that the chromate transporter DVU0426 is crucial for Cr(VI) resistance. [src: field_vs_lab_fitness]

### Limits

- The analysis excludes 678 essential genes (80.1% core) because no transposon mutants were recovered, so they lack fitness data. [src: field_vs_lab_fitness] Including them would raise the overall baseline slightly. It would not change condition-class comparisons, which use only non-essential genes. [src: field_vs_lab_fitness] See [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].
- The single-organism scope limits generalizability, especially to organisms with larger accessory genomes. [src: field_vs_lab_fitness]
- The Nitratidesulfovibrio vulgaris pangenome has relatively few genomes. This makes the core/auxiliary classification coarse. The high baseline core fraction (76.3%) compresses effect sizes. [src: field_vs_lab_fitness]

## Amino acid biosynthesis and apparent serine auxotrophy

DvH is in the Tier 1 Fitness Browser set with available GapMind pathway data. [src: pathway_capability_dependency] Its genome is GCF_000195755.1, with 694 GapMind predictions. [src: essential_metabolome] It has 17/18 amino acid pathways complete (94.4%). [src: essential_metabolome] It is the only analyzed organism that lacks a complete serine biosynthesis pathway under GapMind's complete or likely_complete categories. [src: essential_metabolome] See [[concepts/conservation-of-amino-acid-biosynthesis-pathways-across-bacteria]].

The report offers hypotheses for this gap. It may be a genuine auxotrophy that depends on external serine. [src: essential_metabolome] Serine would be abundant from environmental protein degradation. [src: essential_metabolome] Losing biosynthetic capacity could be advantageous when nutrients are abundant. [src: essential_metabolome] The report proposes genomic economy, meaning loss of energetically costly genes when the product is freely available. [src: essential_metabolome] DvH lives in anaerobic, organic-rich environments. [src: essential_metabolome]

The report also lists caveats:
- DvH may use a non-canonical serine pathway absent from GapMind's reference database. [src: essential_metabolome]
- The pathway may use divergent enzymes below GapMind's homology threshold. [src: essential_metabolome]
- The genes may be present but unannotated in the assembly. [src: essential_metabolome]

### Proposed checks

The report proposes testing DvH growth on serine-free minimal media to confirm auxotrophy. [src: essential_metabolome] It also proposes a literature review of whether serine auxotrophy has been documented experimentally. [src: essential_metabolome] It further proposes checking lower-confidence GapMind predictions for a serine pathway with "steps_missing" status. [src: essential_metabolome]
