---
type: "Concept"
description: "Whether loss of a phage-entry transporter buys resistance at a metabolic price, and whether a defense system that acts at the pore can avoid that price; stops at the ManYZ/lambda example."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
---
# Phage resistance versus metabolic cost trade-off at receptor transporters

This page asks whether losing a phage-entry transporter buys resistance at a metabolic price. The ManYZ mannose transporter and phage lambda are the worked example. [src: snipe_defense_system, discoveries] The evidence has two parts. Published knockout phenotypes and local Fitness Browser scores report the resistance and the cost. [src: snipe_defense_system, discoveries] The SNIPE report concludes that a defense acting at the pore avoids the price. [src: snipe_defense_system] See also [[entities/bacteriophage-lambda]], [[entities/snipe]] and [[entities/manxyz-mannose-phosphotransferase-system]].

## Resistance by receptor loss

Knockouts of the ManYZ pore protect against phage lambda. The phage phenotypes come from Burmeister et al. 2021 (PMID 34032565), which used the Keio collection of Escherichia coli BW25113. These studies are not from the KBase Data Lakehouse. [src: snipe_defense_system]

- manY (EIIC), Keio locus JW1807: zero phage growth after 24h, with loss of mannose transport and a partial glucose transport defect. [src: snipe_defense_system]
- manZ (EIID), Keio locus JW1808: a 5 orders of magnitude reduction in phage growth, with the same metabolic cost as manY. [src: snipe_defense_system]

In coevolution experiments, man mutants sweep to >95% frequency under phage pressure. They decline sharply when phages evolve alternative injection mechanisms. [src: snipe_defense_system]

A genomic pattern fits receptor loss. Lambdavirus 411_P1 infects only 1/188 strains (0.5%), against 43.4% for Myoviridae. The report calls this consistent with widespread ManYZ receptor loss making lambda infection rare. [src: discoveries] This is consistency, not a direct test.

## The metabolic cost

Fitness Browser data (168 experiments, E. coli K-12 Keio collection) show severe ManXYZ knockout defects on D-mannose (fit = -3.93) and D-glucosamine (fit = -2.75). [src: discoveries] The report reads this separation as showing that ManYZ is a mannose/glucosamine-specific transporter, consistent with its role as the lambda entry receptor. [src: snipe_defense_system] For more, see [[concepts/substrate-specificity-of-the-mannose-pts-manxyz-from-genome-wide-fitness]].

## Defense at the pore

SNIPE targets the ManYZ pore, the mannose transporter that lambda uses for DNA injection, and not a general sugar transporter. [src: discoveries] The SNIPE report states that SNIPE constitutively localizes to the inner membrane and cleaves phage DNA as it passes through the pore. [src: snipe_defense_system] It acts at the adsorption/injection step. [src: snipe_defense_system]

From this the report concludes that SNIPE resolves the trade-off. [src: snipe_defense_system] It says SNIPE-bearing strains keep full transporter function and gain the resistance benefit of man knockouts without the metabolic cost. [src: snipe_defense_system] It also reads the co-occurrence of SNIPE and the mannose transporter in one organism as consistent with SNIPE defending pores that offer a phage entry route. [src: snipe_defense_system] For the wider context, see [[concepts/adsorption-receptors-versus-defense-systems-as-determinants-of-phage-host-range]].

## Open Directions

- Measure growth on D-mannose and D-glucosamine in SNIPE-bearing strains against isogenic man knockouts. This would test directly whether SNIPE carries no metabolic cost.
- Test for SNIPE across the strains behind the 1/188 lambda infection figure. This would check whether ManYZ loss and SNIPE presence are alternative routes to lambda resistance.
- Test whether phages that evolve alternative injection mechanisms also escape SNIPE. This would show whether pore defense is more durable than receptor loss.
