---
type: "Finding"
description: "Across 48 Fitness Browser organisms (228,709 genes), 57,011 (24.9%) lack functional annotation; of these, 7,787 show strong fitness effects (|fitness| \u2265 2 in at least one condition) and 9,557 are essential (no viable transposon mutants), together 17,344 experimentally actionable dark genes."
finding_id: "functional_dark_matter--1e0e1f03"
result: "observation"
source: "functional_dark_matter"
quantities: [{"value": "57,011", "what": "genes lacking functional annotation", "unit": "genes", "denominator": "228,709 genes", "scope": "48 Fitness Browser organisms"}, {"value": "24.9%", "what": "fraction of genes unannotated", "unit": "percent", "denominator": "228,709 genes", "scope": "48 Fitness Browser organisms"}, {"value": "7,787", "what": "dark genes with strong fitness effects (|fitness| \u2265 2 in at least one condition)", "unit": "genes", "denominator": "57,011 dark genes", "scope": ""}, {"value": "9,557", "what": "dark genes that are essential (no viable transposon mutants)", "unit": "genes", "denominator": "57,011 dark genes", "scope": ""}]
caveat: "Some 'hypothetical' genes may have annotations in databases not checked (UniProt, InterPro, recent NCBI updates), so the 57,011 dark gene count likely overestimates the true number of functionally uncharacterized genes."
first_added: "2026-10-23"
source_hash: "1ea00a93830c52ac6d4c47418f8d718cf6b5aa2d81462a64855a8308888da1d0"
---
# Many unannotated Fitness Browser genes have measurable phenotypes

Across 48 Fitness Browser organisms (228,709 genes), 57,011 (24.9%) lack functional annotation; of these, 7,787 show strong fitness effects (|fitness| ≥ 2 in at least one condition) and 9,557 are essential (no viable transposon mutants), together 17,344 experimentally actionable dark genes. [src: functional_dark_matter]

## Key figures

- **57,011 genes**: genes lacking functional annotation (denominator 228,709 genes; scope 48 Fitness Browser organisms) [src: functional_dark_matter]
- **24.9%**: fraction of genes unannotated (denominator 228,709 genes; scope 48 Fitness Browser organisms) [src: functional_dark_matter]
- **7,787 genes**: dark genes with strong fitness effects (|fitness| ≥ 2 in at least one condition) (denominator 57,011 dark genes) [src: functional_dark_matter]
- **9,557 genes**: dark genes that are essential (no viable transposon mutants) (denominator 57,011 dark genes) [src: functional_dark_matter]

## Evidence

> Across 48 Fitness Browser organisms (228,709 genes), 57,011 (24.9%) lack functional annotation ("hypothetical protein," DUF, or "uncharacterized"). Of these, 7,787 show strong fitness effects (|fitness| ≥ 2 in at least one condition), and 9,557 are essential (no viable transposon mutants). Together, these 17,344 genes represent the experimentally actionable "dark matter" — genes with clear biological importance but unknown function. [src: functional_dark_matter]

From the report [[summaries/functional_dark_matter__REPORT]].

## Caveat

Some 'hypothetical' genes may have annotations in databases not checked (UniProt, InterPro, recent NCBI updates), so the 57,011 dark gene count likely overestimates the true number of functionally uncharacterized genes. [src: functional_dark_matter]

> 3. **Annotation bias**: Some "hypothetical" genes may have annotations in databases not checked (UniProt, InterPro, recent NCBI updates). The dark gene count (57,011) likely overestimates the true number of functionally uncharacterized genes. [src: functional_dark_matter]

## Other caveats in this report

- The fraction of hypothetical genes ranges from >35% to <15% across species; the report attributes this variation to annotation depth rather than true functional content. [src: functional_dark_matter]
- The pathway-gap result is organism-level co-occurrence, not direct gene-to-gap enzymatic matching. [src: functional_dark_matter]
- Dark-gene gap filling remains a hypothesis requiring enzyme-number matching, structure prediction, or experiments. [src: functional_dark_matter]
- Marinobacter has 49 gapped pathways, and D. desulfuricans ME-23 and P. stutzeri have 45 each; their dark genes are proposed, not established, as possible missing-step enzymes. [src: functional_dark_matter]
- The report interprets carbon-source and motility concordance as possible conserved unannotated functions, and OG05812 as a possible stress-associated regulatory protease; these are functional hypotheses. [src: functional_dark_matter]
