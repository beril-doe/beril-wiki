---
type: "Concept"
description: "Covers how which respiratory components (NADH dehydrogenases, terminal oxidases, SDH) are required varies by carbon source in a bacterium, and why; stops short of general cross-species claims."
sources: ["summaries/discoveries.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Condition-dependent respiratory chain configuration

In *Acinetobacter baylyi* ADP1 ([[entities/acinetobacter-baylyi-adp1]]), the respiratory components that growth requires differ by carbon source. The reports read this as qualitatively different wiring per substrate, not a quantitative gradient. The evidence is from one organism, and the authors caution that the pattern may be species-specific. [src: discoveries, respiratory_chain_wiring]

## Condition-specific requirements

Each of ADP1's 8 carbon sources needs a distinct set of respiratory-chain components. [src: discoveries] The branched chain has 62 genes across 8 subsystems. The report calls the differences qualitative, not a quantitative gradient. [src: respiratory_chain_wiring, discoveries] It describes the first systematic demonstration of this in a single bacterium. [src: respiratory_chain_wiring] It also reads the branching as functional specialization by substrate, not just structural redundancy. [src: respiratory_chain_wiring]

|---|---|---|
| Quinate | Complex I only [src: discoveries, respiratory_chain_wiring] | Cyt bo3, Cyt bd, SDH, all others [src: respiratory_chain_wiring] |
| Acetate | Complex I, cyt bo3, ACIAD3522 and more; the most demanding [src: discoveries, respiratory_chain_wiring] | None [src: respiratory_chain_wiring] |
| Glucose | No specific component [src: discoveries, respiratory_chain_wiring] | All, from full redundancy [src: respiratory_chain_wiring] |
| Lactate | Cyt bo3 [src: respiratory_chain_wiring] | Complex I (mild), Cyt bd [src: respiratory_chain_wiring] |
| Urea | Everything; generally demanding [src: respiratory_chain_wiring] | None [src: respiratory_chain_wiring] |

## The three NADH dehydrogenases

ADP1 has three parallel NADH dehydrogenases with distinct condition profiles. [src: respiratory_chain_wiring] The report reads their non-overlapping requirements as metabolic division of labor. [src: respiratory_chain_wiring, discoveries] See [[entities/respiratory-complex-i-nadh-ubiquinone-oxidoreductase]] and [[entities/aciad3522]].

- Complex I (NDH-1) has 13 subunits and pumps 4 H⁺/NADH. Its growth ratios are 0.37 on quinate (essential), 1.44 on glucose (dispensable) and 0.49 on acetate (defect). [src: respiratory_chain_wiring]
- ACIAD3522 (NADH-FMN oxidoreductase) has 1 subunit and does not pump protons. Its growth ratios are 1.39 on quinate, 1.39 on glucose (both dispensable) and 0.013 on acetate (lethal). [src: respiratory_chain_wiring]
- The report describes Complex I as the high-capacity primary system and NDH-2 as a low-capacity backup. [src: respiratory_chain_wiring] See [[entities/alternative-nadh-dehydrogenase-ndh-2]].

## Why: flux, not regulation

Proteomics shows all three dehydrogenases expressed at similar levels under standard conditions. Complex I averages 27.6 (66th percentile), NDH-2 27.0 (59th) and ACIAD3522 26.2 (48th). All lie within 1.4 units of each other around the genome median of 26.4. [src: discoveries] The report therefore concludes that the cell does not switch configurations by regulating dehydrogenase expression. All three run at once, and the limiting one depends on the NADH flux from the carbon source. [src: discoveries, respiratory_chain_wiring] It calls this a passive, flux-based system, not an active regulatory switch. [src: discoveries, respiratory_chain_wiring]

- Quinate: aromatic ring cleavage feeds a TCA (tricarboxylic acid) burst, so Complex I is the bottleneck. Cyt bo3 and cyt bd are dispensable because NADH reoxidation, not terminal oxidation, limits growth. [src: respiratory_chain_wiring]
- Acetate: direct TCA entry gives continuous NADH production. This needs all available dehydrogenases, with cyt bo3 as the primary terminal oxidase. [src: respiratory_chain_wiring]
- Rate versus yield: quinate has the lower NADH yield but needs Complex I more than glucose does. The report resolves this by NADH flux rate, a concentrated burst against distributed production. [src: respiratory_chain_wiring] See [[concepts/nadh-flux-rate-versus-nadh-yield-as-determinant-of-complex-i-dependence]] and [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].

## Caveats

- Of the respiratory-chain genes, 36 have growth data and 26 do not. The missing ones include NDH-2 and several ATP (adenosine triphosphate) synthase subunits. [src: respiratory_chain_wiring]
- ACIAD3522 may not be a respiratory NADH dehydrogenase, because an NADH-FMN oxidoreductase annotation could mean other metabolic functions. [src: respiratory_chain_wiring]
- The wiring may be species-specific rather than a general rule. [src: respiratory_chain_wiring]

## Open Directions

- Measure NADH flux or the NADH/NAD⁺ ratio directly on quinate, acetate and glucose. This would test the flux explanation, which so far rests on inference.
- Obtain growth data for NDH-2 and the ATP synthase subunits. This would fill the 26-gene gap.
- Test whether ACIAD3522 oxidizes NADH into the quinone pool. This would show whether it is a respiratory enzyme.
- Repeat the carbon-source deletion screen in another organism that has both Complex I and NDH-2. This would test the species-specificity caveat.
