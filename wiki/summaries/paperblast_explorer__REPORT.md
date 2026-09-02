---
type: "Summary"
description: "Quantifies severe literature bias and dark protein-family coverage in PaperBLAST"
doc_type: "short"
full_text: "sources/paperblast_explorer__REPORT.md"
---
# PaperBLAST Data Explorer — Literature Coverage Bias in Protein Sequence Space

## Overview

This analysis characterizes the BERDL `kescience_paperblast` collection, which contains 12.4 million rows across 14 tables linking protein sequences and genes to literature, curated annotations, structural data, and snippets from PubMed Central full-text articles. It combines database inventory, organism- and gene-level coverage analysis, Lorenz inequality curves, and MMseqs2 sequence clustering to quantify research concentration and identify poorly studied protein families. [src: paperblast_explorer]

## Key Findings

### Literature is concentrated in a small number of organisms

*Homo sapiens* accounts for **46.7%** of all gene-paper records in PaperBLAST. The top five organisms—*H. sapiens*, *M. musculus*, *R. norvegicus*, *A. thaliana*, and *D. melanogaster*—account for **72.8%**. Of **20,723** organisms with any literature, the top **1,000** capture **94.2%**, leaving the remaining **19,723** organisms with **5.8%** of the literature. [src: paperblast_explorer]

### Gene-level literature coverage is highly skewed

Of **841K** genes with any text-mined paper link, **551K (65.6%)** have exactly one paper. The median is **1** paper per gene and the mean is **3.8**. The 50 most-referenced genes are all human; the leading examples are p53 with **9,988** papers, TNF with **6,002**, and EGFR with **5,895**. Only **6%** of genes (**50K**) account for **57.7%** of all gene-paper links. [src: paperblast_explorer]

### Lorenz curves show extreme inequality

The organism-level Gini coefficient is **0.967**, while the gene-level Gini coefficient is **0.669**; these values indicate near-total concentration of organism literature and very high concentration of gene literature, respectively. [src: paperblast_explorer]

### Bacterial literature favors pathogens and model organisms

Among **15,312** bacterial organisms, the top **100** capture **44.3%** of bacterial literature. The three leading bacteria are *Mycobacterium tuberculosis* H37Rv with **9,079** papers, *Escherichia coli* K-12 with **8,860**, and *Pseudomonas aeruginosa* PAO1 with **5,928**. The report finds environmental and non-pathogenic organisms dramatically underrepresented. [src: paperblast_explorer]

### Sequence clustering reduces the collection to protein families and superfamilies

Clustering **815,571** PaperBLAST protein sequences with MMseqs2 produced **628K** clusters at **90%** identity, **345K** clusters at **50%** identity, and **215K** clusters at **30%** identity. These correspond respectively to low strain-level redundancy, a protein-family scale, and a superfamily scale. The largest 50%-identity families include HSP70/BiP with **650** members, GAPDH with **609**, enolase with **552**, and GroEL with **443**. [src: paperblast_explorer]

At **90%** identity, **83.3%** of clusters are singletons; at **50%**, **67.5%** are singletons; and at **30%**, **62.8%** are singletons. The largest 90%-identity cluster is actin with **212** members. [src: paperblast_explorer]

### More than half of protein families are dark or dimly studied

At **50%** identity, **9.2%** of protein families (**31,653**) have zero papers across all members, and **46.1%** (**159,046**) have exactly one paper. Only **4.3%** (**14,904**) have **20 or more** papers. In total, **5,218** multi-member families representing **14,534** sequences have no literature whatsoever. The report describes these as dark protein families. [src: paperblast_explorer]

Family size is positively associated with literature coverage: **95.4%** of multi-member 50%-identity clusters have at least one member with a paper, while the remaining **4.6%**—**5,218** families—have none. The dark families are dominated by REBASE methyltransferases and biolip structural entries, which the report characterizes as specialized proteins lacking published functional studies. [src: paperblast_explorer]

## Database Scale and Coverage

The collection contains **12.4 million rows** across 14 tables. Its largest listed tables are `genepaper` with **3,195,890** gene-to-paper links, `site` with **2,089,192** PDB binding, active, and modified-site records, `snippet` with **1,951,949** text excerpts, `generif` with **1,358,798** GeneRIF functional summaries, `gene` with **1,135,366** gene/protein records, `uniq` with **815,571** unique protein sequences, `curatedpaper` with **599,587** curated gene-paper links, and `curatedgene` with **255,096** curated annotations. [src: paperblast_explorer]

The database covers papers from **1951 to 2026**. Publications peak around **2020–2021**, **30.6%** of records are from 2020 onwards, the 2025 data includes **125,438** records from **22,271** papers, and **1,425** records from 2026 are present, indicating an early-2026 snapshot. [src: paperblast_explorer]

The **1.1M** genes span **27,718** organisms across all domains of life. Bacteria account for **5,997** organisms and **397,544** genes (**35.0%** of genes); Unknown classifications account for **14,798** organisms and **397,511** genes (**35.0%**); Eukarya account for **822** organisms and **290,537** genes (**25.6%**); viruses account for **5,730** organisms and **27,199** genes (**2.4%**); and Archaea account for **371** organisms and **22,575** genes (**2.0%**). [src: paperblast_explorer]

The report describes **845K** genes linked to **1.1M** unique papers through **3.2M** many-to-many associations; each gene averages **3.8** papers and each paper mentions **2.9** genes. It also reports that **25.6%** of genes in the gene table (**290K**) have no text-mined paper link and rely solely on curated or GeneRIF annotations. [src: paperblast_explorer]

SwissProt contributes **110,171** proteins and **181,916** unique papers, while biolip contributes **42,571** proteins and **23,768** papers, BRENDA **33,012** proteins and **43,760** papers, MetaCyc **12,700** proteins and **46,176** papers, and EcoCyc **4,198** proteins and **22,304** papers. Their reported papers-per-protein values are respectively **1.7**, **0.6**, **1.3**, **3.6**, and **5.3**. The report states that PaperBLAST includes approximately **19%** of the full SwissProt database, estimated there as approximately **570K** reviewed entries as of 2024. [src: paperblast_explorer]

PaperBLAST includes site annotations for **132,179** PDB structures and **2.1M** site records across binding (**1.69M**), functional (**182K**), modified (**112K**), and mutagenesis (**104K**) types. It contains **48,991** unique ligands; the most frequent listed ligands are zinc ions with **65K** sites, chlorophyll A with **58K**, calcium ions with **53K**, and heme with **44K**. [src: paperblast_explorer]

A cross-database linkage analysis identified **129,823** VIMSS cross-references connecting PaperBLAST to the Fitness Browser, providing a route from literature coverage to experimental fitness phenotypes. [src: paperblast_explorer]

## Interpretation and Contribution

The report interprets the concentration of research on a small number of genes and organisms as consistent with a self-reinforcing “rich-get-richer” dynamic previously described for gene attention. It connects the protein-family results to the dark proteome and functional unknomics, extending the literature-coverage perspective to **5,218** multi-member protein families with zero coverage at **50%** identity. [src: paperblast_explorer]

The novel contribution is a collection-level and protein-family-level characterization of the BERDL-hosted PaperBLAST resource, including Lorenz analyses, per-domain coverage, sequence clustering, and presentation-ready figures quantifying the research coverage gap. [src: paperblast_explorer]

## Caveats

- Text mining is not equivalent to functional characterization: a gene mentioned in a paper may be tangential to the study, and the **65.6%** of genes with one paper may include incidental mentions. [src: paperblast_explorer]
- PaperBLAST mines PubMed Central full-text articles, so papers behind paywalls are missed; this creates systematic bias against fields and journals with lower open-access rates. [src: paperblast_explorer]
- Domain classification is approximate: a heuristic organism-to-domain mapping classified **35%** of organisms as Unknown, and a formal taxonomy lookup would improve accuracy. [src: paperblast_explorer]
- Clustering identity thresholds are arbitrary: the **50%** identity cutoff used for “protein family” is conventional and does not represent a universal biological boundary. [src: paperblast_explorer]
- SwissProt coverage is partial: only **19%** of SwissProt is in PaperBLAST, likely because many entries lack matching PMC full-text; curated knowledge therefore exists for proteins that PaperBLAST cannot connect to. [src: paperblast_explorer]
- The analysis has no negative controls and cannot easily distinguish genuinely unstudied genes from genes whose literature was missed by text mining. [src: paperblast_explorer]

## Slots Into

- [[concepts/gene-function-acquisition-depth]] — The organism-, gene-, and protein-family coverage distributions quantify how unevenly functional knowledge is acquired and identify dark protein families for follow-up. [src: paperblast_explorer]
- [[concepts/provenance-aware-resource-discovery]] — The collection inventory, table-level provenance, sequence-clustering outputs, and explicit PMC/open-access limitations characterize how resource construction shapes discoverability. [src: paperblast_explorer]
- [[concepts/cross-tenant-data-bridging]] — The **129,823** VIMSS cross-references provide a concrete bridge between PaperBLAST literature coverage and Fitness Browser phenotypes. [src: paperblast_explorer]
