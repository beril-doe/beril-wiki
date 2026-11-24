---
type: "Concept"
description: "How incomplete COG/eggNOG annotation, composite categories, choice of domain-annotation source and per-genome annotation density change functional-enrichment conclusions and atlas scores."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/cog_analysis__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md", "summaries/ecotype_functional_differentiation__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/pitfalls.md"]
---
# Annotation coverage and annotation-density bias in functional enrichment

This page covers how incomplete annotation, composite categories, the choice of annotation source and per-genome annotation density change functional-enrichment conclusions and atlas scores. Annotation is uneven across gene classes, and in ADP1 essential genes are far better annotated than dispensable ones. [src: acinetobacter_adp1_explorer] The choice of domain-annotation source can decide whether a test is possible at all: in the gene-function atlas, one Pfam table had no hits for the key photosystem II (PSII) markers. [src: gene_function_ecological_agora] Where annotation density was tested directly in the atlas, it changed no verdict. [src: gene_function_ecological_agora]

## Coverage differs by gene class

In the ADP1 database, annotated genes are not a random sample. 33% of essential genes have COG (clusters of orthologous groups) assignments versus 5% of dispensable genes. [src: acinetobacter_adp1_explorer] 92% of essential genes have KEGG KO (KEGG ortholog) assignments versus 53% of dispensable genes. [src: acinetobacter_adp1_explorer] The database's overall functional annotation coverage via COG/KO/Pfam/UniRef is 34-55%. [src: acinetobacter_adp1_explorer] See [[concepts/annotation-and-pangenome-correlates-of-gene-essentiality]].

In the cog_analysis report, COG annotations cover ~70% of genes, and unassigned genes may skew distributions. [src: cog_analysis] That report also notes that eggNOG v6 annotations may differ from original COG assignments. [src: cog_analysis] It used 32 species, and a larger sample might reveal phylum-specific patterns. [src: cog_analysis]

An ecotype study raises the same concern. It says the 62% of gene clusters without annotations may contain ecotype-specific adaptive genes in poorly characterized categories. That could bias results toward well-annotated housekeeping functions. [src: ecotype_functional_differentiation] See also [[concepts/annotation-source-disagreement-and-coverage]].

## Composite categories

The cog_analysis report counts multi-letter COG categories once per gene instead of splitting them. [src: cog_analysis] It argues they should not be filtered out as noise, because they represent genuine multi-functional genes. [src: cog_analysis] Examples are "LV" (mobile+defense) and "EGP" (amino acid+carb+inorganic ion). The report says these are not annotation artifacts. [src: cog_analysis, discoveries] LV shows +0.34% enrichment with 76% consistency. [src: discoveries] The report suggests this reflects functional modules such as "mobile defense islands". [src: discoveries] In the same analysis, novel/singleton genes show +1.64% enrichment for COG S (Unknown function), with 69% consistency. [src: cog_analysis] See [[entities/clusters-of-orthologous-groups-functional-categories]].

There is also a coding pitfall. In cog_analysis, composite categories such as LV and EGP map to NaN (not a number) when they are absent from a description dictionary, and string operations on those NaN values fail. [src: pitfalls] The recommended fix is to use pd.notna() or pd.isna() before string slicing or other operations on columns that may hold NaN. [src: pitfalls]

## Keyword categorization undercounts

In Bacillota_B subsurface accessory genes, the keyword scanner missed a substantial fraction of anaerobic-niche signals. Those signals are encoded by gene-family or domain names, not by the pre-registered keywords. [src: bacillota_b_subsurface_accessory] The 462-OG (ortholog group) "other_or_unannotated" bucket holds real anaerobic-respiration and electron-transfer signal. [src: bacillota_b_subsurface_accessory] Examples are COG1977 molybdopterin, DsrEFH and 2-oxoglutarate ferredoxin oxidoreductase. [src: bacillota_b_subsurface_accessory] The report estimates that manual reclassification would put the H1-relevant total closer to 80–100 of 547. The scanner's anaerobic-respiration count was 42. [src: bacillota_b_subsurface_accessory] It proposes an LLM-based pass over eggNOG `Description` and bakta `product` text for accurate counts. [src: bacillota_b_subsurface_accessory] See [[concepts/limits-of-keyword-and-marker-based-functional-annotation]].

## Choice of annotation source

Bakta and eggNOG cover different things. Bakta has higher GO (Gene Ontology) term coverage than eggNOG, 15% vs 7.4%. [src: discoveries] The union of the two raises any-functional-annotation coverage from ~70% to 77.3%. [src: discoveries] Bakta rescues 11.2M clusters (of 39.2M) that eggNOG misses entirely. [src: discoveries] The report still considers eggNOG the better source for COG/KEGG/Pfam enrichment analysis for now. [src: discoveries] See [[entities/bakta]].

The domain source matters too. The pilot's first control detection used `eggnog_mapper_annotations.PFAMs`, which stores domain names such as HisKA, not accessions such as PF00512. [src: gene_function_ecological_agora] Adding InterProScan accessions raised detected ribosomal-protein UniRef50s from 9,005 to 19,389 (2.2×). [src: gene_function_ecological_agora] tRNA synthetases rose from 5,640 to 8,514 (1.5×). [src: gene_function_ecological_agora] TCS (two-component system) HKs (histidine kinases) rose from 38,488 to 43,217 (1.1×). [src: gene_function_ecological_agora] The initial implementation went through 8 iterations of bug-fixing before the substrate audit, and results stabilized after the switch to InterProScan. [src: gene_function_ecological_agora] The report recommends InterProScan `interproscan_domains` as the default substrate for domain-accession queries. [src: gene_function_ecological_agora] It uses it as the authoritative Pfam source. [src: gene_function_ecological_agora] The report presents "audit substrate before implementing" as a methodological pattern. [src: gene_function_ecological_agora] See [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]] and [[entities/kbase-ke-pangenome]].

A later audit of marker Pfams reproduced the pitfall. 7 of 33 marker Pfams had zero clusters in `bakta_pfam_domains`, including all 4 critical PSII Pfams: PsbA/PF00124, PsbB/PF02530, PsbC/PF02533 and PsbD/PF00421. [src: gene_function_ecological_agora] `interproscan_domains` had only 1 zero-coverage marker, PF13415, a minor HATPase variant. [src: gene_function_ecological_agora] The median bakta/IPS coverage ratio was 0.102, with IPS showing ~10× higher coverage on average. [src: gene_function_ecological_agora] The report therefore selected `interproscan_domains` for all Phase 3 architectural work, which eliminated the planned HMMER recomputation fallback. [src: gene_function_ecological_agora] It notes the Cyanobacteria PSII hypothesis test would have been structurally impossible on the bakta substrate, since that table had zero PSII Pfam hits. [src: gene_function_ecological_agora]

At the biological level, 4 of 5 pilot controls reached 100% coverage across pilot species. [src: gene_function_ecological_agora] Only AMR (antimicrobial resistance) failed the 80% threshold, at 68.8%. The report calls this biologically expected for environmental and uncultivated lineages. [src: gene_function_ecological_agora]

## Per-genome annotation density

Density can change what an atlas score means. In the metal-ecology analysis, adding annotation depth (n_ko_ann_z) to the conditional PGLS (phylogenetic generalized least squares) model gave β = −0.0304, p = 7.9×10⁻¹¹ and +46.7% amplification, flagged as a suppressor. [src: comprehensive_metal_ecology] The report reads this as amplification, not attenuation: genera with richer annotations have fewer apparent metal-gene specialists. [src: comprehensive_metal_ecology] It calls annotation depth a suppressor variable rather than a confounder. [src: comprehensive_metal_ecology] The covariates n_ko_ann_z and ko_breadth_z are perfectly collinear, so either gives the same result. [src: comprehensive_metal_ecology]

The gene-function atlas tested this directly with D2 residualization (P4-D5). It had been specified as regressing per-genome annotated fraction out as a nuisance covariate, but was repeatedly deferred. [src: gene_function_ecological_agora] The report calls P4-D5 the closure of a long-standing pre-registration debt. [src: gene_function_ecological_agora] Until then, atlas-level D2 residualization was not implemented: per-genome `annotated_fraction` was stored but not regressed out per (rank × KO) score. [src: gene_function_ecological_agora] Producer R² = 0.000, and producer_z was uncorrelated with all 4 covariates. The report attributes this to the within-rank null already absorbing prevalence and clade-size effects. [src: gene_function_ecological_agora] Consumer R² = 0.053, small but non-zero. [src: gene_function_ecological_agora] In the consumer model, mean_annotated_fraction_z = −1.27, so higher-annotated clades have more negative consumer_z. The report calls this consistent with fewer missing KOs. [src: gene_function_ecological_agora] clade_size_z = +1.13 [src: gene_function_ecological_agora], mean_genome_size_z = −0.49 [src: gene_function_ecological_agora] and mean_gc_z = −0.05. [src: gene_function_ecological_agora]

Overall, producer_z is bias-immune and consumer_z carries small bias that changes no verdict. [src: gene_function_ecological_agora] All hypothesis verdicts survived. [src: gene_function_ecological_agora] The largest attenuation was NB12 family-rank consumer-side, d −0.19 → −0.16, ~16% relative, still significant. [src: gene_function_ecological_agora] The synthesis states that all atlas claims survived. [src: gene_function_ecological_agora] NB11 stayed H1 REFRAMED. NB12 stayed H1 SUPPORTED. NB16 stayed H1 SUPPORTED at class rank. [src: gene_function_ecological_agora]

| Test | Raw d | Residualized d | Residualized p |
|---|---|---|---|
| NB12 Mycobacteriaceae × mycolic family, producer_z | +0.31 | +0.31 | 2×10⁻⁶ [src: gene_function_ecological_agora] |
| NB12 Mycobacteriaceae × mycolic family, consumer_z | −0.19 | −0.16 | 1.6×10⁻⁵ [src: gene_function_ecological_agora] |
| NB12 Mycobacteriales × mycolic order, producer_z | +0.29 | +0.29 | 5×10⁻⁶ [src: gene_function_ecological_agora] |
| NB12 Mycobacteriales × mycolic order, consumer_z | −0.29 | −0.28 | <10⁻¹⁰ [src: gene_function_ecological_agora] |
| NB16 Cyanobacteriia × PSII (class), producer_z | +1.50 | +1.50 | 2.1×10⁻⁵ [src: gene_function_ecological_agora] |
| NB16 Cyanobacteriia × PSII (class), consumer_z | +0.70 | +0.63 | 2.3×10⁻⁵ [src: gene_function_ecological_agora] |

## Tensions

- The metal-ecology report finds that annotation depth amplifies the signal when controlled. [src: comprehensive_metal_ecology] The atlas finds producer scores unaffected and consumer scores slightly attenuated. [src: gene_function_ecological_agora] These are different models and outcomes, not a direct conflict.
- Dilution of the Alm signal is attributed partly to scaling from 207 mostly cultivated, highly annotated genomes to 18,989 species representatives. These include DPANN, CPR (candidate phyla radiation) and weakly annotated lineages with sparse HPK (histidine protein kinase) detection. [src: gene_function_ecological_agora] CPR and DPANN under-representation is also acknowledged as a substrate constraint [src: gene_function_ecological_agora], and the atlas says its effective-N reporting flags it per phase. [src: gene_function_ecological_agora] See [[concepts/statistical-power-and-database-coverage-gap-for-archaeal-trait-analyses]].
- The paralog fallback (n_gene_clusters when UniRef90 is absent) covers 21.5% of presence rows, so a with-and-without-fallback sensitivity analysis is motivated. [src: gene_function_ecological_agora]

## Open Directions

- Run the LLM-based pass over eggNOG Description and bakta product text for the Bacillota_B "other" bucket. This would test the 80–100 of 547 estimate against the scanner's 42.
- Repeat COG enrichment on the Bakta/eggNOG union, to see whether the 70% to 77.3% coverage gain changes essential-versus-dispensable enrichment.
- Apply D2-style residualization to the ecotype analysis. This would test whether the 62% unannotated clusters bias results toward housekeeping functions.
- Report the paralog-fallback sensitivity analysis, with and without the fallback.
- Re-run cog_analysis on more than 32 species to look for phylum-specific patterns.
- Audit zero-coverage marker Pfams in other domain tables, as was done for bakta_pfam_domains, before any new marker-based hypothesis test.
