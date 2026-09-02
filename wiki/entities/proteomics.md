---
type: "Method"
description: "Protein-expression measurement used to interpret essentiality and respiratory-chain wiring"
sources: ["summaries/adp1_triple_essentiality__REPORT.md", "summaries/caulobacter_fur_lipida_loss__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Proteomics

## What it is

**Canonical name:** Proteomics. [src: adp1_triple_essentiality]

**Known aliases:** No additional aliases are reported in this document. [src: adp1_triple_essentiality]

**Stable external identifier:** Not applicable or reported for this method in the document. [src: adp1_triple_essentiality]

Proteomics measures protein expression and was used as an independent evidence axis alongside [[entities/flux-balance-analysis]], [[entities/tnseq]], complete-gene knockout phenotypes, and mutant growth measurements in the study of [[entities/acinetobacter-baylyi-adp1]]. [src: adp1_triple_essentiality]

## Evidence from adp1_triple_essentiality

Proteomics measured average log2 expression across 7 *Acinetobacter* strains for 2,288 genes. [src: adp1_triple_essentiality]

Among these genes, essential genes (n = 464) had mean log2 expression of 28.43 ± 2.94, whereas dispensable genes (n = 1,824) had mean log2 expression of 25.73 ± 2.96. [src: adp1_triple_essentiality]

Essential genes therefore showed a difference of 2.70 log2 expression units, corresponding to 6.5-fold higher expression than dispensable genes. [src: adp1_triple_essentiality]

The difference in expression between essential and dispensable genes was statistically significant by the Mann–Whitney U test, with p = 9.91×10⁻⁵⁹. [src: adp1_triple_essentiality]

Expression correlated with knockout essentiality at Pearson r = 0.345 (p = 5.32×10⁻⁶⁵) and Spearman ρ = 0.338 (p = 3.28×10⁻⁶²). [src: adp1_triple_essentiality]

Proteomic expression classified knockout essentiality with ROC AUC = 0.743, where AUC means Area Under the ROC Curve, a threshold-independent classification measure. [src: adp1_triple_essentiality]

These results support [[concepts/multi-omics-integration]] by showing that proteomics provides a complementary continuous predictor alongside flux-balance analysis (FBA), fitness, knockout, and TnSeq evidence. [src: adp1_triple_essentiality]

## Evidence from caulobacter_fur_lipida_loss

Single-replicate outer-membrane proteomics in [[entities/caulobacter-crescentus]] **refines** the existing complementary-evidence claim: it was used with transcriptomics, RB-TnSeq fitness, published regulons, and comparative annotation to examine envelope remodeling rather than to quantify essentiality directly. [src: caulobacter_fur_lipida_loss]

The protein measurements **support** transcript–protein discordance in the Lpt apparatus: LptD changed by log2(4672/4659) = -0.47 and by log2(4672/4580) = -0.62, while LptE changed by -0.78 and -0.68, despite transcript-level increases for MsbA-like CCNA_00307 (+0.89, FDR 0.01) and LptC-related CCNA_03716 (+0.56, FDR 0.005). [src: caulobacter_fur_lipida_loss]

The same proteome found CCNA_01226 (*lptC2*) protein at +1.08 log2 in 4672/4659, with a net change of +0.66 log2 versus wild type, and CCNA_01217 at +0.77 versus 4659 or +0.74 versus wild type; these single-replicate observations are consistent with post-transcriptional stabilization but do not establish it statistically. [src: caulobacter_fur_lipida_loss]

Pal/CCNA_00784 increased by +2.84 at the protein level and +2.08 at the transcript level, while several division and peptidoglycan-remodeling proteins decreased, including PbpC at -1.15 and membrane-bound transglycosylase A at -2.47 log2. [src: caulobacter_fur_lipida_loss]

## Evidence from respiratory_chain_wiring

Proteomics **supports** a passive, flux-based interpretation of condition-specific respiratory-chain wiring in [[entities/acinetobacter-baylyi-adp1]], rather than contradicting the existing use of protein abundance as complementary evidence. Under standard growth conditions, Complex I, NDH-2, and ACIAD3522 had similar protein levels: Complex I mean 27.6 at the 66th percentile, NDH-2 27.0 at the 59th percentile, and ACIAD3522 26.2 at the 48th percentile, compared with a genome median of 26.4; the spread was 1.4 units. [src: respiratory_chain_wiring]

NDH-2 was therefore not repressed and was constitutively co-expressed with Complex I, while gene-phenotype data showed condition-specific respiratory requirements; together these observations support a model in which the limiting dehydrogenase depends on carbon-source-generated NADH flux rather than an active transcriptional switch. [src: respiratory_chain_wiring]

This result **refines** the prior recommendation to combine FBA, fitness, and proteomics: abundance measurements can indicate that respiratory alternatives are present simultaneously, whereas growth-optimized FBA may predict zero flux through NDH-2 and ACIAD3522 because it preferentially routes NADH through the higher-ATP-yielding Complex I. [src: respiratory_chain_wiring]

## Interpretation limits

The expression values were averaged across 7 *Acinetobacter* strains rather than measured only in the exact knockout assay condition, so the association with essentiality is independent supporting evidence rather than a condition-matched causal test. [src: adp1_triple_essentiality]

The report recommends combining FBA, fitness, and proteomics for essentiality prediction, but this proposed integration remains a recommended analysis rather than a completed result in the document. [src: adp1_triple_essentiality]

The Caulobacter outer-membrane proteome had a single replicate per strain, so no per-protein statistics were available; the LptD/LptE decline, *lptC2* induction, Pal-Tol upregulation, and CCNA_01217 increase require replicated proteomics. [src: caulobacter_fur_lipida_loss]

The respiratory-chain protein measurements were made under standard growth conditions and do not directly establish carbon-source-specific abundance changes or measured flux distributions; the flux-based wiring interpretation remains partly inferential. [src: respiratory_chain_wiring]

## Related pages

- [[concepts/gene-essentiality]] — Proteomic expression was evaluated as a continuous predictor of knockout essentiality. [src: adp1_triple_essentiality]
- [[concepts/multi-omics-integration]] — Proteomics was compared with FBA, TnSeq, knockout, and growth evidence, and later exposed transcript–protein discordance in envelope remodeling; respiratory-chain proteomics further supports integrating abundance with fitness and model outputs. [src: adp1_triple_essentiality; caulobacter_fur_lipida_loss; respiratory_chain_wiring]
- [[summaries/adp1_triple_essentiality__REPORT]] — Source summary for the triple-essentiality concordance analysis.
- [[summaries/caulobacter_fur_lipida_loss__REPORT]] — Source summary for the Caulobacter Fur/lipid A-loss multi-omics analysis. [src: caulobacter_fur_lipida_loss]
- [[summaries/respiratory_chain_wiring__REPORT]] — Source summary for condition-specific respiratory-chain wiring in ADP1. [src: respiratory_chain_wiring]
