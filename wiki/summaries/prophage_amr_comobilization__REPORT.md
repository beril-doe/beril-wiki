---
type: "Summary"
description: "Summary of the project Prophage-AMR Co-mobilization Atlas."
doc_type: "short"
full_text: "sources/prophage_amr_comobilization__REPORT.md"
---
# Prophage-AMR Co-mobilization Atlas

This page summarizes the Prophage-AMR Co-mobilization Atlas. It asked whether antimicrobial resistance (AMR) genes sit near prophage markers and whether prophage load predicts AMR breadth across bacterial species. Co-localization is common, but proximity only weakly predicts accessory status. The species-level link between prophage density and AMR breadth is strong. The evidence is correlational and rests on keyword-based prophage calls. The fitness-cost hypothesis (H3) could not be tested. [src: prophage_amr_comobilization]

## Key Findings

### Census and co-localization

- The full pangenome inventory has 83,008 AMR gene clusters and 3.47 million prophage marker clusters. [src: prophage_amr_comobilization]
- The census counts 1,261,929 strict and 3,465,244 broad prophage marker clusters. [src: prophage_amr_comobilization]
- Prophage markers are 83.8% accessory and 53.8% singleton. AMR genes are 69.7% accessory and 36.1% singleton. [src: prophage_amr_comobilization]
- Of 27,702 species, 14,669 (52.9%) carry both AMR and prophage markers. [src: prophage_amr_comobilization]
- The gene-neighborhood dataset covers 36,041 AMR gene instances in 100 species, with 20 genomes sampled per species and 1,953 genomes in total. [src: prophage_amr_comobilization]
- In that dataset, 20,073 instances (55.7%) are on a prophage contig. [src: prophage_amr_comobilization]
- Fewer instances lie close to a marker: 12,026 (33.4%) within 50 genes, 7,137 (19.8%) within 20, 3,731 (10.4%) within 10 and 1,991 (5.5%) within 5. [src: prophage_amr_comobilization]
- Among co-localized AMR genes, the median distance to the nearest marker is 34 genes, and 10.4% of all AMR genes are within 10 genes of a marker. [src: prophage_amr_comobilization]
- The report calls this the first pangenome-scale analysis of prophage–AMR gene-neighborhood co-localization. [src: prophage_amr_comobilization]

### H1: proximity and conservation

- Proximal instances (≤10 genes) number 2,523 accessory and 1,208 core, which is 67.6% accessory. [src: prophage_amr_comobilization]
- Distal instances (>10 genes) number 21,158 accessory and 11,152 core, which is 65.5% accessory. [src: prophage_amr_comobilization]
- The one-sided Fisher's exact test gives OR (odds ratio)=1.10, p=0.005. The bootstrap 95% CI (confidence interval) is [1.024, 1.185]. [src: prophage_amr_comobilization]
- The effect is absent or reversed at close range, with OR=0.78 at 3 genes and OR=0.92 at 5 genes. It strengthens at broader thresholds, with OR=1.19 at 15 genes and OR=1.28 at 50 genes. [src: prophage_amr_comobilization]
- Only 33 of 74 testable species show OR>1. The median species-level OR is 0.85. [src: prophage_amr_comobilization]
- The report describes the 2.1 percentage point accessory-fraction difference as modest and heterogeneous across species. [src: prophage_amr_comobilization]
- Core/accessory labels depend on species-level pangenome calling with motupan, so the same gene can have different conservation status in different species. [src: prophage_amr_comobilization]

The report offers two hypotheses to explain the threshold dependence. Genes immediately next to phage structural genes may be core phage components rather than recently acquired cargo. [src: prophage_amr_comobilization] The stronger effect at 15–50 genes could reflect genomic islands that hold both phage remnants and laterally transferred genes. [src: prophage_amr_comobilization] The report says the close-range reversal was not captured in prior contig-level studies. [src: prophage_amr_comobilization]

### H2: species-level prophage density and AMR breadth

Species with denser prophage markers carry broader AMR repertoires. The association holds after controlling for genome count and in all five major phyla. [src: prophage_amr_comobilization]

- Across n=4,770 species, Spearman rho=0.572, p<10^-300. [src: prophage_amr_comobilization]
- The prophage/genome and AMR/genome measures correlate with rho=0.608, p<10^-300. [src: prophage_amr_comobilization]
- The log-log slope is 0.823 (SE (standard error)=0.018), with R²=0.30. A 10-fold increase in prophage density predicts a ~6.6-fold increase in AMR breadth. [src: prophage_amr_comobilization]
- The partial Spearman correlation controlling for genome count is rho=0.464, p=1.0×10^-253. [src: prophage_amr_comobilization]
- Within phyla, rho is 0.54 in Pseudomonadota, 0.55 in Bacillota_A, 0.40 in Bacillota, 0.59 in Bacteroidota and 0.29 in Actinomycetota. [src: prophage_amr_comobilization]
- The report says this consistency argues against phylogenetic confounding. [src: prophage_amr_comobilization]
- It says prophage density explains 30% of variance in AMR breadth, a stronger predictor than previously documented. [src: prophage_amr_comobilization]
- The report cautions that the association does not prove phage-mediated AMR transfer, because species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization]

The report proposes two non-exclusive mechanisms. Prophages may directly mobilize resistance genes by specialized or generalized transduction. [src: prophage_amr_comobilization] Alternatively, species with many prophages may have high recombination potential and acquire genes from other mobile elements more readily. [src: prophage_amr_comobilization]

### H3: fitness cost

H3, the fitness cost comparison, could not be tested. [src: prophage_amr_comobilization] The Fitness Browser covers only 48 model organisms with RB-TnSeq (random barcode transposon sequencing) data. These overlap poorly with the GTDB pangenome species analyzed. [src: prophage_amr_comobilization] The attempt used the kescience_fitnessbrowser tables genefitness, gene and organism. [src: prophage_amr_comobilization] The result file records H3 as not tested. [src: prophage_amr_comobilization]

### Literature context

The report draws its literature context from PubMed articles. [src: prophage_amr_comobilization]

- Its H2 result aligns with Rendueles et al. (2018), who showed that capsule-encoding bacteria have more prophages and more antibiotic resistance genes across >100 pangenomes. [src: prophage_amr_comobilization]
- The report extends that work to 4,770 species versus ~100. It controls for genome count rather than capsule presence. [src: prophage_amr_comobilization]
- Chen et al. (2018) found ARG–mobile genetic element co-occurrence, including prophage associations, on assembled river-metagenome contigs. The report says its analysis confirms that the association is encoded in reference genomes. [src: prophage_amr_comobilization]
- Bearson & Brunelle (2015) showed that fluoroquinolone exposure induces prophage in multidrug-resistant Salmonella, enabling transduction of resistance plasmids. [src: prophage_amr_comobilization]
- Fisarova et al. (2021) showed high-frequency transduction of AMR plasmids by S. epidermidis phages. [src: prophage_amr_comobilization]

## Data and Methods

The analysis used the [[entities/kbase-ke-pangenome]] database. The tables bakta_amr, bakta_annotations and bakta_pfam_domains identified AMR and prophage markers. [src: prophage_amr_comobilization] The tables gene, gene_genecluster_junction and gene_cluster gave gene coordinates and cluster membership. [src: prophage_amr_comobilization] The tables genome, pangenome and gtdb_taxonomy_r214v1 gave species membership, genome counts and taxonomy. [src: prophage_amr_comobilization]

Generated data files:

- amr_clusters.csv has 83,008 rows of AMR gene clusters with species, core/accessory status and gene names. [src: prophage_amr_comobilization]
- prophage_marker_clusters.csv has 3,465,244 rows of prophage marker clusters from keyword and Pfam detection. [src: prophage_amr_comobilization]
- amr_prophage_species_summary.csv has 27,702 rows of per-species AMR and prophage counts with taxonomy. [src: prophage_amr_comobilization]
- amr_prophage_distances.csv has 36,041 rows of per-AMR-gene-instance distance to the nearest prophage marker. [src: prophage_amr_comobilization]
- JSON files store the census statistics, co-localization summary, H1 Fisher's exact test results with threshold sensitivity, H2 regression and correlation results, and an integrated synthesis of all hypotheses. [src: prophage_amr_comobilization]

Notebooks: 01_amr_prophage_census.py ran the census of AMR and prophage markers across all species. [src: prophage_amr_comobilization] 02_gene_neighborhood_coloc.py calculated gene-level co-localization distances for the top-100 species. [src: prophage_amr_comobilization] 03_conservation_test.py tested H1 with Fisher's exact test of proximity × conservation. [src: prophage_amr_comobilization] 04_species_breadth_test.py tested H2 by regressing AMR breadth on prophage density. [src: prophage_amr_comobilization] 05_synthesis.py attempted H3 and synthesized all hypotheses. [src: prophage_amr_comobilization]

## Caveats and Open Work

- Distances are ordinal gene positions parsed from gene_id, not base pairs, so true genomic distances may differ. [src: prophage_amr_comobilization]
- Prophages are identified by keyword/Pfam matching on bakta_annotations, not by tools such as PHASTER or geNomad. This may include false positives such as phage-defense systems and miss divergent prophages. [src: prophage_amr_comobilization]
- Co-localization used 20 genomes per species. The report says exhaustive analysis of all 293K genomes would strengthen the findings. [src: prophage_amr_comobilization]
- The H1 effect is modest and heterogeneous across species. [src: prophage_amr_comobilization]
- H1 conservation labels vary by species because of pangenome calling. [src: prophage_amr_comobilization]
- H2 is correlational and does not prove phage-mediated transfer. [src: prophage_amr_comobilization]
- H3 stays open: Fitness Browser overlap with GTDB species was too limited. [src: prophage_amr_comobilization]

Next analyses the report proposes:

- Apply geNomad or PHASTER to genomes in the KBase Data Lakehouse and ingest a new table, replacing keyword-based prophage detection with a validated tool and reducing false positives. [src: prophage_amr_comobilization]
- Use scaffoldseq contig sequences to calculate true genomic distances instead of ordinal gene positions. [src: prophage_amr_comobilization]
- Revisit H3 as Fitness Browser coverage expands, to test whether prophage-proximal AMR genes have distinct fitness costs. [src: prophage_amr_comobilization]
- Use the pangenome-level co-localization data to distinguish AMR genes mobilized by prophages, plasmids and ICEs. [src: prophage_amr_comobilization]
- Analyze the WHO priority pathogen subset (K. pneumoniae, A. baumannii, P. aeruginosa, E. coli) in greater depth with all available genomes. [src: prophage_amr_comobilization]

## Slots Into

- [[concepts/prophage-proximity-and-amr-gene-conservation]]: proximal AMR genes are 67.6% accessory versus 65.5% for distal ones, and the effect reverses at ≤5 genes. [src: prophage_amr_comobilization]
- [[concepts/prophage-density-and-amr-repertoire-breadth-across-species]]: rho=0.572 across 4,770 species, robust to genome count and across phyla. [src: prophage_amr_comobilization]
- [[concepts/fitness-cost-of-antimicrobial-resistance-genes]]: the fitness-cost test could not be run. [src: prophage_amr_comobilization]
- [[concepts/annotation-based-prophage-detection-prevalence-and-domesticated-remnants]]: prophages were called by keyword and Pfam matching, which may give false positives. [src: prophage_amr_comobilization]
