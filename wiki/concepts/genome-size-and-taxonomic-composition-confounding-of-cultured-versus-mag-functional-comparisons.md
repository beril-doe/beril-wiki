---
type: "Concept"
description: "How genome-size asymmetry, Patescibacteria dominance of MAGs, MAG incompleteness and geography confound apparent functional differences between cultured and metagenomic genomes; stops at proposed corrections."
sources: ["summaries/oak_ridge_cultivation_gap__REPORT.md"]
---
# Genome-size and taxonomic composition confounding of cultured-versus-MAG functional comparisons

This page covers how differences in genome size, taxonomic composition, MAG (metagenome assembled genome) incompleteness and geography confound apparent functional differences between cultured genomes and MAGs. The evidence is a single report, [[summaries/oak_ridge_cultivation_gap__REPORT]], which compared ENIGMA isolates with subsurface MAGs. It identifies the confounds mainly by reasoning from cohort statistics. It did not run a size-matched test. [src: oak_ridge_cultivation_gap]

## Cohort asymmetry

The two cohorts differ sharply in size, content and genome size, and the report treats genome size as the dominant driver of the bias distribution. [src: oak_ridge_cultivation_gap]

| Property | Cultured | MAG |
|---|---|---|
| Genomes | 3,110 (3,102 with KO annotations) [src: oak_ridge_cultivation_gap] | 2,279 [src: oak_ridge_cultivation_gap] |
| Unique KOs (KEGG orthologs) | 10,291 [src: oak_ridge_cultivation_gap] | 4,458 [src: oak_ridge_cultivation_gap] |
| Genome-KO pairs | 6,347,317 [src: oak_ridge_cultivation_gap] | 727,204 [src: oak_ridge_cultivation_gap] |
| Mean KOs per genome | 2,046 [src: oak_ridge_cultivation_gap] | 319 [src: oak_ridge_cultivation_gap] |
| Genome size | 5.8 Mbp mean [src: oak_ridge_cultivation_gap] | ~1.5 Mbp median [src: oak_ridge_cultivation_gap] |

The report cautions that the headline figure of 78% of KOs showing significant bias conflates genome-size asymmetry with true functional divergence. [src: oak_ridge_cultivation_gap] It attributes much of the functional asymmetry to genome-size disparity rather than specific functional selection. It says this disparity is driven substantially by the taxonomic composition of the MAG cohort. [src: oak_ridge_cultivation_gap]

## Taxonomic composition

The cultured and MAG cohorts sample different parts of the tree. Patescibacteria (also called CPR, candidate phyla radiation) make up approximately 40% of all 2,279 MAGs. [src: oak_ridge_cultivation_gap] Other major MAG phyla include Pseudomonadota (17%), Bacteroidota (8%) and Desulfobacterota. [src: oak_ridge_cultivation_gap] The cultured collection is dominated by Pseudomonadaceae (180 genomes), Variovorax (123), Cupriavidus (111) and other Burkholderiales. The report calls these readily cultivable Gammaproteobacteria and Betaproteobacteria. [src: oak_ridge_cultivation_gap] The report describes cultured ENIGMA isolates as predominantly Proteobacteria with large genomes (5-7 Mbp). It describes the MAG cohort as including 40% Patescibacteria with streamlined genomes (0.5-1.5 Mbp). [src: oak_ridge_cultivation_gap] The report attributes the median MAG genome size of 1.5 Mbp to this CPR dominance. [src: oak_ridge_cultivation_gap] See also [[entities/patescibacteria]] and [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]].

## What the asymmetry does to KO counts

The report reads the 7,669 cultured-enriched KOs as largely a genome-size effect. Larger genomes carry more genes of all kinds. [src: oak_ridge_cultivation_gap] The report says the cultured collection genuinely does not sample CPR organisms. It adds that most of the cultured-enriched KOs are not selected for by cultivation. They are simply present in larger genomes that happen to be cultivable. [src: oak_ridge_cultivation_gap]

The 813 KOs significantly depleted in cultured genomes are read differently. Subsurface MAGs carry them despite smaller genomes, so the report treats them as a stronger signal of true functional divergence. [src: oak_ridge_cultivation_gap] The report predicts that excluding Patescibacteria would leave MAGs with substantially more KOs per genome and narrow the apparent functional gap. This is a prediction, and the report did not test it. [src: oak_ridge_cultivation_gap]

## MAG incompleteness

Mean completeness in the QC-filtered MAG cohort is 78.7%. Some KOs scored as absent from MAGs may lie in the missing 20% of the genome. [src: oak_ridge_cultivation_gap] This makes the 813 MAG-enriched KOs a conservative estimate, with a true count likely higher. It also means some cultured-enriched KOs may be false positives. [src: oak_ridge_cultivation_gap]

## Geography and cohort scope

The cultured collection spans 20+ years of ENIGMA isolation efforts, primarily at ORFRC (Oak Ridge Field Research Center). The MAGs span subsurface sites globally. Composition differences may therefore reflect geography as much as cultivation bias. [src: oak_ridge_cultivation_gap] The MAGs were drawn globally from subsurface and groundwater MAGs in the pangenome resource rather than from ORFRC wells, because CORAL assembly FASTAs were inaccessible. [src: oak_ridge_cultivation_gap] The results therefore do not directly measure the cultivation gap at Oak Ridge. [src: oak_ridge_cultivation_gap] The findings concern subsurface systems generally. [src: oak_ridge_cultivation_gap] See also [[concepts/cultivation-bias-in-genome-collections-versus-uncultivated-lineages]] and [[concepts/genome-type-and-sampling-bias-in-metagenome-assembled-genome-surveys]].

## Proposed corrections

The report proposes repeating the comparison in phyla represented in both cohorts, with size-matched genomes, to separate cultivation selection from genome streamlining. [src: oak_ridge_cultivation_gap] It proposes annotating the 623 ORFRC-specific MAGs once CORAL assembly FASTAs become accessible through JupyterHub or MinIO/CTS. This would give a site-matched cultivation-coverage table. [src: oak_ridge_cultivation_gap]

## Open Directions

- Rerun the KO enrichment test within shared phyla (for example Pseudomonadota) with size-matched genomes. This would show how many of the 7,669 cultured-enriched KOs survive once genome size is controlled.
- Recompute the 813 MAG-enriched KOs after dropping Patescibacteria. This would test the prediction that the functional gap narrows.
- Re-score KO absence using only MAGs above a high completeness threshold, or with a completeness-weighted model. This would bound the false-positive and conservative-estimate effects of incompleteness.
- Annotate the 623 ORFRC MAGs and compare them with the ENIGMA isolates. This would separate geography from cultivation bias.
