---
type: "Concept"
description: "Covers measuring whether acquired gene families are mobile-element machinery or cargo, via per-cluster product keywords and gene-neighborhood scans, and what these measures cannot detect."
sources: ["summaries/costly_dispensable_genes__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md"]
---
# Mobile genetic element context of horizontally acquired gene families

This page covers measuring whether acquired gene families are mobile-element machinery or cargo, using per-cluster product keywords and gene-neighborhood scans, and what these measures cannot detect. Per-cluster keywords are a direct but limited measurement. The neighborhood scan was completed for photosystem II (PSII) only, and both measures have blind spots. [src: gene_function_ecological_agora] See also [[summaries/gene_function_ecological_agora__REPORT]] and [[summaries/costly_dispensable_genes__REPORT]].

## Literature Context

The candidate papers show that horizontally acquired genes are often carried as cargo inside defined mobile genetic elements (MGEs), and that finding that cargo requires genomic-context analysis. A census of 6,549 Tn7-like transposons found that 96% carry at least one cargo gene. That cargo is significantly enriched in nested MGEs such as insertion sequences and toxin-antitoxin modules, and in recombination, anti-MGE defense and antibiotic-resistance genes. It also includes central carbon metabolism enzymes [PMID 34872347](https://pubmed.ncbi.nlm.nih.gov/34872347/). That work depended on a computational method for delineating transposon boundaries, because cargo is hard to separate from its surrounding context. In Vibrionaceae, CRISPR-Cas systems were found predominantly within MGEs (genomic islands, plasmids and transposon-like elements), and a mini type I-F system was always associated with Tn7-like transposons. Phylogenetic analysis indicated these systems were acquired by horizontal gene transfer [PMID 30717668](https://pubmed.ncbi.nlm.nih.gov/30717668/). Related work shows that mosaic integrative and conjugative elements (ICEs) can recombine and carry resistance cargo. One example is the roughly 110 kb ICESag236 from two clinical Streptococcus agalactiae strains [PMID 27621174](https://pubmed.ncbi.nlm.nih.gov/27621174/). Long-read target-enrichment sequencing (TELSeq) recovered MGEs and cargo genes flanking low-abundance resistance genes in metagenomes. Short-read metagenomics could not do this, and the authors read the flanking context as indicating possible transfer across taxa [PMID 36324140](https://pubmed.ncbi.nlm.nih.gov/36324140/). In Mycobacterium abscessus, a toxin-antitoxin system inside an MGE likely enforces retention of the MGE and its cargo. This was shown in two clinical strains, and the authors describe the mechanism as similar to postsegregational killing [PMID 42867246](https://pubmed.ncbi.nlm.nih.gov/42867246/).

The corpus's keyword results are consistent with this picture in a limited way. In the costly_dispensable_genes report, costly+dispensable genes were more likely than costly+conserved genes to carry mobile-element product keywords (OR=7.45, p=4.6e-71). That is an annotation-text enrichment, not evidence that these genes sit next to MGE machinery or inside nested MGEs. It is compatible with the enrichment of insertion sequences and recombination genes reported in Tn7-like cargo [PMID 34872347](https://pubmed.ncbi.nlm.nih.gov/34872347/), but it does not test it. The report's own proposed genomic-island and tRNA-proximity analysis would be the comparable step.

The gene_function_ecological_agora results sit in tension with how the literature establishes mobility. The report found 0.57% (Mycobacteriaceae mycolic-acid), 0.00% (PSII) and 0.00% (PUL) MGE-machinery fractions among recent gains. It concluded that these genes flow by chromosomal recombination and ICEs rather than phage transduction. The papers above show that cargo is identified through context, not through machinery keywords on the cargo itself. Absence of machinery keywords therefore does not exclude MGE carriage, and the report concedes that keywords miss cargo. Only the PSII neighborhood scan was completed, and it found 10.91% of focal features with an MGE neighbor within ±5kb, close to the Poisson expectation of about 10.6%. For PUL and mycolic acid the non-phage-borne conclusion rests on machinery absence alone, and the ICE explanation rests on literature rather than the report's own data. The ICE literature here (for example [PMID 27621174](https://pubmed.ncbi.nlm.nih.gov/27621174/)) shows ICEs carrying cargo, but it concerns streptococci and does not test PUL transfer.

The report's reading of the CRISPR-Cas recent skew as mobile-element-borne agrees with the Vibrionaceae finding that CRISPR-Cas systems sit predominantly on MGEs [PMID 30717668](https://pubmed.ncbi.nlm.nih.gov/30717668/). The corpus's per-cluster and PSII scan approach is a coarse, scalable measure. The context-based methods in the papers suggest what would extend it: ICE-aware and boundary-aware detection.

## Per-cluster product keywords

Keyword matching on gene descriptions can show whether a gene set is enriched for mobile-element (MGE) machinery. It cannot show whether a gene travels on a mobile element. The KBase Data Lakehouse does not ingest genomad_mobile_elements (catalog-verified), so the available signal is bakta_annotations.product keyword matching. The terms are phage, transposase, integrase, plasmid, IS-element, recombinase and conjugation, across all 132M gene_clusters. [src: gene_function_ecological_agora]

In the costly_dispensable_genes report, costly+dispensable genes were 7.45x more likely than costly+conserved genes to contain mobile-element keywords (OR=7.45, p=4.6e-71). The keywords were transposase, integrase, phage, IS element, recombinase and prophage. [src: costly_dispensable_genes] That report proposes genomic context analysis (genomic islands, tRNA proximity, scaffold edges, which it calls hallmarks of horizontal gene transfer) as a next step. [src: costly_dispensable_genes] See mobile element origin of costly non conserved genes and [[entities/insertion-sequence-elements]].

In the atlas, 1.37% of KEGG ortholog (KO)-bearing gene_clusters carry MGE-context products (248,908 of 18,204,007). [src: gene_function_ecological_agora] Biome-stratified rates were similar (~1.1–2.0%), with no strong biome-specific elevation. [src: gene_function_ecological_agora]

The three pre-registered hypothesis KO sets showed near-zero MGE-machinery fractions among recent gains: [src: gene_function_ecological_agora]

| Set | Recent gains | Mean MGE-machinery fraction |
|---|---|---|
| Mycobacteriaceae × mycolic-acid | 6,683 | 0.57% [src: gene_function_ecological_agora] |
| Cyanobacteriia × PSII | 236 | 0.00% [src: gene_function_ecological_agora] |
| Bacteroidota × polysaccharide utilization locus (PUL) | 1,023 | 0.00% [src: gene_function_ecological_agora] |

The report reads this as showing that these KOs are not themselves phage, transposase, integrase or plasmid genes. [src: gene_function_ecological_agora] By KO category, regulatory KOs had a ~10× higher MGE-machinery rate (4.13%) than metabolic (0.37%) or mixed (0.27%) KOs. The report calls this consistent with transposon-bound and phage-bound regulators. [src: gene_function_ecological_agora] See [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]].

## Gene-neighborhood scan

The PSII neighborhood scan asks whether MGE genes sit near focal genes. It covered 27,148 focal features and 218,321 neighbor pairs in Cyanobacteriia. [src: gene_function_ecological_agora] The mean MGE-neighbor fraction was 1.65%, close to the atlas rate of 1.37%. [src: gene_function_ecological_agora] A total of 10.91% of focal features had at least one MGE neighbor within ±5kb. [src: gene_function_ecological_agora] A Poisson baseline with p = 0.014 and about 8 neighbors predicts about 10.6%. [src: gene_function_ecological_agora] The report therefore finds no MGE-cargo enrichment for PSII. [src: gene_function_ecological_agora] It also asserts that this rules out PSII gains traveling as phage/MGE cargo. [src: gene_function_ecological_agora]

Individual subunits varied. The report reads the spread (3.5% to 22.1%) as suggesting differential mobility within the complex, while the ensemble mean sits at baseline. [src: gene_function_ecological_agora]

| KO | Subunit | Features | With MGE neighbor |
|---|---|---|---|
| K02720 | PsbZ | 1,769 | 22.1% [src: gene_function_ecological_agora] |
| K02718 | PsbX/M | 1,500 | 15.5% [src: gene_function_ecological_agora] |
| K02704 | PsbB (CP47) | 1,794 | 14.2% [src: gene_function_ecological_agora] |
| K02703 | PsbA (D1) | 4,217 | 13.7% [src: gene_function_ecological_agora] |
| K02710 | PsbE | 1,188 | 12.6% [src: gene_function_ecological_agora] |
| K02716 | PsbV | 1,386 | 3.5% [src: gene_function_ecological_agora] |

## What these measures cannot detect

Keyword matching detects MGE machinery genes but not cargo genes carried on MGEs without synteny analysis. [src: gene_function_ecological_agora] The neighborhood analysis also cannot detect Integrative Conjugative Element (ICE)-mediated transfer for Bacteroidota PUL. [src: gene_function_ecological_agora] The report had deferred the PUL scan for scale and cited literature consensus on ICE-mediated transfer (Sonnenburg 2010). [src: gene_function_ecological_agora]

The scale failures were as follows:
- The Bacteroidota scan failed because even the two-KO SusC/SusD set gave 723K focal features × 210K contigs. The 1.3GB serialized result exceeded spark.driver.maxResultSize. [src: gene_function_ecological_agora]
- A 309-species sample still gave 80K focal features × 21K contigs, a ~24M-row pandas merge, and an out-of-memory failure on the 9GB DataFrame. [src: gene_function_ecological_agora]
- The Mycobacteriaceae sampled run never started. [src: gene_function_ecological_agora]

See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

## Interpretation and its limits

The report shipped without PUL or mycolic neighborhood scans. It argued that they would refine the picture but not change the headline. [src: gene_function_ecological_agora] It treats the per-cluster results (0%/0.57%) as sufficient for a non-phage-borne conclusion. [src: gene_function_ecological_agora] It also reports PSII at 0% machinery with neighborhood association at baseline. [src: gene_function_ecological_agora]

The mechanism claim rests on literature, not on the report's own scans. It cites chromosomal mycolic-acid operons (Marrakchi 2014) and ICE-mediated PUL transfer (Sonnenburg 2010). [src: gene_function_ecological_agora] It concludes that these genes flow by chromosomal recombination and ICEs rather than phage transduction. [src: gene_function_ecological_agora] The measured support is a keyword result for all three sets and a neighborhood result for PSII only. Because keywords miss cargo, the non-phage-borne conclusion for PUL and mycolic acid rests on machinery absence alone. [src: gene_function_ecological_agora]

By contrast, the report reads the CRISPR-Cas recent skew as consistent with dispersal mainly by mobile-element-borne transfers, aligned with Metcalf et al. 2014. [src: gene_function_ecological_agora] See [[entities/crispr-cas]].

## Tensions

- The report says PSII baseline results rule out MGE cargo. [src: gene_function_ecological_agora] The same report says keyword matching cannot detect cargo without synteny. [src: gene_function_ecological_agora] The neighborhood scan also cannot see ICE transfer. [src: gene_function_ecological_agora]
- PSII subunit rates range from 3.5% to 22.1%. [src: gene_function_ecological_agora] The ensemble mean of 10.91% is at the baseline. [src: gene_function_ecological_agora]

## Open Directions

- Run batched or sampled PUL and mycolic neighborhood scans, using Spark-side aggregation instead of pandas merges. This would close the gap left by the scale failures.
- Ingest genomad_mobile_elements or an equivalent MGE caller, to replace product-keyword matching with a detector independent of annotation text.
- Add ICE-specific detection, such as relaxase and integrase near PUL loci, to test ICE transfer directly.
- Test whether elevated PSII subunits (for example PsbZ at 22.1%) differ from baseline, using per-subunit Poisson expectations.
- Run genomic-island, tRNA-proximity and scaffold-edge analysis for costly+dispensable genes.
