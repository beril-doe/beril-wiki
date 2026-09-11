---
type: "Summary"
description: "Pangenome atlas of lanthanide-dependent methanol oxidation and its environmental distribution"
doc_type: "short"
full_text: "sources/lanthanide_methylotrophy_atlas__REPORT.md"
---
# Lanthanide Methylotrophy Atlas — Summary

## Overview

This report presents a 293,059-genome atlas of lanthanide-dependent methanol oxidation across the KBase Data Lakehouse pangenome, testing the distribution of xoxF (REE-dependent methanol dehydrogenase), mxaF (Ca-dependent methanol dehydrogenase), lanmodulin, PQQ-biosynthesis markers, and environmental associations using GTDB-r214 taxonomy, eggNOG, Bakta, and environmental metadata. The study finds strong global dominance of xoxF over mxaF, high xoxF rates in Acidobacteriota and Gemmatimonadota, strict clade restriction of Bakta-validated lanmodulin, strongest enrichment in soil/sediment, and substantial marker-source disagreement attributable partly to annotation gaps. [src: lanthanide_methylotrophy_atlas]

## Key Findings

### xoxF strongly outnumbers mxaF

eggNOG K00114 (xoxF; EC 1.1.2.8) occurs in 3,690 genomes, whereas K14028 (mxaF; EC 1.1.2.7) occurs in 195 genomes, giving a global xoxF:mxaF ratio of 18.92 : 1 with a Clopper-Pearson 95% CI of [13.07, 27.69]. xoxF represents 0.9498 of joint xoxF + mxaF calls, with a 95% CI of [0.9425, 0.9558]. A one-sided binomial test against the pre-registered xoxF fraction threshold of 10/11 ≈ 0.909 gives p = 7.6 × 10⁻²², strongly supporting H1. [src: lanthanide_methylotrophy_atlas]

After Benjamini-Hochberg FDR correction across 29 testable phyla, the directional H1 verdict survives in every phylum with any MDH calls and adequate sample size, including Pseudomonadota, Acidobacteriota, Actinomycetota, Bacteroidota, Campylobacterota, Verrucomicrobiota, Chloroflexota, Gemmatimonadota, Methylomirabilota, Halobacteriota, and Thermoproteota. [src: lanthanide_methylotrophy_atlas]

Three phylogenetic validations also support H1: naive genome-level pooling gives 3,885 MDH-informative genomes and an xoxF fraction of 0.950 [95% CI 0.942, 0.956]; equal weighting across 271 MDH-informative GTDB families gives 0.960 [95% CI 0.941, 0.976]; and a Bayesian binomial GLMM with random intercepts for phylum and family gives 0.993 [95% CI 0.992, 0.994]. The GLMM corresponds to a phylogeny-corrected ratio of ~143 : 1 with a 95% credible interval of [122, 169]. [src: lanthanide_methylotrophy_atlas]

### High-rate carriers extend beyond canonical methylotrophs

Acidobacteriota contains 285 xoxF genomes and 3 mxaF genomes among 1,006 genomes, a 28.3 % xoxF rate and a 95 : 1 xoxF:mxaF ratio, with p_BH = 1.2 × 10⁻⁷⁹. Gemmatimonadota contains 98 xoxF and 1 mxaF among 386 genomes, a 25.4 % xoxF rate and a 98 : 1 ratio, with p_BH = 1.5 × 10⁻²⁷. Methylomirabilota contains 23 xoxF and 7 mxaF among 80 genomes, a 28.7 % xoxF rate and a 3.3 : 1 ratio, with p_BH = 0.011. [src: lanthanide_methylotrophy_atlas]

Pseudomonadota contains 2,988 xoxF and 171 mxaF genomes among 117,619 genomes, a 2.5 % xoxF rate and a 17.5 : 1 ratio. Verrucomicrobiota contains 19 xoxF and 5 mxaF genomes among 2,440 genomes, a 0.78 % xoxF rate and a 3.8 : 1 ratio, with p_BH = 0.015. Within Pseudomonadota, Pseudomonadaceae contributes 566 xoxF genomes versus 1 mxaF genome; Beijerinckiaceae has 171 xoxF genomes among 508 genomes, a 33.7 % rate; and Hyphomicrobiaceae has 33 xoxF genomes among 56 genomes, a 58.9 % rate. [src: lanthanide_methylotrophy_atlas]

Bacteroidota, Cyanobacteriota, Chloroflexota, Planctomycetota, Campylobacterota, Actinomycetota, Halobacteriota, and Thermoproteota have xoxF calls but zero mxaF annotations. These patterns suggest that lanthanide-dependent methanol oxidation is distributed beyond the classical methylotroph lineages, but the report notes that annotation-based detection does not establish enzyme activity or methylotrophic physiology. [src: lanthanide_methylotrophy_atlas]

### Lanmodulin is clade-restricted and only partly co-occurs with xoxF

Bakta-validated product = Lanmodulin occurs in 62 genomes spanning 10 species. All 62/62 = 100 % occur within Beijerinckiaceae, Acetobacteraceae, or Hyphomicrobiaceae, supporting H3a with a one-sided binomial p = 9.8 × 10⁻⁷ against the 80 % threshold. [src: lanthanide_methylotrophy_atlas]

xoxF co-occurs with lanmodulin in 49/62 = 79.0 % of these genomes, just below the pre-registered 80 % threshold; the one-sided binomial p = 0.65, so H3b is not formally supported. The 13/62 lanmodulin genomes without xoxF may reflect annotation incompleteness or alternative lanthanide-handling pathways, while xoxF genomes without lanmodulin may handle REEs through other mechanisms. [src: lanthanide_methylotrophy_atlas]

The dominant lanmodulin carrier is Methylobacterium extorquens, with 22 genomes and 1 lanmodulin copy each. Other contributors are an uncharacterised Acetobacteraceae genus, g__BOG-930, with 12 genomes; M. thiocyanatum with 6; M. rhodesianum with 6; M. aminovorans with 4; Hyphomicrobium_B with 2; and Methylocella with 2. [src: lanthanide_methylotrophy_atlas]

### Soil/sediment is the strongest environmental enrichment

Among environmental classes, soil_sediment contains 13,779 genomes, has a 6.84 % xoxF rate, and is enriched relative to generic_environmental with OR = 1.92 and p_BH = 6.1 × 10⁻³⁹. Marine environments contain 15,554 genomes, have a 4.76 % xoxF rate, OR = 1.31, and p_BH = 7.8 × 10⁻⁷. The generic_environmental reference contains 21,538 genomes with a 3.69 % rate. [src: lanthanide_methylotrophy_atlas]

Volcanic_geothermal contains 3,450 genomes with a 3.19 % rate, OR = 0.86, and p_BH = 0.20. Mining contains 1,636 genomes with a 4.10 % rate, OR = 1.12, and p_BH = 0.38. REE-impacted samples contain 37 genomes with a 10.81 % rate, OR = 3.51, and p_BH = 0.082. Methylotrophic samples contain 5 genomes with a 20.0 % rate, OR = 8.70, and p_BH = 0.20. Host-associated samples contain 107,600 genomes with a 0.22 % rate, OR = 0.058, and p_BH = 0.0. [src: lanthanide_methylotrophy_atlas]

H2 is therefore partially supported: soil/sediment and marine environments show inferential enrichment, whereas the REE-impacted signal is descriptively elevated but does not clear the FDR threshold. Within Acidobacteriota, soil/sediment enrichment remains significant with OR = 2.16 and p_BH = 2.2 × 10⁻⁵, indicating that the broad soil signal is not entirely explained by phylogenetic composition. [src: lanthanide_methylotrophy_atlas]

### REE-acid-mine-drainage MAGs are dominated by stress biology

The 37 metagenome-assembled genomes from samples tagged “rare earth elements-acid mine drainage (REEs-AMD) contaminated river water” are taxonomically diverse and are led by acidophilic and metal-tolerant lineages including Acidocella, Acidiphilium, Thiomonas, Metallibacterium, Burkholderiaceae_A/_B genera, Chitinophagaceae, Acidimicrobiia, Chloroflexota, Cyanobacteriota, and the previously uncharacterised f__REEB76 / g__REEB76 clade. [src: lanthanide_methylotrophy_atlas]

Only 4/37 REE-AMD MAGs carry any xoxF, and 0/37 carry Bakta-validated lanmodulin or xoxJ. Stress-associated products are more prevalent: RecN occurs in 33 MAGs, RadA in 32, RecO in 31, RecA in 28, RadC in 24, FtsH zinc metalloprotease in 31, proton-translocating NAD(P)+ transhydrogenase in 27, MerR-family heavy-metal-responsive regulators in 30, thioredoxin reductase in 25, and glutathione peroxidase in 24. [src: lanthanide_methylotrophy_atlas]

### PQQ asymmetry is largely an annotation gap

Among 2,320 xoxF-bearing genomes initially lacking any eggNOG PQQ-biosynthesis annotation, 33 have complete eggNOG pqqA-E calls, 1,472 have partial eggNOG pqq calls covering 1–4 of A-E, 899 have Bakta-only strong evidence with at least 3 PQQ products, 389 have Bakta-only partial evidence with 1–2 PQQ products, and 897 have no PQQ detected by either source. [src: lanthanide_methylotrophy_atlas]

Of 2,185 genomes with no eggNOG pqq annotation, 1,288 (59 %) have at least 1 Bakta PQQ product, indicating annotation gaps. The remaining 897 genomes, equal to 24 % of all xoxF carriers, lack PQQ evidence from either source and are candidates for assembly incompleteness, pseudogenization, or genuine reliance on community-acquired PQQ. [src: lanthanide_methylotrophy_atlas]

### Marker-source calibration changes interpretation

In a 134,578-row hit-bearing matrix, lanmodulin has 0 calls in both sources, 505 eggNOG-only calls, and 62 Bakta-only calls; Bakta is therefore the trustworthy source for lanmodulin. xoxJ has 41 calls in both sources, 46,369 eggNOG-only calls, and 20 Bakta-only calls; Bakta is preferred because eggNOG KO K02030 is non-specific. xoxF has 418 calls in both sources, 3,272 eggNOG-only calls, and 1,402 Bakta-only calls; eggNOG K00114 is primary and Bakta is used as a union source. mxaF has 4 calls in both sources, 191 eggNOG-only calls, and 8 Bakta-only calls; eggNOG K14028 is primary. [src: lanthanide_methylotrophy_atlas]

The 505 eggNOG Preferred_name = lanM false positives are concentrated in unrelated gut Bacillota, including Streptococcus pneumoniae (10), Blautia_A wexlerae (9), Enterococcus faecalis (8), Ruminococcus_B gnavus (8), and Streptococcus pyogenes (7). Bakta product = Lanmodulin identifies 62 genomes, all in canonical α-Proteobacterial methylotroph clades, so future KBase Data Lakehouse lanmodulin analyses should use Bakta product exclusively. [src: lanthanide_methylotrophy_atlas]

## Caveats and Future Work

The report addresses phylogenetic non-independence for H1 using pooled, family-equal-weight, and Bayesian GLMM analyses, all of which support H1; however, H2 still relies on within-phylum stratified analyses rather than a fully phylogeny-aware mixed model. [src: lanthanide_methylotrophy_atlas]

Marker calls vary substantially between eggNOG and Bakta, so headline statistics use a marker-specific source of truth and secondary union-of-sources analyses. Sequence-level evidence is out of scope: the study does not screen for pseudogenes, truncated ORFs, or assembly fragmentation. Genuinely novel REE-handling enzymes lacking KEGG or RefSeq homologs would also be missed. [src: lanthanide_methylotrophy_atlas]

The REE-AMD anchor contains only 37 MAGs from a single bioproject and is descriptive only; larger, independent collections from REE-mining tailings, leachate, and bioreactors are needed for inferential testing. The 897 xoxF genomes with no PQQ evidence require ORF-integrity and genome-completeness analysis, such as CheckM2, to distinguish fragmentation, pseudogenization, and community-PQQ acquisition. [src: lanthanide_methylotrophy_atlas]

AlphaEarth coverage is 1,457 / 3,690 = 39.5 % of xoxF genomes, compared with a 28 % pangenome baseline, leaving 60.5 % without environmental coordinates. Coverage-restricted PCA/UMAP analysis could test whether xoxF carriers form distinct environmental or biogeographic clusters, stratified by phylum. [src: lanthanide_methylotrophy_atlas]

The ncbi_env environmental classification is text-mining-derived and uses hierarchical regex priorities, so broad classes such as host_associated may contain misclassifications. The study also proposes characterizing f__REEB76, examining lanmodulin sequence diversity in 22 Methylobacterium extorquens genomes with 1 copy each, testing lanthanum and cerium chloride with targeted RB-TnSeq, and reporting the 505 eggNOG lanM false-positive pattern upstream. [src: lanthanide_methylotrophy_atlas]

## Slots Into

- [[concepts/pangenome-integration]] — The 293,059-genome atlas, GTDB-r214 stratification, and 18.92 : 1 xoxF:mxaF distribution provide cross-genome evidence for integrating functional markers with taxonomy. [src: lanthanide_methylotrophy_atlas]
- [[concepts/environment-embedding-geography]] — Soil/sediment enrichment, marine enrichment, host-associated depletion, limited AlphaEarth coverage, and proposed embedding analysis connect marker distribution to environmental geography. [src: lanthanide_methylotrophy_atlas]
- [[concepts/gene-function-acquisition-depth]] — Broad xoxF distribution, lanmodulin clade restriction, PQQ annotation gaps, and eggNOG-versus-Bakta calibration refine how marker annotations should be interpreted as evidence of function. [src: lanthanide_methylotrophy_atlas]
