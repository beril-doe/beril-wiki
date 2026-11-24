---
type: "Summary"
description: "Summary of the project PaperBLAST Data Explorer — Characterizing Literature Coverage Bias in Protein Sequence Space."
doc_type: "short"
full_text: "sources/paperblast_explorer__REPORT.md"
---
# PaperBLAST Data Explorer — Characterizing Literature Coverage Bias in Protein Sequence Space

The top 50 most-referenced genes are all human, and the top 3 bacteria are pathogens or model organisms. [src: paperblast_explorer] At 50% identity, 9.2% of protein families have zero papers. [src: paperblast_explorer] The report says it gives the first comprehensive protein-family-level characterization of the PaperBLAST collection hosted by the KBase Data Lakehouse. [src: paperblast_explorer] Its text-mining basis limits how far these coverage figures can be read as functional knowledge. [src: paperblast_explorer] The report also proposes five follow-up analyses, including a cross-reference with the Fitness Browser and AlphaFold-based study of the dark families. [src: paperblast_explorer]

## Key Findings

### Concentration across organisms

Homo sapiens accounts for 46.7% of all gene-paper records. [src: paperblast_explorer]

The top 5 organisms (H. sapiens, M. musculus, R. norvegicus, A. thaliana, D. melanogaster) capture 72.8%. [src: paperblast_explorer]

Of 20,723 organisms with literature, the top 1,000 capture 94.2%, and the remaining 19,723 share 5.8%. [src: paperblast_explorer]

The organism-level Gini coefficient is 0.967, where 1.0 is perfect inequality. [src: paperblast_explorer]

The report likens this to wealth inequality in economics: a small fraction of biological entities receive nearly all research attention. [src: paperblast_explorer]

Among 15,312 bacterial organisms, the top 100 capture 44.3% of bacterial literature. [src: paperblast_explorer]

The top 3 bacteria are pathogens or model organisms: [[entities/mycobacterium-tuberculosis]] H37Rv with 9,079 papers, [[entities/escherichia-coli]] K-12 with 8,860, and [[entities/pseudomonas-aeruginosa-pao1]] with 5,928. [src: paperblast_explorer]

Environmental and non-pathogenic organisms are dramatically underrepresented. [src: paperblast_explorer]

### Concentration across genes

Of 841K genes with any text-mined paper link, 551K (65.6%) have exactly 1 paper. [src: paperblast_explorer]

The median is 1 paper per gene and the mean is 3.8. [src: paperblast_explorer]

Just 6% of genes (50K) account for 57.7% of all gene-paper links. [src: paperblast_explorer]

The gene-level Gini is 0.669, which the report calls very high. [src: paperblast_explorer]

The top 50 most-referenced genes are all human. [src: paperblast_explorer]

They are led by p53 (9,988 papers), TNF (6,002) and EGFR (5,895). [src: paperblast_explorer]

The papers-per-gene histogram is extremely right-skewed: most genes sit at 1 paper, and the tail extends to nearly 10,000 papers for p53. [src: paperblast_explorer]

The report finds the top 50 genes are exclusively human cancer/disease genes. [src: paperblast_explorer] It sees this as consistent with Stoeger et al. (2018), whom it describes as showing that the most-studied human genes keep attracting the most new research, a self-reinforcing "rich-get-richer" dynamic. [src: paperblast_explorer] It also describes them as showing that gene attention can be predicted from chemical, physical and biological properties, so the bias is systematic, not random. [src: paperblast_explorer]

### Protein families and dark families

The report clustered 815,571 PaperBLAST protein sequences with [[entities/mmseqs2]] at three identity thresholds. [src: paperblast_explorer]

This gave 628K clusters at 90% (77%, read as low strain-level redundancy). [src: paperblast_explorer]

It gave 345K clusters at 50% (protein-family level) and 215K at 30% (superfamily level). [src: paperblast_explorer]

At 90% identity, 83.3% of clusters are singletons, which the report reads as most sequences already being non-redundant at the strain level. [src: paperblast_explorer] The largest 90% cluster is actin, with 212 members. [src: paperblast_explorer] At 50% identity 67.5% of clusters are singletons, and at 30% 62.8%. [src: paperblast_explorer]

At 30% identity, a relatively small number of large superfamily clusters capture a substantial fraction of sequences. The long tail of singleton families accounts for the rest. [src: paperblast_explorer]

See [[concepts/sequence-clustering-resolution-and-protein-family-definition]].

The largest families are housekeeping proteins: HSP70/BiP (650 members at 50% identity), GAPDH (609), enolase (552) and GroEL (443). [src: paperblast_explorer]

Protein family size is positively related to literature coverage. [src: paperblast_explorer]

At 50% identity, 9.2% of families (31,653) have zero papers across all members, and 46.1% (159,046) have exactly 1. [src: paperblast_explorer] The report says 55% of families at 50% identity have 0 or 1 papers, and presents this as extending the dark-proteome observation to literature coverage. [src: paperblast_explorer] That observation is Perdigao et al. (2015), cited as estimating that about 40% of protein residues fall in dark regions with no structural or functional information. [src: paperblast_explorer]

Only 4.3% of families (14,904) have 20 or more papers. [src: paperblast_explorer]

There are 5,218 multi-member "dark" families, covering 14,534 sequences, with no literature. [src: paperblast_explorer] This is 4.6% of multi-member 50% identity clusters; the other 95.4% have at least one member with a paper. [src: paperblast_explorer] The report calls the 5,218 genuinely unstudied protein families. [src: paperblast_explorer] They are dominated by REBASE methyltransferases and biolip structural entries, specialized proteins that lack published functional studies. [src: paperblast_explorer]

Rocha et al. (2023) is credited with coining "functional unknomics" for the systematic study of conserved genes of unknown function. [src: paperblast_explorer]

See [[concepts/unstudied-protein-families-and-the-literature-defined-dark-proteome]].

### Database composition

The kescience_paperblast collection on the KBase Data Lakehouse holds 12.4 million rows across 14 tables, and the report uses all 14. [src: paperblast_explorer]

Genes are linked to papers by text mining PubMed Central full-text articles, plus curated annotations from 13 databases and PDB structural data. [src: paperblast_explorer]

| Table | Rows | Content |
|---|---|---|
| genepaper | 3,195,890 | text-mined gene-to-paper links [src: paperblast_explorer] |
| site | 2,089,192 | PDB binding/active/modified sites [src: paperblast_explorer] |
| snippet | 1,951,949 | text excerpts mentioning genes [src: paperblast_explorer] |
| generif | 1,358,798 | GeneRIF functional summaries [src: paperblast_explorer] |
| gene | 1,135,366 | gene/protein metadata [src: paperblast_explorer] |
| uniq | 815,571 | unique protein sequences [src: paperblast_explorer] |
| curatedpaper | 599,587 | curated gene-paper links [src: paperblast_explorer] |
| curatedgene | 255,096 | curated annotations (SwissProt, BRENDA, etc.) [src: paperblast_explorer] |

The 1.1M genes span 27,718 organisms across all domains of life. [src: paperblast_explorer]

| Domain | Organisms | Genes | Share of genes |
|---|---|---|---|
| Bacteria | 5,997 | 397,544 | 35.0% [src: paperblast_explorer] |
| Unknown | 14,798 | 397,511 | 35.0% [src: paperblast_explorer] |
| Eukarya | 822 | 290,537 | 25.6% [src: paperblast_explorer] |
| Virus | 5,730 | 27,199 | 2.4% [src: paperblast_explorer] |
| Archaea | 371 | 22,575 | 2.0% [src: paperblast_explorer] |

Bacteria dominate by organism count (6,000), but Eukarya dominate by gene count (291K), owing to over-representation of human and model-organism genes. [src: paperblast_explorer]

The "Unknown" class is a caveat: 14,798 organisms are not easily classified by name heuristics alone. [src: paperblast_explorer]

### Gene-paper links and curation

845K genes link to 1.1M unique papers through 3.2M many-to-many associations. [src: paperblast_explorer]

Each gene averages 3.8 papers and each paper mentions 2.9 genes. [src: paperblast_explorer]

The report calls the similar gene and paper counts (~1.1M each) somewhat coincidental, because most genes have few papers and most papers mention few genes. [src: paperblast_explorer]

About 25.6% of genes in the gene table (290K) have no text-mined paper link and rely only on curated or GeneRIF annotations. [src: paperblast_explorer]

[[entities/swiss-prot]] contributes the most curated entries (110K proteins, 182K unique papers). [src: paperblast_explorer]

PaperBLAST includes about 19% of full SwissProt (~570K reviewed entries as of 2024), the subset matched to PMC open-access literature. [src: paperblast_explorer]

The curated database table gives these figures:

| Database | Proteins | Papers | Papers/protein |
|---|---|---|---|
| SwissProt | 110,171 | 181,916 | 1.7 [src: paperblast_explorer] |
| biolip | 42,571 | 23,768 | 0.6 [src: paperblast_explorer] |
| BRENDA | 33,012 | 43,760 | 1.3 [src: paperblast_explorer] |
| MetaCyc | 12,700 | 46,176 | 3.6 [src: paperblast_explorer] |
| EcoCyc | 4,198 | 22,304 | 5.3 [src: paperblast_explorer] |

EcoCyc has the highest paper density per protein (5.3), reflecting deep curation of E. coli metabolism. [src: paperblast_explorer]

### Structural annotations

PaperBLAST includes site annotations for 132,179 PDB structures, with 2.1M site records across 4 types. [src: paperblast_explorer] The types are binding (1.69M), functional (182K), modified (112K) and mutagenesis (104K). [src: paperblast_explorer]

The 48,991 unique ligands are topped by zinc ions (65K sites), chlorophyll A (58K), calcium ions (53K) and heme (44K). [src: paperblast_explorer]

### Cross-database links

The report finds 129,823 VIMSS cross-references connecting PaperBLAST to the [[entities/fitness-browser]]. It sees this as a path from literature coverage to experimental fitness phenotypes, for finding functionally important but understudied genes. [src: paperblast_explorer]

### Time coverage

The database covers papers from 1951 to 2026. [src: paperblast_explorer]

Publications peak around 2020–2021, and 30.6% of records are from 2020 onwards. [src: paperblast_explorer]

The 2025 data has 125,438 records from 22,271 papers. [src: paperblast_explorer]

There are 1,425 records from 2026, which the report reads as a snapshot taken in early 2026. [src: paperblast_explorer]

### Background

PaperBLAST was created by Price & Arkin (2017) to connect protein sequences to relevant literature. [src: paperblast_explorer] Their later work on interactive functional-annotation tools (2024) and Curated BLAST (2019) developed the text-mining approach further. [src: paperblast_explorer]

## Caveats and Open Work

The "Unknown" domain class covers 14,798 organisms, so domain-level counts depend on name-based classification. [src: paperblast_explorer] The heuristic mapping classified 35% of organisms as Unknown, and a formal taxonomy lookup would improve accuracy. [src: paperblast_explorer]

The SwissProt subset is limited to entries matched to PMC open-access literature. [src: paperblast_explorer] Only 19% of SwissProt is in PaperBLAST, likely because many entries lack matching PMC full text. Curated knowledge therefore exists for proteins PaperBLAST cannot connect to. [src: paperblast_explorer]

Text-mined mentions do not imply functional characterization. The 65.6% of genes with 1 paper likely include many incidental mentions. [src: paperblast_explorer]

PaperBLAST mines full text only from PubMed Central. Paywalled papers are missed, which biases against fields and journals with lower open-access rates. [src: paperblast_explorer]

The 50% identity cutoff for "protein family" is conventional but arbitrary, not a universal biological boundary. [src: paperblast_explorer]

There are no negative controls, so genuinely unstudied genes cannot easily be told apart from genes whose literature text mining missed. [src: paperblast_explorer]

### Next analyses the report proposes

- Cross-reference with the Fitness Browser: use the 130K VIMSS links to find fitness-important genes that lack literature, as candidates for "high-impact understudied genes." [src: paperblast_explorer]
- Formal taxonomy integration: replace the heuristic domain classification with NCBI taxonomy lookup to quantify Bacteria/Archaea/Eukarya/Virus coverage accurately. [src: paperblast_explorer]
- Temporal trend analysis: track whether literature concentration is rising or falling, that is, whether a broader or narrower set of genes is studied each year. [src: paperblast_explorer]
- Dark family characterization: use AlphaFold structure prediction and domain annotation to infer putative functions for the 5,218 dark protein families. [src: paperblast_explorer]
- Literature graph analysis: build a gene-gene co-citation network from genepaper data to find functionally related but differentially studied gene clusters. [src: paperblast_explorer]

## Slots Into

- [[concepts/literature-coverage-bias-and-text-mining-limits]]: organism and gene concentration (Gini 0.967 and 0.669) quantifies the bias in text-mined literature. [src: paperblast_explorer]
- [[concepts/sequence-clustering-resolution-and-protein-family-definition]]: clusters at 90%, 50% and 30% identity give 628K, 345K and 215K groups. [src: paperblast_explorer]
- [[concepts/unstudied-protein-families-and-the-literature-defined-dark-proteome]]: 5,218 multi-member families have no literature, and 9.2% of 50%-identity families have zero papers. [src: paperblast_explorer]
