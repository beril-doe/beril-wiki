---
type: "Finding"
description: "Of 841K genes with any text-mined paper link, 551K (65.6%) have exactly 1 paper, the median is 1 and the mean is 3.8; the top 50 most-referenced genes are all human, and just 6% of genes (50K) account for 57.7% of all gene-paper links."
finding_id: "paperblast_explorer--3dc1e920"
result: "observation"
source: "paperblast_explorer"
quantities: [{"value": "551K (65.6%)", "what": "genes with exactly 1 paper", "unit": "", "denominator": "841K genes with any text-mined paper link", "scope": "PaperBLAST"}, {"value": "3.8", "what": "mean papers per gene", "unit": "papers", "denominator": "841K genes with any text-mined paper link", "scope": "PaperBLAST"}, {"value": "57.7%", "what": "share of all gene-paper links accounted for by 6% of genes (50K)", "unit": "%", "denominator": "all gene-paper links", "scope": "PaperBLAST"}, {"value": "9,988", "what": "papers for p53, the most-referenced gene", "unit": "papers", "denominator": "", "scope": "PaperBLAST"}]
caveat: "A gene mentioned in a paper may be tangential to the study, so the 65.6% with 1 paper likely includes many incidental mentions."
first_added: "2026-10-23"
source_hash: "21c92287da8100c2ce6f5e7686137d1f4a58e8270def5e4de9a0da68a56494f6"
---
# Most text-mined genes have one paper; a few genes dominate links

Of 841K genes with any text-mined paper link, 551K (65.6%) have exactly 1 paper, the median is 1 and the mean is 3.8; the top 50 most-referenced genes are all human, and just 6% of genes (50K) account for 57.7% of all gene-paper links. [src: paperblast_explorer]

## Key figures

- **551K (65.6%)**: genes with exactly 1 paper (denominator 841K genes with any text-mined paper link; scope PaperBLAST) [src: paperblast_explorer]
- **3.8 papers**: mean papers per gene (denominator 841K genes with any text-mined paper link; scope PaperBLAST) [src: paperblast_explorer]
- **57.7%**: share of all gene-paper links accounted for by 6% of genes (50K) (denominator all gene-paper links; scope PaperBLAST) [src: paperblast_explorer]
- **9,988 papers**: papers for p53, the most-referenced gene (scope PaperBLAST) [src: paperblast_explorer]

## Evidence

> Of 841K genes with any text-mined paper link, **551K (65.6%)** have exactly 1 paper. The median is 1, the mean is 3.8. The top 50 most-referenced genes are all human — led by p53 (9,988 papers), TNF (6,002), and EGFR (5,895). Just 6% of genes (50K) account for 57.7% of all gene-paper links. [src: paperblast_explorer]

From the report [[summaries/paperblast_explorer__REPORT]].

## Caveat

A gene mentioned in a paper may be tangential to the study, so the 65.6% with 1 paper likely includes many incidental mentions. [src: paperblast_explorer]

> **Text mining ≠ functional characterization**: A gene mentioned in a paper may be tangential to the study. The 65.6% with 1 paper likely includes many incidental mentions. [src: paperblast_explorer]

## Other caveats in this report

- The approximately 40% estimate concerns protein residues lacking structural or functional information; the report's 55% concerns 50%-identity families with 0 or 1 papers. Their denominators and definitions differ. [src: paperblast_explorer]
- Mining only PubMed Central full text misses paywalled papers and can bias measured coverage by open-access rate. [src: paperblast_explorer]
- The 50% sequence-identity definition of a protein family is conventional, not a universal biological boundary. [src: paperblast_explorer]
- Only 19% of SwissProt is represented in PaperBLAST; missing matching PMC full text is offered as a likely explanation, not demonstrated as the cause. [src: paperblast_explorer]
- Without negative controls, apparent lack of literature cannot be distinguished reliably from literature missed by text mining. [src: paperblast_explorer]
