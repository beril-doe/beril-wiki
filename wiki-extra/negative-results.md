# Negative Results and Caveats

What each project reports as limitations, null results, or abandoned
analyses — read before repeating an analysis.

## [[summaries/acinetobacter_adp1_explorer__REPORT|Acinetobacter baylyi ADP1 Data Explorer]]

No gene has measurements across all 6 data modalities, and FBA flux data cover only 15% of genes; consequently, the FBA-TnSeq concordance analysis is limited to 866 genes. [src: acinetobacter_adp1_explorer]

The pangenome cluster mapping is indirect and passes through 3 tables. Although it is 100% complete at the reported gene level, the indirection could introduce edge cases where clusters split or merge between the KBase Data Lakehouse and ADP1 pangenome analyses. [src: acinetobacter_adp1_explorer]

The 87% dependence of growth phenotype predictions on gapfilled reactions limits interpretation of those predictions, and the 243 missing functions represent gaps in genomic evidence that affect prediction reliability. [src: acinetobacter_adp1_explorer]

The database covers only *A. baylyi*, so cross-species comparisons require comparable databases for other organisms. [src: acinetobacter_adp1_explorer]

The observed FBA-TnSeq discordance, urea-specific fitness pattern, core-metabolism conservation, and gapfilling dependence are primarily results from this ADP1-centered dataset. The report presents pathway enrichment of the 227 discordant genes, cross-species fitness comparison, PhageFoundry cross-referencing, urea-specific gene identification, and pangenome-informed gapfill confidence assessment as future analyses rather than completed findings. [src: acinetobacter_adp1_explorer]

## [[summaries/adp1_deletion_phenotypes__REPORT|ADP1 Deletion Collection Phenotype Analysis]]

- Growth ratios are single-timepoint measurements with unknown technical noise, so condition-specificity scores may reflect measurement error as well as biology. [src: adp1_deletion_phenotypes]
- The complete matrix contains 2,034 genes and excludes 499 essential genes plus 316 genes with incomplete data, biasing the analysis toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]
- Only 8 carbon sources were tested, so the approximately 5 independent dimensions may increase when additional conditions are measured. [src: adp1_deletion_phenotypes]
- Pangenome core/accessory status comes from the KBase Data Lakehouse’s species-level pangenome for *A. baylyi* and may have limited resolution compared with a population-level analysis. [src: adp1_deletion_phenotypes]
- The low clustering silhouette score and absent FDR-significant enrichments support a gradient interpretation, but the report’s proposed independent component analysis (ICA) and expanded condition panel remain future work rather than completed analyses. [src: adp1_deletion_phenotypes]

## [[summaries/adp1_triple_essentiality__REPORT|Triple Essentiality Concordance Analysis for *Acinetobacter baylyi* ADP1]]

The original analysis is restricted by design to 478 TnSeq-dispensable genes because TnSeq-essential genes do not provide viable deletion mutants for the growth-rate analysis. Therefore, its null result concerns growth variation among dispensable genes and cannot be interpreted as a whole-genome test of FBA lethality prediction. [src: adp1_triple_essentiality]

The Q25 threshold flags the bottom 25% of growth rates separately in each condition, so the reported “any defect” rate across eight conditions is an aggregation-dependent quantity. The report notes an expected rate of 1 − 0.75⁸ = 90% under independent conditions, compared with the observed 72%, reflecting positive inter-condition correlation. [src: adp1_triple_essentiality]

The refined knockout comparison merges minimal-media and rich-media calls by prioritizing minimal-media data and using rich-media data as fallback. Rich-media knockout data covered 2,953 genes, including 346 essential and 2,607 dispensable genes; the merged minimal-media set covered 3,092 genes, including 499 essential genes. [src: adp1_triple_essentiality]

Proteomics expression was averaged across 7 *Acinetobacter* strains rather than measured only in the exact knockout assay condition, so its association with essentiality is independent supporting evidence rather than a condition-matched causal test. [src: adp1_triple_essentiality]

The five RB-TnSeq thresholds were tested without formal multiple-testing correction. The report states that because every threshold produced negative Cohen’s kappa, correction would not change the conclusion of systematic disagreement across the tested thresholds. [src: adp1_triple_essentiality]

The proposed explanations for TnSeq/knockout discordance—including partial or truncated protein production, read-through transcription, retained functional domains, and condition aggregation—are mechanistic hypotheses rather than directly resolved demonstrations in this report. Likewise, the proposed explanation that trace aromatics in experimental media account for aromatic-pathway discordance requires testing with measured media composition and revised FBA constraints. [src: adp1_triple_essentiality]

The report recommends condition-matched TnSeq and knockout experiments, domain- and insertion-position analysis of the 211 knockout-essential/TnSeq-dispensable genes, addition of trace aromatic compounds to FBA media definitions, condition-specific flux simulations, and combined FBA-plus-fitness-plus-proteomics prediction. [src: adp1_triple_essentiality]

## [[summaries/alphafold_msa_annotation__REPORT|AlphaFold MSA Depth as a Lens on the Bacterial Annotation Gap]]

- Only 29.3% of gene clusters bridged to AlphaFold MSA depths because the analysis required a non-UPI UniProt accession; the remaining 70.7% likely contains a larger annotation gap, but that inference is not directly measured. [src: alphafold_msa_annotation]
- MSA depth was looked up for each gene cluster's representative sequence, so within-cluster sequence diversity was ignored and the representative may have higher or lower MSA depth than typical cluster members. [src: alphafold_msa_annotation]
- The 293K genomes were not phylogenetically balanced; common taxa such as *Pseudomonas* and *E. coli* were over-represented, influencing core-gene counts and MSA-depth distributions. [src: alphafold_msa_annotation]
- Spearman ρ = 0.7563 was computed on the full 38,051,842-pair dataset without subgroup stratification, so its value may differ among core, auxiliary, and singleton clusters and among organisms with different annotation gaps. [src: alphafold_msa_annotation]
- The analysis used a static version-6 KBase Data Lakehouse AlphaFold snapshot, and later UniProt deposits may change MSA depths. [src: alphafold_msa_annotation]

## [[summaries/amr_cofitness_networks__REPORT|AMR Co-Fitness Support Networks]]

- The flagellar and biosynthesis enrichment may reflect shared “useless under laboratory conditions” status rather than mechanistic co-regulation. A permutation matched on mean fitness level, rather than only conservation class, is required to distinguish these explanations. [src: amr_cofitness_networks]
- Cofitness is not equivalent to co-regulation: high cofitness indicates shared fitness phenotypes, not direct transcriptional control. Missing fitness values were treated as zero in z-score space through `np.nan_to_num`, which approximates but does not equal pairwise-complete Pearson correlation; the report considers the dense Fitness Browser matrices unlikely to substantially alter conclusions. [src: amr_cofitness_networks]
- GO-term granularity may obscure specific signals because broad categories such as transmembrane transport and membrane functions appear in nearly all support networks and genomes. [src: amr_cofitness_networks]
- At |r| > 0.3, the mean support network contains 233 genes and therefore includes many weak associations; confirmation at |r| > 0.4 is needed. [src: amr_cofitness_networks]
- The null result for the relationship between network size and fitness cost may reflect insufficient variance in fitness cost across genes. [src: amr_cofitness_networks]
- The 28 organisms are lab-adapted, phylogenetically biased, include many Pseudomonas organisms, and have limited ecological diversity. [src: amr_cofitness_networks]
- The operon-exclusion heuristic uses matrix row index position as a proxy for genomic proximity, although genomic `begin`, `end`, and `strand` columns were available for coordinate-based exclusion. Only 0.6% of pairs were excluded by the current heuristic. [src: amr_cofitness_networks]
- The most important follow-up analyses are fitness-matched permutations; cofitness computed separately for antibiotic and standard-growth conditions; direct assessment of mean fitness for flagellar knockouts; Pfam-domain enrichment; and testing other conditionally dispensable gene classes such as phage-defense and secondary-metabolite genes. [src: amr_cofitness_networks]

## [[summaries/amr_environmental_resistome__REPORT|Environmental Resistome at Pangenome Scale]]

Environment and phylogeny remain deeply entangled despite family-level controls; some families are nearly entirely clinical, and only 14% of tested families showed significant within-family effects. NCBI sampling strongly overrepresents clinical isolates, while soil and aquatic species are undersampled, potentially inflating the clinical-versus-environmental contrast. Majority-vote species classifications collapse within-species variation, although sensitivity analyses at 60–90% thresholds partly mitigate this issue. [src: amr_environmental_resistome]

AMRFinderPlus-focused annotation may underestimate novel environmental resistance and bias results toward clinical enrichment, where resistance genes are better characterized. The 95% prevalence threshold for core AMR is dependent on species genome count, so core/accessory labels are imprecise for sparsely sampled species. The association is correlational: clinical exposure could increase AMR, AMR could contribute to clinical isolation, or both could reflect virulence-resistance co-selection. [src: amr_environmental_resistome]

Effect sizes were modest despite very small p-values: environment explained 2–13% of variance in AMR composition (η² = 0.02–0.13), while phylogeny likely explains more. The 18.7% of clusters (15,550) lacking mechanism assignments may bias mechanism comparisons if unclassified clusters are distributed non-randomly across environments. [src: amr_environmental_resistome]

Planned but unperformed analyses included PCoA ordination, PERMANOVA, environment-specific gene identification, metagenome-assembled genome/isolate assessment, and an archaea-specific analysis. The originally planned per-genome Fisher’s exact test was replaced by the species-level within-species proxy because billion-row joins were computationally costly. [src: amr_environmental_resistome]

## [[summaries/amr_fitness_cost__REPORT|Fitness Cost of Antimicrobial Resistance Genes]]

- All **25** tested organisms are lab-adapted strains. Laboratory compensation may have reduced measurable costs relative to wild strains, so the estimate may underestimate costs in natural populations. [src: amr_fitness_cost]
- Tier 2 contains **86%** of the AMR genes and is based on keyword matching from Bakta annotations, which may include non-AMR genes such as general efflux transporters; the Tier 1 sensitivity analysis gives consistent results. [src: amr_fitness_cost]
- Matched antibiotic validation covers only four AMR classes: beta-lactam, aminoglycoside, chloramphenicol, and tetracycline. Macrolide, glycopeptide, and polymyxin resistance could not be validated. [src: amr_fitness_cost]
- Approximately **4.6%** of AMR genes are putatively essential and absent from fitness matrices. If these are the most costly AMR genes, **+0.086** is a lower bound. [src: amr_fitness_cost]
- RB-TnSeq measures fitness relative to the pool average. The **+0.086** value is the difference between AMR knockout fitness (**−0.024**) and non-AMR knockout fitness (approximately **−0.11**), not an absolute selection coefficient; comparison with isogenic-strain literature is not a direct equivalence. [src: amr_fitness_cost]
- Transposon insertions can have polar effects on downstream genes in operons, potentially confounding AMR-gene fitness measurements. [src: amr_fitness_cost]
- The product classifier does not handle fosfomycin or tellurite resistance annotations, leaving approximately **25 genes** in the unknown mechanism category; reclassification would move them to enzymatic inactivation and metal resistance, respectively. [src: amr_fitness_cost]
- Core/accessory labels use a **≥95%** prevalence threshold, but most Fitness Browser species have few GTDB genomes: the median is **9**, with a range of **2–399**. A gene present in all **9** sampled genomes may be mislabeled core at larger sampling depth, so the core-versus-accessory null result is especially cautious for species with fewer than **20** genomes. [src: amr_fitness_cost]
- The class-matched analysis has only **157** pairs and is non-significant (**p = 0.14**) despite a mean flip of **+0.113**; the any-antibiotic analysis has greater power (**N = 797**, **p = 0.0001**). [src: amr_fitness_cost]

## [[summaries/amr_pangenome_atlas__REPORT|Pan-Bacterial AMR Gene Landscape]]

The report identifies sampling bias as a limitation because genome databases over-represent clinical pathogens, potentially inflating AMR counts for human-associated species. AMRFinderPlus also includes stress-response genes such as mercury- and arsenic-resistance genes, so the 83K hits are not all antibiotic resistance in the narrow sense. [src: amr_pangenome_atlas]

AlphaEarth embeddings covered only 28% of genomes and were biased toward genomes with geographic metadata. The Fitness Browser analysis covered only 37/48 Fitness Browser organisms with AMR genes, and these were predominantly environmental strains; consequently, it did not capture the cost of recently acquired mobile resistance in pathogens. [src: amr_pangenome_atlas]

Keyword-based mechanism classification left 22% of hits in Other/Unclassified; systematic mapping through CARD ARO terms could reduce this category. Singleton inflation may also cause some singleton AMR clusters to reflect annotation artifacts rather than true species-specific resistance genes. [src: amr_pangenome_atlas]

The six hypotheses involved many individual tests, including per-mechanism binomial tests, per-phylum correlations, and per-environment comparisons. Formal Bonferroni or FDR correction was not applied because the primary p-values were extreme, with many < 1e-100, and the report states that correction would not change the conclusions; per-gene and per-phylum tests remain exploratory and hypothesis-generating. FDR means false discovery rate. [src: amr_pangenome_atlas]

The 100% DIAMOND identity threshold used for Fitness Browser pangenome linking is conservative: it avoids paralog confusion but may miss closely related variants, including alleles differing by a single synonymous substitution, and may therefore undercount fitness effects. [src: amr_pangenome_atlas]

## [[summaries/amr_strain_variation__REPORT|Within-Species AMR Strain Variation]]

- The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly for Klebsiella pneumoniae, Staphylococcus aureus, and Escherichia coli; environmental species are underrepresented. [src: amr_strain_variation]
- Metadata sparsity limits interpretation of temporal and ecological results. Only 70% of genomes had parseable collection dates, and 52.7% had no classifiable isolation_source. [src: amr_strain_variation]
- AMR detection relies on the AMRFinderPlus database, so novel resistance mechanisms absent from that database are missed. [src: amr_strain_variation]
- ANI extraction for Mantel tests was limited to species with <=500 genomes, excluding mega-species such as Escherichia coli (15,388 genomes) and Klebsiella pneumoniae (14,240 genomes) from phylogenetic-signal analysis. [src: amr_strain_variation]
- BacDive and NCBI keyword environment classifiers are approximate, and dedicated metadata curation would improve ecotype analyses. [src: amr_strain_variation]
- Resistance-gene co-occurrence in islands does not prove co-selection; genes may simply be linked on the same mobile genetic element without functional synergy. [src: amr_strain_variation]
- The stronger phylogenetic signal of non-core than core AMR genes may be partly statistical: core genes are nearly universal by definition, producing little Jaccard-distance variance and suppressing Mantel r. [src: amr_strain_variation]

## [[summaries/annotation_gap_discovery__REPORT|Annotation-Gap Discovery via Phenotype-Fitness-Pangenome-Gapfilling Integration]]

The draft models were based on automated RAST annotations and contained systematic errors; the 42.5% baseline FBA accuracy, dominated by false positives, reflected overly permissive models that predicted growth on carbon sources the organisms could not use. [src: annotation_gap_discovery]

Gapfilling is non-unique: multiple valid solutions may exist for each false-negative case. The study used default ModelSEED gapfilling, which minimizes the number of added reactions but does not guarantee biological optimality. [src: annotation_gap_discovery]

The mapping between Fitness Browser experiment names and ModelSEED exchange reactions required manual curation of 109 carbon sources to compound IDs, so mapping errors could generate spurious false negatives. [src: annotation_gap_discovery]

Fitness significance depends on the selected absolute-fitness threshold and the number of experiments; organisms with fewer carbon-source experiments have less statistical power. [src: annotation_gap_discovery]

GapMind covers ~80 carbon and amino acid pathways rather than full metabolism, so many gapfilled reactions fall outside its coverage. [src: annotation_gap_discovery]

The FBA knockout validation was inconclusive because the models could not grow on carbon-source minimal media without the gapfilled reactions; consequently, the reactions being tested were themselves required for growth, making single-gene knockout analysis circular in this setting. [src: annotation_gap_discovery]

The dataset was phylogenetically biased: 12 of 14 organisms were Proteobacteria. The sole Bacteroidetes organism, *B. thetaiotaomicron*, had the lowest resolution rate, suggesting that the approach may be less effective for phylogenetically distant clades with divergent metabolism. [src: annotation_gap_discovery]

## [[summaries/aromatic_catabolism_network__REPORT|Aromatic Catabolism Support Network in ADP1]]

The PQQ dependency is not exclusively aromatic: PQQ-biosynthesis genes also appear as glucose-specific in the adp1_deletion_phenotypes project, where they are associated with PQQ-dependent glucose dehydrogenase. [src: aromatic_catabolism_network]

The 8-condition co-fitness matrix provides approximately 5 independent dimensions, so additional conditions are needed to sharpen subsystem boundaries. The ortholog-transferred cross-species data is confounded by organism-specific respiratory architectures, and the non-core Complex I assignments rely on correlation rather than direct physical evidence. [src: aromatic_catabolism_network]

The report proposes searching the ADP1 genome for NDH-2 and testing its deletion on quinate versus glucose; experimentally validating ACIAD3137 and ACIAD2176 by protein-protein interaction or co-purification studies; expanding the condition panel with benzoate, catechol, vanillate, iron limitation, and respiratory inhibitors; comparing Complex I retention across aromatic-degrading species using pangenome data; and adding PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints to the ADP1 FBA model. [src: aromatic_catabolism_network]

## [[summaries/bacdive_metal_validation__REPORT|BacDive Isolation Environment × Metal Tolerance Prediction]]

The heavy-metal group contains only n=10 matched isolates and was at the detection limit for d=1.00, so a larger dataset is needed to estimate the effect precisely. [src: bacdive_metal_validation]

BacDive represents culturable, described strains rather than the full diversity of environmental bacteria, and culture-collection bias may under-represent metal-tolerant extremophiles. [src: bacdive_metal_validation]

Species-level matching is lossy: 56.6% of BacDive strains did not match a GTDB species, primarily because GTDB uses different species boundaries from LPSN/DSMZ. Genome-accession matching through GCA→pangenome genome_id could improve coverage but requires a Spark query. [src: bacdive_metal_validation]

The metal tolerance score is genome-size-normalized as metal clusters divided by annotated clusters. This controls for genome size, which is important because Pseudomonadota tend to have larger genomes, but normalization does not eliminate the possibility that metal-tolerance functions correlate with total metabolic complexity. [src: bacdive_metal_validation]

The metal-utilization validation is underpowered because only 24 records matched strains with metal scores; the negative direction for positive utilizers should not be over-interpreted. [src: bacdive_metal_validation]

The absence of a significant signal in Bacillota and Bacteroidota cannot distinguish real biological differences from limited power because contamination-isolate sample sizes were small. [src: bacdive_metal_validation]

## [[summaries/bacdive_phenotype_metal_tolerance__REPORT|BacDive Phenotype Signatures of Metal Tolerance]]

The Metal Fitness Atlas scores are genome-based predictions rather than direct metal-tolerance measurements. Controlling for `n_metal_clusters` mitigates circular reasoning in partial correlations, but the associations remain phenotype-to-genome correlations rather than phenotype-to-phenotype measurements. [src: bacdive_phenotype_metal_tolerance]

Species-name matching recovered 5,647 of 27,702 GTDB species (38.4%); GCA accession matching was not implemented and could recover additional links. [src: bacdive_phenotype_metal_tolerance]

The 12-organism direct validation was underpowered: all Gram-typed organisms were Gram-negative, preventing within-set testing of H1a. [src: bacdive_phenotype_metal_tolerance]

BacDive testing is biased toward well-studied organisms, including Pseudomonas and Escherichia coli, which have many phenotype tests, whereas poorly studied species have sparse data. [src: bacdive_phenotype_metal_tolerance]

The H₂S result is underpowered because only 8 H₂S-negative species were present in the matched set; consequently, d = -0.87 is unreliable and likely inflated by small-sample bias. [src: bacdive_phenotype_metal_tolerance]

The composite-score analysis does not establish metal-specific mechanisms. Per-metal scores would be needed to test whether catalase predicts copper, urease predicts nickel, or H₂S predicts zinc, copper, and cadmium tolerance. [src: bacdive_phenotype_metal_tolerance]

Suggested follow-up includes GCA accession matching; PGLS (phylogenetic generalized least squares) or phylogenetic PCA to remove phylogenetic signal; inclusion of BacDive machine-learning-predicted phenotypes with attention to model-dependent bias; and experimental testing of the underpowered H₂S hypothesis. Urease-positive and urease-negative organisms from the same taxonomic class should be profiled with RB-TnSeq (random barcode transposon sequencing) under nickel and other metals to test nickel-specific rather than general tolerance. [src: bacdive_phenotype_metal_tolerance]

## [[summaries/bacillota_b_subsurface_accessory__REPORT|Subsurface Bacillota_B Specialization — What Distinguishes Deep-Clay Lineages from Soil Congeners?]]

The anchor cohort contains 10 genomes and the baseline contains 62. Fisher’s exact testing is considered adequate for the large 547-OG effect, but marginal effects supported by anchor counts of 3–5 are described as primarily descriptive. [src: bacillota_b_subsurface_accessory]

The anchor cohort is borehole- and porewater-dominated by construction, reflecting cultivation bias toward porewater isolates. The comparison therefore cannot test whether rock-attached Bacillota_B differ in gene content. [src: bacillota_b_subsurface_accessory]

Genus-level phylogenetic confounding is only partly mitigated: the cohort spans four orders, but the 10-genome anchor is clumped among 3 BRH-c8a genomes, 2 BRH-c4a genomes, 2 Desulfosporosinus genomes, Desulforudis, Ch130, and 1 other genome. Some enriched OGs may therefore be lineage markers rather than recurrent subsurface-specialization features. [src: bacillota_b_subsurface_accessory]

The OG hierarchy is imperfect. The analysis used Firmicutes-level OGs where available and bacteria/root fallbacks otherwise; some enriched OGs are therefore at coarse taxonomic levels. A Bacillota_B-specific eggNOG tier was unavailable because Bacillota_B genomes are distributed across legacy NCBI-taxonomy classes. [src: bacillota_b_subsurface_accessory]

Keyword-based functional categorization undercounted relevant functions: the “other_or_unannotated” group contained substantial anaerobic-respiration and electron-transfer signal, including COG1977 molybdopterin metabolism, DsrEFH-like proteins, and 2-oxoglutarate:ferredoxin oxidoreductase. Manual reclassification or an LLM-based extractor would be needed to refine category counts. [src: bacillota_b_subsurface_accessory]

The corrected iron-reduction analysis is considered robust for the multi-heme cytochrome signal but is a Phase 1 correction. It does not fully determine whether the original clay-project comparison with the Bagnoud porewater pattern should be retained; the sulfite-reduction side remains robust, whereas the iron-reduction side loses force. [src: bacillota_b_subsurface_accessory]

The report proposes applying the correction to the clay-project branch, refining the 462-OG category with an LLM-based scan, decomposing the H1 signal by genus, localizing the functions responsible for the larger anchor genomes, and testing the same enrichment framework in other phylum-matched subsurface comparisons. [src: bacillota_b_subsurface_accessory]

## [[summaries/berdl_data_atlas__REPORT|BERDL Data Atlas — Inventory, Topic Map, and Cross-Reference Synergies]]

- Join-key presence demonstrates schema-level compatibility, not valid value-space overlap. UC2–UC5 require live-cluster execution; UC1 is the only sample-validated use case. [src: berdl_data_atlas]
- Two tenant-to-agency mappings, evaluation and lambda, remain unverified by program documentation and account for 4 tables total. The mappings for phagefoundry and msyscolo were user-corrected to DOE BRaVE and DOE/NSF, respectively. [src: berdl_data_atlas]
- The realized-use audit mined project README files, so data-source mentions in research plans or notebook source may have been missed; the reported tenant breadth is therefore a lower bound. [src: berdl_data_atlas]
- Most NB05 depth counts are COUNT(*) row totals; only the canonical KBase genome count uses COUNT(DISTINCT genome_id). A pangenome gene row represents one genome-gene pair, so 1.01B gene rows correspond approximately to 293K genomes multiplied by approximately 3.4K genes per genome. [src: berdl_data_atlas]
- Across-tenant deduplication was not performed. Refdata and KBase may contain the same UniProt entries through different cluster indices, and ENIGMA and genome-depot tables share genome records with the ENIGMA SDT layer. [src: berdl_data_atlas]
- The validated UC1 cohort lacks per-residue pLDDT and structural-feature data in kescience_alphafold.alphafold_entries; these features must be ingested or computed from PDB files for downstream structure-function analysis. [src: berdl_data_atlas]
- NMDC metabolomics, proteomics, and lipidomics layers are largely untapped despite containing 3.1M, 346K, and 1.4M records, respectively, and are identified as cross-validation resources for UC4 and UC5. [src: berdl_data_atlas]

## [[summaries/caulobacter_fur_lipida_loss__REPORT|Regulatory and proteomic architecture of Δfur-permitted lipid A loss in *Caulobacter crescentus*]]

The Δ*sspB*-buffered cbb3/*fix* respiratory program is a clean transcript-level observation, but its fitness phenotype-bearing rate was 34.6%, versus 33.25% for the genome background, with hypergeometric p = 0.515 and fold = 1.04×. Consequently, the claim that respiratory ATP is required for envelope remodeling remains a working hypothesis, not an established mechanism. [src: caulobacter_fur_lipida_loss]

The fitness compendium contained zero iron-limitation experiments among 198 Caulobacter experiments, so the iron-limitation arm of H2 was descoped to envelope-only analysis. Testing that arm requires additional RB-TnSeq experiments under bipyridyl chelation, ferric supplementation, and hemin, or a cross-walk to published Δ*fur* phenotypes. [src: caulobacter_fur_lipida_loss]

CtpA was rejected at the preregistered bar because pvalue = 0.048 failed the BORDERLINE lower bound of 0.05, FDR = 0.109 failed the PASS criterion, and protein was not detected. The cumulative 4599-vs-4580 FDR = 0.035 result cannot isolate the Δ*lpxc*-specific response because it conflates Δ*fur*, Δ*sspB*, and Δ*lpxc* effects. [src: caulobacter_fur_lipida_loss]

The OM proteome had a single replicate per strain, so no per-protein statistics were available. The *lptC2* protein induction, Pal-Tol upregulation, LptD/LptE decline, and CCNA_01217 increase require replicated proteomics before publication-level claims can be made. [src: caulobacter_fur_lipida_loss]

The transcriptome used a single PYE rich-medium growth condition, and the observed Fur signal represents constitutive Δ*fur* derepression rather than a direct iron-limitation response. Caulobacter SigU lacks a characterized published regulon, and the late ChvI cohort did not pass the relaxed coherence criterion. [src: caulobacter_fur_lipida_loss]

The comparative PaperBLAST analysis was vulnerable to naming-convention false negatives, and *M. catarrhalis* was under-annotated in PaperBLAST with 162 genes total. NCBI annotation strengthened the headline absence claims, but a deeper Pfam HMM search against named RefSeq proteomes is still needed to detect unannotated paralogs. [src: caulobacter_fur_lipida_loss]

The peptidoglycan gene set included two likely regex false positives: CCNA_00565, a γ-glutamyltranspeptidase matched through “transpeptidase,” and CCNA_01833, a glucosylceramidase matched because “ceramidase” contains “amidase.” Their inclusion did not change the H4 verdict, which remained well above the ≥3 threshold. [src: caulobacter_fur_lipida_loss]

The report identifies replicated OM proteomics, targeted *lptC2* and Pal assays, SigU-induction RNA-seq, genetic tests of the dual-release model, lipidomics, iron-axis fitness experiments, Tol-Pal phospholipid-transport assays, cross-species engineering, and sequence-based homology searches as specific resolving work. [src: caulobacter_fur_lipida_loss]

## [[summaries/cf_formulation_design__REPORT|Rational Design of Protective Microbiome Formulations for Competitive Exclusion of *Pseudomonas aeruginosa* in Cystic Fibrosis Airways]]

The inhibition assays were planktonic and used PA14, whereas PA in cystic-fibrosis lungs primarily occupies structured biofilms. The carbon panel contained 22 tested substrates and omitted mucins, lipids, iron, polyamines, and the sugar alcohols identified genomically. [src: cf_formulation_design]

The metabolic model was based on 142 isolates covering 62 of 211 species (29%), and growth kinetics were available for only 32 isolates; the core cohort was enriched for deeply characterized taxa, including *Rothia*, *Streptococcus*, *Neisseria*, and *Gemella*. [src: cf_formulation_design]

Pairwise interaction data covered only 3 A × 3 B isolate combinations, and the complete 10-pair interaction matrix for the five-species core has not been measured. Moreover, `fact_pairwise_interaction` was identical to `fact_carbon_utilization`, with correlation = 1.0 and mean difference = 0.0, so endpoint OD data cannot assess per-substrate co-culture effects; current interaction conclusions rely on the RFU-based competition assay. [src: cf_formulation_design]

Engraftability was inferred from patient prevalence and transcriptional activity rather than measured after administration. Only 21 lung genomes across 5 species were available for lung-adaptation comparisons, and *M. luteus* had zero lung genomes and zero detected patient engraftability despite its central role in achieving 100% niche coverage. [src: cf_formulation_design]

PA14-based inhibition measurements have not been validated against PAO1 or ExoS+ clinical strains, although the pangenome analysis found no amino-acid pathway differences between ExoU+ and ExoS+ PA. The report therefore prioritizes testing PAO1 and 3–5 mucoid clinical PA isolates. [src: cf_formulation_design]

The primary *N. mucosa* conservation analysis used a 15-genome clade even though the PROTECT reference mapped to an 8-genome clade; the 8-genome sensitivity check showed stronger conservation, with 18/18 amino-acid pathways at >95% versus 16/18 in the 15-genome clade, 37/62 carbon pathways versus 27/62, and 1 respiratory genome. [src: cf_formulation_design]

## [[summaries/clay_confined_subsurface__REPORT|Self-Sufficiency, Anaerobic Toolkit, and Cultivation Bias in Clay-Confined Cultured Bacterial Genomes]]

- The deep anchor cohort is small (n = 9 before quality filtering), so only large effects, described as Cohen’s d > 0.7 for unfiltered comparisons, are reliably detectable; marginal results such as the within-Bacillota_B self-sufficiency comparison at p = 0.07 are descriptive. [src: clay_confined_subsurface]
- Compartment annotations were inferred from keywords in isolation-source strings, so some bentonite or “rock” entries could plausibly be porewater or rock-attached; the H3 sulfate-reduction result was reported as robust to two stricter compartment definitions. [src: clay_confined_subsurface]
- The GapMind metric covers 18 amino-acid pathways and has limited resolving power near the upper end; the report proposes checking all standard amino-acid-biosynthesis EC numbers in eggNOG as a finer-grained sensitivity analysis. [src: clay_confined_subsurface]
- eggNOG cluster-level annotations propagate within ≥90% AAI clusters, so strain-level marker variants, including a single non-functional dsrA in an otherwise complete operon, may be missed. [src: clay_confined_subsurface]
- The report recommends adding deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge; comparing BRC-3 and BIC-A1 directly; applying the sulfate-reduction/iron-reduction diagnostic to other subsurface settings; resolving Bacillota_B differences at genus level; and linking genome presence to Bagnoud’s metaproteomic evidence. [src: clay_confined_subsurface]

## [[summaries/cofitness_coinheritance__REPORT|Co-fitness and Co-inheritance in Bacterial Pangenomes]]

The prevalence ceiling limits interpretability because most Fitness Browser genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs. The analysis is therefore most informative for species with substantial auxiliary gene content. [src: cofitness_coinheritance]

The two Ralstonia organisms were excluded despite being the most phylogenetically diverse and lowest-ANI organisms in the target set, removing species that might have been especially informative. [src: cofitness_coinheritance]

Phylogenetic control was limited: stratification was available for 7 of 9 organisms, and most species lacked genomes in the far stratum (>0.05 branch distance). The near-versus-medium difference of mean phi=0.102 versus 0.067 was consistent with shared ancestry, but the missing far stratum limited full disentanglement of functional and phylogenetic effects. [src: cofitness_coinheritance]

Pairwise co-fitness captures gene-pair relationships, whereas ICA modules capture multi-gene coordinated regulation and may better represent selective units constraining co-inheritance. [src: cofitness_coinheritance]

Near-clonal species behaved differently: Ddia6719 (ANI 99.47%) had delta=+0.093 and pseudo3_N2E3 (ANI 99.66%) had delta=+0.026. Both retained enough accessory variation to detect co-inheritance, but their high baseline phi values make absolute phi values less interpretable. [src: cofitness_coinheritance]

Proposed next analyses are to restrict comparisons to auxiliary-only pairs where both clusters are below 95% prevalence; calculate co-fitness directly from raw genefitness data for Ralstonia and other organisms lacking precomputed values; resolve reference-genome mapping for improved phylogenetic control; build module co-transfer networks and test cross-module prediction; and expand to species with >30% auxiliary genes and existing co-fitness data. [src: cofitness_coinheritance]

## [[summaries/cog_analysis__REPORT|COG Functional Category Analysis]]

COG annotations covered approximately 70% of genes, so unassigned genes may skew the distributions. [src: cog_analysis]

The analysis used 32 species, and a larger sample could reveal phylum-specific patterns that are not visible in the current comparison. [src: cog_analysis]

Composite COG categories were counted once per gene rather than split among their component functions, and [[entities/eggnog]] v6 annotations may differ from original COG assignments. [src: cog_analysis]

The report identifies future analytical directions including comparisons across additional taxonomic groups, detailed examination of COG V defense and COG L recombination functions, and correlation of novel-gene functions with environmental metadata to test whether patterns vary by habitat. [src: cog_analysis]

## [[summaries/conservation_fitness_synthesis__REPORT|Gene Conservation, Fitness, and the Architecture of Bacterial Genomes]]

Module-family breadth did not predict conservation: families spanning more organisms did not have higher core fractions, with rho=-0.01 and p=0.91. The report attributes the absence of a gradient in part to an already high baseline that leaves little room for one. [src: conservation_fitness_synthesis]

Accessory genes were not systematically burdensome. Contrary to the streamlining hypothesis, they were less costly than core genes. [src: conservation_fitness_synthesis]

Condition-specific fitness did not mean niche-specific fitness. Genes with strong condition-specific effects were more likely to be core rather than accessory, indicating that core genes simply had more detectable effects under the tested conditions. [src: conservation_fitness_synthesis]

The findings do not directly establish fitness in natural environments: the laboratory measurements capture the cost of maintaining genes, while the pangenome captures evolutionary pressure to retain them. The costly-and-conserved category is therefore evidence for, rather than a direct measurement of, purifying selection in nature. [src: conservation_fitness_synthesis]

## [[summaries/conservation_vs_fitness__REPORT|Conservation vs Fitness — Linking FB Genes to Pangenome Clusters]]

The essential-gene definition is an upper bound: genes without fitness data may lack transposon insertions because they are short, occur in low-complexity regions, or lie at scaffold edges, rather than because they are essential. Gene-length validation found that essential genes were slightly shorter on average, indicating possible insertion bias. [src: conservation_vs_fitness]

Pangenome coverage varies among clades, and clades containing only 2 genomes can have trivially high core fractions because a gene present in both genomes equals 100% core, reducing the discriminative power of the core-versus-auxiliary classification. [src: conservation_vs_fitness]

The main Escherichia coli clade was absent from the pangenome because it contained too many genomes; Keio, an E. coli BW25113 strain, mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness]

Essentiality was measured under a single growth condition represented by the RB-TnSeq library construction conditions, so genes essential only under stress conditions were not captured. [src: conservation_vs_fitness]

Dyella79 was excluded from Phase 2 because the FB gene table used the locus-tag format N515DRAFT_* whereas the protein sequences used ABZR86_RS*, producing a 0% join rate. [src: conservation_vs_fitness]

Ten organisms were excluded from Phase 2 because they had <90% DIAMOND coverage, reducing taxonomic breadth. [src: conservation_vs_fitness]

## [[summaries/core_gene_tradeoffs__REPORT|Core Gene Paradox — Why Are Core Genes More Burdensome?]]

- Laboratory conditions capture only a fraction of the environmental conditions bacteria face in nature. [src: core_gene_tradeoffs]
- “Burden” defined as fit > 1 may reflect trade-offs rather than true dispensability. [src: core_gene_tradeoffs]
- The 90% identity threshold used for DIAMOND matching may miss rapidly evolving genes. [src: core_gene_tradeoffs]
- Fitness Browser condition types are biased toward experimentally convenient conditions rather than ecologically relevant conditions. [src: core_gene_tradeoffs]

## [[summaries/costly_dispensable_genes__REPORT|The 5,526 Costly + Dispensable Genes]]

- “Burden” is defined as max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and the result is sensitive to noise in the fitness data. [src: costly_dispensable_genes]
- SEED and KEGG annotations cover only 56-79% of genes, and the unannotated fraction may have different functional profiles. [src: costly_dispensable_genes]
- The pangenome core/accessory classification is binary; using the fraction of genomes carrying each gene would provide more resolution. [src: costly_dispensable_genes]
- The 90% identity DIAMOND threshold used for Fitness Browser–pangenome linking may miss recently acquired genes with low sequence similarity. [src: costly_dispensable_genes]
- The extreme 21.5% costly+dispensable proportion in psRCH2 may reflect strain-specific genomic features rather than a general pattern. [src: costly_dispensable_genes]
- Ortholog groups are assigned using bidirectional best hits across 48 organisms, so genes with orthologs outside this set may be misclassified as orphans. [src: costly_dispensable_genes]
- Condition-specific phenotype data is biased toward conditions that can be tested in the laboratory. [src: costly_dispensable_genes]

## [[summaries/counter_ion_effects__REPORT|Counter Ion Effects on Metal Fitness Measurements]]

The 39.8% overlap depends on the NaCl-importance threshold, defined using fit < -1 or n_sick ≥ 1; stricter or more permissive thresholds could reduce or increase the overlap. The *S. elongatus* estimate is especially sensitive because it had 12 NaCl experiments spanning 0.5–250 mM, whereas other organisms had 1–6 NaCl experiments. [src: counter_ion_effects]

NaCl cannot isolate chloride because it delivers both Na⁺ and Cl⁻ and produces osmotic effects. A KCl or choline chloride control would more specifically test chloride effects, although some Fitness Browser organisms have choline chloride experiments at different concentrations. [src: counter_ion_effects]

Approximately 14.3% of protein-coding genes, classified as putative essential genes, lacked transposon insertions and were absent from both NaCl and metal-fitness data. These genes are 82% core, and their exclusion affects the original and corrected conservation analyses equally. [src: counter_ion_effects]

Manganese, cadmium, selenium, mercury, iron, molybdenum, and tungsten were each tested in only 1 organism, so their overlap statistics lack cross-organism replication. The psRCH2 CuCl₂–CuSO₄ comparison is additionally limited by aerobic/anaerobic confounding. [src: counter_ion_effects]

The shared-stress versus metal-specific classification did not include formal functional-enrichment tests; the SEED annotation comparison was descriptive. The proposed mechanistic categories therefore remain hypotheses requiring direct functional testing. [src: counter_ion_effects]

The report proposes formal COG, KEGG, and PFAM enrichment tests; comparison with choline chloride; module-level analysis using independent component analysis (ICA); refinement of condition-specific metal-gene analysis; and matched CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ RB-TnSeq experiments under identical conditions. It also proposes DvH NaCl dose-response experiments at 0.1, 1, 10, 100, and 500 mM to match effective chloride doses. [src: counter_ion_effects]

## [[summaries/discoveries|Discoveries Log]]

Several results are explicitly exploratory, coverage-limited, or dependent on analytical specification. The SSO geochemical model lacks ingested measurement values; AlphaEarth analyses had 3,838/83,287 genomes with NaN dimensions and 36.6% of genomes clustered at coordinates with more than 50 genomes of more than 10 species; only 6.8% of species had sufficient embedding coverage. [src: discoveries]

The NMDC metabolomics dataset was dominated by one study: 125/131 samples (95%) came from `nmdc:sty-11-r2h77870`. Only approximately 2% of compounds had KEGG IDs, substring matching risked collisions such as leucine versus isoleucine, and three amino-acid pathways—cysteine, histidine, and lysine—were untestable because compounds were absent. [src: discoveries]

BacDive species matching linked 42,227 strains (43.4% of 97K) to 6,426 GTDB pangenome species, leaving 56.6% unmatched because GTDB species boundaries differ from LPSN/DSMZ taxonomy. Phenotype-only metal-tolerance models were phylogenetically confounded: adding phenotype features changed R² by -0.009, while the full genome-resistance model reached R²=0.63. [src: discoveries]

Annotation proxies require source-specific validation. EggNOG `Preferred_name='lanM'` produced 505 additional hits with zero overlap with 62 Bakta-validated Lanmodulin genomes, eggNOG KO K02030 produced 46,369 nonspecific hits, and only 418 of 5,092 genomes with any xoxF marker hit both eggNOG K00114 and Bakta lanthanide-dependent methanol-dehydrogenase products. Results should therefore report marker definitions explicitly and avoid treating generic KOs or stale preferred names as definitive. [src: discoveries]

## [[summaries/ecotype_analysis__REPORT|Ecotype Correlation Analysis]]

- AlphaEarth embeddings covered only 28.4% of genomes, limiting the environmental signal available for analysis. [src: ecotype_analysis]
- Geographic coordinates in NCBI metadata were often missing or imprecise, reducing the quality of environmental associations. [src: ecotype_analysis]
- Partial correlations assume linear relationships between distance matrices and may not capture nonlinear ecological effects. [src: ecotype_analysis]
- Geographic coordinates are less biologically meaningful for host-associated organisms because they generally describe collection sites rather than the organisms’ actual microenvironments. [src: ecotype_analysis]

## [[summaries/ecotype_env_reanalysis__REPORT|Ecotype Reanalysis — Environmental vs Human-Associated Species]]

- **No downsampling:** The reanalysis produced partial correlations 27x higher overall than the original analysis. The report states that absolute values are not comparable, although the within-method group comparison is valid. [src: ecotype_env_reanalysis]
- **NaN exclusion:** Environmental species had a higher NaN rate, 21%, than human-associated species, 7%, so the environmental group was more filtered. The report states that this would bias toward finding a stronger environmental signal, which was not observed. [src: ecotype_env_reanalysis]
- **K. pneumoniae exclusion:** Klebsiella pneumoniae was excluded because it exceeded Spark's maxResultSize during gene-cluster extraction and consequently had no correlation data. [src: ecotype_env_reanalysis]
- **Majority-vote classification:** A species with 51% gut genomes would be classified as Human-associated. The continuous Spearman analysis was used to address this limitation and also found no relationship. [src: ecotype_env_reanalysis]
- **Unresolved methodological discrepancy:** A specific comparison of downsampled versus full-genome extraction is needed to explain the 27x partial-correlation discrepancy. [src: ecotype_env_reanalysis]
- **Functional specificity:** Testing gene subsets, including transport and secondary-metabolism categories, could determine whether environmental effects are masked by whole-genome Jaccard distances. [src: ecotype_env_reanalysis]
- **Environment ontology:** Repeating the analysis with structured ENVO terms from env_broad_scale could test whether more precise environmental classification changes the result. [src: ecotype_env_reanalysis]
- **Genome-count control:** Adding genome count as a covariate could test whether unequal sampling depth inflates correlations in species with more genomes. [src: ecotype_env_reanalysis]

## [[summaries/ecotype_functional_differentiation__REPORT|Ecotype Functional Differentiation]]

- The analysis covered 12 species from a 15-species sample (80%), out of 456 eligible species; although the stratified sample represented pangenome-size bins, it may not capture broader phylogenetic or ecological diversity. [src: ecotype_functional_differentiation]
- KMeans was used because HDBSCAN was unavailable on the cluster; KMeans assumes spherical clusters and requires a selected k, whereas HDBSCAN could better handle variable-density subpopulations. [src: ecotype_functional_differentiation]
- Approximately 38% of gene clusters had COG annotations, leaving 62% unannotated; unannotated ecotype-specific adaptive genes may therefore be missed or the results may be biased toward better-characterized functions. [src: ecotype_functional_differentiation]
- Without within-species phylogenetic controls such as core-genome trees, the analysis cannot distinguish ecological adaptation from phylogenetic or demographic substructure. [src: ecotype_functional_differentiation]
- Effect sizes were small: the largest mean effects were 0.039 for S and 0.034 for L in the report’s rounded narrative, while the detailed table gives 0.0392 and 0.0337; these represent approximately 3–4 percentage-point differences in COG-category proportions, and statistical significance may partly reflect large sample sizes. [src: ecotype_functional_differentiation]
- Variable Spark query times of 94s–1642s during heavy cluster usage caused two species to be lost to S3 read errors. [src: ecotype_functional_differentiation]

## [[summaries/enigma_carbon_census_1__REPORT|ENIGMA Carbon Census — Tiered Knowledge Census of 83 Enrichment Compounds]]

“Organism-dark” means not linkable through the queried the KBase Data Lakehouse and curated resources, not unknown to science. Class-level catabolic literature exists for compounds including monoterpenes and nicotine, while the project’s zero literature rescues resulted from a shallow PubMed-title-only screen. A PaperBLAST or abstract-level search could reclassify part of the dark set. [src: enigma_carbon_census_1]

The dark fraction depends on the catabolic-direction filter: the 8 ENIGMA-isolate calls used a genome-prevalence-<10% signature-reaction filter retaining reactions that were catabolic according to KEGG degradation-map membership or a 3-reaction curated allowlist. A different filter could change the callable/dark boundary. Lauric acid was independently callable through measured fitness and was not subject to this filter. [src: enigma_carbon_census_1]

Soil-versus-freshwater enrichment statistics were exploratory and not calibrated. Treating each metagenome as independent in rank tests over compositional, zero-inflated relative abundances can inflate significance; all 83 genera reached q<0.05, with many q values near 1e-70. Direction and rank were considered more trustworthy than the p-values, and label-free outlier discovery was the more defensible signal. [src: enigma_carbon_census_1]

The environmental atlas is a biome-occupancy proxy, not evidence of compound degradation or activity. The H3 contrast was genuinely untestable because only 2 necromass compounds were ENIGMA-isolate-callable and both were phthalate-class aromatics. The marine arm was small and gene-blind, with 302 runs and presence/abundance data only. [src: enigma_carbon_census_1]

The callable-versus-dark physicochemical analysis was descriptive rather than calibrated inference because n=9 callable compounds were available and the Mann–Whitney p-values were uncorrected. Xanthine remains a category error in the carbon census until downstream tables are regenerated after excluding R02107. [src: enigma_carbon_census_1]

The project also identified data-pipeline requirements: NMDC and Planet Microbe inputs were species-level, so genus abundance required species-to-genus aggregation; the NMDC denominator was 3825 taxonomy-bearing covstats files rather than approximately 6700 sample-file-lookup rows; and sample-level environment labels from biosample_set provided 99% coverage across two ontologies, compared with approximately 13% from study-table GOLD labels. [src: enigma_carbon_census_1]

## [[summaries/enigma_contamination_functional_potential__REPORT|Contamination Gradient vs Functional Potential in ENIGMA Communities]]

The ENIGMA taxonomy table `ddt_brick0000454` provides labels through Genus but no species or strain labels, so direct species-level bridge testing is not possible for this dataset slice. Genus-level mapping may therefore mask strain-level adaptation. [src: enigma_contamination_functional_potential]

A total of 862 of 1,392 observed genera were unmapped to the current pangenome bridge, and the bridge includes substantial ambiguity, including 380 multi-clade genera and a maximum of 433 species clades per genus. [src: enigma_contamination_functional_potential]

COG-fraction proxies are coarse summaries rather than curated metal-resistance pathways. Exploratory sensitivity significance was concentrated in defense and depended on coverage and covariate specification; broader effects across outcomes are not established. [src: enigma_contamination_functional_potential]

Site structure was represented by coarse `location_prefix` effects rather than full hierarchical or random-effects modeling. The analysis therefore does not yet establish whether the exploratory defense associations persist under richer well- or location-level structure control. [src: enigma_contamination_functional_potential]

The document identifies five next analyses: replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries; increase taxonomic resolution using species- or strain-level ENIGMA or metagenomic data; fit models with depth, location cluster, sampling date, and compositional controls; investigate unmapped-genera contributions and bridge expansion; and add mixed-effects or hierarchical site models. [src: enigma_contamination_functional_potential]

## [[summaries/enigma_sso_asv_ecology__REPORT|SSO Subsurface Community Ecology — Spatial Structure, Functional Gradients, and Hydrogeological Drivers]]

Direct SSO geochemistry is unavailable in the analyzed dataset: 221 geochemistry sample tubes are registered in CORAL, but metals, ion chromatography/total organic carbon, isotopes, ammonia, and nitrite measurements have not been loaded. Consequently, the proposed northeast-to-southwest plume, the M5 mixing-zone interpretation, the M6 plume-core interpretation, and the inferred redox ladder are environmental hypotheses based on community composition and trait inference. [src: enigma_sso_asv_ecology]

Groundwater ASV coverage exists for only 5 of 9 wells—L7, L9, M4, M6, and U2—and excludes the critical inferred hotspot wells M5 and U3. Pump-test ASV data from Brick 460-462 for L8, M5, and U2 remains available for future extraction. The predicted groundwater pattern is that *Rhodanobacter* will be highest at M5 and lower at L8 and U2. [src: enigma_sso_asv_ecology]

Genus-level functional annotation covered only 21% of total reads, with 65 of 1,038 genera annotated; the report therefore treats process abundance estimates as lower bounds. Genus-level taxonomy covered 44% of sediment reads, species-level classification was approximately 0%, and 56% of reads remained outside the genus-level inference. Class-level traits had 78% coverage and showed consistent redox patterns, but the report recommends sensitivity analysis against the lower-coverage genus-level results. [src: enigma_sso_asv_ecology]

Trait scores at phylum and class levels are consensus estimates rather than empirical measurements of the specific SSO populations, and functional assignments are based on literature-linked taxonomy rather than direct genomic evidence. Metagenomics at the same spatial resolution is proposed to test these assignments and recover functional capacity from reads not classified at genus level. [src: enigma_sso_asv_ecology]

The sediment–groundwater comparison is confounded by the 18-month sampling offset, sediment has no within-well temporal replication, and seasonal or plume dynamics could affect the comparison. The report also notes that the single sediment timepoint cannot assess temporal dynamics, while the 9-day groundwater result cannot establish stability across seasons or longer plume fluctuations. [src: enigma_sso_asv_ecology]

The most direct resolving analyses are to load the 221 SSO geochemistry samples into CORAL; test whether nitrate, pH, and metal concentrations form the predicted northeast-to-southwest gradient; examine nearby EU/ED well metals from the 100WS/27WS bricks; extract pump-test ASVs from Brick 460-462; analyze the 18 M6-C2 isolate genomes for anaerobic metabolisms; perform weighted UniFrac using ASV sequences from Bricks 457/460/477; and repeat 16S profiling across seasons. [src: enigma_sso_asv_ecology]

## [[summaries/env_embedding_explorer__REPORT|AlphaEarth Embeddings, Geography & Environment Explorer]]

AlphaEarth coverage is only 28.4% of all genomes and is biased toward genomes with valid latitude and longitude metadata; the 38% human-associated fraction may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer]

The coordinate-quality heuristic is a crude first pass: it flags legitimate field sites such as Rifle and Saanich Inlet. Refinement should use isolation_source homogeneity at each location to distinguish genuine sampling sites from institutional addresses. [src: env_embedding_explorer]

Environment harmonization has a long tail: 17% of genomes fall into Other, and keyword matching may miss site-specific labels and non-English terms. The proposed improvements are to add clinical body-site terms such as cerebrospinal fluid, lung, and throat; add underground-laboratory terms such as Aspo and Olkiluoto; use generic water-source terms; and use env_broad_scale as a fallback when isolation_source is ambiguous. [src: env_embedding_explorer]

UMAP is a nonlinear projection whose apparent cluster structure depends on parameters including n_neighbors and min_dist and may not represent the true high-dimensional topology. DBSCAN with eps=0.5 produced 320 clusters, which may be too fine-grained; coarser clustering may better match environment categories. [src: env_embedding_explorer]

Embedding NaN values affect 4.6% of the AlphaEarth records, and their cause is unknown; missing satellite imagery at the corresponding coordinates is one possible explanation. [src: env_embedding_explorer]

The coordinate-distance relationship is strongest below 2,000 km and plateaus above 5,000 km, so it should not be interpreted as a simple raw-distance effect. The report instead relates it to environmental distance-decay and notes that environmental variation can explain community differences more strongly than geographic separation in comparable microbial-ecology studies. [src: env_embedding_explorer]

## [[summaries/essential_genome__REPORT|The Pan-Bacterial Essential Genome]]

The essential-gene definition is an upper bound: genes without transposon insertions may lack insertions because of small size, AT-rich sequence, or scaffold-edge effects rather than true essentiality. [src: essential_genome]

RB-TnSeq, or random barcode transposon sequencing, defines essentiality under specific library-construction conditions, typically rich media. Genes essential only under stress may therefore be missed. [src: essential_genome]

BBH orthology is conservative and can miss paralogs, gene fusions, and distant homologs; consequently, some apparent orphan essentials may have undetected orthologs with diverged sequences. [src: essential_genome]

Connected components can over-merge unrelated genes through transitive connections in the BBH graph, particularly for multi-domain proteins. [src: essential_genome]

The 48-organism set is taxonomically limited and biased toward culturable Proteobacteria, so essentiality patterns in uncultured lineages, Actinobacteria, or Firmicutes are underrepresented. [src: essential_genome]

Module-transfer predictions are indirect because they derive from non-essential orthologs in other organisms, and the function of an essential gene may have diverged from that of its ortholog. [src: essential_genome]

## [[summaries/essential_metabolome__REPORT|Essential Metabolome: GapMind Pathway Analysis Across Essential-Gene Organisms]]

The observed conservation supports the hypothesis that amino-acid prototrophy is common among free-living bacteria: 17 of 18 pathways were complete in all 7 organisms, and 6 of 7 organisms had all 18 pathways. However, the report explicitly concludes that the result demonstrates near-universal rather than strictly universal completeness because no pathway was universal at 100% across all 18 amino-acid pathways and DvH had a serine gap. [src: essential_metabolome]

The report does not establish that complete pathways are essential for viability. Essential-gene experiments used RB-TnSeq, or random-barcode transposon sequencing, in rich media, where nutrient supplementation can make biosynthetic genes appear non-essential. The data therefore cannot distinguish genes essential for biosynthesis from genes essential for viability. [src: essential_metabolome]

The study analyzed only 7 organisms, with limited phylogenetic diversity consisting mostly of Proteobacteria plus one Deltaproteobacterium, so its results cannot be generalized to bacteria as a whole. [src: essential_metabolome]

GapMind predictions are computational rather than experimental and use complete or likely_complete categories; non-canonical pathways, divergent enzymes below homology thresholds, and genes absent from genome annotations may be missed. In particular, DvH may possess a non-canonical or divergent serine pathway, or an unannotated pathway gene, so growth testing on serine-free minimal medium is required to validate auxotrophy. [src: essential_metabolome]

The source data included 305M GapMind predictions across 293K genomes in [[entities/kbase-ke-pangenome]], 859 universally essential gene families across 45 organisms, 80 pathway-completeness records, 18 amino-acid pathway records, 62 carbon-pathway records, 7,389 raw GapMind predictions for the selected organisms, and 8 manual organism-to-genome mappings. [src: essential_metabolome]

## [[summaries/euk_in_prok_correlates__REPORT|Metadata Correlates of Eukaryotic Contamination in NMDC Prokaryote-Targeted Metagenomes]]

The cross-study analysis included only approximately 9 studies, with one soil study accounting for approximately 43% of runs. The cross-study generalization test was therefore under-powered, and the within-study result was demonstrated for one soil study only; it may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

NMDC did not populate DNA-extraction kit, size fractionation or filtration, host-depletion method, or library-preparation fields. Processing booleans in `biosample_to_workflow_run` were near-constant, with `has_filtration` all false. The strongest literature-linked wet-lab factors therefore remain unmeasured residuals. [src: euk_in_prok_correlates]

Absolute eukaryotic fractions are classifier- and database-dependent. Because only GOTTCHA2 yielded a usable eukaryotic fraction, its values should be interpreted as relative or ordinal rather than calibrated absolute contamination. [src: euk_in_prok_correlates]

Even within the NEON soil study, `env_local_scale` and geography may track sub-batches such as sampling campaigns. The within-study analysis is the best available control, not a randomized design. [src: euk_in_prok_correlates]

Of the 2,759 runs, 1,067 were pooled from multiple biosamples. Each pooled run inherited environment and collection metadata from a single representative biosample selected by `MIN(biosample_id)`. If pooled biosamples differed in local metadata, this introduced predictor label noise; the report characterizes this as a conservative bias that can weaken associations rather than manufacture them. [src: euk_in_prok_correlates]

Sampling depth was not measured in the NEON soil study because it had zero non-null `depth` values. The depth association was therefore a cross-study statistic and was not part of the batch-controlled within-study result. [src: euk_in_prok_correlates]

The classifier databases were not interchangeable for eukaryote quantification: Kraken2 and Centrifuge were prokaryote-restricted in this NMDC deployment, whereas GOTTCHA2 was plastid- and eukaryote-aware. Cross-collection contamination-QC correlates should therefore control for study or batch using GroupKFold by study or within-study contrasts. [src: euk_in_prok_correlates]

## [[summaries/field_vs_lab_fitness__REPORT|Field vs Lab Gene Importance in *Desulfovibrio vulgaris* Hildenborough]]

The fitness analysis excludes 678 essential genes, 80.1% of which are core, because they lacked transposon mutants. Including them would raise the overall baseline slightly but would not change condition-class comparisons among non-essential genes. [src: field_vs_lab_fitness]

This is a single-organism analysis of DvH, so generalizability is limited, particularly to organisms with larger accessory genomes. The *Nitratidesulfovibrio vulgaris* pangenome contains relatively few genomes, producing a coarse core/auxiliary classification with a high 76.3% baseline core fraction that compresses effect sizes. [src: field_vs_lab_fitness]

Condition classification was manually mapped from `condition_1` labels, and edge cases such as zinc sulfate as a metal versus sulfate source required subjective judgment. The primary fitness threshold was < -2, although sensitivity analysis from -1 to -3 supported the reported pattern. [src: field_vs_lab_fitness]

Gene length is confounded with both fitness-measurement quality, because short genes receive fewer transposon insertions, and core status, because core genes tend to be longer. The field-specific and lab-specific gene sets were small (n=50-52 per group), limiting power for their comparison. Field and lab fitness effects were correlated (r ~ 0.7 from the scatter plot), so most genes that were sick in one context were also sick in the other. [src: field_vs_lab_fitness]

The ENIGMA CORAL field samples and ASVs may enable future community and geochemistry analyses, but the current database survey does not provide DvH gene-level fitness data. Proposed extensions include applying the classification to other ENIGMA organisms with environmental relevance and Fitness Browser data, replacing binary core/auxiliary status with quantitative gene-cluster prevalence, linking ENIGMA community composition to geochemistry, characterizing the genomic context and acquisition history of accessory resistance genes, and using continuous fitness scores in prediction models. [src: field_vs_lab_fitness]

## [[summaries/fitness_effects_conservation__REPORT|Fitness Effects vs Conservation — Quantitative Analysis]]

The fitness measurements are biased toward rich media and standard stresses, so many ecological niches are unrepresented. [src: fitness_effects_conservation]

The 16-percentage-point conservation gradient, although statistically robust, means that fitness importance is only a weak predictor of conservation. [src: fitness_effects_conservation]

Fitness measurements were based on single-gene knockouts and therefore did not capture epistatic interactions. [src: fitness_effects_conservation]

The Fitness Browser covered 43 bacteria, primarily Proteobacteria, limiting generalizability to other bacterial lineages. [src: fitness_effects_conservation]

Singleton and novel genes may lack fitness data because of poor transposon coverage rather than true neutrality. [src: fitness_effects_conservation]

## [[summaries/fitness_modules__REPORT|Pan-bacterial Fitness Modules via Independent Component Analysis]]

- Module-ICA had near-zero precision for predicting specific KEGG KO assignments because it captures process-level rather than gene-level function. The 6,691 predictions for hypothetical proteins should therefore be read as indicating involvement in a biological process, not possession of a specific KO-defined function. [src: fitness_modules]

- Organisms with fewer than approximately 100 experiments produced weaker modules; for example, Caulo with 198 experiments showed only 2.9x correlation enrichment. [src: fitness_modules]

- A 40% component cap, meaning components could not exceed 40% of the number of experiments, was necessary to avoid FastICA convergence failures but may cause some modules to be missed in organisms with few experiments. [src: fitness_modules]

- PFam-based annotations provided the best coverage but operate at the domain level and may overcount functional associations. [src: fitness_modules]

- The strict threshold and annotation results depend on analysis choices: the initial D'Agostino K-squared membership approach produced weakly enriched, oversized modules, while the absolute weight threshold and lower enrichment-overlap threshold produced the reported improvements. [src: fitness_modules]

- The report's cross-organism alignment used BBH ortholog pairs and ortholog groups, so the 156 module families and their consensus labels represent aligned conservation patterns rather than proof that every member has an identical molecular function. [src: fitness_modules]

## [[summaries/functional_dark_matter__REPORT|Functional Dark Matter — Experimentally Prioritized Novel Genetic Systems]]

Environmental metadata are sparse: AlphaEarth embeddings cover only 28% of genomes (83K/293K), and NCBI isolation-source metadata are inconsistent. NMDC validation is genus-level, only 5 of 6 carrier genera were matched, and common genera such as *Pseudomonas*, *Klebsiella*, and *Bacteroides* may generate broad correlations with abiotic variables independent of specific dark-gene functions. [src: functional_dark_matter]

The 57,011 dark-gene count likely overestimates true functional darkness because annotations may exist in databases or releases not checked. Module predictions, which cover 6,142 dark genes in the integrated census and are reported as 6,691 in a later project-specific accounting, are guilt-by-association inferences rather than direct experimental validation. [src: functional_dark_matter]

Fitness Browser condition coverage is uneven, and MR-1 has 121 historical conditions; organisms with deeper condition coverage can therefore produce more specific phenotypes and receive higher prioritization scores. The GapMind analysis is limited to amino-acid biosynthesis and carbon-utilization pathways, identifies organism-level co-occurrence rather than direct gene-to-step assignments, and does not address signaling, regulation, or structural functions comprehensively. [src: functional_dark_matter]

Essential genes are penalized in fitness-centric scoring because they lack viable transposon mutants, no `genefitness` rows, and no differential fitness magnitudes; the separate essential-gene prioritization partly corrects this bias but relies on neighborhood and domain inference. The neighborhood heuristic uses a five-gene window, same-strand orientation, and gaps of no more than 300 bp, whereas tools such as DOOR, STRING, and EFI-GNT use broader taxonomic and multimodal evidence. [src: functional_dark_matter]

The NMDC trait correlations are vulnerable to compositional coupling: 441/449 exploratory tests were significant despite only 7/7 pre-registered trait directions being the meaningful directional metric. A full sample-label permutation test remains future work. Likewise, the 29/47 lab–field concordance rate has a one-sided binomial p = 0.072, and equivalent annotated-accessory-gene controls were not run through the complete biogeographic pipeline. [src: functional_dark_matter]

The prioritization weights are expert-assigned and exact ranks are sensitive to them. Overall rank correlations remained ρ > 0.93 across six alternative configurations, but only 64% of the original fitness-active top 50 remained under conservation-dominant or drop-tractability settings, while essential-gene top-50 retention was 36% when tractability was dropped and 48% when neighbor context was dropped. [src: functional_dark_matter]

The Fitness Browser’s 77% Pseudomonadota composition limits cross-phylum inference. The extended covering set improves coverage from 4 to 6 phyla, but non-Fitness-Browser ortholog-group coverage is estimated at the genus level and may overestimate individual-organism coverage; these organisms also lack Fitness Browser condition profiles and therefore support broad screens rather than condition-specific experiments. [src: functional_dark_matter]

## [[summaries/fw300_metabolic_consistency__REPORT|Metabolic Consistency of Pseudomonas FW300-N2E3 Across Four KBase Data Lakehouse Databases]]

- Only 21/58 WoM metabolites (36%) could be tested against any other database, and only 3 metabolites had four-way coverage. The untested 64% may contain additional discordances. [src: fw300_metabolic_consistency]
- WoM exometabolomics was measured on R2A rich medium, whereas Fitness Browser fitness was measured on minimal medium with single carbon or nitrogen sources; condition-dependent metabolism limits direct comparison. [src: fw300_metabolic_consistency]
- BacDive aggregates *P. fluorescens* strains and, under GTDB reclassification, spans a broad clade identified as *Pseudomonas_E fluorescens_E*. Per-strain consensus was applied before species-level rates were computed, but strain-level variation means the species consensus may not represent FW300-N2E3 specifically. [src: fw300_metabolic_consistency]
- The report states in its literature-context discussion that only tryptophan, with n=52, has sufficient data for a confident conclusion, while its primary tryptophan result reports 0+/50- with n=50. This difference is retained rather than reconciled because the document gives both values. [src: fw300_metabolic_consistency]
- Manual name matching identified 28 WoM–Fitness Browser and 8 WoM–BacDive matches; two Fitness Browser matches were approximate base-to-nucleoside mappings. Additional matches may have been missed because of nomenclature differences, although excluding the two approximate matches changed mean concordance only from 0.937 to 0.930. [src: fw300_metabolic_consistency]
- Fitness Browser coverage includes pleiotropic housekeeping genes: the top 18 genes were significant across all 21 conditions because of amino acid biosynthesis requirements rather than substrate-specific catabolism. Separating housekeeping and substrate-specific signals is needed to sharpen WoM–Fitness Browser integration. [src: fw300_metabolic_consistency]
- The planned NB04 pathway-level analysis, which would map fitness-important genes to specific GapMind pathway steps, was deferred. This limits mechanistic interpretation of the tryptophan overflow hypothesis. [src: fw300_metabolic_consistency]
- BacDive compound coverage varies from 1 to 51 strains, and raw records can be higher because of duplicate entries per strain; sample size must therefore accompany consensus utilization values. [src: fw300_metabolic_consistency]

## [[summaries/gene_function_ecological_agora__REPORT|Gene Function Ecological Agora]]

The project did not identify donors at deep ranks because per-CDS sequence data were unavailable in queryable KBase Data Lakehouse schemas. M26 tree-based donor inference is exploratory and algebraically counts potential family-mate donors, which biases toward Open-Innovator classifications; composition-based confirmation and full DTL reconciliation remain future work. [src: gene_function_ecological_agora]

The PSII result is specifically a class-rank finding: the class-level sample had n = 21 PSII KOs, whereas genus, family, and order results were STABLE, and the phylum consumer statistic was unavailable because of insufficient reference data. The class-rank interpretation is consistent with PSII being a class-defining, ancient innovation, but it should not be generalized to all taxonomic ranks. [src: gene_function_ecological_agora]

The Alm 2006 quantitative correlation was not reproduced because the project’s 18,989-species substrate differs from the original 207-genome substrate, M22 measures tree-attributed gain events rather than all per-genome paralog expansion, and the definition of “recent” differs between the analyses. [src: gene_function_ecological_agora]

PUL and mycolic gene-neighborhood analyses were scale-bounded by a 723K-feature × 210K-contig join and pandas spatial-merge memory failures. The non-phage-borne conclusion for these systems therefore relies on per-cluster MGE-machinery rates and literature context, not complete cargo-neighborhood scans. [src: gene_function_ecological_agora]

Cyanobacteria BacDive coverage was only n = 4, the pangenome-openness cross-validation was null at atlas scale with Spearman r = −0.011 across 894 genera, and the targeted Mycobacteriaceae and Cyanobacteriia openness tests were underpowered with n = 10 and n = 83 genera, respectively. [src: gene_function_ecological_agora]

Cross-phase uncertainty was not propagated into a unified atlas confidence interval, bootstrap confidence intervals for individual M22 events were deferred, and Sankoff results were not comprehensively cross-validated against DTLOR or other modern reconciliation methods. Ecology results establish association or consistency with expected environments, not causal effects of environment on gene innovation. [src: gene_function_ecological_agora]

## [[summaries/genotype_to_phenotype_enigma__REPORT|Genotype × Condition to Phenotype Prediction from ENIGMA Growth Curves]]

- Condition alignment was based on normalized names and produced 42 molecular matches; the report estimates that ChEBI-ID-based canonicalization could expand this to 60–80 matches. [src: genotype_to_phenotype_enigma]

- Only 35.7% of growth curves were fit-ok. Although the 55.1% no-growth fraction is interpreted as biological, approximately 9% of curves failed fitting for technical reasons including monotone violations, short duration, and edge-well effects. [src: genotype_to_phenotype_enigma]

- Genus-level biogeography used Microbial Atlas 16S data. Species-level biogeography was available for only 20 pangenome-linked strains with verified GTDB matches. [src: genotype_to_phenotype_enigma]

- Spearman co-occurrence measures correlation rather than causation. The report recommends SparCC analysis on the full 100WS ASV matrix to strengthen the niche-partition result. [src: genotype_to_phenotype_enigma]

- Uranium, nitrate, and metal concentrations are available in CORAL bricks 10/80, but sample-to-location name resolution is incomplete, preventing a completed local test of contamination levels for the acidic Cluster B strains. [src: genotype_to_phenotype_enigma]

- GC%, codon usage bias (CUB), and Morgan molecular fingerprints were not used: GC% was available for only 32 of 727 genomes, CUB required nucleotide sequences inaccessible from JupyterHub, and Morgan fingerprints required RDKit. CUB computation from GenBank files is proposed as the next test of continuous growth-rate prediction. [src: genotype_to_phenotype_enigma]

- The Fitness Browser concordance analysis produced 1.19× enrichment after correlation-group expansion, but full validation with KEGG-module expansion remains to be done. The report also notes that the n = 7 initial analysis did not test cross-genus generalization, per-condition prediction quality, or condition-specific features. [src: genotype_to_phenotype_enigma]

- The active-learning framework is actionable but H6 is only partially supported. A formal retrospective subsampling test comparing AL-ranked additions with random selection, followed by wet-lab execution of the 50-condition proposal, remains necessary. [src: genotype_to_phenotype_enigma]

## [[summaries/harvard_forest_warming__REPORT|Harvard Forest Long-Term Warming — DNA vs RNA Functional Response]]

- The study used a single sampling date, 2017-05-24, so it cannot detect seasonal effects. [src: harvard_forest_warming]

- Omics-rich layers had limited sample sizes (n=28 metagenomes and n=39 metatranscriptomes), reducing per-KO FDR power across 12–14K KOs. [src: harvard_forest_warming]

- Metatranscriptome KO counts came from contig annotations and represent transcript-pool composition rather than TPM-quantified expression; contig-level annotation counts approximately represent relative transcript abundance but are biased by assembly quality. [src: harvard_forest_warming]

- The paired DNA/RNA comparison is affected by the horizon × incubation confound, and organic-horizon DNA lacks direct samples, preventing incubation from being factored cleanly out of that DNA analysis. [src: harvard_forest_warming]

- The single-timepoint RNA pool may include diurnal and microspatial variation from moisture pulses, root-exudate availability, and temperature conditions that are unrelated to chronic warming. The report therefore treats comparable long-term DNA and RNA response magnitude as compatible with, but not excluding, an earlier transient in which RNA could lead DNA. [src: harvard_forest_warming]

- `abiotic_features` was all zeros for these samples because of an NMDC parsing artifact, so the analysis lacked in-lakehouse soil temperature, pH, and nitrogen measurements; the +5°C treatment label was the only environmental contrast. [src: harvard_forest_warming]

- The project excluded `nmdc_arkin`, so it had no quantitative NOM, metabolomics, or proteomics layers. The ChEBI labels for the differential metabolite hits were not resolved through external ontologies. [src: harvard_forest_warming]

- The pmoA/pmoB and glyoxylate-cycle findings are directional gene-level signals, and the individual RNA signals did not survive FDR across 14K KOs. The report interprets the heated-mineral metabolite-richness decrease as consistent with faster substrate turnover, but it is not quantitative metabolomics evidence. [src: harvard_forest_warming]

## [[summaries/ibd_phage_targeting__REPORT|Metagenome-Prioritized Phage Cocktails for Crohn's Disease and IBD]]

The ecotype framework is operationally useful but not uniformly reproducible: LOSO ARI averaged 0.113, the E3 Tier-A list came from a single eligible cMD study, E0 and E2 lacked viable within-ecotype CD-versus-nonIBD contrasts, and hard ecotype assignments discretize an underlying continuum. The Kaiju-to-MetaPhlAn3 projection also showed method asymmetry: LDA was more robust, whereas GMM assigned all 26 UC Davis samples to E3 with confidence >0.97 under sparse feature overlap, an interpretation judged artifactual. [src: ibd_phage_targeting]

The project used a partial multi-method differential-abundance consensus because LinDA was implemented in pure Python and ANCOM-BC/MaAsLin2 were not completed. The NB08a species × BGC interaction test was not performed, its full-catalog comparator may inflate the OR = 44.4 estimate, and raw-read strain-resolution analyses were dropped under the no-raw-reads scope. [src: ibd_phage_targeting]

The metabolomics ecotype clustering result is specifically limited by uncorrected batch effects: pooled HMP2 and FRANZOSA m/z-bridge clustering separated cohorts, with PC1 explaining 79 % of variance and cross-cohort LOSO ARI = 0.000, below the taxonomic baseline of 0.113. The 3-modality MOFA+ plan was reduced to a 2-modality CCA pilot because HMP2 pathway abundance was unavailable in the mart, and the polyamine signature remains single-cohort because no m/z bridge was found. [src: ibd_phage_targeting]

PhageFoundry coverage applies to its 188 tested E. coli strains, not UC Davis patient isolates, and the dataset lacks explicit AIEC-versus-commensal labels, burst-size measurements, titer data, and in-vivo delivery validation. HMP2 viromics had an 80 % family-classification Unknown fraction, and endogenous phage correlations were modest with maximum absolute ρ ≤ 0.18. The three gut-anaerobe coverage gaps remain unresolved pending INPHARED and IMG/VR searches. [src: ibd_phage_targeting]

The UC Davis per-patient framework is based on only 23 patients, has no patient-specific bile-acid measurements or AIEC strain-resolution diagnostics, and uses Kaiju-derived target presence. Patient 6967 is the only biological-replicate longitudinal trajectory, so the E1→E3 drift, cocktail Jaccard = 0.60, 3–6-month reassessment interval, five-fold qPCR trigger, and state-dependent dosing rules are hypotheses rather than clinically validated rules. [src: ibd_phage_targeting]

## [[summaries/lab_field_ecology__REPORT|Lab Fitness Predicts Field Ecology at Oak Ridge]]

The report identifies several limitations: 16S amplicon sequencing resolves only to genus level; the 108 overlapping samples may not capture the full Oak Ridge geochemical range; geochemistry measurements are point-in-time observations; the aggregate metal-tolerance score is crude; multiple communities per sample, including different filter sizes and replicates, were aggregated; only 12 Fitness Browser genera had sufficient data for the metal-tolerance correlation; and pH, dissolved oxygen, carbon sources, and other confounders were not controlled. [src: lab_field_ecology]

The report proposes species- or strain-level matching using ENIGMA CORAL metagenomic genome or assembly tables, multivariate CCA or RDA analysis controlling for pH, redox, and carbon sources, temporal analysis across sampling dates, metal-specific fitness scores matched to corresponding site concentrations, and addition of *Rhodanobacter* to the Fitness Browser. [src: lab_field_ecology]

## [[summaries/lanthanide_methylotrophy_atlas__REPORT|Lanthanide Methylotrophy Atlas — Summary]]

The report addresses phylogenetic non-independence for H1 using pooled, family-equal-weight, and Bayesian GLMM analyses, all of which support H1; however, H2 still relies on within-phylum stratified analyses rather than a fully phylogeny-aware mixed model. [src: lanthanide_methylotrophy_atlas]

Marker calls vary substantially between eggNOG and Bakta, so headline statistics use a marker-specific source of truth and secondary union-of-sources analyses. Sequence-level evidence is out of scope: the study does not screen for pseudogenes, truncated ORFs, or assembly fragmentation. Genuinely novel REE-handling enzymes lacking KEGG or RefSeq homologs would also be missed. [src: lanthanide_methylotrophy_atlas]

The REE-AMD anchor contains only 37 MAGs from a single bioproject and is descriptive only; larger, independent collections from REE-mining tailings, leachate, and bioreactors are needed for inferential testing. The 897 xoxF genomes with no PQQ evidence require ORF-integrity and genome-completeness analysis, such as CheckM2, to distinguish fragmentation, pseudogenization, and community-PQQ acquisition. [src: lanthanide_methylotrophy_atlas]

AlphaEarth coverage is 1,457 / 3,690 = 39.5 % of xoxF genomes, compared with a 28 % pangenome baseline, leaving 60.5 % without environmental coordinates. Coverage-restricted PCA/UMAP analysis could test whether xoxF carriers form distinct environmental or biogeographic clusters, stratified by phylum. [src: lanthanide_methylotrophy_atlas]

The ncbi_env environmental classification is text-mining-derived and uses hierarchical regex priorities, so broad classes such as host_associated may contain misclassifications. The study also proposes characterizing f__REEB76, examining lanmodulin sequence diversity in 22 Methylobacterium extorquens genomes with 1 copy each, testing lanthanum and cerium chloride with targeted RB-TnSeq, and reporting the 505 eggNOG lanM false-positive pattern upstream. [src: lanthanide_methylotrophy_atlas]

## [[summaries/lignin_community_enrichment__REPORT|Lignin Enrichment and Ecological Memory in Microbial Communities]]

The n=3-per-group design limits statistical power, particularly for pairwise tests; n>=5 per group was proposed for future experiments. The use of 97% vsearch OTUs rather than ASVs may merge closely related organisms. The ITS analysis used NCBI ITS_RefSeq_Fungi with 19,375 reference sequences rather than UNITE, so environmental taxa may be missed and genus-level assignments are more reliable than finer assignments. [src: lignin_community_enrichment]

ITS findings are preliminary because replicate consistency was poor, within-group Bray–Curtis distances approached 1.0 for Round-2 groups, sequencing depth varied from 6,953–200,902 reads per sample before rarefaction, some samples had very low diversity, and sample LL_1 was excluded after retaining 74 reads, reducing L-L to n=2. The fungal memory effect was therefore not statistically detectable, and the notable Pleurotus emergence in LC-LC requires confirmation. [src: lignin_community_enrichment]

PERMDISP was significant for both markers, so PERMANOVA results reflect both differences in group location and differences in dispersion. No technical metadata on extraction or library-preparation batches were available, preventing formal assessment of batch effects. The reported functional interpretation of lignin degradation is based on taxonomic associations and literature context; gene-level pathway enrichment was not directly measured. [src: lignin_community_enrichment]

The planned Procrustes comparison of bacterial and fungal ordinations was not completed because near-random ITS replicate structure would make the fit difficult to interpret. Future work proposed by the document includes larger replication, DADA2 ASV analysis, UNITE-based ITS taxonomy, phylogenetic diversity and UniFrac analyses, KBase Data Lakehouse cross-referencing of Pseudomonas, Acinetobacter, and Comamonas through [[entities/kbase-ke-pangenome|kbase_ke_pangenome]], functional inference of beta-ketoadipate and protocatechuate pathways, deeper ITS sequencing, and intermediate time points to resolve restructuring kinetics. [src: lignin_community_enrichment]

## [[summaries/metabolic_capability_dependency__REPORT|Metabolic Capability vs Metabolic Dependency]]

The study states that SEED-proxy mapping can introduce false positives because related subsystem annotations may not represent direct GapMind pathway membership; direct GapMind per-step gene assignments would improve precision. The large intermediate zone (32.3%) makes the latent fraction moderately sensitive to threshold tightening, as shown by the 4.7%–21.1% sensitivity range. [src: metabolic_capability_dependency]

Fitness experiments are biased toward laboratory conditions, so pathways that are important in environments not represented by the tested media may appear latent. Pathway-level conservation cannot detect partial erosion or progressive loss of individual genes within otherwise complete pathways, and only 48 organisms were fitness-tested among 293,000 genomes with pathway predictions, limiting generalization across taxa. [src: metabolic_capability_dependency]

The conservation comparison may be affected by species-level averaging: many genomes in a species clade were not fitness-tested, potentially inflating apparent conservation of pathways classified from a limited set of organisms. The reported Black Queen signal may also be difficult to detect because gene loss can require longer evolutionary timescales than current sampling captures. [src: metabolic_capability_dependency]

The ecotype analysis is observational. Environment-cluster associations, including those in *Salmonella* and *Phenylobacterium*, may be confounded by phylogenetic structure because explicit phylogenetic correction was not performed. Marine non-associations may reflect coarse NCBI isolation-source metadata or pathway-level annotations that miss ecologically relevant gene-content and expression differences. [src: metabolic_capability_dependency]

An attempted organism-to-clade linkage using NCBI taxonomy IDs from `kbase_ke_pangenome.gtdb_metadata` returned zero matches because the relevant column contained boolean strings rather than numeric taxids. Downstream analyses therefore used organism-level fitness aggregates without an explicit clade-level linkage, which may reduce the precision of the H2a conservation comparison. [src: metabolic_capability_dependency]

## [[summaries/metal_cross_resistance__REPORT|Gene-Resolution Metal Cross-Resistance Across Diverse Bacteria]]

Metal concentrations differed among experiments, so dose-response effects could influence cross-resistance estimates. Organisms also ranged from 3 to 112 metal experiments, affecting the reliability of per-organism matrices. [src: metal_cross_resistance]

The 28 organisms are not phylogenetically independent; formal phylogenetic comparative methods such as PGLS (phylogenetic generalized least squares) or independent contrasts would strengthen the conservation claim. [src: metal_cross_resistance]

The BacDive validation is underpowered: the limitations section reports n = 26 at Fitness Browser organism scale, while the validation results report 20 independent species after matching and collapsing. The report emphasizes that this scale lacks the statistical power achieved by the Metal Fitness Atlas at pangenome scale with 42K strains. [src: metal_cross_resistance]

No negative controls were tested. Because all tested metal pairs were positive, the study cannot distinguish universal cross-resistance from a general-stress response to all metals without non-metal stress controls; the report states that the counter_ion_effects project partially addresses this issue. [src: metal_cross_resistance]

The study identifies future analytical needs including pangenome-scale validation across 27K species, phylogenetic independent contrasts, normalization by metal concentration relative to MIC, ICA (independent component analysis) of metal-condition modules, and AlphaFold-based structural analysis of metal-shared proteins. [src: metal_cross_resistance]

## [[summaries/metal_fitness_atlas__REPORT|Pan-Bacterial Metal Fitness Atlas]]

Metal coverage was uneven: cobalt and nickel were tested in 27 organisms, whereas uranium, chromium, mercury, cadmium, selenium, and manganese were tested in only one or two organisms. Consequently, cross-species patterns for rare metals largely reflect DvH and psRCH2 biology. [src: metal_fitness_atlas]

Metal concentrations were not normalized by dose or tolerance threshold; for example, nickel concentrations ranged from 0.01-2.0 mM across organisms. Fitness effects therefore cannot be compared directly without accounting for each organism's relative exposure. [src: metal_fitness_atlas]

Phylogenetic non-independence remains a limitation because multiple *Pseudomonas fluorescens* strains can inflate apparent cross-species conservation, although exclusion of four duplicate FW300 strains left the principal core-enrichment result robust. [src: metal_fitness_atlas]

The broad metal-important definition, fit < -1 OR n_sick ≥ 1, captures approximately 3.3% of genes and includes many general stress genes rather than metal-specific resistance genes. The report therefore recommends repeating the analysis with genes important for metals but not for other stresses. [src: metal_fitness_atlas]

Putatively essential genes, estimated at approximately 14.3% of protein-coding genes and approximately 82% core, lack transposon insertions and are absent from the fitness data. Because these genes are overwhelmingly core, their exclusion makes the observed core enrichment a conservative estimate. [src: metal_fitness_atlas]

The conservation analysis covered 22 of 48 organisms because only 22 had pangenome links; the report also states that 22 of 31 metal-tested organisms were covered in the primary conservation analysis. The nine excluded metal-tested organisms lacked Fitness Browser pangenome links, and 26 organisms lacked Fitness Browser pangenome mappings in the broader mapping context. [src: metal_fitness_atlas]

The repertoire prediction did not validate as a predictor of metal fitness. The report identifies regulatory or expression-based modeling, concentration-relative-to-MIC normalization, phylogenetic independent contrasts, enrichment-based pangenome scoring, and functional annotation of the 149 novel candidates using PaperBLAST, InterPro, and structural prediction as required next steps. [src: metal_fitness_atlas]

## [[summaries/metal_resistance_global_biogeography__REPORT|Global Biogeography of Environmental Bacterial Metal Resistance]]

- The report is preliminary. Data extraction and coordinate retrieval were complete at NB01, while NB02 spatial analysis and NB03 figures were initially pending; NB02 results are now reported, but production figure completion remains pending. [src: metal_resistance_global_biogeography]
- The **30.8%** per-sample coordinate gap is a substantial limitation for global mapping and creates geographic blind spots in public metagenomic archives. Which biomes are most underrepresented remains an open question. [src: metal_resistance_global_biogeography]
- The Atacama/Andean and USA hotspots may reflect single-study or expedition-level artefacts. The report requires checking distinct `sample_accession` prefixes within each hotspot. [src: metal_resistance_global_biogeography]
- Sampling-effort correction remains necessary; the report proposes testing whether hotspots persist after normalising by **log(n_MAGs)**. [src: metal_resistance_global_biogeography]
- The matplotlib import must be fixed in the NB01 map cell before the production figure is generated. [src: metal_resistance_global_biogeography]

## [[summaries/metal_specificity__REPORT|Metal-Specific vs General Stress Genes]]

The analysis had 40.7% gene attrition because locusId format mismatches excluded ANA3, Dino, Keio, MR1, Miya, PV4, and SB2B, including important model organisms such as Keio (*E. coli*), MR1 (*Shewanella*), and ANA3. The report cautions that excluded genes may have different specificity profiles and that the absent organisms are taxonomically diverse. [src: metal_specificity]

The 5% sick-rate threshold is arbitrary: results were qualitatively stable across 1–20%, but exact fractions varied. The planned validation against the Fitness Browser's built-in `specificphenotype` annotations was not performed. [src: metal_specificity]

The ICA module analysis failed to identify metal-specific modules; the proposed correction is to use precomputed z-scored module activities from Metal Atlas NB05. Further work should also resolve the locusId mismatches, replicate the counter-ion analysis using fit < -1 without the |t| > 4 requirement, and use AlphaFold predictions to examine metal-binding sites in UCP030820, YebC, and DUF1043. [src: metal_specificity]

## [[summaries/microbeatlas_metal_ecology__REPORT|Metal Resistance Ecology — Phylogenetic Conservation vs. Environmental Selection]]

MicrobeAtlas niche breadth is a sequencing-effort proxy rather than confirmed ecological range. Detection across 13 environment categories is affected by sampling intensity, primer bias, geographic and temporal non-uniformity, and missing environments; Levins' B_std corrects for unequal environment sizes but not for detection-probability differences. Genus aggregation also means that a broad genus score can reflect different species occupying different habitats rather than one organism being a generalist. [src: microbeatlas_metal_ecology]

The strict 5% prevalence analysis preserved the direction of the association but reduced the PGLS sample size by 37%, from 606 to 379, and produced p = 0.092. Primer bias, missing environments, and the ecological meaning of sparse detections remain unresolved without a multi-primer, multi-region survey design. [src: microbeatlas_metal_ecology]

The 48-genus archaeal analysis is biased toward cultured methanogens, halophiles, and thermoacidophiles and misses environmentally dominant groups including Thaumarchaeota and Woesearchaeota. The report states that ≥200 archaeal genera would be needed for improved power in the planned expansion, while its formal power analysis estimates n ≥ 702 for 80% power at α = 0.05 under the observed effect and error assumptions. [src: microbeatlas_metal_ecology]

Pangenome coverage is uneven: the correlation between sequenced genomes per genus and inferred metal type diversity was r = 0.35 with p = 2.6×10⁻¹⁹, and single-genome genera had lower metal type counts than multi-genome genera with Mann–Whitney p = 5.1×10⁻¹⁰. Coverage and rarefaction analyses substantially addressed this concern, but a formal rarefaction curve across multiple species-per-genus thresholds remains outstanding. [src: microbeatlas_metal_ecology]

Environment categories are heterogeneous, especially aquatic, which combines marine, freshwater, estuarine, hydrothermal-vent, and pond environments. Aquatic represented 40,353 OTUs, or 40.8% of the dataset; excluding it reduced β from +0.021 to +0.0085 but retained nominal significance at p = 0.031. Finer subdivision into marine, freshwater, and saline categories requires re-analysis of MicrobeAtlas metadata. [src: microbeatlas_metal_ecology]

The Gaussian PGLS treats metal type diversity, an integer count from 1–7, as a continuous z-scored predictor; the report considers this standard when the count is an independent variable but notes that residual normality should be inspected. Pagel's λ for the count trait also assumes Brownian-motion evolution, and discrete-state, threshold, Poisson, or negative-binomial phylogenetic models remain possible alternatives. [src: microbeatlas_metal_ecology]

The GTDB r214 genus-representative tree was used for all phylogenetic analyses, but sensitivity to NCBI, SILVA-based 16S, or other GTDB trees was not tested. Genus-level pruning discards within-genus phylogenetic structure, although the within-genus metal-type standard-deviation test was non-significant at p = 0.18. [src: microbeatlas_metal_ecology]

AMRFinderPlus annotations use HMM-based detection against the NCBI Bacterial AMR Reference Gene Database, and the report notes possible cross-reactive false positives, uncertainty in the “other” metal category, and the absence of manual validation. The recommended follow-up is manual BLAST verification of 100 randomly sampled annotated gene clusters. [src: microbeatlas_metal_ecology]

Track B community-weighted means cover only 16.8% of reads because the remaining approximately 83% could not be joined to genus-level GTDB AMR annotations. If uncovered genera have systematically different resistance profiles, the community-weighted means could be biased upward; correlation between per-sample covered-read fraction and community-weighted mean is required as a diagnostic. [src: microbeatlas_metal_ecology]

The study's robustness and sensitivity analyses were post-hoc exploratory analyses rather than confirmatory tests, and the analysis plan was not preregistered. The report also identifies unresolved needs for HGT-burden predictors, site-level contamination metadata, co-resistance clustering, finer environment classification, alternative phylogenetic mixed models, AMRFinderPlus validation, and a public Zenodo archive with a citable DOI. [src: microbeatlas_metal_ecology]

## [[summaries/module_conservation__REPORT|Fitness Modules × Pangenome Conservation]]

The baseline core rate is already ~81.5%, limiting the maximum observable enrichment; consequently, the +4.5 percentage-point difference to 86% is statistically significant but represents a modest absolute effect. [src: module_conservation]

The pangenome-linked analysis covers a 29/32 organism subset because Cola, Kang, and SB2B lack pangenome links; their species had too few genomes in GTDB for pangenome construction. [src: module_conservation]

Upstream ICA module membership uses |Pearson r| >= 0.3 with a maximum of 50 genes per module, so this threshold can influence which genes are classified as module members and therefore the conservation composition. [src: module_conservation]

The >90% core and <50% core cutoffs used to classify core, mixed, and accessory modules are convenient classification thresholds rather than biologically motivated boundaries. [src: module_conservation]

Essential genes are excluded from all modules because ICA requires fitness data and essential genes lack transposon insertions; therefore, the reported module conservation profiles cannot characterize essential-gene modules. [src: module_conservation]

## [[summaries/nmdc_community_metabolic_ecology__REPORT|Community Metabolic Ecology via NMDC × Pangenome Integration]]

Metabolomics technical heterogeneity could affect broader multi-study analyses, although 95% of H1 samples (125/131) came from one NMDC study, and the second study contained only 6 samples. The report recommends study-level random-effects models when broader multi-study coverage becomes available. [src: nmdc_community_metabolic_ecology]

All 33 Freshwater samples lacked paired metabolomics, so H1 was effectively a soil-only test. Whether BQH dynamics operate at the same scale in freshwater communities remains untested. [src: nmdc_community_metabolic_ecology]

Abiotic features, including pH, temperature, and total organic carbon, were absent as usable measurements: all were NaN in the 174-sample analysis matrix. Consequently, partial correlations controlling for environmental gradients could not be performed, and abiotic variables may confound H1 and H2. [src: nmdc_community_metabolic_ecology]

GapMind measures genomic potential rather than expression. The presence of pathway genes does not show that biosynthesis is active; metatranscriptomic data would be needed to test whether expressed pathway completeness correlates more strongly with metabolite pools. [src: nmdc_community_metabolic_ecology]

Metabolite-to-pathway matching used string-based compound-name matching. An isoleucine substring collision with the leucine pattern was corrected in NB04 cell-14 using first-match-wins, and the reported results use the corrected run. KEGG compound IDs had only a 2% annotation rate; cysteine, histidine, and lysine remained untestable because corresponding compounds were absent from detections. [src: nmdc_community_metabolic_ecology]

Shikimic acid and 3-dehydroshikimic acid were used as metabolomics proxies for chorismate, but they are upstream intermediates rather than chorismate itself. Their concentrations therefore reflect precursor availability rather than the chorismate pool directly, making the chorismate correlation (r = −0.038) especially uncertain. [src: nmdc_community_metabolic_ecology]

Approximately 1,352 Centrifuge taxa matched multiple GTDB clades within the same genus. One representative clade was selected by alphabetical tiebreaking on `gtdb_species_clade_id`; these genus-proxy-ambiguous taxa accounted for approximately 6.5% of mapped abundance. [src: nmdc_community_metabolic_ecology]

Sample-size imbalance limited testing of glutamine (n = 4) and proline (n = 9), despite their biological importance. Methionine also had limited power (n = 18, q = 0.117), and the report identifies larger metabolomics datasets as necessary to evaluate these pathways more reliably. [src: nmdc_community_metabolic_ecology]

The 61 Unknown-ecosystem samples may comprise mixed soil subtypes or sediment environments. Resolving their habitat identity through NMDC ENVO annotations or study metadata could improve ecosystem comparisons and reveal finer-scale metabolic niche structure. [src: nmdc_community_metabolic_ecology]

## [[summaries/nmdc_context_audit__REPORT|NMDC Context Audit]]

The provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage rather than an ingestion manifest, because no ingestion manifest is exposed in the catalog. [src: nmdc_context_audit]

Descriptions for `kbase.nmdc_*` databases are access-restricted by `ForbiddenException`, so steward-authored notes, if any, could not be captured. [src: nmdc_context_audit]

Completeness is assessed relative to snapshot timestamps and was not tested by comparison with live upstream NMDC or NCBI record counts; such comparison would require external API calls and was out of scope. [src: nmdc_context_audit]

The report does not directly observe users choosing the wrong resource. Its interpretation that label overload drives sub-optimal selection is based on gap analysis and prior-project reuse skew, so that causal claim remains inferred. [src: nmdc_context_audit]

The audit enumerates 7 real, maintained resources among 20 NMDC-named database entries, but also records aliases, test databases including `globalusers.nmdc_core_test*`, a phantom `kbase_nmdc_neon` with 0 tables, and broken user copies including `mamillerpa/my.nmdc_flattened_biosamples` with a dangling Iceberg pointer. [src: nmdc_context_audit]

## [[summaries/pangenome_openness__REPORT|Pangenome Openness Analysis]]

The sample is limited to species with both pangenome statistics and ecotype-analysis results. [src: pangenome_openness]

Pangenome openness is a single summary metric and may not represent the full complexity of pangenome structure. [src: pangenome_openness]

Environment and phylogeny effects were derived from partial correlations, which may not fully disentangle confounded variables. [src: pangenome_openness]

The upstream ecotype analysis may have limited statistical power for some species with few genomes. [src: pangenome_openness]

## [[summaries/paperblast_explorer__REPORT|PaperBLAST Data Explorer — Literature Coverage Bias in Protein Sequence Space]]

- Text mining is not equivalent to functional characterization: a gene mentioned in a paper may be tangential to the study, and the **65.6%** of genes with one paper may include incidental mentions. [src: paperblast_explorer]
- PaperBLAST mines PubMed Central full-text articles, so papers behind paywalls are missed; this creates systematic bias against fields and journals with lower open-access rates. [src: paperblast_explorer]
- Domain classification is approximate: a heuristic organism-to-domain mapping classified **35%** of organisms as Unknown, and a formal taxonomy lookup would improve accuracy. [src: paperblast_explorer]
- Clustering identity thresholds are arbitrary: the **50%** identity cutoff used for “protein family” is conventional and does not represent a universal biological boundary. [src: paperblast_explorer]
- SwissProt coverage is partial: only **19%** of SwissProt is in PaperBLAST, likely because many entries lack matching PMC full-text; curated knowledge therefore exists for proteins that PaperBLAST cannot connect to. [src: paperblast_explorer]
- The analysis has no negative controls and cannot easily distinguish genuinely unstudied genes from genes whose literature was missed by text mining. [src: paperblast_explorer]

## [[summaries/pathway_capability_dependency__REPORT|Metabolic Capability vs Dependency]]

- Fitness Browser coverage limited Tier 1 to 7 of 48 organisms with matching GapMind data, and these model organisms had near-complete core genomes that compressed the conservation-validation signal. [src: pathway_capability_dependency]
- GapMind covered 80 pathways—18 amino acid biosynthesis pathways and 62 carbon-source utilization pathways—but did not assess cofactor biosynthesis, lipid metabolism, or secondary metabolism. [src: pathway_capability_dependency]
- Laboratory fitness does not capture the full range of natural selective pressures; the report specifically notes that 28,017 genes were costly in laboratory conditions but conserved in nature. [src: pathway_capability_dependency]
- KEGG-based mapping can miss genes lacking KEGG annotations or carrying incorrect annotations, potentially underestimating the number of genes assigned to a pathway. [src: pathway_capability_dependency]
- Ecotype counts depend on hierarchical clustering with a fixed 50% maximum-distance cut; different thresholds would produce different counts, so the median of 4 should be treated as an order-of-magnitude estimate. [src: pathway_capability_dependency]
- Correlations were controlled for genome count and checked within taxonomic groups, but full phylogenetic independent contrasts were not computed. The related ecotype_analysis project found that phylogeny dominates gene content in 60.5% of species. [src: pathway_capability_dependency]
- Species with more sequenced genomes are more likely to show pathway variation and more ecotypes; partial correlations reduce but do not eliminate this sampling bias. [src: pathway_capability_dependency]
- The median-based importance threshold is circular for condition-specific reclassification, because applying a median threshold to each subset can cause pathways to cross it. An independent validation set, such as known essentials from essential_metabolome, would provide a more defensible threshold. [src: pathway_capability_dependency]
- The proposed correlation between metabolic ecotypes and AlphaEarth environmental niche breadth was not executed. AlphaEarth embeddings covered 28% of genomes, or 83K/293K, which would limit the available sample size. [src: pathway_capability_dependency]

## [[summaries/pgp_pangenome_ecology__REPORT|PGP Gene Distribution Across Environments & Pangenomes]]

Environment classification was conservative and noisy: only 1,637 species (5.9% of species with an environment label) were classified as soil/rhizosphere dominant, while 291,279 genomes had isolation-source metadata and 93.5% were classifiable. The report states that NCBI is biased toward clinical and host-associated sampling and that the acdS and pqqC enrichment effects may therefore underestimate true rhizosphere enrichment. [src: pgp_pangenome_ecology]

PGP detection relied on Bakta gene annotations matching exact gene names such as nifH, acdS, and pqqC. Product-only annotations and variant gene names could be missed, particularly for less-characterized PGP genes. [src: pgp_pangenome_ecology]

Gene-cluster annotations were not functionally validated: truncations, frameshifts, and pseudogenization were not filtered, so a cluster annotated as pqqC was not necessarily functional. [src: pgp_pangenome_ecology]

ipdC was rare, occurring in only 214 of 11,272 species (1.9%), which limited statistical power for the stratified H4 analysis; the soil reversal (OR = 0.30, p = 0.02) should therefore be treated as hypothesis-generating rather than conclusive. [src: pgp_pangenome_ecology]

GapMind tryptophan and tyrosine completeness scores may proxy for overall metabolic pathway completeness. The report states that genome size, COG coverage, or total pathway count should be controlled to separate aromatic-pathway-specific effects from general metabolic capacity. [src: pgp_pangenome_ecology]

The report also notes that co-occurrence does not establish physical linkage: whether pqqC and acdS occupy the same genomic island, operon, or separate loci remains unresolved. It proposes operonic-context analysis, deeper nifH ecological stratification, a controlled ipdC model, focused hcnA–hcnC phylogeny, and comparison with commercial inoculant strains as next steps. [src: pgp_pangenome_ecology]

## [[summaries/phage_defense_arsenal__REPORT|Pan-Bacterial Anti-Phage Defense Arsenal]]

CRISPR-Cas prevalence is inflated by permissive EggNOG description matching. The combined EggNOG-or-Pfam presence set used for syndrome analysis prioritizes recall, so CRISPR-Cas syndrome specificity may be reduced even though the significance results are not expected to be invalidated. [src: phage_defense_arsenal]

The DISARM accessory-enrichment result is unreliable because PF00176 also identifies widespread non-DISARM SNF2 helicases. A PADLOC MacSyFinder-style HMM-plus-context refinement is needed; the report states that arms-race and syndrome results involving DISARM are unaffected because they use species-level presence/absence rather than per-cluster classification. [src: phage_defense_arsenal]

Retron detection uses the broad RVT_1 Pfam PF00078. The stringent call requires at least one other narrow defense system and is therefore a defense-context filter rather than a retron-specificity filter; it reduced candidates from 15,109 to 15,098, dropping 11 species. Results should be interpreted as reverse-transcriptase candidates in defense-syndrome context, not as characterized retron systems. [src: phage_defense_arsenal]

The prophage classifier deliberately captures broad module candidates including integrase, holin, endolysin, CI-like repressor, and tail proteins, which can also match non-phage bacterial genes. Consequently, `n_prophage_modules` saturates at 7 for 35% of species; the primary arms-race predictor is instead the unbounded `n_prophage_clusters` count. [src: phage_defense_arsenal]

The ≥5-genome filter reduced the analysis set to 7,323 of 27,690 pangenome species, or 26%, biasing the analysis toward well-sampled, culturable, high-priority organisms. Extrapolation to the full 293K-genome tree, including many environmental MAGs, remains untested. [src: phage_defense_arsenal]

The arms-race analysis controls for phylum categorically but does not use a phylogenetically corrected regression. Its partial correlations and negative-binomial GLM are therefore consistent with, but do not formally establish, a phylogenetically independent arms race. [src: phage_defense_arsenal]

The negative-binomial GLM fixes dispersion at alpha = 1.0 rather than estimating it. Both focal coefficients remained significant at p < 0.001 with wide margins, but standard errors may be slightly under- or over-stated; refitting with an estimated alpha would sharpen inference. [src: phage_defense_arsenal]

## [[summaries/phb_granule_ecology__REPORT|Polyhydroxybutyrate Granule Formation Pathways — Distribution Across Clades and Environmental Selection]]

NMDC cross-validation correlations were statistically significant but small (|rho| < 0.12). NMDC abiotic measurements are point-in-time values rather than measures of temporal variability, and the studies are biased toward terrestrial and soil environments, limiting direct testing of the feast/famine hypothesis. [src: phb_granule_ecology]

PHA synthase class analysis failed because Pfam accession IDs were not mapped to eggNOG domain names; mapping PF00561 to Abhydrolase_1 for Class I/II and PF07167 to PhaC_N for Class III/IV is required to classify the 11,792 phaC clusters. [src: phb_granule_ecology]

Environment metadata are sparse: 34.9% of species have “other_unknown” as their primary environment, so environmental enrichment may be underestimated. AlphaEarth coverage is also limited: 83K/293K genomes, or 28%, have embeddings, and the 2,008 species analyzed represent 7.2% of total species diversity, potentially biasing niche-breadth analyses toward better-sampled lineages. [src: phb_granule_ecology]

Because phaA and phaB participate in general metabolism beyond PHB biosynthesis, the 46.5% precursors-only category likely overestimates partial PHB capability. The pangenome includes complete genomes and MAGs with variable genome quality and gene-detection rates. [src: phb_granule_ecology]

PHB presence is correlated with phylogeny and genome size, and the PHB–niche-breadth association falls from raw rho = 0.106 with p = 1.77e-06 to partial rho = -0.047 with p = 0.037 after controlling for genome size. Although PHB environmental enrichment persists across all four genome-size quartiles with 1.4–4.6x enrichment and all p < 1e-11, phylogenetic logistic regression or phylogenetic independent contrasts are still needed to account for shared ancestry. [src: phb_granule_ecology]

PHB has functions beyond carbon storage, including stress resistance, redox balance, and cryoprotection, so environmental variability is supported as a selective force but is not necessarily the sole driver of PHB distribution. The HGT inference is likewise based on phylogenetic discordance and core/accessory status; a directly reconstructed phaC gene tree is needed to identify incongruent branches. [src: phb_granule_ecology]

## [[summaries/pitfalls|KBase Data Lakehouse: Common Pitfalls & Gotchas]]

The document repeatedly warns that table schemas, namespace availability, access permissions, API behavior, database contents, and naming conventions can change. Queries should therefore begin with live catalog and schema discovery rather than copied historical SQL, and archived reports and notebooks should be treated as historical records rather than automatically valid executable instructions. [src: pitfalls]

Several recommendations are project-specific safeguards rather than universal thresholds. Examples include the held-out-feature Jaccard boundaries of 0.5 and 0.3, bootstrap sizes of 250–400, the ICA limit of at most 40% of the number of experiments, the `|r| >= 0.3` module-membership rule, the ANI cap of <=500 genomes, and the 50–100 genome extraction batches for large species. These values should be reported with their analysis context rather than generalized without validation. [src: pitfalls]

The document records apparent method- or interface-specific inconsistencies that require care: direct Spark accepts a quoted species ID containing `--`, whereas the REST API rejects queries containing `--`; one section describes per-organism Fitness Browser convenience tables as long format while another database-specific note says they may be pre-pivoted and have non-standard schemas; and NMDC schema notes differ on whether abiotic numeric fields arrive as strings or doubles. The stated resolution is to inspect the live schema and query interface before relying on either description. [src: pitfalls]

Coverage limitations are not equivalent to biological absence. Missing AlphaEarth coordinates, sparse NCBI environment attributes, BacDive–GTDB naming differences, unmatched species concepts, orphan pangenomes, absent tables, and workflow-specific file identifiers can all produce zero or incomplete joins without indicating that the underlying biology is absent. [src: pitfalls]

## [[summaries/plant_microbiome_ecotypes__REPORT|Plant Microbiome Ecotypes — Compartment-Specific Functional Guilds and Their Genetic Architecture]]

Plant-compartment labels were inferred primarily from NCBI isolation_source metadata, whose quality and coverage vary; only 7,995 of 293,059 genomes, or 2.7%, had plant-associated annotations, and the endophyte category contained only 29 species. BacDive identified 2,482 plant-related strains but contributed zero additional genome upgrades beyond ncbi_env. [src: plant_microbiome_ecotypes]

The marker set is literature-curated and gene presence does not establish expression or phenotype. T3SS, T6SS, flagella, chemotaxis, biofilm, quorum sensing, and secretion functions can support colonization, interbacterial competition, beneficial symbiosis, or pathogenicity, and negative controls such as Escherichia, Salmonella, and Clostridioides were frequently classified as dual-nature. RNA-seq or experimental validation is required to determine whether PGP and pathogenic marker sets are co-expressed under the same conditions. [src: plant_microbiome_ecotypes]

Genome size correlates with total marker count at r = 0.44, p < 1e-300. Among plant-associated species, the dual-nature rate was 54% in the lowest genome-size quartile versus 87% in the top three quartiles; approximately 33% of dual-nature species shifted to neutral after genome-size normalization in an earlier sensitivity analysis. The 78.7% refined dual-nature value therefore contains a real genome-size gradient and remains dependent on marker definitions and scoring assumptions. [src: plant_microbiome_ecotypes]

Phylogenetic control remains incomplete. The original genus-level fixed-effect logistic regression failed to converge for 0/14 markers; the cluster-robust GLM is a practical genus-level analogue rather than a full phylogenetic generalized linear mixed model. A full GTDB-tree covariance analysis was not feasible because a dense 25K × 25K covariance matrix would be intractable in memory. The within-genus shuffle used only 200 permutations, which is under-resolved for p ≤ 0.005, and a full permulation-style analysis remains future work. [src: plant_microbiome_ecotypes]

The raw OG enrichment was saturated at 5,341/5,671 significant tests, and the report cautions that this mostly reflects taxonomic divergence. Although 48/50 gene families survived phylum and genome-size control, two models were singular, and the earlier phylum-level models had convergence warnings. The causal direction between plant association and enriched functions therefore remains unresolved. [src: plant_microbiome_ecotypes]

The complementarity analysis was limited by 80 GapMind pathways, a potentially over-stringent core-level completeness threshold, and loss of 62/322 genera, or 19.3%, in the NMDC taxonomy bridge. The corrected effect is small, with Cohen’s d = −0.39 for prevalence weighting, but unmatched genera could include complementary partners. [src: plant_microbiome_ecotypes]

HGT evidence is indirect because GeNomad mobile-element annotations were unavailable. The transposase/integrase co-occurrence signal, lower overall marker singleton ratio, and MGnify genus-level mobilome enrichment do not provide a single genome-level estimate of horizontal transfer. MGnify BGC, mobilome, and defense data were available only for the soil biome, so those comparisons do not directly contrast rhizosphere with bulk soil. [src: plant_microbiome_ecotypes]

The MGnify and pangenome classifications have only 11.7% Jaccard overlap because they measure different phenomena: isolation metadata versus metagenomic detection. The subclade analysis is additionally limited by phylogenetic-tree coverage, with only 18/65 candidate species represented. Expanded tree coverage, accessory-gene profiling, gene-content trees, and direct mobile-element annotations are needed to resolve these uncertainties. [src: plant_microbiome_ecotypes]

## [[summaries/prophage_amr_comobilization__REPORT|Prophage-AMR Co-mobilization Atlas]]

Distances were calculated from ordinal gene positions parsed from gene_id formats rather than base-pair coordinates, so the reported gene distances may differ from true genomic distances. [src: prophage_amr_comobilization]

Prophage markers were identified by keyword and Pfam matching in bakta_annotations rather than by dedicated prophage-prediction tools such as PHASTER or geNomad. This approach may include false positives, including phage-defense systems, and may miss divergent prophages. [src: prophage_amr_comobilization]

The co-localization analysis sampled 20 genomes per species for the 100-species analysis rather than examining all 293K genomes; exhaustive analysis could strengthen the findings. [src: prophage_amr_comobilization]

Core and accessory labels depend on species-level pangenome calling with motupan, so the same gene can have different conservation status in different species. [src: prophage_amr_comobilization]

The fitness analysis was limited by the overlap between the 48 fitness-browser model organisms and GTDB pangenome species, preventing an H3 comparison. [src: prophage_amr_comobilization]

The H2 association between prophage density and AMR breadth is correlational and does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization]

## [[summaries/prophage_ecology__REPORT|Prophage Gene Modules and Terminase-Defined Lineages Across Bacterial Phylogeny and Environmental Gradients]]

The analysis identifies prophage-associated genes through eggNOG functional annotations rather than dedicated prophage tools such as geNomad or VIBRANT. Consequently, the reported near-universal prevalence may include domesticated remnants and bacterial homologs of phage genes, including bacterial integrases, and the false-positive rate is uncharacterized. [src: prophage_ecology]

Genome size was the dominant predictor of prophage burden, with rho=0.717, and residual confounding cannot be excluded despite genome-size stratification and partial correlations because larger genomes contain more genes of all types. [src: prophage_ecology]

NCBI isolation_source metadata were sparse and inconsistently labeled. The 10 environmental categories collapse substantial within-category variation, and the other_unknown category contained 9,659 species (35%), limiting statistical power. [src: prophage_ecology]

NMDC prophage-burden inference was indirect and assumed genus-level conservation of prophage content, an assumption that may fail for recently acquired or lost prophages. The approach had been validated for the PHB granule ecology project but had not been independently validated for prophage genes. [src: prophage_ecology]

Module co-occurrence was tested in only 15 species, one per phylum, providing broad phylogenetic coverage but limited within-phylum replication. Head morphogenesis was testable in only 6 species because of sparsity, and the 200-permutation null model was considered adequate but not exhaustive for estimating Z-scores. [src: prophage_ecology]

Only 28% of genomes had AlphaEarth environmental embeddings, producing a biased subsample toward clinically and environmentally well-sampled lineages. [src: prophage_ecology]

## [[summaries/pseudomonas_carbon_ecology__REPORT|Carbon Source Utilization Predicts Ecology and Lifestyle in Pseudomonas]]

The report identifies sampling bias as a limitation: *P. aeruginosa* comprised 53% of all genomes (6,760/12,732) because of clinical importance, while many environmental species had fewer than 10 sequenced genomes. This imbalance affects the power of species-level comparisons. [src: pseudomonas_carbon_ecology]

Isolation-source classification was based on free-text keywords and introduced approximately 6.7% “unknown” and approximately 29.1% “other” classifications; misclassification could attenuate the ecological signal. Species-level majority-vote assignment also obscures genuinely generalist species that inhabit multiple environments. [src: pseudomonas_carbon_ecology]

GapMind’s 62 carbon pathways cover common carbon sources but omit genus-specific capabilities, particularly aromatic degradation pathways such as toluene, naphthalene, and benzoate degradation that are central to *P. putida* ecology. The report proposes extending the analysis with aromatic-pathway modules, including KEGG modules, to test whether they provide stronger environmental signal. [src: pseudomonas_carbon_ecology]

Phylogenetic confounding is substantial: the dominant PCA signal separates subgenera rather than lifestyles, and the analyses do not explicitly control for phylogenetic non-independence among species. The report proposes phylogenetic generalized least squares (PGLS), a regression method that accounts for phylogenetic relatedness, or phylogenetic logistic regression using the GTDB species tree. [src: pseudomonas_carbon_ecology]

The report further notes that the moderate classifier accuracy may reflect small sample sizes per class, overlap between related environments such as soil and rhizosphere, and the coarse resolution of the 62 GapMind pathways. It proposes genome-level prediction using the full 789K genome-pathway matrix, within-species analysis of *P. fluorescens* and *P. putida* metabolic ecotypes, and cross-reference with RB-TnSeq fitness data from the `kescience_fitnessbrowser` collection for experimental validation. [src: pseudomonas_carbon_ecology]

## [[summaries/respiratory_chain_wiring__REPORT|Condition-Specific Respiratory Chain Wiring in ADP1]]

- NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be directly tested in the current dataset. [src: respiratory_chain_wiring]
- The stoichiometry analysis uses theoretical pathway biochemistry rather than measured flux distributions. [src: respiratory_chain_wiring]
- The cross-species comparison has only 4 organisms without NDH-2 and is insufficient for statistical significance. [src: respiratory_chain_wiring]
- The NDH-2 gene search may miss orthologs because annotation varies among Fitness Browser organisms. [src: respiratory_chain_wiring]
- ACIAD3522 may not be a true respiratory NADH dehydrogenase; its NADH-FMN oxidoreductase annotation could represent another metabolic function. [src: respiratory_chain_wiring]
- Text matching on gene descriptions likely produced false-positive NDH-2 calls, especially in organisms with incompletely annotated Complex I subunits; KO-based identification using K03885 would be more reliable. [src: respiratory_chain_wiring]
- The planned pangenome KO co-occurrence analysis was not performed, leaving NDH-2/Complex I co-occurrence across Acinetobacter species untested. [src: respiratory_chain_wiring]
- The proposed wiring model can be tested by constructing an NDH-2 deletion mutant, measuring NADH/NAD⁺ ratios on each carbon source, expanding the cross-species K03885 and K00330–K00343 analysis across 27K species, characterizing ACIAD3522, and reanalyzing quinate-versus-succinate proteomics for respiratory-chain proteins. [src: respiratory_chain_wiring]

## [[summaries/snipe_defense_system__REPORT|SNIPE Defense System in the KBase Data Lakehouse Pangenome]]

The report states that eggNOG Pfam annotations may miss divergent SNIPE homologues, and that only 54/4,572 DUF4041 clusters showed Mug113 co-annotation, suggesting that many SNIPE nuclease domains may go undetected. DUF4041 is strongly associated with SNIPE but may also occur in non-SNIPE proteins. [src: snipe_defense_system]

The AlphaEarth analysis covered 28.4% of genomes and was skewed toward environmental isolates with geographic metadata, limiting generalization to the full pangenome. The planned comparison of COG V defense-gene density could not be completed through the REST API because it required Spark Connect for a 93M × 132M row join. [src: snipe_defense_system]

NMDC metagenome ecosystem analysis was limited because only 2 samples matched the API query format; the report identifies interactive MCP-tool queries as a way to improve coverage. PhageFoundry provides genome annotations but no fitness/TnSeq tables for *Klebsiella*, so strain-specific mutant libraries or curated external *K. pneumoniae* Tn-Seq datasets would be needed to test SNIPE and ManYZ fitness directly. [src: snipe_defense_system]

The report’s H1 assessment is supported across prevalence, accessory status, environmental association, and the proposed ManYZ trade-off, while H0 is rejected for taxonomic distribution and environmental niche association. However, the environmental result establishes statistical association rather than a specific causal habitat mechanism, and the archaeal Fitness Browser example does not establish the Enterobacterales phage-lambda mechanism in archaea. [src: snipe_defense_system]

## [[summaries/soil_frontier_genomics__REPORT|Soil Microbial Dark Matter and the Clay Shield Null Result]]

The negative out-of-sample R² diagnosis is incomplete. The three model families predict worse than the training mean, but the analyses do not distinguish among train/test distributional shift caused by spatial autocorrelation within GroupKFold folds, high-leverage outlier samples dominating test-fold mean squared error, and genuine unpredictability of functional gene counts from the measured predictors at global scale. Only the third explanation would support a strong biological null interpretation; the first two would indicate modelling failure. [src: soil_frontier_genomics]

The GDI is a novel index without published precedent. Because GDI = Richness / (Mean_Completeness + 1), it can equal 902 even when there are zero genomes, because completeness = 0 makes the denominator 1. The index also conflates sampling gap and OTU richness, potentially allowing the richness term to dominate; separate reporting of richness and completeness with a two-dimensional scatterplot may be more interpretable. [src: soil_frontier_genomics]

The Forest GDI = 902.36 versus Cropland GDI = 890.82 difference is 1.3%; without bootstrap confidence intervals, the two values are not meaningfully distinguishable. The report therefore recommends describing forest and cropland as jointly the highest-GDI biomes rather than implying a ranked ordering. [src: soil_frontier_genomics]

The +0.8 pH unit discovery-bias gap requires a reverse-causality check. Alkaline soils may have fewer genomes in databases because fewer samples from those pH ranges were sequenced, rather than because alkaline microbes are harder to assemble or less studied. Controlling for the number of 16S samples in each pH bin before computing GDI would distinguish assembly or annotation gaps from sampling gaps. [src: soil_frontier_genomics]

Pending analyses are: decomposing negative R² into distributional shift, outlier leverage, and true unpredictability using spatial blocking; computing rarefaction-corrected GDI after uniform 16S sequencing-depth correction; estimating bootstrap 95% CIs for biome-level GDI rankings; controlling pH discovery bias for the number of 16S samples per pH bin; and reporting Forest versus Cropland GDI with uncertainty. These NB05 validations require re-running from the BERIL Observatory 16S tables and `kbase_ke_pangenome` completeness data because no local CSV output is available. [src: soil_frontier_genomics]

## [[summaries/soil_metal_functional_genomics__REPORT|Soil Metal Concentrations Drive Functional Gene Shifts]]

All reported associations are observational. Co-contamination is a major confound because chromium, copper, lead, and zinc co-vary in many industrial soils; it is therefore unresolved whether individual COG–metal associations are metal-specific or reflect a generic response to multi-metal contamination. Partial-correlation models are planned to address this distinction. [src: soil_metal_functional_genomics]

The reported db-RDA R² = 0.799 is conditional: project accession was removed before fitting metal predictors. If project effects explain most community COG variance, this value describes metals’ explanation of residual variance rather than total variance. The unconditional R² for metals alone was not reported and may be substantially lower; both values should be reported. [src: soil_metal_functional_genomics]

The 2,355 discoveries among 3,915 implied tests (nine metals × 435 COGs) represent a 60% discovery rate, but the report cautions that metal co-contamination makes tests non-independent. Benjamini–Hochberg FDR correction may therefore be anti-conservative under positive correlation, and the true FDR may be higher than reported. [src: soil_metal_functional_genomics]

Effect sizes have not been systematically reported across all 2,355 associations. The planned effect-size audit will examine the Spearman rho distribution and flag associations with rho < 0.05, because statistical significance may not imply substantial biological effect. [src: soil_metal_functional_genomics]

The copper-specific analysis used a 10 km proximity criterion to match soil samples with KBase genomes. Some genomes designated as nearby may not be co-located with the copper measurements, so copper–COG attribution requires sensitivity analyses at 5 km and 20 km. [src: soil_metal_functional_genomics]

The planned validation includes Moran’s I spatial-autocorrelation testing on residuals, with SEVM if spatial autocorrelation is significant; partial correlation of COG ~ Cr | Cu + Zn + Pb; mechanistic classification of significant COGs into resistance, stress, membrane, energy, and unknown categories; reporting unconditional db-RDA R²; and copper proximity sensitivity at 5 km and 20 km. [src: soil_metal_functional_genomics]

NB05 items 1–4 require rerunning analyses from the `kescience_mgnify` and `kbase_ke_pangenome` Spark tables. No local CSV containing the Spearman rho values or model residuals is available, so these validations cannot be completed without Spark access. [src: soil_metal_functional_genomics]

## [[summaries/t4ss_cazy_environmental_hgt__REPORT|T4SS–CAZy Environmental HGT]]

The observed T4SS co-localization with GT2 glycosyltransferase cassettes and phylogenetic incongruence in the GT2 gene tree provide positive evidence for 32 cross-phylum HGT events. The absence of plasmid-borne CAZy genes in the ICEfinder analysis, together with 10× higher MGE density in T4SS-positive genomes, is consistent with chromosomal or integrative mechanisms involving IMEs or integrative conjugative elements rather than plasmid mobilization. These results support the hypothesis that T4SS machinery mediates environmental dissemination of carbohydrate-active enzyme diversity across phylogenetically distant bacteria, but all associations are observational and require experimental validation for mechanistic confirmation. [src: t4ss_cazy_environmental_hgt]

The report identifies four pending validation tasks: a synteny-threshold permutation test requiring unfiltered Spark data; BLAST validation of Node_4915 against NCBI nr; a housekeeping-gene null baseline; and biome-enrichment factorization using θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)]. [src: t4ss_cazy_environmental_hgt]

## [[summaries/truly_dark_genes__REPORT|Truly Dark Genes — What Remains Unknown After Modern Annotation?]]

The pangenome linkage gap prevents assessment of 17,479 dark genes (31%); the report estimates that approximately 2,841 of them may be truly dark, describing this as a 31% coverage gap in the prioritized list. [src: truly_dark_genes]

Bakta may produce false-negative functional calls: some genes labeled hypothetical may have known functions that did not match the Bakta PSC database at the tested version, v6.0. [src: truly_dark_genes]

BBH ortholog coverage includes only 32 of 48 Fitness Browser organisms, so truly dark genes from the remaining 16 organisms lack concordance and ortholog-breadth data. [src: truly_dark_genes]

GC deviation is an imperfect HGT indicator because gene-specific composition biases, including those associated with membrane proteins, and amelioration over time can also produce deviation. [src: truly_dark_genes]

Short genes are inherently harder to annotate because they contain fewer domains and have fewer homologs, and they are harder to measure for fitness because they provide fewer transposon-insertion sites. Consequently, the length difference of d = −0.432 may partially explain other observed differences. [src: truly_dark_genes]

Some strong fitness phenotypes may result from polar effects on downstream genes rather than from the truly dark gene itself. [src: truly_dark_genes]

The proposed biological interpretation is therefore strongest for the directly measured differences and weaker for causal explanations: accessory-genome enrichment, GC deviation, mobile-element proximity, and narrow taxonomic breadth support recent acquisition and rapid evolution, but do not by themselves establish HGT or gene function. [src: truly_dark_genes]

## [[summaries/webofmicrobes_explorer__REPORT|Web of Microbes Data Explorer]]

The report identifies the lack of consumption data as the fundamental limitation: this snapshot records what organisms produce but not what they consume, preventing tests of whether consumed metabolites predict gene essentiality. The dataset is also small, comprising 37 organisms (20 experimental organisms), and comes from a single laboratory. [src: webofmicrobes_explorer]

The snapshot is frozen in 2018 and was accessed through the Wayback Machine, so it may not represent the current WoM state. The GNPS2-hosted version or Northen laboratory datasets, including the Northen Lab Defined Medium study of 110 soil bacteria, may provide a larger and richer resource with consumption data. [src: webofmicrobes_explorer]

GapMind pathway matching failed because pathway names did not contain simple metabolite names; a dedicated pathway-to-metabolite mapping table is needed. WoM coverage of *E. coli* BW25113 is especially limited despite the richness of its Keio Fitness Browser data, with only 12 WoM observations focused on sulfur and cysteine. [src: webofmicrobes_explorer]

The report proposes obtaining the current WoM dataset from GNPS2 or the Northen laboratory; building a GapMind pathway-to-metabolite lookup table; testing gene fitness against metabolites produced by `pseudo3_N2E3` and `pseudo13_GW456_L13`; testing whether higher `E/(E+I)` ratios associate with more open pangenomes or accessory genes; and re-ingesting WoM when consumption data become available. [src: webofmicrobes_explorer]

