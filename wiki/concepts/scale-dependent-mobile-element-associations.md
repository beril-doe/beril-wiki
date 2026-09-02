---
type: "Concept"
description: "How genomic scale changes mobile-element association and mobilization inference"
sources: ["summaries/prophage_amr_comobilization__REPORT.md"]
---
# Scale-Dependent Mobile-Element Associations and Mobilization Inference

Mobile-element associations can change with the genomic scale at which they are measured: local gene proximity, contig-level co-occurrence, and species-level repertoire breadth do not provide equivalent evidence for mobilization. The [[summaries/prophage_amr_comobilization__REPORT]] shows a modest and heterogeneous local association between antimicrobial-resistance (AMR) genes and prophage markers, but a substantially stronger species-level association between prophage-marker density and AMR repertoire breadth. [src: prophage_amr_comobilization]

## Evidence Across Scales

### Gene and contig scale

Across the full pangenome inventory, 83,008 AMR gene clusters and 3,465,244 broad prophage marker clusters were identified, including 1,261,929 strict prophage-marker clusters. [src: prophage_amr_comobilization] Prophage markers were 83.8% accessory and 53.8% singleton, whereas AMR genes were 69.7% accessory and 36.1% singleton. [src: prophage_amr_comobilization]

Among 36,041 AMR gene instances from 1,953 genomes sampled across 100 species, 20,073 (55.7%) occurred on contigs carrying strict prophage markers. [src: prophage_amr_comobilization] The same analysis found that 12,026 (33.4%) were within 50 genes of a prophage marker, 7,137 (19.8%) were within 20 genes, 3,731 (10.4%) were within 10 genes, and 1,991 (5.5%) were within 5 genes; the median distance to the nearest prophage marker among co-localized AMR genes was 34 genes. [src: prophage_amr_comobilization]

At a 10-gene threshold, AMR genes near prophage markers were 67.6% accessory, compared with 65.5% for distal AMR genes. [src: prophage_amr_comobilization] Fisher's exact test gave an odds ratio of 1.10, one-sided p=0.005, and a bootstrap 95% confidence interval of [1.024, 1.185]. [src: prophage_amr_comobilization] The statistically significant association was therefore modest, corresponding to a 2.1 percentage point difference in accessory fraction. [src: prophage_amr_comobilization]

The local association was threshold-dependent rather than uniformly positive: the odds ratio was 0.78 at 3 genes, 0.92 at 5 genes, 1.10 at 10 genes, 1.19 at 15 genes, and 1.28 at 50 genes. [src: prophage_amr_comobilization] Only 33 of 74 testable species had species-level odds ratios above 1, and the median species-level odds ratio was 0.85. [src: prophage_amr_comobilization] This **refines** a simple proximity-based mobilization interpretation because broader windows produced stronger aggregate associations while the species-level pattern remained inconsistent. [src: prophage_amr_comobilization]

The reversal at very close range may reflect the presence of core phage components immediately adjacent to phage structural genes, whereas broader windows may capture genomic islands containing both prophage remnants and laterally transferred genes. [src: prophage_amr_comobilization] These mechanisms were interpretations rather than direct tests of mobilization. [src: prophage_amr_comobilization]

### Species and repertoire scale

Across 4,770 species, prophage marker density was positively associated with AMR repertoire breadth, with Spearman rho=0.572, p<10^-300, and n=4,770 species. [src: prophage_amr_comobilization] A log-log regression had a slope of 0.823 (SE=0.018), p<10^-300, and R²=0.30; the report states that a 10-fold increase in prophage density predicts a ~6.6-fold increase in AMR breadth. [src: prophage_amr_comobilization] After controlling for genome count, the partial Spearman correlation remained rho=0.464 with p=1.0×10^-253. [src: prophage_amr_comobilization]

The species-level association was significant across the five reported major phyla: Pseudomonadota (rho=0.54), Bacillota_A (rho=0.55), Bacillota (rho=0.40), Bacteroidota (rho=0.59), and Actinomycetota (rho=0.29). [src: prophage_amr_comobilization] This cross-phylogenetic consistency **supports** an association that is not explained solely by the reported phylum groupings, but it does not establish phage-mediated AMR transfer. [src: prophage_amr_comobilization]

The species-level result is compatible with two non-exclusive explanations: prophages may mobilize resistance genes through specialized or generalized transduction, and species with high recombination potential may independently acquire genes from multiple mobile elements. [src: prophage_amr_comobilization] Because the analysis is correlational, the result cannot distinguish direct phage-mediated transfer from shared ecological, genomic, or recombination-related propensity. [src: prophage_amr_comobilization]

## What Each Scale Can Support

Contig-level co-occurrence establishes that AMR genes and strict prophage markers can occupy the same contig in the analyzed genomes, but it does not by itself establish that a prophage carries, excises with, or transfers an AMR gene. [src: prophage_amr_comobilization] Gene-window results provide a scale-sensitive association whose magnitude changes from an odds ratio of 0.78 at 3 genes to 1.28 at 50 genes, so the selected distance threshold materially affects the inferred relationship. [src: prophage_amr_comobilization]

Species-level density and repertoire correlations capture broader accumulation patterns than local neighborhoods and produced the strongest association in this report. [src: prophage_amr_comobilization] However, those correlations cannot separate phage mobilization from plasmid or integrative-conjugative-element mobilization, shared recombination capacity, or other causes of joint AMR and prophage accumulation. [src: prophage_amr_comobilization]

This distinction **complements** [[concepts/environmental-resistome]], where AMR distributions are interpreted across genomic and ecological contexts, and it **refines** [[concepts/pangenome-integration]] by showing that integrated pangenome signals depend on whether evidence is summarized at the neighborhood, contig, or species level. [src: prophage_amr_comobilization] It also connects to [[concepts/phage-defense-syndromes-and-arms-race]] because keyword and Pfam-based prophage-marker identification may include phage-defense systems and may miss divergent prophages. [src: prophage_amr_comobilization]

## Measurement and Inference Limits

Distances were calculated from ordinal gene positions parsed from gene_id formats rather than base-pair coordinates, so the reported gene distances may differ from true genomic distances. [src: prophage_amr_comobilization] Prophage markers were identified by keyword and Pfam matching in bakta_annotations rather than by dedicated prophage-prediction tools such as PHASTER or geNomad, which may cause false positives, including phage-defense systems, and may miss divergent prophages. [src: prophage_amr_comobilization]

The co-localization analysis sampled 20 genomes per species for the 100-species analysis rather than examining all 293K genomes, so the local association may change under exhaustive genome-level analysis. [src: prophage_amr_comobilization] Core and accessory labels depended on species-level pangenome calling with motupan, meaning that the same gene can have different conservation status in different species. [src: prophage_amr_comobilization]

The proposed fitness comparison could not be tested because the BERDL fitness browser contained RB-TnSeq, random barcode transposon sequencing, data for only 48 model organisms, with poor overlap with the GTDB pangenome species analyzed here. [src: prophage_amr_comobilization] Whether prophage-proximal AMR genes have distinct fitness costs therefore remains unresolved. [src: prophage_amr_comobilization]

## Open Directions

- Apply geNomad or PHASTER to BERDL genomes and compare dedicated prophage calls with keyword/Pfam calls to quantify false positives, missed divergent prophages, and the contribution of phage-defense systems to the observed associations. [src: prophage_amr_comobilization]
- Recompute AMR–prophage distances from scaffold sequences at base-pair resolution and test whether the threshold-dependent odds ratios persist when ordinal gene-position errors are removed. [src: prophage_amr_comobilization]
- Analyze all available genomes from Klebsiella pneumoniae, Acinetobacter baumannii, Pseudomonas aeruginosa, and Escherichia coli to determine whether the local and species-level associations are robust to the 20-genomes-per-species sampling design. [src: prophage_amr_comobilization]
- Partition prophage, plasmid, and integrative-conjugative-element signals and fit comparative models that test whether prophage density predicts AMR breadth independently of other mobile elements. [src: prophage_amr_comobilization]
- Revisit the fitness comparison as fitness-browser coverage expands, testing whether prophage-proximal and distal AMR genes differ in RB-TnSeq fitness effects. [src: prophage_amr_comobilization]
