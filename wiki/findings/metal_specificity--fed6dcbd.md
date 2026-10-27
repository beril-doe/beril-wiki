---
type: "Finding"
description: "The Cochran-Mantel-Haenszel test comparing metal-specific vs general-sick core enrichment across organisms is statistically significant (p=0.011), indicating metal-specific genes are less core-enriched than general sick genes across organisms."
finding_id: "metal_specificity--fed6dcbd"
result: "observation"
source: "metal_specificity"
quantities: [{"value": "p=0.011", "what": "Cochran-Mantel-Haenszel test comparing core enrichment of metal-specific vs general-sick genes", "unit": "", "denominator": "", "scope": "across organisms"}]
caveat: "The report says excluding putatively essential genes biases all categories toward core enrichment, so the true baseline core fraction is likely lower than 81%, making the reported deltas conservative."
first_added: "2026-10-27"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Metal-specific genes are less core-enriched than general-sick genes

The Cochran-Mantel-Haenszel test comparing metal-specific vs general-sick core enrichment across organisms is statistically significant (p=0.011), indicating metal-specific genes are less core-enriched than general sick genes across organisms. [src: metal_specificity]

## Key figures

- **p=0.011**: Cochran-Mantel-Haenszel test comparing core enrichment of metal-specific vs general-sick genes (scope across organisms) [src: metal_specificity]

## Evidence

> **CMH test**: The Cochran-Mantel-Haenszel test comparing metal-specific vs general-sick core enrichment across organisms is statistically significant (p=0.011), confirming that metal-specific genes are less core-enriched than general sick genes across organisms. [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

The report says excluding putatively essential genes biases all categories toward core enrichment, so the true baseline core fraction is likely lower than 81%, making the reported deltas conservative. [src: metal_specificity]

> This biases all categories toward core enrichment — the true baseline core fraction is likely lower than 81%, making the reported deltas conservative. [src: metal_specificity]

## Other caveats in this report

- The metal-specific fraction was ~41% at a 2% sick-rate cutoff and ~67% at 10%. [src: metal_specificity]
- Seven of 31 metal-tested organisms were excluded because locusId formats did not match fitness-matrix indices. [src: metal_specificity]
- Included organisms represented 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report expects no systematic bias from the taxonomically diverse exclusions, but does not establish that empirically. [src: metal_specificity]
- The conservation analysis covered 22 organisms with pangenome links and distinguished pooled from organism-mean core fractions. [src: metal_specificity]
