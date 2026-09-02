---
type: "Dataset"
description: "Orthology database used to provide partial clues for dark genes"
sources: ["summaries/truly_dark_genes__REPORT.md"]
---
# eggNOG

## What this entity is

**Canonical name:** eggNOG, an orthology and functional-annotation resource used in the report to provide partial clues about genes that remained hypothetical after reannotation. [src: truly_dark_genes]

**Known aliases:** eggNOG-mapper is the associated annotation workflow named in the report. [src: truly_dark_genes]

**Stable external identifier:** No stable external identifier is specified in the report. [src: truly_dark_genes]

## Key facts from truly_dark_genes

- eggNOG-mapper provided partial signal for 43.5% of the 6,427 genes classified as truly dark. [src: truly_dark_genes]
- The report identifies 2,551 eggNOG annotations for 2,551 unique truly dark gene clusters, corresponding to 43.5% of the 5,870 unique clusters. [src: truly_dark_genes]
- eggNOG evidence was one component of the 12-dimensional clue matrix used to distinguish genes with no clues, sequence-identification clues, partial functional clues, or phenotype-only clues. [src: truly_dark_genes]
- The report places 711 truly dark genes, or 11.1%, in the tier with partial functional evidence from Pfam, COG, or eggNOG. [src: truly_dark_genes]
- Together, the partial-function tier and the phenotype-only tier contain 2,314 genes considered the most promising for narrowing experimental hypotheses. [src: truly_dark_genes]
- For one prioritized candidate, DvH/206658, eggNOG suggested “trehalose synthase” despite the gene retaining a hypothetical annotation. [src: truly_dark_genes]
- The report contrasts eggNOG’s partial functional signal with sparse domain and pathway coverage: only 4.0% of truly dark genes had Pfam hits and 4.6% had KEGG KOs. [src: truly_dark_genes]

## Related pages

- [[summaries/truly_dark_genes__REPORT]] — source summary for the analysis of genes remaining unknown after modern annotation.
- [[concepts/functional-dark-matter]] — cross-project synthesis of residual unknown gene function.
- [[entities/pfam]] — protein-family domain resource used alongside eggNOG evidence.
- [[entities/kegg]] — pathway and orthology resource used for comparison with eggNOG coverage.
