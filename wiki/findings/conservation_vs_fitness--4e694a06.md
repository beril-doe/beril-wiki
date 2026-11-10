---
type: "Finding"
description: "Essential-core genes were the most enzyme-rich (41.9%) and best annotated (87% known function), enriched in Protein Metabolism (+13.7 percentage points vs non-essential) and depleted in Carbohydrates (-7.9%), Amino Acids (-5.6%) and Membrane Transport (-4.0%), which the report interprets as conditionally important functions."
finding_id: "conservation_vs_fitness--4e694a06"
result: "observation"
source: "conservation_vs_fitness"
quantities: [{"value": "41.9%", "what": "share of essential-core genes classified as enzymes", "unit": "%", "denominator": "essential-core genes", "scope": ""}, {"value": "87%", "what": "essential-core genes with known function", "unit": "%", "denominator": "essential-core genes", "scope": ""}, {"value": "+13.7 percentage points", "what": "Protein Metabolism enrichment of essential-core versus non-essential genes", "unit": "percentage points", "denominator": "", "scope": ""}, {"value": "-7.9%", "what": "Carbohydrates depletion in essential-core versus non-essential genes", "unit": "%", "denominator": "", "scope": ""}]
caveat: "RB-TnSeq essentiality is defined under the specific library construction conditions, so genes essential only under stress conditions would not be captured."
first_added: "2026-10-27"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Essential-core genes are enzyme-rich and enriched in protein metabolism

Essential-core genes were the most enzyme-rich (41.9%) and best annotated (87% known function), enriched in Protein Metabolism (+13.7 percentage points vs non-essential) and depleted in Carbohydrates (-7.9%), Amino Acids (-5.6%) and Membrane Transport (-4.0%), which the report interprets as conditionally important functions. [src: conservation_vs_fitness]

## Key figures

- **41.9%**: share of essential-core genes classified as enzymes (denominator essential-core genes) [src: conservation_vs_fitness]
- **87%**: essential-core genes with known function (denominator essential-core genes) [src: conservation_vs_fitness]
- **+13.7 percentage points**: Protein Metabolism enrichment of essential-core versus non-essential genes [src: conservation_vs_fitness]
- **-7.9%**: Carbohydrates depletion in essential-core versus non-essential genes [src: conservation_vs_fitness]

## Evidence

> **Essential-core genes** are the most enzyme-rich (41.9%) and best-annotated (87% with known function). They are enriched in Protein Metabolism (+13.7 percentage points vs non-essential), Cofactors/Vitamins (+6.2%), Cell Wall (+3.9%), and Fatty Acid biosynthesis (+3.1%). They are depleted in Carbohydrates (-7.9%), Amino Acids (-5.6%), and Membrane Transport (-4.0%) -- functions that tend to be conditionally important rather than universally essential. [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

RB-TnSeq essentiality is defined under the specific library construction conditions, so genes essential only under stress conditions would not be captured. [src: conservation_vs_fitness]

> - **Single growth condition for essentiality**: RB-TnSeq essentiality is defined under the specific library construction conditions. Genes essential only under stress conditions would not be captured. [src: conservation_vs_fitness]

## Other caveats in this report

- 34 organisms had >=90% mapping coverage, but only 33 entered downstream analysis because Dyella79 had a locus-tag mismatch. [src: conservation_vs_fitness]
- Putative essential genes were slightly shorter on average, consistent with possible transposon-insertion bias. [src: conservation_vs_fitness]
- The report characterizes the essential-core association as modest (OR=1.56), noting that many genes are core irrespective of essentiality. [src: conservation_vs_fitness]
- The report cites TraDIS work in E. coli K-12 as a precedent for gene-length bias in transposon-based essentiality calls. [src: conservation_vs_fitness]
- The putative-essential definition is an upper bound: absent fitness data may reflect short genes, low-complexity regions, or scaffold edges rather than essentiality; shorter average gene length suggests some insertion bias. [src: conservation_vs_fitness]
