# Negative Results and Caveats

What each project reports as limitations, null results, or abandoned
analyses — read before repeating an analysis.

## [[summaries/acinetobacter_adp1_explorer__REPORT|Acinetobacter baylyi ADP1 Data Explorer]]

- No gene has all six modalities, and FBA covers only 866 genes. [src: acinetobacter_adp1_explorer]
- The cluster mapping is indirect and may have split or merge edge cases. [src: acinetobacter_adp1_explorer]
- Predictions depend heavily on gapfilling. [src: acinetobacter_adp1_explorer]
- The database covers only A. baylyi. Cross-species work would need similar databases for other organisms. [src: acinetobacter_adp1_explorer]
- The PhageFoundry Acinetobacter genome browser was not deeply queried. [src: acinetobacter_adp1_explorer]

The report proposes these next analyses:

- Test whether the 227 FBA-TnSeq discordant genes are enriched for specific pathways or regulatory functions, to guide model refinement. [src: acinetobacter_adp1_explorer]
- Use the cluster ID mapping to compare ADP1 mutant growth with Fitness Browser data for related organisms, even though ADP1 is not in that dataset. [src: acinetobacter_adp1_explorer]
- Cross-reference the PhageFoundry Acinetobacter genome browser with phage susceptibility data. [src: acinetobacter_adp1_explorer]
- Identify urea-specific genes and examine their pangenome conservation. [src: acinetobacter_adp1_explorer]
- Assess gapfill confidence using pangenome conservation, given 243 missing functions and 87% of predictions depending on gapfilling, to improve prediction reliability. [src: acinetobacter_adp1_explorer]

## [[summaries/adp1_deletion_phenotypes__REPORT|ADP1 Deletion Collection Phenotype Analysis]]

- The clustering null result limits any claim of functional modules; the only discrete module is the 24-gene quinate group. [src: adp1_deletion_phenotypes]
- The ADP1 versus *E. coli* difference may reflect method, since this study used single-gene deletions and Nichols et al. used chemical perturbations. [src: adp1_deletion_phenotypes]
- 272 dispensable genes have no growth data, and the missing genes are biased toward short, less annotated, less conserved genes. [src: adp1_deletion_phenotypes]
- Growth ratios are single-timepoint measurements with unknown technical noise, and the specificity analysis assumes variation across conditions is biological, not measurement error. [src: adp1_deletion_phenotypes]
- The complete matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing it toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]
- Only 8 carbon sources were tested, so the ~5 independent dimensions may increase with more conditions. [src: adp1_deletion_phenotypes]
- Pangenome core/accessory status comes from the species-level *A. baylyi* pangenome, which may have limited resolution compared with a population-level analysis. [src: adp1_deletion_phenotypes]
- Proposed next analyses: apply independent component analysis (ICA) instead of hierarchical clustering, since ICA may find latent factors that hierarchical clustering misses. [src: adp1_deletion_phenotypes]
- Compare ADP1 specificity profiles with Fitness Browser RB-TnSeq data for organisms grown on overlapping carbon sources such as glucose and lactate, to ask whether the same pathways are condition-specific across species. [src: adp1_deletion_phenotypes]
- Use the condition-specific gene sets to infer regulatory relationships, since genes co-specific for a condition may share transcriptional regulators. [src: adp1_deletion_phenotypes]
- Expand the condition panel with more carbon sources, nitrogen sources or stress conditions. [src: adp1_deletion_phenotypes]

## [[summaries/adp1_triple_essentiality__REPORT|Triple Essentiality Concordance Analysis for *Acinetobacter baylyi* ADP1]]

- The Q25 threshold flags about 25% of genes per condition, so aggregating "any defect" over 8 conditions gives a high background rate by design. The expected rate is 1 − 0.75⁸ = 90% if conditions were independent, against 72% observed. [src: adp1_triple_essentiality]
- The glucarate result runs opposite to prediction, so the weak flux–growth trends are not uniform across conditions. [src: adp1_triple_essentiality]
- The report states that FBA essentiality predictions require experimental validation. [src: adp1_triple_essentiality]
- The report calls knockouts the best proxy for lethality, but notes that fitness, expression and growth rates reveal additional biology. [src: adp1_triple_essentiality]
- Aromatic enrichment (OR = 9.7) and the 70% figure come from the original study. [src: adp1_triple_essentiality]

## [[summaries/alphafold_msa_annotation__REPORT|AlphaFold MSA Depth as a Lens on the Bacterial Annotation Gap]]

- The 29.3% UniProt coverage is not random. Well-characterised organisms such as E. coli, Pseudomonas and Bacillus are over-represented, so the analysis is biased toward better-studied diversity. [src: alphafold_msa_annotation] Only gene clusters with a non-UPI UniProt accession are included. [src: alphafold_msa_annotation]
- The 71% of clusters without AlphaFold entries skew toward poorly characterised organisms and likely harbour a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation] The report suggests the gap for the remaining 70.7% is likely larger. [src: alphafold_msa_annotation]
- MSA depth is looked up for the cluster representative only, so within-cluster diversity is ignored and the representative may be higher or lower than the typical member. [src: alphafold_msa_annotation]
- The 293K genomes are phylogenetically imbalanced, with Pseudomonas and E. coli over-represented. This influences core gene counts and MSA depth distributions. [src: alphafold_msa_annotation]
- The AlphaFold database in the KBase Data Lakehouse is a single version-6 snapshot, and newly deposited UniProt entries may change MSA depths as databases grow. [src: alphafold_msa_annotation]
- The report's attribution of the accessory hypothetical excess to horizontal transfer, rapid evolution and narrow taxonomic distribution is tentative ("likely"). [src: alphafold_msa_annotation]
- The report calls the paradox proteins prime candidates for experimental structural characterisation. [src: alphafold_msa_annotation]

Next analyses the report proposes:
- Run the MSA-depth–domain-richness test (H3) separately for core, auxiliary and singleton clusters, to see whether the gradient is steeper in one class. [src: alphafold_msa_annotation]
- Compare ESM pLDDT with AlphaFold MSA depth for the same clusters. ESMFold does not use MSA depth, so it gives an orthogonal structural novelty signal. [src: alphafold_msa_annotation] The comparison would find proteins novel in sequence space but potentially foldable without homologs. [src: alphafold_msa_annotation]
- Map the 415K paradox clusters onto the GTDB phylogeny to find the phyla and families with the highest densities of conserved-yet-novel proteins. [src: alphafold_msa_annotation]
- Join the paradox list to kescience_fitnessbrowser fitness scores, where available, to find proteins essential for growth in at least one condition. That would be experimental evidence of function without annotation. [src: alphafold_msa_annotation]

## [[summaries/amr_cofitness_networks__REPORT|AMR Co-Fitness Support Networks]]

- The enrichment may reflect shared dispensability rather than genuine co-regulation. [src: amr_cofitness_networks]
- The permutation test matched random genes by conservation class but not by mean fitness level. [src: amr_cofitness_networks] The report suggests flagellar enrichment might disappear entirely if random genes were matched to the slightly-positive fitness distribution of AMR genes. [src: amr_cofitness_networks]
- A fitness-matched permutation, drawing random genes with the same slightly-positive fitness distribution, is needed to tell the two apart. [src: amr_cofitness_networks]
- The report names this permutation, with mean fitness from −0.05 to +0.05, as the key unresolved test. [src: amr_cofitness_networks]
- The report calls the most important follow-up a permutation test drawing random non-AMR genes matched on mean fitness level, not just conservation class. If random genes with fitness between −0.05 and +0.05 also show flagellar/biosynthesis enrichment in their cofitness neighborhoods, the enrichment is a shared-dispensability artifact. [src: amr_cofitness_networks]
- If AMR genes uniquely enrich even among fitness-matched genes, the report says the co-regulation interpretation is supported. [src: amr_cofitness_networks]
- High cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation, even without the dispensability confound. [src: amr_cofitness_networks]
- Mechanism-specific results are weak after multiple-testing correction. [src: amr_cofitness_networks]
- Cofitness treats missing fitness values as zero in z-score space (np.nan_to_num), which approximates but does not equal pairwise-complete Pearson correlation. [src: amr_cofitness_networks] The report considers this unlikely to affect conclusions because FB matrices are relatively dense. [src: amr_cofitness_networks]
- Broad GO terms (transmembrane transport, membrane) appear in nearly all networks and genomes, potentially masking specific signals. [src: amr_cofitness_networks]
- At |r| > 0.3 the mean network size is 233 genes, including many weak associations; confirmation at |r| > 0.4 is needed. [src: amr_cofitness_networks]
- The 28 organisms are lab-adapted, phylogenetically biased (many Pseudomonas) and ecologically limited. [src: amr_cofitness_networks]
- The 5-ORF exclusion zone uses matrix row index as a proxy for genomic proximity, which may not reflect chromosomal gene order. [src: amr_cofitness_networks] The begin, end and strand columns are loaded and could support coordinate-based exclusion. [src: amr_cofitness_networks]
- The report proposes computing cofitness separately for antibiotic conditions and standard growth. Elevated AMR–flagella cofitness specifically under antibiotic stress would support a regulatory connection. [src: amr_cofitness_networks]
- The report proposes checking flagellar knockout mean fitness across FB experiments. Positive fitness would confirm shared dispensability as plausible, while near-zero or negative fitness would strengthen co-regulation. [src: amr_cofitness_networks]
- The report proposes Pfam domain-level enrichment, which may reveal more specific support-network functions than broad GO terms. [src: amr_cofitness_networks]
- The report proposes testing phage defense, secondary metabolite and other condition-specific gene classes for the same cofitness patterns. If they show them, the signal is general to laboratory-dispensable genes, not AMR-specific. [src: amr_cofitness_networks]

## [[summaries/amr_environmental_resistome__REPORT|Environmental Resistome at Pangenome Scale]]

- The AlphaEarth analysis confirms the discrete findings but adds limited interpretability, because the embedding dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
- The clinical-exposure result is a species-level proxy; a true per-genome within-species comparison was not done. The planned per-genome Fisher's exact test was replaced because billion-row joins were too costly. [src: amr_environmental_resistome]
- PCoA (principal coordinates analysis) ordination, PERMANOVA (permutational multivariate analysis of variance), environment-specific gene identification, MAG (metagenome assembled genomes) or isolate assessment, and archaea-specific analysis were planned in RESEARCH_PLAN v2 but not executed. [src: amr_environmental_resistome]
- The continuous clinical-fraction vs % accessory correlation is borderline. [src: amr_environmental_resistome]
- 18.7% of AMR clusters have no mechanism and are excluded from the mechanism fractions. [src: amr_environmental_resistome]
- The narrative efflux (15-21%) and target-modification (19-29%) ranges for clinical and gut bacteria do not match the report's table values. [src: amr_environmental_resistome]
- Only 20 of 141 testable families (14%) show significant within-family effects. [src: amr_environmental_resistome]
- Environment and phylogeny remain deeply entangled despite family-level control, and some families, including many Enterobacteriaceae, are almost entirely clinical. [src: amr_environmental_resistome]
- All tests are highly significant, but effects are modest (η² = 0.02–0.13), so environment explains 2-13% of variance, and phylogeny likely explains much more. [src: amr_environmental_resistome]
- NCBI overrepresents clinical isolates and undersamples soil and aquatic species. The "clinical species carry more AMR" finding partly reflects that clinical species are sequenced because they have AMR. [src: amr_environmental_resistome]
- Majority-vote classification collapses within-species variation; a "clinical" species may include environmental strains. A sensitivity analysis at 60-90% thresholds mitigates this. [src: amr_environmental_resistome]
- AMRFinderPlus focuses on known resistance genes and may underestimate novel resistance in environmental bacteria, biasing results toward more AMR in clinical species. [src: amr_environmental_resistome]
- The 95% prevalence threshold for core depends on genome count, so core/accessory labels are imprecise for species with few genomes. [src: amr_environmental_resistome]
- The report observes correlation, not causation. Clinical species may carry more AMR because of antibiotic exposure, or may be clinical because of virulence-resistance co-selection. [src: amr_environmental_resistome]

### Proposed next analyses

- Identify AMR gene clusters present in both soil and clinical species as candidates for recent cross-niche HGT (cf. Forsberg et al. 2012). [src: amr_environmental_resistome]
- For species sampled across decades (for example S. aureus and K. pneumoniae), test whether the accessory AMR fraction has increased over time. [src: amr_environmental_resistome]
- Combine the environment-AMR profiles with amr_fitness_cost to test whether clinically enriched AMR genes are costlier (recently acquired) or cheaper (under strong selection). [src: amr_environmental_resistome]
- Use nmdc_arkin metagenome taxonomic profiles to infer community AMR load from species AMR profiles, validating species-level findings in environmental communities. [src: amr_environmental_resistome]
- Once genomad_mobile_elements is available in the KBase Data Lakehouse, test whether accessory AMR clusters in clinical species associate preferentially with plasmids, transposons or integrative elements. [src: amr_environmental_resistome]

## [[summaries/amr_fitness_cost__REPORT|Fitness Cost of Antimicrobial Resistance Genes]]

- The class-matched flip validation did not reach significance, probably because of small per-class samples and organism heterogeneity. [src: amr_fitness_cost] Only 4 AMR classes (beta-lactam, aminoglycoside, chloramphenicol, tetracycline) have matched antibiotic experiments, and macrolide, glycopeptide and polymyxin classes could not be validated. [src: amr_fitness_cost]
- The core/accessory null depends on imprecise core calls from few genomes per species (median 9), so it should be read cautiously for species with <20 genomes. [src: amr_fitness_cost]
- The organisms are lab-adapted, so costs may already be compensated. [src: amr_fitness_cost] All 25 are lab-adapted, so compensatory evolution during maintenance may mean natural-population costs are underestimated. [src: amr_fitness_cost]
- 86% of AMR genes are Tier 2 keyword matches from bakta annotations that may include non-AMR genes such as general efflux transporters. The Tier 1 sensitivity analysis gives consistent results, which mitigates this. [src: amr_fitness_cost]
- The Tier 2 classifier omits fosfomycin and tellurite resistance annotations, leaving ~25 genes in the "unknown" mechanism group. They could be reclassified as enzymatic_inactivation and metal_resistance respectively. [src: amr_fitness_cost]
- Transposon insertions can cause polar effects on downstream genes, which may confound fitness for AMR genes in operons. [src: amr_fitness_cost]
- Comparisons with isogenic-competition literature are reassuring but not direct equivalences. [src: amr_fitness_cost]
- The explanations (cost floor, donor optimization, compensatory evolution) are proposals, not measurements. [src: amr_fitness_cost]

### Next analyses the report proposes

- Test whether mechanism predicts cost within a single genetic background in organisms with many AMR genes (Cup4G11: 77, BFirm: 50), controlling for phylogenetic differences. [src: amr_fitness_cost]
- Distinguish narrow-spectrum drug pumps from general RND systems such as AcrAB-TolC, and test whether constitutively expressed efflux systems have lower costs. [src: amr_fitness_cost]
- Instead of averaging across all non-antibiotic experiments, test whether AMR costs vary under metal, osmotic and carbon-limitation stresses. [src: amr_fitness_cost]
- Cross-reference the 144 metal resistance genes with fitness data against the `metal_fitness_atlas` project, to test whether genes costly under standard conditions are protective under metal stress. [src: amr_fitness_cost]
- Scale the analysis from 25 FB organisms to all 293K KBase Data Lakehouse genomes by predicting AMR cost from gene-cluster conservation patterns. [src: amr_fitness_cost]

## [[summaries/amr_pangenome_atlas__REPORT|Pan-Bacterial AMR Gene Landscape]]

- Of the 14,723 AMR-carrying species, 7,838 (53.2%) received a non-Other/Unknown environment classification. The Kruskal-Wallis test used only these species, across 6 categories. [src: amr_pangenome_atlas]
- The Other/Unknown bin holds 46.8% of species. This reflects sparse and inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- Genome databases over-represent clinical pathogens, inflating AMR counts for human-associated species. [src: amr_pangenome_atlas]
- The 83K AMRFinderPlus hits are not all antibiotic resistance, because the scope includes mercury and arsenic stress-response genes. [src: amr_pangenome_atlas]
- Only 28% of genomes have AlphaEarth embeddings, biased toward genomes with geographic metadata. [src: amr_pangenome_atlas]
- The 100% identity threshold avoids paralog confusion but may undercount fitness effects of closely related variants, such as alleles differing by a single synonymous substitution. [src: amr_pangenome_atlas]
- FB organisms are predominantly environmental isolates with intrinsic resistance. The fitness cost of recently acquired mobile resistance in clinical pathogens may differ substantially. [src: amr_pangenome_atlas] Only 37/48 FB organisms had AMR genes, so the fitness analysis does not capture those costs. [src: amr_pangenome_atlas]
- Mechanism classification uses keywords, not the CARD Antibiotic Resistance Ontology (ARO). The 22.2% Other/Unclassified category includes products matching no keyword set, such as ribosomal protection proteins with non-standard names and novel mechanisms. [src: amr_pangenome_atlas]
- Some singleton AMR clusters may be annotation artifacts rather than true species-specific resistance genes. [src: amr_pangenome_atlas]
- No Bonferroni or false discovery rate (FDR) correction was applied across the tests of the six hypotheses. The report argues the primary p-values are extreme (many < 1e-100) and correction would not change conclusions. [src: amr_pangenome_atlas] Per-gene and per-phylum tests are exploratory and hypothesis-generating. [src: amr_pangenome_atlas]
- Proposed next step: map bakta_db_xrefs cross-references to CARD ARO terms, for a systematic ontology-based classification that would reduce the unclassified fraction. [src: amr_pangenome_atlas]
- Proposed next step: replace keyword-based mechanism classification with systematic CARD ARO mapping to reduce the 22% "Other/Unclassified" category. [src: amr_pangenome_atlas]
- Proposed next step: map AMR gene prevalence in NMDC/MGnify environmental metagenomes to test whether accessory AMR genes seen in isolates are also prevalent in community DNA. [src: amr_pangenome_atlas]
- Proposed next step: use phylogenetic tree distances to estimate AMR gene gain/loss rates and ask whether acquired genes are gained faster than lost. [src: amr_pangenome_atlas]
- Proposed next step: a co-localization analysis to test whether AMR genes cluster in genomic islands or co-localize with mobile element markers such as IS elements and integrons. [src: amr_pangenome_atlas]
- Proposed next step: cross-reference AMR proteins with AlphaFold/PDB structures to identify novel resistance folds. [src: amr_pangenome_atlas]

## [[summaries/amr_strain_variation__REPORT|Within-Species AMR Strain Variation]]

- Environment-ecotype association testing is limited by metadata sparsity. [src: amr_strain_variation]
- The temporal null likely reflects poor collection-date metadata. [src: amr_strain_variation]
- E. coli is absent from the ecotype case studies. [src: amr_strain_variation] ANI extraction was limited to species with <=500 genomes, which also excluded E. coli (15,388 genomes) and K. pneumoniae (14,240 genomes) from the phylogenetic signal analysis. [src: amr_strain_variation]
- The BacDive-approximating classifier covers only 35% of species, against 91% for the NCBI classifier. [src: amr_strain_variation] Both classifiers are approximate, and dedicated metadata curation would improve ecotype analyses. [src: amr_strain_variation]
- The genome collection is heavily biased toward clinical and human-associated isolates, particularly K. pneumoniae, S. aureus and E. coli. Environmental species are underrepresented. [src: amr_strain_variation]
- AMR identification relies on the AMRFinderPlus database and misses novel mechanisms absent from it. [src: amr_strain_variation]
- Next steps proposed by the report:
  - Make UMAP and heatmap case studies with clinical metadata overlays for K. pneumoniae, E. coli, S. aureus, P. aeruginosa, S. enterica and A. baumannii. [src: amr_strain_variation]
  - Develop subsampling strategies for Mantel tests in species with >500 genomes. [src: amr_strain_variation]
  - Obtain curated collection dates through NCBI metadata curation. [src: amr_strain_variation]
  - Map islands to mobile element context: plasmid versus chromosome, integron boundaries and IS elements. [src: amr_strain_variation]
  - Use island co-occurrence structure to predict future co-acquisition, in a PanKA-style approach. [src: amr_strain_variation]
  - Link AMR ecotypes to virulence factor profiles and metabolic pathway variation from other KBase Data Lakehouse analyses. [src: amr_strain_variation]

## [[summaries/annotation_gap_discovery__REPORT|Annotation-Gap Discovery via Phenotype-Fitness-Pangenome-Gapfilling Integration]]

- Validation inserted 23 gene-protein-reaction rules into SBML models for high/medium-confidence EC-matching candidates. [src: annotation_gap_discovery] Gene knockout simulation then showed zero wildtype growth on minimal carbon source media. [src: annotation_gap_discovery] The report calls this an expected limitation, because the models need the gapfilled reactions themselves for growth on those carbon sources. [src: annotation_gap_discovery] The knockout validation was inconclusive, because single-gene knockout analysis is circular in this context. [src: annotation_gap_discovery]
- Draft models from automated RAST annotations contain systematic errors. The 42.5% baseline FBA accuracy is dominated by false positives from overly permissive growth predictions. [src: annotation_gap_discovery]
- Multiple valid gapfill solutions may exist for each false-negative case. The default ModelSEED gapfilling minimizes added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery]
- The report manually mapped 109 Fitness Browser carbon source condition names to ModelSEED compound IDs (identifiers). Mapping errors would produce spurious false negatives. [src: annotation_gap_discovery]
- Gene fitness significance depends on the |fitness| threshold and experiment count. Organisms with fewer carbon source experiments have less statistical power. [src: annotation_gap_discovery]
- GapMind covers ~80 carbon and amino acid pathways rather than full metabolism, so many gapfilled reactions fall outside its coverage. [src: annotation_gap_discovery]
- Twelve of 14 organisms are Proteobacteria, which limits generalizability. [src: annotation_gap_discovery]
- Dark reactions were resolved far less often, so the hardest gaps remain largely open. [src: annotation_gap_discovery]
- Exact GapMind concordance could not be assessed at step level. [src: annotation_gap_discovery]
- 105 pairs (52.2%) remain unresolved. [src: annotation_gap_discovery]

The report proposes these next steps:
- Test the 44 high-confidence gene-reaction assignments by targeted gene knockouts, such as CRISPR interference (CRISPRi), on specific carbon sources. [src: annotation_gap_discovery]
- Extend the pipeline to all 48 Fitness Browser organisms. This would increase statistical power for pangenome co-occurrence analysis and may resolve more gaps through phylogenetic proximity. [src: annotation_gap_discovery]
- Use gapseq instead of RAST/ModelSEED for initial reconstruction. This could reduce false-positive FBA predictions and yield more targeted gapfill cases. [src: annotation_gap_discovery]
- Target the 50 EC-less gapfilled reactions with computational enzyme prediction tools (e.g., DeepEC, CLEAN) and experimental biochemistry. [src: annotation_gap_discovery]
- Extend the approach to microbial communities to identify cross-feeding interactions mediated by annotation-gap reactions. [src: annotation_gap_discovery]
- Apply ICA-based approaches (Borchert et al. 2024) to the fitness data to find functional gene modules that resolve gaps missed by per-gene analysis. [src: annotation_gap_discovery]

## [[summaries/aromatic_catabolism_network__REPORT|Aromatic Catabolism Support Network in ADP1]]

- Those 8 conditions provide only ~5 independent dimensions. [src: aromatic_catabolism_network] More conditions would sharpen subsystem boundaries. [src: aromatic_catabolism_network]
- Ortholog-transferred fitness mixes organisms with different respiratory-chain architectures. Direct Complex I measurements on aromatic substrates in a single organism would be more definitive. [src: aromatic_catabolism_network]
- The Complex I co-fitness assignments beyond the nuo operon may be indirect. [src: aromatic_catabolism_network] The report proposes protein-protein interaction studies or Complex I co-purification to tell physical accessory factors from indirect regulatory connections. [src: aromatic_catabolism_network]
- The report proposes searching the ADP1 genome for NDH-2 genes. If present, their deletion phenotypes on quinate versus glucose would directly test whether NDH-2 compensates for Complex I on non-aromatic substrates. [src: aromatic_catabolism_network]
- The report proposes adding benzoate, catechol and vanillate, plus iron limitation and respiratory inhibitors. These would refine subsystem boundaries and test the NADH-flux hypothesis directly. [src: aromatic_catabolism_network]
- The report proposes using eggnog_mapper_annotations in the KBase Data Lakehouse to test whether Acinetobacter species carrying the pca pathway more often retain Complex I (KOs K00330–K00343) than species lacking aromatic degradation. [src: aromatic_catabolism_network]

## [[summaries/bacdive_metal_validation__REPORT|BacDive Isolation Environment × Metal Tolerance Prediction]]

- The heavy metal group is small. With n=10 versus ~5,000 baseline isolates, the minimum detectable effect at 80% power is approximately d=0.93. [src: bacdive_metal_validation] The observed d=1.00 barely exceeds it. [src: bacdive_metal_validation] The group sits at the detection limit, so its effect size is imprecise. [src: bacdive_metal_validation] A larger heavy metal dataset is needed to estimate it precisely. [src: bacdive_metal_validation]
- RESEARCH_PLAN.md referenced n=31 heavy metal isolates, but only 10 matched pangenome species with scores after the bridge. [src: bacdive_metal_validation]
- Species-level matching is lossy. It failed for 56.6% of strains, primarily because GTDB uses different species boundaries than LPSN/DSMZ. [src: bacdive_metal_validation] Genome accession-based matching (GCA to pangenome genome_id) would improve coverage but requires a Spark query. [src: bacdive_metal_validation]
- BacDive holds culturable, described strains rather than full environmental diversity. Metal-tolerant extremophiles may be under-represented. [src: bacdive_metal_validation]
- The current metabolite_utilization table may miss metal tolerance tests available through the BacDive API (application programming interface), such as MIC data and growth inhibition. [src: bacdive_metal_validation]

Next analyses proposed by the report:
- GCA accession-based matching: query kbase_ke_pangenome.genome to match BacDive GCA accessions directly to pangenome genome_ids, potentially recovering more of the 56.6% unmatched strains. [src: bacdive_metal_validation]
- ENIGMA CORAL integration: cross-reference ENIGMA community data at the Oak Ridge metal-contaminated site for complementary field validation. [src: bacdive_metal_validation]
- Per-metal environment analysis: for metals with sufficient BacDive representation (iron, manganese), test whether specific metal tolerance gene families predict specific contamination environments. [src: bacdive_metal_validation]
- Expanding BacDive metal phenotypes beyond the current table. [src: bacdive_metal_validation]

## [[summaries/bacdive_phenotype_metal_tolerance__REPORT|BacDive Phenotype Signatures of Metal Tolerance]]

- The Gram-stain effect cannot be tested within classes. [src: bacdive_phenotype_metal_tolerance]
- The urease effect vanishes within Gammaproteobacteria and Bacilli, which the report takes as further evidence of phylogenetic confounding. [src: bacdive_phenotype_metal_tolerance]
- The H₂S estimate rests on 8 negatives and is likely inflated. [src: bacdive_phenotype_metal_tolerance]
- The direct Fitness Browser check has no Gram-positive organisms. [src: bacdive_phenotype_metal_tolerance] The report considers the 12-organism validation underpowered. [src: bacdive_phenotype_metal_tolerance]
- Metal Fitness Atlas scores are genome-based predictions, not direct measurements. Controlling for n_metal_clusters in partial correlations mitigates circularity, but the associations remain phenotype-to-genome, not phenotype-to-phenotype. [src: bacdive_phenotype_metal_tolerance]
- Species-name matching reaches only 38.4% (5,647/27,702 GTDB species). GCA accession matching could recover additional links but was not implemented. [src: bacdive_phenotype_metal_tolerance]
- BacDive testing is biased toward well-studied organisms such as Pseudomonas and E. coli, while poorly studied species have sparse data. [src: bacdive_phenotype_metal_tolerance]
- The analysis uses only measured phenotype values. [src: bacdive_phenotype_metal_tolerance]
- The report suggests adding GCA accession matching, which could recover 10–30% more species. [src: bacdive_phenotype_metal_tolerance]
- The report suggests including BacDive's ML-predicted Gram stain, motility and oxygen tolerance, which could raise coverage substantially. [src: bacdive_phenotype_metal_tolerance] This would introduce model-dependent bias. [src: bacdive_phenotype_metal_tolerance]
- The report proposes using PGLS (phylogenetic generalized least squares) or phylogenetic PCA (principal component analysis) to formally remove phylogenetic signal before testing phenotype-metal associations. [src: bacdive_phenotype_metal_tolerance]
- The report proposes per-metal phenotype analysis, such as catalase for copper and urease for nickel, instead of composite scores. [src: bacdive_phenotype_metal_tolerance] This would require per-metal scores for the 27K species. [src: bacdive_phenotype_metal_tolerance]
- The report proposes testing the H₂S-to-chalcophilic-metal hypothesis (d = -0.87, underpowered) with sulfate-reducing bacteria under zinc/copper challenge. [src: bacdive_phenotype_metal_tolerance]
- The report proposes per-metal fitness profiling of urease+ versus urease- bacteria from the same class, ideally Gammaproteobacteria, where the pangenome-scale urease effect is near zero. [src: bacdive_phenotype_metal_tolerance]
- The report proposes RB-TnSeq (random barcode transposon sequencing) with matched urease+/- strains under nickel versus other metals to test nickel-specific tolerance directly. [src: bacdive_phenotype_metal_tolerance]

> **Erratum.** The report gives 38.4% for two different denominators. 37,368 of 97,334 matched strains is 38.4%; 5,647 of 27,702 GTDB species, the figure this sentence uses, is about one fifth, roughly half what the percentage suggests. [src: bacdive_phenotype_metal_tolerance]

## [[summaries/bacillota_b_subsurface_accessory__REPORT|Subsurface Bacillota_B Specialization — What Distinguishes Deep-Clay Lineages from Soil Congeners?]]

- The keyword scanner undercounts anaerobic signals, and 462 of 547 OGs fall in "other". The 80–100 estimate comes from manual reclassification. [src: bacillota_b_subsurface_accessory]
- The anchor cohort is only 10 genomes, against 62 in the baseline. Fisher's exact is adequate for large effects and the 547 enriched OGs are robust, but marginal effects with anchor counts of 3–5 should be treated descriptively. [src: bacillota_b_subsurface_accessory]
- The 10-genome anchor is genus-clumped: 3 BRH-c8a + 2 BRH-c4a + 2 Desulfosporosinus + Desulforudis + Ch130 + 1 other. [src: bacillota_b_subsurface_accessory]
- Genus-level phylogenetic confounding is partly mitigated by the cohort spanning four orders (Desulfotomaculales, Desulfitobacteriales, Ammonifexales, Thermacetogeniales), but not eliminated. [src: bacillota_b_subsurface_accessory]
- The anchor cohort is borehole/porewater-dominated by construction, so the comparison cannot test whether rock-attached Bacillota_B differs in gene content. [src: bacillota_b_subsurface_accessory]
- Some enriched OGs sit at coarse root level. eggNOG has no Bacillota_B-specific tier, because Bacillota_B is GTDB-defined while eggNOG uses NCBI taxonomy. [src: bacillota_b_subsurface_accessory]
- Within Bacillota_B, the PFAM cytochrome hits are few: PF02085.21 has 4 hits in 4 clusters. PF00034.26, PF13442.11 and PF22678.1 each have 1 hit in 1 cluster. [src: bacillota_b_subsurface_accessory] PF14537 (Cytochrom_NNT) has 0 hits and 0 clusters, confirmed as silently absent, the documented plant_microbiome_ecotypes pitfall. [src: bacillota_b_subsurface_accessory]
- Corrected IR detection leaves the clay project's IR-side comparisons non-significant. [src: bacillota_b_subsurface_accessory]

Next analyses the report proposes:

- A per-genus H1 analysis would separate genus-specific lineage-marker noise from enriched OGs recurrent across several subsurface-specialist genera, the genuine deep-clay signature. [src: bacillota_b_subsurface_accessory] With n=10 this is at the limit of statistical resolution. More clay-isolated Bacillota_B from BacDive linkage or future KBase Data Lakehouse pangenome ingests would improve power. [src: bacillota_b_subsurface_accessory]
- Retarget the NB01–04 pipeline to within-Bacteroidota, within-Pseudomonadota and within-Acidobacteriota deep-clay versus soil comparisons. Each would test whether the H1 functional-category signal generalizes or is Bacillota_B-specific. [src: bacillota_b_subsurface_accessory]
- Break down the extra gene fraction by COG / KEGG pathway to localize the genome expansion. [src: bacillota_b_subsurface_accessory]

## [[summaries/berdl_data_atlas__REPORT|BERDL Data Atlas — Inventory, Topic Map, and Cross-Reference Synergies]]

- The `protein_id` bridge proposed for UC1 was incorrect and needed correction by SQL probing. [src: berdl_data_atlas]
- UC1 was validated on a sample on the live cluster. The structure-function analysis itself is downstream work. [src: berdl_data_atlas]
- The zero-use bridges refer to the audit time and the audited BERIL projects only. [src: berdl_data_atlas]
- UC3, UC4 and UC5 are proposals whose bridges had no realized use. [src: berdl_data_atlas]

## [[summaries/caulobacter_fur_lipida_loss__REPORT|The regulatory and proteomic architecture of Δ*fur*-permitted lipid A loss in *Caulobacter crescentus*]]

This part of the report lists what limits its conclusions. CtpA fails its pre-registered bar, the outer-membrane proteome has no replicates, the fitness threshold was miscalibrated, and several comparative and mechanistic claims depend on screens, inference or outside literature. [src: caulobacter_fur_lipida_loss]

### CtpA and contrast design

CtpA was rejected at the pre-registered bar in *Caulobacter crescentus*. The 4599-vs-4584 transcript test gave pvalue=0.048 and FDR (false discovery rate)=0.109. That fails the BORDERLINE lower bound of 0.05 and the PASS bar of 0.05. [src: caulobacter_fur_lipida_loss] CtpA was also not detected in the single-replicate outer-membrane (OM) proteome. [src: caulobacter_fur_lipida_loss] Earlier drafts mislabeled this result as BORDERLINE, and the report corrects that. [src: caulobacter_fur_lipida_loss] The cumulative 4599-vs-4580 contrast (FDR=0.035) is significant. It conflates Δfur + ΔsspB and Δlpxc effects. The pre-registered 4599-vs-4584 contrast was designed to isolate the Δlpxc-specific response. [src: caulobacter_fur_lipida_loss] CtpA's hypothesized LpxF-substitute role (Zik 2022) remains untested. [src: caulobacter_fur_lipida_loss] See [[concepts/contrast-design-and-confounding-in-testing-a-putative-lipid-a-processing-enzyme]].

### Proteomics

The OM proteome has a single replicate per strain and no per-protein statistics, so only direction is interpretable. [src: caulobacter_fur_lipida_loss] The lptC2 protein induction, the Pal-Tol upregulation, the LptD/LptE protein decline and the CCNA_01217 protein increase need the replicated proteomics scheduled for summer 2026 before they can be claimed at publication rigor. [src: caulobacter_fur_lipida_loss] See [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]].

The Pal upregulation data show Pal up. The mechanistic reading is retrograde phospholipid transport for OM lipid homeostasis. That reading depends on Tan & Chng 2025 and remains an inference, not a direct measurement. [src: caulobacter_fur_lipida_loss] The report replaced an earlier "LPS-Mg²⁺-bridged stacking" mechanism. That mechanism was uncited and inconsistent with current Tol-Pal biology. [src: caulobacter_fur_lipida_loss] See [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss]].

### Fitness thresholds and the iron arm

The Path B (SspB-buffered) fitness phenotype-bearing rate is indistinguishable from genome background. [src: caulobacter_fur_lipida_loss] The pre-registered ≥10% threshold sat below the 33.25% background rate. Adversarial review surfaced this miscalibration, and it is recorded as a learned pattern. [src: caulobacter_fur_lipida_loss] See [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background]]. The "respiratory ATP (adenosine triphosphate) required" arm of the dual-release switch model is a working hypothesis, not an established finding. [src: caulobacter_fur_lipida_loss]

KBase Data Lakehouse fitness data supplied multi-condition resolution for the envelope arm of H2. [src: caulobacter_fur_lipida_loss] The Caulobacter Fitness Browser (FB) compendium has zero iron-limitation experiments out of 198. [src: caulobacter_fur_lipida_loss] H2's iron-limitation arm was therefore descoped to exploratory under the preflight rule. Testing the iron axis needs either more RB-TnSeq (random barcode transposon sequencing) under bipyridyl chelation or a cross-walk to Leaden 2018's published Δfur phenotype. [src: caulobacter_fur_lipida_loss]

The transcriptome used a single growth condition, PYE rich medium. Its Fur signal is therefore constitutive Δfur derepression, not a real iron-limitation response. [src: caulobacter_fur_lipida_loss] See [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]].

### SigU attribution

*Caulobacter* SigU (CCNA_02977) is uncharacterized in PaperBLAST. [src: caulobacter_fur_lipida_loss] The H1 SigU-as-driver test was reframed from literature overlap to a functional coherence check on the late cohort. Even this relaxed criterion failed (Fisher p=0.243). [src: caulobacter_fur_lipida_loss] Targeted SigU-induction RNA-seq would resolve the cohort attribution. [src: caulobacter_fur_lipida_loss]

### Comparative annotation screens

NB06 PaperBLAST has a ~80% false-negative rate for known *Caulobacter* essential lipid A biosynthesis genes. LpxA, LpxC, LpxD and LpxK each had 0 hits in PaperBLAST, while NCBI confirms 11-18 each. [src: caulobacter_fur_lipida_loss] The post-review NB06b NCBI annotation re-test reconfirmed the headline biology. Sphingolipid-pathway genes are absent in *A. baumannii*, *N. meningitidis* and *M. catarrhalis*, and ChvG-ChvI is restricted to alphaproteobacteria. [src: caulobacter_fur_lipida_loss] NB06 should now be read as a screen, and NB06b is the authoritative comparative measurement for the headline claim. [src: caulobacter_fur_lipida_loss] *M. catarrhalis* is under-annotated in PaperBLAST (162 genes total), so its presence/absence rows are advisory only. [src: caulobacter_fur_lipida_loss] See [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]] and [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]].

### Corrections to cohort counts and gene sets

Earlier drafts described an "early cohort of 30 genes" that included the 10 both-phase genes. The corrected NB03 disjoint ChvI partition is 20 unique-to-early + 10 both-phase + 49 late. The phase-structure verdict is unchanged. [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].

NB05 description-text matching falsely put CCNA_00565 (γ-glutamyltranspeptidase, a glutathione enzyme) and CCNA_01833 (glucosylceramidase, a ceramide enzyme) into the pre-curated PG-remodeling set. [src: caulobacter_fur_lipida_loss] They remain in the union of significant hits. They do not change the H4 verdict, which is well above the ≥3 threshold. [src: caulobacter_fur_lipida_loss]

- The iron-limitation arm of H2 could not be tested because the compendium has zero iron-limitation experiments. H2 was restricted to the envelope axis. [src: caulobacter_fur_lipida_loss]
- Path A enrichment is only marginal, and the threshold is uninformative on its own. [src: caulobacter_fur_lipida_loss]
- The single-replicate outer-membrane proteome cannot show whether the canonical Lpt apparatus is maintained, replaced or downregulated. Replicated proteomics are required. [src: caulobacter_fur_lipida_loss]
- Two peptidoglycan-set members are likely regex false positives: CCNA_00565 γ-glutamyltranspeptidase and CCNA_01833 glucosylceramidase. [src: caulobacter_fur_lipida_loss]
- SigU-induction RNA-seq is needed to test SigU as driver. [src: caulobacter_fur_lipida_loss]
- Earlier drafts overstated bidirectional peptidoglycan reorganisation. [src: caulobacter_fur_lipida_loss]

## [[summaries/cazyme_pangenome_ecology__REPORT|CAZyme Pangenome Ecology — Carbohydrate Metabolism Distribution Across 49K Bacterial Genomes]]

- Sampling effort confounds apparent pangenome openness, so the openness association is weak after controls. [src: cazyme_pangenome_ecology]
- The openness signal is absent in most phyla tested. [src: cazyme_pangenome_ecology]
- The GT/GH interpretations (capsules, biofilms, fiber substrates) are the report's readings, not direct tests. [src: cazyme_pangenome_ecology]
- The genome_cazy table gives only 7 top-level classes (GH, GT, PL, CE, AA, CB, CL), not families. [src: cazyme_pangenome_ecology] Family-level work needs arkinlab_dbcan, which has only 1,161 MGnify genomes, 2.3% of the catalog. [src: cazyme_pangenome_ecology]
- Soil (34%) and marine (23%) dominate the dataset. [src: cazyme_pangenome_ecology] Rare biomes (barley-rhizosphere n=74, zebrafish-fecal n=67) have limited statistical power. [src: cazyme_pangenome_ecology]
- Incomplete MAGs may still undercount absolute CAZyme abundance, despite no systematic isolate–MAG bias within biomes. [src: cazyme_pangenome_ecology]
- Phylogeny was controlled by within-phylum stratification, not formal regression such as PGLS (phylogenetic generalized least squares), which would need a resolved tree for 9,347 species. [src: cazyme_pangenome_ecology]
- The design is cross-sectional: profiles are compared across biomes, not tracked in lineages colonizing new environments. [src: cazyme_pangenome_ecology] Causal direction cannot be established from these data. [src: cazyme_pangenome_ecology]
- Proposed next analyses:
  - Repeat at CAZy family level as arkinlab_dbcan grows. [src: cazyme_pangenome_ecology]
  - Apply PGLS or phylogenetic mixed models with a GTDB species tree. [src: cazyme_pangenome_ecology]
  - Track CAZyme gain and loss across close species in different biomes. [src: cazyme_pangenome_ecology]
  - Cross-reference CAZyme profiles with kescience_fitnessbrowser fitness data. [src: cazyme_pangenome_ecology]
  - Test whether GT/GH predicts biome in a held-out set [src: cazyme_pangenome_ecology] and whether it correlates with EPS production or polysaccharide degradation phenotypes. [src: cazyme_pangenome_ecology]

## [[summaries/cf_formulation_design__REPORT|Rational Design of Protective Microbiome Formulations for Competitive Exclusion of *Pseudomonas aeruginosa* in Cystic Fibrosis Airways]]

- Metabolic overlap explains only 27% of inhibition variance, and the strongest inhibitors combine competition with direct antagonism, so metabolic competition alone does not account for them. [src: cf_formulation_design]
- No individual commensal outgrows PA14 on any tested substrate, so the report requires community-level niche coverage. [src: cf_formulation_design]
- Modest antagonism in some pairs means combinations are not uniformly additive. The report uses pairwise results to inform which combinations to advance to mouse models. [src: cf_formulation_design]

## [[summaries/clay_confined_subsurface__REPORT|Self-Sufficiency, Anaerobic Toolkit, and Cultivation Bias in Clay-Confined Cultured Bacterial Genomes]]

- The IR results are withdrawn, and the rock-attached versus porewater dichotomy is only half supported. [src: clay_confined_subsurface]
- The negative self-sufficiency result is read as showing that the cultured cohort lacks the extreme self-sufficient lineages, which are characteristically uncultivated MAGs (metagenome assembled genomes) or single-cell genomes. [src: clay_confined_subsurface]
- The 18-pathway GapMind universe has a ceiling, since most cultured organisms reach 17–18/18. [src: clay_confined_subsurface] The report likewise says it saturates near 18 for most cultivable bacteria, limiting upper-end resolution. [src: clay_confined_subsurface] It suggests a finer metric, such as presence of all standard amino-acid biosynthesis EC (Enzyme Commission) numbers in eggNOG, as a sensitivity check. [src: clay_confined_subsurface]
- Cohorts are small: 6 deep genomes after filtering, and 4 within Bacillota_B. [src: clay_confined_subsurface] With n=9 deep genomes only large effects (Cohen's d > 0.7) are reliably detectable in unfiltered comparisons. [src: clay_confined_subsurface] Marginal p-values, such as H1 within-Bacillota_B p=0.07, are descriptive. [src: clay_confined_subsurface]
- The "n=5 vs 19" structure of the Bacillota_B comparison may hide further granularity, because Desulfosporosinus, BRH-c8a and BRH-c4a may differ in which non-SR features they carry. [src: clay_confined_subsurface] A within-Bacillota_B genus-level pangenome analysis could surface the deep-clay-specific accessory genome. [src: clay_confined_subsurface]
- The cohort is cultured-only, so conclusions apply to cultivable porewater-cultured deep-clay isolates, not the full Mont Terri / bentonite community. [src: clay_confined_subsurface] CPR (candidate phyla radiation) / DPANN episymbionts and rock-attached Geobacter / Geothrix lineages are essentially absent. [src: clay_confined_subsurface] MAG-augmented work is needed to test whether the real community matches literature predictions. [src: clay_confined_subsurface]
- The compartment field is keyword-inferred from isolation_source strings, so some bentonite or rock entries could be porewater or rock-attached. [src: clay_confined_subsurface]
- eggNOG annotations propagate within ≥90% AAI clusters, so strain-level variants such as a single non-functional dsrA in a complete operon may be missed. [src: clay_confined_subsurface]

### Proposed next steps

- The report's strongest proposed next step is to ingest deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite and Oak Ridge into the pangenome and re-run the H1/H2/H3 framework with the expanded cohort. This would test whether the self-sufficiency signal (H1) emerges once rock-attached and uncultivated lineages are present. [src: clay_confined_subsurface]
- An exploratory within-Mont-Terri comparison of the BRC-3 porewater and BIC-A1 borehole genomes (5 + 3 genomes per borehole) could test whether the Bagnoud-paradigm SR-rich pattern is borehole-specific or site-wide. [src: clay_confined_subsurface]
- Granite-hosted (Olkiluoto), basalt-hosted (Oak Ridge) and salt-cavern subsurface cohorts in the KBase Data Lakehouse or future ingests could be tested with the same SR/IR marker framework. [src: clay_confined_subsurface]
- For Lakehouse Opalinus genomes that match Bagnoud's MAGs by ANI (average nucleotide identity), a future project could ask whether the observed gene presence corresponds to expression-validated activity. [src: clay_confined_subsurface]

## [[summaries/cofitness_coinheritance__REPORT|Co-fitness and Co-inheritance in Bacterial Pangenomes]]

Ralstonia UW163 and GMI1000 were excluded from the primary analysis. They have zero co-fitness data in the Fitness Browser despite appearing in its organism table. [src: cofitness_coinheritance] The report notes that these two organisms, the most phylogenetically diverse with the lowest ANI, would likely have been the most informative. [src: cofitness_coinheritance] Phylogenetic distance stratification was computed for 7 of 9 organisms, and the missing far stratum means functional coupling cannot be fully separated from phylogenetic signal. [src: cofitness_coinheritance] Other limits sit next to the results above: the Korea artifact, the small overall effect, the non-significant cross-organism test, and the prevalence ceiling. [src: cofitness_coinheritance]

The report proposes these next steps:

- Re-analyze using only gene pairs where both clusters are auxiliary (<95% prevalence), to maximize presence/absence variance. [src: cofitness_coinheritance]
- Calculate pairwise Pearson correlations from raw genefitness data for Ralstonia and other organisms lacking pre-computed co-fitness. [src: cofitness_coinheritance]
- Resolve the reference-genome mapping to enable phylogenetic distance stratification. [src: cofitness_coinheritance]
- Build module co-transfer networks across species and test whether co-fitness predicts cross-module co-inheritance. [src: cofitness_coinheritance]
- Target additional organisms with >30% auxiliary genes and existing co-fitness data. [src: cofitness_coinheritance]

## [[summaries/cog_analysis__REPORT|COG Functional Category Analysis]]

- COG annotations cover about 70% of genes, and unassigned genes may skew distributions. [src: cog_analysis] See [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment]].
- Composite multi-letter COG categories are counted once per gene, not split. [src: cog_analysis]
- The analysis uses 32 species, and a larger sample might reveal phylum-specific patterns. [src: cog_analysis]
- eggNOG v6 annotations may differ from original COG assignments. [src: cog_analysis] See [[entities/eggnog-orthologous-groups]].
- The report proposes analysing multiple species for consistent patterns. [src: cog_analysis]
- It proposes comparing COG distributions across taxonomic groups. [src: cog_analysis]
- It proposes investigating COG V (defense) and L (recombination) in detail. [src: cog_analysis]
- It proposes correlating novel-gene functions with environmental metadata to test whether they vary by habitat. [src: cog_analysis]

## [[summaries/comprehensive_metal_ecology__REPORT|Metal-Gene Density Predicts Ecological Niche Breadth in Prokaryotes]]

This part of the report asks whether geological proxies and a series of permutation, control and sensitivity tests support the metal-gene density association with niche breadth. The ore-deposit cross-reference is exploratory and null. The main association survives a predictor permutation test and quality restrictions, but it is not distinguishable from coreness-matched KO sets (KO = KEGG ortholog). [src: comprehensive_metal_ecology]

### Ore-deposit proximity (exploratory)

Cross-referencing KO density against ore-deposit proximity (CMMI database, n = 18–19 regions) gave weak, non-significant correlations. The report calls this exploratory only. Copper gave r = 0.34 (p = 0.17), zinc r = 0.34 (p = 0.17) and lead r = 0.01 (p = 0.99). [src: comprehensive_metal_ecology]

### Is the overall association distinct from null expectations?

The predictor permutation test (n = 1,000) supports a real association. The null β had mean ≈ 0 and SD (standard deviation) = 0.0029. The observed β = −0.0207 lay 7.14 SD below the null mean, with empirical p = 0/1000 (< 0.001). [src: comprehensive_metal_ecology] The baseline conditional PGLS (phylogenetic generalized least squares) model gave β = −0.0207 with p = 2.1×10⁻⁸. [src: comprehensive_metal_ecology]

The coreness-matched test limits this result. In NB20, 1,000 KO sets matched on count and coreness decile gave a null β median of −0.018 (range −0.039 to +0.012). The observed β = −0.021 gave emp_p = 0.298. [src: comprehensive_metal_ecology] The report concludes that the overall association is not distinguishable from coreness-matched alternatives. [src: comprehensive_metal_ecology] It locates the distinctive feature of the metal-gene set in its internal functional split, not in overall β magnitude. That split is resistance β ≈ 0 against cofactor biosynthesis β = −0.033. [src: comprehensive_metal_ecology]

Across 293,059 prokaryotic genomes, the core fraction at the 95% prevalence threshold was 0 for all five metal functional categories. No metal KO meets the near-universal threshold. [src: comprehensive_metal_ecology]

### Negative controls

All three named housekeeping controls in NB17 showed strongly negative β (−0.029 to −0.034). The report says they set a streamlining baseline and are not true nulls. [src: comprehensive_metal_ecology] NB18 confirmed five true-negative categories, all with |β| < 0.006 and q > 0.45. They are non-metal ABC (ATP-binding cassette) transporters, beta-lactam AMR (antimicrobial resistance), glycan biosynthesis, cell motility and two-component systems. [src: comprehensive_metal_ecology]

### Internal split of the metal-gene set

The report concludes that the resistance-null / constitutive-significant split is distinctive to metal genes. [src: comprehensive_metal_ecology] Three results support this.

- **Sub-functional resolution (NB19).** All AMR and TCS (two-component system) subcategories are positive, which the report describes as inducible/HGT (horizontal gene transfer) character. [src: comprehensive_metal_ecology] The sole significantly negative ABC subcategory is Lipid/LPS (lipopolysaccharide) export (β = −0.030, q = 3.3×10⁻⁵). The report reads this as consistent with constitutive outer-membrane maintenance. [src: comprehensive_metal_ecology]
- **Random partitions (NB25).** The 140-KO metal-gene set was randomly split into groups of 106 and 7, matching the resistance and cofactor group sizes. The observed Δβ = 0.035259 exceeded all 1,000 null splits (p < 0.001). The null median was −0.006 and the SD was 0.007. [src: comprehensive_metal_ecology]
- **Family comparison (NB25).** Comparison families gave Δβ = 0.032 for ABC, 0.012 for AMR and 0.006 for TCS. [src: comprehensive_metal_ecology] The metal-gene set has the largest internal split. [src: comprehensive_metal_ecology]

A leave-one-KO-out analysis of 4 assignable cofactor KOs (NB26) kept all 4 models significant. β ranged from −0.016 to −0.029, all p < 0.001, with no sign changes. No single KO drives the cofactor association. [src: comprehensive_metal_ecology]

### Confounders and sensitivity

Genome size is the only true confounder the report identifies. It reduces β by 46.7%, which lies within the coreness-permutation CI (confidence interval). [src: comprehensive_metal_ecology] Adding genome size gave β = −0.0110 (p = 0.006), a −46.7% true attenuation. [src: comprehensive_metal_ecology] The NB20 Block 4 comparison places the observed 46.7% attenuation within the permuted 95% CI [43.9%, 318.2%] (permuted median 94.9%). The report calls this weak evidence because the interval is wide. [src: comprehensive_metal_ecology]

Adding annotation depth (n_ko_ann_z) gave β = −0.0304 (p = 7.9×10⁻¹¹), a +46.7% amplification identified as a suppressor effect. [src: comprehensive_metal_ecology] The report explains this as follows. Genera with richer annotations have fewer apparent metal-gene specialists, so controlling for annotation bias strengthens the signal. [src: comprehensive_metal_ecology] The covariates n_ko_ann_z and ko_breadth_z are perfectly collinear, because both derive from n_ko_primary. Either gives the same conditional result. [src: comprehensive_metal_ecology]

The NB22 MAG-quality sensitivity analysis found a non-significant completeness covariate (p = 0.43) and an unchanged density β. [src: comprehensive_metal_ecology] Contamination showed a slight positive association (p = 0.042), with density β changed by <1.2%. [src: comprehensive_metal_ecology] In the high-quality subset (≥90%/≤5%, n = 511), the signal persisted with β = −0.018 and p = 0.005. [src: comprehensive_metal_ecology]

This part of the report tests whether soil redox explains the link between bedrock metal content and genus niche breadth. It then lists the limitations of the whole study. The redox controls leave the chromium signal unchanged. The limitations show a small effect size and several replication or coverage gaps. [src: comprehensive_metal_ecology]

### Redox proxy controls (Q4)

The analysis used two globally comprehensive soil proxies from enriched_metadata_gee. High soil moisture implies waterlogging, anaerobic conditions and immobile Cr(III). High soil organic matter (SOM, 0 cm) implies microbial O₂ drawdown and reducing capacity. [src: comprehensive_metal_ecology] The report used proxies because direct Cr(VI) data do not exist globally. The CSU speciation table has all-null BCR fraction fields and WoSIS has only pH, organic carbon and texture. GEMAS is Europe-only (4,343 pts) and NGSA mobile chromium is Australia-only (1,315 pts). [src: comprehensive_metal_ecology] The analysis is marked complete. It writes four N-series rows to data/latitude_mechanism_results.csv and adds moisture and SOM covariates to data/genus_lat_env_covariates.csv. [src: comprehensive_metal_ecology]

Genus-level correlations with bedrock metal (n ≈ 1,213–1,218) are weak. Moisture is not significantly correlated with bedrock Cr (r = −0.050, p = 0.083). It is negatively correlated with bedrock Co (r = −0.140, p = 9.3×10⁻⁷). [src: comprehensive_metal_ecology] SOM is not significantly correlated with Cr (r = −0.015, p = 0.597) or Co (r = −0.047, p = 0.103). [src: comprehensive_metal_ecology] The report reads bedrock Cr as near-orthogonal to both proxies. It reads Co-rich bedrock as slightly drier and more oxidizing mafic terrain. [src: comprehensive_metal_ecology]

### Niche-breadth models with redox covariates

- N_Cr (+ moisture), n = 1,219 genera: bedrock Cr β = +0.0175 (p = 1.2×10⁻⁸); pH β = +0.0117 (p = 5.4×10⁻³); moisture β = +0.003 (p = 0.44, NS). [src: comprehensive_metal_ecology]
- N_Co (+ moisture), n = 1,213: bedrock Co β = +0.0072 (p = 0.021); pH β = +0.0120 (p = 5.2×10⁻³); moisture β = +0.003 (p = 0.50, NS). [src: comprehensive_metal_ecology]
- N_Cr_som, n = 1,218: bedrock Cr β = +0.0187 (p = 1.3×10⁻⁹); pH β = +0.003 (p = 0.39, NS); SOM β = −0.0155 (p = 6.8×10⁻⁵). [src: comprehensive_metal_ecology]
- N_Co_som, n = 1,213: bedrock Co β = +0.0075 (p = 0.016); pH β = +0.005 (p = 0.21, NS); SOM β = −0.0134 (p = 6.6×10⁻⁴). [src: comprehensive_metal_ecology]

The report concludes that the bedrock Cr signal is not mediated by soil redox. β_Cr is unchanged between N_Cr and K_Cr (0.0175 vs 0.0176), and moisture is NS. This rules out the proposed "Cr(VI) via reducing/waterlogged soils" pathway. [src: comprehensive_metal_ecology] The report proposes two possible mechanisms, which it does not test. One is chronic Cr(III)/Ni/Mg stress in serpentine soils. The other is that ultramafic terrain selects niche specialists through correlated factors such as Ca/Mg ratio, soil structure and slow weathering. [src: comprehensive_metal_ecology]

### SOM as an incidental finding

High-SOM soils have narrower niches independently of bedrock metal type (β = −0.016, p = 6.8×10⁻⁵ in the Cr model). The report calls this incidental and outside the original model set. [src: comprehensive_metal_ecology] Including SOM absorbs the pH association: pH goes from p ≈ 0.003 in K models to p = 0.39. [src: comprehensive_metal_ecology] The report reads the "broader niches at high pH" signal as largely mediated through or confounded with SOM. High-SOM boreal and peatland environments tend to be acidic. The report suggests SOM may affect metal speciation through DOM chelation more directly than pH does. [src: comprehensive_metal_ecology] For the same reason, the pH niche-breadth signal in Finding 13 (β = −0.760) may be partly SOM-mediated. SOM-metal chelation in acidic peatland soils may confound a direct pH → speciation → specialist-selection reading. [src: comprehensive_metal_ecology]

### Limitations: effect size and causality

The metal-gene functional landscape is correlational. The evidence supports metal-content enrichment above compaction, but causality is unresolved. [src: comprehensive_metal_ecology] Metal-gene density explains a small share of genus-level niche-breadth variance (r² = 0.046 in P1), and breadth is multidimensionally determined. [src: comprehensive_metal_ecology] Explicit genome-size correction attenuates the association by 46.7% but does not eliminate it. [src: comprehensive_metal_ecology] In NB23, genome size partly confounds the association (46.7% attenuation), but the signal survives (p = 0.006). [src: comprehensive_metal_ecology] Annotation depth acts as a suppressor variable, not a confounder. [src: comprehensive_metal_ecology]

### Limitations: replication and data coverage

- The Australia-only NGSA replication (P3) is near-zero, which lowers confidence that the soil-concentration predictor is universal. [src: comprehensive_metal_ecology]
- The BacDive NB09 culture-based geographic niche-breadth replication is pending execution. [src: comprehensive_metal_ecology]
- ENIGMA FRC data cover n = 3 wells and are uninformative at that size. [src: comprehensive_metal_ecology]
- Levins' B_std from 16S OTUs (operational taxonomic units) may carry noise from coarse OTU–genus matching and MicrobeAtlas annotations. [src: comprehensive_metal_ecology]
- The cofactor category's strongest categorical signal rests on 7 KOs (KEGG orthologs). It is statistically robust (ΔAIC = −35.4), but its narrow biological definition warrants caution. [src: comprehensive_metal_ecology]

### Limitations: MAG quality

Per-Mb metal-gene density may be affected by MAG (metagenome assembled genome) incompleteness that is not random across taxa. [src: comprehensive_metal_ecology] NB22 tested this. Adding completeness leaves the density β unchanged (p = 0.43, NS). [src: comprehensive_metal_ecology] Adding contamination gives p = 0.042 with <1.2% β change. [src: comprehensive_metal_ecology] The high-quality-restricted analysis (n = 511) gives β = −0.018, p = 0.005, and the report treats the concern as addressed. [src: comprehensive_metal_ecology]

### Limitations: resistance genes, coreness and specificity

Resistance-gene null confidence intervals (CI) do not exclude small effects. The report therefore reads the null as absence of a substantial phylogenetically conserved association. [src: comprehensive_metal_ecology] The NB20 coreness-matched permutation does not support uniqueness of the metal gene set among conserved gene categories. Its emp_p is 0.298, and the primary β = −0.021 lies within the null distribution. [src: comprehensive_metal_ecology] The report places the distinctiveness of the metal gene set in its internal functional split, not its overall magnitude, which is part of the streamlining landscape. [src: comprehensive_metal_ecology] In NB23, core fraction is zero at the 95% threshold for all metal categories, so coreness cannot explain functional specificity. [src: comprehensive_metal_ecology]

### Limitations: co-occurrence confound

The positive-partner-count signal in Findings 15–16 (β = 138–210 across strata) correlates with niche breadth (Spearman ρ = 0.33–0.37, p < 10⁻⁴⁰). [src: comprehensive_metal_ecology] Partial analyses controlling for B_std are needed before the signal can be called independent of the primary specialisation axis. [src: comprehensive_metal_ecology]

- The effect is small (r² = 0.046). [src: comprehensive_metal_ecology] Housekeeping controls also associate negatively with niche breadth, so specificity to metals is not shown. [src: comprehensive_metal_ecology]
- Archaeal replication is non-significant, likely from low power. [src: comprehensive_metal_ecology] The Firmicutes within-phylum test is borderline and non-significant. [src: comprehensive_metal_ecology]
- P5 is not independent of P1. [src: comprehensive_metal_ecology]
- The per-KO driver analysis is exploratory. [src: comprehensive_metal_ecology] The cofactor jackknife shows that one KO, K01772, shifts β substantially. [src: comprehensive_metal_ecology]
- The plasmid test rests on only 3 double-signal resistance KOs. [src: comprehensive_metal_ecology] The report notes that BV-BRC sampling estimates for large-n genes add noise. [src: comprehensive_metal_ecology]

## [[summaries/conservation_fitness_synthesis__REPORT|Gene Conservation, Fitness, and the Architecture of Bacterial Genomes]]

- The report states that laboratory conditions are an impoverished proxy for nature. [src: conservation_fitness_synthesis] A gene with positive fitness when deleted in rich media may be essential in soil, biofilm, host tissue or other natural conditions. [src: conservation_fitness_synthesis]
- The identities of the 5,526 costly and dispensable genes are open. They may be mobile elements or recently acquired genes on the way out. [src: conservation_fitness_synthesis]
- It is open whether organisms from more variable environments have more core trade-off genes. The report proposes connecting laboratory fitness to AlphaEarth environmental data. [src: conservation_fitness_synthesis]
- It is open whether universally essential gene families exist across all 43 organisms. [src: conservation_fitness_synthesis]
- The co-regulated functions of the 48 accessory modules are unknown. [src: conservation_fitness_synthesis]

## [[summaries/conservation_vs_fitness__REPORT|Conservation vs Fitness -- Linking FB Genes to Pangenome Clusters]]

- The essential-gene definition is an upper bound. Genes without fitness data may lack insertions because they are short, in low-complexity regions or at scaffold edges, not because they are essential. [src: conservation_vs_fitness] Essential genes are also slightly shorter on average, consistent with some transposon insertion bias. [src: conservation_vs_fitness] See [[concepts/limits-of-transposon-based-essentiality-calls]].
- Essentiality from random barcode transposon sequencing (RB-TnSeq) is defined under the library-construction conditions. Genes essential only under stress would be missed. [src: conservation_vs_fitness]
- Clades with only 2 genomes have trivially high core fractions, which reduces core/auxiliary discrimination. [src: conservation_vs_fitness]
- *E. coli* was excluded because its main clade was absent from the pangenome (too many genomes). Keio (E. coli BW25113) mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness]
- Phase 2 excluded 10 organisms with <90% DIAMOND coverage, which reduced taxonomic breadth. [src: conservation_vs_fitness]
- The enrichment is modest (median OR 1.56) and significant in only 18 of 33 organisms. [src: conservation_vs_fitness]

Proposed next steps:
- Test whether genes important under specific stress conditions (fitness < -2) show different conservation patterns. [src: conservation_vs_fitness]
- Use FB ortholog data to find essential gene families conserved across species. [src: conservation_vs_fitness]
- Correlate mean fitness effect with core-genome fraction, rather than using only the essential/non-essential split. [src: conservation_vs_fitness]
- Characterize the 3,683 essential-auxiliary genes more deeply, asking whether they compensate for missing core functions. [src: conservation_vs_fitness]

## [[summaries/core_gene_tradeoffs__REPORT|Core Gene Paradox -- Why Are Core Genes More Burdensome?]]

- Lab conditions capture only a fraction of the environmental conditions bacteria face in nature. [src: core_gene_tradeoffs]
- Fitness Browser condition types are biased toward experimental convenience, not ecological relevance. [src: core_gene_tradeoffs]
- Burden (fit > 1) may reflect trade-offs rather than true dispensability. [src: core_gene_tradeoffs]
- The 90% identity threshold for DIAMOND matching may miss rapidly evolving genes. [src: core_gene_tradeoffs]

## [[summaries/costly_dispensable_genes__REPORT|The 5,526 Costly + Dispensable Genes]]

Caveats:

- Burden is defined as max_fit > 1 in any experiment, so one experiment can classify a gene as burdensome, which makes the result sensitive to noise. [src: costly_dispensable_genes]
- SEED/KEGG annotations cover only 56-79% of genes, and unannotated genes may differ functionally. [src: costly_dispensable_genes]
- The core/auxiliary classification is binary. [src: costly_dispensable_genes]
- The 90% identity DIAMOND threshold for linking may miss recently acquired genes with low similarity. [src: costly_dispensable_genes]
- Ortholog groups use bidirectional best hit (BBH) across 48 organisms, so genes with orthologs outside the set would be misclassified as orphans. [src: costly_dispensable_genes]
- Condition-specific phenotype data are biased toward lab-testable conditions. [src: costly_dispensable_genes]

Proposed next analyses:

- Explain the psRCH2 outlier, which has 21.5% costly+dispensable genes. [src: costly_dispensable_genes]
- Ask whether it is a recent phage invasion, IS element expansion, or genomic island acquisition. [src: costly_dispensable_genes]
- Test whether these genes cluster in genomic islands, near tRNA genes or at scaffold edges, which are hallmarks of HGT. [src: costly_dispensable_genes]
- Track the genes across multiple sequenced strains and close relatives to see whether they are being lost. [src: costly_dispensable_genes]
- Use ENIGMA CORAL community data to test whether organisms with more of these genes co-occur with organisms that could supply the lost functions. [src: costly_dispensable_genes]
- Replace the binary classification with the fraction of species genomes carrying each gene cluster. [src: costly_dispensable_genes]

## [[summaries/counter_ion_effects__REPORT|Counter Ion Effects on Metal Fitness Measurements]]

The SynE outlier is addressed by the exclusion analysis above. [src: counter_ion_effects] The psRCH2 salt comparison is confounded by oxygen status, and it is the only within-metal counter-ion comparison. [src: counter_ion_effects] The cadmium (n=92) and iron (n=9) corrected deltas, each from one organism, are statistically unreliable. [src: counter_ion_effects] Manganese (n=30, 1 org) is low-powered, though its 100% core result is robust by ceiling effect. [src: counter_ion_effects] Several per-metal overlaps rest on one organism, with no cross-organism replication. [src: counter_ion_effects]

- NaCl delivers Na⁺ as well as Cl⁻, so its profile includes sodium toxicity and osmotic effects. The report proposes KCl or choline chloride as more specific chloride controls. [src: counter_ion_effects]
- The 39.8% overlap depends on the NaCl-importance threshold (fit < -1 or n_sick ≥ 1). Stricter thresholds would reduce it and more permissive ones would increase it. [src: counter_ion_effects]
- Putative essential genes (~14.3% of protein-coding genes) lack insertions and are absent from both datasets. They are 82% core, and excluding them affects original and corrected analyses equally. [src: counter_ion_effects]
- The shared-stress versus metal-specific classification was not formally tested for functional enrichment by hypergeometric tests, and the SEED annotation comparison is descriptive. [src: counter_ion_effects]
- H1d, on chloride versus oxyanion functional profiles, was dropped and not tested. [src: counter_ion_effects]

### Follow-up proposed by the report

- Use COG (clusters of orthologous groups), KEGG and PFAM annotations to test whether shared-stress genes are enriched for envelope/transport functions and metal-specific genes for metal-binding/efflux. [src: counter_ion_effects]
- Compare metal–choline chloride overlap with metal–NaCl overlap to separate chloride from osmotic confounding; several Fitness Browser organisms have choline chloride experiments. [src: counter_ion_effects]
- Apply the metal–NaCl overlap analysis to ICA (independent component analysis) modules from the fitness_modules project, asking whether metal-responsive modules overlap NaCl-responsive ones. [src: counter_ion_effects]
- Use the classification to refine the Atlas result on condition-specific metal genes. [src: counter_ion_effects]
- Run RB-TnSeq with matched metal chloride and sulfate concentrations in a single organism under identical growth conditions, which the report calls the most impactful follow-up because it removes the aerobic/anaerobic confound of the psRCH2 comparison. [src: counter_ion_effects]
- Specific proposed pairs: CuCl₂ 0.5 mM versus CuSO₄ 0.5 mM in MR-1 or DvH, since copper is the most-tested metal and both salts are available [src: counter_ion_effects]; ZnCl₂ 0.2 mM versus ZnSO₄ 0.2 mM in MR-1, adding chloride to the already-tested sulfate form to test the null directly [src: counter_ion_effects]; and CoCl₂ 0.1 mM versus CoSO₄ 0.1 mM in DvH, since cobalt has the highest Cl⁻ load in current data. [src: counter_ion_effects]
- Run NaCl dose-response experiments at 0.1, 1, 10, 100 and 500 mM in DvH to allow dose-matching between NaCl stress and effective Cl⁻ from metal salts. [src: counter_ion_effects]

## [[summaries/discoveries|Discoveries Log]]

- The v1.7 FAIL was technically correct for its schema but was not a scientific refutation. The report says a "structurally degenerate" verdict is an invitation to fix the schema, not to conclude on the science. [src: discoveries]
- The v1.7 failure is attributed to name-regex missing iron in heme pathway names, so the lesson rests on this one project and test. [src: discoveries]

## [[summaries/ecotype_analysis__REPORT|Ecotype Correlation Analysis]]

- AlphaEarth embeddings have only 28.4% genome coverage, which limits the environmental signal available. [src: ecotype_analysis]
- Geographic coordinates from NCBI metadata are often missing or imprecise, which reduces the quality of environmental associations. [src: ecotype_analysis] See [[concepts/coordinate-quality-and-institutional-address-artifacts-in-genome-geolocation]].
- Partial correlations assume linear relationships between distance matrices, so they may miss nonlinear ecological effects. [src: ecotype_analysis]
- For host-associated organisms, the coordinates reflect the collection site rather than the organism's actual microenvironment. Latitude and longitude are therefore less meaningful for them, which limits the free-living versus host-associated comparison. [src: ecotype_analysis]

The report proposes three next analyses:
1. Test whether specific COG (clusters of orthologous groups) categories, such as V-Defense and L-Mobile, show stronger environment effects. [src: ecotype_analysis]
2. Try alternative embedding distances, or use environmental metadata directly. [src: ecotype_analysis]
3. For species with identified ecotypes, compare gene content between ecotype clusters. [src: ecotype_analysis]

## [[summaries/ecotype_env_reanalysis__REPORT|Ecotype Reanalysis — Environmental vs Human-Associated Species]]

- **No downsampling:** The median partial correlation across all 183 species was 0.081, against 0.003 in the original. [src: ecotype_env_reanalysis] This 27x difference makes absolute values not comparable with the original, but the group comparison stays valid because both groups use the same method. [src: ecotype_env_reanalysis] Larger samples detect weaker correlations, and omitting downsampling changes distance distributions. [src: ecotype_env_reanalysis]
- **NaN exclusion:** Of 30 species with NaN (not a number) partial correlations, rates were 10/47 = 21% for environmental, 13/66 = 20% for Mixed/Other and 7/100 = 7% for human-associated. [src: ecotype_env_reanalysis] The report says this would bias toward a stronger environmental signal, opposite to what was observed, so correcting it would only strengthen the null. [src: ecotype_env_reanalysis]
- **Klebsiella pneumoniae:** This major clinical species was excluded because gene cluster extraction exceeded Spark's maxResultSize. [src: ecotype_env_reanalysis] See [[entities/klebsiella-pneumoniae]].
- **Majority vote:** A species with 51% gut genomes counts as human-associated. The continuous Spearman analysis addresses this and confirms the null. [src: ecotype_env_reanalysis]
- **Proposed next steps:** Compare downsampled and full-genome extraction to explain the 27x gap. [src: ecotype_env_reanalysis] Test specific gene subsets, since environment may act on functional categories such as transport and secondary metabolism rather than whole-genome Jaccard distance. [src: ecotype_env_reanalysis] Repeat with ENVO (Environment Ontology) terms from env_broad_scale. [src: ecotype_env_reanalysis] Add genome count as a covariate, since species with more genomes may have inflated correlations. [src: ecotype_env_reanalysis]

## [[summaries/ecotype_functional_differentiation__REPORT|Ecotype Functional Differentiation]]

Two sampled species experienced transient Spark S3 read errors. Separately, one species, Limisoma sp., had too little structure for valid clustering. [src: ecotype_functional_differentiation] Spark query times varied from 94s to 1642s per species during heavy cluster usage, and 2 species were lost to S3 read errors. [src: ecotype_functional_differentiation] The moderate silhouette scores mean the ecotypes overlap and are not discrete. [src: ecotype_functional_differentiation] The significance-rate advantage of adaptive over housekeeping categories is modest, so H1 is only partly supported. [src: ecotype_functional_differentiation]

- Sample: 12 species were retained from 15 sampled (80%), out of 456 eligible. The pangenome-size-stratified sample may not capture phylogenetic or ecological breadth. [src: ecotype_functional_differentiation]
- Clustering: KMeans was used because HDBSCAN was unavailable on the cluster. [src: ecotype_functional_differentiation] KMeans assumes spherical clusters and needs a prespecified k (searched 2-6), whereas HDBSCAN would better handle variable-density subpopulations. [src: ecotype_functional_differentiation]
- Annotation: only ~38% of gene clusters have COG annotations. [src: ecotype_functional_differentiation] The 62% without annotations may contain ecotype-specific adaptive genes in poorly characterized categories, potentially biasing results toward well-annotated housekeeping functions. [src: ecotype_functional_differentiation]
- Phylogeny: gene-content ecotypes may reflect within-species phylogenetic substructure, not ecological specialization. Without within-species phylogenetic controls, the report cannot distinguish adaptive ecotypes from demographic subpopulations. [src: ecotype_functional_differentiation]
- Effect size: the largest mean effects (S: 0.039, L: 0.034) are ~3-4 percentage point differences in COG category proportions. They are statistically significant because of large sample sizes, but biologically modest. [src: ecotype_functional_differentiation]

Next analyses proposed by the report:

- Scale to all 456 eligible species, using off-peak execution or optimized queries, since Spark load constrained the sample of 15. [src: ecotype_functional_differentiation]
- Overlay core-genome phylogenetic trees on ecotype assignments to separate ecological adaptation from demographic substructure. [src: ecotype_functional_differentiation]
- Characterize S (unknown function) genes with AlphaFold structure prediction or domain analysis, to test for cryptic defense, transport or regulatory functions. [src: ecotype_functional_differentiation]
- For species with soil, host-associated or aquatic habitat metadata, test whether ecotype-defining COG categories correlate with environmental source. [src: ecotype_functional_differentiation]
- Re-run clustering with HDBSCAN, if available, to assess how sensitive ecotype definitions are to clustering method. [src: ecotype_functional_differentiation]

## [[summaries/enigma_carbon_census_1__REPORT|ENIGMA Carbon Census — A Tiered Knowledge Census of 83 Enrichment Compounds]]

This part of the report places the census results against the literature. It reads catabolic knowledge in the queried resources as deep for aromatics and phthalates and absent for most alkaloids and terpenoids. [src: enigma_carbon_census_1] It also lists the limits on what the atlas and the statistics can support.

### Aromatic catabolism is well characterized

Six of the eight callable compounds route through well-characterized aromatic catabolism. Salicylate, the hydroxybenzoates/-aldehyde and the two phthalates converge on protocatechuate/catechol and the β-ketoadipate pathway. [src: enigma_carbon_census_1] The report calls this funnel the canonical bacterial route for hydroxybenzoates, salicylate and phthalates. [src: enigma_carbon_census_1] See [[entities/ketoadipate-pathway]]. Because the six share one lower pathway, they co-occur within the aromatic block. [src: enigma_carbon_census_1]

The other two callables do not use this funnel. [src: enigma_carbon_census_1] Phenylethylamine goes by amine oxidation to phenylacetate and then the phenylacetyl-CoA (paa) pathway. That route is mechanistically separate, so its cross-block co-occurrence signal is not part of the β-ketoadipate funnel. [src: enigma_carbon_census_1] Xanthine is a purine (nitrogen) pathway compound mis-included here. [src: enigma_carbon_census_1]

### Phthalate and terephthalate, and Burkholderiales

The report calls terephthalate/phthalate catabolism the best-characterized necromass aromatic catabolism in the census. [src: enigma_carbon_census_1] Terephthalate goes via terephthalate dioxygenase to protocatechuate. Degraders are concentrated in Pseudomonadota (Ideonella/Comamonas) and in actinobacterial degraders. [src: enigma_carbon_census_1] Literature support for Burkholderiales/Comamonadaceae dominance is strongest for phthalate/terephthalate catabolism, which matches the report's versatility ranking. [src: enigma_carbon_census_1] See [[entities/burkholderiales]].

The periphyton enrichment of this clade rests mainly on the project's own abundance data, at ~97% prevalence in periphyton samples. [src: enigma_carbon_census_1] The report says this is the project's own observation, pending a targeted literature anchor. [src: enigma_carbon_census_1]

### Dark compounds and literature gaps

The report says the dark compounds are a deliverable, not a failure of method. The interpretation text names 75 dark compounds [src: enigma_carbon_census_1], while the contribution summary gives a dark fraction of 89% (74/83). [src: enigma_carbon_census_1] The report does not explain this one-compound difference, so both figures are given as stated. The dark compounds name where genetic determinants of carbon use cannot be linked in these resources, and where enrichment is the candidate discovery route. [src: enigma_carbon_census_1] "Organism-dark" means not linkable through the queried the KBase Data Lakehouse and curated resources. It does not mean unknown to science. [src: enigma_carbon_census_1] Class-level catabolic literature exists for monoterpenes (Marmulla & Harder, *Front. Microbiol.* 2014) and for alkaloids such as nicotine (Huang et al., *Front. Microbiol.* 2020). [src: enigma_carbon_census_1] The census found zero literature rescues, but that reflects a PubMed-title-only screen, not absence of evidence. A PaperBLAST/abstract-level pass would likely reclassify part of the dark set. [src: enigma_carbon_census_1] See [[concepts/resource-darkness-of-compound-catabolism]].

The report lists three contributions:
- a tier-stratified linkage from 83 named compounds through structures, pathways, ENIGMA isolate strains, GTDB phylogeny, SSO field occurrence and global biome abundance, with the Tier 0 gap treated as a result [src: enigma_carbon_census_1];
- a quantified dark fraction of 89% (74/83), with per-class and per-reason structure to guide enrichment prioritization [src: enigma_carbon_census_1];
- a periphyton-resolved abundance reservoir for the implicated genera that bulk-environment labels obscure. [src: enigma_carbon_census_1]

### Limits of the global atlas

No environmental dataset measures the census compounds. The atlas therefore reports biome occupancy of the implicated genera, not catabolic flux. [src: enigma_carbon_census_1] It is a biome-occupancy proxy, and enrichment of a genus in soil does not mean it degrades the compound there. [src: enigma_carbon_census_1] The signal is biologically coherent: soil generalists in soil, aquatic Betaproteobacteria in freshwater, a Comamonadaceae periphyton reservoir, and terrestrial taxa rare in the open ocean. [src: enigma_carbon_census_1] This validates the taxonomic/abundance pipeline and the ENVO (Environment Ontology)/GOLD labels. It does not validate the compound→pathway→organism inference. It also cannot show that any genus degrades a census compound in a sampled environment. [src: enigma_carbon_census_1] The marine arm has 302 PM runs with presence/abundance only and no gene information, so it suits only a negative biome contrast. [src: enigma_carbon_census_1] See [[concepts/biome-abundance-atlases-as-a-proxy-for-catabolic-potential]].

The soil-versus-freshwater enrichment p/q-values are exploratory and not calibrated. Each metagenome is treated as independent in a rank test over compositional, zero-inflated abundances. [src: enigma_carbon_census_1] All 83 genera reach q<0.05, many at q~1e-70, which the report attributes to massively inflated significance. [src: enigma_carbon_census_1] The direction and rank of the contrast are trustworthy, but the p-values should not be quoted as calibrated significance. [src: enigma_carbon_census_1] The label-free outlier mode (Arm B) is the more defensible discovery signal. [src: enigma_carbon_census_1] See [[concepts/calibration-and-denominators-in-environmental-abundance-contrasts]].

### Callability, filters and the xanthine error

The 8 ENIGMA isolate-call callables rest on a genome-prevalence-<10% signature-reaction filter. It keeps a reaction only if it is catabolic for the compound, by KEGG degradation map membership or a 3-reaction curated allowlist. [src: enigma_carbon_census_1] A different filter would move the callable/dark boundary, so the dark fraction is conditional on this choice. [src: enigma_carbon_census_1] The 9th callable, lauric acid, rests on an independent measured-fitness basis and is not subject to this filter. [src: enigma_carbon_census_1] See [[concepts/catabolic-direction-filtering-and-mis-scored-carbon-calls]].

Xanthine's allowlisted reaction R02107 (xanthine→urate, xanthine oxidase) is the purine pathway, which is nitrogen acquisition and not carbon catabolism. [src: enigma_carbon_census_1] A bacterial carbon route for purines exists, but it is a distinct anaerobic gene cluster that the project does not score. [src: enigma_carbon_census_1] The carbon-callable set is therefore effectively 8 of the 9 callable. [src: enigma_carbon_census_1] R02107 has been removed from the carbon allowlist in build_nb03.py. The committed deliverable tables still include xanthine because they were not regenerated, and rerunning NB03→NB04→NB08 would drop it. [src: enigma_carbon_census_1]

With only n=9 callable compounds, the physicochemical contrasts (callable compounds smaller/simpler) are directional only. They use uncorrected Mann–Whitney p-values and are descriptive, not calibrated significance. [src: enigma_carbon_census_1]

### Completeness scores and taxonomy bridging

The sig_completeness metric is the fraction of each compound's own signature reactions that a genome carries. [src: enigma_carbon_census_1] High-certainty calls are not comparable across compounds. Terephthalic acid has a single required reaction, so any carrier scores 1.0 ("high"). Phthalic acid has a 3-reaction signature, which cannot score that way. [src: enigma_carbon_census_1] The "terephthalic 34/34 high" headline is therefore the weakest completeness call, not the strongest. The report advises reading certainty as the raw n_sig_carried / n_required in phylo_utilizer_map.tsv. [src: enigma_carbon_census_1]

The pangenome↔ENIGMA taxonomic bridge is genus-level at best. The report avoids isolate-specific transfer of pangenome Tier-2 reconstructions and uses direct genome_depot annotation instead. [src: enigma_carbon_census_1] See [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]].

### Untestable source hypothesis

The source-tracking hypothesis H3 is genuinely untestable with these compounds. The n=2 necromass callables are fully confounded with phthalate chemistry, and the report states this rather than forcing a result. [src: enigma_carbon_census_1] See [[concepts/confounding-of-compound-source-with-chemical-class]].

- Darkness is resource-darkness, and a literature/PaperBLAST pass would reclassify some dark compounds. [src: enigma_carbon_census_1]
- Lauric acid sits outside both arms, since it has measured fitness but no isolate prediction. [src: enigma_carbon_census_1]
- The terephthalic-acid high-certainty figure is a single-signature artifact. [src: enigma_carbon_census_1]
- Physicochemical comparisons are directional because n=9. [src: enigma_carbon_census_1]
- The soil-versus-freshwater contrast is exploratory. The global atlas measures organism abundance, not catabolism. [src: enigma_carbon_census_1]
- Conservation fractions describe within-called-set specialization only. [src: enigma_carbon_census_1]

## [[summaries/enigma_contamination_functional_potential__REPORT|Contamination Gradient vs Functional Potential in ENIGMA Communities]]

Coverage-aware models raise the effective rows at fraction level. Species-proxy high-coverage tests are underpowered (n=1). [src: enigma_contamination_functional_potential] Species-proxy mode retained too little coverage for a high-coverage test. [src: enigma_contamination_functional_potential] The positive adjusted associations are exploratory. Most have FDR q above 0.05, and the within-fraction tests did not reproduce them. [src: enigma_contamination_functional_potential] Exploratory sensitivity-model significance is concentrated in defense and depends on coverage/covariate specification. Broader effects across outcomes are not established. [src: enigma_contamination_functional_potential] The stress-score result (p = 0.0407) is a single exploratory exception among mostly null outcomes. [src: enigma_contamination_functional_potential] The report suggests that finer taxonomic resolution does not yet strengthen inference. [src: enigma_contamination_functional_potential]

Other limits the report states:
- The ENIGMA taxonomy table ddt_brick0000454 gives labels only through Genus, so true species-level bridge testing is not possible in this slice. [src: enigma_contamination_functional_potential]
- Genus-level mapping may mask strain-level adaptation. [src: enigma_contamination_functional_potential]
- 862/1,392 observed genera were unmapped to the current pangenome bridge. [src: enigma_contamination_functional_potential]
- COG-fraction proxies are coarse summaries, not curated resistance pathways. [src: enigma_contamination_functional_potential]
- The bridge and annotation stack depends on GTDB and eggNOG conventions, and at genus level broad COG-style signals can dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential]
- Site structure is represented by coarse location_prefix effects, not full hierarchical or random-effects modeling. [src: enigma_contamination_functional_potential]

Next analyses the report proposes:
1. Replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries. [src: enigma_contamination_functional_potential]
2. Increase taxonomic resolution (species/strain-level bridge from metagenomic or higher-resolution ENIGMA taxonomy) and quantify gains over genus and species-proxy modes. [src: enigma_contamination_functional_potential]
3. Fit adjusted models with explicit depth, location cluster and sampling date covariates and compositional modeling controls. [src: enigma_contamination_functional_potential]
4. Investigate the contribution of unmapped genera to contamination gradients and bridge expansion opportunities. [src: enigma_contamination_functional_potential]
5. Add mixed-effects or hierarchical site models with well/location-level random effects to test whether defense associations persist under richer structure control. [src: enigma_contamination_functional_potential]

## [[summaries/enigma_sso_asv_ecology__REPORT|SSO Subsurface Community Ecology — Spatial Structure, Functional Gradients, and Hydrogeological Drivers]]

- The Procrustes result (p = 0.080) and the east-west column Mantel (p = 0.092) are marginal and not significant at 0.05. [src: enigma_sso_asv_ecology]
- The hillslope alignment is null [src: enigma_sso_asv_ecology], and well identity is not significant. [src: enigma_sso_asv_ecology]
- Genus-level functional annotation covers only 21% of total reads (65 of 1,038 genera), so process abundance estimates are lower bounds. [src: enigma_sso_asv_ecology] The unclassified 56% of reads could harbor additional functional capacity. [src: enigma_sso_asv_ecology]
- The report recommends assessing this gap by comparing genus-level patterns with class-level traits (78% coverage), which show consistent redox patterns. [src: enigma_sso_asv_ecology]
- Species-level classification is ~0%, and genus level covers only 44% of sediment reads. [src: enigma_sso_asv_ecology]
- Functional inference relies on literature-based trait assignments rather than direct genomic evidence. [src: enigma_sso_asv_ecology] Phylum/class-level trait scores are consensus estimates, not empirical measurements for these populations. [src: enigma_sso_asv_ecology]
- The plume explanations for the corridor, depth pattern and process peaks are the report's interpretations. [src: enigma_sso_asv_ecology] The M5 mixing-zone claim awaits geochemistry validation. [src: enigma_sso_asv_ecology]
- No direct geochemistry is available: 221 SSO sample tubes are registered in CORAL but not loaded. [src: enigma_sso_asv_ecology]
- Sediment cores were collected once per well (Feb-Mar 2023), with no within-well temporal replication. [src: enigma_sso_asv_ecology] A single core sampling event cannot show temporal plume dynamics or community response. [src: enigma_sso_asv_ecology]
- The 18-month offset between sediment (2023) and groundwater (2024) confounds material type with time, limiting cross-material temporal comparisons. [src: enigma_sso_asv_ecology] Seasonal or plume dynamics could confound the comparison. [src: enigma_sso_asv_ecology]
- Only 5 of 9 wells have groundwater ASV data (L7, L9, M4, M6, U2), missing M5 (denitrification hotspot) and U3 (plume entry). [src: enigma_sso_asv_ecology]
- Depth and date effects in groundwater were null (p = 0.430 and p = 0.998). [src: enigma_sso_asv_ecology]

### Proposed next analyses

- Load the 221 registered geochemistry samples (metals, IC/TOC, isotopes, NH₃/NO₂) into CORAL to correlate community composition directly with environmental measurements and validate or refute the plume model. [src: enigma_sso_asv_ecology]
- Extract pump test ASV data from Brick 460-462 (wells L8/M5/U2) [src: enigma_sso_asv_ecology] as a third temporal snapshot (Mar 2024) to test the M5 denitrification hotspot prediction and add temporal resolution. [src: enigma_sso_asv_ecology]
- Use the actual 16S sequences in Bricks 457/460/477 for weighted UniFrac, which may be more sensitive to plume effects than Bray-Curtis on ASV counts. [src: enigma_sso_asv_ecology]
- Run shotgun metagenomics at the same spatial resolution to confirm functional inferences currently based on taxonomy-to-trait mapping [src: enigma_sso_asv_ecology] and to capture the 56% of reads without genus-level classification. [src: enigma_sso_asv_ecology]
- Repeat 16S profiling across seasons and plume dynamics to test whether community structure tracks plume fluctuations in real time. [src: enigma_sso_asv_ecology]

## [[summaries/env_embedding_explorer__REPORT|AlphaEarth Embeddings, Geography & Environment Explorer]]

- The coordinate heuristic is a rough first pass. The report recommends checking whether genomes at each location share homogeneous isolation sources (a real site) or diverse unrelated ones (an institution). [src: env_embedding_explorer] It flags legitimate sites including Rifle and Saanich Inlet and needs refinement using isolation_source homogeneity. [src: env_embedding_explorer]
- The pooled distance curve blends environmental and human-associated signals. [src: env_embedding_explorer]
- Taxonomic structure in the UMAP is confounded with environment. [src: env_embedding_explorer] UMAP is non-linear, its cluster structure depends on n_neighbors and min_dist, and it may not reflect true high-dimensional topology. [src: env_embedding_explorer]
- DBSCAN eps=0.5 produced 320 clusters, likely too fine-grained, and coarser clustering may better match environment categories. [src: env_embedding_explorer]
- The keyword mapping leaves 17% of genomes as Other. [src: env_embedding_explorer] Keyword matching misses site-specific labels and non-English terms. [src: env_embedding_explorer]
- AlphaEarth coverage is only 28.4% of all genomes and is biased toward genomes with valid lat/lon metadata. [src: env_embedding_explorer] The 38% clinical/human bias may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer]
- The cause of the 4.6% NaN embedding values is unknown, possibly missing satellite imagery at those coordinates. [src: env_embedding_explorer]
- Proposed next steps from the report:
  - Reduce "Other" by adding keywords for clinical body sites, underground labs and generic water sources, with env_broad_scale as fallback. [src: env_embedding_explorer]
  - Re-run the ecotype analysis on environmental-only samples, where the embeddings carry more geographic signal. [src: env_embedding_explorer]
  - Correlate A00–A63 with latitude, temperature, precipitation, NDVI or land cover to learn what each dimension encodes. [src: env_embedding_explorer]
  - Compare ENVO-based classification with keyword harmonization for genomes with env_broad_scale. [src: env_embedding_explorer]
  - Test whether environmental samples with similar embeddings share more accessory genes after controlling for phylogeny. [src: env_embedding_explorer]

## [[summaries/essential_genome__REPORT|The Pan-Bacterial Essential Genome]]

- The report attributes its smaller experimentally defined universally essential set to restricting it to genes whose transposon disruption is lethal across all 48 tested organisms, a more stringent criterion than computational conservation. [src: essential_genome]
- The 4,385 orphan hypothetical essential genes are not predictable by the module-transfer method. [src: essential_genome]
- Predictions cover 35.3% of predictable targets. [src: essential_genome]
- The essential gene definition is an upper bound, because missing insertions can reflect small gene size, AT-rich sequence, or scaffold edge effects rather than true essentiality. [src: essential_genome]
- BBH orthology is conservative: it misses paralogs, gene fusions and distant homologs, so some orphan essentials may have undetected diverged orthologs. [src: essential_genome]
- Connected components of the BBH graph can over-merge unrelated genes through transitive connections, particularly for multi-domain proteins. [src: essential_genome]
- Essentiality is defined under library construction conditions, typically rich media, so genes essential only under stress are missed. [src: essential_genome]
- The 48 organisms are biased toward culturable Proteobacteria, and uncultured lineages, Actinobacteria and Firmicutes are underrepresented. [src: essential_genome]
- Module-transfer predictions are indirect, because they come from non-essential orthologs in other organisms and the essential gene's function may have diverged. [src: essential_genome]

Next analyses proposed by the report:
- Characterize the 7,084 orphan essentials: mobile-element association, recent acquisition, rapid evolution and functional categories. [src: essential_genome]
- Test the 1,382 module-transfer predictions by CRISPRi (CRISPR interference) knockdown under conditions predicted by module context. [src: essential_genome]
- Test whether essentiality of variably essential families correlates with metabolic pathway completeness, including absence of an alternative pathway. [src: essential_genome]
- Rerun the analysis as Fitness Browser taxonomic coverage grows, to test whether the 15 pan-essential families remain universal. [src: essential_genome]
- Cross-reference the Database of Essential Genes to find families essential in organisms outside the Fitness Browser. [src: essential_genome]

## [[summaries/essential_metabolome__REPORT|GapMind Pathway Analysis Across Essential Gene Organisms]]

- Coverage limits the work to a pilot of 7 organisms, not the intended 45 FB organisms with essential gene data. [src: essential_metabolome]
- Coverage is unknown for the remaining 38 FB organisms. [src: essential_metabolome]
- The sample has limited phylogenetic diversity, mostly Proteobacteria plus 1 Deltaproteobacterium. [src: essential_metabolome]
- The results cannot be generalized to a pan-bacterial scale. [src: essential_metabolome]
- GapMind predictions are computational, not experimental. [src: essential_metabolome]
- Using complete and likely_complete categories may miss partial pathways. [src: essential_metabolome]
- GapMind may miss organisms with divergent metabolic genes. [src: essential_metabolome]
- Non-canonical or poorly characterized pathways are not detected. [src: essential_metabolome]
- The RB-TnSeq (random barcode transposon sequencing) experiments behind the essential gene data used rich media. [src: essential_metabolome]
- Nutrient supplementation may make biosynthetic genes appear non-essential. [src: essential_metabolome]
- The report cannot distinguish genes essential for biosynthesis from those essential for viability. [src: essential_metabolome]

Next analyses the report proposes:
- A literature review of whether D. vulgaris serine auxotrophy has been documented experimentally. [src: essential_metabolome]
- Checking lower-confidence GapMind predictions for a D. vulgaris serine pathway with "steps_missing" status. [src: essential_metabolome]
- Expanding the FB organism mapping to increase the sample size. [src: essential_metabolome]
- An eggNOG pathway analysis using Enzyme Commission (EC) annotations mapped to KEGG pathways for all 45 FB organisms, including E. coli. [src: essential_metabolome]
- A hybrid approach combining pathway-level GapMind analysis with gene-level eggNOG analysis for comprehensive coverage. [src: essential_metabolome]
- Mapping essential genes directly to metabolic pathways rather than relying on GapMind. [src: essential_metabolome]

The report also leaves open three questions:
- Are pathways predicted complete actually essential for viability? [src: essential_metabolome]
- Which pathways are essential only under specific growth conditions? [src: essential_metabolome]
- Do pathway gaps cluster by phylogeny or ecology? [src: essential_metabolome]

## [[summaries/euk_in_prok_correlates__REPORT|Metadata Correlates of Eukaryotic Contamination in NMDC Prokaryote-Targeted Metagenomes]]

### Limits

- Only GOTTCHA2 can estimate eukaryotic reads here. [src: euk_in_prok_correlates] Its values are database-dependent and should be read as relative/ordinal, not calibrated absolute contamination. [src: euk_in_prok_correlates]
- Study and batch confounding blocks any cross-study environment claim. [src: euk_in_prok_correlates]
- NMDC's read-based taxonomy spans only ~9 studies, with one soil study at ≈43% of runs, so the cross-study generalization test is under-powered. [src: euk_in_prok_correlates]
- The data-landscape scan found no on-system source with per-sample eukaryotic read fraction across many studies. MGnify is a MAG (metagenome assembled genomes) catalog, SPIRE/GEM/Tara are MAG collections, and EMP (Earth Microbiome Project) is 16S. [src: euk_in_prok_correlates]
- The within-study result is demonstrated for one soil study only and may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]
- Even within the study, env_local_scale and geography may track sampling-campaign sub-batches, so within-study control is not randomized. [src: euk_in_prok_correlates]
- NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method or library-prep fields, so wet-lab factors cannot be tested. [src: euk_in_prok_correlates] Processing booleans in biosample_to_workflow_run are near-constant, with has_filtration all false. [src: euk_in_prok_correlates] Host depletion and extraction kit, the strongest literature levers, remain in the unmeasured residual. [src: euk_in_prok_correlates]
- 1,067 of 2,759 runs pool multiple biosamples and inherit metadata from a single representative biosample (MIN(biosample_id)). [src: euk_in_prok_correlates] Differing local metadata injects predictor label noise, a conservative bias that can only weaken associations, not manufacture them. [src: euk_in_prok_correlates]

### Proposed next analyses

- Break the batch confound with more studies, for example the SPF corpus (136K metagenomes / thousands of studies) or a broader collection, to enable a properly powered cross-study analysis. [src: euk_in_prok_correlates]
- Extend the within-study design to aquatic and plant-associated studies to test whether the vegetation/geography effect generalizes beyond soil. [src: euk_in_prok_correlates]
- Test whether the algal-plastid versus root-fungal source split holds within batch-controlled cohorts. [src: euk_in_prok_correlates]
- Acquire wet-lab metadata (extraction kit, host-depletion method, size fraction) to test the strongest literature levers that NMDC omits. [src: euk_in_prok_correlates]
- Calibrate GOTTCHA2 eukaryotic fraction against a spike-in or SPF estimate to move from ordinal to calibrated estimates. [src: euk_in_prok_correlates]

## [[summaries/field_vs_lab_fitness__REPORT|Field vs Lab Gene Importance in *Desulfovibrio vulgaris* Hildenborough]]

- ENIGMA CORAL holds 4,346 field samples with uranium and metals geochemistry across 596 Oak Ridge locations, and 213,044 amplicon sequence variants (ASVs) for community composition. [src: field_vs_lab_fitness] The report considers these potentially useful for future analyses but not for gene-level fitness analysis. [src: field_vs_lab_fitness]
- Essential genes are excluded from the fitness analysis because they have no fitness data. [src: field_vs_lab_fitness]
- The heavy-metals and lab-antibiotic results are not significant, and the lab-antibiotic dip at -2 reflects a small sample. [src: field_vs_lab_fitness]
- The single-organism scope limits generalizability, particularly to organisms with larger accessory genomes. [src: field_vs_lab_fitness]
- The *Nitratidesulfovibrio vulgaris* pangenome has relatively few genomes. This gives a coarse core/auxiliary classification and a high baseline core fraction (76.3%) that compresses effect sizes. [src: field_vs_lab_fitness]
- The field-specific and lab-specific gene sets are small (n=50-52), which limits statistical power for the key comparison. [src: field_vs_lab_fitness]
- Condition classification involved subjective judgment on edge cases, and gene length is confounded with both fitness measurement quality and core status. [src: field_vs_lab_fitness]
- Proposed next step: apply the field versus lab classification to other ENIGMA organisms with Fitness Browser data, such as *Pseudomonas* FW300 strains, to test whether the pattern generalizes. [src: field_vs_lab_fitness]
- Proposed next step: replace binary core/auxiliary status with the fraction of genomes carrying the gene cluster, to increase statistical power. [src: field_vs_lab_fitness]
- Proposed next step: use the 213K ASVs and 4,346 field samples in ENIGMA CORAL to ask whether *Desulfovibrio* abundance at Oak Ridge sites correlates with the geochemistry conditions tested in the Fitness Browser. [src: field_vs_lab_fitness]
- Proposed next step: examine whether antibiotic and heavy-metal resistance genes in the accessory genome are on mobile elements, recently acquired, or shared with co-occurring Oak Ridge species. [src: field_vs_lab_fitness]
- Proposed next step: use continuous fitness scores, such as mean or minimum fitness per condition class, instead of binary important/not-important status as logistic-regression predictors. [src: field_vs_lab_fitness]

## [[summaries/fitness_effects_conservation__REPORT|Fitness Effects vs Conservation -- Quantitative Analysis]]

- The 16-point gradient is statistically robust, but fitness importance only weakly predicts conservation. [src: fitness_effects_conservation]
- Lab conditions favour rich media and standard stresses, so many ecological niches are unrepresented. [src: fitness_effects_conservation]
- Fitness is measured for single-gene knockouts, so epistatic interactions are not captured. [src: fitness_effects_conservation]
- The 43 bacteria are mainly Proteobacteria, which limits generalizability. [src: fitness_effects_conservation]
- Singleton or novel genes may lack fitness data because of poor transposon coverage rather than true neutrality. [src: fitness_effects_conservation]

## [[summaries/fitness_modules__REPORT|Pan-bacterial Fitness Modules via Independent Component Analysis]]

- Organisms with fewer than ~100 experiments give weaker modules. Caulo, with 198 experiments, showed only 2.9x correlation enrichment. [src: fitness_modules]
- The component cap (components <= 40% of experiments) avoids FastICA convergence failures but may miss modules in low-experiment organisms. [src: fitness_modules]
- Proposed next steps are to extend to more organisms as new RB-TnSeq datasets appear. [src: fitness_modules] The report also proposes integrating module predictions with core, auxiliary and singleton pangenome classes. [src: fitness_modules] It would test which modules are enriched in accessory genes. [src: fitness_modules] It would also build a web interface for browsing module families and predictions. [src: fitness_modules]

## [[summaries/functional_dark_matter__REPORT|Functional Dark Matter — Experimentally Prioritized Novel Genetic Systems]]

This part of the report lists its contributions and the limits on them. The contributions are a unified catalog, a prioritized candidate list, lab-field concordance testing, cross-organism concordance, a darkness spectrum and organism-selection routes. [src: functional_dark_matter] Several of its validation results are partial or marginal. [src: functional_dark_matter]

### Claimed contributions

The report integrates 57,011 dark genes across 48 bacteria, drawing fitness, conservation, module, ortholog and domain data from 4 prior observatory projects that were previously fragmented across analyses. [src: functional_dark_matter] It combines 6 scored evidence axes into 100 ranked candidates with functional hypotheses and suggested experiments for the Arkin Lab and collaborators. [src: functional_dark_matter] Cross-organism fitness concordance reveals 65 ortholog groups with conserved phenotypes that could not be identified from any single organism. [src: functional_dark_matter]

The lab-field concordance framework connects lab fitness phenotypes to environmental biogeography via pangenome carrier analysis. [src: functional_dark_matter] It finds 61.7% concordance across 47 testable clusters. [src: functional_dark_matter] NMDC metagenomic correlations independently validated it, with 4/4 pre-registered predictions confirmed. [src: functional_dark_matter]

### Darkness spectrum and resource allocation

The darkness spectrum is a five-tier inventory, T1 Void through T5 Dawn, that quantifies each gene's darkness across 6 independent evidence axes. [src: functional_dark_matter] Only 7.5% of dark genes (4,273 T1 Void) are truly unknown with zero evidence. [src: functional_dark_matter] The largest group, 39.5% (T4 Penumbra), has 3–4 converging lines of evidence and is ready for targeted characterization. [src: functional_dark_matter] The report recommends confirmation for T5 Dawn genes [src: functional_dark_matter], targeted experiments for T4 Penumbra genes [src: functional_dark_matter] and broad screens for T1 Void genes. [src: functional_dark_matter]

### Organism selection

The dual-route covering set uses two complementary greedy weighted set-cover algorithms. [src: functional_dark_matter] Route A (evidence-weighted, NB09) selects 42 organisms optimized for genes with testable hypotheses. [src: functional_dark_matter] Route B (conservation-weighted, NB11) selects 42 organisms optimized for discovering functions of broadly conserved true knowledge gaps. [src: functional_dark_matter] The routes share 39 organisms but order them differently, reflecting different experimental strategies. [src: functional_dark_matter] An extended tractable list of 73 organisms (48 FB, the Fitness Browser, plus 25 literature-curated organisms from 3 additional phyla) offers a way to expand coverage beyond the Proteobacteria-dominated Fitness Browser. [src: functional_dark_matter]

### Validation strength and null controls

The NMDC validation is strong in raw significance but limited by compositional coupling. NMDC trait_features analysis (NB06 Section 3) confirmed all 7 pre-registered trait-condition predictions with FDR (false discovery rate) < 10⁻²¹. [src: functional_dark_matter] It also found 441/449 exploratory tests significant at FDR < 0.05. [src: functional_dark_matter] The report says this extreme significance likely reflects compositional coupling, because abundant genera contribute to both carrier abundance and community trait scores. [src: functional_dark_matter] The correlations show ecological co-occurrence, not causal gene-phenotype links. [src: functional_dark_matter]

NB10 adds partial null approximations:
- A sign test on 7/7 trait directions gives p = 0.0078. [src: functional_dark_matter]
- A sign test on 4/4 abiotic directions gives p = 0.0625. [src: functional_dark_matter]
- Fisher's combined probability across all 11 pre-registered tests gives p ≈ 0. [src: functional_dark_matter]
- An inflation factor of ~20× for exploratory tests (441/449 significant vs. 22.5 expected) quantifies the coupling. [src: functional_dark_matter]

A full permutation test shuffling sample labels remains future work and needs Spark access to raw per-sample matrices. [src: functional_dark_matter]

For lab-field concordance, the evidence is only marginal. NB10's binomial test (29/47 vs. p = 0.5) gives one-sided p = 0.072, with a Wilson score 95% CI (confidence interval) of [0.474, 0.742]. This indicates concordance marginally above chance. [src: functional_dark_matter] Fisher's combined probability across all 47 individual tests gives p = 0.031. [src: functional_dark_matter] A full null comparison using annotated accessory genes through the same biogeographic pipeline would further strengthen rejection of H0, but it requires Spark for carrier genome queries. [src: functional_dark_matter]

The NB06 concordance null control shows dark genes reach concordance indistinguishable from annotated genes, which supports H1. [src: functional_dark_matter] Equivalent null controls were not run for the biogeographic and lab-field concordance analyses. [src: functional_dark_matter]

### Limits of the data

- Environmental metadata are sparse. AlphaEarth embeddings cover only 28% of genomes (83K/293K), and NCBI isolation-source metadata are inconsistent, which limits biogeographic tests. [src: functional_dark_matter]
- NMDC validation works at genus level, mapping taxon columns to pangenome genera via ncbi_taxid, and may miss species-specific signals. [src: functional_dark_matter] Only 5 of 6 carrier genera matched. The high significance rate (76/105) likely reflects common genera such as *Pseudomonas* and *Klebsiella* dominating both datasets. [src: functional_dark_matter]
- The 57,011 dark-gene count likely overestimates truly uncharacterized genes, because databases not checked may annotate some hypothetical genes. [src: functional_dark_matter]
- The 6,691 module-based predictions from fitness_modules are guilt-by-association inferences, not direct experimental validation. [src: functional_dark_matter] The "high confidence" prioritization label reflects evidence convergence, not experimental proof. [src: functional_dark_matter]
- Condition coverage differs across organisms. Organisms with more conditions, such as MR-1 with 121, produce more specific phenotypes and so score higher. [src: functional_dark_matter]

### GapMind and gap-filling limits

GapMind covers amino acid biosynthesis and carbon utilization pathways but not all metabolic functions. [src: functional_dark_matter] The analysis misses dark genes with signaling, regulatory or structural roles. [src: functional_dark_matter] It identifies organism-level co-occurrence of pathway gaps and dark genes, not direct gene-to-step assignments. [src: functional_dark_matter] NB10 partly addresses this with curated pathway-enzyme domain matching (EC, Enzyme Commission, prefix, PFam family and keyword compatibility). It identifies 42,239 domain-compatible gene-pathway candidates, including 5,398 high-confidence EC matches. [src: functional_dark_matter] Full gene-to-step validation would need AlphaFold structure prediction or experimental enzymology. [src: functional_dark_matter]

### Essential genes

Of the 17,344 scored dark genes, 9,557 (55%) are essential, with no viable transposon mutants. [src: functional_dark_matter] None appear in the NB05 top 100. Essential genes have zero rows in genefitness, so fitness importance scores them at the essentiality bonus floor, and experimental tractability penalizes them as non-knockable. [src: functional_dark_matter] NB07 prioritizes them separately, using gene neighbors, phylogenetic breadth, cross-organism conservation, domains and CRISPRi (CRISPR interference) tractability. It produces 50 ranked candidates amenable to CRISPRi knockdown. [src: functional_dark_matter]

### Operon and neighborhood methods

NB07's operon predictions use a single-genome positional heuristic: a 5-gene window, same strand and a gap of ≤300 bp. [src: functional_dark_matter] NB08 adds cross-species synteny across 48 Fitness Browser genomes and co-fitness confirmation, but still falls short of industry-standard tools. [src: functional_dark_matter] For comparison, DOOR v2.0 uses intergenic distance, neighborhood conservation, phylogenetic distance and experimentally validated training sets across thousands of genomes. [src: functional_dark_matter] STRING v12 combines genomic neighborhood, gene fusion, phylogenetic co-occurrence, co-expression and text mining across >14,000 organisms. [src: functional_dark_matter]

- The eggNOG breadth classification does not discriminate among candidates, because 99.9% of dark gene clusters (30,721 of 30,756) map to universal breadth. [src: functional_dark_matter]
- A species-count metric correlates with the original ranking (Spearman ρ = 0.982), but top-50 overlap is 62%. [src: functional_dark_matter]
- K. oxytoca BWI76_RS15525 has FDR 0.069 and P. putida N2C3 AO356_24150 has FDR 0.178, so these enrichments are not significant at 0.05. [src: functional_dark_matter]
- Genomic-proximity hypotheses are leads, and DOOR and ProOpDB use signals beyond strand and gap distance. [src: functional_dark_matter]
- STRING v12 and EFI-GNT analyze thousands of genomes with more sophisticated scoring. [src: functional_dark_matter]

## [[summaries/fw300_metabolic_consistency__REPORT|Metabolic Consistency of Pseudomonas FW300-N2E3 Across Four KBase Data Lakehouse Databases]]

- Only 21 of 58 metabolites were testable, and 37 (64%) were seen only in WoM. [src: fw300_metabolic_consistency] Only 3 had four-way coverage, and the untested 64% may hold additional discordances. [src: fw300_metabolic_consistency]
- The report describes the high concordance as largely structural, because FB (21/21 = 100%) and GapMind (13/13 = 100%) are invariably concordant with WoM production. [src: fw300_metabolic_consistency]
- The BacDive comparison rests on 7 matched metabolites, and the 43% rate did not differ significantly from the species baseline. [src: fw300_metabolic_consistency]
- Trehalose, lysine and glycine have small BacDive samples, so only tryptophan is a high-confidence discordance. [src: fw300_metabolic_consistency] The report states that only tryptophan has sufficient BacDive data for a confident conclusion, and it gives n=52 for this statement. [src: fw300_metabolic_consistency] The report does not explain how this n=52 relates to the 50 strains in the tryptophan comparison above. [src: fw300_metabolic_consistency] Sample-size-based scoring shows many BacDive discordances are data-limited. [src: fw300_metabolic_consistency]
- BacDive compound coverage varies from 1 to 51 strains under per-strain consensus, and raw records can be higher because of duplicates. [src: fw300_metabolic_consistency]
- Using BacDive consensus without sample size can produce false discordance calls. [src: fw300_metabolic_consistency] Strain variation, such as trehalose at 1/6 positive, means species consensus may not reflect FW300-N2E3's capabilities. [src: fw300_metabolic_consistency]
- Two FB matches were approximate; excluding them changed little. [src: fw300_metabolic_consistency]
- Low matching rates reflect nomenclature and scope differences. [src: fw300_metabolic_consistency]
- WoM used R2A rich medium, whereas FB used minimal medium with single C/N sources, so some WoM metabolites may only be produced on rich media. [src: fw300_metabolic_consistency]
- The planned NB04 mapping of fitness genes to GapMind pathway steps was deferred. It would strengthen the mechanistic interpretation of the tryptophan overflow hypothesis. [src: fw300_metabolic_consistency]
- The report notes that no published study has systematically compared WoM exometabolomic profiles with FB gene fitness data, despite their shared ENIGMA/Arkin Lab origin. [src: fw300_metabolic_consistency]

Next analyses the report proposes:
- Pathway-level analysis (NB04) to learn whether tryptophan fitness genes are biosynthetic, catabolic or regulatory, which would distinguish overflow metabolism from active catabolism. [src: fw300_metabolic_consistency]
- Repeating the analysis in other ENIGMA isolates, such as *Pseudomonas stutzeri* RCH2, to test whether the pattern is species-specific or general. [src: fw300_metabolic_consistency]
- Using InChIKey and CHEBI identifiers instead of name matching to expand WoM–BacDive overlap beyond 8 metabolites. [src: fw300_metabolic_consistency]
- Using the tryptophan finding to parameterize a community metabolic model of cross-feeding with tryptophan auxotrophs in the Oak Ridge groundwater community. [src: fw300_metabolic_consistency]
- Comparing WoM profiles across growth media to separate constitutive from medium-dependent production. [src: fw300_metabolic_consistency]

## [[summaries/gc_ecotype_ecology__REPORT|GC Content as an Ecological Signal Across Bacterial Ecotypes]]

- Seven species had all genomes collapse to a single ANI cluster and were dropped, and 108 species produced valid p-values. [src: gc_ecotype_ecology]
- The robustness tests cover fewer species than the primary test: 39 for phylogenetic regression and only 16 for the geographic test. [src: gc_ecotype_ecology]
- Some species have very few ANI clusters: Enterococcus faecium has only 2 among 1,633 genomes [src: gc_ecotype_ecology], and Streptococcus thermophilus has 5. [src: gc_ecotype_ecology] For these, connected-components control could partly reflect cluster-level confounds, and the phylogenetic-PCoA control mitigates this only for the subset retaining significance. [src: gc_ecotype_ecology] Such species need a stricter or alternative phylogenetic control before strong claims can be made. [src: gc_ecotype_ecology]
- The AlphaEarth–isolation agreement rests on only 17 jointly testable species. [src: gc_ecotype_ecology]
- Effect sizes are small in absolute terms. [src: gc_ecotype_ecology]
- The result is associational and observational. Without strain-replicate transplant experiments, hidden confounders such as geographic sampling bias correlated with isolation source cannot be excluded. [src: gc_ecotype_ecology]
- The permutation null rules out random label associations within species, but not all confounders. [src: gc_ecotype_ecology]
- Metadata are sparse: isolation_source is missing for ~16% of genomes and ~30% map only to "other". [src: gc_ecotype_ecology] The categorical scheme is coarse and conservative, and finer categories likely exist but were not extracted. [src: gc_ecotype_ecology] Sampling bias is substantial (57K clinical genomes versus 384 plant_microbiome). [src: gc_ecotype_ecology] Latitude/longitude coverage is ~28% globally. [src: gc_ecotype_ecology]
- The BH correction is appropriate for discovery, but per-species effect estimates are subject to selection bias if cherry-picked from the top. [src: gc_ecotype_ecology]
- The linear/categorical model does not capture possible nonlinear effects of environment on GC. [src: gc_ecotype_ecology] The AlphaEarth PCA plus Pearson analysis captures only linear monotone signals. [src: gc_ecotype_ecology]
- Only genome-level GC is analyzed. Within-genome heterogeneity (GC₃, gene-body versus intergenic, mobile elements) might amplify or contradict the genome-mean signal. [src: gc_ecotype_ecology]
- The mechanistic explanations above are candidates, not tested here. [src: gc_ecotype_ecology]
- The largest partial R² values come from species with many small ANI clusters, so they partly reflect the small residual variance left after control. [src: gc_ecotype_ecology]

## [[summaries/gene_copy_number_variation__REPORT|Gene Copy Number Variation Across Pangenome Functional Categories]]

- Copy-number analyses should stratify by is_core before inferring functional constraint, because an unstratified 8× effect becomes 2× within core and 5× within accessory. [src: gene_copy_number_variation]
- Clusters come from motupan at 90% AAI. Recent paralogs diverged <10% merge into one cluster and ancient paralogs diverged >10% appear as separate clusters, so the analysis captures operationally recognized rather than phylogenetically complete paralogs. [src: gene_copy_number_variation]
- Fragmented metagenome-assembled genomes (MAGs) can inflate or deflate multi-copy counts, and contig artifacts enter the per-cluster-per-genome metrics linearly. [src: gene_copy_number_variation] The report does not condition on checkm_completeness or contig N50 and says a robustness pass on the tightest-quality genome subset would strengthen the claim. [src: gene_copy_number_variation] It proposes restricting to checkm_completeness ≥ 95 and checkm_contamination ≤ 2 and rerunning NB03 to test whether fragmented assemblies inflate the L effect. [src: gene_copy_number_variation]
- The 24 species were selected for 50–300-genome coverage, which oversamples clinically important and well-studied taxa. [src: gene_copy_number_variation]
- The 5 phyla (Pseudomonadota, Bacillota, Bacteroidota, Actinomycetota, Campylobacterota) are the top 5 by candidate count, and candidate phyla radiation (CPR), Patescibacteria, Spirochaetota and archaea are left out. [src: gene_copy_number_variation]
- The Spirochaetota pilot species Borreliella burgdorferi was retained but flagged as a multi-partite-genome outlier. Plasmid-borne duplication raises housekeeping and adaptive rates together and breaks the direction test. [src: gene_copy_number_variation]
- Housekeeping {F, H} covers ~5% of species-level rows and adaptive {L, V, M, K} ~15%. [src: gene_copy_number_variation] Roughly 80% of clusters are "other" and excluded from the primary test, so extrapolating the class effect to all bacterial genes is not automatic. [src: gene_copy_number_variation]
- The report does not test direct positive selection on copy number. Its observations fit purifying selection against dosage imbalance for housekeeping paralogs, neutral tolerance for adaptive paralogs plus positive selection on some, or proximity to mobile elements. [src: gene_copy_number_variation] Distinguishing these needs dN/dS on paralog pairs and mobile-element context data. [src: gene_copy_number_variation]
- The three-way join (gene × gene_genecluster_junction × gene_cluster, ~1B rows each) took 140–290 s per species, median ~200 s. [src: gene_copy_number_variation] The 24-species pilot needs ~80 min. The report recommends CTS batch processing rather than a JupyterHub notebook loop for 100+ species. [src: gene_copy_number_variation] See [[entities/spark-extraction-of-per-species-pangenome-copy-counts]].
- A background jupyter nbconvert run of the Spark loop died silently after ~1.5 hr, leaving the notebook unchanged and only an intermediate CSV. [src: gene_copy_number_variation] The standalone resumable script streamed progress with print(flush=True) and finished within the same wall-clock budget. [src: gene_copy_number_variation]
- Per-phylum ratios rest on 4–5 species each. [src: gene_copy_number_variation]

### Proposed next analyses

- Split cluster L into IS-element loci (via bakta_amr or genomad_mobile_elements cross-reference, if available in the current KBase Data Lakehouse migration state) versus true DNA repair loci (recA, mutL, uvr*). [src: gene_copy_number_variation] If the effect concentrates in IS elements, the story becomes transposition-mediated copy-number variation rather than adaptive paralogy, which matters for the dosage-balance interpretation. [src: gene_copy_number_variation]
- Scale to 100–200 species for phylum-specific tests and to decompose the Pseudomonadota versus Campylobacterota effect-size difference, using CTS batch processing. [src: gene_copy_number_variation]
- Run a within-genome analysis on species with 200+ high-quality genomes, testing whether adaptive clusters have heavier-tailed copy-count distributions than housekeeping ones, since the current rate metric is between-genome. [src: gene_copy_number_variation]
- Cross-reference with the ~30 Fitness Browser–pangenome-linked species to ask whether paralog copy count correlates with fitness in relevant conditions. [src: gene_copy_number_variation] This would connect the copy-number story to the dosage-selection story of Elliott, Cuff & Neidle 2013. [src: gene_copy_number_variation]

## [[summaries/gene_function_ecological_agora__REPORT|Gene Function Ecological Agora]]

- Donor identification at deep ranks was deferred. Per-CDS sequence is not in the KBase Data Lakehouse queryable schemas, and composition-based donor inference would need external FASTA plus codon profiling, which the report says breaks the Phase 3 budget. [src: gene_function_ecological_agora]
- AleRax / ALE does not run at full GTDB scale. Four-quadrant labels exist only at genus rank for the Phase 3 candidate set (~10K KOs), not atlas-wide. [src: gene_function_ecological_agora]
- The cross-walk was demonstrated on PSII. PUL and mycolic analyses were deferred at scale because of a pandas spatial-merge out-of-memory failure. [src: gene_function_ecological_agora]
- Three pre-registration omissions were corrected: M2 dosage biology, M12 absolute-zero criterion and M14 misreading of Alm 2006. [src: gene_function_ecological_agora] Three reviewer-side fabrications were detected: Mendoza 2020 and Koech 2025 and a Burch 2023 PMID error. [src: gene_function_ecological_agora]
- The Cyanobacteria PSII genus-rank test was too sparse to evaluate. [src: gene_function_ecological_agora] The UniRef50 unit cannot aggregate to the HK family. [src: gene_function_ecological_agora]

## [[summaries/genotype_to_phenotype_enigma__REPORT|Genotype x Condition to Phenotype Prediction from ENIGMA Growth Curves]]

- Short strain names caused false matches: MT20 (Rhodanobacter glycinis) matched Streptococcus pneumoniae, injecting 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma] Authoritative taxonomy plus a genus-consistency check cut pangenome linkages from 32 to 20 and removed all false matches. [src: genotype_to_phenotype_enigma]
- The exometabolomic result rests on only 6 strains. [src: genotype_to_phenotype_enigma]
- The claim that resolving failures would raise accuracy from 65.1% toward a per-class ceiling of ~78% is a proposal, not a measured result. [src: genotype_to_phenotype_enigma]
- The pH-dependent growth difference between clusters is a hypothesis the report states for testing. [src: genotype_to_phenotype_enigma]

## [[summaries/harvard_forest_warming__REPORT|Harvard Forest Long-Term Warming — DNA vs RNA Functional Response]]

- The paired DNA/RNA subset confounds horizon with incubation, so the direct-only analysis is the cleaner test. [src: harvard_forest_warming]
- Omics coverage is unbalanced because the NMDC pipeline produced no metagenomes for organic-direct or some mineral-direct samples. This drives the H1 sensitivity caveat. [src: harvard_forest_warming] All organic-horizon DNA samples are lab-incubated, so incubation cannot be factored out cleanly there. [src: harvard_forest_warming]
- All samples come from a single date (2017-05-24), so RNA may carry non-warming noise. The design cannot detect seasonal effects, which Shinfuku et al. 2024 show are substantial at this site. [src: harvard_forest_warming]
- RNA-pool KO signals do not survive FDR. [src: harvard_forest_warming] Sample sizes (n=28 metagenome, n=39 metatranscriptome) limit per-KO FDR power across 12-14K KOs. [src: harvard_forest_warming]
- Metatranscriptome KO data from contig annotations measure transcript-pool composition, not TPM-quantified expression, and are biased by assembly quality. [src: harvard_forest_warming]
- Quantitative metabolomics, NOM and proteomics are excluded because nmdc_arkin tables are excluded. Equivalent layers exist in nmdc_arkin.{nom_gold, metabolomics_gold, proteomics_gold}. [src: harvard_forest_warming]
- abiotic_features are all zeros, from an NMDC parsing artifact, so no soil temperature, pH or nitrogen data exist in the KBase Data Lakehouse. The +5°C label is the only environmental contrast. [src: harvard_forest_warming]
- The report notes that its verdict does not exclude an early transient RNA lead. [src: harvard_forest_warming]

The report proposes these next analyses:
- Add nmdc_arkin quantitative NOM, metabolomics and proteomics layers to strengthen H2. It calls quantitative SOM chemistry the most direct complement to its gene-level findings. [src: harvard_forest_warming]
- Resolve ChEBI labels for the top differential metabolite hits with an ontology resolver, and run pathway enrichment against KEGG modules. [src: harvard_forest_warming]
- Run a cross-study meta-analysis with NMDC SPRUCE peatland (nmdc:sty-11-33fbta56) and Alaskan permafrost thaw (nmdc:sty-11-db67n062) to test whether the methanotrophy-up signature reproduces across sites. [src: harvard_forest_warming]
- Identify which MAGs in the 298-MAG cohort carry the upregulated pmoA/pmoB, and test whether they are USCα methanotrophs or distributed across phyla. [src: harvard_forest_warming]
- Test the hypothesis that warming activates a ruderal community subset characterized by Actinobacteria, glyoxylate-cycle-active organisms and methanotrophy, using Choudoir et al. 2025 pangenome data. [src: harvard_forest_warming]

## [[summaries/ibd_phage_targeting__REPORT|Metagenome-Prioritized Phage Cocktails for Crohn's Disease and IBD]]

The report states limits on statistical independence. [src: ibd_phage_targeting] It also states limits on the cross-feeding hypothesis. [src: ibd_phage_targeting] Further limits cover the iron-siderophore comparator [src: ibd_phage_targeting], phage availability [src: ibd_phage_targeting], the small UC Davis cohort [src: ibd_phage_targeting] and the calprotectin threshold. [src: ibd_phage_targeting]

### Statistical independence and weak replication

CLR-MW and LinDA both use the same ecotype-defined subsamples. They share a selection-on-outcome bias, so bootstrap stability does not remove feature leakage. [src: ibd_phage_targeting] Only the within-substudy CD-vs-nonIBD contrast is an independent evidence source. This is why the NB04d Tier-A gating requires within-substudy concordance. [src: ibd_phage_targeting] See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

Pillar 2 cross-cohort replication is weak. The Tier-A list, especially E3, should be treated as hypotheses for experimental validation, not established targets. The UC Davis cocktail drafts inherit this limitation. [src: ibd_phage_targeting]

### Cross-feeding hypothesis not supported

Paired sample-level metabolite-metagenomic data (NB09c) do not support the NB07c cross-feeding hypothesis. [src: ibd_phage_targeting] Only 7 strict cross-feeding triangles emerge. Lactate × Anaerostipes caccae (+0.18) has the opposite sign to lactate × Flavonifractor plautii (-0.23) and lactate × Enterocloster bolteae (-0.20). That is inconsistent with a lactate-mediated loop. [src: ibd_phage_targeting] The report reads the NB07c coupling as shared-environment co-occurrence in healthy or normobiotic samples. [src: ibd_phage_targeting] It infers that phage targeting of pathobionts is unlikely to substantially deplete A. caccae through metabolic coupling. [src: ibd_phage_targeting] See [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]].

The E3_CD module couples more weakly than E1_CD. Its two oral Actinomyces anchors couple only weakly (~ρ=0.17–0.19) to module pathobionts. [src: ibd_phage_targeting] The NB07c cocktail-design implication is therefore E1-specific. UC Davis E3 patients (31 % of the cohort) may need a different module-anchor framework. [src: ibd_phage_targeting]

### Iron-siderophore signature

The narrowing of the iron theme to Escherichia coli is correlation-based. It uses species-by-pathway Spearman ρ across CMD_IBD samples. [src: ibd_phage_targeting] The v1.8 analysis found that 8 of 15 iron pathways were menaquinol biosynthesis, which is not strictly E. coli-specific. [src: ibd_phage_targeting] The strongest signature pathways, ENTBACSYN-PWY and HEMESYN2-PWY, are E. coli-canonical. [src: ibd_phage_targeting] NB08a adds direct genomic evidence. E. coli alone among actionable Tier-A core species carries iron-siderophore MIBiG matches, with 54 BGCs (biosynthetic gene clusters) versus 0 in the other 5 actionable species. [src: ibd_phage_targeting] See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

Several limits apply:
- HUMAnN3 species-stratified attribution needs raw reads and was dropped per plan v1.9. NB08a genomic BGC content is the substitute within the no-raw-reads scope. [src: ibd_phage_targeting]
- The strict H3c species-by-BGC interaction test remains untested and was dropped per plan v1.9. [src: ibd_phage_targeting]
- NB08a Test 3 uses the ref_cborf_enrichment CD-vs-HC main-effect table. Its CB-ORF CD-up enrichment cannot separate an interaction from species and BGC main effects. [src: ibd_phage_targeting]
- The interaction test needs raw-read-dependent species-stratified per-sample BGC abundance. The report calls the drop a structural scope limitation, not a deferred follow-up. The operational NB08a test is main-effect-only. [src: ibd_phage_targeting]
- The Tier-A background comparator is the full catalog of 10,060 BGCs across all species, not a matched comparator. [src: ibd_phage_targeting]
- The Fisher odds ratio (OR) of 44× for iron_siderophore is partly inflated by the catalog-wide rarity of iron MIBiG matches (51 / 9,774 = 0.5 %). It should not be read as a precise effect size. [src: ibd_phage_targeting]
- The report proposes a more conservative matched-niche comparator. It would combine gut Proteobacteria and CD-associated Firmicutes at similar genome-assembly depth. [src: ibd_phage_targeting]
- The report states that the qualitative E. coli-only signature is robust across comparator choices. [src: ibd_phage_targeting]

### Phage availability

The report names INPHARED and IMG/VR queries as the highest-priority external extension before clinical translation. Its internal-only scope excludes them. [src: ibd_phage_targeting] See [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]].

The E1 patient cocktail draft is a hybrid 3-strategy framework, not a pure phage cocktail. The report calls this a structural property of gut-anaerobe phage availability. [src: ibd_phage_targeting]

PhageFoundry holds 96 phages × 188 E. coli strains × 17,672 susceptibility pairs. The report calls this sufficient for a 5-phage AIEC (adherent-invasive E. coli) cocktail at 95 % strain coverage. [src: ibd_phage_targeting] The other 5 actionable Tier-A species are not in phagefoundry_strain_modelling. Their phage availability rests on ref_phage_biology literature curation alone. [src: ibd_phage_targeting] The 95 % figure applies to the 188 PhageFoundry-tested strains, not UC Davis patient isolates. Patient applicability needs AIEC strain-resolution diagnostics on stool isolates, queued in the NB17 near-term roadmap. [src: ibd_phage_targeting]

### HMP2 viromics

HMP2 viromics has 80 % Unknown family classification, so most phage observations cannot be linked to a target host. [src: ibd_phage_targeting] The E. coli correlations with Podoviridae (+0.18) and Myoviridae (+0.13) are restricted to the classifiable 20 %. [src: ibd_phage_targeting] Better resolution needs VirMAP/MARVEL reruns with newer phage reference databases, which is out of scope. [src: ibd_phage_targeting]

NB14 phageome effect sizes with ecotype and diagnosis are modest (max |ρ|≤0.18). The phageome is a noisier channel than species taxonomy, where NB04e effect sizes routinely have |CLR-Δ|>1.0. [src: ibd_phage_targeting] The 3-layer phage-evidence convergence rests on directional concordance, not matched effect sizes. [src: ibd_phage_targeting]

### UC Davis cohort and clinical translation

The 23-patient UC Davis cohort is small. Per-patient cocktail recommendations are exemplars or templates, not statistically robust validation. Generalization needs multi-center validation. [src: ibd_phage_targeting] The operational strategy distribution is 12 reserve / 4 E1 hybrid / 4 E0 limited / 1 E1 full / 1 E3 / 1 state-dependent. It should be revisited in a larger CD cohort. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

- **Bile acids:** The cohort has no per-patient bile-acid measurements. The F. plautii bile-acid-coupling-cost annotation is ecotype-level evidence from paired HMP2 samples. [src: ibd_phage_targeting] Clinical translation requires per-patient bile-acid panels for monitoring and dosing. [src: ibd_phage_targeting]
- **AIEC diagnostics:** The cohort has no per-patient AIEC strain-resolution diagnostic. Eight of 23 patients carry detectable E. coli by Kaiju. The 5-phage AIEC recommendation assumes AIEC-subset prevalence from Dogan 2014 / Dubinsky 2022. [src: ibd_phage_targeting] Per-patient genotyping for pks-island, Yersiniabactin and Enterobactin is a near-term prerequisite. [src: ibd_phage_targeting]
- **Dosing rules:** The state-dependent dosing rule is n=1. Patient 6967 is the only multi-timepoint patient with biological-replicate samples. [src: ibd_phage_targeting] The 5 dosing rules and the clinical workflow are mechanistically interpretable through ecotype biology and per-ecotype module structure. Prospective validation needs expanded longitudinal sampling. [src: ibd_phage_targeting]
- **Patient 1112:** Its technical-replicate Spearman ρ=1.000 validates the technical-noise floor. It is not a biological-replicate trajectory. [src: ibd_phage_targeting]
- **Timing:** Visit timing and the duration of patient 6967's E1→E3 drift are unknown. The 3-6 month re-test interval is a clinical-convention default, not derived from data. [src: ibd_phage_targeting]
- **M. gnavus qPCR proxy:** It is a hypothesis. The 14× expansion in patient 6967's E3 transition suggests a 5-fold trigger for full ecotype re-testing, but it comes from a single trajectory. [src: ibd_phage_targeting] Validation needs a prospective cohort with paired qPCR and metagenomics across timepoints. [src: ibd_phage_targeting]
- **Cocktail Jaccard 0.60:** Its generalizability is unknown. Whether 3-of-5 component overlap warrants redesign depends on patient-response heterogeneity, which is outside project scope. [src: ibd_phage_targeting]
- **Calprotectin threshold:** NB17 splits active from quiescent patients at 250 μg/g. This clinical convention is not validated against per-patient response. [src: ibd_phage_targeting] Some patients at 41–248 μg/g, currently C_quiescent, may benefit from an active cocktail. The threshold should be re-evaluated in a pilot. [src: ibd_phage_targeting]

- NB09d's metabolite-ecotype failure concerns cross-cohort portability specifically. Within-cohort metabolite ecotypes might still serve single-laboratory translation. [src: ibd_phage_targeting]
- NB11 aggregates by subject, which loses longitudinal information. Mixed-effects regression might add power, but unbalanced visit counts complicate interpretation. [src: ibd_phage_targeting]
- The F. plautii bai-operon presumption is not directly tested: the CD signal is read as abundance, not strain dominance. [src: ibd_phage_targeting]
- Patient 6967 is the only multi-timepoint UC Davis CD patient with biological replicates. [src: ibd_phage_targeting] The M. gnavus qPCR proxy rests on that single patient and stays a hypothesis. [src: ibd_phage_targeting]
- The mean-per-module statistic is diluted by modules that contain 0 Tier-A hits by construction. [src: ibd_phage_targeting]
- The E3 Tier-A list is provisional and single-study. [src: ibd_phage_targeting]

## [[summaries/lab_field_ecology__REPORT|Lab Fitness Predicts Field Ecology at Oak Ridge]]

16S amplicon data resolves to genus level only, so species/strain-level matching to FB organisms is not possible. [src: lab_field_ecology]

The 108 overlapping samples may not capture the full range of Oak Ridge geochemistry. [src: lab_field_ecology]

The metal tolerance score is a crude aggregate; condition-specific fitness scores (e.g., uranium-only) would be more informative. [src: lab_field_ecology]

Community data include multiple communities per sample (different filter sizes, replicates), which were aggregated. [src: lab_field_ecology]

Only 12 FB genera have enough data for the metal tolerance correlation, limiting statistical power. [src: lab_field_ecology]

Confounding variables (pH, dissolved oxygen, carbon sources) are not controlled for. [src: lab_field_ecology]

### Next analyses proposed by the report

- Species-level resolution: use metagenomic data, if available in ENIGMA CORAL genome/assembly tables, instead of 16S amplicons to match FB organisms at species or strain level. [src: lab_field_ecology]
- Multivariate analysis: use CCA (canonical correlation analysis) or RDA to model community composition from multiple geochemical variables at once, controlling for pH, redox, and carbon sources. [src: lab_field_ecology]
- Condition-specific fitness: compute per-metal fitness scores (e.g., uranium-specific, chromium-specific) instead of an aggregate stress tolerance, and correlate them with the corresponding metal concentrations at each site. [src: lab_field_ecology]
- Temporal analysis: the ENIGMA samples span multiple dates, so test whether community changes over time track geochemical changes. [src: lab_field_ecology]
- Rhodanobacter: add it to the Fitness Browser, since it dominates contaminated wells but is absent from the FB. [src: lab_field_ecology]

## [[summaries/lanthanide_methylotrophy_atlas__REPORT|Lanthanide Methylotrophy Atlas — Distribution and Environmental Context of REE-Dependent Methanol Oxidation Across 293K Genomes]]

- The REE-impacted enrichment is descriptive only, because n=37 is too small to clear the FDR threshold. [src: lanthanide_methylotrophy_atlas]
- H3b falls just under its pre-registered threshold. [src: lanthanide_methylotrophy_atlas]
- 897 xoxF genomes (24 %) lack PQQ evidence from either source. The candidate explanations are assembly incompleteness, pseudogenization or reliance on community-acquired PQQ. Telling them apart needs sequence-level inspection, which the report leaves out of scope. [src: lanthanide_methylotrophy_atlas]
- Source choice matters. eggNOG lanM calls are false positives, and bakta over-calls pqqA-E. [src: lanthanide_methylotrophy_atlas]

## [[summaries/lignin_community_enrichment__REPORT|Lignin Enrichment and Ecological Memory in Microbial Communities]]

Fungal replicates agree poorly. Within-group Bray-Curtis distances reach 0.99–1.00 for several Round 2 groups, against 0.09 for 16S, which limits statistical inference for ITS. [src: lignin_community_enrichment] This tempers the fungal results above, which are best read as descriptive.

With n=3 per group, pairwise Mann-Whitney U tests cannot go below p=0.10, because only 10 permutations exist for 3 vs 3. Individual OTUs therefore cannot reach FDR-corrected significance. [src: lignin_community_enrichment] Pairwise PERMANOVA on 3 vs 3 samples has the same floor of about p=0.10. [src: lignin_community_enrichment] Global tests, meaning Kruskal-Wallis across all 7 groups and global PERMANOVA, reach significance because they pool more samples. [src: lignin_community_enrichment] The report names the Round 2 factorial PERMANOVA (n=12) as its most powered test. It gives p=0.002 for Round 1 history and p=0.018 for Round 2 carbon source. [src: lignin_community_enrichment] Effect sizes (CLR differences and R²) stay interpretable when p-values are constrained. [src: lignin_community_enrichment]

## [[summaries/metabolic_capability_dependency__REPORT|Metabolic Capability vs Metabolic Dependency]]

- Threshold sensitivity: varying the active threshold ±25% (1.5–2.5) and the latent threshold ±25% (0.75–1.25) gave latent fractions of 4.7% to 21.1% (SD = 5.9 percentage points across 16 threshold combinations). [src: metabolic_capability_dependency] The large intermediate zone (32.3%) makes the latent fraction moderately sensitive to tightening. [src: metabolic_capability_dependency]
- The qualitative conclusion held across the full range tested: a non-trivial fraction of complete pathways is fitness-neutral, with carbon pathways most affected. [src: metabolic_capability_dependency]
- Condition dependence: carbon pathways such as deoxyribose or ethanol utilization may be encoded but never activated in the lab. They can then appear latent despite ecological importance. [src: metabolic_capability_dependency] Laboratory-biased fitness experiments may inflate the latent fraction, because lab media may not reflect the full range of conditions under which pathways are expressed. [src: metabolic_capability_dependency]
- Coarse conservation measure: it does not detect partial gene erosion, meaning individual gene deletions within an otherwise complete pathway. [src: metabolic_capability_dependency] Evolutionary lag is proposed as a further reason: ongoing Black Queen gene loss may be undetectable in current genome sampling, so mid-loss capabilities still appear conserved at species level. [src: metabolic_capability_dependency]
- Sampling: fitness experiments cover only 48 organisms, so untested organisms in the same species clade may inflate apparent conservation of complete pathways. [src: metabolic_capability_dependency] The 48 organisms are a small fraction of the 293,000 genomes with pathway predictions, so results may not generalize to all taxonomic groups. [src: metabolic_capability_dependency]
- SEED-proxy noise: mapping GapMind pathway membership through SEED subsystems adds false positives from related subsystems that dilute the fitness signal and may misclassify pathways. [src: metabolic_capability_dependency] A direct mapping using GapMind gene assignments would improve precision. [src: metabolic_capability_dependency]
- The ecotype analysis is observational. Environment-cluster links in *Salmonella* and *Phenylobacterium* suggest ecological selection, but phylogenetic confounding is possible without explicit correction. [src: metabolic_capability_dependency]
- Organism-to-clade matching failed: the NB02 attempt to link Fitness Browser organisms to GapMind species clades through NCBI taxonomy IDs in `kbase_ke_pangenome.gtdb_metadata` returned zero matches, because the column held boolean strings rather than numeric taxids. [src: metabolic_capability_dependency] Downstream analyses therefore use organism-level fitness aggregates without clade-level linkage, which may reduce the precision of the H2a conservation comparison. [src: metabolic_capability_dependency]
- Coverage: the GapMind deoxyribonate and myoinositol pathways had no matching SEED role descriptions and are absent from all analyses. [src: metabolic_capability_dependency]
- Full-name phenylalanine and tyrosine entries also lacked SEED coverage, but their phe and tyr equivalents were included by abbreviation matching. [src: metabolic_capability_dependency]
- Alanine appears in fitness metrics but was excluded from classification for all organisms, because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [src: metabolic_capability_dependency]

The report proposes these next analyses:
- Replace pathway-level conservation with per-gene dN/dS or gene presence/absence across a phylogeny, to test progressive gene loss directly. [src: metabolic_capability_dependency]
- Use GapMind per-step gene assignments instead of SEED proxies, to improve mapping precision and reduce false positives. [src: metabolic_capability_dependency]
- Identify lineages with recent gene loss (singleton or auxiliary pangenome genes) in latent pathways, and verify actual deletion events in the phylogeny. [src: metabolic_capability_dependency]
- Supplement NCBI isolation source with BacDive or GTDB environmental labels, to improve the ecotype-environment test. [src: metabolic_capability_dependency]
- Test whether organisms with higher latent fractions more often encode public-goods pathways or co-occur with cross-feeding partners in community datasets. [src: metabolic_capability_dependency]

## [[summaries/metal_cross_resistance__REPORT|Gene-Resolution Metal Cross-Resistance Across Diverse Bacteria]]

- Different experiments used different metal concentrations, so dose-response effects could influence cross-resistance estimates. [src: metal_cross_resistance]
- Organisms range from 3 to 112 metal experiments, affecting the reliability of per-organism matrices. [src: metal_cross_resistance]
- Phylogenetic non-independence and the underpowered BacDive validation are described above. [src: metal_cross_resistance]
- The absence of non-metal stress controls is described above. [src: metal_cross_resistance]

The report proposes these next steps:

- Pangenome-scale H3 validation across 27K species using the Metal Fitness Atlas KEGG/PFAM mapping, checked against BacDive polymetallic isolation environments. [src: metal_cross_resistance]
- PGLS or phylogenetic PCA (principal component analysis) to control for phylogenetic non-independence. [src: metal_cross_resistance]
- Normalizing fitness effects by metal concentration relative to MIC. [src: metal_cross_resistance]
- Applying ICA (independent component analysis) from the fitness_modules project to metal conditions, to test whether cross-resistance genes cluster into coherent regulatory units. [src: metal_cross_resistance]
- Using AlphaFold structures to test whether metal binding sites or membrane interfaces in metal-shared proteins explain multi-metal sensitivity. [src: metal_cross_resistance]

## [[summaries/metal_fitness_atlas__REPORT|Pan-Bacterial Metal Fitness Atlas]]

- Cadmium and uranium show no significant core enrichment, which the report attributes likely to limited organism coverage. [src: metal_fitness_atlas]
- The 9 organisms without FB-pangenome links are excluded from the conservation analysis. [src: metal_fitness_atlas]
- There is no dose-response normalization. Concentrations vary across organisms (nickel 0.01-2.0 mM), and fitness effects depend on concentration relative to each organism's tolerance threshold. [src: metal_fitness_atlas]
- The metal-important definition (fit < -1 OR n_sick ≥ 1, ~3.3% of genes) is broad, and most such genes are general stress genes rather than metal-specific. [src: metal_fitness_atlas]
- Putatively essential genes (~14.3% of protein-coding genes, ~82% core) lack insertions and are excluded, so the observed core enrichment is a conservative estimate. [src: metal_fitness_atlas]
- Repertoire prediction failed validation: gene presence/absence does not predict metal tolerance, and a regulatory or expression-based model is needed. [src: metal_fitness_atlas]
- Predictions for unknown genes rest only on cross-species fitness data. [src: metal_fitness_atlas]
- Unnormalized pangenome scores reflect genome size rather than metal biology. [src: metal_fitness_atlas]
- The atlas scores 27,702 species but cannot validate predictions for organisms without RB-TnSeq libraries. [src: metal_fitness_atlas]
- No rare earth element experiments exist in the Fitness Browser, and Putida has no metal experiments. [src: metal_fitness_atlas]

Next analyses the report proposes:

- Repeat the conservation analysis using only genes important for metals but not other stresses, to separate the core stress response from metal-resistance gene evolution. [src: metal_fitness_atlas]
- Use PaperBLAST, InterPro and AlphaFold structural prediction on the 89 truly unknown and 43 DUF-domain families among the 149 novel candidates. [src: metal_fitness_atlas]
- Normalize fitness effects by metal concentration relative to MIC for fair cross-species comparison. [src: metal_fitness_atlas]
- Apply phylogenetic independent contrasts to control phylogenetic non-independence. [src: metal_fitness_atlas]
- Replace count-based pangenome metal scores with per-species hypergeometric enrichment tests controlling total functional annotation content. [src: metal_fitness_atlas]

Declined data-file and notebook inventory claims are omitted as file inventory.

## [[summaries/metal_resistance_global_biogeography__REPORT|Global Biogeography of Environmental Bacterial Metal Resistance]]

- Regional patterns cannot be interpreted until hotspot identification and sampling-effort correction are done. [src: metal_resistance_global_biogeography]
- Expedition-level clustering checks are pending for the Atacama and USA clusters. [src: metal_resistance_global_biogeography] The report plans to test whether the Atacama hotspot (OR=9.8) and the USA clusters are single-study artefacts by checking distinct sample_accession prefixes per hotspot. [src: metal_resistance_global_biogeography]
- The report has not yet confirmed that hotspots persist after normalising by log(n_MAGs). [src: metal_resistance_global_biogeography]
- The map cell has a NameError from a missing import of matplotlib.pyplot. [src: metal_resistance_global_biogeography] Fixing it in the NB01 map cell remains pending for the production figure. [src: metal_resistance_global_biogeography]
- Which biomes are most underrepresented in geospatial metadata is unresolved. [src: metal_resistance_global_biogeography]

## [[summaries/metal_specificity__REPORT|Metal-Specific vs General Stress Genes]]

- Seven of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) could not be processed. Their metal-important gene locusIds did not match the fitness matrix index format. [src: metal_specificity]
- The report notes 40.7% gene attrition: 5,229 gene records were excluded for locusId mismatches. The excluded organisms include the important model organisms Keio (Escherichia coli), MR1 (Shewanella) and ANA3, and the excluded genes may have different specificity profiles. [src: metal_specificity]
- The 24 included organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report considers the excluded organisms taxonomically diverse and does not expect systematic bias from their absence. [src: metal_specificity]
- Planned validation against the Fitness Browser specificphenotype table's built-in condition-specificity annotations was not completed. [src: metal_specificity]
- Genes absent from fitness data (~14%, ~82% core) bias all conservation estimates toward core enrichment. [src: metal_specificity]
- The 5% sick-rate threshold is arbitrary; exact fractions vary across 1-20%. [src: metal_specificity]
- The osmotic-overlap comparison with counter_ion_effects differs in threshold stringency. [src: metal_specificity]
- Proposed next steps: fix the integer-vs-string locusId format for the excluded organisms to recover the remaining 40% of gene records. [src: metal_specificity] Validate specificity against the specificphenotype table. [src: metal_specificity] Rerun the ICA module analysis with the atlas's pre-computed z-scores. [src: metal_specificity] Replicate the counter_ion_effects threshold (fit < -1 without |t| > 4) to validate the osmotic overlap. [src: metal_specificity] Use AlphaFold predictions to find metal-binding sites in UCP030820, YebC and DUF1043. [src: metal_specificity]

## [[summaries/microbeatlas_metal_ecology__REPORT|Metal Resistance Ecology — Phylogenetic Conservation vs. Environmental Selection]]

This part of the report interprets the metal-diversity and niche-breadth result and sets out its limits. It argues that the link is novel and survives several robustness checks. It also states that the evidence rests on inferred traits and uneven data, not on measured physiology. [src: microbeatlas_metal_ecology]

### Interpretation

The report says it is the first analysis to link genus-level metal type diversity, inferred from pangenome antimicrobial resistance (AMR) annotations across 6,789 species, to global niche breadth from a 464K-sample 16S atlas, with phylogenetic control by phylogenetic generalized least squares (PGLS). [src: microbeatlas_metal_ecology] It joins a pangenome database of 6,789 sequenced species across the GTDB bacterial tree with a global atlas of 98,919 OTUs (operational taxonomic units) × 463,972 samples. The report says this gives a taxonomic and geographic scope that site-specific studies lack. [src: microbeatlas_metal_ecology]

Earlier site-specific studies found generalist taxa enriched in metal-contaminated environments. They could not tell whether total gene burden, core resistance or breadth of metal type coverage was the relevant variable. [src: microbeatlas_metal_ecology] The global PGLS identifies metal type diversity, not gene count or core fraction, as the predictor of niche breadth. [src: microbeatlas_metal_ecology] Pagel's λ was 0.26–0.44 for AMR metrics and 0.79–0.91 for niche breadth. The report uses this to separate vertically inherited resistance repertoires from horizontally acquired accessory genes. [src: microbeatlas_metal_ecology] It concludes that the horizontally labile diversity component is the one that covaries with ecological range. [src: microbeatlas_metal_ecology]

### Niche-breadth measurement limits

MicrobeAtlas detection across 13 environment categories confounds habitat use with sampling intensity, V3–V4 or V4 primer bias, and uneven geographic and temporal SRA/ENA contributions. [src: microbeatlas_metal_ecology] Densely sampled soil, marine and plant environments can inflate apparent niche breadth relative to deep subsurface, brine and ice taxa. [src: microbeatlas_metal_ecology] Levins' B_std corrects for unequal environment sizes. It cannot correct for missing environments or differing detection probabilities. [src: microbeatlas_metal_ecology] Correcting primer bias and missing environments would need a multi-primer, multi-region survey design. [src: microbeatlas_metal_ecology]

Genus-level aggregation is a proxy. A genus may look broad-niched because different species occupy different habitats. [src: microbeatlas_metal_ecology] The PGLS β reflects covariation between inferred niche breadth and inferred metal tolerance capacity, not confirmed physiology. [src: microbeatlas_metal_ecology]

A stricter 5% within-environment prevalence threshold for B_std kept the positive direction (β = +0.017 vs +0.022 original). It reduced significance, because 37% fewer genera passed the filter. [src: microbeatlas_metal_ecology] The report concludes that rare transient detections do not explain the effect. [src: microbeatlas_metal_ecology]

### Aquatic category

MicrobeAtlas's 13 broad categories lump heterogeneous habitats. "Aquatic" combines marine, freshwater, estuarine, hydrothermal vent and pond environments. [src: microbeatlas_metal_ecology] A taxon found in both a marine coastal and a freshwater lake sample counts as broad-niched, although this could reflect related but ecologically distinct ecotypes. [src: microbeatlas_metal_ecology] Excluding aquatic gives p = 0.031, the weakest of all 13 exclusions but still significant. [src: microbeatlas_metal_ecology] Excluding any other environment gives p < 0.01, so the report states the result does not depend on the aquatic category. [src: microbeatlas_metal_ecology] Splitting aquatic into marine, freshwater and saline subcategories needs sample metadata re-analysis. That metadata is not available in the current KBase Data Lakehouse extraction. [src: microbeatlas_metal_ecology]

### Genome sampling depth

Sequenced genome count per genus correlates with inferred metal type diversity (Spearman r = 0.35, p = 2.6×10⁻¹⁹). [src: microbeatlas_metal_ecology] Single-genome genera have lower metal type counts than multi-genome genera (Mann-Whitney p = 5.1×10⁻¹⁰). [src: microbeatlas_metal_ecology] The result nevertheless survives several controls:

- With n_species_with_amr as a PGLS covariate, metal type diversity stays significant (β = +0.020, p = 3.4×10⁻⁴). [src: microbeatlas_metal_ecology] The linear pangenome-coverage covariate is borderline (p = 0.07), which the report reads as a modest, non-dominant sampling effect. [src: microbeatlas_metal_ecology]
- Rarefying to 1 species per genus over 200 iterations gives p < 0.05 in 89.5% of iterations, with median β (+0.015) in the same direction. [src: microbeatlas_metal_ecology]
- With z-scored log(n_species) as a covariate, metal types stay significant (p = 6.4×10⁻⁴). Log(n_species) is itself significant (p = 0.016), which confirms a log-linear genome-count effect. [src: microbeatlas_metal_ecology]
- Adding log(n_species) moves the metal type β from +0.021 to +0.020. The report reads this as a small confound with independent effects. [src: microbeatlas_metal_ecology]

A formal pangenome rarefaction curve over several species-per-genus thresholds would quantify the coverage-depth effect more precisely. [src: microbeatlas_metal_ecology] The report marks the genome-size covariate limitation as addressed by robustness analysis R5. [src: microbeatlas_metal_ecology]

### Archaea

Only 48 archaeal genera had both MicrobeAtlas representation (≥ 3 OTUs) and AMR data in kbase_ke_pangenome. [src: microbeatlas_metal_ecology] The archaeal PGLS gave a nonsignificant, positive metal-type coefficient (β = +0.0145, p = 0.467). Its standard errors exceed the coefficient, which the report attributes to severe underpowering, not a true null. [src: microbeatlas_metal_ecology] Power is 11% at α=0.05, so the report warns against reading the result as negative evidence. [src: microbeatlas_metal_ecology]

The report includes the result only to quantify the statistical gap, not as evidence for or against the hypothesis. [src: microbeatlas_metal_ecology] It says stricter readers may treat the section as a power-analysis appendix, not an attempted replication. [src: microbeatlas_metal_ecology] The 48 genera are biased toward cultured methanogens, halophiles and thermoacidophiles. They miss the environmentally dominant MicrobeAtlas archaea, including Thaumarchaeota and Woesearchaeota. [src: microbeatlas_metal_ecology] Adequate power needs ≥200 archaeal genera with AMR data, which requires expanded archaeal pangenome sequencing and annotation. [src: microbeatlas_metal_ecology]

### Trait distribution assumptions

Metal type diversity is an integer count from 1 to 7. The report uses it as a continuous z-scored predictor in a Gaussian PGLS. [src: microbeatlas_metal_ecology] The Gaussian assumption applies to the B_std residuals, not to the metal-type distribution. The report says PGLS residuals should be inspected for normality. [src: microbeatlas_metal_ecology]

If metal type count were the response, a Poisson or negative binomial PGLS would be appropriate (phylolm with Poisson family, or MCMCglmm). [src: microbeatlas_metal_ecology] The Pagel's λ analysis of metal_types assumes Brownian motion with Gaussian increments, which approximates an integer trait. [src: microbeatlas_metal_ecology] Discrete-state (Mk) or threshold models are alternatives, but they are not standard for this continuous-trait PGLS analysis. [src: microbeatlas_metal_ecology]

The evolutionary readings are interpretations. They are not direct tests of vertical versus horizontal inheritance. [src: microbeatlas_metal_ecology] The breadth-versus-depth conclusion rests on PGLS associations, not on experiments. [src: microbeatlas_metal_ecology]

## [[summaries/module_conservation__REPORT|Fitness Modules x Pangenome Conservation]]

- The baseline core rate of ~81.5% limits the maximum observable enrichment. The +4.5pp difference is significant but modest in absolute terms. [src: module_conservation]
- Only 29 of 32 module organisms are covered. Cola, Kang and SB2B lack pangenome links because their species had too few genomes in GTDB for pangenome construction. [src: module_conservation]
- The upstream membership threshold affects which genes are in a module and could influence conservation composition. [src: module_conservation]
- The 90% and 50% class cutoffs are arbitrary conveniences, not biologically motivated. [src: module_conservation]
- Essential genes are absent from modules by construction. [src: module_conservation]

## [[summaries/neon_mag_functional_discovery__REPORT|NEON Metagenome Lineage Novelty and Functional Ecology]]

This part of the report asks how far the NEON H4b result depends on the 173 MAGs (metagenome assembled genomes) that lack per-gene annotation tables. Four sensitivity estimators show the central claim holds except in one scenario the report calls unrealistic. The coverage gap itself is strongly habitat-biased, so the result generalizes only to a water-skewed sub-cohort. [src: neon_mag_functional_discovery]

### The coverage gap and its bias

The per-MAG re-analysis was limited because nmdc_results.annotation_kegg_orthology covers only 57% of NEON MetagenomeAnnotation workflows (1,799 / 3,137). [src: neon_mag_functional_discovery] The 73-MAG H4b cohort is a non-random 30% subset of the 246-MAG analysis target. Per-gene-table coverage is 100% for water genera and 0–30% for soil. [src: neon_mag_functional_discovery] Coverage and survival into the NB04b cohort fall together across habitat groups:

| Genus group | Coverage | NB04b outcome |
|---|---|---|
| Surface-water cyanobacteria (Planktothrix, Dolichospermum, Rubrivivax) | 100% | All 27 MAGs survived [src: neon_mag_functional_discovery] |
| Benthic generalists (Ferruginibacter, Flavobacterium, UBA953) | ~85% | 16 / 19 survived [src: neon_mag_functional_discovery] |
| Soil acidobacteria (Sulfotelmatobacter, Palsa-465, Palsa-1447) | ~30% | 12 / 40 survived [src: neon_mag_functional_discovery] |
| Soil cultured genera (Mycobacterium, Bradyrhizobium, Acidoferrum) | ~10% | 5 / 65 survived [src: neon_mag_functional_discovery] |
| Soil unculturable / novel (Acidocella, BOG-234, Pseudolabrys, Pseudonocardia, Reyranella) | 0% | 0 / 28 survived [src: neon_mag_functional_discovery] |

The report says the five fully attrited soil genera are the kind of MAGs that NB02 flagged as novel-lineage candidates. It thinks they most likely sit in workflows that NMDC has not yet fully processed into per-gene tables. [src: neon_mag_functional_discovery] The report records partial, habitat-biased annotation coverage as a generalizable pitfall in docs/pitfalls.md. [src: neon_mag_functional_discovery] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

### Four sensitivity estimators

To bound the dependence on the missing 173 MAGs, the report computed four estimators. [src: neon_mag_functional_discovery] The first three leave the result essentially unchanged. Only the worst case fails.

| Estimator | Median field-only KOs / MAG | Median Jaccard | Fraction of MAGs with ≥ 10 field-only KOs |
|---|---|---|---|
| Naive (observed only, n=73) | 371 [src: neon_mag_functional_discovery] | 0.43 [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Inverse-coverage-reweighted (effective n=218) | 319 [src: neon_mag_functional_discovery] | 0.43 [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Best-case imputation (missing MAGs = same-genus median) | 371 [src: neon_mag_functional_discovery] | not reported [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Worst-case (missing MAGs = 0 field-only) | 0 [src: neon_mag_functional_discovery] | not reported [src: neon_mag_functional_discovery] | 29.7% [src: neon_mag_functional_discovery] |

A bootstrap of 2,000 weighted resamples gave a 95% CI (confidence interval) of 180–384 on the reweighted median field-only KO (KEGG ortholog) count. This overlaps the naive 371 estimate. [src: neon_mag_functional_discovery] The report concludes that the claim of hundreds of accessory KOs absent from cultured pangenomes survives reweighting and best-case imputation with essentially no change. [src: neon_mag_functional_discovery] It places the realistic range for the missing cohort between the reweighted and best-case scenarios, and both fully support H4b. [src: neon_mag_functional_discovery] See [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes]].

### The worst-case failure

In the worst case, all 173 missing MAGs return zero field-only KOs. The fraction with ≥10 then falls to 29.7%, right at the pre-registered 30% falsification threshold. This is the only scenario where H4b fails. [src: neon_mag_functional_discovery] The report calls it biologically unrealistic. None of the 5 fully attrited soil genera is a known monoterpene-naïve or aldehyde-dehydrogenase-only lineage. Published Acidobacteriota genome content suggests they would carry substantial niche-specific accessory genes. [src: neon_mag_functional_discovery]

Even so, the H4b result generalizes only within a water-skewed sub-cohort. The report attributes the photosystem-heavy enrichment list to that bias, not to a unique feature of field-only KOs across all NEON MAGs. [src: neon_mag_functional_discovery]

### Other limits on the NEON cohort

- The NMDC NEON re-host holds bacterial / archaeal metagenomes only. No metatranscriptomic, metaproteomic, metabolomic, lipidomic or NOM data are associated with these three studies, so multi-omics framing is not feasible. [src: neon_mag_functional_discovery] The nmdc_arkin _gold tables return zero NEON rows. [src: neon_mag_functional_discovery]
- Of the 1,609 MQ+HQ MAGs, only 40 are archaeal, all from soil and 4 of them HQ. [src: neon_mag_functional_discovery]
- A clean cross-domain functional comparison was not feasible at this sample size. Archaea remain a soil-only side panel for future work. [src: neon_mag_functional_discovery]
- nmdc_arkin.kegg_module_terms in the KBase Data Lakehouse has empty name, description and category columns for all 370 modules, and only module_id is populated. [src: neon_mag_functional_discovery] The report therefore resolved module IDs (identifiers) against an external KEGG reference. [src: neon_mag_functional_discovery]

- The H4b analysis supports the hypothesis only on the available cohort. It inherits a 53% cohort attrition from a habitat-biased gap in NMDC per-gene annotation tables. [src: neon_mag_functional_discovery] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].
- The soil novelty trend cannot separate biological novelty from a GTDB coverage gap without a full-length 16S phylogeny against an unbiased reference. [src: neon_mag_functional_discovery]
- The nmdc_arkin.kegg_module_terms table has 370 rows with only module_id and empty name and category fields. Module labels therefore came from external KEGG references. [src: neon_mag_functional_discovery]
- The soil horizon test is capped at p = 0.001 by 999 permutations. [src: neon_mag_functional_discovery] A nested model with a pH × horizon interaction is untested follow-up work. [src: neon_mag_functional_discovery]

## [[summaries/nmdc_community_metabolic_ecology__REPORT|Community Metabolic Ecology via NMDC × Pangenome Integration]]

- All 33 Freshwater samples lacked paired metabolomics. They were excluded from the metabolite correlation tests (H1) but kept for the PCA (H2). [src: nmdc_community_metabolic_ecology] H1 is therefore effectively soil-only, and Black Queen dynamics in freshwater communities at this scale are untested. [src: nmdc_community_metabolic_ecology]
- Most pathways were not significant after FDR correction, and several had small n. [src: nmdc_community_metabolic_ecology]
- Nearly all H1 samples came from a single study. [src: nmdc_community_metabolic_ecology]
- Abiotic features (pH, temperature, total organic carbon and others) were all NaN (not a number) in the 174-sample matrix. Partial correlations controlling for environmental gradients were therefore impossible, and these variables could confound both H1 and H2. [src: nmdc_community_metabolic_ecology]
- GapMind completeness indicates gene presence, not expression. Transcriptomics would be needed to test whether expressed biosynthesis correlates more strongly with metabolite pools. [src: nmdc_community_metabolic_ecology]
- KEGG compound IDs (identifiers) in NMDC have a 2% annotation rate, limiting KEGG-based matching. [src: nmdc_community_metabolic_ecology]
- The 61 Unknown-ecosystem samples are unresolved in habitat identity. [src: nmdc_community_metabolic_ecology]

Next analyses the report proposes:

- Control H1 for pH, temperature and total organic carbon with partial correlation or mixed-effects modelling once abiotic data are populated for the metabolomics-overlap samples, to strengthen the signal or identify confounders. [src: nmdc_community_metabolic_ecology]
- Replicate across additional NMDC studies with paired taxonomy and metabolomics, to test whether the leucine and arginine signals generalise beyond the current cohort. [src: nmdc_community_metabolic_ecology]
- Obtain or generate metabolomics for the 33 Freshwater samples, to test whether Black Queen dynamics differ between aquatic and terrestrial communities. [src: nmdc_community_metabolic_ecology]
- Pair metatranscriptomics with metabolomics in a subset of samples, to compare expressed pathway completeness, genomic potential and metabolite abundance, and test whether expression rather than gene presence drives the signal. [src: nmdc_community_metabolic_ecology]
- Improve KEGG compound annotations in metabolomics_gold for cys, his and lys, which would expand the H1 test set from 13 to 16 testable pathways and improve power. [src: nmdc_community_metabolic_ecology]
- Resolve habitat identity of the Unknown samples via NMDC ENVO (Environment Ontology) annotations or study metadata, which could improve H2 power and reveal finer-scale metabolic niche structure. [src: nmdc_community_metabolic_ecology]

## [[summaries/nmdc_context_audit__REPORT|NMDC Context Audit]]

- The evidence is consistent with the overloaded label driving sub-optimal resource selection. This is inferred from the gap analysis and prior-project usage skew, not from a directly observed wrong choice. [src: nmdc_context_audit]
- Wasted time and compute and weakened conclusions are plausible consequences of such mistakes, not observed outcomes. [src: nmdc_context_audit]
- Provenance classes are inferred from schema, table properties, tenant metadata and prior project usage. No ingestion manifest is exposed in the catalog. [src: nmdc_context_audit]
- kbase.nmdc_* database descriptions are access-restricted, so some metadata, such as steward-authored notes, could not be captured. [src: nmdc_context_audit]
- Completeness is assessed relative to snapshot timestamps. The audit did not compare against live upstream NMDC or NCBI record counts, which would need external API (application programming interface) calls and were out of scope. [src: nmdc_context_audit]
- The recommended fixes are for review and are not yet applied. [src: nmdc_context_audit]

Next analyses proposed by the report:
- Apply the schema-page and berdl skill NMDC module recommendations and measure whether new NMDC projects reach the right resource faster. [src: nmdc_context_audit]
- Add a lightweight currency/provenance annotation to berdl_inventory.py output so disambiguation is dynamic, not just documentary. [src: nmdc_context_audit]
- Extend the provenance-audit method to other overloaded labels in the KBase Data Lakehouse, such as any tenant co-hosting external mirrors. The report asserts that the six-class framework generalizes. [src: nmdc_context_audit]
- Diff nmdc.metadata and nmdc.ncbi_biosamples against live upstream record counts to quantify completeness lag precisely. [src: nmdc_context_audit]

## [[summaries/oak_ridge_cultivation_gap__REPORT|What Metabolic Functions Does the Cultured Collection Miss?]]

- The MAG side was originally scoped to 623 ORFRC-specific MAGs from enigma_coral. Their assembly FASTAs were inaccessible from JupyterHub, so the report's findings concern subsurface systems generally rather than Oak Ridge specifically. [src: oak_ridge_cultivation_gap] The report says the results do not directly measure the cultivation gap at Oak Ridge, though the broader comparison is arguably more generalizable. [src: oak_ridge_cultivation_gap]
- The cultured collection spans 20+ years of isolation, primarily at ORFRC, while MAGs span global sites, so composition differences may reflect geography as much as cultivation bias. [src: oak_ridge_cultivation_gap]
- Genome-size disparity and Patescibacteria dominance confound the cultured-enriched KO counts. [src: oak_ridge_cultivation_gap] No genome-size-normalized analysis was performed. [src: oak_ridge_cultivation_gap]
- The report's prediction that excluding Patescibacteria would narrow the gap is stated as an expectation. [src: oak_ridge_cultivation_gap]
- MAGs are incomplete (mean completeness 78.7% in the QC-filtered cohort), so some KOs scored absent may lie in the missing 20% of the genome. [src: oak_ridge_cultivation_gap] This makes the 813 MAG-enriched KOs a conservative estimate, and some cultured-enriched KOs may be false positives. [src: oak_ridge_cultivation_gap]
- Annotation-pipeline sensitivity differences could bias the comparison, though KO-level comparison is more robust than pathway-level. [src: oak_ridge_cultivation_gap]
- The NiFe-hydrogenase result may reflect KO assignments that conflate hydrogenase groups. [src: oak_ridge_cultivation_gap]

### Next analyses proposed by the report

- Genome-size-normalized analysis: repeat the comparison in phyla represented in both cohorts, with size-matched genomes, to separate cultivation selection from genome streamlining. [src: oak_ridge_cultivation_gap]
- ORFRC-specific MAG comparison: when CORAL assembly FASTAs become accessible through JupyterHub or MinIO/CTS, annotate the 623 ORFRC-specific MAGs to produce a site-matched cultivation-coverage table. [src: oak_ridge_cultivation_gap]
- Investigate the 554 MAG-only KOs, which likely include Patescibacteria-specific functions. [src: oak_ridge_cultivation_gap] Cross-referencing them with the HGT analysis of Gios et al. (2025) could show which were horizontally acquired. [src: oak_ridge_cultivation_gap]
- Accessory genome analysis: compare plasmid- and prophage-borne content between cohorts using the pangenome's bakta annotations, to test the Goff et al. (2024) prediction that MGE-borne metal resistance is specifically depleted in cultured isolates. [src: oak_ridge_cultivation_gap]
- Cross-site generalization: apply cultivation_bias_diagnostic() to other KBase Data Lakehouse sites with both cultured and MAG collections, to test whether the porewater-bias signature is universal across subsurface environments. [src: oak_ridge_cultivation_gap]

## [[summaries/pangenome_openness__REPORT|Pangenome Openness Analysis]]

- Sample size is limited to species with both pangenome statistics and ecotype analysis results. [src: pangenome_openness]
- Openness is a single summary metric that may not capture the full complexity of pangenome structure. [src: pangenome_openness]
- Environment and phylogeny effects come from partial correlations that may not fully disentangle confounded variables. [src: pangenome_openness]
- The upstream ecotype analysis may have limited statistical power for species with few genomes. [src: pangenome_openness]

Proposed next analyses:
- Stratify by gene function, asking whether open pangenomes show environment effects specifically in L (mobile) or V (defense) categories. [src: pangenome_openness]
- Test alternative openness metrics: auxiliary fraction, Heap's law alpha, or pangenome fluidity. [src: pangenome_openness]
- Test an openness x lifestyle interaction, such as open pathogens versus open environmental species. [src: pangenome_openness]

## [[summaries/paperblast_explorer__REPORT|PaperBLAST Data Explorer — Characterizing Literature Coverage Bias in Protein Sequence Space]]

The "Unknown" domain class covers 14,798 organisms, so domain-level counts depend on name-based classification. [src: paperblast_explorer] The heuristic mapping classified 35% of organisms as Unknown, and a formal taxonomy lookup would improve accuracy. [src: paperblast_explorer]

The SwissProt subset is limited to entries matched to PMC open-access literature. [src: paperblast_explorer] Only 19% of SwissProt is in PaperBLAST, likely because many entries lack matching PMC full text. Curated knowledge therefore exists for proteins PaperBLAST cannot connect to. [src: paperblast_explorer]

Text-mined mentions do not imply functional characterization. The 65.6% of genes with 1 paper likely include many incidental mentions. [src: paperblast_explorer]

PaperBLAST mines full text only from PubMed Central. Paywalled papers are missed, which biases against fields and journals with lower open-access rates. [src: paperblast_explorer]

The 50% identity cutoff for "protein family" is conventional but arbitrary, not a universal biological boundary. [src: paperblast_explorer]

There are no negative controls, so genuinely unstudied genes cannot easily be told apart from genes whose literature text mining missed. [src: paperblast_explorer]

### Next analyses the report proposes

- Cross-reference with the Fitness Browser: use the 130K VIMSS links to find fitness-important genes that lack literature, as candidates for "high-impact understudied genes." [src: paperblast_explorer]
- Formal taxonomy integration: replace the heuristic domain classification with NCBI taxonomy lookup to quantify Bacteria/Archaea/Eukarya/Virus coverage accurately. [src: paperblast_explorer]
- Temporal trend analysis: track whether literature concentration is rising or falling, that is, whether a broader or narrower set of genes is studied each year. [src: paperblast_explorer]
- Dark family characterization: use AlphaFold structure prediction and domain annotation to infer putative functions for the 5,218 dark protein families. [src: paperblast_explorer]
- Literature graph analysis: build a gene-gene co-citation network from genepaper data to find functionally related but differentially studied gene clusters. [src: paperblast_explorer]

## [[summaries/pathway_capability_dependency__REPORT|Metabolic Capability vs Dependency]]

- The fitness-based classification covers only 7 of 48 Fitness Browser organisms with GapMind data. These are well-studied model organisms with near-complete core genomes, which the report says compresses the conservation contrast. [src: pathway_capability_dependency]
- The median-based importance threshold splits pathways approximately 50/50 into important and not-important by construction. [src: pathway_capability_dependency] The report cautions that all Latent Capabilities becoming important under some condition may partly reflect inevitable threshold crossing. [src: pathway_capability_dependency] Calibrating against an independent validation set, such as known essentials from essential_metabolome, would give a more defensible threshold. [src: pathway_capability_dependency]
- Latent Capability reflects standard laboratory conditions only. [src: pathway_capability_dependency] Condition-type stratification only partially addresses the fact that laboratory RB-TnSeq cannot capture the full range of natural selective pressures. [src: pathway_capability_dependency]
- Genes without KEGG annotations, or with incorrect ones, are missed, which may underestimate the true number of genes per pathway. [src: pathway_capability_dependency]
- GapMind covers amino acid biosynthesis and carbon utilization only. Cofactor biosynthesis, lipid metabolism and secondary metabolism are not assessed. [src: pathway_capability_dependency]
- Genome count confounds the pan-bacterial associations, and small genus samples limit power. [src: pathway_capability_dependency] Species with more sequenced genomes are more likely to show pathway variation and more ecotypes. Partial correlations mitigate but do not fully eliminate this bias. [src: pathway_capability_dependency]
- Full phylogenetic independent contrasts were not computed. The report controlled for genome count and checked within taxonomic groups. [src: pathway_capability_dependency]
- Phylogeny dominates gene content in 60.5% of species in ecotype_analysis, so metabolic ecotypes may partly reflect intra-species phylogenetic structure. [src: pathway_capability_dependency]
- The fixed 50% distance threshold for ecotypes is a simplification, and other thresholds would give different counts. [src: pathway_capability_dependency] The median of 4 ecotypes per species should be read as an order-of-magnitude estimate. [src: pathway_capability_dependency]
- The planned H2 analysis correlating metabolic ecotypes with AlphaEarth environmental niche breadth was not executed. [src: pathway_capability_dependency] AlphaEarth embeddings cover only 28% of genomes (83K/293K), which would significantly limit the sample size. [src: pathway_capability_dependency]

## [[summaries/pgp_pangenome_ecology__REPORT|PGP Gene Distribution Across Environments & Pangenomes]]

- The report considers the acdS and pqqC enrichment ORs (7.0 and 2.9) likely underestimates, because many soil isolates carry broader "environmental" labels. [src: pgp_pangenome_ecology]
- ncbi_isolation_source is noisy and NCBI is heavily biased toward clinical and host-associated isolates. [src: pgp_pangenome_ecology]
- Name-only gene detection misses genes annotated only by product description or with variant names, particularly less-characterized PGP genes. [src: pgp_pangenome_ecology]
- There was no functional validation: an annotated pqqC cluster is not necessarily functional, and truncations, frameshifts and pseudogenization are not filtered. [src: pgp_pangenome_ecology]
- A phylum-plus-soil logistic model (Model 3) for ipdC failed through quasi-complete separation, caused by ipdC's rarity (214 species, 1.9%). Conclusions therefore rest on Models 1 and 2. [src: pgp_pangenome_ecology] Only 214/11,272 species carry ipdC, which limits power for the stratified H4 analysis. [src: pgp_pangenome_ecology]
- The soil reversal (OR = 0.30, p = 0.02) should be treated as hypothesis-generating rather than conclusive. [src: pgp_pangenome_ecology]
- GapMind trp and tyr completeness scores both proxy overall pathway completeness. Controlling for genome size or total pathway count would be needed to isolate specific coupling. [src: pgp_pangenome_ecology] A better H4 test would control for genome completeness (size, COG coverage, clusters of orthologous groups) to separate aromatic-pathway effects from general metabolic capacity. [src: pgp_pangenome_ecology]
- The RESEARCH_PLAN estimated ~1,913 nifH clusters, but the actual count was 2,756 (43% higher). The report attributes this to growth of the GTDB r214 pangenome and says it affects no analysis. [src: pgp_pangenome_ecology]
- Proposed next step: determine whether pqqC and acdS are physically co-located (same island or operon) or occur at separate loci, to separate operon linkage from independent co-selection. [src: pgp_pangenome_ecology]
- Proposed next step: compare marine/aquatic diazotrophs, including cyanobacteria and Azotobacter, with legume-symbiotic rhizobia and free-living soil diazotrophs in genome structure and PGP trait co-occurrence. [src: pgp_pangenome_ecology]
- Proposed next step (controlled H4 test): regress ipdC presence on trp completeness while controlling for genome-wide pathway completeness (number of complete pathways or genome size), to isolate the aromatic-amino-acid-specific signal from global metabolic capacity. [src: pgp_pangenome_ecology]
- Proposed next step: a focused study of hcnA-C phylogeny and co-occurrence with biocontrol phenotypes. [src: pgp_pangenome_ecology]
- Proposed next step: cross-reference species carrying pqqC + acdS + hcnC with commercial inoculant strains, to assess whether the genomic signature predicts inoculant efficacy. [src: pgp_pangenome_ecology]

## [[summaries/phage_defense_arsenal__REPORT|Pan-Bacterial Anti-Phage Defense Arsenal — Distribution, Arms Race, and Syndromes]]

### Detection caveats

The report attributes DISARM's near-baseline core fraction almost certainly to detection artefact. The DrmB SNF2 helicase Pfam anchor (PF00176) is a widespread housekeeping-helicase domain, and it inflates the DISARM cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal] A DISARM-specific refinement using PADLOC's MacSyFinder-style HMM+context rules would remedy this. [src: phage_defense_arsenal] The DISARM arms-race and syndrome results survive this caveat because they use species-level presence/absence, not per-cluster core/auxiliary calls. [src: phage_defense_arsenal] The CRISPR over-counting from description matching is a further detection caveat. [src: phage_defense_arsenal] Prevalence numbers should be read as upper bounds. The combined eggNOG OR Pfam presence set used for syndromes favors recall, so CRISPR-Cas syndromes may be slightly underestimated in specificity but not in significance. [src: phage_defense_arsenal] Retron detection uses only RVT_1 (PF00078), a broad reverse-transcriptase Pfam. [src: phage_defense_arsenal] Housekeeping-helicase false positives inflate DISARM and reduce retron specificity. [src: phage_defense_arsenal]

### Sampling and inference caveats

Requiring ≥5 genomes reduces the bacterial analysis set to 7,323 species (26 % of 27,690 pangenome species), which biases it toward well-sampled, culturable, high-priority organisms. [src: phage_defense_arsenal] The universal-phylum arms-race pattern applies within this set. Extrapolation to the full 293K-genome tree, which includes many metagenome assembled genomes (MAGs) from environmental samples, is plausible but untested. [src: phage_defense_arsenal] Partial correlation and the GLM control for phylum categorically but not for finer phylogenetic structure. [src: phage_defense_arsenal] The report calls categorical control a coarse-grained analog and leaves open whether the arms race is independent of shared ancestry or partly a within-genus pattern amplified to appear cross-phylum. [src: phage_defense_arsenal]

### Proposed next analyses

- Refine broad-marker detection for Retron, DISARM and Gabija with PADLOC's MacSyFinder-style operon-level rules (multi-Pfam plus gene-order constraints). [src: phage_defense_arsenal] The report predicts this would fix the DISARM accessory-enrichment result and sharpen the syndrome and arms-race analyses without changing the qualitative conclusions. [src: phage_defense_arsenal]
- Extend detection to 20+ defense systems using DefenseFinder/PADLOC HMMs, including CRISPR-Cas subtypes, Zorya, Thoeris, Wadjet, Druantia, pAgo, PARIS, ThsA-ThsB and defense-associated antitoxin cassettes. [src: phage_defense_arsenal] The report expects the focused 7-system panel to generalize, and says a larger panel would enable a defense-repertoire principal-component analysis and genus-level clustering of defensive phenotype. [src: phage_defense_arsenal]
- Refit the negative-binomial GLM with the GTDB tree as a phylogenetic covariance structure, for example with phyr::pglmm, as a stronger arms-race test. [src: phage_defense_arsenal]
- Follow up R-M Type II × Gabija (OR = 24): compare species carrying only R-M Type II with those carrying both, then test for a quantitative fitness advantage from Gabija in phage-challenge experiments in Escherichia coli or Bacillus subtilis. [src: phage_defense_arsenal]
- Add an environment layer, cross-referencing defense repertoires with NCBI-env isolation source or AlphaEarth embeddings to test whether defense syndromes are habitat-specific. [src: phage_defense_arsenal] The report deferred this third pillar at the plan-review checkpoint. [src: phage_defense_arsenal]
- The report suggests exploring which covariates predict the variation in effect size across phyla. [src: phage_defense_arsenal] It also says the R-M Type II–Gabija pairing merits mechanistic follow-up. [src: phage_defense_arsenal]

## [[summaries/phb_granule_ecology__REPORT|Polyhydroxybutyrate Granule Formation Pathways — Distribution Across Clades and Environmental Selection]]

- The "precursors-only" category (46.5%) reflects the pleiotropy of phaA (beta-ketothiolase, K00626) and phaB (acetoacetyl-CoA reductase, K00023). Both act in general fatty acid and thiolase metabolism beyond PHB synthesis. [src: phb_granule_ecology] See [[concepts/pathway-completeness-inference-from-ko-annotations-and-pleiotropic-enzymes]].
- phaR (K18080) was absent from all 27K species in the eggNOG annotations. This suggests poor annotation coverage or misassignment. [src: phb_granule_ecology]
- The raw niche-breadth association is largely explained by genome size. [src: phb_granule_ecology]
- The NMDC mapping covered 3,014/3,492 (86.3%) of taxon columns, so the rest were unmapped. [src: phb_granule_ecology]

## [[summaries/pitfalls|KBase Data Lakehouse: Common Pitfalls & Gotchas]]

- Several items are described as specific incidents, such as one project's out-of-memory failure, one branch collision or one bad filter. [src: pitfalls]
- The ibd_phage_targeting synonym map is hand-curated and enough only for a targeted species battery. [src: pitfalls]
- Within ecotype-assigned CrohnsPhage samples, the report states that 0 sub-studies have both ≥ 10 HC and ≥ 10 CD samples. Only 5 have ≥ 10 CD. [src: pitfalls]
- Two-stage junction filtering gave no speedup, so this item offers no fix for presence-matrix cost. [src: pitfalls]
- The unmatched 56.6% of BacDive records are described as different species concepts or genera absent from GTDB r214. [src: pitfalls]

## [[summaries/plant_microbiome_ecotypes__REPORT|Plant Microbiome Ecotypes — Compartment-Specific Functional Guilds and Their Genetic Architecture]]

This part of the report compares pangenome-derived plant classifications with MGnify metagenomic detection. It also places the Phase 2 results against the literature and states the limits that remain. The cross-validation shows low agreement between the two sources, and the report treats the subclade null result as support for accessory-gene-driven plant adaptation. [src: plant_microbiome_ecotypes]

### Cross-validation against MGnify

Agreement between the two sources was low: 11.7% Jaccard between pangenome isolation-source plant classification and MGnify metagenomic rhizosphere detection. [src: plant_microbiome_ecotypes] The sources measure different things. Pangenome classification uses cultivation metadata about where a strain was isolated, whereas MGnify captures where a genome is detected metagenomically. [src: plant_microbiome_ecotypes] See [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa]].

The report suggests that the 390 pangenome-only plant genera likely include opportunistic soil bacteria isolated from plants rather than rhizosphere specialists. [src: plant_microbiome_ecotypes] It also suggests that the 341 MGnify-only rhizosphere genera may include uncultured lineages absent from GTDB. [src: plant_microbiome_ecotypes] Both are interpretations, not tested results.

Seventeen genera were consistently present across tomato, maize and barley rhizospheres, including Pseudomonas_E, Streptomyces, Variovorax and Acidovorax. The report proposes them as a candidate core rhizosphere microbiome for crop-agnostic biocontrol. [src: plant_microbiome_ecotypes] The report states that integrating the KBase Data Lakehouse pangenome data (293K genomes) with the MGnify catalogue (20,473 species, 4 biomes) independently validates T3SS (type III secretion system) enrichment in rhizosphere, mobilome patterns and core rhizosphere genera. [src: plant_microbiome_ecotypes]

### Subclade null result and accessory genome

The report found no subclade-level segregation of plant-associated genomes (H7). [src: plant_microbiome_ecotypes] It calls this consistent with Melnyk et al. (2019), who showed that plant-lifestyle transitions in Pseudomonas are driven by convergent gain and loss of accessory genomic islands rather than core-genome phylogeny. [src: plant_microbiome_ecotypes] The report reads this as support for plant adaptation through horizontal acquisition of accessory gene clusters in any phylogenetic background, rather than vertical inheritance along clonal lineages. [src: plant_microbiome_ecotypes] Its practical conclusion is that strain-level prediction of plant-association potential needs accessory genome profiling, not core-genome phylotyping. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

### Agreement with the literature

- H1 compartment-specific signatures align with Trivedi et al. (2020) and Knief et al. (2012). The report extends them to a genome-scale analysis of 1,136 species. [src: plant_microbiome_ecotypes]
- The H2 core/accessory pattern is consistent with Levy et al. (2018). It contradicts Loper et al. (2012) for biocontrol traits, likely because of the report's broader taxonomic scope. [src: plant_microbiome_ecotypes]
- The functional redundancy result (H3 rejected) is consistent with Louca et al. (2018) and Puente-Sanchez et al. (2024). [src: plant_microbiome_ecotypes]
- The partial H4 HGT (horizontal gene transfer) proxy results align with Ghaly et al. (2024), who found integrons as HGT hotspots in plant-associated bacteria. [src: plant_microbiome_ecotypes] They also align with Pinto-Carbo et al. (2016), who demonstrated HGT between obligate plant symbionts. [src: plant_microbiome_ecotypes]
- Dual-nature prevalence corroborates Drew et al. (2021) and Etesami (2025). The report calls its analysis the first genome-scale quantification, across 25,660 species. [src: plant_microbiome_ecotypes]
- Phase 2 mobilome enrichment in plant-associated genera aligns with Rajabal et al. (2024). It contrasts with the genome-level findings of Levy et al. (2018) and Bograd et al. (2025). The report says the resolution likely depends on scale, genus versus genome. [src: plant_microbiome_ecotypes]
- MGnify shows 2× T3SS enrichment in rhizosphere versus soil. [src: plant_microbiome_ecotypes] The report calls this consistent with Gonzalez-Vallina et al. (2024) and Tampakaki (2022), who found T3SS widespread in both beneficial and pathogenic plant bacteria. [src: plant_microbiome_ecotypes]
- Cytochrome oxidase is enriched in plant-associated species. [src: plant_microbiome_ecotypes] The report calls this consistent with Preisig et al. (1996), who characterized high-affinity cbb3 oxidase as essential for symbiotic nitrogen fixation in microaerobic root nodules. [src: plant_microbiome_ecotypes]

### Claimed contributions

The report calls its classification of 25,660 bacterial species into plant-interaction cohorts, by pangenome-scale marker-gene analysis, the first systematic one at this scale. Earlier studies examined tens to hundreds of genomes. [src: plant_microbiome_ecotypes] Across the full bacterial tree of life, the beneficial gene core fraction (64.6%) exceeds the pathogenic one (45.2%), with bootstrap confidence intervals. [src: plant_microbiome_ecotypes] Phase 2 extended this to 50 novel OGs (ortholog groups) with 60.1–83.1% core fractions. [src: plant_microbiome_ecotypes]

The report finds that 60–85% of plant-associated species carry both PGP (plant growth promoting) and pathogenic markers. It says this challenges the binary classification used in most PGPB screening programs. [src: plant_microbiome_ecotypes] The refined 17-marker panel with KEGG module gating kept the pattern at 78.7% after removing ubiquitous bacterial functions. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

The report reports genus-level mobilome enrichment in MGnify (p=1.49×10⁻⁵) and contrasts it with genome-level mobile element depletion in the literature. [src: plant_microbiome_ecotypes] It suggests that plant adaptation involves HGT-mediated accessory gene acquisition followed by core genome stabilization. [src: plant_microbiome_ecotypes]

### Caveats

- **Compartment metadata:** Classification relies on NCBI isolation_source metadata of variable quality and coverage. [src: plant_microbiome_ecotypes] Only 7,995 of 293,059 genomes (2.7%) had plant-associated annotations. [src: plant_microbiome_ecotypes] Endophyte species (n=29) fell below the 30-species threshold. [src: plant_microbiome_ecotypes]
- **Pfam versioning:** The bakta_pfam_domains table stores versioned Pfam IDs (identifiers) such as PF13629.12 rather than bare accessions such as PF00771. This caused zero hits in the original NB02 query. [src: plant_microbiome_ecotypes] NB13 Cell 3 fixed it with a LIKE 'PF00771%' pattern. [src: plant_microbiome_ecotypes] The marker set remains literature-curated. [src: plant_microbiome_ecotypes]
- **GapMind:** Core-level completeness scoring gave 0% across all compartments, which suggests the threshold is too stringent for broad taxonomic comparisons. [src: plant_microbiome_ecotypes] The threshold remains an open question. [src: plant_microbiome_ecotypes] NB06's max-aggregated species-to-genus scores inflated the complementarity Cohen's d to -7.54. [src: plant_microbiome_ecotypes] The NB14 prevalence-weighted re-test gave d = -0.39, credible in magnitude and in the same direction. [src: plant_microbiome_ecotypes]
- **Confounder control:** The plan specified genus-level fixed effects. Phase 1 used phylum-level control because of computational cost, and NB10's statsmodels genus-level logit failed for 0/14 markers. [src: plant_microbiome_ecotypes] NB14's scikit-learn L1-regularized logit, with top-20 genus dummies and log₁₀(genome size) covariates, converged. For 9/17 markers the bootstrap 95% CIs (confidence intervals) excluded zero. [src: plant_microbiome_ecotypes]
- **Sensitivity and permutation:** Excluding the top-3 species per compartment cut PERMANOVA (permutational multivariate analysis of variance) R² from 0.527 to 0.072, still significant at p = 0.001. [src: plant_microbiome_ecotypes] Within-genus label shuffling left only 3/15 markers (nitrogen fixation, ACC deaminase, T3SS) surviving the strict permutation null. [src: plant_microbiome_ecotypes] ACC is 1-aminocyclopropane-1-carboxylate. Phylogeny versus ecology variance decomposition remains future work. [src: plant_microbiome_ecotypes] The NB04 code-error issue is documented. Compartment profiling uses PERMANOVA rather than logit as the primary test. [src: plant_microbiome_ecotypes]
- **HGT proxies:** Without GeNomad mobile-element annotations, HGT was assessed indirectly. Strong transposase co-occurrence but lower-than-baseline singleton enrichment shows the limits of proxies. [src: plant_microbiome_ecotypes]
- **Dual nature:** Presence of both PGP and pathogenic markers does not confirm simultaneous expression. Transcriptomic or experimental validation is needed to separate lifestyle flexibility from annotation artifacts, such as T6SS serving inter-bacterial competition. [src: plant_microbiome_ecotypes] Negative controls (NB08) classified non-plant Escherichia, Salmonella and Clostridioides as 100% dual-nature. [src: plant_microbiome_ecotypes]

This part of the report lists the limits on its results. These include confounding by non-specific markers and genome size, dispersion effects, model convergence failures, database coverage gaps and identifier mismatches. It also records which limits later notebooks resolved and which remain open. [src: plant_microbiome_ecotypes]

### Marker specificity and dual-nature rates

The dual-nature classification is inflated by markers that are not plant-specific. Negative controls (NB08) classified *Staphylococcus* as 98% dual-nature. [src: plant_microbiome_ecotypes] The report explains that flagella, chemotaxis, biofilm, quorum sensing and secretion-system markers are ubiquitous across bacteria. [src: plant_microbiome_ecotypes] Together with a genome-size confound, this means the NB02 dual-nature rate of 60.3% substantially overestimates genuine plant-adapted duality. [src: plant_microbiome_ecotypes] The NB07 composite score gave 25.2% dual-nature, but that rate depends on arbitrary scoring weights. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

### Genome size

Genome size, measured as gene cluster count, correlates moderately with total marker count (r=0.44, p<1e-300), so larger genomes accumulate more markers by chance. [src: plant_microbiome_ecotypes] Plant species in the bottom genome-size quartile were 54% dual-nature, against 87% in the top three quartiles. The 78.7% figure therefore masks a gradient. [src: plant_microbiome_ecotypes] In NB14, all 50 novel OGs (ortholog groups) kept positive plant-association coefficients with genome size as a covariate. [src: plant_microbiome_ecotypes] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

### Compartment effect: location versus dispersion

The compartment effect is supported, but its PERMANOVA effect size may be inflated by dispersion differences. NB08 PERMDISP (permutational analysis of multivariate dispersions) found significant dispersion heterogeneity between cohorts (H=33.12, p=3.0e-7). The PERMANOVA R²=0.53 may therefore partly reflect variance differences. [src: plant_microbiome_ecotypes] Fisher enrichment tests still support the compartment effect (69/96 significant), but the PERMANOVA effect size should be treated as an upper bound. [src: plant_microbiome_ecotypes]

A later db-RDA on plant-compartment functional profiles gave a location-only R² of 0.060, which is 84% of total PERMANOVA R² (0.071). [src: plant_microbiome_ecotypes] PERMDISP confirmed dispersion heterogeneity (F=15.6, p=0.001). [src: plant_microbiome_ecotypes] The report concludes that the residual effect is small but real and mostly location, not dispersion. [src: plant_microbiome_ecotypes] See [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]].

### Phylogenetic confounding and model fitting

Of the tested OGs, 94.2% (5,341/5,671) were significantly associated with plant status. This reflects genome-wide compositional differences rather than plant-specific enrichment. [src: plant_microbiome_ecotypes] Only the 50 OGs that survive phylogenetic control are candidate plant-interaction genes. [src: plant_microbiome_ecotypes] Separately, among plant-enriched OGs, 48/50 survive per-species phylum plus genome-size regression at q<0.05. [src: plant_microbiome_ecotypes]

NB10 genus-level fixed-effects logistic regression for the 14 refined markers failed to converge in every model (0/14). [src: plant_microbiome_ecotypes] NB14 resolved this with L1-penalized logistic regression (scikit-learn, saga solver) using top-20 genus dummies and log₁₀(genome size). [src: plant_microbiome_ecotypes] A genus-cluster-robust GLM (generalized linear model) gave proper Wald CIs (confidence intervals), and 8/14 markers were significant at q<0.05. [src: plant_microbiome_ecotypes] It agrees with L1 on 13/14 markers and disconfirms one L1 false positive, iaa_biosynthesis. [src: plant_microbiome_ecotypes] This supports separate tiers of species-level, cassette-level and not-robust signal. [src: plant_microbiome_ecotypes]

A full PGLMM with GTDB-tree-derived random-effect covariance remains theoretically stronger. Its 25K x 25K dense covariance matrix is intractable, so genus-level cluster-robust GLM serves as the practical analogue. [src: plant_microbiome_ecotypes] PGLMMs with the full GTDB tree remain future work. [src: plant_microbiome_ecotypes]

### Cross-validation and data coverage

The NMDC taxonomy bridge matched 260/322 genera (80.7%) and lost 62 (19.3%). [src: plant_microbiome_ecotypes] The effect on the complementarity hypothesis (H3) is unknown. If the lost genera include key complementary partners, the observed redundancy signal could be artifactual. [src: plant_microbiome_ecotypes] See [[concepts/functional-redundancy-versus-complementarity-among-co-occurring-genera]].

Pangenome-derived and MGnify-derived plant-associated genera overlap by only 11.7% (Jaccard). [src: plant_microbiome_ecotypes] The report attributes this to isolation metadata versus metagenomic detection rather than classification error. It says the low concordance still limits the strength of the cross-validation. [src: plant_microbiome_ecotypes] See [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa]].

BacDive cross-validation found 2,482 plant-related strains but added 0 genome upgrades beyond ncbi_env. This indicates complete overlap between the two metadata sources for the plant-associated genome set. [src: plant_microbiome_ecotypes]

MGnify BGC (biosynthetic gene cluster), mobilome and defense annotations exist only for the soil biome, not for the tomato, maize or barley rhizosphere biomes. [src: plant_microbiome_ecotypes] The mobilome and BGC analyses therefore compare soil-dwelling plant-associated genera with soil-dwelling non-plant genera, not rhizosphere with bulk soil. [src: plant_microbiome_ecotypes]

### Subclade analyses and identifier plumbing

NB12's null H7 result came from genome identifier (ID) format mismatches. The phylogenetic tree table used bare NCBI accessions, and the environment metadata used GTDB-prefixed IDs. [src: plant_microbiome_ecotypes] NB13 fixed this by prepending GB_ to GCA_ accessions and RS_ to GCF_ accessions. This gave 100% overlap (1306/1306 genomes) and recovered 599 plant-associated genomes. [src: plant_microbiome_ecotypes] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

The full 65-species H7 scan found 5/17 testable species significant after Bonferroni correction. [src: plant_microbiome_ecotypes] Three of those five were also Cochran-valid. [src: plant_microbiome_ecotypes] The H6 host × subclade extension found robust pathovar-host segregation in 2/9 species: *X. campestris* × Brassica and *X. vasicola* × *Zea mays*. [src: plant_microbiome_ecotypes] Coverage limits this scan. 47/65 candidate species lack phylogenetic tree coverage in the KBase Data Lakehouse, which the report calls a database limitation rather than a methodology issue. [src: plant_microbiome_ecotypes] Only 18 species have tree data. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

### Annotation audit and review status

The Pfam audit found 12/22 marker Pfams absent from bakta_pfam_domains but present in interproscan_domains, mostly secretion-system components. [src: plant_microbiome_ecotypes] NB10 already uses InterProScan, so the report says its biological claims are unaffected. [src: plant_microbiome_ecotypes]

The report says the five issues from the 2026-04-24 adversarial review, which were only partly addressed in Phase 2b, were all closed on 2026-04-25. [src: plant_microbiome_ecotypes] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

- The 47 species without phylogenetic-tree coverage leave the true within-species effect across all 65 candidate species unestimable until the GTDB tree is more completely populated in the KBase Data Lakehouse. [src: plant_microbiome_ecotypes]
- Only 80.7% of NMDC genera matched, and sensitivity analysis of this loss was deferred to future work. [src: plant_microbiome_ecotypes]
- The 2 enriched OGs that did not fit the genome-size-controlled analysis failed from singular matrices, not biological rejection. [src: plant_microbiome_ecotypes]
- That bakta uses a reduced core Pfam HMM set is the report's proposed explanation of the annotation gap, not a tested result. [src: plant_microbiome_ecotypes]

## [[summaries/prophage_amr_comobilization__REPORT|Prophage-AMR Co-mobilization Atlas]]

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

## [[summaries/prophage_ecology__REPORT|Prophage Gene Modules and Terminase-Defined Lineages Across Bacterial Phylogeny and Environmental Gradients]]

The module calls rest on eggNOG functional annotations used as proxies, not dedicated tools such as geNomad or VIBRANT. [src: prophage_ecology] This likely inflates prevalence by including domesticated remnants and bacterial homologs such as integrases, and the false positive rate is uncharacterized. [src: prophage_ecology] Near-universal modules A, D and F may therefore reflect domesticated remnants rather than active prophages. [src: prophage_ecology] Module definitions are validated for the core backbone (A, D, F) but less so for accessory functions (E, G). [src: prophage_ecology] Genome size is the dominant predictor, and residual confounding cannot be excluded despite stratification and partial correlations. [src: prophage_ecology] The PERMANOVA used a 1,773-species subsample with only 99 permutations. [src: prophage_ecology] The NMDC burden is inferred from taxonomy, not measured directly, and rests on untested genus-level conservation. [src: prophage_ecology] Environment metadata are sparse, coarse and 35% "other_unknown". [src: prophage_ecology] The embedding subsample covers only 28% of genomes. [src: prophage_ecology] The co-occurrence tests have limited within-phylum replication, and module B was testable in only 6 species. [src: prophage_ecology] The 200-permutation null gives adequate but not exhaustive precision. [src: prophage_ecology] The null TerL result means lineage-level environmental adaptation was not detected beyond host phylogeny. [src: prophage_ecology]

The report proposes these next analyses:
- Run geNomad or VIBRANT on representative genomes to estimate false positive and negative rates of the annotation-based approach and calibrate module prevalence. [src: prophage_ecology]
- Use sequential or partial PERMANOVA to quantify the unique environmental variance after controlling for phylogeny and genome size together, instead of testing each predictor independently. [src: prophage_ecology]
- Split future analysis into a core prophage backbone (A, D, F) and accessory functions (B, C, E, G). [src: prophage_ecology]
- Test the "arms race" hypothesis by asking whether anti-defense genes (Module G) co-localize with defense system genes in the same genomes. [src: prophage_ecology]
- Cross-reference environment-enriched modules with prophage induction triggers (SOS response, pH stress, temperature shifts) to explain the NMDC pH and temperature correlations. [src: prophage_ecology]
- Use NMDC longitudinal samples, if available, to test within-site changes in prophage burden over time, giving causal evidence beyond cross-sectional correlations. [src: prophage_ecology]

## [[summaries/pseudomonas_carbon_ecology__REPORT|Carbon Source Utilization Predicts Ecology and Lifestyle in Pseudomonas]]

- Classifiable isolation metadata covered only 64.2% of genomes (8,171/12,732). [src: pseudomonas_carbon_ecology] Clinical and other human isolates made up 33.0% and 13.0% of genomes. [src: pseudomonas_carbon_ecology] Keyword classification left ~6.7% "unknown" and ~29.1% "other", and misclassification could attenuate ecological signal. [src: pseudomonas_carbon_ecology]
- P. aeruginosa comprises 53% of all genomes (6,760/12,732) because of clinical importance. Many environmental species have <10 sequenced genomes, which affects the power of species-level comparisons. [src: pseudomonas_carbon_ecology]
- The environment classifier is only modestly predictive. [src: pseudomonas_carbon_ecology] GapMind's 62 pathways may be too coarse for strain-level niche differences within environmental species. [src: pseudomonas_carbon_ecology]
- The 62 pathways miss genus-specific capabilities, notably toluene, naphthalene and benzoate degradation central to P. putida ecology. [src: pseudomonas_carbon_ecology]
- The dominant PCA signal separates subgenera rather than lifestyles. [src: pseudomonas_carbon_ecology]
- The subgenus comparison used only 7 Pseudomonas s.s. species against 189 Pseudomonas_E species. [src: pseudomonas_carbon_ecology]
- Within Pseudomonas_E, lifestyle categories overlap substantially. [src: pseudomonas_carbon_ecology] Differences there are subtle, and the analyses do not explicitly control for phylogenetic non-independence. [src: pseudomonas_carbon_ecology]
- Majority-vote assignment of one environment per species obscures generalist species that inhabit multiple environments. [src: pseudomonas_carbon_ecology]

The report proposes these next analyses.
- Extend to aromatic degradation using KEGG modules for toluene, benzoate and naphthalene. [src: pseudomonas_carbon_ecology] The report hypothesizes these likely carry stronger environmental signal. [src: pseudomonas_carbon_ecology]
- Use phylogenetic generalized least squares (PGLS) or phylogenetic logistic regression with the GTDB species tree to test whether lifestyle-pathway associations persist after controlling for relatedness. [src: pseudomonas_carbon_ecology]
- Analyze within-species pathway variation to look for metabolic ecotypes, meaning subpopulations adapted to different niches. [src: pseudomonas_carbon_ecology]
- Cross-reference pathway predictions with random barcode transposon sequencing (RB-TnSeq) fitness data from kescience_fitnessbrowser to validate functionally important pathways. [src: pseudomonas_carbon_ecology]
- Move to genome-level prediction using the full 789K genome-pathway matrix with genome-specific isolation sources, to gain statistical power. [src: pseudomonas_carbon_ecology]

## [[summaries/respiratory_chain_wiring__REPORT|Condition-Specific Respiratory Chain Wiring in ADP1]]

- Of the 62 respiratory genes, 36 have growth data and 26 do not, including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring]
- NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be tested directly. [src: respiratory_chain_wiring]
- The stoichiometry uses theoretical pathway biochemistry, not measured flux distributions. [src: respiratory_chain_wiring]
- The ADP1 wiring pattern may be species-specific rather than a general rule. [src: respiratory_chain_wiring]
- The NDH-2 gene search in FB organisms may miss orthologs because of variable annotation. [src: respiratory_chain_wiring]
- NDH-2 identification in NB04 uses gene-description text matching, which likely produces false positives for organisms with incompletely annotated Complex I subunits. [src: respiratory_chain_wiring]
- An example is pseudo3_N2E3, whose 8 putative NDH-2 hits are probably a Complex I operon. [src: respiratory_chain_wiring]
- The report considers KO-based identification (K03885) more reliable. [src: respiratory_chain_wiring]
- The planned pangenome KO co-occurrence analysis was not performed, so NDH-2/Complex I co-occurrence across Acinetobacter species remains untested. [src: respiratory_chain_wiring]
- Proposed next step: construct an ADP1 NDH-2 knockout, the definitive experimental test of the prediction that NDH-2 deletion makes Complex I essential on glucose. [src: respiratory_chain_wiring]
- Proposed next step: measure NADH/NAD⁺ ratios per carbon source by metabolomics. [src: respiratory_chain_wiring]
- Proposed next step: query the full KBase Data Lakehouse pangenome for NDH-2 (K03885) and Complex I (K00330-K00343) co-occurrence across 27K species, for a much larger sample. [src: respiratory_chain_wiring]
- Proposed next step: characterize ACIAD3522 to determine whether it is a true respiratory NADH dehydrogenase or a metabolic enzyme. [src: respiratory_chain_wiring]
- Proposed next step: reanalyze respiratory chain proteins in the quinate-versus-succinate proteomics of Stuani et al. (2014), to test whether ADP1 upregulates Complex I on aromatics and NDH-2 on glucose. [src: respiratory_chain_wiring]

## [[summaries/snipe_defense_system__REPORT|SNIPE Defense System in the KBase Data Lakehouse Pangenome]]

- Published knockout and coevolution data used for the cost argument are not from the KBase Data Lakehouse. [src: snipe_defense_system]
- The M. maripaludis SNIPE is archaeal, so its phage context differs from the phage lambda system. [src: snipe_defense_system] Its gene is mostly dispensable. [src: snipe_defense_system]
- ManXYZ fitness exists only for E. coli K-12, and no Klebsiella strain in the Fitness Browser carries ManXYZ by gene name. [src: snipe_defense_system]
- PhageFoundry provides genome annotations only (GenomeDepot format), with no fitness/TnSeq (transposon sequencing) tables, so no Klebsiella-specific SNIPE or ManYZ fitness data exist here. [src: snipe_defense_system] Generating them would need new mutant libraries in natural SNIPE carriers such as K. pneumoniae NCTC9140 or HS11286. [src: snipe_defense_system] The report has developed PLAN_fitness_data_curation.md to curate external K. pneumoniae Tn-Seq datasets. [src: snipe_defense_system]
- The Klebsiella SNIPE inference rests on protein length, and the report says only that this strongly suggests two domains. [src: snipe_defense_system]
- AlphaEarth results cover only 28.4% of genomes and do not name the environmental variables behind each dimension. [src: snipe_defense_system]
- eggNOG Pfam annotations may miss divergent SNIPE homologues. [src: snipe_defense_system] DUF4041 (T5orf172) is strongly associated with SNIPE, but some hits may represent non-SNIPE proteins. [src: snipe_defense_system]
- The planned comparison of COG V defense gene density in SNIPE versus non-SNIPE species could not be completed via REST API, because the 93M × 132M row join requires Spark Connect. [src: snipe_defense_system]
- The NMDC metagenome ecosystem breakdown was limited because only 2 samples matched the API query format. The report suggests interactive MCP tool queries would improve coverage. [src: snipe_defense_system]

## [[summaries/soil_frontier_genomics__REPORT|Soil Microbial Dark Matter and the Clay Shield Null Result]]

### Negative R² is not fully diagnosed

The report states that its diagnosis of the negative R² is incomplete. All three model families predict worse than the training mean. [src: soil_frontier_genomics] Three causes have not been distinguished:
- Train/test distributional shift from spatial autocorrelation within GroupKFold folds. [src: soil_frontier_genomics]
- High-leverage outlier samples in test folds that dominate the mean squared error (MSE). [src: soil_frontier_genomics]
- Genuine unpredictability of functional gene counts from the measured predictors at global scale. [src: soil_frontier_genomics]

Only genuine unpredictability supports a strong biological null. Distributional shift or outlier leverage would indicate a modelling failure. [src: soil_frontier_genomics] So the "not supported" conclusion is weaker than a clean null.

### GDI validity

- GDI is a novel index without published precedent. [src: soil_frontier_genomics]
- The formula gives a GDI of 902 even with zero genomes (completeness = 0, denominator = 1). [src: soil_frontier_genomics]
- GDI conflates sampling gap and OTU richness, and the richness term alone could dominate it. [src: soil_frontier_genomics]
- Separate reporting of richness and completeness, with a 2D scatter, would be more interpretable. [src: soil_frontier_genomics]
- Forest (902.36) and Cropland (890.82) differ by 1.3%. Without bootstrap CIs they are not meaningfully distinguishable. [src: soil_frontier_genomics]
- The report recommends describing them as jointly the highest-GDI biomes, not as a ranked order. [src: soil_frontier_genomics]
- The +0.8 pH gap needs a reverse-causality check. Alkaline soils may have fewer database genomes because fewer such samples were ever sequenced, not because the microbes are harder to assemble or less studied. [src: soil_frontier_genomics]
- Controlling for the number of 16S samples in each pH bin before computing GDI would separate assembly/annotation gaps from sampling gaps. [src: soil_frontier_genomics]

### Pending work

1. Decompose the negative R² into distributional shift, outlier leverage, and true unpredictability. This requires a rerun with spatial blocking. [src: soil_frontier_genomics]
2. Compute a rarefaction-corrected GDI, using uniform 16S sequencing depth before the richness calculation. [src: soil_frontier_genomics]
3. Compute bootstrap 95% CIs on biome-level GDI rankings. This requires a raw-data rerun. [src: soil_frontier_genomics]
4. Control the pH discovery bias for the number of 16S samples per pH bin. [src: soil_frontier_genomics]
5. Report Forest versus Cropland GDI with uncertainty before claiming a ranked ordering. [src: soil_frontier_genomics]

## [[summaries/soil_metal_functional_genomics__REPORT|Soil Metal Concentrations Drive Functional Gene Shifts]]

### Status

The report is preliminary: Spearman correlation, db-RDA, and PGLS analyses are complete in NB01–NB04, while NB05 effect size and spatial validation and NB06 figures are pending. [src: soil_metal_functional_genomics]

All reported metal-COG associations are observational. [src: soil_metal_functional_genomics]

### db-RDA interpretation

The report cautions that conditional db-RDA R² = 0.799 may describe metals' explanation of residual rather than total community COG variance if project effects account for the majority of variance. [src: soil_metal_functional_genomics]

The unconditional db-RDA R² for metals alone without removing project effects is unreported and may be substantially lower than the conditional figure. [src: soil_metal_functional_genomics]

Reporting unconditional db-RDA R² (metals only, without project accession conditioning) remains pending. [src: soil_metal_functional_genomics]

### Multiple testing and confounding

The report describes 2,355 significant associations at FDR < 0.05 in 51,748 samples from 9 metals × 435 COGs = 3,915 tests as a high 60% discovery rate. [src: soil_metal_functional_genomics]

The report asserts that co-contaminating metals make tests non-independent, that Benjamini-Hochberg FDR correction assumes independent tests and is anti-conservative under positive correlation, and that true FDR is likely higher than reported. [src: soil_metal_functional_genomics]

Co-contamination is a significant confound because Cr, Cu, Pb, and Zn co-vary in many industrial soils. [src: soil_metal_functional_genomics]

Whether individual COG-metal associations are metal-specific or reflect a generic stress response to multi-metal contamination remains unresolved, with NB05 partial correlation models pending. [src: soil_metal_functional_genomics]

The report identifies the NB05 item 3 partial correlation model as the remedy for this confounding. [src: soil_metal_functional_genomics]

The pending partial correlation model is COG ~ Cr | Cu + Zn + Pb, intended to distinguish metal-specific from general responses. [src: soil_metal_functional_genomics]

Spearman ρ effect sizes have not been systematically reported across all 2,355 associations, and many associations may be statistically significant but biologically small. [src: soil_metal_functional_genomics]

The pending effect size audit will examine the ρ distribution across 2,355 associations and flag ρ < 0.05. [src: soil_metal_functional_genomics]

### Copper proximity

The copper-specific analysis matches soil samples to KBase genomes using a 10 km proximity criterion, at which many nearby genomes may not be co-located with copper measurements. [src: soil_metal_functional_genomics]

The report states that sensitivity analyses at 5 km and 20 km thresholds are needed before attributing COG-copper associations to measured sites. [src: soil_metal_functional_genomics]

Rerunning copper proximity analyses at 5 km and 20 km thresholds remains pending. [src: soil_metal_functional_genomics]

### Other pending work

The pending spatial autocorrelation validation will test Moran's I on residuals and use SEVM if significant. [src: soil_metal_functional_genomics]

Pending mechanistic classification will assign significant COGs to resistance, stress, membrane, energy, and unknown categories. [src: soil_metal_functional_genomics]

NB05 items 1–4 require re-running analyses from the `kescience_mgnify`/`kbase_ke_pangenome` Spark tables. [src: soil_metal_functional_genomics]

No local CSV output of Spearman ρ values or model residuals is available, so the pending validations cannot be completed without Spark access. [src: soil_metal_functional_genomics]

## [[summaries/t4ss_cazy_environmental_hgt__REPORT|T4SS-CAZy Environmental HGT]]

The analysis is preliminary: NB01–NB04 are complete, while NB05 threshold validation and NB06 manuscript figures are pending. [src: t4ss_cazy_environmental_hgt] All associations are observational, and mechanistic confirmation requires experimental validation. [src: t4ss_cazy_environmental_hgt] The ≤10 kb co-occurrence threshold is not yet validated. [src: t4ss_cazy_environmental_hgt]

Pending work:
- A synteny threshold permutation test, which requires Spark unfiltered data. [src: t4ss_cazy_environmental_hgt]
- BLAST validation of Node_4915, which requires BLAST against NCBI nr. [src: t4ss_cazy_environmental_hgt]
- A housekeeping gene null baseline. [src: t4ss_cazy_environmental_hgt]
- Biome enrichment factorisation, θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)]. [src: t4ss_cazy_environmental_hgt]

## [[summaries/thermodynamic_impact__REPORT|Thermodynamic Impact of OPAM2 pKa Predictions on Metabolic Modeling]]

All models were gapfilled on complete media, which may mask thermodynamic infeasibilities that would emerge under minimal media conditions. [src: thermodynamic_impact] The phenotype prediction results (NB08) highlight this: TMFA blocks growth on all alternative carbon sources. [src: thermodynamic_impact]

- The diverse organism analysis used LP-relaxed TMFA without integer variables for tractability. Full MILP TMFA may reveal additional direction-locking effects, although the E. coli analysis suggests these are minor. [src: thermodynamic_impact]
- TMFA used default concentration bounds of 1 µM – 10 mM, and organism-specific metabolomics could shift some reactions across the feasibility boundary. [src: thermodynamic_impact]
- MILP solutions came from GLPK, which may find different optima than commercial solvers (Gurobi, CPLEX) in degenerate solution spaces. [src: thermodynamic_impact]
- The study did not experimentally validate pKa accuracy. [src: thermodynamic_impact]
- The phenotype panel of 12 carbon sources captures a limited phenotypic space. [src: thermodynamic_impact]

## [[summaries/truly_dark_genes__REPORT|Truly Dark Genes — What Remains Unknown After Modern Annotation?]]

- The 17,479 unlinked dark genes could not be assessed. [src: truly_dark_genes] At the 16.3% truly-dark rate, the report estimates ~2,841 additional truly dark genes among them, including 2,208 with strong fitness phenotypes. [src: truly_dark_genes] The ranked list covers ~69% of the estimated total truly dark gene population. [src: truly_dark_genes] The report calls this a 31% coverage gap. [src: truly_dark_genes] This is an extrapolation, not a measurement. [src: truly_dark_genes] The report proposes extending pangenome linkage to these genes, then running bakta to find more candidates. [src: truly_dark_genes]
- Some bakta "hypothetical protein" calls may be false negatives, meaning genes with known functions that did not match the PSC database version tested (v6.0). [src: truly_dark_genes]
- BBH (bidirectional best hit) orthologs cover only 32 of 48 FB organisms. Truly dark genes from the other 16 lack concordance and ortholog-breadth data. [src: truly_dark_genes]
- Methanococcus strains S2 and JJ hold 55% of truly dark genes, a concentration the report attributes to archaeal underrepresentation in annotation databases. [src: truly_dark_genes]
- The HGT interpretation rests on GC deviation and proximity to mobile elements. The report describes the GC result as consistent with HGT and the mobile-element result as supporting it. [src: truly_dark_genes] GC deviation is an imperfect HGT proxy. It can also reflect gene-specific composition biases, such as membrane proteins, or amelioration over time. [src: truly_dark_genes]
- Short genes are harder to annotate and harder to measure fitness for. The length difference (d = −0.432) may therefore partly explain other differences. [src: truly_dark_genes]
- Some strong fitness phenotypes may reflect polar effects on downstream genes rather than the truly dark gene's own function. [src: truly_dark_genes]

### Dark island hypotheses

The report defines dark islands as contiguous hypothetical regions. [src: truly_dark_genes] It hypothesizes that they likely represent recently acquired genomic islands consistent with HGT signatures. [src: truly_dark_genes] It also hypothesizes phage-derived regions, supported by integrase/phage protein proximity. [src: truly_dark_genes] A third hypothesis is species-specific gene neighborhoods that arose after the last common ancestor shared with well-studied organisms. [src: truly_dark_genes] It suggests some islands may be prophage remnants. [src: truly_dark_genes] It suggests others may be recently acquired metabolic cassettes. [src: truly_dark_genes]

### Proposed next steps

The report proposes AlphaFold2/ESMFold structure prediction with Foldseek as the next frontier for these candidates. [src: truly_dark_genes] It would run these on the top-100 candidates and search for remote structural homologs. [src: truly_dark_genes] The report calls this the most promising path to annotating sequences with no detectable sequence homology. [src: truly_dark_genes] It proposes growth assays in predicted conditions, such as motility assays for PV4/5210953 [src: truly_dark_genes] and nitrogen limitation for ANA3/7026383. [src: truly_dark_genes] It suggests Mobile-CRISPRi could enable rapid functional testing across organisms. [src: truly_dark_genes] It also proposes a focused Methanococcus analysis using high cofitness signals (r > 0.97) to map operonic structure and predict functions for archaeal-specific hypothetical proteins. [src: truly_dark_genes] The report states that archaea contribute 55% of truly dark genes. [src: truly_dark_genes]

## [[summaries/webofmicrobes_explorer__REPORT|Web of Microbes Data Explorer]]

- The snapshot has no organism consumption action. Newer GNPS2 data may add consumption. [src: webofmicrobes_explorer]
- The report predicts that ingesting NLDM would resolve the no-consumption limitation and increase the organism count 3–5×. [src: webofmicrobes_explorer]
- The data are small (37 organisms, 5 projects) and from a single laboratory. [src: webofmicrobes_explorer] 37 organisms (20 experimental) is too few for statistical analyses across organism groups. [src: webofmicrobes_explorer]
- The frozen 2018 Wayback Machine snapshot may not reflect current WoM. The report expects the GNPS2-hosted version or Northen lab internal datasets, including the NLDM 110-organism panel, to be substantially richer. [src: webofmicrobes_explorer]
- E. coli BW25113 is the same strain as Keio, but WoM data cover only 12 observations in one medium. [src: webofmicrobes_explorer]
- The Synechococcus match is at genus level only. [src: webofmicrobes_explorer]
- Formula-only ModelSEED matches are ambiguous and need manual curation. [src: webofmicrobes_explorer]
- 81 identified compounds have no ModelSEED link. [src: webofmicrobes_explorer]
- GapMind linkage is blocked until a pathway-to-substrate/product lookup table exists. [src: webofmicrobes_explorer]
- Species-level pangenome matching was not attempted. [src: webofmicrobes_explorer]
- The report proposes using metabolic novelty rate as a phenotype to cross-reference with pangenome gene content. [src: webofmicrobes_explorer]

Next analyses the report proposes:

- Obtain the current WoM dataset from GNPS2 or the Northen lab to address the missing consumption data. [src: webofmicrobes_explorer]
- Build a GapMind pathway-to-metabolite lookup table from the GapMind documentation, enabling the WoM–GapMind link that failed in notebook 02. [src: webofmicrobes_explorer]
- For pseudo3_N2E3 and pseudo13_GW456_L13, identify genes that are fitness-important on carbon sources the same organism produces, testing whether metabolic output predicts gene essentiality. [src: webofmicrobes_explorer]
- Test whether organisms with higher E/(E+I) ratios have more open pangenomes or more accessory genes. [src: webofmicrobes_explorer]
- Re-run the ingestion pipeline (data/wom_ingest/) when newer WoM data are available, to update kescience_webofmicrobes and enable the blocked consumption analyses. [src: webofmicrobes_explorer]


