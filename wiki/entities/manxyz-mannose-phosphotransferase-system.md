---
type: "Gene_Or_Pathway"
description: "The Escherichia coli mannose/glucosamine PTS (manX, manY, manZ operon) whose ManYZ pore is the phage lambda entry receptor."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["ManXYZ", "ManYZ", "manXYZ", "mannose PTS"]
---
# ManXYZ mannose phosphotransferase system

This page covers the ManXYZ mannose phosphotransferase system (also ManYZ, mannose PTS). The report interprets its ManYZ pore as a mannose/glucosamine-specific transporter that serves as the phage lambda entry receptor. [src: snipe_defense_system] Fitness Browser knockout data from the Escherichia coli K-12 Keio collection show severe defects on D-mannose and D-glucosamine and none on D-fructose. [src: discoveries] The operon and receptor interpretations are the reports' own. See also [[entities/escherichia-coli]] and [[entities/bacteriophage-lambda]].

## Key facts

- manX encodes EIIAB (locus b1817), manY encodes EIIC (Keio locus JW1807) and manZ encodes EIID (Keio locus JW1808). [src: snipe_defense_system]
- The report attributes specific fitness defects on D-mannose and D-glucosamine to manX, citing Price et al. 2018. [src: snipe_defense_system]

## Substrate specificity from fitness data

ManXYZ knockouts are severely defective on D-mannose and D-glucosamine but not on D-fructose. [src: discoveries] In 168 Keio experiments, the fitness on D-mannose was -3.93 and on D-glucosamine -2.75. Fructose fitness ranged from +0.18 to +0.66, so ManXYZ is dispensable there. [src: discoveries] The report reads this substrate separation as confirming that ManYZ is mannose/glucosamine-specific rather than fructose-specific. [src: snipe_defense_system] For more detail see [[concepts/substrate-specificity-of-the-mannose-pts-manxyz-from-genome-wide-fitness]].

Per-gene summaries across the 168 experiments:

| Gene | Worst fitness | Average fitness | Conditions fit < -1 | Conditions fit < -2 |
|---|---|---|---|---|
| manX | -3.93 | -0.249 | 6 | 4 [src: snipe_defense_system] |
| manY | -3.82 | -0.171 | 10 | 4 [src: snipe_defense_system] |
| manZ | -4.14 | -0.082 | 7 | 4 [src: snipe_defense_system] |

Mean fitness with sole carbon sources was as follows. On D-glucosamine it was -3.79 for manX, -2.79 for manY and -3.63 for manZ. [src: snipe_defense_system] On D-mannose it was -2.75 for manX, -3.00 for manY and -2.74 for manZ. [src: snipe_defense_system]

The three genes are co-fitness correlated: manX↔manZ r=0.851, manX↔manY r=0.705 and manY↔manZ r=0.725. The report reads this as confirming a single operon. [src: snipe_defense_system]

## Annotation conflict

UniProt annotates ManX as a "fructose-specific" PTS component. [src: snipe_defense_system] The fitness results contradict the UniProt annotation "fructose import across plasma membrane" (GO:0005354, Gene Ontology) for ManX. [src: discoveries]

## Phage lambda receptor role

In the cited Burmeister study (2021), manY loss gave zero phage lambda growth after 24h. It also caused loss of mannose transport and a partial glucose transport defect. [src: snipe_defense_system] manZ loss gave a 5 orders of magnitude reduction in phage growth, with the same metabolic cost as manY. [src: snipe_defense_system] See [[concepts/phage-resistance-versus-metabolic-cost-trade-off-at-receptor-transporters]].

## Distribution in PhageFoundry genomes

PF02378 / PTS_EIIC (ManY family) has 4,619 annotations in PhageFoundry Klebsiella, 891 in Acinetobacter, 1,067 in Pseudomonas aeruginosa and 260 in Pseudomonas viridiflava. [src: snipe_defense_system] PF00358 / PTS_EIIA_1 (ManX family) has 571 annotations in Klebsiella and 0 in the other three. [src: snipe_defense_system] Klebsiella has 28 proteins with mannose PTS IID (ManZ) eggNOG annotations but 1 protein with a mannose PTS IIA (ManX) eggNOG annotation. [src: snipe_defense_system] See [[entities/klebsiella]].

The report finds that SNIPE co-occurring with its target mannose transporter is consistent with SNIPE defending ManYZ pores that provide a phage entry route. [src: snipe_defense_system] See [[concepts/adsorption-receptors-versus-defense-systems-as-determinants-of-phage-host-range]].
