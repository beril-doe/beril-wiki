---
type: "Finding"
description: "In PaperBLAST, Homo sapiens alone accounts for 46.7% of all gene-paper records, the top 5 organisms capture 72.8%, and of 20,723 organisms with any literature the top 1,000 capture 94.2%, leaving the remaining 19,723 organisms sharing just 5.8% of the literature."
finding_id: "paperblast_explorer--415e8345"
result: "observation"
source: "paperblast_explorer"
quantities: [{"value": "46.7%", "what": "share of all gene-paper records attributable to Homo sapiens", "unit": "%", "denominator": "all gene-paper records in PaperBLAST", "scope": "PaperBLAST"}, {"value": "72.8%", "what": "share of gene-paper records captured by the top 5 organisms", "unit": "%", "denominator": "all gene-paper records in PaperBLAST", "scope": "H. sapiens, M. musculus, R. norvegicus, A. thaliana, D. melanogaster"}, {"value": "94.2%", "what": "share of the literature captured by the top 1,000 organisms", "unit": "%", "denominator": "all gene-paper records in PaperBLAST", "scope": "top 1,000 of 20,723 organisms with any literature"}, {"value": "5.8%", "what": "share of the literature shared by the remaining 19,723 organisms", "unit": "%", "denominator": "all gene-paper records in PaperBLAST", "scope": "remaining 19,723 of 20,723 organisms with any literature"}]
caveat: "PaperBLAST mines full text only from PubMed Central, so paywalled papers are missed, creating a systematic bias against fields and journals with lower open-access rates."
first_added: "2026-10-23"
source_hash: "21c92287da8100c2ce6f5e7686137d1f4a58e8270def5e4de9a0da68a56494f6"
---
# Literature is concentrated in very few organisms, led by humans

In PaperBLAST, Homo sapiens alone accounts for 46.7% of all gene-paper records, the top 5 organisms capture 72.8%, and of 20,723 organisms with any literature the top 1,000 capture 94.2%, leaving the remaining 19,723 organisms sharing just 5.8% of the literature. [src: paperblast_explorer]

## Key figures

- **46.7%**: share of all gene-paper records attributable to Homo sapiens (denominator all gene-paper records in PaperBLAST; scope PaperBLAST) [src: paperblast_explorer]
- **72.8%**: share of gene-paper records captured by the top 5 organisms (denominator all gene-paper records in PaperBLAST; scope H. sapiens, M. musculus, R. norvegicus, A. thaliana, D. melanogaster) [src: paperblast_explorer]
- **94.2%**: share of the literature captured by the top 1,000 organisms (denominator all gene-paper records in PaperBLAST; scope top 1,000 of 20,723 organisms with any literature) [src: paperblast_explorer]
- **5.8%**: share of the literature shared by the remaining 19,723 organisms (denominator all gene-paper records in PaperBLAST; scope remaining 19,723 of 20,723 organisms with any literature) [src: paperblast_explorer]

## Evidence

> *Homo sapiens* alone accounts for **46.7%** of all gene-paper records in PaperBLAST. The top 5 organisms (*H. sapiens*, *M. musculus*, *R. norvegicus*, *A. thaliana*, *D. melanogaster*) capture **72.8%**. Of 20,723 organisms with any literature, the top 1,000 capture 94.2%, leaving the remaining 19,723 organisms sharing just 5.8% of the literature. [src: paperblast_explorer]

From the report [[summaries/paperblast_explorer__REPORT]].

## Caveat

PaperBLAST mines full text only from PubMed Central, so paywalled papers are missed, creating a systematic bias against fields and journals with lower open-access rates. [src: paperblast_explorer]

> **PMC open-access only**: PaperBLAST only mines full-text from PubMed Central. Papers behind paywalls are missed, creating a systematic bias against fields/journals with lower open-access rates. [src: paperblast_explorer]

## Other caveats in this report

- The approximately 40% estimate concerns protein residues lacking structural or functional information; the report's 55% concerns 50%-identity families with 0 or 1 papers. Their denominators and definitions differ. [src: paperblast_explorer]
- A text-mined paper mention does not establish functional characterization; some single-paper links may be incidental. [src: paperblast_explorer]
- The 50% sequence-identity definition of a protein family is conventional, not a universal biological boundary. [src: paperblast_explorer]
- Only 19% of SwissProt is represented in PaperBLAST; missing matching PMC full text is offered as a likely explanation, not demonstrated as the cause. [src: paperblast_explorer]
- Without negative controls, apparent lack of literature cannot be distinguished reliably from literature missed by text mining. [src: paperblast_explorer]
