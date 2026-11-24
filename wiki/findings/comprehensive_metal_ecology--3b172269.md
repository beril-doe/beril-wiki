---
type: "Finding"
description: "In the bacterial global MGnify MAG niche-breadth analysis, Cofactor Biosynthesis (7 KOs) has \u03b2 = \u22120.033, SE = 0.005, and FDR p = 5.2\u00d710\u207b\u2079."
finding_id: "comprehensive_metal_ecology--3b172269"
result: "observation"
source: "comprehensive_metal_ecology"
quantities: [{"value": "\u22120.033", "what": "cofactor biosynthesis \u03b2", "unit": "", "denominator": "", "scope": "7 KOs"}, {"value": "5.2\u00d710\u207b\u2079", "what": "FDR p", "unit": "", "denominator": "", "scope": ""}]
caveat: "Three of the seven metal cofactor KOs were absent from the MGnify MAG dataset and contributed zero density, so the exploratory jackknife used only the four detectably represented KOs."
first_added: "2026-11-24"
source_hash: "3a3c00f14f9f661079f1855285d588dac32dfd6a5fef36e2729641e52137bbec"
---
# Cofactor biosynthesis genes carry the strongest metal-gene niche signal

In the bacterial global MGnify MAG niche-breadth analysis, Cofactor Biosynthesis (7 KOs) has β = −0.033, SE = 0.005, and FDR p = 5.2×10⁻⁹. [src: comprehensive_metal_ecology]

## Key figures

- **−0.033**: cofactor biosynthesis β (scope 7 KOs) [src: comprehensive_metal_ecology]
- **5.2×10⁻⁹**: FDR p [src: comprehensive_metal_ecology]

## Evidence

> | Cofactor Biosynthesis | 7 | **−0.033** | 0.005 | 5.2×10⁻⁹ | **strongest** | [src: comprehensive_metal_ecology]

From the report [[summaries/comprehensive_metal_ecology__REPORT]].

## Caveat

Three of the seven metal cofactor KOs were absent from the MGnify MAG dataset and contributed zero density, so the exploratory jackknife used only the four detectably represented KOs. [src: comprehensive_metal_ecology]

> Of the seven cofactor KOs, three were absent from the MGnify MAG dataset and contributed zero density; the jackknife was performed on the four KOs with detectable representation. [src: comprehensive_metal_ecology]

## Other caveats in this report

- The report suggests that low power combined with a small effect size likely explains the non-significant archaeal replication. [src: comprehensive_metal_ecology]
- The report argues that the appropriate null model for the metal-gene signal is the constitutive housekeeping β (≈ −0.029 to −0.035), rather than zero. [src: comprehensive_metal_ecology]
- The report classifies the named housekeeping controls as streamlining indicators rather than true-negative controls, requiring a valid negative control's per-Mb density not to scale with specialisation. [src: comprehensive_metal_ecology]
- The primary metal-gene coefficient is not distinguishable in overall magnitude from randomly selected conserved gene sets with equal coreness structure. [src: comprehensive_metal_ecology]
- The AusMicrobiome P5 analysis is not an independent replication because all 482 genera are a subset of P1 and the density predictor is identical. [src: comprehensive_metal_ecology]
