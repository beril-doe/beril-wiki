---
type: "Finding"
description: "Contrary to its prediction, host-associated bacteria score slightly but significantly higher than environmental bacteria (d=+0.14, p<0.0001)."
finding_id: "bacdive_metal_validation--894e1826"
result: "correction"
source: "bacdive_metal_validation"
quantities: [{"value": "d=+0.14", "what": "Cohen's d host-associated vs baseline", "unit": "", "denominator": "", "scope": "BacDive"}]
caveat: "This likely reflects genome size confounding: host-associated bacteria in BacDive are dominated by large-genome Pseudomonadota pathogens (e.g., Pseudomonas, Klebsiella, Acinetobacter), inflating the normalized metal score."
first_added: "2026-11-24"
source_hash: "6b482275a5774daed2242605f701225afa538da071ebfacdff398459a8d660a0"
---
# Host-associated bacteria score higher than predicted, likely from genome size

Contrary to its prediction, host-associated bacteria score slightly but significantly higher than environmental bacteria (d=+0.14, p<0.0001). [src: bacdive_metal_validation]

## Key figures

- **d=+0.14**: Cohen's d host-associated vs baseline (scope BacDive) [src: bacdive_metal_validation]

## Evidence

> The data show the opposite: host-associated bacteria score slightly but significantly higher (d=+0.14, p<0.0001). [src: bacdive_metal_validation]

From the report [[summaries/bacdive_metal_validation__REPORT]].

## Caveat

This likely reflects genome size confounding: host-associated bacteria in BacDive are dominated by large-genome Pseudomonadota pathogens (e.g., Pseudomonas, Klebsiella, Acinetobacter), inflating the normalized metal score. [src: bacdive_metal_validation]

> This likely reflects genome size confounding: host-associated bacteria in BacDive are dominated by Pseudomonadota pathogens (e.g., *Pseudomonas*, *Klebsiella*, *Acinetobacter*) with large genomes and correspondingly more KEGG-annotated gene clusters, inflating the normalized metal score. [src: bacdive_metal_validation]

## Other caveats in this report

- The report notes that contamination-isolate sample sizes are small in Bacillota and Bacteroidota. [src: bacdive_metal_validation]
- Positive BacDive metal utilizers had lower metal tolerance scores, but the report cautions against overinterpreting this surprising, nonsignificant direction because the sample was tiny. [src: bacdive_metal_validation]
- The observed BacDive heavy metal effect d=1.00 barely exceeded the detection threshold, providing just enough power to detect the effect. [src: bacdive_metal_validation]
- The report states that a larger heavy metal contamination dataset is needed to precisely estimate the effect size. [src: bacdive_metal_validation]
- Although RESEARCH_PLAN.md referenced n=31 BacDive heavy metal isolates, only 10 matched pangenome species with metal tolerance scores after the species-name bridge. [src: bacdive_metal_validation]
