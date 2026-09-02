---
type: "Compound"
description: "Quinate is an aromatic carbon source with distinctive Complex I dependence in ADP1."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Quinate

## Identity

**Canonical name:** Quinate. [src: acinetobacter_adp1_explorer]

**Type:** Compound. [src: acinetobacter_adp1_explorer]

**Known aliases:** No aliases were reported in the document. [src: acinetobacter_adp1_explorer]

**Stable external identifier:** No stable external identifier was reported in the document. [src: acinetobacter_adp1_explorer]

## Evidence from ADP1 studies

Quinate was one of 8 carbon sources used for mutant growth-fitness measurements in [[entities/acinetobacter-baylyi-adp1]]. [src: acinetobacter_adp1_explorer]

Pairwise mutant-fitness correlation between quinate and urea was **r = 0.11**, indicating an almost uncorrelated relationship in this dataset. [src: acinetobacter_adp1_explorer] Urea fitness was weakly correlated with the other tested conditions, with correlations of **r = 0.12-0.28**, while the mean pairwise correlation across the 8 carbon sources was **0.44**. [src: acinetobacter_adp1_explorer] The weak quinate–urea relationship supports the hypothesis that urea catabolism involves a largely independent set of genes, although this interpretation is based on the ADP1-centered dataset. [src: acinetobacter_adp1_explorer]

The deletion-collection analysis **refines** this correlation-based picture by classifying quinate as a robust condition: only **1.6%** of genes showed severe defects at growth ratio < 0.5, and the mean growth ratio was **1.36**. [src: adp1_deletion_phenotypes] The analysis identified a 24-gene module with extreme quinate-specific defects, including aromatic degradation pathway genes, while scores were near zero on other conditions. [src: adp1_deletion_phenotypes]

Quinate-specific genes included **pcaC, pcaG, pcaH, pcaB, quiA, quiB, pqqC, and pqqD**, linking quinate fitness to [[entities/quinate-degradation-pathway]] and [[entities/pqq-biosynthesis]]. [src: adp1_deletion_phenotypes] The quinate-specific set also included NADH-ubiquinone oxidoreductase subunits; this suggests the hypothesis that aromatic catabolism creates distinctive electron-transport-chain demands, rather than establishing that mechanism. [src: adp1_deletion_phenotypes]

The new 51-gene support-network analysis **supports and extends** this pathway-specific interpretation: it assigns 44/51 genes to aromatic degradation, Complex I, iron acquisition, or PQQ biosynthesis, with the pathway converting quinate through protocatechuate and β-ketoadipate to succinyl-CoA and acetyl-CoA. [src: aromatic_catabolism_network] Complex I accounts for 21/51 genes, and FBA (flux-balance analysis) measured fluxes of **0.55 versus 0.31**, or **1.76×** higher on aromatic substrates, while predicting **0%** essentiality; observed quinate-specific defects in **10/13** Complex I operon subunits therefore **refine** the earlier respiratory-demand hypothesis and expose a model blind spot. [src: aromatic_catabolism_network]

The respiratory-chain wiring analysis **supports and mechanistically refines** this interpretation: quinate generated **4 total NADH**, or **0.57 NADH per carbon**, and required Complex I, whereas cytochrome bo3, cytochrome bd, succinate dehydrogenase, and the other listed respiratory components were dispensable. [src: respiratory_chain_wiring] Complex I had a growth ratio of **0.37** on quinate, compared with **1.44** on glucose and **0.49** on acetate. [src: respiratory_chain_wiring] The report proposes that quinate-ring cleavage produces succinyl-CoA and acetyl-CoA simultaneously, creating a concentrated TCA-cycle NADH burst that may exceed NDH-2 reoxidation capacity; this is a biochemical hypothesis based on theoretical stoichiometry, not measured flux distributions. [src: respiratory_chain_wiring] This condition-specific configuration **supports** the earlier hypothesis that aromatic catabolism creates distinctive electron-transport-chain demands, while **refining** it from a general pathway association to a proposed NADH-flux-capacity mechanism. [src: respiratory_chain_wiring]

The network also **supports** roles for PQQ and iron supply in quinate catabolism, while the PQQ dependency is not exclusive to quinate because PQQ-biosynthesis genes also appeared as glucose-specific in the deletion-phenotype study. [src: aromatic_catabolism_network] Co-fitness correlations assign the previously unknown proteins ACIAD3137 and ACIAD2176 to candidate Complex I-associated functions at **r > 0.98**, although the analysis used only 8 conditions and the assignments may be indirect. [src: aromatic_catabolism_network]

These findings contribute to [[concepts/condition-specific-fitness]] and are documented in [[summaries/acinetobacter_adp1_explorer__REPORT]], [[summaries/adp1_deletion_phenotypes__REPORT]], [[summaries/aromatic_catabolism_network__REPORT]], and [[summaries/respiratory_chain_wiring__REPORT]]. [src: acinetobacter_adp1_explorer, adp1_deletion_phenotypes, aromatic_catabolism_network, respiratory_chain_wiring]
