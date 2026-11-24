---
type: "Gene_Or_Pathway"
description: "Proton-pumping NDH-1 respiratory complex encoded by the 13-gene nuo operon, dominant in the ADP1 aromatic support network."
sources: ["summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/respiratory_chain_wiring__REPORT.md"]
aliases: ["Complex I", "NADH:quinone oxidoreductase", "NDH-1", "nuo operon"]
---
# Respiratory Complex I (NADH:ubiquinone oxidoreductase)

Respiratory Complex I (NADH:ubiquinone oxidoreductase), also called Complex I, NADH:quinone oxidoreductase, NDH-1 or the nuo operon, is the proton-pumping respiratory complex of [[entities/acinetobacter-baylyi-adp1]]. [src: respiratory_chain_wiring] In ADP1 it is the dominant support requirement for aromatic catabolism. [src: aromatic_catabolism_network]

## Key facts

- Complex I is NADH:ubiquinone oxidoreductase in the ADP1 aromatic-catabolism support network. [src: aromatic_catabolism_network]
- The operon has 13 subunits (nuoA–N), all on the same strand with <100 bp intergenic distances. [src: aromatic_catabolism_network]
- It pumps 4 H⁺/NADH. [src: respiratory_chain_wiring]
- Complex I is one of 8 subsystems in a 62-gene ADP1 respiratory inventory, where it accounts for 13 genes. [src: respiratory_chain_wiring]
- Under standard growth conditions its mean protein expression is 27.6 (66th percentile). [src: respiratory_chain_wiring]

## Role in aromatic catabolism

Complex I accounts for 21 of 51 quinate-specific genes (41%). [src: aromatic_catabolism_network] The report calls NADH reoxidation the largest metabolic dependency of aromatic catabolism. [src: aromatic_catabolism_network] These genes sit in a support network with two other subsystems: iron acquisition (7 genes) and PQQ (pyrroloquinoline quinone) biosynthesis (2 genes). [src: discoveries] The proposed explanation is that the tricarboxylic acid (TCA) cycle fully oxidizes the succinyl-CoA and acetyl-CoA from β-ketoadipate. This generates reduced nicotinamide adenine dinucleotide (NADH) at multiple steps, and Complex I is needed to reoxidize it under high flux. [src: aromatic_catabolism_network] See [[concepts/support-gene-networks-around-catabolic-pathways]] and [[entities/quinate]].

Disrupting any single subunit eliminates the entire complex, which the report gives as the reason 10/13 subunits independently produce quinate-specific growth defects. [src: aromatic_catabolism_network]

## Condition dependence

Complex I is quinate-essential and glucose-dispensable. [src: discoveries] Growth ratios are 0.37 on quinate (essential), 1.44 on glucose (dispensable) and 0.49 on acetate (defect). [src: respiratory_chain_wiring] On lactate, cytochrome bo3 is required, Complex I has a mild effect and cytochrome bd is dispensable. [src: respiratory_chain_wiring] The report describes Complex I as the high-capacity primary NADH dehydrogenase, with NDH-2 as a low-capacity backup. [src: respiratory_chain_wiring] See [[concepts/condition-dependent-respiratory-chain-configuration]], [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]] and [[entities/alternative-nadh-dehydrogenase-ndh-2]].

## Co-fitness

Within-category co-fitness is dramatically higher than between-category co-fitness. The Complex I mean r is 0.992, against r = 0.961 for aromatic pathway genes. [src: aromatic_catabolism_network] The report reads r = 0.992 as essentially identical phenotypic profiles, consistent with single-operon co-regulation. [src: aromatic_catabolism_network]

Two DUF-domain proteins, ACIAD3137 and ACIAD2176, show r > 0.98 with Complex I genes. The report proposes them as candidate accessory factors. [src: aromatic_catabolism_network] See [[entities/aciad3137-and-aciad2176]].

Caveat: the 11 co-fitness assignments beyond the core nuo operon rest on phenotypic correlation only. Some may be indirect connections rather than physical association with Complex I. [src: aromatic_catabolism_network]
