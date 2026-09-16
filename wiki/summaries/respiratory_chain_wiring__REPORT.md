---
type: "Summary"
description: "Summary of the respiratory_chain_wiring project, which reports that carbon source selects qualitatively different respiratory-chain configurations in Acinetobacter baylyi ADP1, proposes an NADH flux-rate explanation, and records a null cross-species NDH-2 compensation test and standard-condition proteomics."
doc_type: "short"
full_text: "sources/respiratory_chain_wiring__REPORT.md"
---
# Condition-Specific Respiratory Chain Wiring in ADP1

## Overview

This report maps how the branched respiratory chain of [[entities/acinetobacter-baylyi-adp1]] is configured by carbon source. It argues that substrate catabolism selects qualitatively different respiratory configurations through NADH flux rate and capacity constraints, rather than through a simple quantitative change in total reducing-equivalent yield. The analysis combines gene-phenotype data, flux-balance analysis (FBA), theoretical stoichiometry, cross-species Fitness Browser data, and proteomics. [src: respiratory_chain_wiring]

## Key Findings

### 1. Carbon source determines respiratory-chain configuration

ADP1 has 62 respiratory-chain genes across 8 subsystems. Quinate requires only Complex I; acetate requires Complex I, cytochrome bo3, ACIAD3522, and additional components; glucose has no specifically required respiratory component; lactate specifically requires cytochrome bo3; and urea is generally demanding across the respiratory chain. This is a qualitative difference in configuration rather than a quantitative gradient. [src: respiratory_chain_wiring]

- **Quinate:** Complex I is required, while cytochrome bo3, cytochrome bd, succinate dehydrogenase, and all other listed components are dispensable. [src: respiratory_chain_wiring]
- **Acetate:** Complex I, cytochrome bo3, ACIAD3522, and additional components are required; no listed component is dispensable, making acetate the most demanding condition. [src: respiratory_chain_wiring]
- **Lactate:** cytochrome bo3 is required; Complex I is mildly important and cytochrome bd is dispensable. [src: respiratory_chain_wiring]
- **Glucose:** no specific respiratory component is required and all listed components show full redundancy. [src: respiratory_chain_wiring]
- **Urea:** the condition is generally demanding and requires everything in the reported respiratory-chain profile. [src: respiratory_chain_wiring]

### 2. Three NADH dehydrogenases have distinct condition profiles

ADP1 contains three parallel NADH dehydrogenases: 13-subunit proton-pumping Complex I, single-subunit non-proton-pumping NDH-2, and single-subunit, non-proton-pumping ACIAD3522, an NADH-FMN oxidoreductase. Complex I pumps 4 H⁺/NADH. Complex I growth ratios are 0.37 on quinate, 1.44 on glucose, and 0.49 on acetate; ACIAD3522 growth ratios are 1.39 on quinate, 1.39 on glucose, and 0.013 on acetate. NDH-2 has no growth data. [src: respiratory_chain_wiring]

NDH-2 is identified as ACIAD_RS16420 with KO K03885. It is dispensable by TnSeq (transposon-insertion sequencing, which measures mutant fitness in pooled libraries) but absent from the deletion collection, is a standalone gene rather than part of a respiratory operon, and is in the core genome. FBA predicts zero flux through NDH-2 on all standard carbon sources because the model routes NADH through Complex I. [src: respiratory_chain_wiring]

ACIAD3522 is dispensable on quinate and glucose but has a 0.013 growth ratio on acetate, where the report describes it as lethal. The report cautions that ACIAD3522 may not be a respiratory NADH dehydrogenase in the strict sense and could have another metabolic function. [src: respiratory_chain_wiring]

### 3. Proposed explanation of the quinate–Complex I paradox: NADH flux rate

Quinate produces 4 total NADH, or 0.57 NADH per carbon, compared with 9 total NADH and 1.50 NADH per carbon for glucose, 3 total NADH and 1.50 NADH per carbon for acetate, and 5 total NADH and 1.67 NADH per carbon for lactate. Despite its lower total yield, quinate makes Complex I more important, with a growth ratio of 0.37, whereas Complex I is dispensable on glucose, with a growth ratio of 1.44. [src: respiratory_chain_wiring]

The proposed resolution is that aromatic-ring cleavage through the β-ketoadipate pathway produces succinyl-CoA and acetyl-CoA simultaneously, generating a concentrated TCA-cycle NADH burst that exceeds NDH-2 reoxidation capacity. Glucose distributes NADH production across Entner–Doudoroff pathway steps and the TCA cycle, remaining within the proposed NDH-2 capacity. This is a biochemical interpretation based on theoretical pathway stoichiometry, not measured flux distributions. [src: respiratory_chain_wiring]

The reported substrate profiles are: quinate, 4 NADH and 0.57 NADH/carbon with a concentrated TCA burst and Complex I growth of 0.37; glucose, 9 NADH and 1.50 NADH/carbon with distributed Entner–Doudoroff plus TCA production and Complex I growth of 1.44; acetate, 3 NADH and 1.50 NADH/carbon with all production through the TCA cycle and Complex I growth of 0.49; and lactate, 5 NADH and 1.67 NADH/carbon with pyruvate plus TCA production and Complex I growth of 0.77. [src: respiratory_chain_wiring]

### 4. Cross-species NDH-2 compensation is not supported

After filtering likely false positives by retaining organisms with 1–2 NDH-2 hits and excluding organisms with more than 2 hits, 5 of 14 organisms had validated NDH-2. Organisms with validated NDH-2 had a larger mean Complex I aromatic deficit, −0.297, than organisms without validated NDH-2, −0.156. The difference was not statistically significant, with p = 0.52, and was opposite to the predicted compensation pattern. [src: respiratory_chain_wiring]

The report therefore concludes that NDH-2 presence does not predict reduced Complex I dependence on aromatic substrates in the cross-species dataset. The ADP1 wiring pattern may be species-specific rather than a general rule. The comparison included only 4 organisms lacking NDH-2, making it underpowered. [src: respiratory_chain_wiring]

### 5. Proteomics supports metabolic rather than transcriptional wiring

Under standard growth conditions, the three NADH dehydrogenases had similar protein levels: Complex I mean 27.6 at the 66th percentile, NDH-2 27.0 at the 59th percentile, and ACIAD3522 26.2 at the 48th percentile, compared with a genome median of 26.4. The spread was 1.4 units. Under these standard conditions NDH-2 was not repressed, and the report describes it as constitutively co-expressed with Complex I. These are standard-condition measurements, not condition-specific ones. [src: respiratory_chain_wiring]

The report interprets these measurements as supporting its hypothesis of a passive, flux-based wiring model in which the dehydrogenases are present simultaneously and the limiting enzyme depends on the NADH flux rate generated by the carbon source, rather than on an active transcriptional switch. [src: respiratory_chain_wiring]

### 6. Respiratory-chain inventory and model limitations

The 62 respiratory-chain genes comprise Complex I with 13 genes, NDH-2 with 1 gene, NADH-flavin oxidoreductases with 5 genes, cytochrome bo3 with 4 genes, cytochrome bd with 5 genes, Complex II/succinate dehydrogenase with 5 genes, ATP synthase with 9 genes, and other respiratory components with 20 genes. Of these genes, 36 have growth data and 26 do not, including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring]

FBA predicts zero flux through NDH-2 and ACIAD3522 on all standard media because it optimizes growth and preferentially routes NADH through Complex I, which produces more ATP per NADH. The report identifies this optimization assumption as a fundamental reason that FBA misses condition-specific respiratory requirements and capacity constraints that can force use of alternative, suboptimal pathways. [src: respiratory_chain_wiring]

### 7. Proposed substrate-specific wiring model

**Quinate:** the report proposes that aromatic-ring cleavage produces a TCA-cycle NADH burst that makes Complex I the bottleneck. In this model cytochrome bo3 and cytochrome bd are dispensable because NADH reoxidation, not the terminal oxidase step, is limiting. This is an interpretation of the requirement profile rather than a measured flux result. [src: respiratory_chain_wiring]

**Acetate:** the proposed model is that direct TCA-cycle entry gives continuous NADH production, which requires all available dehydrogenases plus cytochrome bo3 as the primary terminal oxidase. ACIAD3522 is specifically lethal on acetate, with a 0.013 growth ratio. [src: respiratory_chain_wiring]

**Lactate:** pyruvate entry is proposed to give moderate NADH flux along with a specific cytochrome bo3 requirement. Complex I is only mildly important, with a growth ratio of 0.77. The report reads this as suggesting that NDH-2 partially compensates, which remains a hypothesis because NDH-2 has no growth data. [src: respiratory_chain_wiring]

**Glucose:** the proposed model is that the Entner–Doudoroff pathway distributes NADH production across multiple steps, so NDH-2 capacity is sufficient and no specific respiratory component is required. This NDH-2 capacity explanation is untested in the current data. [src: respiratory_chain_wiring]

### 8. Data sources, outputs and reference

A user-provided SQLite database supplied growth ratios, FBA predictions, and reaction stoichiometry from four tables: `genome_features`, `gene_phenotypes`, `gene_reaction_data`, and `genome_reactions`. [src: respiratory_chain_wiring]

The [[entities/kescience-fitnessbrowser]] collection (tables `experiment`, `gene`, `genefitness`) supplied the cross-species aromatic experiments and the Complex I/NDH-2 fitness data. [src: respiratory_chain_wiring]

The project's generated data outputs include `data/cross_species_respiratory.csv`, which has 14 rows of Complex I aromatic fitness across Fitness Browser organisms, and `data/fb_aromatic_experiments.csv`, which lists 33 Fitness Browser experiments with aromatic substrates. [src: respiratory_chain_wiring]

Figures [src: respiratory_chain_wiring]:
- `respiratory_chain_heatmap.png` shows raw growth ratios for all 36 respiratory genes across 8 conditions.
- `subsystem_profiles.png` shows mean growth by subsystem and condition.
- `respiratory_clustermap.png` clusters z-scored respiratory gene profiles by similarity.
- `wiring_model.png` compares glucose, quinate, and acetate requirements side by side.
- `nadh_stoichiometry.png` compares NADH yield with Complex I requirement and includes a reducing-equivalent bar chart.
- `wiring_matrix.png` summarizes requirement level by substrate and component.
- `ndh2_vs_complex_I.png` compares cross-species Complex I fitness on aromatic and non-aromatic substrates by NDH-2 status.
- `proteomics_respiratory.png` places NADH dehydrogenase protein abundance against the genome-wide distribution.

The report cites de Berardinis et al. (2008), "A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1" (*Molecular Systems Biology* 4:174; PMID: 18319726), which identifies the study organism as *Acinetobacter baylyi* ADP1. [src: respiratory_chain_wiring]

## Caveats and Open Tests

- NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be directly tested in the current dataset. [src: respiratory_chain_wiring]
- The stoichiometry analysis uses theoretical pathway biochemistry rather than measured flux distributions. [src: respiratory_chain_wiring]
- The cross-species comparison has only 4 organisms without NDH-2 and is insufficient for statistical significance. [src: respiratory_chain_wiring]
- The NDH-2 gene search may miss orthologs because annotation varies among Fitness Browser organisms. [src: respiratory_chain_wiring]
- ACIAD3522 may not be a true respiratory NADH dehydrogenase; its NADH-FMN oxidoreductase annotation could represent another metabolic function. [src: respiratory_chain_wiring]
- Text matching on gene descriptions likely produced false-positive NDH-2 calls, especially in organisms with incompletely annotated Complex I subunits; for example, pseudo3_N2E3 has 8 "NDH-2" hits that are probably a Complex I operon. KO-based identification using K03885 would be more reliable. [src: respiratory_chain_wiring]
- The planned pangenome KO co-occurrence analysis was not performed, leaving NDH-2/Complex I co-occurrence across Acinetobacter species untested. [src: respiratory_chain_wiring]
- The proposed wiring model can be tested by constructing an NDH-2 deletion mutant, measuring NADH/NAD⁺ ratios on each carbon source, expanding the cross-species K03885 and K00330–K00343 analysis across 27K species, characterizing ACIAD3522, and reanalyzing quinate-versus-succinate proteomics for respiratory-chain proteins. [src: respiratory_chain_wiring]
- The central prediction is that NDH-2 deletion makes Complex I essential on glucose. Only an experiment can test it, and an ADP1 NDH-2 knockout would be the definitive test. [src: respiratory_chain_wiring]
- The flux-rate hypothesis predicts higher NADH/NAD⁺ ratios in quinate-grown cells than in glucose-grown cells. Metabolomics could test this directly, but the ratios have not been measured. [src: respiratory_chain_wiring]
- It remains unresolved whether ACIAD3522 is a true respiratory NADH dehydrogenase or a metabolic enzyme. Its acetate lethality and FMN cofactor suggest a specific role in acetate catabolism that needs further investigation. [src: respiratory_chain_wiring]
- The report has not established whether ADP1 upregulates Complex I on aromatic substrates or NDH-2 on glucose. It proposes reanalyzing the quinate-versus-succinate proteomics of Stuani et al. (2014) for respiratory-chain proteins to test this. [src: respiratory_chain_wiring]

## Slots Into

- [[concepts/condition-specific-fitness]] — supplies a substrate-specific example in which gene fitness and respiratory requirements change qualitatively across carbon sources. [src: respiratory_chain_wiring]
- [[concepts/metabolic-model-gapfilling]] — demonstrates that FBA can miss alternative respiratory flux because growth optimization routes NADH through the ATP-favorable pathway. [src: respiratory_chain_wiring]
- [[concepts/gene-essentiality]] — adds condition-specific Complex I and ACIAD3522 fitness evidence, including Complex I growth ratios of 0.37 on quinate, 1.44 on glucose, and 0.49 on acetate, and ACIAD3522 growth of 0.013 on acetate. [src: respiratory_chain_wiring]
- [[concepts/multi-omics-integration]] — integrates gene-phenotype measurements, FBA, theoretical stoichiometry, cross-species fitness, and proteomics to interpret respiratory-chain wiring. The report reads protein co-expression under standard conditions as supporting its hypothesis of metabolic rather than transcriptional wiring, and condition-specific proteomics is still needed. [src: respiratory_chain_wiring]
- [[concepts/respiratory-capacity-and-nadh-load]] — the central case for the hypothesis that NADH flux rate, rather than total NADH yield, sets Complex I dependence: quinate gives 0.57 NADH/carbon with Complex I growth of 0.37, while glucose gives 1.50 NADH/carbon with growth of 1.44. The case rests on theoretical stoichiometry and the per-substrate wiring model. [src: respiratory_chain_wiring]
- [[concepts/condition-space-dimensionality]] — urea is generally demanding across the respiratory chain, unlike the substrate-specific profiles of the other carbon sources. [src: respiratory_chain_wiring]
- [[concepts/genetic-perturbation-coverage-bias]] — 26 of 62 respiratory genes lack growth data. These include NDH-2, which is TnSeq-dispensable but missing from the deletion collection, so the central compensation prediction cannot be tested. [src: respiratory_chain_wiring]
- [[concepts/cross-species-fitness-transferability]] — a null cross-species NDH-2 compensation test (p = 0.52, with only 4 organisms without NDH-2) suggests the ADP1 wiring may be species-specific. [src: respiratory_chain_wiring]
- [[concepts/callability-limited-comparative-inference]] — the missing NDH-2 growth data blocks a direct test of glucose compensation. [src: respiratory_chain_wiring]
- [[concepts/sampling-depth-and-downsampling-effects]] — the cross-species comparison is underpowered, with only 4 organisms lacking NDH-2. [src: respiratory_chain_wiring]
- [[concepts/homology-search-negative-evidence]] — text-matched NDH-2 calls may miss orthologs or include misannotated Complex I subunits. [src: respiratory_chain_wiring]
- [[concepts/functional-marker-validation]] — the report recommends KO K03885 over description text matching for identifying NDH-2. [src: respiratory_chain_wiring]
- [[concepts/evidence-triangulation-for-functional-annotation]] — ACIAD3522's NADH-FMN oxidoreductase annotation leaves its respiratory role unresolved despite its acetate lethality. [src: respiratory_chain_wiring]
- [[concepts/essentiality-assay-discordance]] — NDH-2 is TnSeq-dispensable but has no deletion data, and testing its predicted effect on Complex I essentiality on glucose needs a knockout. [src: respiratory_chain_wiring]
