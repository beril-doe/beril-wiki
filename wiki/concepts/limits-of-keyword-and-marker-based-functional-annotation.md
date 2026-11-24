---
type: "Concept"
description: "How keyword scanning, eggNOG OG tiers, and wrong or unavailable KO markers cause missed or spurious functional signals, and how multi-signal detection (PFAM plus motif counting) corrects them."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/prophage_amr_comobilization__REPORT.md"]
---
# Limits of keyword and marker-based functional annotation

Keyword scans, generic ortholog labels and mismatched KEGG ortholog (KO) markers each missed real signal or created false signal in the cited projects. [src: bacillota_b_subsurface_accessory, discoveries, pitfalls] Multi-heme cytochrome detection in Bacillota_B was corrected by combining protein-family (PFAM) hits with sequence-motif counting. [src: bacillota_b_subsurface_accessory] Most evidence is from single projects, so the examples are illustrations, not a measured error rate.

## Literature Context

The one candidate paper bearing on this page is the update of the Clusters of Orthologous Groups (COG) database. It describes an orthology-based approach to annotation, in which the function of characterized members of a protein family is transferred to the carefully identified orthologs of that family. The approach depends on complete microbial genomes and on careful manual curation of each COG, aimed at avoiding annotation errors and overprediction [PMID 25428365](https://pubmed.ncbi.nlm.nih.gov/25428365/). The update expanded genome coverage to representative complete genomes from all bacterial and archaeal lineages down to the genus level. The authors report that the original COG assignments had an error rate below 0.5% [PMID 25428365](https://pubmed.ncbi.nlm.nih.gov/25428365/). This is a statement about curated COG assignments. It is not a measure of keyword scanning or of KO-marker substitution. The paper also notes that functions of many previously uncharacterized COGs have since been elucidated, including several widespread conserved proteins involved in translation, rRNA maturation and tRNA modification [PMID 25428365](https://pubmed.ncbi.nlm.nih.gov/25428365/). The evidence is an abstract only, so the details of the curation are not available here.

The corpus is consistent with this literature in one respect. Curated, family-level annotation is the stronger signal, and its value depends on curation that avoids overprediction. The hub's cases of failure involve labels that lack this specificity. K02030 is a generic amino acid ABC transporter substrate-binding family. Filtering eggNOG by it returns 46,369 hits, almost none of them xoxJ, whereas the specific bakta product call matches 61 genomes. The ribosomal KO range K02860-K02899 + K02950-K02998 mixes universal and accessory variants. Both cases show what happens when a coarse or stale label is used as a proxy for a specific function, which is the overprediction that the COG curation aims to prevent [PMID 25428365](https://pubmed.ncbi.nlm.nih.gov/25428365/). The corpus's cautions about the 462-OG "other_or_unannotated" bucket also fit the paper's point that annotation of many families is still incomplete.

The corpus extends the literature but does not test it. The COG paper does not address keyword scanning of free-text descriptions, KO markers that are absent from KEGG (such as omcS and mtr multi-heme cytochromes), or the lack of a Bacillota_B tier in eggNOG. The corpus findings on these points are novel relative to this candidate, and they rest mostly on single projects. The hub itself says they illustrate failure modes and do not measure an error rate. The Bacillota_B project's corrected iron-reduction rates of 40–56% drew on PFAM hits and CXXCH motif counting. The reusable triple-signal detector that combines curated PFAMs (PF02085, PF22678) with CXXCH counting is a proposal in the report, not an established or validated method. The COG paper's error rate below 0.5% should not be read as support for the corpus's detection methods, and nothing in it is in tension with the corpus.

## Keyword scanning misses signals

A keyword scanner finds only what its pre-registered words anticipate. In the Bacillota_B subsurface analysis, the scanner missed a substantial fraction of anaerobic-niche signals because they are encoded by gene-family or domain names. [src: bacillota_b_subsurface_accessory] The 462-OG (ortholog group) "other_or_unannotated" bucket therefore undercounts real anaerobic-respiration and electron-transfer signal. [src: bacillota_b_subsurface_accessory] It contained COG1977 molybdopterin, DsrEFH and 2-oxoglutarate ferredoxin oxidoreductase. [src: bacillota_b_subsurface_accessory] The report proposes an LLM-based pass over eggNOG `Description` and bakta `product` text to count categories accurately. [src: bacillota_b_subsurface_accessory]

The same failure appears elsewhere. In aromatic_catabolism_network, keyword matching on RAST function descriptions misclassified enzymes with non-obvious names. [src: pitfalls] ACIAD1710, a core pca pathway enzyme, fell into "Other" because the list had "muconate" but not "muconolactone". [src: pitfalls] The recommended fix is to treat keywords as a first pass, validate with co-fitness correlations, and test classifiers against known category members. Co-fitness recovered pcaC (r=0.978 with the Aromatic pathway). [src: pitfalls]

Exact-name matching has the same weakness. The plant-growth-promoting (PGP) analysis matched bakta `gene` annotations to exact names such as nifH, acdS and pqqC. [src: pgp_pangenome_ecology] It misses genes annotated only by product description or with variant names, especially less-characterized PGP genes. [src: pgp_pangenome_ecology] Prophage identification by keyword/Pfam matching on bakta annotations may include false positives such as phage-defense systems and miss divergent prophages. [src: prophage_amr_comobilization]

Gene name alone can also be the weaker signal. For Psl detection, KOs K20997–K21005 in eggnog_mapper_annotations gave ~95% prevalence, against <1% by gene name alone. [src: pitfalls]

## Coarse or wrong ortholog labels

Generic or stale labels cause false positives. K02030 is the generic amino acid ABC (ATP-binding cassette) transporter substrate-binding protein family. [src: discoveries] Filtering eggNOG by it returns 46,369 hits across nearly every phylum, almost none of them xoxJ. [src: discoveries] The specific bakta product call for XoxJ matches just 61 genomes. [src: discoveries] The guidance is to use bakta product or eggNOG Preferred_name='xoxJ', and never K02030 as a proxy. [src: discoveries] The lanthanide atlas reached the same conclusion in its marker calibration. [src: lanthanide_methylotrophy_atlas] In its hit-bearing genome matrix, xoxJ has 41 genomes called by both sources, 46,369 by eggNOG only and 20 by bakta only, and the atlas trusts bakta only because K02030 is non-specific. [src: lanthanide_methylotrophy_atlas]

eggNOG tiers can be too coarse. Some enriched Bacillota_B OGs sit at root level. eggNOG has no Bacillota_B tier, because Bacillota_B is defined by GTDB while eggNOG uses NCBI taxonomy. [src: bacillota_b_subsurface_accessory]

Class definitions fail in a similar way. A description-matched neg_ribosomal class was dominated by clade-restricted accessory proteins and false matches, not universal ribosomal proteins. [src: gene_function_ecological_agora] Description-based detection that was mostly clean at UniRef50 did not survive KO aggregation, because the 50% majority-vote threshold admits accessory members. [src: gene_function_ecological_agora] The strict ribosomal KO range K02860-K02899 + K02950-K02998 is a pre-2000 KEGG-numbering approximation that mixes universal and accessory variants. [src: gene_function_ecological_agora] It is bimodal, with q25=0.11 and median=18.83 on Sankoff/n_present. [src: gene_function_ecological_agora]

## Wrong or unavailable KO markers

The clay_confined_subsurface project used K07811, K17324 and K17323 as iron-reduction (IR) markers. [src: bacillota_b_subsurface_accessory] They are TMAO reductase, glycerol ABC transport ATP-binding protein and glycerol ABC permease. [src: clay_confined_subsurface] Their thresholds were 1336.87, 363.93 and 318.27. [src: bacillota_b_subsurface_accessory] KEGG has no canonical KO for Geobacter omcS or the Shewanella mtr multi-heme outer-surface cytochromes, so unrelated genes were substituted. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] The report attributes the clay "Mitzscherling rock-attached signature in shallow clay" to mismatched gene IDs plus an eggNOG-mapper threshold that filters sequence similarity, not KO identity. [src: bacillota_b_subsurface_accessory] A sister project independently flagged the same issue for omcS, mtrCAB and MGE-borne resistance cassettes. [src: clay_confined_subsurface] See [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction]].

## Multi-signal correction

Multi-heme cytochrome PFAMs are sparse in Bacillota_B, with only ~6 clusters across the four PFAMs. [src: bacillota_b_subsurface_accessory] The per-PFAM counts were:

| PFAM | Name | Hits | Clusters |
|---|---|---|---|
| PF02085.21 | Cytochrom_CIII | 4 | 4 [src: bacillota_b_subsurface_accessory] |
| PF00034.26 | Cytochrom_C | 1 | 1 [src: bacillota_b_subsurface_accessory] |
| PF13442.11 | Cytochrome_CBB3 | 1 | 1 [src: bacillota_b_subsurface_accessory] |
| PF22678.1 | Cytochrom_c_NrfB-like | 1 | 1 [src: bacillota_b_subsurface_accessory] |
| PF14537 | Cytochrom_NNT | 0 | 0 [src: bacillota_b_subsurface_accessory] |

PF14537 was confirmed silently absent, a documented plant_microbiome_ecotypes pitfall. [src: bacillota_b_subsurface_accessory] CXXCH motif counting on gene_cluster.faa_sequence carried most of the IR signal, so the corrected IR rates (40–56%) are far higher than PFAM-only detection would give. [src: bacillota_b_subsurface_accessory] The report proposes triple-signal detection, combining curated PFAMs (PF02085, PF22678) with CXXCH counting, as a reusable KBase Data Lakehouse method when KO assignment is unreliable. [src: bacillota_b_subsurface_accessory] It says the method applies across the pangenome for iron-reduction or extracellular-electron-transfer questions. [src: bacillota_b_subsurface_accessory] See [[entities/multi-heme-cytochrome-detector]].

## Open Directions

- Run the proposed LLM pass over eggNOG Description and bakta product text for the 462-OG bucket. Compare category counts with the keyword scan to measure the undercount.
- Rerun the clay project's iron-reduction comparison with PFAM plus CXXCH detection. This would test whether the shallow-clay rock-attached signature survives.
- Audit other KO-based markers for generic-family KOs like K02030. Compare each against bakta product calls.
- Replace the ribosomal KO range with a curated universal r-protein list. Check whether the bimodality disappears.
- Compare gene-name-only PGP detection against product-description matching to quantify the missed genes.
