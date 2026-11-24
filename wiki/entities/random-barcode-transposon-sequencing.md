---
type: "Method"
description: "Pooled transposon-mutant fitness profiling across diverse conditions."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/caulobacter_fur_lipida_loss__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/essential_genome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/fitness_effects_conservation__REPORT.md", "summaries/fitness_modules__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["RB-TnSeq", "RBTnSeq", "TnSeq"]
---
# Random barcode transposon sequencing

One report crossed pathway predictions with RB-TnSeq fitness data, and another notes that its atlas cannot validate predictions for organisms without RB-TnSeq libraries. [src: pathway_capability_dependency, metal_fitness_atlas]

## Key facts

- Wetmore et al. (2015) demonstrated that RB-TnSeq across diverse conditions identifies condition-specific gene functions. [src: adp1_deletion_phenotypes]
- According to the report's PubMed account, Wetmore et al. (2015, mBio) established the method, performed 387 genome-wide fitness assays across 5 bacteria and identified 5,196 genes with significant phenotypes. [src: annotation_gap_discovery]
- Price et al. (2018) showed that mutant fitness data across thousands of conditions reveals gene function at scale. [src: fitness_modules]
- RB-TnSeq measures fitness relative to the pool average. [src: amr_fitness_cost]
- All Fitness Browser fitness scores reported in one analysis are log2 ratios from RB-TnSeq, and carbon-source conditions were identified using condition_1 and expGroup = 'carbon source'. [src: snipe_defense_system]
- The standard Fitness Browser protocol for a broad screen uses ~50-100 conditions. [src: functional_dark_matter]

## Data sources built on RB-TnSeq

The Fitness Browser supplies RB-TnSeq mutant fitness for ~194K genes across 43 bacteria, attributed to Price et al. (2018) and upstream projects. [src: conservation_fitness_synthesis, fitness_effects_conservation, core_gene_tradeoffs] The conservation gradient built on it spans 194,216 protein-coding genes across 43 diverse bacteria, from archaea (Methanococcus) to plant pathogens (Ralstonia) to gut commensals (Bacteroides). [src: conservation_fitness_synthesis] One report draws on the database kescience_fitnessbrowser, using the tables genefitness, gene, exps and ortholog. [src: fitness_modules] The Caulobacter data (orgId=Caulo) contain 198 experiments. [src: caulobacter_fur_lipida_loss]

## What the data have shown

- In the Fitness Browser analysis, 25,271 genes (17.8%) are true trade-off genes: important (fit < -1) in some conditions and burdensome (fit > 1) in others. [src: core_gene_tradeoffs]
- In Caulobacter, the genome-background phenotype-bearing rate is 33.25% (n=3943 genes; K=1311 phenotype-bearing), with phenotype-bearing defined as |fitness t| > 4 in at least 2 envelope-stress experiments. [src: caulobacter_fur_lipida_loss]
- In Acinetobacter baylyi ADP1, 499 genes are essential on minimal media versus 346 on LB. The report attributes the difference to the additional biosynthetic burden of minimal media. [src: acinetobacter_adp1_explorer]
- The report states that its own per-gene, per-condition analysis and the Borchert machine-learning approach both show that RB-TnSeq data hold functional information beyond simple essentiality calls. [src: annotation_gap_discovery] According to the report's PubMed account, Borchert et al. (2024) applied independent component analysis to Pseudomonas putida RB-TnSeq data and identified 84 functional gene modules. [src: annotation_gap_discovery] The report proposes that such approaches could resolve gaps missed by per-gene analysis. [src: annotation_gap_discovery]
- The report contrasts its experimental RB-TnSeq essentiality across 48 organisms with Duffield et al. (2010), who computationally identified 52 conserved essential proteins across 14 bacterial genomes. [src: essential_genome]
- The DvH work adds a pangenome conservation dimension to the barcoded-library fitness measurements of Trotter et al. (2023). [src: field_vs_lab_fitness] The report claims to be the first analysis to stratify RB-TnSeq fitness effects by ecological relevance. [src: field_vs_lab_fitness]
- One report describes direct RB-TnSeq ManXYZ fitness measurements in Escherichia coli K-12 from the Keio collection over 168 experiments, citing Price et al. 2018. [src: snipe_defense_system]
- Another report crossed GapMind pathway-completeness predictions with RB-TnSeq fitness data from the Fitness Browser to classify 161 organism-pathway combinations across 7 model bacteria into four categories, to assess metabolic capability versus dependency. [src: pathway_capability_dependency]

## Metrics used in the ADP1 triple-essentiality study

The ADP1 minimal-media analysis used essentiality_fraction and fitness-based classification. [src: adp1_triple_essentiality] The report describes TnSeq fitness as a continuous growth-rate-cost measure, useful for fitness effects and gene importance. [src: adp1_triple_essentiality] It describes the essentiality fraction as a continuous cross-condition measure that is poor for lethality but useful for condition-dependent importance. [src: adp1_triple_essentiality] The refined analysis added binary vectors at 5 thresholds (0.01-0.20) alongside the continuous measures. [src: adp1_triple_essentiality] Thresholds were chosen from the essentiality_fraction distribution (mean=0.026, median=0.0). [src: adp1_triple_essentiality] Fitness was inverted (fitness × -1) for receiver operating characteristic (ROC) analysis. [src: adp1_triple_essentiality] The report cites Price et al. (2018) for this methodology. [src: adp1_triple_essentiality]

## Limits and caveats

- Essentiality calls are an upper bound. Missing insertions can reflect small gene size, AT-rich sequence or scaffold edge effects rather than true essentiality. [src: essential_genome] See [[concepts/limits-of-transposon-based-essentiality-calls]].
- Essentiality is defined under library construction conditions, typically rich media, so genes essential only under stress are missed. [src: essential_genome]
- Condition-type stratification only partially addresses the fact that laboratory RB-TnSeq does not capture the full range of natural selective pressures. [src: pathway_capability_dependency]
- The Pan-Bacterial Metal Fitness Atlas scores 27,702 species but cannot validate predictions for organisms without RB-TnSeq libraries. [src: metal_fitness_atlas]
- In the DvH analysis, 678 essential genes (80.1% core) are excluded because no transposon mutants were recovered, so they lack fitness data. [src: field_vs_lab_fitness]
- Fitness measurements concern single-gene knockouts and do not capture epistatic interactions. [src: fitness_effects_conservation]
- Singleton or novel genes may lack fitness data because of poor transposon coverage rather than true neutrality. [src: fitness_effects_conservation]
- Insertions can cause polar effects on downstream genes, which may confound fitness for AMR (antimicrobial resistance) genes in operons. [src: amr_fitness_cost]
- About 4.6% of AMR genes are putatively essential because they are absent from fitness matrices. If these are the most costly AMR genes, the +0.086 estimate is a lower bound. [src: amr_fitness_cost] That +0.086 is the difference between AMR knockout fitness (−0.024) and non-AMR knockout fitness (~−0.11), not an absolute selection coefficient. [src: amr_fitness_cost]
- The RB-TnSeq organisms are lab-adapted strains with extensive evolutionary time to compensate for resistance costs. [src: amr_fitness_cost]
- Organisms with fewer than ~100 experiments produce weaker fitness modules. Caulo, with 198 experiments, showed only 2.9x correlation enrichment. [src: fitness_modules]
- The Caulobacter compendium has zero iron-limitation experiments out of 198. [src: caulobacter_fur_lipida_loss] This failed the preflight requirement of at least 3, so the report descoped hypothesis H2 to the envelope axis only. [src: caulobacter_fur_lipida_loss]
- Counter-ion effects would be proportionally smaller at typical RB-TnSeq concentrations (0.05–2 mM). This is consistent with the report's finding that counter ions are negligible for genome-wide fitness. [src: counter_ion_effects]

## Proposed experiments

- Caulobacter: fitness experiments under bipyridyl chelation, ferric salt supplementation and hemin, to close the iron axis of H2. [src: caulobacter_fur_lipida_loss]
- Metals: manganese RB-TnSeq in MR-1, Keio, Cup4G11, Putida and Caulo, and chromium RB-TnSeq in MR-1, Cup4G11, Keio and pseudo3_N2E3. [src: metal_fitness_atlas]
- Uranium RB-TnSeq in MR-1, ANA3, PV4 and Cup4G11. The report notes the current uranium effect (delta=+0.035, p=0.34) is not significant, and more organisms would show whether uranium fitness genes are neutral or the effect was underpowered. [src: metal_fitness_atlas]
- Tungsten RB-TnSeq in Methanococcus_S2, Methanococcus_JJ and Keio, to test whether tungsten dependence is unique to sulfate reducers. [src: metal_fitness_atlas]
- Libraries for key bioleaching species, to bridge the gap between the atlas and industrial applications. [src: metal_fitness_atlas]
- Counter ions: RB-TnSeq with matched metal chloride and sulfate concentrations in a single organism. This would remove the aerobic/anaerobic confound in the psRCH2 comparison. [src: counter_ion_effects]
- ADP1: comparing condition-specificity profiles with Fitness Browser data for organisms grown on overlapping carbon sources such as glucose and lactate. [src: adp1_deletion_phenotypes]
- Pseudomonas: cross-referencing carbon pathway predictions with RB-TnSeq fitness data from kescience_fitnessbrowser, to validate which pathways matter in specific carbon sources. [src: pseudomonas_carbon_ecology]
- Fitness modules: extending the analysis to additional organisms as new RB-TnSeq datasets become available. [src: fitness_modules]

### Dark-gene roadmap

RB-TnSeq libraries already exist for the Fitness Browser organisms. [src: functional_dark_matter] The report states that 10 RB-TnSeq experiments cover 45% of the top 500 dark genes. [src: functional_dark_matter] It identifies 14,450 hypothesis-bearing dark genes across all 42 organisms and recommends targeted RB-TnSeq or CRISPRi (CRISPR interference) under predicted conditions. [src: functional_dark_matter] It pairs targeted screens with Route A and broad phenotypic screens with Route B. [src: functional_dark_matter] For the darkest genes it recommends broad screens, and E. coli K-12 has 109 genes in this category. [src: functional_dark_matter]

- The proposed MR-1 stress screen uses 5 stress conditions (oxidative, osmotic, metal, heat, pH). It addresses 161 hypothesis-bearing dark genes, including candidate 202463 (fit=6.4 under stress). [src: functional_dark_matter]
- The MR-1 nitrogen screen uses nitrogen limitation and amino acid supplements. It addresses the K03306 paralog family (3 genes, fits 3.9–5.5) and 74 total dark genes. [src: functional_dark_matter]
- The top 5 fitness-active candidates (4 in MR-1, 1 in P. putida N2C3) are described as immediately testable. [src: functional_dark_matter]
- The report proposes testing the K03306 paralog family under nitrogen limitation and comparing single and double mutants. [src: functional_dark_matter]
- The report prioritizes new organisms for library construction by phylogenetic gap filled, laboratory tractability, overlap with widespread dark gene families, and environmental or biomedical relevance. [src: functional_dark_matter]

The Caulobacter notebook ranks Path A and Path B Fur-released gene sets by RB-TnSeq fitness and checks the H2 threshold. [src: caulobacter_fur_lipida_loss]
