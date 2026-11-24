---
type: "Concept"
description: "How reliable curated KEGG-ortholog lists and curated HMMs are for annotating metal processing and resistance genes, including cross-reactivity, weak 'other' categories, category overlaps, substrate-binding transporter gaps and absence of manual validation."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Validity of curated metal-gene annotation

This page covers how reliable curated KEGG-ortholog lists and curated HMMs are for annotating metal genes. The comprehensive_metal_ecology report's structural audit supports its gene-list design, by its own interpretation. The microbeatlas_metal_ecology report checked its AMR (antimicrobial resistance) annotation only informally, with spot checks and no manual validation of a subset. [src: comprehensive_metal_ecology, microbeatlas_metal_ecology]

## Literature Context

The two candidate papers are single-strain genome reports. They are modest, indirect context for this page, and neither tests the validity of metal-gene annotation.

The first paper mined the genome of one soil Bacillus cereus isolate, VLR6. It used Bakta annotation with keyword screening, CARD-RGI for antibiotic resistance, and antiSMASH for biosynthetic gene clusters [PMID 42968907](https://pubmed.ncbi.nlm.nih.gov/42968907/). Annotation-based mining reported a heavy-metal-resistance gene set. The set included a zntA-annotated Pb(II)/Cd(II)/Zn(II)-class P-type ATPase homologue, a complete ars operon (arsRBC) and two czcR-family regulators [PMID 42968907](https://pubmed.ncbi.nlm.nih.gov/42968907/). The calls came from annotation text and keyword screening. The abstract does not say how reliable those calls are. Its stated caveat is that phenotypic lead-MIC determination and metabolomic or transcriptomic validation are still required before any bioactivity can be attributed to the strain or its predicted metabolites [PMID 42968907](https://pubmed.ncbi.nlm.nih.gov/42968907/). That caveat is about bioactivity, not about the metal-gene calls.

The second paper describes Burkholderia gladioli YNK-FB0053, a rapeseed rhizosphere strain. Its multi-database annotation identified genes linked to zinc homeostasis, iron acquisition and siderophore-related processes, and heavy metal resistance, among other traits [PMID 42495130](https://pubmed.ncbi.nlm.nih.gov/42495130/). The abstract does not name the metal-resistance genes or the annotation method behind them. It says that genome-based predictions for nitrogen metabolism, iron acquisition and siderophore-related traits, phytohormone biosynthesis, antibiotic resistance and biosafety need targeted biochemical validation. Heavy-metal resistance is not on that list [PMID 42495130](https://pubmed.ncbi.nlm.nih.gov/42495130/). Its confirmed phenotypes were biofilm formation, root colonization and plant growth promotion, not metal resistance [PMID 42495130](https://pubmed.ncbi.nlm.nih.gov/42495130/).

These papers fit the corpus only loosely. They show that single-genome studies report metal-resistance gene sets from annotation-based screening. They are consistent with the corpus's concern that annotation-derived calls rest on unvalidated sources. The microbeatlas_metal_ecology report did only spot checks and no manual validation of a subset, and the hub page records that. Neither paper checks metal-gene calls by BLAST against reference sequences or reports a false-positive rate. They therefore neither support nor contradict the hub's specific claims. Those claims are the 10/140 KOs (7.1%) with metal-binding clan support, the substrate-binding transporter gap for ZnuA and MntH, the 83/382 cofactor overlap, the 17% "other" category and the cross-reactivity risk. The corpus's proposed 100-cluster BLAST audit and rerun without the "other" category address questions that these abstracts leave open, so that work remains novel relative to these candidates.

## Structural-domain audit of the KEGG ortholog (KO) list

A Pfam/InterPro audit of all 140 primary KOs (via KEGG representational state transfer (REST) → UniProt → InterPro application programming interface (API)) found metal-binding clan membership or metal-binding singleton Pfams in 10/140 KOs (7.1%). [src: comprehensive_metal_ecology] The clans checked were HMA CL0704, 4Fe-4S CL0344, Fer2/2Fe-2S CL0486, C2H2-zf CL0361 and MBB CL0193. [src: comprehensive_metal_ecology] The other 130 KOs had Pfam annotations but no metal-coordination clan. [src: comprehensive_metal_ecology]

Of those 130, 113 carry ATP-binding cassette (ABC) transporter scaffolds (PF00005/PF00950/PF01032), MerR/CusR/ZntR sensor Pfams and outer-membrane efflux proteins. The report calls these mechanistically correct metal-processing proteins whose Pfam domains are substrate-binding or transport scaffolds rather than metal-coordination sites. [src: comprehensive_metal_ecology]

### Substrate-binding transporter gap

ZnuA (K02035) is a Zn²⁺ ABC importer substrate-binding component. It has PF13377/PF12838 Zn-binding clusters but is not in a curated metal-binding InterPro clan. [src: comprehensive_metal_ecology] MntH (K03322) is a Mn²⁺/Fe²⁺ NRAMP secondary transporter with a PF07690 MFS scaffold and no metal-coordination residue motif in its Pfam family record. [src: comprehensive_metal_ecology] The report treats the missing clan evidence for these well-characterised importers as an annotation gap for substrate-binding metal transporters, not a gene-list problem. [src: comprehensive_metal_ecology] It concludes that this expected pattern validates the gene-list architecture. [src: comprehensive_metal_ecology] That is the report's own interpretation. The audit itself shows only that 7.1% of KOs have clan support. [src: comprehensive_metal_ecology]

## Overlap with cofactor and vitamin categories

The cofactor audit cross-referenced all 382 KEGG cofactors-and-vitamins KOs against the 730-KO curated metal list (all 5 evidence tiers), BacMet2 and Pfam clan coverage. [src: comprehensive_metal_ecology] The 730-KO list is evidence-tiered and covers 5 tiers and 24 metals. [src: comprehensive_metal_ecology] The audit found 83 shared KOs. [src: comprehensive_metal_ecology] Of these, 12 are in the primary 140 and were already excluded from the 370-KO non-metal cofactor comparison set. [src: comprehensive_metal_ecology]

The other 71 were flagged from Tiers 3–5 or BacMet2. They fall in heme, cobalamin/cobamide, molybdopterin and biotin biosynthesis, which are metal-dependent cofactor pathways by KEGG design. [src: comprehensive_metal_ecology] The genes named are hemA/B/C/D/E/G/H/J/L/N and hemQ, cobA–Q and cbiA–T, moaA/C, and bioA/B/D/F/I/U/W. [src: comprehensive_metal_ecology] The report classes these 71 as mechanistically non-metal cofactors that produce cofactors for other enzymes. It says their presence in the comparison set does not alter interpretation. [src: comprehensive_metal_ecology]

The effect estimate β is −0.029 for the full 382-KO set and for the 12-KO-reduced 370-KO set. The report reads this as minimal quantitative impact. [src: comprehensive_metal_ecology] It concludes that the comparison is valid and that the 83/382 overlap does not threaten the specificity interpretation. [src: comprehensive_metal_ecology]

## Category scope

The global panel includes all metals with ≥34 KOs: Cu, Zn, Fe, Ni, Co, Mn, Tl, Al and S. [src: comprehensive_metal_ecology] The Australian replication tests only the 5 metals available in NGSA geochemistry: Cu, Zn, Pb, Ni and Co. [src: comprehensive_metal_ecology] Sulfur KOs mostly encode Fe–S cluster biogenesis proteins (iscS, iscU, sufB, nifU), which are metal-cofactor systems. [src: comprehensive_metal_ecology] The report justifies aluminum by documented bacterial toxicity and dedicated resistance systems. [src: comprehensive_metal_ecology] See [[entities/iron-sulfur-cluster-biogenesis]] and [[entities/aluminum]].

## HMM-based AMR annotation

The microbeatlas report annotates metal AMR genes with [[entities/amrfinderplus]] HMM detection against the NCBI Bacterial AMR Reference Gene Database. [src: microbeatlas_metal_ecology] For metals it uses curated HMMs built from experimentally validated sequences, such as merA/merB for mercury, arsABCDR for arsenate and copABCD for copper. [src: microbeatlas_metal_ecology] Gathering thresholds are set during calibration to balance sensitivity and specificity. No identity threshold is added, because HMM scores are not identity values. [src: microbeatlas_metal_ecology] See also [[concepts/metal-resistance-genes-within-amr-catalogs]].

### Limits of this annotation

- Cross-reactive metalloproteases or ABC transporters that resemble metal resistance proteins could be misclassified. AMRFinderPlus taxon-specific cutoffs reduce this risk. [src: microbeatlas_metal_ecology]
- The "other" category is 17% of annotated clusters and captures metal-associated genes outside the 7 primary types. [src: microbeatlas_metal_ecology] The report warns it may include weaker hits. [src: microbeatlas_metal_ecology] Excluding it would leave a 6-metal analysis (Hg, As, Cu, Zn, Cd, Cr, Ni only). [src: microbeatlas_metal_ecology]
- No manual validation of a subset was performed in that study. [src: microbeatlas_metal_ecology] Formal AMRFinderPlus validation was not done, only spot checks. [src: microbeatlas_metal_ecology]
- The report recommends randomly sampling 100 annotated gene clusters for manual BLAST verification against the original protein sequences, to quantify the false positive rate. [src: microbeatlas_metal_ecology] Separately, it proposes randomly sampling 100 AMRFinderPlus-annotated metal AMR gene clusters for manual BLAST verification against reference sequences, to quantify the HMM-based false positive rate for each metal type category. [src: microbeatlas_metal_ecology]

Spot checks of prevalent arsD and merP families gave biologically expected distributions, high in contaminated-environment genera and lower in strict aerobes. The report calls this informal support. [src: microbeatlas_metal_ecology] See [[entities/arsenic-resistance-ars-genes]] and [[entities/mercury-resistance-mer-genes]]. The leave-one-metal-out analysis (S1) is read as showing that multiple metal types contribute. A single category's spurious annotations would therefore not explain the result. [src: microbeatlas_metal_ecology] See [[concepts/single-metal-dominance-versus-distributed-metal-type-diversity-effects]].

## Open Directions

- Draw 100 random annotated gene clusters and check them by BLAST against reference sequences. Report the false-positive rate for each metal type. This closes the gap left by the absence of manual validation.
- Rerun the main analysis without the "other" category. This would show how much the weaker hits drive the result.
- Add substrate-binding-aware evidence for ZnuA- and MntH-type importers, such as curated transporter families. This would close the clan gap, since only 10/140 primary KOs have clan support.
