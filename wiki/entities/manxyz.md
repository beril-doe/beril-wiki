---
type: "Gene_Or_Pathway"
description: "Mannose/glucosamine PTS transporter linked to SNIPE phage defense"
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
---
# ManXYZ

## Identity

**Canonical name:** ManXYZ. **Known alias:** ManX-family PTS domain. **Stable external identifier:** No stable external identifier was reported in the source. [src: discoveries]

ManXYZ is a phosphotransferase-system transporter associated with mannose and glucosamine uptake. [src: discoveries] The new SNIPE analysis **supports** this assignment and **contradicts** a fructose-specific interpretation: in 168 *Escherichia coli* K-12 experiments, *manX*, *manY*, and *manZ* showed fitness values of -2.75, -3.00, and -2.74 on D-mannose, versus -0.22, +0.15, and -0.07 on D-fructose; *fruA* was -0.06 on D-mannose and -1.44 on D-fructose. [src: snipe_defense_system]

## Evidence from discoveries

Fitness Browser measurements in *Escherichia coli* K-12 showed that ManXYZ knockouts had a fitness effect of **-3.93** on D-mannose and **-2.75** on D-glucosamine. [src: discoveries]

The same knockouts had positive fitness effects of **+0.18 to +0.66** on D-fructose, contradicting the interpretation that ManXYZ is a fructose transporter. [src: discoveries] The new measurements **refine** this substrate comparison: the strongest reported defects were on D-glucosamine, with *manX*, *manY*, and *manZ* values of -3.79, -2.79, and -3.63, and on D-mannose, with values of -2.75, -3.00, and -2.74. [src: snipe_defense_system]

ManXYZ’s three genes also showed cofitness correlations of 0.851 for *manX*↔*manZ*, 0.705 for *manX*↔*manY*, and 0.725 for *manY*↔*manZ*, **supporting** their operation as a single operon. [src: snipe_defense_system] This transporter function is relevant to [[entities/snipe-defense-system]]: SNIPE is proposed to cleave phage DNA entering through the ManYZ pore, potentially retaining mannose transport while avoiding the metabolic cost of transporter loss. [src: snipe_defense_system]

A full two-domain SNIPE protein with **129 experiments** was identified in *Methanococcus maripaludis* JJ. [src: discoveries]

*Klebsiella* had **1 DUF4041 annotation across 3 proteins** and **4,619 PTS_EIIC annotations**, making it the only PhageFoundry species with both SNIPE and the ManX-family PTS domain in this analysis. [src: discoveries] The new report **refines** this co-occurrence: it found 28 mannose PTS IID/ManZ proteins and 1 mannose PTS IIA/ManX protein in the corresponding genome browser, but no *Klebsiella* SNIPE or ManXYZ fitness data were available. [src: snipe_defense_system]

## Related pages

The transporter evidence comes from the [[entities/kescience-fitnessbrowser]] resource and is interpreted using *Escherichia coli* K-12 data from [[entities/escherichia-coli]]. [src: discoveries]

The associated defense-system comparison connects ManXYZ to [[entities/snipe-defense-system]] and to the broader [[concepts/environmental-resistome]] synthesis. [src: discoveries]

See the complete cross-project account in [[summaries/discoveries]] and [[summaries/snipe_defense_system__REPORT]]. [src: discoveries; snipe_defense_system]
