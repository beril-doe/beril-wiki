---
type: "Gene_Or_Pathway"
description: "The aromatic catabolic pathway (pca/qui genes) that converts quinate via protocatechuate to succinyl-CoA and acetyl-CoA; it stops short of the individual protocatechuate dioxygenase enzyme and PQQ cofactor synthesis."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/pitfalls.md", "summaries/respiratory_chain_wiring__REPORT.md"]
aliases: ["Quinate and protocatechuate degradation pathway", "aromatic degradation pathway", "beta-ketoadipate pathway", "pca genes", "pca/qui pathway", "protocatechuate pathway", "protocatechuate–catechol funnel", "quinate degradation"]
---
# β-ketoadipate pathway

The β-ketoadipate pathway (pca/qui genes) takes quinate through protocatechuate and β-ketoadipate to succinyl-CoA and acetyl-CoA. [src: aromatic_catabolism_network] The best evidence comes from [[entities/acinetobacter-baylyi-adp1]], where deletion phenotypes, co-fitness and operon analyses all point to it. [src: adp1_deletion_phenotypes, aromatic_catabolism_network] The respiratory-chain report also describes it in P. putida KT2440, in terms that align with published knowledge. [src: respiratory_chain_wiring]

## Key facts

- In ADP1, quinate catabolism proceeds through protocatechuate to β-ketoadipate, yielding succinyl-CoA and acetyl-CoA that enter the tricarboxylic acid (TCA) cycle. [src: aromatic_catabolism_network]
- The ADP1 quinate-specific network includes 8 aromatic pathway genes, with the core route quinate → protocatechuate → β-ketoadipate → TCA cycle. [src: aromatic_catabolism_network]
- The ADP1 triple-essentiality report calls the pathway a signature feature of ADP1. [src: adp1_triple_essentiality]
- ACIAD1710 is 4-carboxymuconolactone decarboxylase (Enzyme Commission number EC 4.1.1.44), a core pca pathway enzyme. [src: pitfalls]

## Deletion phenotypes in ADP1

Quinate is the most robust condition in the ADP1 deletion collection, with only 1.6% of genes defective. [src: adp1_deletion_phenotypes] Pathway genes are the exception to this robustness. A module of 24 aromatic-degradation genes has extreme quinate-specific defects (mean z-score = -7.28 on quinate, near-zero on other conditions). [src: adp1_deletion_phenotypes] This is the only discrete phenotypic module in the dataset. [src: adp1_deletion_phenotypes] See [[concepts/continuous-versus-discrete-structure-of-condition-dependent-gene-essentiality]].

The top quinate-specific genes are pcaC, pcaG, pcaH, pcaB, quiA, quiB, pqqC and pqqD. They cover protocatechuate/quinate degradation and pyrroloquinoline quinone (PQQ) biosynthesis. [src: adp1_deletion_phenotypes] See [[entities/pyrroloquinoline-quinone-biosynthesis]]. The quinate-specific set has 51 genes at spec > 0.5, z < -1. It extends past the core pathway to Complex I NADH-ubiquinone oxidoreductase subunits. The report suggests that aromatic catabolism places unique demands on the electron transport chain. [src: adp1_deletion_phenotypes]

The report states that this condition-specificity aligns with Fischer et al. (2008), who showed coordinated, carbon-source-dependent regulation of ADP1 aromatic degradation operons. [src: adp1_deletion_phenotypes]

## Link to Complex I dependence

One report explains the ADP1 Complex I dependence on quinate through the pathway's chemistry. β-ketoadipate ring cleavage makes succinyl-CoA and acetyl-CoA at the same time. This creates a concentrated NADH (reduced nicotinamide adenine dinucleotide) burst in the TCA cycle, which exceeds the reoxidation capacity of NDH-2. [src: respiratory_chain_wiring] See [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]] and [[concepts/nadh-flux-rate-versus-nadh-yield-as-determinant-of-complex-i-dependence]].

## Discordant genes and annotation

Aromatic degradation was strongly enriched among discordant ADP1 genes (odds ratio OR = 9.70, q = 0.012). [src: adp1_triple_essentiality] Nine of 11 aromatic degradation genes were discordant. [src: adp1_triple_essentiality] They include the β-ketoadipate pathway enzymes 4-carboxymuconolactone decarboxylase and β-ketoadipate enol-lactone hydrolase. [src: adp1_triple_essentiality] See [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]].

Keyword annotation initially miscategorized ACIAD1710. The keyword list checked for "muconate" but not "muconolactone", so the gene was classed as "Other". [src: pitfalls] Co-fitness analysis recovered pcaC (4-carboxymuconolactone decarboxylase). [src: aromatic_catabolism_network] Its correlation with the Aromatic pathway was r=0.978. [src: pitfalls] See [[concepts/condition-specific-gene-phenotypes-and-functional-annotation-yield]] and [[concepts/support-gene-networks-around-catabolic-pathways]].

## Operon organization

ADP1 operon predictions match the transcriptional organization mapped experimentally by Dal et al. (2005). That includes a 12-gene pca/qui operon spanning pcaIJFBDCHG-quiABC plus transport genes. [src: aromatic_catabolism_network] See [[concepts/operon-organization-versus-functional-coupling-of-pathway-support-genes]].

## Wider distribution and convergence

The ENIGMA carbon census describes the β-ketoadipate/protocatechuate–catechol funnel as the canonical bacterial route for hydroxybenzoates, salicylate and phthalates. [src: enigma_carbon_census_1] Six of its eight callable compounds route through well-characterized aromatic catabolism. Salicylate, the hydroxybenzoates/-aldehyde and the two phthalates converge on protocatechuate/catechol and the β-ketoadipate pathway. [src: enigma_carbon_census_1] The report concludes that the six callable aromatics share one lower pathway and so co-occur within the aromatic block. [src: enigma_carbon_census_1] See [[concepts/co-occurrence-and-modularity-of-catabolic-capacities-across-genomes]] and [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]].

Terephthalate proceeds via terephthalate dioxygenase to protocatechuate. Its degraders are concentrated in Pseudomonadota (Ideonella/Comamonas) and actinobacterial lineages. [src: enigma_carbon_census_1]

Phenylethylamine is the exception. It enters the phenylacetyl-CoA (paa) ring-cleavage route rather than the shared funnel. [src: enigma_carbon_census_1] It is oxidized by amine oxidation to phenylacetate and then the paa pathway. This is mechanistically separate from the β-ketoadipate funnel, so its cross-block co-occurrence signal is not part of the funnel. [src: enigma_carbon_census_1]

The respiratory-chain report describes pseudomonas putida KT2440 as a well-studied aromatic degrader that channels diverse aromatic compounds through the β-ketoadipate pathway. It states that its P. putida aromatic fitness data align with published knowledge of Pseudomonas aromatic catabolism. [src: respiratory_chain_wiring]

## Related pages

See also [[entities/quinate]], [[summaries/adp1_deletion_phenotypes__REPORT]], [[summaries/adp1_triple_essentiality__REPORT]], [[summaries/aromatic_catabolism_network__REPORT]], [[summaries/enigma_carbon_census_1__REPORT]], [[summaries/pitfalls]] and [[summaries/respiratory_chain_wiring__REPORT]].
