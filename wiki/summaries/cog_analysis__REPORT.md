---
type: "Summary"
description: "Summary of the project COG Functional Category Analysis."
doc_type: "short"
full_text: "sources/cog_analysis__REPORT.md"
---
# COG Functional Category Analysis

This page summarises the COG (clusters of orthologous groups) Functional Category Analysis. The report analysed 32 species across 9 phyla (357,623 genes) and reports a consistent "two-speed genome". [src: cog_analysis]

## Key Findings

### Novel genes are enriched in mobile and defense functions

- Novel/singleton genes show +10.88% enrichment for COG L (mobile elements), with 100% consistency across species, which the report calls the strongest signal. [src: cog_analysis]
- Novel/singleton genes show +2.83% enrichment for COG V (defense mechanisms), with 100% consistency. [src: cog_analysis]
- Novel/singleton genes show +1.64% enrichment for COG S (unknown function), with 69% consistency. [src: cog_analysis]

### Core genes are enriched in housekeeping and metabolism

- J (translation): -4.65% enrichment, 97% consistency, the strongest depletion. [src: cog_analysis]
- F (nucleotide metabolism): -2.09% enrichment, 100% consistency. [src: cog_analysis]
- H (coenzyme metabolism): -2.06% enrichment, 97% consistency. [src: cog_analysis]
- E (amino acid metabolism): -1.81% enrichment, 81% consistency. [src: cog_analysis]
- C (energy production): -1.75% enrichment, 88% consistency. [src: cog_analysis]

### Composite COG categories

- The report states that multi-function genes with composite COG assignments are not annotation artifacts. [src: cog_analysis]
- Its examples are LV, meaning mobile plus defense, and EGP, meaning amino acid plus carbohydrate plus inorganic ion. [src: cog_analysis]
- LV shows +0.34% enrichment with 76% consistency. [src: cog_analysis]
- The report suggests this enrichment reflects functional modules such as "mobile defense islands". [src: cog_analysis]
- It argues these genes are genuine multi-functional genes and should not be filtered out as noise. [src: cog_analysis]

### The report's interpretation

These points are the report's interpretations, not separate measurements.

- It interprets core genes as an ancient, conserved "metabolic engine" of translation, energy and biosynthesis. [src: cog_analysis]
- It interprets novel genes as recent acquisitions for ecological adaptation, including mobile elements, defense and niche-specific functions. [src: cog_analysis]
- It asserts that horizontal gene transfer (HGT), not vertical inheritance, is the primary innovation mechanism. [src: cog_analysis]
- It reads the +10.88% L enrichment as suggesting that most genomic novelty comes from mobile elements. [src: cog_analysis]
- It states the patterns hold across bacterial phyla, suggesting deep evolutionary constraint. [src: cog_analysis]
- It states that all 8 predictions from the initial N. gonorrhoeae analysis were confirmed across 32 species. [src: cog_analysis]
- It calls the result a fundamental organizing principle of bacterial pangenome structure. [src: cog_analysis]

The report links the L result to Koonin & Wolf (2008) and Treangen & Rocha (2011), which it describes as showing HGT as the primary source of prokaryotic gene novelty. [src: cog_analysis] It links core enrichment in J and C to Charlesworth & Jensen (2022) and the minimal-genome literature. [src: cog_analysis] See [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]] and [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

## Data and Methods

The analysis used the kbase_ke_pangenome tables gene_cluster, gene_genecluster_junction and eggnog_mapper_annotations. [src: cog_analysis] See [[entities/kbase-ke-pangenome]]. The report provides COG category proportions by gene class for 32 species. [src: cog_analysis]

## Caveats and Open Work

- COG annotations cover about 70% of genes, and unassigned genes may skew distributions. [src: cog_analysis] See [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment]].
- Composite multi-letter COG categories are counted once per gene, not split. [src: cog_analysis]
- The analysis uses 32 species, and a larger sample might reveal phylum-specific patterns. [src: cog_analysis]
- eggNOG v6 annotations may differ from original COG assignments. [src: cog_analysis] See [[entities/eggnog-orthologous-groups]].
- The report proposes analysing multiple species for consistent patterns. [src: cog_analysis]
- It proposes comparing COG distributions across taxonomic groups. [src: cog_analysis]
- It proposes investigating COG V (defense) and L (recombination) in detail. [src: cog_analysis]
- It proposes correlating novel-gene functions with environmental metadata to test whether they vary by habitat. [src: cog_analysis]

## Slots Into

- [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]]: COG L enrichment of +10.88% with 100% consistency among novel genes. [src: cog_analysis]
- [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]]: core genes are enriched in translation, nucleotide, coenzyme, amino acid and energy functions. [src: cog_analysis]
- [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment]]: COG annotation covers about 70% of genes. [src: cog_analysis]
