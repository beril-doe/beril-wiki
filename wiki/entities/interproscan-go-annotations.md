---
type: "Dataset"
description: "InterProScan-derived GO term annotations for pangenome cluster representatives, giving uniform coverage of Fitness Browser genes."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md"]
aliases: ["interproscan_go"]
---
# InterProScan GO annotations

InterProScan GO annotations (alias: interproscan_go) are Gene Ontology (GO) term annotations from InterProScan for pangenome cluster representatives. In the antimicrobial resistance (AMR) cofitness work they gave uniform coverage of Fitness Browser (FB) genes and turned a null enrichment result into a significant one. The evidence comes from one project, with a restatement in the discoveries digest. [src: amr_cofitness_networks, discoveries]

## Key facts

- The annotations come from the interproscan_go table in [[entities/kbase-ke-pangenome]]. The AMR cofitness report used it alongside interproscan_domains (Pfam) and bakta_annotations, for GO terms, Pfam domains and KEGG orthology of FB gene clusters. [src: amr_cofitness_networks] See also [[entities/pfam-domain-annotations]].
- The generated file data/fb_interproscan_go.csv holds 438,000 rows of InterProScan GO terms for FB gene clusters. [src: amr_cofitness_networks]
- The report gives gene coverage as 68%, which it calls 3.6× better than old SEED annotations. [src: amr_cofitness_networks, discoveries] Its comparison table lists InterProScan GO coverage as 60% uniform across all genes. Old SEED/KEGG coverage was 40–80% per organism and variable. [src: amr_cofitness_networks] The report states both figures (68% and 60%) and does not reconcile them.

## Comparison with old annotations

Uniform, higher coverage changed the enrichment results. With old annotations, 0 of 280 enrichment tests were significant at a false discovery rate (FDR) below 0.05. With InterProScan GO, 35 of 3,193 were. [src: amr_cofitness_networks, discoveries] No GO term was enriched in 3 or more organisms with old annotations. Six were with InterProScan GO, involving flagella and amino acid biosynthesis. [src: amr_cofitness_networks]

The old KEGG analysis gave p = 1.0 for cross-mechanism Jaccard exceeding within-mechanism Jaccard. InterProScan GO gave 4.3×10⁻¹³. [src: amr_cofitness_networks]

## Interpretation

The report concludes that genome-wide cofitness analyses need high-coverage, uniformly computed functional annotations, and that InterProScan on pangenome cluster representatives supplies them. [src: amr_cofitness_networks] It reads the null-to-significant change as showing that legacy annotations are insufficient for functional genomics. [src: amr_cofitness_networks] This is the report's own interpretation of one analysis. See [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]] and [[summaries/amr_cofitness_networks__REPORT]].
