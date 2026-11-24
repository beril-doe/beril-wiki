---
type: "Finding"
description: "Of 20,723 organisms with any literature in PaperBLAST, the top 1,000 capture 94.2%, leaving the remaining 19,723 organisms sharing just 5.8% of the literature."
finding_id: "paperblast_explorer--32784e8f"
result: "observation"
source: "paperblast_explorer"
quantities: [{"value": "94.2%", "what": "share of literature captured by the top 1,000 organisms", "unit": "percent", "denominator": "total literature across the 20,723 organisms with any literature", "scope": "PaperBLAST, top 1,000 organisms"}, {"value": "5.8%", "what": "share of literature held by the remaining 19,723 organisms", "unit": "percent", "denominator": "total literature across the 20,723 organisms with any literature", "scope": "PaperBLAST, remaining 19,723 organisms"}]
caveat: "PaperBLAST only mines full text from PubMed Central, so paywalled papers are missed, creating a systematic bias against fields or journals with lower open-access rates."
first_added: "2026-11-24"
source_hash: "21c92287da8100c2ce6f5e7686137d1f4a58e8270def5e4de9a0da68a56494f6"
---
# A thousand organisms hold nearly all PaperBLAST literature

Of 20,723 organisms with any literature in PaperBLAST, the top 1,000 capture 94.2%, leaving the remaining 19,723 organisms sharing just 5.8% of the literature. [src: paperblast_explorer]

## Key figures

- **94.2%**: share of literature captured by the top 1,000 organisms (denominator total literature across the 20,723 organisms with any literature; scope PaperBLAST, top 1,000 organisms) [src: paperblast_explorer]
- **5.8%**: share of literature held by the remaining 19,723 organisms (denominator total literature across the 20,723 organisms with any literature; scope PaperBLAST, remaining 19,723 organisms) [src: paperblast_explorer]

## Evidence

> Of 20,723 organisms with any literature, the top 1,000 capture 94.2%, leaving the remaining 19,723 organisms sharing just 5.8% of the literature. [src: paperblast_explorer]

From the report [[summaries/paperblast_explorer__REPORT]].

## Caveat

PaperBLAST only mines full text from PubMed Central, so paywalled papers are missed, creating a systematic bias against fields or journals with lower open-access rates. [src: paperblast_explorer]

> - **PMC open-access only**: PaperBLAST only mines full-text from PubMed Central. Papers behind paywalls are missed, creating a systematic bias against fields/journals with lower open-access rates. [src: paperblast_explorer]

## Other caveats in this report

- In PaperBLAST, 14,798 organisms received an Unknown domain classification, indicating many organisms are not easily classified using name heuristics alone. [src: paperblast_explorer]
- PaperBLAST includes approximately 19% of the full SwissProt database (~570K reviewed entries as of 2024), specifically the subset matched to PMC open-access literature. [src: paperblast_explorer]
- PaperBLAST text-mined paper mentions do not imply functional characterization, and the report suggests that the 65.6% with 1 paper likely include many incidental mentions. [src: paperblast_explorer]
- The report's heuristic organism-to-domain mapping classified 35% of organisms as Unknown, and a formal taxonomy lookup would improve accuracy. [src: paperblast_explorer]
- The report's 50% identity protein-family cutoff is conventional but arbitrary and not a universal biological boundary. [src: paperblast_explorer]
