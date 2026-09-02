---
type: "Gene_Or_Pathway"
description: "Aromatic degradation pathway converting quinate-derived intermediates to TCA-cycle inputs"
sources: ["summaries/adp1_triple_essentiality__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Beta-ketoadipate pathway

## What this entity is

The beta-ketoadipate pathway is an aromatic-compound degradation pathway examined as part of the FBA–experimental growth comparison in *Acinetobacter baylyi* ADP1. [src: adp1_triple_essentiality]

**Canonical name:** beta-ketoadipate pathway. [src: adp1_triple_essentiality]  
**Known aliases:** none reported in the source. [src: adp1_triple_essentiality]  
**Stable external identifier:** none reported in the source. [src: adp1_triple_essentiality]

It is related to [[entities/aromatic-amino-acid-biosynthesis]], [[entities/quinate-degradation-pathway]], [[concepts/metabolic-model-gapfilling]], and [[entities/flux-balance-analysis]]. [src: adp1_triple_essentiality]

The pathway is the central route in a 51-gene quinate-catabolism support network, converting quinate through [[entities/protocatechuate]] and beta-ketoadipate to succinyl-CoA and acetyl-CoA for entry into the TCA cycle. [src: aromatic_catabolism_network] The network identifies respiratory, iron-acquisition, PQQ-cofactor, and regulatory functions as metabolic support for the pathway, refining its interpretation from an isolated degradation route to a distributed dependency system. [src: aromatic_catabolism_network]

The respiratory-chain analysis further refines this interpretation: quinate catabolism theoretically produces 4 NADH, or 0.57 NADH per carbon, and generates succinyl-CoA and acetyl-CoA simultaneously through aromatic-ring cleavage, potentially creating a concentrated TCA-cycle NADH burst. [src: respiratory_chain_wiring] This supports a hypothesis that the pathway’s respiratory requirement reflects NADH flux rate and dehydrogenase capacity, rather than total reducing-equivalent yield alone; the proposed flux pattern is based on theoretical stoichiometry, not measured flux distributions. [src: respiratory_chain_wiring]

## Evidence from adp1_triple_essentiality

Aromatic degradation was strongly enriched among genes discordant between FBA predictions and experimental phenotypes: 9 of 11 genes were discordant, with odds ratio (OR) = 9.70 and Benjamini-Hochberg false discovery rate (FDR)-adjusted q = 0.012. [src: adp1_triple_essentiality]

Directional enrichment for FBA under-prediction was also observed for aromatic degradation, with OR = 12.0 and FDR-adjusted q = 0.004. [src: adp1_triple_essentiality]

The report identifies beta-ketoadipate-pathway genes, including 4-carboxymuconolactone decarboxylase and beta-ketoadipate enol-lactone hydrolase, as examples of genes predicted as blocked by FBA but associated with experimental growth defects. [src: adp1_triple_essentiality]

These observations support the hypothesis that missing aromatic substrates or mismatched environmental assumptions, rather than network topology alone, may explain part of the pathway’s FBA–growth discordance. [src: adp1_triple_essentiality] The new network analysis supports this model-gap interpretation: FBA captures a 1.76× higher Complex I flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31, yet predicts 0% essentiality for Complex I. [src: aromatic_catabolism_network] The respiratory-chain analysis further supports the model-gap interpretation by showing that FBA routes NADH through Complex I and predicts zero flux through alternative dehydrogenases, potentially missing capacity-limited, condition-specific respiratory requirements. [src: respiratory_chain_wiring] The proposed explanation that trace aromatic compounds in experimental media account for the discordance remains untested and requires measured media composition together with revised FBA constraints. [src: adp1_triple_essentiality]

## Related evidence

Quinate dehydrogenase requires the PQQ cofactor, while protocatechuate 3,4-dioxygenase requires non-heme Fe²⁺ for ring cleavage, linking pathway activity to cofactor supply and iron acquisition. [src: aromatic_catabolism_network] The 51-gene network assigns 8 genes to aromatic functions, 21 to Complex I, 7 to iron acquisition, and 2 to PQQ biosynthesis; 30/51 genes lack FBA reaction mappings, refining the earlier evidence for model under-representation of pathway-support functions. [src: aromatic_catabolism_network]

Condition-specific FBA flux showed weak and mixed correlations with measured growth across tested carbon sources, including glucarate ρ = +0.246 (p = 0.005; n = 127), a positive correlation opposite to the expected direction. [src: adp1_triple_essentiality]

The PQQ dependency supports aromatic-catabolism involvement but is not exclusive to it: PQQ-biosynthesis genes also appear as glucose-specific in the deletion-phenotype analysis, where they are associated with PQQ-dependent glucose dehydrogenase. [src: aromatic_catabolism_network] The respiratory-chain report adds that Complex I has a growth ratio of 0.37 on quinate, compared with 1.44 on glucose, supporting a qualitative, substrate-specific respiratory requirement associated with quinate catabolism rather than a simple dependence on total NADH yield. [src: respiratory_chain_wiring] This entity therefore contributes to [[concepts/gene-essentiality]], [[concepts/condition-specific-fitness]], [[concepts/metabolic-model-gapfilling]], and [[concepts/multi-omics-integration]] through model–phenotype comparison and integrated pathway-support evidence. [src: adp1_triple_essentiality, aromatic_catabolism_network]

## Open directions

- Add trace aromatic compounds to the FBA media definitions and test whether predictions for the implicated beta-ketoadipate-pathway genes improve. [src: adp1_triple_essentiality]
- Measure experimental media composition and compare it with condition-specific FBA constraints to test whether environmental assumptions explain the discordance. [src: adp1_triple_essentiality]
- Add PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints to the ADP1 FBA model and test whether pathway-support essentiality is better captured. [src: aromatic_catabolism_network]
- Perform condition-matched knockout and TnSeq experiments for the implicated pathway genes to determine whether their growth defects are reproducible under the relevant aromatic conditions. [src: adp1_triple_essentiality]
- Measure NADH/NAD⁺ ratios and respiratory-chain protein abundance during quinate versus succinate growth, and test whether the predicted concentrated NADH burst explains the quinate-specific Complex I requirement. [src: respiratory_chain_wiring]

See the source summaries: [[summaries/adp1_triple_essentiality__REPORT]], [[summaries/aromatic_catabolism_network__REPORT]], and [[summaries/respiratory_chain_wiring__REPORT]].
