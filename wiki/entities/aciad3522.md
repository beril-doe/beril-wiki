---
type: "Gene_Or_Pathway"
description: "ADP1 NADH-FMN oxidoreductase that is lethal when disrupted on acetate and of uncertain respiratory role."
sources: ["summaries/discoveries.md", "summaries/respiratory_chain_wiring__REPORT.md"]
aliases: ["NADH-FMN oxidoreductase"]
---
# ACIAD3522

ACIAD3522 is an NADH-FMN oxidoreductase in [[entities/acinetobacter-baylyi-adp1]] (ADP1). [src: discoveries] Its disruption is nearly lethal on acetate but harmless on quinate and glucose, and its respiratory role is unclear. [src: discoveries, respiratory_chain_wiring] The evidence is a growth-ratio matrix, a flux balance analysis (FBA) prediction and an expression value. [src: discoveries, respiratory_chain_wiring]

## Key facts

- ACIAD3522 has a growth ratio of 0.013 on acetate, which is essentially lethal. It shows no defect on quinate (1.39) or glucose (1.39). [src: discoveries]
- The report table lists it as a one-subunit enzyme that does not pump protons: 1.39 on quinate (dispensable), 1.39 on glucose (dispensable) and 0.013 on acetate (lethal). [src: respiratory_chain_wiring]
- This is the largest condition-specific effect of any single gene in the 2,034-gene growth matrix. [src: discoveries]
- Under standard growth conditions its protein expression is 26.2 (48th percentile). [src: respiratory_chain_wiring] That is similar to the other NADH dehydrogenases: Complex I at 27.6 (66th percentile) and NDH-2 at 27.0 (59th percentile). The genome median is 26.4. [src: respiratory_chain_wiring]

## Role in acetate growth

On acetate, ADP1 requires Complex I, cytochrome bo3, ACIAD3522 and further respiratory components, so acetate is the most demanding carbon source. [src: respiratory_chain_wiring] See [[entities/cytochrome-bo3-oxidase]] and [[concepts/condition-dependent-respiratory-chain-configuration]].

The biological role is unknown. The extreme acetate specificity suggests an NADH-linked reaction that is uniquely required for acetate catabolism. [src: discoveries] The acetate lethality and the FMN cofactor also point to a specific role in acetate catabolism that deserves further investigation. [src: respiratory_chain_wiring]

## Caveats

- FBA predicts zero flux through ACIAD3522 on all conditions. [src: discoveries] This does not match its strong acetate phenotype. [src: discoveries]
- ACIAD3522 may not be a true respiratory NADH dehydrogenase. An NADH-FMN oxidoreductase annotation could indicate other metabolic functions. [src: respiratory_chain_wiring]
- The report proposes characterizing it to decide whether it is a respiratory NADH dehydrogenase or a metabolic enzyme. [src: respiratory_chain_wiring]

See also [[summaries/discoveries]], [[summaries/respiratory_chain_wiring__REPORT]] and [[concepts/fitness-modules-essential-genes-and-condition-specific-gene-function]].
