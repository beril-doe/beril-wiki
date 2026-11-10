---
type: "Finding"
description: "Of the 7,609 metal-important gene records with fitness matrix data across 24 organisms, 4,177 (54.9%) are metal-specific, showing significant fitness defects under metal stress but a <5% sick rate across 5,945 non-metal experiments."
finding_id: "metal_specificity--0f40573a"
result: "observation"
source: "metal_specificity"
quantities: [{"value": "4,177", "what": "metal-specific gene records", "unit": "records", "denominator": "7,609 metal-important gene records with fitness matrix data", "scope": "24 organisms"}, {"value": "54.9%", "what": "fraction classified metal-specific", "unit": "", "denominator": "7,609 gene records", "scope": "<5% sick rate threshold"}, {"value": "5,945", "what": "non-metal experiments used to define the sick rate", "unit": "experiments", "denominator": "", "scope": ""}]
caveat: "7 organisms and 5,229 gene records (40.7% gene attrition) were excluded due to locusId format mismatches, including Keio, MR1 and ANA3."
first_added: "2026-10-27"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Just over half of metal-important genes are metal-specific

Of the 7,609 metal-important gene records with fitness matrix data across 24 organisms, 4,177 (54.9%) are metal-specific, showing significant fitness defects under metal stress but a <5% sick rate across 5,945 non-metal experiments. [src: metal_specificity]

## Key figures

- **4,177 records**: metal-specific gene records (denominator 7,609 metal-important gene records with fitness matrix data; scope 24 organisms) [src: metal_specificity]
- **54.9%**: fraction classified metal-specific (denominator 7,609 gene records; scope <5% sick rate threshold) [src: metal_specificity]
- **5,945 experiments**: non-metal experiments used to define the sick rate [src: metal_specificity]

## Evidence

> Of the 7,609 metal-important gene records with fitness matrix data across 24 organisms, 4,177 (54.9%) are metal-specific — they show significant fitness defects under metal stress but a <5% sick rate across 5,945 non-metal experiments. [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

7 organisms and 5,229 gene records (40.7% gene attrition) were excluded due to locusId format mismatches, including Keio, MR1 and ANA3. [src: metal_specificity]

> **40.7% gene attrition**: 7 organisms and 5,229 gene records were excluded due to locusId format mismatches between the metal atlas and fitness matrices. [src: metal_specificity]

## Other caveats in this report

- The metal-specific fraction was ~41% at a 2% sick-rate cutoff and ~67% at 10%. [src: metal_specificity]
- Seven of 31 metal-tested organisms were excluded because locusId formats did not match fitness-matrix indices. [src: metal_specificity]
- Included organisms represented 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report expects no systematic bias from the taxonomically diverse exclusions, but does not establish that empirically. [src: metal_specificity]
- The conservation analysis covered 22 organisms with pangenome links and distinguished pooled from organism-mean core fractions. [src: metal_specificity]
