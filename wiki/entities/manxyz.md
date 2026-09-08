---
type: Gene_Or_Pathway
description: Mannose/glucosamine PTS transporter linked to SNIPE phage defense
sources:
- id: discoveries
  resource: ../summaries/discoveries.md
  title: discoveries
- id: snipe_defense_system
  resource: ../summaries/snipe_defense_system__REPORT.md
  title: snipe defense system
title: ManXYZ
---
# ManXYZ

## Identity

**Canonical name:** ManXYZ. **Known alias:** ManX-family PTS domain. **Stable external identifier:** No stable external identifier was reported in the source. [^discoveries]

ManXYZ is a phosphotransferase-system transporter associated with mannose and glucosamine uptake. [^discoveries] The new SNIPE analysis **supports** this assignment and **contradicts** a fructose-specific interpretation: in 168 *Escherichia coli* K-12 experiments, *manX*, *manY*, and *manZ* showed fitness values of -2.75, -3.00, and -2.74 on D-mannose, versus -0.22, +0.15, and -0.07 on D-fructose; *fruA* was -0.06 on D-mannose and -1.44 on D-fructose. [^snipe_defense_system]

## Evidence from discoveries

Fitness Browser measurements in *Escherichia coli* K-12 showed that ManXYZ knockouts had a fitness effect of **-3.93** on D-mannose and **-2.75** on D-glucosamine. [^discoveries]

The same knockouts had positive fitness effects of **+0.18 to +0.66** on D-fructose, contradicting the interpretation that ManXYZ is a fructose transporter. [^discoveries] The new measurements **refine** this substrate comparison: the strongest reported defects were on D-glucosamine, with *manX*, *manY*, and *manZ* values of -3.79, -2.79, and -3.63, and on D-mannose, with values of -2.75, -3.00, and -2.74. [^snipe_defense_system]

ManXYZ’s three genes also showed cofitness correlations of 0.851 for *manX*↔*manZ*, 0.705 for *manX*↔*manY*, and 0.725 for *manY*↔*manZ*, **supporting** their operation as a single operon. [^snipe_defense_system] This transporter function is relevant to [snipe-defense-system](snipe-defense-system.md): SNIPE is proposed to cleave phage DNA entering through the ManYZ pore, potentially retaining mannose transport while avoiding the metabolic cost of transporter loss. [^snipe_defense_system]

A full two-domain SNIPE protein with **129 experiments** was identified in *Methanococcus maripaludis* JJ. [^discoveries]

*Klebsiella* had **1 DUF4041 annotation across 3 proteins** and **4,619 PTS_EIIC annotations**, making it the only PhageFoundry species with both SNIPE and the ManX-family PTS domain in this analysis. [^discoveries] The new report **refines** this co-occurrence: it found 28 mannose PTS IID/ManZ proteins and 1 mannose PTS IIA/ManX protein in the corresponding genome browser, but no *Klebsiella* SNIPE or ManXYZ fitness data were available. [^snipe_defense_system]

## Related pages

The transporter evidence comes from the [kescience-fitnessbrowser](kescience-fitnessbrowser.md) resource and is interpreted using *Escherichia coli* K-12 data from [escherichia-coli](escherichia-coli.md). [^discoveries]

The associated defense-system comparison connects ManXYZ to [snipe-defense-system](snipe-defense-system.md) and to the broader [environmental-resistome](../concepts/environmental-resistome.md) synthesis. [^discoveries]

See the complete cross-project account in [discoveries](../summaries/discoveries.md) and [snipe_defense_system__REPORT](../summaries/snipe_defense_system__REPORT.md). [^discoveries][^snipe_defense_system]

[^discoveries]: [discoveries](../summaries/discoveries.md)
[^snipe_defense_system]: [snipe defense system](../summaries/snipe_defense_system__REPORT.md)
