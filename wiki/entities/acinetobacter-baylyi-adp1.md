---
type: "Organism"
description: "Acinetobacter baylyi strain ADP1, a naturally competent soil bacterium with TnSeq, fitness, proteomics and metabolic-model data in a dedicated database."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/respiratory_chain_wiring__REPORT.md"]
aliases: ["ADP1", "Acinetobacter baylyi", "Acinetobacter sp. ADP1"]
---
# Acinetobacter baylyi ADP1

Acinetobacter baylyi strain ADP1, a naturally competent soil bacterium with TnSeq, fitness, proteomics and metabolic-model data in a dedicated database.

## Key facts

- The ADP1 SQLite database has 15 tables with 461,522 total rows and 135 MB of data for ADP1 and 13 related genomes. [src: acinetobacter_adp1_explorer] See adp1 sqlite database berdl tables db.
- The central genome_features table has 5,852 genes and 51 annotation columns spanning six data modalities. [src: acinetobacter_adp1_explorer]
- All 13 KBase Data Lakehouse-format genomes belong to s__Acinetobacter_baylyi, clade s__Acinetobacter_baylyi--RS_GCF_000368685.1. [src: acinetobacter_adp1_explorer] Its pangenome has 3,207 core and 1,684 accessory gene clusters. [src: acinetobacter_adp1_explorer]
- ADP1 is absent from the [[entities/fitness-browser]]. The report therefore calls its mutant growth data a unique resource in the KBase Data Lakehouse. [src: acinetobacter_adp1_explorer]
- One report describes ADP1 as renowned for aromatic compound metabolism (Barbe et al. 2004). [src: adp1_triple_essentiality] It calls the beta-ketoadipate pathway a signature feature. [src: adp1_triple_essentiality] Aromatic degradation genes are described as central to this well-characterized catabolism. [src: adp1_triple_essentiality] See [[entities/ketoadipate-pathway]].
- The respiratory wiring report claims the first systematic demonstration that ADP1 uses qualitatively different respiratory configurations for different carbon sources, not only quantitative flux adjustments. [src: respiratory_chain_wiring]

## Proteomics and strains

Seven engineered strains are documented, all with proteomics. They are wild-type ADP1 and six aromatic amino acid pathway derivatives (ΔaroF, ΔaroG, dgoA variants). [src: acinetobacter_adp1_explorer] Protein abundance was measured for 2,383 genes across the 7 strains. [src: acinetobacter_adp1_explorer] Cross-strain correlation is high, which the report reads as targeted rather than global proteome effects. [src: acinetobacter_adp1_explorer]

## Essentiality datasets

The triple-essentiality report compares FBA (flux balance analysis), RB-TnSeq (random barcode transposon sequencing), knockout phenotypes, mutant growth rates and proteomics as predictors of essentiality. [src: adp1_triple_essentiality] The original analysis covered only TnSeq-dispensable genes (n=478). The refined study covered all genes (n=5,852), including TnSeq-essential genes, across RB-TnSeq thresholds 0.01, 0.025, 0.05, 0.10 and 0.20. [src: adp1_triple_essentiality] The rich-media (LB) knockout set tested 2,953 genes: 346 essential and 2,607 dispensable. [src: adp1_triple_essentiality] The minimal-media set tested 3,092 genes, 499 of them essential. [src: adp1_triple_essentiality]

## Deletion-collection growth on eight carbon sources

The 8 carbon sources fall into demanding, moderate and robust tiers, and the tiers hold across several thresholds. [src: adp1_deletion_phenotypes] Urea is the most demanding, with 97.9% of genes showing severe defects at ratio < 0.5. [src: adp1_deletion_phenotypes] Quinate is the most robust, with only 1.6% defective. [src: adp1_deletion_phenotypes] Growth ratios are mutant/wild-type. Values below 1.0 mean a defect. Values above 1.0 mean no defect or a slight advantage from normalization. [src: adp1_deletion_phenotypes] The complete matrix has 2,034 genes measured on all 8 sources. [src: adp1_deletion_phenotypes]

In total, 625 genes (31%) have a condition specificity score ≥ 1.0, so their importance is concentrated on one carbon source. [src: adp1_deletion_phenotypes] The digest lists these as mapping to expected metabolic pathways. [src: discoveries] See condition specific gene importance across carbon sources.

Clustering the 2,034 genes by growth profile gives an optimal K=3 with silhouette=0.24, so there are no discrete functional modules. [src: discoveries] The exception is 24 genes that form a tight quinate-specific aromatic-degradation module. [src: discoveries] Essentiality varies continuously across conditions, which the digest says supports the Guzman et al. (2018) adaptive-flexibility framework. [src: discoveries] See [[concepts/continuous-versus-discrete-structure-of-condition-dependent-gene-essentiality]].

## Aromatic catabolism network

The 51 quinate-specific genes form a metabolic dependency network around the β-ketoadipate pathway. [src: aromatic_catabolism_network] Quinate catabolism runs through protocatechuate and β-ketoadipate to succinyl-CoA and acetyl-CoA, which enter the TCA (tricarboxylic acid) cycle. [src: aromatic_catabolism_network] The pathway has 8 core genes, while 51 genes show quinate-specific growth defects. The digest states this as a 7:1 support-to-pathway ratio. [src: discoveries] The aromatic catabolism report instead describes the 51 genes as over 8× the core pathway, in 4 biochemically rational subsystems. The two reports give different ratios, and this page does not reconcile them. [src: aromatic_catabolism_network, discoveries] The subsystems sit at distinct sites: Complex I operon at 714–729 kb, pca/qui pathway at 1,709–1,724 kb, PQQ (pyrroloquinoline quinone) biosynthesis at 2,461 kb, and iron acquisition genes scattered across 4 loci. [src: aromatic_catabolism_network] PQQ dependency is not exclusively aromatic, because PQQ genes also look glucose-specific through PQQ-dependent glucose dehydrogenase. [src: aromatic_catabolism_network] See [[concepts/support-gene-networks-around-catabolic-pathways]] and [[entities/pyrroloquinoline-quinone-biosynthesis]].

## Respiratory chain wiring

ADP1 has 62 respiratory genes in 8 subsystems: Complex I (13), NDH-2 (1), NADH-flavin oxidoreductases (5), cytochrome bo3 (4), cytochrome bd (5), Complex II/SDH (5), ATP synthase (9) and other components (20). [src: respiratory_chain_wiring] Of these, 36 have growth data and 26 do not, including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring] Each of the 8 carbon sources needs a distinct set of components. [src: discoveries] The report calls this qualitatively different wiring per substrate class, not a quantitative gradient. [src: discoveries, respiratory_chain_wiring] See [[concepts/condition-dependent-respiratory-chain-configuration]].

- Quinate requires only Complex I. [src: discoveries]
- Acetate is the most demanding, requiring Complex I, cytochrome bo3, ACIAD3522 and more. [src: discoveries]
- Glucose requires no specific component, because of full redundancy. [src: discoveries]

Quinate yields fewer NADH per carbon (0.57) than glucose (1.50), yet Complex I is more essential on quinate. [src: discoveries] The proposed explanation is that β-ketoadipate products succinyl-CoA and acetyl-CoA enter the TCA cycle together. This makes an NADH burst beyond NDH-2 reoxidation capacity. [src: discoveries] See [[concepts/nadh-flux-rate-versus-nadh-yield-as-determinant-of-complex-i-dependence]].

ADP1's three NADH dehydrogenases (Complex I, NDH-2, ACIAD3522) have non-overlapping condition requirements. The report interprets this as metabolic division of labor in electron transport. [src: respiratory_chain_wiring]

Standard-condition proteomics shows similar expression of the three NADH dehydrogenases: Complex I mean 27.6 (66th percentile) [src: discoveries], NDH-2 27.0 (59th) [src: discoveries] and ACIAD3522 26.2 (48th). [src: discoveries] All lie within 1.4 units of each other around the genome median (26.4). [src: discoveries] The report concludes the cell does not switch configurations by regulating expression. All three run at once, and the limiting one depends on NADH flux from the carbon source. [src: discoveries]

Complex I has 13 subunits, is proton-pumping, and is quinate-essential but glucose-dispensable. [src: discoveries] See [[entities/respiratory-complex-i-nadh-ubiquinone-oxidoreductase]].

### ACIAD3522

ACIAD3522, an NADH-FMN oxidoreductase, has a growth ratio of 0.013 on acetate, essentially lethal. It shows no defect on quinate (1.39) or glucose (1.39). [src: discoveries] This is the largest condition-specific effect of any single gene in the 2,034-gene matrix. [src: discoveries] See [[entities/aciad3522]]. Genes ACIAD3137 (UPF0234/YitK) and ACIAD2176 (DUF2280) correlate at r > 0.98 with Complex I genes across 8 conditions. [src: discoveries] See [[entities/aciad3137-and-aciad2176]].

### Where FBA fails

FBA predicts zero flux through ACIAD3522 in all conditions. [src: discoveries] For Complex I it predicts 1.76× higher flux on aromatics but 0% essentiality. [src: discoveries] Of the 51 quinate-specific genes, 30 (59%) have no FBA reaction mappings. They include PQQ biosynthesis, iron acquisition, regulators and respiratory components. [src: discoveries] See [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]].

## Caveats

- No gene has data across all six modalities. Pairwise overlaps are substantial, particularly between essentiality, pangenome and proteomics. [src: acinetobacter_adp1_explorer]
- The database covers only A. baylyi, so cross-species comparison needs similar databases for other organisms. [src: acinetobacter_adp1_explorer]
- Of 2,593 TnSeq-dispensable genes, 272 (10.5%) lack deletion-collection growth data. The other 2,321 have data. [src: adp1_deletion_phenotypes, discoveries] See [[concepts/coverage-gaps-in-deletion-collections-and-their-link-to-pangenome-conservation]].
- The complete 2,034-gene matrix excludes essential genes (499) and genes with incomplete data (316). This biases it toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]
- The deletion collection is biased toward well-characterized, conserved genes. [src: discoveries] See [[entities/de-berardinis-et-al-2008-adp1-deletion-mutant-collection]].
- Of the 62 respiratory genes, 26 lack growth data, including NDH-2 and several ATP synthase subunits, so the wiring map is incomplete for those components. [src: respiratory_chain_wiring]

## Source summaries

[[summaries/acinetobacter_adp1_explorer__REPORT]], [[summaries/adp1_deletion_phenotypes__REPORT]], [[summaries/adp1_triple_essentiality__REPORT]], [[summaries/aromatic_catabolism_network__REPORT]], [[summaries/respiratory_chain_wiring__REPORT]], [[summaries/discoveries]].
