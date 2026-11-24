---
type: "Concept"
description: "How annotation sources (Bakta, eggNOG, UniRef50 bridges, KO assignments) differ in coverage and reliability, including false positives for specialty marker genes, and which source to use for which analysis; stops at dark-gene biology."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/oak_ridge_cultivation_gap__REPORT.md"]
---
# Annotation source disagreement and coverage

This page covers how annotation sources differ in coverage and reliability. It is about Bakta, eggNOG, UniRef50 bridges and KO assignments. Neither Bakta nor eggNOG dominates: eggNOG covers more COG, KEGG and Pfam, and Bakta covers more GO terms, product descriptions and UniRef50 links. [src: discoveries] For the specialty markers lanmodulin and XoxJ, eggNOG Preferred_name 'lanM' returned 505 false positives and the generic KO K02030 hit 46,369 eggNOG entries, almost none of them xoxJ, while Bakta product was the trustworthy source. [src: lanthanide_methylotrophy_atlas, discoveries] The lanthanide atlas reports that eggNOG and Bakta calls disagree substantially for xoxJ, lanmodulin and PQQ (pyrroloquinoline quinone) biosynthesis, so it uses a calibrated source per marker. [src: lanthanide_methylotrophy_atlas] See [[entities/bakta]] and [[entities/eggnog-orthologous-groups]].

## Coverage differs by annotation type

Neither source dominates. eggNOG covers more of the enrichment-style categories, and Bakta covers more of the descriptive ones. [src: discoveries]

- eggNOG has higher coverage for clusters of orthologous groups (COG) (51% vs 8.2%), KEGG (38.5% vs 17.3%) and Pfam (63% vs 7.7%). [src: discoveries]
- Bakta has higher coverage for Gene Ontology (GO) terms (15% vs 7.4%) and product descriptions (71.2% vs 70.4%). It is also the only source of UniRef50 links, at 79.2%. [src: discoveries]
- The union of the two sources raises any-functional-annotation coverage from ~70% to 77.3%. Bakta rescues 11.2M clusters (of 39.2M) that eggNOG misses entirely. [src: discoveries]
- On this basis the report considers eggNOG the better current source for COG/KEGG/Pfam enrichment analysis. [src: discoveries]

In the AMR (antimicrobial resistance) pangenome analysis, 93.0% of AMR clusters have both Bakta product annotations and eggNOG hits. The remaining 7.0% have Bakta annotations only. [src: amr_pangenome_atlas] Sparsely annotated (1-source) AMR clusters are enriched for singletons (55.4% vs 34.6%). [src: amr_pangenome_atlas] Zero AMR clusters have Pfam domain hits in `bakta_pfam_domains`. The report suggests AMRFinderPlus and Pfam HMM scans target non-overlapping sequence space for these families. [src: amr_pangenome_atlas]

In the annotation-gap leave-one-out cross-validation, Bakta alternative annotations added 22 newly resolved pairs (10.9%) and yielded 1,459 Bakta EC (Enzyme Commission) candidate entries. [src: annotation_gap_discovery] The NB04 alone configuration also resolved 22 pairs (10.9%). [src: annotation_gap_discovery]

### Pipeline sensitivity in the cultured–MAG comparison

A separate report compares eggNOG KO (KEGG ortholog) calls with Genome Depot. Per-genome Jaccard similarity is low (median 0.140, IQR 0.057–0.400). The report attributes this to eggNOG calling a narrower KO set per genome, typically ~1,000–1,800 KOs versus ~1,500–2,200 for Genome Depot, which inflates the union denominator. [src: oak_ridge_cultivation_gap] It reads the gap as consistent with pipeline sensitivity differences, not systematic disagreement about which functions are present. [src: oak_ridge_cultivation_gap] It cautions that systematic sensitivity differences between pipelines could still bias the cultured–MAG (metagenome assembled genomes) comparison, though KO-level comparison is more robust than pathway-level. [src: oak_ridge_cultivation_gap]

## Why Bakta's COG, KEGG and Pfam coverage is low

The report attributes the low figures to Bakta's design. It cites confirmation from the Bakta developer across GitHub issues #350, #385, #391 and #393. [src: discoveries]

- Bakta's PSC database is optimized for product descriptions, not functional categories. Only ~14% of PSC entries have COG and ~19% have KEGG. [src: discoveries]
- COG 2024 no longer provides representative sequences. This forces a lossy indirect WP accession→IPS→PSC mapping. [src: discoveries]
- HMMER runs only on hypotheticals (~7.7%). The 92% with PSC matches never get Pfam searched. [src: discoveries]
- Bakta's PSC uses DIAMOND fast mode, while eggNOG uses HMM-based ortholog assignment, which the report describes as more sensitive. [src: discoveries]
- The developer planned to integrate eggNOG into PSC representatives (issue #325). This may have partly happened in DB v6.0, but with limited impact. [src: discoveries]
- The report states that the Arche benchmark paper (Alonso-Reyes & Albarracin 2025, PMID 40811208) independently confirmed Bakta's conservative annotation transfer relative to other tools. [src: discoveries]

## UniRef50 bridges

Only 33.3% of Bakta's 17.6M distinct UniRef50 IDs exist in `kbase_uniprot.uniprot_identifier`. [src: discoveries] For the IDs that match, the bridge reaches RefSeq (71%), OrthoDB (46%), STRING (40%) and KEGG (36%). [src: discoveries] GO, EC, InterPro and Pfam are missing from the bridge. The report says importing full UniProt would unlock them. [src: discoveries] See [[entities/uniref]].

Bridges still help for unannotated genes. Of the 6,427 genes that stay hypothetical in both the Fitness Browser (FB) and Bakta, 79.4% gain UniRef50 links, 69.1% gain UniParc/UniRef100 links, and 62.4% gain RefSeq links. [src: functional_dark_matter]

## False positives for specialty markers

For specialty markers, the report's calibration finds that Bakta's curated product field outperforms eggNOG's Preferred_name. It describes this as generalizable beyond rare-earth-element biology. [src: lanthanide_methylotrophy_atlas]

### Cross-source agreement by marker

The agreement analysis counts genomes in a 134,578-row hit-bearing matrix. [src: lanthanide_methylotrophy_atlas] The table gives each marker's counts and the source the report trusts.

| Marker | Both | eggNOG only | Bakta only | Report's choice |
|---|---|---|---|---|
| lanmodulin | 0 | 505 | 62 | Bakta only; eggNOG Preferred_name='lanM' is noise [src: lanthanide_methylotrophy_atlas] |
| xoxJ | 41 | 46,369 | 20 | Bakta only; KO K02030 is non-specific [src: lanthanide_methylotrophy_atlas] |
| xoxF | 418 | 3,272 | 1,402 | eggNOG K00114 primary, Bakta as union [src: lanthanide_methylotrophy_atlas] |
| mxaF | 4 | 191 | 8 | eggNOG K14028 [src: lanthanide_methylotrophy_atlas] |
| pqqA-E | varied | varied | 50–90K | Bakta over-calls; eggNOG primary [src: lanthanide_methylotrophy_atlas] |

### Lanmodulin

Across 134K pangenome genomes, the two sources for lanmodulin disagree completely. [src: discoveries]

- Bakta product='Lanmodulin' flags 62 genomes, all in α-Proteobacterial methylotroph clades (Beijerinckiaceae *Methylobacterium*, Acetobacteraceae BOG-930, Hyphomicrobiaceae). [src: discoveries, lanthanide_methylotrophy_atlas]
- eggNOG Preferred_name='lanM' flags 505 additional genomes, none of them Bakta-validated. They concentrate in unrelated gut Bacillota that are not lanthanide users: *Streptococcus pneumoniae* 10, *Blautia_A wexlerae* 9, *Enterococcus faecalis* 8, *Ruminococcus_B gnavus* 8 and *Streptococcus pyogenes* 7. [src: discoveries, lanthanide_methylotrophy_atlas]
- The report calls these 505 hits false positives. It suggests the eggNOG labelling is stale or a propagated misannotation, not a true homology call, and says it is worth reporting upstream. [src: discoveries, lanthanide_methylotrophy_atlas]
- The report says the pattern is likely a single seed-ortholog label that has propagated, concentrated in a handful of *Streptococcus*, *Blautia* and *Enterococcus* species, and proposes reporting it to the eggNOG-mapper team. [src: lanthanide_methylotrophy_atlas]
- Guidance: use Bakta product='Lanmodulin' exclusively for lanmodulin analyses. Treat eggNOG Preferred_name='lanM' as zero-information. [src: discoveries, lanthanide_methylotrophy_atlas]

### XoxJ and KO K02030

K02030 is the generic KEGG ortholog for the amino acid ABC (ATP-binding cassette) transporter substrate-binding protein family. [src: discoveries] Filtering eggNOG by KEGG_ko LIKE '%K02030%' returns 46,369 hits across nearly every phylum, almost none of them xoxJ. [src: discoveries] The specific Bakta product call ("rare earth element methanol dehydrogenase accessory protein XoxJ") matches just 61 genomes. [src: discoveries] The report finds K02030 non-specific for xoxJ. It recommends the Bakta product or eggNOG Preferred_name='xoxJ', and never K02030 as a proxy. [src: discoveries, lanthanide_methylotrophy_atlas]

### xoxF

The eggNOG-only set (3,272 genomes) appears to include Bakta entries labeled Putative dehydrogenase XoxF, which the report's regex missed, plus other generic dehydrogenases that hit K00114. [src: discoveries] The Bakta-only set (1,402) includes lanthanide-dependent ethanol dehydrogenase variants that the KEGG KO filter excludes. [src: discoveries] The report recommends reporting results both ways, with the eggNOG-K00114 set as primary and either-source as inclusive. It also says to disclose the gap and to name the source behind any xoxF count. [src: discoveries] See [[entities/xoxf-lanthanide-dependent-methanol-dehydrogenase]].

## Limits of annotation-bounded atlases

The lanthanide atlas is bounded by what eggNOG and Bakta call. It would not detect genuinely novel rare-earth-element-handling enzymes that lack KEGG/RefSeq homologs. [src: lanthanide_methylotrophy_atlas] Headline statistics use the calibrated source per marker, with union-of-sources analyses reported alongside. [src: lanthanide_methylotrophy_atlas] The report also finds no lanthanide or methanol coverage in BacDive `metabolite_utilization`. [src: lanthanide_methylotrophy_atlas]

## Reclassifying "hypothetical" genes

Of 39,532 dark genes with pangenome links, Bakta reclassifies 33,105 (83.7%) as not hypothetical. Its PSC/PSCC pipeline assigns product descriptions where the Fitness Browser had only "hypothetical protein". [src: functional_dark_matter] These make up 58.1% of all dark genes. [src: functional_dark_matter] The report interprets this as independent validation of experimental prioritization. It says the dark genes with the strongest fitness effects tend to be annotated in UniProt but absent from the Fitness Browser's annotation vintage. [src: functional_dark_matter] This page stops here. See [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]] for the dark-gene biology.

## Which source for which analysis

- Use eggNOG for COG, KEGG and Pfam enrichment analysis. [src: discoveries]
- Use Bakta for product descriptions, GO terms and UniRef50 links, and to rescue clusters eggNOG misses. [src: discoveries]
- Use Bakta product for lanmodulin and XoxJ. [src: discoveries, lanthanide_methylotrophy_atlas]
- For xoxF, report both sources, with eggNOG K00114 primary. [src: discoveries, lanthanide_methylotrophy_atlas]
- For mxaF, the report trusts eggNOG K14028. For pqqA-E it uses eggNOG as primary because Bakta over-calls. [src: lanthanide_methylotrophy_atlas]

## Open Directions

- Test whether the Bakta-product advantage for specialty markers holds beyond lanmodulin and XoxJ. One approach is to calibrate other rare, curated markers against eggNOG Preferred_name and KO. This would check whether the "generalizable pattern" claim holds.
- Re-run the xoxF comparison with a regex that includes "Putative dehydrogenase XoxF". Then split the 3,272 eggNOG-only genomes into true xoxF and generic dehydrogenases.
- Import full UniProt into the KBase Data Lakehouse. Measure how many GO, EC, InterPro and Pfam annotations it adds through the UniRef50 bridge, which currently matches only 33.3% of Bakta IDs.
- Check whether the stale eggNOG lanM label traces to specific seed orthologs, then report it upstream.
- Quantify how Bakta's HMMER-on-hypotheticals-only design biases Pfam-based marker detection. Compare against a full Pfam scan on a sample of clusters.
- Re-test the Bakta over-calling of pqqA-E (50–90K Bakta-only genomes) against a stricter product filter, to see how many calls survive.
