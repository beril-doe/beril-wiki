---
type: "Finding"
description: "In 1,574 bacterial genera matched across the GTDB phylogeny and global MGnify MAG data, per-Mb Tier 1+2 metal-gene KO density was negatively associated with standardised Levins' niche breadth (\u03b2 = \u22120.021, SE = 0.0037, t = \u22125.63, p = 2.1\u00d710\u207b\u2078, FDR joint p = 6.4\u00d710\u207b\u2078, Pagel's \u03bb = 0.757, \u0394AIC = \u221229.4, r\u00b2 = 0.046)."
finding_id: "comprehensive_metal_ecology--84a388ca"
result: "observation"
source: "comprehensive_metal_ecology"
quantities: [{"value": "\u03b2 = \u22120.021", "what": "PGLS coefficient of metal-gene density on niche breadth", "unit": "", "denominator": "", "scope": "1,574 bacterial genera"}, {"value": "6.4\u00d710\u207b\u2078", "what": "FDR joint p-value", "unit": "", "denominator": "", "scope": ""}, {"value": "r\u00b2 = 0.046", "what": "variance explained", "unit": "", "denominator": "", "scope": ""}, {"value": "\u03bb = 0.757", "what": "Pagel's lambda", "unit": "", "denominator": "", "scope": ""}]
caveat: "In P1, metal-gene density explains only a small fraction of genus-level niche breadth variance (r\u00b2 = 0.046), with ecological breadth multidimensionally determined."
first_added: "2026-11-24"
source_hash: "3a3c00f14f9f661079f1855285d588dac32dfd6a5fef36e2729641e52137bbec"
---
# Metal-gene density negatively associated with bacterial niche breadth after phylogenetic control

In 1,574 bacterial genera matched across the GTDB phylogeny and global MGnify MAG data, per-Mb Tier 1+2 metal-gene KO density was negatively associated with standardised Levins' niche breadth (β = −0.021, SE = 0.0037, t = −5.63, p = 2.1×10⁻⁸, FDR joint p = 6.4×10⁻⁸, Pagel's λ = 0.757, ΔAIC = −29.4, r² = 0.046). [src: comprehensive_metal_ecology]

## Key figures

- **β = −0.021**: PGLS coefficient of metal-gene density on niche breadth (scope 1,574 bacterial genera) [src: comprehensive_metal_ecology]
- **6.4×10⁻⁸**: FDR joint p-value [src: comprehensive_metal_ecology]
- **r² = 0.046**: variance explained [src: comprehensive_metal_ecology]
- **λ = 0.757**: Pagel's lambda [src: comprehensive_metal_ecology]

## Evidence

> In 1,574 bacterial genera matched across the GTDB phylogeny and global MGnify MAG data, per-Mb Tier 1+2 metal-gene KO density is significantly negatively associated with standardised Levins' niche breadth (β = −0.021, SE = 0.0037, t = −5.63, p = 2.1×10⁻⁸, FDR joint p = 6.4×10⁻⁸, Pagel's λ = 0.757, ΔAIC = −29.4, r² = 0.046). [src: comprehensive_metal_ecology]

From the report [[summaries/comprehensive_metal_ecology__REPORT]].

## Caveat

In P1, metal-gene density explains only a small fraction of genus-level niche breadth variance (r² = 0.046), with ecological breadth multidimensionally determined. [src: comprehensive_metal_ecology]

> **r² = 0.046 in P1**: Metal-gene density explains a small fraction of genus-level niche breadth variance. Ecological breadth is multidimensionally determined. [src: comprehensive_metal_ecology]

## Other caveats in this report

- The report suggests that low power combined with a small effect size likely explains the non-significant archaeal replication. [src: comprehensive_metal_ecology]
- The report argues that the appropriate null model for the metal-gene signal is the constitutive housekeeping β (≈ −0.029 to −0.035), rather than zero. [src: comprehensive_metal_ecology]
- Three of the seven metal cofactor KOs were absent from the MGnify MAG dataset and contributed zero density, so the exploratory jackknife used only the four detectably represented KOs. [src: comprehensive_metal_ecology]
- The report classifies the named housekeeping controls as streamlining indicators rather than true-negative controls, requiring a valid negative control's per-Mb density not to scale with specialisation. [src: comprehensive_metal_ecology]
- The primary metal-gene coefficient is not distinguishable in overall magnitude from randomly selected conserved gene sets with equal coreness structure. [src: comprehensive_metal_ecology]
