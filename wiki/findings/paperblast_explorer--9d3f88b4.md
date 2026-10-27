---
type: "Finding"
description: "At 50% identity, 9.2% of protein families (31,653) have zero papers across all members and 46.1% (159,046) have exactly 1 paper, while only 4.3% (14,904) have 20 or more; 5,218 multi-member families representing 14,534 sequences have no literature whatsoever."
finding_id: "paperblast_explorer--9d3f88b4"
result: "null result"
source: "paperblast_explorer"
quantities: [{"value": "9.2%", "what": "protein families with zero papers across all members", "unit": "%", "denominator": "protein families at 50% identity", "scope": "31,653 families"}, {"value": "46.1%", "what": "protein families with exactly 1 paper", "unit": "%", "denominator": "protein families at 50% identity", "scope": "159,046 families"}, {"value": "4.3%", "what": "families with 20 or more papers", "unit": "%", "denominator": "protein families at 50% identity", "scope": "14,904 families"}, {"value": "5,218", "what": "multi-member families with no literature, representing 14,534 sequences", "unit": "families", "denominator": "", "scope": "50% identity clusters"}]
caveat: "Without negative controls, genuinely unstudied genes cannot be easily distinguished from genes whose literature was missed by text mining."
first_added: "2026-10-23"
source_hash: "21c92287da8100c2ce6f5e7686137d1f4a58e8270def5e4de9a0da68a56494f6"
---
# Many protein families have no or one paper; some lack any literature

At 50% identity, 9.2% of protein families (31,653) have zero papers across all members and 46.1% (159,046) have exactly 1 paper, while only 4.3% (14,904) have 20 or more; 5,218 multi-member families representing 14,534 sequences have no literature whatsoever. [src: paperblast_explorer]

## Key figures

- **9.2%**: protein families with zero papers across all members (denominator protein families at 50% identity; scope 31,653 families) [src: paperblast_explorer]
- **46.1%**: protein families with exactly 1 paper (denominator protein families at 50% identity; scope 159,046 families) [src: paperblast_explorer]
- **4.3%**: families with 20 or more papers (denominator protein families at 50% identity; scope 14,904 families) [src: paperblast_explorer]
- **5,218 families**: multi-member families with no literature, representing 14,534 sequences (scope 50% identity clusters) [src: paperblast_explorer]

## Evidence

> At 50% identity, **9.2% of protein families** (31,653) have **zero papers** across all members, and **46.1%** (159,046) have exactly 1 paper. Only **4.3%** of families (14,904) have 20 or more papers. 5,218 multi-member families — representing 14,534 sequences — have no literature whatsoever. These are the "dark" protein families. [src: paperblast_explorer]

From the report [[summaries/paperblast_explorer__REPORT]].

## Caveat

Without negative controls, genuinely unstudied genes cannot be easily distinguished from genes whose literature was missed by text mining. [src: paperblast_explorer]

> **No negative controls**: We cannot easily distinguish genes that are genuinely unstudied from genes whose literature was missed by text mining. [src: paperblast_explorer]

## Other caveats in this report

- The approximately 40% estimate concerns protein residues lacking structural or functional information; the report's 55% concerns 50%-identity families with 0 or 1 papers. Their denominators and definitions differ. [src: paperblast_explorer]
- A text-mined paper mention does not establish functional characterization; some single-paper links may be incidental. [src: paperblast_explorer]
- Mining only PubMed Central full text misses paywalled papers and can bias measured coverage by open-access rate. [src: paperblast_explorer]
- The 50% sequence-identity definition of a protein family is conventional, not a universal biological boundary. [src: paperblast_explorer]
- Only 19% of SwissProt is represented in PaperBLAST; missing matching PMC full text is offered as a likely explanation, not demonstrated as the cause. [src: paperblast_explorer]
