---
type: "Organism"
description: "Enterobacterial phage that enters Escherichia coli through the ManYZ pore, used as the model for the SNIPE and man-mutant resistance trade-off."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["Lambdavirus", "phage lambda"]
---
# Bacteriophage lambda

This page covers bacteriophage lambda, also called Lambdavirus or phage lambda. Lambdavirus 411_P1 infects only 1/188 Escherichia coli strains (0.5%). [src: discoveries] The evidence combines a host-range survey with published knockout phenotypes in [[entities/escherichia-coli]]. The survey result is an interpretation of receptor loss, not a direct test of it. [src: snipe_defense_system]

## Key facts

- Lambdavirus 411_P1 (phage lambda) infects 1/188 strains (0.5%), versus 43.4% for Myoviridae. [src: discoveries]
- The one infected strain is NILS06. This is the lowest infection rate of any phage in the dataset. [src: snipe_defense_system]
- The report reads this as consistent with widespread ManYZ variation or loss conferring near-universal lambda resistance across diverse E. coli strains. [src: snipe_defense_system] See [[concepts/adsorption-receptors-versus-defense-systems-as-determinants-of-phage-host-range]].

## Receptor knockouts and the resistance trade-off

The lambda phenotypes come from Burmeister et al. 2021 (PMID 34032565). They use the E. coli BW25113 Keio collection. [src: snipe_defense_system] See [[entities/manxyz-mannose-phosphotransferase-system]] for the transporter.

- Deleting manY (EIIC, Keio locus JW1807) gives zero phage growth after 24h. It also causes loss of mannose transport and a partial glucose transport defect. [src: snipe_defense_system]
- Deleting manZ (EIID, Keio locus JW1808) reduces phage growth by 5 orders of magnitude. The metabolic cost is the same as for manY. [src: snipe_defense_system]
- In coevolution experiments, man mutants sweep to >95% frequency under phage pressure. They decline sharply when phages evolve alternative injection mechanisms. [src: snipe_defense_system]

See [[concepts/phage-resistance-versus-metabolic-cost-trade-off-at-receptor-transporters]], [[summaries/snipe_defense_system__REPORT]] and [[summaries/discoveries]].
