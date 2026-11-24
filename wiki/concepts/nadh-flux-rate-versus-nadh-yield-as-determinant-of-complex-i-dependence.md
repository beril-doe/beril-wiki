---
type: "Concept"
description: "Covers whether the rate or concentration of NADH production, rather than total NADH yield per carbon, explains dependence on Complex I across substrates, including stoichiometric evidence and untested predictions."
sources: ["summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# NADH flux rate versus NADH yield as determinant of Complex I dependence

Covers whether the rate or concentration of NADH production, rather than total NADH yield per carbon, explains dependence on Complex I across substrates, including stoichiometric evidence and untested predictions.

## The yield paradox

NADH yield per carbon does not predict Complex I dependence in ADP1. Quinate gives fewer NADH per carbon (0.57) than glucose (1.50), yet Complex I is more essential on quinate. [src: discoveries] The respiratory chain report also lists acetate at 1.50 NADH per carbon. [src: respiratory_chain_wiring]

| Substrate | Total NADH | NADH/carbon | Production pattern | Complex I growth |
|---|---|---|---|---|
| Quinate | 4 | 0.57 | Concentrated TCA burst | 0.37 (essential) [src: respiratory_chain_wiring] |
| Glucose | 9 | 1.50 | Distributed (ED + TCA) | 1.44 (dispensable) [src: respiratory_chain_wiring] |
| Acetate | 3 | 1.50 | All through TCA | 0.49 (defect) [src: respiratory_chain_wiring] |
| Lactate | 5 | 1.67 | Pyruvate + TCA | 0.77 (mild) [src: respiratory_chain_wiring] |

TCA is tricarboxylic acid and ED is the Entner-Doudoroff pathway.

## Flux-rate explanation

The reports resolve the paradox by NADH flux rate. Aromatic ring cleavage by the β-ketoadipate pathway yields succinyl-CoA and acetyl-CoA together. Both enter the TCA cycle at once, which creates a concentrated NADH burst that exceeds the reoxidation capacity of NDH-2. [src: discoveries, respiratory_chain_wiring] The aromatic catabolism report likewise says full TCA oxidation of these products generates NADH at multiple steps and needs Complex I under high flux. [src: aromatic_catabolism_network] Glucose spreads NADH production across ED steps and the TCA cycle, which stays within NDH-2 capacity. [src: discoveries, respiratory_chain_wiring]

The proteomic data fit a passive model. Under standard growth, the three NADH dehydrogenases are expressed at similar levels. [src: respiratory_chain_wiring] The report gives the spread as only 1.4 units [src: respiratory_chain_wiring]:

- Complex I: mean 27.6 (66th percentile). [src: respiratory_chain_wiring]
- NDH-2: 27.0 (59th percentile). [src: respiratory_chain_wiring]
- ACIAD3522: 26.2 (48th percentile). [src: respiratory_chain_wiring]
- Genome median: 26.4. [src: respiratory_chain_wiring]

The report states that NDH-2 is not repressed but constitutively co-expressed with Complex I. It interprets the wiring as passive and flux-based rather than an active transcriptional switch. All three dehydrogenases are present, and the one that becomes limiting depends on the carbon source's NADH flux rate. [src: respiratory_chain_wiring]

## Cross-species support

The aromatic catabolism report concludes that Complex I dependency tracks high-NADH substrates, not aromatics specifically. [src: aromatic_catabolism_network] Its cross-species data show Complex I is essential on aromatics, acetate and succinate, which generate high TCA flux. [src: aromatic_catabolism_network] Per-condition Fitness Browser analysis finds the largest Complex I defects relative to background on acetate (-1.55) and succinate (-1.39). [src: aromatic_catabolism_network] This **supports** flux over aromatic identity. The report proposes that the principle should apply to any substrate whose catabolism produces concentrated reducing equivalents. [src: respiratory_chain_wiring]

## Untested predictions

The flux-rate hypothesis predicts higher NADH/NAD⁺ ratios in quinate-grown ADP1 cells than in glucose-grown cells, and the report proposes metabolomics as a direct test. [src: respiratory_chain_wiring] The report also proposes testing whether ADP1 upregulates Complex I on aromatic substrates and NDH-2 on glucose, by reanalyzing respiratory chain proteins in the Stuani et al. (2014) quinate-versus-succinate proteomics. [src: respiratory_chain_wiring]

## Caveats

The stoichiometry uses theoretical pathway biochemistry, not measured flux distributions. [src: respiratory_chain_wiring] The acetate case also shows that yield alone is not the whole story. Acetate has the same NADH per carbon as glucose (1.50) but shows a Complex I defect, while glucose does not. [src: respiratory_chain_wiring]

## Open Directions

- Measure NADH/NAD⁺ ratios in quinate- and glucose-grown ADP1 by metabolomics, to test the predicted higher ratio on quinate.
- Reanalyze respiratory chain proteins in the Stuani et al. (2014) proteomics, to test whether the wiring is regulated or passive.
- Replace the theoretical stoichiometry with measured flux distributions, for example from isotope tracing, to test the concentrated-burst assumption.
- Test other substrates predicted to give concentrated reducing equivalents, to check whether the principle generalizes.

See also [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].
