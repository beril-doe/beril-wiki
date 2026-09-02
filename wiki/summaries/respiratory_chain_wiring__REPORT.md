---
type: "Summary"
description: "Condition-specific respiratory-chain wiring in Acinetobacter baylyi ADP1"
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

ADP1 contains three parallel NADH dehydrogenases: 13-subunit proton-pumping Complex I, single-subunit non-proton-pumping NDH-2, and single-subunit ACIAD3522, an NADH-FMN oxidoreductase. Complex I pumps 4 H⁺/NADH. Complex I growth ratios are 0.37 on quinate, 1.44 on glucose, and 0.49 on acetate; ACIAD3522 growth ratios are 1.39 on quinate, 1.39 on glucose, and 0.013 on acetate. NDH-2 has no growth data. [src: respiratory_chain_wiring]

NDH-2 is identified as ACIAD_RS16420 with KO K03885. It is TnSeq-dispensable but absent from the deletion collection, is a standalone gene rather than part of a respiratory operon, and is in the core genome. FBA predicts zero flux through NDH-2 on all standard carbon sources because the model routes NADH through Complex I. [src: respiratory_chain_wiring]

ACIAD3522 is dispensable on quinate and glucose but has a 0.013 growth ratio on acetate, where the report describes it as lethal. The report cautions that ACIAD3522 may not be a respiratory NADH dehydrogenase in the strict sense and could have another metabolic function. [src: respiratory_chain_wiring]

### 3. The quinate–Complex I paradox is explained by NADH flux rate

Quinate produces 4 total NADH, or 0.57 NADH per carbon, compared with 9 total NADH and 1.50 NADH per carbon for glucose, 3 total NADH and 1.50 NADH per carbon for acetate, and 5 total NADH and 1.67 NADH per carbon for lactate. Despite its lower total yield, quinate makes Complex I more important, with a growth ratio of 0.37, whereas Complex I is dispensable on glucose, with a growth ratio of 1.44. [src: respiratory_chain_wiring]

The proposed resolution is that aromatic-ring cleavage through the β-ketoadipate pathway produces succinyl-CoA and acetyl-CoA simultaneously, generating a concentrated TCA-cycle NADH burst that exceeds NDH-2 reoxidation capacity. Glucose distributes NADH production across Entner–Doudoroff pathway steps and the TCA cycle, remaining within the proposed NDH-2 capacity. This is a biochemical interpretation based on theoretical pathway stoichiometry, not measured flux distributions. [src: respiratory_chain_wiring]

The reported substrate profiles are: quinate, 4 NADH and 0.57 NADH/carbon with a concentrated TCA burst and Complex I growth of 0.37; glucose, 9 NADH and 1.50 NADH/carbon with distributed Entner–Doudoroff plus TCA production and Complex I growth of 1.44; acetate, 3 NADH and 1.50 NADH/carbon with all production through the TCA cycle and Complex I growth of 0.49; and lactate, 5 NADH and 1.67 NADH/carbon with pyruvate plus TCA production and Complex I growth of 0.77. [src: respiratory_chain_wiring]

### 4. Cross-species NDH-2 compensation is not supported

After filtering likely false positives by retaining organisms with 1–2 NDH-2 hits and excluding organisms with more than 2 hits, 5 of 14 organisms had validated NDH-2. Organisms with validated NDH-2 had a larger mean Complex I aromatic deficit, −0.297, than organisms without validated NDH-2, −0.156. The difference was not statistically significant, with p = 0.52, and was opposite to the predicted compensation pattern. [src: respiratory_chain_wiring]

The report therefore concludes that NDH-2 presence does not predict reduced Complex I dependence on aromatic substrates in the cross-species dataset. The ADP1 wiring pattern may be species-specific rather than a general rule. The comparison included only 4 organisms lacking NDH-2, making it underpowered. [src: respiratory_chain_wiring]

### 5. Proteomics supports metabolic rather than transcriptional wiring

Under standard growth conditions, the three NADH dehydrogenases had similar protein levels: Complex I mean 27.6 at the 66th percentile, NDH-2 27.0 at the 59th percentile, and ACIAD3522 26.2 at the 48th percentile, compared with a genome median of 26.4. The spread was 1.4 units. NDH-2 was therefore not repressed and was constitutively co-expressed with Complex I. [src: respiratory_chain_wiring]

These measurements support a passive, flux-based wiring model in which the dehydrogenases are present simultaneously and the limiting enzyme depends on the NADH flux rate generated by the carbon source, rather than on an active transcriptional switch. [src: respiratory_chain_wiring]

### 6. Respiratory-chain inventory and model limitations

The 62 respiratory-chain genes comprise Complex I with 13 genes, NDH-2 with 1 gene, NADH-flavin oxidoreductases with 5 genes, cytochrome bo3 with 4 genes, cytochrome bd with 5 genes, Complex II/succinate dehydrogenase with 5 genes, ATP synthase with 9 genes, and other respiratory components with 20 genes. Of these genes, 36 have growth data and 26 do not, including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring]

FBA predicts zero flux through NDH-2 and ACIAD3522 on all standard media because it optimizes growth and preferentially routes NADH through Complex I, which produces more ATP per NADH. The report identifies this optimization assumption as a fundamental reason that FBA misses condition-specific respiratory requirements and capacity constraints that can force use of alternative, suboptimal pathways. [src: respiratory_chain_wiring]

## Caveats and Open Tests

- NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be directly tested in the current dataset. [src: respiratory_chain_wiring]
- The stoichiometry analysis uses theoretical pathway biochemistry rather than measured flux distributions. [src: respiratory_chain_wiring]
- The cross-species comparison has only 4 organisms without NDH-2 and is insufficient for statistical significance. [src: respiratory_chain_wiring]
- The NDH-2 gene search may miss orthologs because annotation varies among Fitness Browser organisms. [src: respiratory_chain_wiring]
- ACIAD3522 may not be a true respiratory NADH dehydrogenase; its NADH-FMN oxidoreductase annotation could represent another metabolic function. [src: respiratory_chain_wiring]
- Text matching on gene descriptions likely produced false-positive NDH-2 calls, especially in organisms with incompletely annotated Complex I subunits; KO-based identification using K03885 would be more reliable. [src: respiratory_chain_wiring]
- The planned pangenome KO co-occurrence analysis was not performed, leaving NDH-2/Complex I co-occurrence across Acinetobacter species untested. [src: respiratory_chain_wiring]
- The proposed wiring model can be tested by constructing an NDH-2 deletion mutant, measuring NADH/NAD⁺ ratios on each carbon source, expanding the cross-species K03885 and K00330–K00343 analysis across 27K species, characterizing ACIAD3522, and reanalyzing quinate-versus-succinate proteomics for respiratory-chain proteins. [src: respiratory_chain_wiring]

## Slots Into

- [[concepts/condition-specific-fitness]] — supplies a substrate-specific example in which gene fitness and respiratory requirements change qualitatively across carbon sources. [src: respiratory_chain_wiring]
- [[concepts/metabolic-model-gapfilling]] — demonstrates that FBA can miss alternative respiratory flux because growth optimization routes NADH through the ATP-favorable pathway. [src: respiratory_chain_wiring]
- [[concepts/gene-essentiality]] — adds condition-specific Complex I and ACIAD3522 fitness evidence, including Complex I growth ratios of 0.37 on quinate, 1.44 on glucose, and 0.49 on acetate, and ACIAD3522 growth of 0.013 on acetate. [src: respiratory_chain_wiring]
- [[concepts/multi-omics-integration]] — integrates gene-phenotype measurements, FBA, theoretical stoichiometry, cross-species fitness, and proteomics to interpret respiratory-chain wiring. [src: respiratory_chain_wiring]
