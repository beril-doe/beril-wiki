---
type: "Finding"
description: "Metal-specific genes are 1.64x more likely to match metal-resistance keywords (efflux, transporter, metal, CDF, siderophore, etc.) than general sick genes (12.2% vs 7.8%, Fisher exact OR=1.64, p=2.4e-8)."
finding_id: "metal_specificity--94cbeb4a"
result: "observation"
source: "metal_specificity"
quantities: [{"value": "12.2%", "what": "metal-specific genes matching metal-resistance keywords", "unit": "", "denominator": "", "scope": ""}, {"value": "7.8%", "what": "general-sick genes matching metal-resistance keywords", "unit": "", "denominator": "", "scope": ""}, {"value": "1.64", "what": "Fisher exact odds ratio", "unit": "", "denominator": "", "scope": ""}, {"value": "2.4e-8", "what": "Fisher exact p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "The report's prose on general-stress keywords (11.5% vs 13.7%) points the opposite way from its table, which gives 13.7% to metal-specific and 11.5% to general sick genes."
first_added: "2026-10-27"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Metal-specific genes are enriched for metal-resistance function keywords

Metal-specific genes are 1.64x more likely to match metal-resistance keywords (efflux, transporter, metal, CDF, siderophore, etc.) than general sick genes (12.2% vs 7.8%, Fisher exact OR=1.64, p=2.4e-8). [src: metal_specificity]

## Key figures

- **12.2%**: metal-specific genes matching metal-resistance keywords [src: metal_specificity]
- **7.8%**: general-sick genes matching metal-resistance keywords [src: metal_specificity]
- **1.64**: Fisher exact odds ratio [src: metal_specificity]
- **2.4e-8**: Fisher exact p-value [src: metal_specificity]

## Evidence

> Metal-specific genes are 1.64x more likely to match metal-resistance keywords (efflux, transporter, metal, CDF, siderophore, etc.) than general sick genes (12.2% vs 7.8%, Fisher exact OR=1.64, p=2.4e-8). [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

The report's prose on general-stress keywords (11.5% vs 13.7%) points the opposite way from its table, which gives 13.7% to metal-specific and 11.5% to general sick genes. [src: metal_specificity]

> Conversely, general sick genes show slightly higher enrichment for general stress keywords (DNA repair, cell wall, chaperone, etc.) at 11.5% vs 13.7%. [src: metal_specificity]

## Other caveats in this report

- The metal-specific fraction was ~41% at a 2% sick-rate cutoff and ~67% at 10%. [src: metal_specificity]
- Seven of 31 metal-tested organisms were excluded because locusId formats did not match fitness-matrix indices. [src: metal_specificity]
- Included organisms represented 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report expects no systematic bias from the taxonomically diverse exclusions, but does not establish that empirically. [src: metal_specificity]
- The conservation analysis covered 22 organisms with pangenome links and distinguished pooled from organism-mean core fractions. [src: metal_specificity]
