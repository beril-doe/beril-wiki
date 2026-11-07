---
type: "Finding"
description: "Of 39,532 dark genes with pangenome links, 33,105 (83.7%) are reclassified by Bakta (v1.12.0, DB v6.0) as not hypothetical, whereas the Fitness Browser had only 'hypothetical protein'; this represents 58.1% of all dark genes."
finding_id: "functional_dark_matter--edbf95bc"
result: "correction"
source: "functional_dark_matter"
quantities: [{"value": "33,105", "what": "linked dark genes reclassified by Bakta as not hypothetical", "unit": "genes", "denominator": "39,532 dark genes with pangenome links", "scope": "Bakta v1.12.0 (DB v6.0)"}, {"value": "83.7%", "what": "share of linked dark genes reclassified", "unit": "percent", "denominator": "39,532 linked dark genes", "scope": ""}, {"value": "58.1%", "what": "share of all dark genes reclassified", "unit": "percent", "denominator": "57,011 dark genes", "scope": ""}]
caveat: "Some 'hypothetical' genes may have annotations in databases not checked (UniProt, InterPro, recent NCBI updates), and the 57,011 dark gene count likely overestimates truly uncharacterized genes."
first_added: "2026-10-23"
source_hash: "1ea00a93830c52ac6d4c47418f8d718cf6b5aa2d81462a64855a8308888da1d0"
---
# Bakta reclassifies most linked dark genes as non-hypothetical

Of 39,532 dark genes with pangenome links, 33,105 (83.7%) are reclassified by Bakta (v1.12.0, DB v6.0) as not hypothetical, whereas the Fitness Browser had only 'hypothetical protein'; this represents 58.1% of all dark genes. [src: functional_dark_matter]

## Key figures

- **33,105 genes**: linked dark genes reclassified by Bakta as not hypothetical (denominator 39,532 dark genes with pangenome links; scope Bakta v1.12.0 (DB v6.0)) [src: functional_dark_matter]
- **83.7%**: share of linked dark genes reclassified (denominator 39,532 linked dark genes) [src: functional_dark_matter]
- **58.1%**: share of all dark genes reclassified (denominator 57,011 dark genes) [src: functional_dark_matter]

## Evidence

> Bakta v1.12.0 (DB v6.0) annotations for the 132.5M pangenome cluster representatives were cross-referenced against the 57,011 dark gene catalog. Of 39,532 dark genes with pangenome links, **33,105 (83.7%) are reclassified by bakta as NOT hypothetical** — bakta's PSC/PSCC pipeline assigns them a product description where the Fitness Browser had only "hypothetical protein." This represents 58.1% of all dark genes. [src: functional_dark_matter]

From the report [[summaries/functional_dark_matter__REPORT]].

## Caveat

Some 'hypothetical' genes may have annotations in databases not checked (UniProt, InterPro, recent NCBI updates), and the 57,011 dark gene count likely overestimates truly uncharacterized genes. [src: functional_dark_matter]

> 3. **Annotation bias**: Some "hypothetical" genes may have annotations in databases not checked (UniProt, InterPro, recent NCBI updates). The dark gene count (57,011) likely overestimates the true number of functionally uncharacterized genes. [src: functional_dark_matter]

## Other caveats in this report

- The fraction of hypothetical genes ranges from >35% to <15% across species; the report attributes this variation to annotation depth rather than true functional content. [src: functional_dark_matter]
- The pathway-gap result is organism-level co-occurrence, not direct gene-to-gap enzymatic matching. [src: functional_dark_matter]
- Dark-gene gap filling remains a hypothesis requiring enzyme-number matching, structure prediction, or experiments. [src: functional_dark_matter]
- Marinobacter has 49 gapped pathways, and D. desulfuricans ME-23 and P. stutzeri have 45 each; their dark genes are proposed, not established, as possible missing-step enzymes. [src: functional_dark_matter]
- The report interprets carbon-source and motility concordance as possible conserved unannotated functions, and OG05812 as a possible stress-associated regulatory protease; these are functional hypotheses. [src: functional_dark_matter]
