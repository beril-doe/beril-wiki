# Research Opportunities

Concrete next analyses this corpus makes possible — every concept page's
Open Directions, gathered in one place. Follow a link for the evidence.

## [[concepts/gene-essentiality|Essential genes can be strain-specific, accessory, or highly divergent]]

- Use Fitness Browser condition-specific fitness values, focusing on genes with fitness < -2 under stress conditions, and test whether stress-important genes show stronger accessory or strain-specific enrichment than genes classified as essential under library-construction conditions. [src: conservation_vs_fitness]
- Combine Fitness Browser ortholog data with pangenome clusters and cross-species conservation statistics to identify essential gene families that recur across species while retaining strain-specific members. [src: conservation_vs_fitness]
- Analyze the 3,683 essential-auxiliary genes with functional annotation and genomic-context methods to test whether they compensate for missing core functions or instead represent mobile-element-associated dependencies. [src: conservation_vs_fitness]
- Re-run essentiality–conservation models after stratifying by pangenome clade size and coverage to determine how much the 1.56 median odds ratio depends on low-resolution core classifications. [src: conservation_vs_fitness]

## [[concepts/adaptive-versus-housekeeping-functional-differentiation|Adaptive Functions Differentiate More Strongly Than Housekeeping Functions Among Gene-Content Ecotypes]]

- Use the 1,820 genome-to-ecotype assignments and core-genome phylogenetic trees with phylogenetically controlled models to test whether the 2.13x adaptive-versus-housekeeping mean-effect-size ratio persists after accounting for shared ancestry. [src: ecotype_functional_differentiation]
- Extend the analysis from the 15-species stratified sample to all 456 eligible species and test whether the 79.8% versus 68.8% significance-rate contrast is consistent across genome-count bins and phylogenetic groups. [src: ecotype_functional_differentiation]
- Combine the ecotype assignments with habitat metadata and multivariate association methods to test whether the larger adaptive-category shifts predict environmental differences rather than only lineage structure. [src: ecotype_functional_differentiation]
- Analyze the 62% of gene clusters lacking COG annotations with AlphaFold or domain analysis to determine whether unannotated ecotype-differentiating genes are enriched for adaptive functions and whether the adaptive-versus-housekeeping contrast changes after their inclusion. [src: ecotype_functional_differentiation]
- Recluster the same genome-by-gene-content data with HDBSCAN and compare category-level significance and effect sizes with the KMeans results to test whether the conclusion depends on spherical-cluster assumptions and the selected value of k. [src: ecotype_functional_differentiation]

## [[concepts/adversarial-research-quality-assurance|Adversarial Validation of Computational Biology Claims]]

- Use the 9 adversarial review rounds and their identified failure classes to build a blinded checklist study, then measure which checks most often overturn a claim. [src: discoveries]
- Re-audit load-bearing citations against PubMed metadata and DOI records, then quantify the fraction of claims affected by PMID hijacking or hallucinated author lists. [src: discoveries]
- Reconstruct the M1–M26 revision history with a hypothesis-family map, then test whether each correction belongs to a pre-registered family or a post-hoc metric family. [src: discoveries]
- Execute representative BERDL analyses from lineage files and schema dictionaries, then measure how often stale catalogs, sentinel codes, or incomplete joins change the result. [src: discoveries]
- Benchmark cached CSV-based Spark workflows against direct `toPandas()` execution on joins involving the 2.5B-row UniProt identifier table, then identify reproducible thresholds for kernel failure and runtime degradation. [src: discoveries]

## [[concepts/environmental-resistome|Resistance Ecology Is Shaped by Annotation Completeness]]

- Re-annotate the 15,550 mechanism-unassigned clusters with broader homology, profile-HMM, and structure-based searches, then test whether environment-dependent mechanism fractions and effect sizes change. [src: amr_environmental_resistome]
- Compare AMRFinderPlus calls with independent resistance-gene resources and manually reviewed environmental candidates to quantify false-negative rates by environment and mechanism. [src: amr_environmental_resistome]
- Recalculate core and accessory AMR after stratifying species by genome-count depth, then test whether the clinical 68% versus soil 43% accessory contrast persists under matched sampling. [src: amr_environmental_resistome]
- Use metagenome-assembled genomes and isolate genomes with comparable annotation quality to test whether clinical enrichment remains after reducing differences in sampling and annotation coverage. [src: amr_environmental_resistome]
- Perform environment-specific gene identification on annotated and previously unclassified clusters, asking whether novel environmental candidates explain part of the observed metal-resistance enrichment. [src: amr_environmental_resistome]

## [[concepts/antimicrobial-resistance-fitness-cost|Fitness costs and conditional benefits of antimicrobial-resistance genes]]

- Use organism-stratified models on Cup4G11 (**77** AMR genes) and BFirm (**50** AMR genes) to test mechanism effects while controlling for genetic background. [src: amr_fitness_cost]
- Subclassify efflux pumps into narrow-spectrum drug pumps and general RND systems such as AcrAB-TolC, then test whether constitutively expressed systems have lower baseline costs. [src: amr_fitness_cost]
- Replace averages across non-antibiotic experiments with condition-specific analyses of metal, osmotic, and carbon-limitation stresses to test whether the baseline-cost estimate changes by environmental condition. [src: amr_fitness_cost]
- Cross-reference the **144** metal-resistance genes with fitness measurements and the metal fitness atlas to test whether genes costly under standard conditions are protective under metal stress. [src: amr_fitness_cost]
- Extend the analysis from **25** Fitness Browser organisms to all **293K** BERDL genomes by predicting AMR cost from gene-cluster conservation patterns and testing whether the laboratory-derived relationship generalizes across the broader genome collection. [src: amr_fitness_cost]

## [[concepts/gene-essentiality|Bidirectional fitness effects of core genes]]

- Reanalyze the Fitness Browser data with condition-stratified effect distributions and interaction terms to test whether the heavier positive and negative tails of core genes persist within matched assay conditions. [src: fitness_effects_conservation]
- Combine transposon coverage metrics with singleton and auxiliary-gene fitness estimates to distinguish true neutrality from callability-limited missing data. [src: fitness_effects_conservation]
- Compare single-gene knockout effects with multi-gene or combinatorial perturbation data to test whether epistasis explains additional bidirectional effects among core genes. [src: fitness_effects_conservation]
- Add environmental-condition data beyond rich media and standard stresses to test whether the core-gene cost-benefit pattern transfers to natural niche conditions. [src: fitness_effects_conservation]
- Use phylogenetically stratified models across the 43 bacteria to test whether the association between fitness breadth and core status is lineage-specific or broadly transferable. [src: fitness_effects_conservation]

## [[concepts/structural-annotation-gap|Reference-database coverage shapes genomic annotation inference]]

- Recompute the bridge using all 132,531,501 gene clusters, including the 70.7% without a successful AlphaFold entry, with identifier recovery and stratified missingness analysis to test whether the unrepresented population has a larger annotation gap. [src: alphafold_msa_annotation]
- Recalculate MSA depth and InterProScan richness by phylogenetically balanced taxon strata, using mixed-effects or stratified Spearman analyses, to determine how much of ρ = 0.7563 is driven by organism composition. [src: alphafold_msa_annotation]
- Compare representative-sequence MSA depths with member-level depths within gene clusters, using within-cluster distributions, to quantify whether representatives systematically overestimate or underestimate typical reference coverage. [src: alphafold_msa_annotation]
- Join the 415,603 core clusters with Fitness Browser measurements and test condition-specific associations between low MSA depth, hypothetical status, and fitness effects. [src: alphafold_msa_annotation]
- Reprocess the static version-6 AlphaFold snapshot against later UniProt deposits and compare MSA-depth changes, to measure how temporal database growth alters inferred annotation coverage. [src: alphafold_msa_annotation]

## [[concepts/biosynthetic-prototrophy-and-auxotrophy|Biosynthetic Prototrophy, Auxotrophy, and Nutrient Dependence]]

- Inspect lower-confidence GapMind predictions and records with a steps_missing status for *D. vulgaris* to determine whether the serine gap reflects a near-complete pathway rather than a true absence. [src: essential_metabolome]
- Test *D. vulgaris* growth on serine-free minimal medium and matched serine-supplemented medium to distinguish physiological auxotrophy from a computational detection gap. [src: essential_metabolome]
- Expand organism-to-genome mapping across the remaining 38 organisms and rerun GapMind to test whether the 17-of-18 amino-acid completeness pattern persists across broader phylogenetic coverage. [src: essential_metabolome]
- Combine GapMind with [[entities/eggnog]] EC-to-[[entities/kegg]] pathway analysis to test whether independent annotation pipelines recover the same serine and carbon-source capacities. [src: essential_metabolome]
- Link essential-gene calls directly to pathway membership and assay organisms in defined media to test whether predicted pathway completeness corresponds to condition-specific biosynthetic essentiality. [src: essential_metabolome]
- Stratify pathway gaps by phylogeny and ecology after expanding the sample to test whether nutrient dependence is associated with lineage or environment. [src: essential_metabolome]

## [[concepts/biosynthetic-self-sufficiency-and-cultivation|Cultured genomes do not necessarily capture extreme biosynthetic self-sufficiency]]

- Add Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge deep-subsurface MAGs, then compare GapMind and eggNOG amino-acid pathway completeness with the cultured cohort to test whether uncultured lineages contain more extreme self-sufficiency. [src: clay_confined_subsurface]
- Recalculate self-sufficiency from all standard amino-acid-biosynthesis EC numbers in eggNOG and compare the result with the 18-pathway GapMind score to determine whether the apparent deficit is a metric ceiling or a biological difference. [src: clay_confined_subsurface]
- Resolve Bacillota_B differences at genus level and repeat quality-filtered, phylum-stratified comparisons to test whether cohort composition explains the deep-versus-baseline pattern. [src: clay_confined_subsurface]
- Compare BRC-3 and BIC-A1 isolation sources directly, using genome completeness and pathway-level biosynthetic profiles, to test whether borehole source contributes to the observed cultivation bias. [src: clay_confined_subsurface]

## [[concepts/callability-limited-comparative-inference|Unequal evidence callability can make ecological contrasts untestable]]

- Re-run the groundwater-versus-necromass comparison after targeted PaperBLAST and PubMed/abstract-level searches promote dark compounds to callable status, then ask whether the source contrast remains after matching compounds by chemical class and evidence tier. [src: enigma_carbon_census_1]
- Apply a study-aware mixed model or sample-level permutation to NMDC and SSO metadata, using the available sample-level environment labels, and ask whether source-associated occurrence differences persist without treating every metagenome as an independent identically sampled observation. [src: enigma_carbon_census_1]
- Regenerate the committed callable tables after excluding R02107 and ask whether xanthine changes any class, source, or co-occurrence conclusion. [src: enigma_carbon_census_1]
- Test the 29 fully orphan compounds and the 6 biosynthesis-known/catabolism-unknown compounds with wet-lab enrichment and genome-resolved sequencing, asking whether the current source imbalance reflects true specialization or resource-level missingness. [src: enigma_carbon_census_1]
- Pair periphyton and soil metagenomes with compound-resolved measurements and metatranscriptomic or metaproteomic assays, asking whether the observed Burkholderiales/Comamonadaceae reservoir is active on the enrichment compounds. [src: enigma_carbon_census_1]

## [[concepts/capability-versus-kinetic-predictability|Genomic Capability Is More Predictable Than Continuous Growth Kinetics]]

- Use GenBank nucleotide sequences to compute codon usage bias and test whether it improves genus-blocked prediction of µmax, lag, and max_A, closing the gap left by the current bulk-feature regressions. [src: genotype_to_phenotype_enigma]
- Expand condition canonicalization from normalized names to ChEBI-ID-based matching and test whether increasing the estimated 42 molecular matches to 60–80 improves capability-model training coverage. [src: genotype_to_phenotype_enigma]
- Collect hundreds of genomes per condition and compare KO × condition models with pathway-level models to test whether the observed shift from genome-scale proxies to substrate-specific predictors persists at larger sample sizes. [src: genotype_to_phenotype_enigma]
- Perform retrospective subsampling that compares the 50 active-learning-ranked additions with random selection, testing whether the proposed design reduces false positives and false negatives more efficiently. [src: genotype_to_phenotype_enigma]
- Fit hierarchical or mechanistic kinetic models using growth-curve time series, expression or proteomic measurements, and genomic features to test whether adding regulatory and enzyme-abundance information resolves the negative cross-genus R² values. [src: genotype_to_phenotype_enigma]

## [[concepts/chemical-space-annotation-coverage-bias|Chemical representation biases metabolic utilization inference]]

- Apply PaperBLAST and abstract-level PubMed mining to the 74 organism-dark compounds, asking how many can be reclassified through literature evidence without new experiments. [src: enigma_carbon_census_1]
- Re-run the census with complementary annotation pipelines and explicit provenance tracking, asking whether the 29 fully orphan compounds remain chemically unrepresented or become linkable through alternative databases. [src: enigma_carbon_census_1]
- Regenerate all committed tables after removing R02107 from the carbon allowlist, asking whether xanthine changes the callable-set composition and downstream class comparisons. [src: enigma_carbon_census_1]
- Compare the callable and dark sets with calibrated, multiple-testing-corrected physicochemical models using a larger compound collection, asking whether Complexity, MolecularWeight, HeavyAtomCount, TPSA, and hydrogen-bond donors predict annotation status independently of chemical class. [src: enigma_carbon_census_1]
- Test the 74 dark compounds in targeted enrichment and measured-fitness experiments, beginning with the 29 fully orphan compounds and the 6 biosynthesis-known/catabolism-unknown compounds, asking which resource-defined gaps correspond to realized microbial utilization. [src: enigma_carbon_census_1]
- Use study-aware mixed models or sample-level permutations for soil-versus-freshwater comparisons, asking whether environmental occurrence of implicated genera predicts compound utilization after accounting for compositional and zero-inflated abundance data. [src: enigma_carbon_census_1]

## [[concepts/chromosomal-and-integrative-gene-transfer|Chromosomal and Integrative Routes of Horizontal Gene Transfer]]

- Use the unfiltered Spark data for a synteny-threshold permutation test to determine whether the ≤10 kb T4SS–CAZy co-occurrence exceeds a distance-matched null expectation. [src: t4ss_cazy_environmental_hgt]
- BLAST Node_4915 against NCBI nr to test whether its 8-phylum distribution and maximum divergence of 4.843 are consistent with homologous transfer rather than annotation or tree-reconstruction artifacts. [src: t4ss_cazy_environmental_hgt]
- Compare GT2–T4SS neighborhoods with housekeeping-gene neighborhoods as a null baseline to test whether the observed cross-phylum signal is specific to GT2-associated loci. [src: t4ss_cazy_environmental_hgt]
- Apply the proposed biome-enrichment factorization, θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)], to test whether co-occurrence reflects an interaction beyond the independent distributions of T4SS and CAZy genes. [src: t4ss_cazy_environmental_hgt]
- Combine ICEfinder calls, IME annotations, contig context, and long-read or closed-genome validation to determine whether the observed GT2 neighborhoods are chromosomal, integrative, or plasmid-associated. [src: t4ss_cazy_environmental_hgt]

## [[concepts/circularity-in-metabolic-model-validation|Gapfilled Models Can Make Their Own Validation Circular]]

- Reconstruct the 38 false-negative cases with gapseq and compare growth predictions and knockout outcomes to test whether reducing the 330 false positives changes the circularity of validation. [src: annotation_gap_discovery]
- Experimentally test the 44 high-confidence assignments, prioritizing rxn02185 and rxn03436 across 9 organisms, using targeted gene knockouts or CRISPRi and matched carbon-source growth assays. [src: annotation_gap_discovery]
- Hold out carbon sources or fitness experiments during model repair, then evaluate the 23 GPR-linked candidates against the withheld data to ask whether candidate-dependent growth generalizes beyond the evidence used for gapfilling. [src: annotation_gap_discovery]
- Compare model predictions before and after removal of each candidate reaction and pair the simulations with direct mutant fitness measurements to determine whether loss of predicted growth reflects biological gene requirement or a gapfilling dependency. [src: annotation_gap_discovery]

## [[concepts/classifier-database-compatibility-in-taxonomic-quantification|Classifier database compatibility limits cross-study taxonomic quantification]]

- Reclassify the same raw reads with matched, eukaryote-aware Kraken2, Centrifuge, and GOTTCHA2 databases, then use paired agreement analyses to determine which environmental contrasts persist after database scope is harmonized. [src: euk_in_prok_correlates]
- Build a study-held-out benchmark using the 9 NMDC studies and GroupKFold, with classifier identity and reference-database version as recorded covariates, to test whether environmental prediction improves after measurement compatibility is controlled. [src: euk_in_prok_correlates]
- Compare classifier-derived eukaryotic fractions with targeted plastid, fungal, and protist markers in the 1,186-run NEON subset, using within-study models to ask whether the GOTTCHA2 signal tracks distinct biological sources or database-specific detection. [src: euk_in_prok_correlates]
- Reconstruct pooled-run metadata from all contributing biosamples rather than the representative `MIN(biosample_id)` record, then test whether metadata-label uncertainty changes the within-study vegetation and geography associations. [src: euk_in_prok_correlates]

## [[concepts/sampling-depth-and-downsampling-effects|Clinical Sampling Bias and the Interpretation of Ecological Genomic Patterns]]

- Compare downsampled and full-genome gene-cluster extraction on the same species, using matched distance calculations, to determine why the median partial correlation changed from 0.003 to 0.081 and was characterized as a 27x difference. [src: ecotype_env_reanalysis]
- Add genome count as a covariate in the partial-correlation analysis to test whether unequal sampling depth inflates correlations in species with more genomes. [src: ecotype_env_reanalysis]
- Recompute correlations for transport, secondary-metabolism, and other functional gene subsets using the same environmental and human-associated groups to test whether whole-genome Jaccard distances mask ecological effects. [src: ecotype_env_reanalysis]
- Replace majority-vote categories with structured ENVO terms from env_broad_scale and repeat the group and continuous-fraction analyses to test whether finer environmental ontology changes the null result. [src: ecotype_env_reanalysis]
- Stratify or model NaN outcomes jointly with environment category, genome count, and phylogeny to test whether nonrandom missingness changes the Environmental versus Human-associated comparison. [src: ecotype_env_reanalysis]
- Compare AlphaEarth geographic signal with independent epidemiological and ecological metadata for species such as Klebsiella or Enterococcus to test whether embedding structure reflects regional epidemiology rather than ecological differentiation. [src: ecotype_env_reanalysis]

## [[concepts/cofitness-network-architecture|Cofitness Network Architecture, Organism Specificity, and Shared Dispensability]]

- Run AMR and non-AMR permutations matched on mean fitness, including the −0.05 to +0.05 range, and test whether flagellar and amino-acid enrichment persists; recompute truly-dark neighborhood enrichment with insertion-density and mean-fitness controls. [src: amr_cofitness_networks; truly_dark_genes]
- Recompute cofitness by antibiotic versus standard-growth conditions; measure mean fitness for flagellar knockouts; and test phage-defense and secondary-metabolite controls. [src: amr_cofitness_networks]
- Apply PADLOC MacSyFinder-style multi-PFam and gene-order rules to Retron, DISARM, and Gabija, then test whether the R-M Type II × Gabija syndrome survives stricter calls. [src: phage_defense_arsenal]
- Fit the defense–prophage relationship with a GTDB-tree phylogenetic mixed-effects model and refit the negative-binomial model with estimated dispersion. [src: phage_defense_arsenal]
- Compare Cas1-specific, EggNOG, and context-refined CRISPR-Cas calls, and determine whether defense-pair enrichment is stable across detection methods. [src: phage_defense_arsenal]
- Experimentally compare R-M Type II-only and R-M Type II-plus-Gabija species in matched phage-challenge assays. [src: phage_defense_arsenal]
- Expand defense analysis beyond seven systems and cross-reference defense syndromes with isolation-source metadata or AlphaEarth embeddings. [src: phage_defense_arsenal]
- Apply Pfam enrichment, replace the row-index operon heuristic with genomic coordinates, and reassess extra-operon network sizes. [src: amr_cofitness_networks]
- Reanalyze ICA with |weight| >= 0.3, a 50-gene cap, and a 40% component cap across organisms matched for experiment count. [src: fitness_modules]
- Experimentally test module-only, family-backed, and truly-dark top-100 predictions under module-informed conditions without treating them as exact KO assignments; prioritize PV4/5210953 motility, ANA3/7026383 nitrogen limitation, DvH/206658 stress, and Methanococcus_S2/MMP_RS06570 fluoride-efflux-associated tests. [src: fitness_modules; truly_dark_genes]
- Extend pangenome linkage to the 17,479 unlinked dark genes; test whether the estimated approximately 2,841 additional truly dark genes and their 2,208 estimated strong-phenotype subset are enriched in dark islands, mobile elements, or ICA modules. [src: truly_dark_genes]
- Use AlphaFold2 or ESMFold followed by Foldseek for the top 100 candidates, test growth under predicted conditions, apply mobile-CRISPRi, and distinguish polar effects from gene-autonomous phenotypes. [src: truly_dark_genes]
- Restrict cofitness–co-inheritance analyses to auxiliary-only pairs below 95% prevalence, build module co-transfer networks, and expand to species with >30% auxiliary genes. [src: cofitness_coinheritance]
- Recover raw genefitness data for Ralstonia UW163 and Ralstonia GMI1000 and add a well-populated far phylogenetic stratum. [src: cofitness_coinheritance]
- Map resistance islands to plasmids, chromosomes, integron boundaries, and insertion sequences, then stratify by island context and AMR ecotype. [src: amr_strain_variation]
- Test the ADP1 NADH-flux hypothesis by deleting NDH-2 across quinate, acetate, succinate, glucose, and lactate, then add benzoate, catechol, vanillate, iron limitation, and respiratory inhibitors. [src: aromatic_catabolism_network]
- Validate ACIAD3137 and ACIAD2176 by interaction or co-purification assays and compare Complex I retention across aromatic degraders. [src: aromatic_catabolism_network]
- Measure the complete 10-pair formulation matrix, repeat assays with PAO1 and 3–5 mucoid clinical PA isolates, and test structured biofilms. [src: cf_formulation_design]
- Classify 5,526 costly-and-dispensable genes as mobile, recently acquired, or undergoing loss, and test whether module membership distinguishes transient accessory architecture. [src: conservation_fitness_synthesis]
- Use AlphaEarth data to test whether environmental variability predicts core trade-offs; identify universally essential families; and test whether 48 accessory modules retain their co-inheritance advantage after phylogenetic and prevalence matching. [src: conservation_fitness_synthesis]
- Match metal and NaCl profiles on mean fitness and conservation, apply formal COG, KEGG, and Pfam enrichment, and use choline chloride or KCl controls with matched CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ experiments. [src: counter_ion_effects]
- Apply ICA to metal–NaCl matrices to test whether shared-stress modules explain condition-specific architecture. [src: counter_ion_effects]
- Hold ortholog scope and Pfam coverage constant when testing whether process-level module predictions replicate across 32 organisms. [src: discoveries]
- Test whether the 1.29× core enrichment and 17.8% trade-off rate persist after matching prevalence, mean fitness, organism, condition, and experimental coverage. [src: discoveries]
- Characterize 7,084 orphan essentials for mobile-element association, recent acquisition, rapid evolution, and missed divergent orthology. [src: essential_genome]
- Test the 1,382 module-transfer predictions by CRISPRi under module-informed conditions and link variable essentiality to pathway completeness. [src: essential_genome]
- Expand Fitness Browser taxonomic coverage and compare universal essential families with the Database of Essential Genes. [src: essential_genome]
- Test the 57,011 dark-gene spectrum using CRISPRi for essential candidates, RB-TnSeq or targeted deletion for non-essential candidates, and matched conditions across organisms; ask whether module, synteny, and cofitness evidence predicts reproducible phenotypes. [src: functional_dark_matter]
- Reanalyze the 1,256 GapMind gaps with direct EC and structure-based matching, then experimentally test the highest-confidence gene–pathway assignments rather than treating organism-level co-occurrence as assignment. [src: functional_dark_matter]
- Repeat lab–field validation with compositional-control permutations, annotated-accessory controls, genome-level AlphaEarth coverage, and sample-label permutation tests; determine whether the 29/47 concordance and NMDC directions remain gene-specific. [src: functional_dark_matter]
- Extend conservation and covering-set analyses beyond the Pseudomonadota-heavy Fitness Browser, then test whether the 42-organism set remains optimal after adding condition coverage and phylum balance. [src: functional_dark_matter]
- Recompute Producer × Participation classifications across matched taxonomic ranks and report leaf_consistency alongside module conservation to test whether apparently conserved architecture is uniform within clades. [src: gene_function_ecological_agora]
- Cross-validate the 17,073,194 Sankoff gain events with DTLOR or another reconciliation method, bootstrap individual acquisition-depth estimates, and test whether recent-to-ancient ratios persist after controlling for annotation density. [src: gene_function_ecological_agora]
- Obtain per-CDS sequence data and perform composition-based confirmation and full DTL reconciliation for M26 donor labels; test whether donor inference changes Open-Innovator classifications. [src: gene_function_ecological_agora]
- Repeat PSII, mycolic-acid, and PUL neighborhood scans with memory-scalable joins, and test whether the 10.91% PSII MGE-neighbor fraction remains distinct from the 10.6% Poisson baseline. [src: gene_function_ecological_agora]
- Expand Cyanobacteriia phenotype coverage beyond n = 4 and test whether AlphaEarth environmental clusters predict function-class architecture after phylogenetic and sampling controls. [src: gene_function_ecological_agora]
- Repeat metal cross-resistance with non-metal stress controls, normalize fitness by concentration relative to MIC, and use PGLS or independent contrasts to test whether positive directionality persists after phylogenetic correction. [src: metal_cross_resistance]
- Apply ICA to metal-condition matrices and compare universal-stress, metal-shared, and metal-specific modules after matching organisms for experiment count. [src: metal_cross_resistance]
- Map cross-resistance gene signatures with KEGG/PFAM across 27K species and test whether the 318 conserved ortholog groups predict metal-associated environments at pangenome scale rather than at the underpowered species scale. [src: metal_cross_resistance]
- Use AlphaFold-based structural analysis to test whether metal-shared proteins have convergent binding or stress-response features, and experimentally validate the strongest shared-versus-specific candidates. [src: metal_cross_resistance]
- Reanalyze module conservation after matching organisms for pangenome availability and experiment count, and test whether the 86.0% versus 81.5% core difference persists under alternative ICA thresholds and module-size caps. [src: module_conservation]
- Test whether the 38 accessory module families retain apparent co-inheritance or niche-specific signatures after controlling for phylogeny, prevalence, genome size, and annotation coverage; distinguish horizontal transfer from other causes of low core fraction. [src: module_conservation]
- Use CRISPRi or other perturbations to determine whether essential genes form condition-specific modules invisible to transposon-based ICA. [src: module_conservation]

## [[concepts/cofitness-network-architecture|Cofitness Networks Do Not Establish Direct Co-regulation]]

- Recompute AMR cofitness against random non-AMR genes matched to the same mean-fitness distribution, including the −0.05 to +0.05 range proposed in the report, and test whether flagellar and amino-acid-biosynthesis enrichment persists after mean-fitness matching. [src: amr_cofitness_networks]
- Partition fitness matrices into antibiotic-exposure and standard-growth conditions, then test whether support-network edges and functional enrichment are condition-specific or persist across both regimes. [src: amr_cofitness_networks]
- Compare direct regulatory evidence, such as shared transcription-factor targets or condition-specific expression responses, with cofitness edges to ask what fraction of high-|r| associations have independent support for co-regulation. [src: amr_cofitness_networks]
- Recalculate networks at |r| > 0.4 and |r| > 0.5, using coordinate-based operon exclusion rather than matrix row position, and test whether the organism-specificity and enrichment results remain stable. [src: amr_cofitness_networks]
- Measure mean fitness for flagellar knockouts and other conditionally dispensable gene classes under the same experimental conditions, then test whether their fitness profiles explain the AMR-neighborhood enrichment without invoking direct co-regulation. [src: amr_cofitness_networks]

## [[concepts/collection-site-versus-microenvironment-mismatch|Collection-Site Versus Organismal Microenvironment Mismatch]]

- Combine the 13,381-genome metadata table with direct environmental metadata and alternative embedding distances, then test whether environmental predictors improve gene-content associations after accounting for phylogenetic distance. [src: ecotype_analysis]
- Stratify the 172-species result by host-associated versus environmental lifestyle and replace collection coordinates with host, tissue, body-site, or other organism-proximal metadata where available; test whether the environmental effect changes. [src: ecotype_analysis]
- Use COG functional categories, including V-Defense and L-Mobile, instead of whole-genome gene content to ask whether collection-site mismatch obscures environment-associated variation in specific gene subsets. [src: ecotype_analysis]
- For species with identified ecotypes, compare gene content between ecotype clusters using organism-proximal environmental metadata and ask whether within-species contrasts recover associations missed by collection-site coordinates. [src: ecotype_analysis]

## [[concepts/community-metabolic-interdependence|Community Metabolic Interdependence and Black Queen Predictions]]

- Reanalyze the NMDC metabolomics samples with study-stratified correlations and leave-one-study-out validation to test whether the 11/13 directional pattern persists after reducing the influence of `nmdc:sty-11-r2h77870`, which contributed 125/131 samples (95%). [src: discoveries]
- Replace substring metabolite matching with identifier-validated KEGG or equivalent mappings, then retest leucine, isoleucine, and the previously untestable cysteine, histidine, and lysine pathways to determine whether the Black Queen pattern is mapping-sensitive. [src: discoveries]
- Combine sample-level metabolite abundances with genome-resolved pathway presence and condition-specific fitness measurements to test whether negative metabolite associations identify producers, consumers, or both. [src: discoveries]
- Test the tyrosine outlier using independent cohorts and targeted metabolomics to distinguish a real anti-Black-Queen relationship from cohort, annotation, or measurement effects. [src: discoveries]
- Compare pathway presence, pathway completeness, and measured metabolite pools across the 7 Fitness Browser organisms and 23 GapMind pathways to ask when Latent Capabilities become realized community dependencies. [src: discoveries]

## [[concepts/comparative-conservation-metric-calibration|Calibrating Conservation Metrics for Unknown Bacterial Genes]]

- Recalculate the same dark-gene rankings with matched reference sets and identical ortholog-group definitions, then test whether the 62% top-50 and 58% top-100 overlap values improve when database breadth is held constant. [src: functional_dark_matter]
- Compare kingdom-, phylum-, class-, family-, genus-, and species-level conservation scores against independent fitness measurements to test which taxonomic resolution best predicts experimentally measurable phenotypes. [src: functional_dark_matter]
- Use bootstrap resampling of species and phyla in the 93.5M gene-cluster reference to quantify confidence intervals for conservation ranks and identify candidates whose priority is database-sensitive. [src: functional_dark_matter]
- Re-run the 42-organism covering-set optimization under alternative conservation metrics and compare coverage of the 28,584 high-priority dark genes, asking whether the selected experimental panel is robust to metric choice. [src: functional_dark_matter]
- Test whether conservation-weighted candidates outperform fitness-only candidates in CRISPRi or RB-TnSeq follow-up, separating broad conservation from experimentally validated functional importance. [src: functional_dark_matter]

## [[concepts/competitive-exclusion-consortium-design|Designing Protective Microbial Consortia Requires Joint Optimization of Inhibition, Coverage, Safety, and Engraftability]]

- Measure the complete 10-pair interaction matrix for the five-species core with the RFU-based competition assay, then test whether pairwise effects are additive, synergistic, or antagonistic. [src: cf_formulation_design]
- Repeat inhibition and growth-kinetic assays with PAO1 and 3–5 mucoid clinical PA isolates, then ask whether the ranking of k=2 and k=3 formulations transfers beyond PA14. [src: cf_formulation_design]
- Test the candidate consortia in structured biofilm airway models using the omitted substrates and airway-relevant components, then determine whether planktonic inhibition predicts biofilm suppression. [src: cf_formulation_design]
- Administer the k=2 and k=3 formulations in an in vivo engraftment model and quantify persistence of each species, directly testing whether inferred engraftability predicts establishment. [src: cf_formulation_design]
- Experimentally test xylitol, myoinositol, xylose, and arabinose supplementation with the candidate commensals and PA, asking whether the predicted pathway gaps create selective commensal growth without increasing PA growth. [src: cf_formulation_design]
- Recompute the multi-objective ranking with uncertainty intervals for inhibition, coverage, safety, and measured engraftment, asking whether the recommended formulation remains optimal when inferred objectives are replaced by direct measurements. [src: cf_formulation_design]

## [[concepts/complementary-annotation-pipelines|Complementary Annotation Pipelines Rescue Functional Inference]]

- Join the 17.6M Bakta UniRef50 identifiers against a refreshed BERDL UniProt identifier table, and quantify how much downstream functional evidence becomes recoverable after the missing identifier coverage is addressed. [src: discoveries]
- Build a gold-standard subset with experimentally characterized proteins, then compare Bakta-only, eggNOG-only, and union annotations by precision and recall rather than coverage alone. [src: discoveries]
- Stratify the 11.2M Bakta-rescued clusters by COG, KEGG, Pfam, GO, product-description, and UniRef50 evidence to determine which annotation classes contribute most to functional recovery. [src: discoveries]
- Test whether pipeline-specific annotations alter downstream resistome, pangenome, or dark-gene conclusions by rerunning the same analyses with Bakta-only, eggNOG-only, and provenance-filtered union annotations. [src: discoveries]

## [[concepts/composite-functional-annotation|Composite Functional Categories Can Represent Multifunctional Genes]]

- Reanalyze the 32-species dataset using alternative COG and [[entities/eggnog]] annotation versions, then test whether the LV enrichment remains +0.34% and 76% consistent. [src: cog_analysis]
- Compare composite assignments with gene-neighborhood, domain, and experimental-function evidence to test whether LV genes represent linked mobile-and-defense modules rather than annotation artifacts. [src: cog_analysis]
- Expand the taxonomic sample beyond the 32 analyzed species and test whether composite-category enrichment is conserved across additional phyla or varies by lineage. [src: cog_analysis]
- Stratify composite-category distributions by environmental metadata to test whether multifunctional mobile-and-defense annotations vary by habitat. [src: cog_analysis]

## [[concepts/composite-resistance-score-limitations|Limits of Composite Resistance Scores for Mechanistic Inference]]

- Match BacDive strains to GTDB genomes using GCA accessions and repeat the phenotype-to-score analysis to test whether the 38.4% species-name matching rate limited mechanistic resolution. [src: bacdive_phenotype_metal_tolerance]
- Replace the composite score with per-metal scores and use PGLS (phylogenetic generalized least squares) or phylogenetic PCA to test whether catalase predicts copper, urease predicts nickel, and H₂S production predicts zinc, copper, or cadmium tolerance after removing phylogenetic signal. [src: bacdive_phenotype_metal_tolerance]
- Assemble urease-positive and urease-negative organisms within the same taxonomic classes and apply [[entities/tnseq]] or [[entities/crispri]] under nickel and other metals to test nickel-specific mechanisms rather than general composite tolerance. [src: bacdive_phenotype_metal_tolerance]
- Experimentally test the H₂S hypothesis with balanced positive and negative controls under zinc, copper, and cadmium exposure to determine whether the observed d = -0.867 was a small-sample artifact. [src: bacdive_phenotype_metal_tolerance]
- Compare composite-score predictions with direct Fitness Browser growth or fitness measurements across matched organisms and metals to determine which resistance-gene features predict measured tolerance rather than a derived genome-based score. [src: bacdive_phenotype_metal_tolerance]

## [[concepts/computational-pathway-prediction-validation|Pathway-completeness predictions gain support from matched growth phenotypes]]

- Map the 601 unique significant Fitness Browser genes and 4,764 total significant gene-condition hits onto individual GapMind pathway steps using the deferred NB04 analysis, and ask whether the 13/13 pathway–growth agreement is explained by pathway-specific genes rather than shared housekeeping requirements. [src: fw300_metabolic_consistency]
- Repeat the GapMind–Fitness Browser comparison for other ENIGMA isolates, including *Pseudomonas stutzeri* RCH2, and ask whether the observed 13/13 agreement generalizes across organisms. [src: fw300_metabolic_consistency]
- Compare complete GapMind predictions with growth across multiple media and single-substrate conditions, and ask how often pathway completeness remains predictive when environmental context changes. [src: fw300_metabolic_consistency]
- Integrate WoM metabolite profiles with GapMind predictions and community metabolic modeling to test whether predicted biosynthetic capacity explains tryptophan secretion and potential cross-feeding in the Oak Ridge groundwater community. [src: fw300_metabolic_consistency]

## [[concepts/condition-dependent-gene-tradeoffs|Condition-Dependent Gene Fitness Trade-Offs]]

- Use the Fitness Browser condition matrix together with environmental metadata and condition-specific fitness models to test whether genes classified as Costly + Conserved become beneficial or less costly under ecologically relevant conditions, addressing the gap between laboratory burden and natural selection. [src: core_gene_tradeoffs]
- Reanalyze the 25,271 trade-off genes with functional-category stratification and phylogenetically controlled models to determine whether the 1.29-fold core enrichment is driven by particular lineages or pathways. [src: core_gene_tradeoffs]
- Compare the 28,017 Costly + Conserved genes with direct field or host-associated fitness measurements to test whether their conservation is consistent with purifying selection rather than condition sampling or annotation bias. [src: core_gene_tradeoffs]
- Repeat conservation mapping with similarity thresholds below and above 90% identity, followed by targeted homology searches, to quantify how rapidly evolving genes affect the trade-off classification. [src: core_gene_tradeoffs]
- Test whether the -1 and 1 fitness cutoffs alter the number and functional composition of trade-off genes by applying preregistered alternative thresholds to the same per-gene measurements. [src: core_gene_tradeoffs]

## [[concepts/condition-space-dimensionality|Condition-space dimensionality separates general sensitivity from substrate-specific requirements]]

- Measure the same deletion collection across an expanded condition panel and use PCA or independent component analysis to test whether the approximately 5-dimensional structure remains stable or increases with substrate diversity. [src: adp1_deletion_phenotypes]
- Replicate the single-timepoint growth measurements with technical replicates and quantify measurement error to test whether condition-specificity scores ≥ 1.0 distinguish biological substrate requirements from noise. [src: adp1_deletion_phenotypes]
- Map the 625 condition-specific genes onto pathway annotations and compare their loadings across conditions to determine which metabolic modules define the additional axes beyond general sensitivity. [src: adp1_deletion_phenotypes]
- Test the hypothesis that quinate and protocatechuate catabolism impose distinctive respiratory-chain demands by measuring respiratory Complex I mutants under quinate, glucose, and related aromatic substrates. [src: adp1_deletion_phenotypes]
- Reanalyze the 24-gene quinate module with additional aromatic substrates to test whether it is specific to quinate or represents a broader aromatic-catabolism axis. [src: adp1_deletion_phenotypes]

## [[concepts/condition-specific-fitness|Condition-Specific Mutant Fitness]]

- Use the 8-carbon-source mutant-fitness matrix with pathway enrichment to test weak urea correlations, and compare ADP1 profiles with comparable organisms. [src: acinetobacter_adp1_explorer]
- Add measured trace aromatic compounds to condition-specific FBA media; construct an ADP1 NDH-2 deletion mutant and measure NADH/NAD⁺ ratios and growth on quinate, glucose, acetate, lactate, and urea. [src: adp1_triple_essentiality; respiratory_chain_wiring]
- Directly map GapMind per-step genes to Fitness Browser fitness and essentiality, test whether the 15.8% latent fraction persists under independent thresholds, and extend the comparison beyond the 7 organisms with matching genomes. [src: metabolic_capability_dependency; pathway_capability_dependency]
- Test variable-pathway–openness relationships with full phylogenetic independent contrasts and matched genome-count sampling within the 18 genera. [src: pathway_capability_dependency]
- Test whether accessory-dependent leucine, valine, arginine, lysine, and threonine pathways predict measured metabolite exchange rather than genomic potential; obtain paired metabolomics for the 33 Freshwater samples and metatranscriptomics for expressed pathway completeness. [src: pathway_capability_dependency; nmdc_community_metabolic_ecology]
- Test metal cross-resistance with non-metal controls, MIC-relative dose normalization, and PGLS or independent contrasts; recompute metal-specificity fractions across 1–20% sick-rate thresholds. [src: metal_cross_resistance; metal_specificity]
- Match Fitness Browser organisms to ENIGMA CORAL genomes at species or strain level, and fit multivariate models to Oak Ridge samples while controlling for pH, redox, and carbon sources. [src: lab_field_ecology]
- Reanalyze the lignin experiment with DADA2 ASVs, larger replication, UNITE-based ITS taxonomy, phylogenetic diversity, and strain-resolved functional assays. [src: lignin_community_enrichment]
- Use plant-associated genome sets to test whether compartment markers predict matched condition-specific fitness with genus-blocked validation and transcriptomics; expand phylogenetic coverage and apply sparse PGLMMs. [src: plant_microbiome_ecotypes]
- Test SNIPE–ManXYZ coupling directly with matched strains, ManXYZ fitness assays on D-mannose and D-glucosamine, and phage challenge. [src: snipe_defense_system]
- For truly dark genes, extend pangenome linkage to the 17,479 unlinked genes; use AlphaFold2 or ESMFold and Foldseek for the top 100 candidates; test PV4/5210953 on motility, ANA3/7026383 under nitrogen limitation, and selected candidates with mobile-CRISPRi; characterize dark islands and perform a Methanococcus-focused analysis using cofitness signals reported as r > 0.97. [src: truly_dark_genes]
- Reanalyze dark-gene condition distributions in a matched matrix controlling for gene length, insertion density, organism, and polar effects, and test whether cofitness-module predictions improve experimental prioritization. [src: truly_dark_genes]

The detailed analyses are available in [[summaries/adp1_deletion_phenotypes__REPORT]], [[summaries/adp1_triple_essentiality__REPORT]], [[summaries/aromatic_catabolism_network__REPORT]], [[summaries/conservation_fitness_synthesis__REPORT]], [[summaries/core_gene_tradeoffs__REPORT]], [[summaries/costly_dispensable_genes__REPORT]], [[summaries/counter_ion_effects__REPORT]], [[summaries/essential_genome__REPORT]], [[summaries/essential_metabolome__REPORT]], [[summaries/field_vs_lab_fitness__REPORT]], [[summaries/fitness_effects_conservation__REPORT]], [[summaries/fitness_modules__REPORT]], [[summaries/functional_dark_matter__REPORT]], [[summaries/genotype_to_phenotype_enigma__REPORT]], [[summaries/ibd_phage_targeting__REPORT]], [[summaries/lab_field_ecology__REPORT]], [[summaries/lignin_community_enrichment__REPORT]], [[summaries/metabolic_capability_dependency__REPORT]], [[summaries/metal_cross_resistance__REPORT]], [[summaries/metal_fitness_atlas__REPORT]], [[summaries/metal_specificity__REPORT]], [[summaries/nmdc_community_metabolic_ecology__REPORT]], [[summaries/pathway_capability_dependency__REPORT]], [[summaries/plant_microbiome_ecotypes__REPORT]], [[summaries/respiratory_chain_wiring__REPORT]], [[summaries/snipe_defense_system__REPORT]], and [[summaries/truly_dark_genes__REPORT]].

## [[concepts/confirmatory-exploratory-ecological-association-discordance|Confirmatory Nulls and Exploratory Signals in Ecological Association Testing]]

- Replace broad COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries, then test whether the confirmatory contamination association remains null at finer functional resolution. [src: enigma_contamination_functional_potential]
- Add species- or strain-level ENIGMA or metagenomic data and repeat the confirmatory and coverage-adjusted models to test whether genus-level aggregation masks adaptation. [src: enigma_contamination_functional_potential]
- Fit models including depth, location cluster, sampling date, and compositional controls, using mixed-effects or hierarchical structure, to determine whether the exploratory defense association persists beyond coarse `location_prefix` adjustment. [src: enigma_contamination_functional_potential]
- Investigate the 862 unmapped genera and expand the genus-to-clade bridge to test whether missing coverage changes the direction or magnitude of the contamination–functional association. [src: enigma_contamination_functional_potential]
- Reanalyze the 212 sample-fraction rows with preregistered fraction-stratified and pooled contrasts to determine whether the pooled exploratory signal can be reproduced across the `0.2_micron_filter` and `10_micron_filter` fractions. [src: enigma_contamination_functional_potential]

## [[concepts/continuous-versus-modular-phenotype-landscapes|Continuous Versus Modular Phenotype Landscapes]]

- Measure the same deletion collection across an expanded condition panel and use PCA or independent component analysis (ICA) to test whether the approximately 5 observed dimensions persist and whether additional pathway-specific modules emerge. [src: adp1_deletion_phenotypes]
- Repeat the 8-condition growth measurements with technical replicates and time-course assays to determine whether the 24-gene quinate module and its mean quinate z-score of -7.28 exceed measurement noise. [src: adp1_deletion_phenotypes]
- Compare single-gene deletion profiles with chemical-genetic profiles using the same clustering, silhouette, and FDR procedures to test whether perturbation type changes the balance between continuous gradients and discrete modules. [src: adp1_deletion_phenotypes]
- Test the 51-gene quinate-specific set experimentally, including the respiratory Complex I subunits, to determine whether aromatic catabolism creates distinctive electron-transport-chain demands. [src: adp1_deletion_phenotypes]

## [[concepts/core-gene-annotation-paradox|Conserved Core Genes Can Remain Structurally and Functionally Uncharacterized]]

- Join the 415,603 low-MSA core clusters to [[entities/kescience-fitnessbrowser]] measurements and use condition-specific fitness analysis to ask whether structurally isolated core proteins have essential or condition-dependent phenotypes. [src: alphafold_msa_annotation]
- Recompute MSA depth and InterPro-family richness after stratifying the 38,051,842 bridged pairs by pangenome class and organismal lineage, using Spearman correlations and balanced taxon sampling to ask whether the ρ = 0.7563 relationship is consistent across taxa. [src: alphafold_msa_annotation]
- Compare representative-sequence MSA depths with member-level sequence diversity for the 415,603 low-MSA core clusters, using within-cluster pangenome sequence analysis to ask whether representatives conceal deeper or shallower support among cluster members. [src: alphafold_msa_annotation]
- Prioritize the 286,439 hypothetical low-MSA core clusters for structure prediction and experimental characterization, using the 137 EC-annotated and 346 KEGG-mapped clusters as annotated comparators to ask which structural features predict recoverable function. [src: alphafold_msa_annotation]
- Extend the bridge analysis to the 70.7% of clusters without AlphaFold MSA depth, using alternative sequence-similarity and domain resources to ask whether the unbridged population contains a larger conserved annotation gap. [src: alphafold_msa_annotation]

## [[concepts/core-genome-burden-paradox|The Core-Genome Burden Paradox]]

- Use the 5,526 costly-and-dispensable genes, mobile-element annotations, and comparative-genomic analyses to test whether these genes are enriched for mobile elements, recent acquisitions, or signatures of gene loss. [src: conservation_fitness_synthesis]
- Combine core-versus-accessory status, laboratory fitness measurements, and AlphaEarth environmental data with statistical tests to ask whether organisms from more variable environments contain more trade-off genes in their core genomes. [src: conservation_fitness_synthesis]
- Analyze the 43-organism conservation and fitness dataset with cross-species comparative methods to identify gene families that are universally essential across all 43 organisms. [src: conservation_fitness_synthesis]
- Reanalyze the 48 accessory modules containing exclusively flexible-genome co-regulated functions with module-level fitness and conservation data to determine whether they represent coherent adaptive programs. [src: conservation_fitness_synthesis]
- Pair RB-TnSeq measurements with fitness assays in soil, biofilm, and host-associated conditions to test whether laboratory-burdensome conserved genes become beneficial in natural-environment proxies. [src: conservation_fitness_synthesis]

## [[concepts/costly-dispensable-gene-loss|Evolutionary loss of costly, non-conserved genes]]

- Reanalyze gene presence as a continuous fraction of pangenome genomes, rather than a binary core/accessory label, and test whether increasing laboratory burden predicts decreasing prevalence after controlling for organism and gene length. [src: costly_dispensable_genes]
- Re-link Fitness Browser genes to pangenomes with sequence-similarity-sensitive homology methods and manual synteny checks to determine how many apparent costly+dispensable genes were missed or misclassified by the 90% identity DIAMOND threshold. [src: costly_dispensable_genes]
- Compare longitudinal genomes or closely related strain phylogenies for mobile-element-rich costly genes to test whether their loss, retention, or pseudogenization follows the predicted burden-associated pattern. [src: costly_dispensable_genes]
- Test *Pseudomonas stutzeri* RCH2 against related strains using mobile-element annotation, genome architecture, and phylogenetic reconstruction to distinguish recent invasion from strain-specific genomic expansion. [src: costly_dispensable_genes]
- Measure the 14.1% condition-specific subset across community, host-associated, and environmental conditions using targeted competition assays to ask whether context-specific benefits explain persistence of costly+dispensable genes. [src: costly_dispensable_genes]

## [[concepts/coverage-confounding-of-community-functional-scores|Mapped Coverage Constrains Community Functional Associations]]

- Replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries, then test whether contamination associations persist after mapped-coverage adjustment. [src: enigma_contamination_functional_potential]
- Add species- or strain-level ENIGMA or metagenomic data and test whether finer taxonomic resolution reduces unmapped abundance and changes the defense association. [src: enigma_contamination_functional_potential]
- Fit models including depth, location cluster, sampling date, and compositional controls to determine whether coverage-adjusted associations survive richer confounding control. [src: enigma_contamination_functional_potential]
- Investigate the functional contribution of unmapped genera and expand the genus-to-clade bridge to determine whether missing coverage drives the observed score instability. [src: enigma_contamination_functional_potential]
- Fit mixed-effects or hierarchical site models using well- or location-level structure to test whether the exploratory defense associations persist beyond coarse `location_prefix` effects. [src: enigma_contamination_functional_potential]
- Compare the detailed results with [[summaries/enigma_contamination_functional_potential__REPORT]] and integrate the workflow with [[concepts/multi-omics-integration]] to quantify how geochemistry, community composition, pangenome mapping, and functional annotation jointly constrain inference. [src: enigma_contamination_functional_potential]

## [[concepts/cross-cohort-microbiome-portability|Cross-Cohort Portability of Microbiome Classifiers and Metabolomics]]

- Re-run the metabolomics comparison with ComBat, SVA, RUV, and quantile normalization on the same 122 m/z-bridge metabolites, then test whether cohort separation and LOSO ARI decline without erasing diagnosis-associated structure. [src: discoveries]
- Evaluate external-cohort calibration using the pooled classifier on the UC Davis cohort, testing whether recalibration and a non-constant `is_ibd` design improve the 41% agreement and reduce the 19/22 E1 assignments. [src: discoveries]
- Harmonize MetaPhlAn3 and Kaiju species namespaces, quantify the effect of restoring the 46% of training species not detected in Kuehl, and test whether projected ecotype proportions remain stable across feature spaces. [src: discoveries]
- Reproduce the *C. scindens* and Tier-A candidate analyses with within-substudy CLR effects, leakage-free splits, and independent cohort replication to determine which biomarkers retain sign and effect size. [src: discoveries]
- Compare curator-validated MetaCyc hierarchy assignments against regex categories in held-out cohorts, asking whether iron/heme acquisition remains associated with IBD when pathway definitions are fixed before testing. [src: discoveries]
- Extend [[concepts/multi-omics-integration]] by linking strain-level genomic content, metabolite measurements, and abundance across cohorts, while testing whether species-abundance-mediated and strain-content-mediated signals transfer differently. [src: discoveries]

## [[concepts/cross-condition-metabolic-comparability|Metabolic evidence is condition-dependent across assays and databases]]

- Map the 601 unique Fitness Browser genes and 4,764 significant gene-condition hits to GapMind pathway steps using the deferred NB04 analysis, and test whether genes associated with FW300-N2E3 tryptophan production are biosynthetic, catabolic, or regulatory. [src: fw300_metabolic_consistency]
- Repeat the four-database comparison for additional ENIGMA isolates, including *Pseudomonas stutzeri* RCH2, and test whether the observed concordance and discordance patterns are isolate-specific or reproducible across organisms. [src: fw300_metabolic_consistency]
- Expand Web-of-Microbes–BacDive matching with InChIKey or CHEBI identifiers, and test whether identifier-based joining increases the 8/58 BacDive match count without conflating biologically distinct compounds. [src: fw300_metabolic_consistency]
- Use community metabolic modeling for the Oak Ridge groundwater community to test whether FW300-N2E3 tryptophan secretion can support auxotrophic community members under the relevant environmental conditions. [src: fw300_metabolic_consistency]
- Compare FW300-N2E3 Web-of-Microbes profiles across growth media to test which metabolites are constitutive and which are medium-dependent. [src: fw300_metabolic_consistency]

## [[concepts/cross-species-fitness-transferability|Ortholog-transferred fitness phenotypes are constrained by organism-specific network architecture]]

- Measure Complex I and NDH-2 deletion fitness directly in ADP1 on quinate, glucose, acetate, and succinate to test whether the phenotype tracks aromatic catabolism or NADH-generating substrate load. [src: aromatic_catabolism_network]
- Search the ADP1 genome for NDH-2 and combine deletion experiments with respiratory-capacity measurements to determine whether alternative NADH dehydrogenase activity explains the glucose and lactate results. [src: aromatic_catabolism_network]
- Stratify the [[entities/kescience-fitnessbrowser]] ortholog-transferred data by organism and respiratory-chain architecture, then compare effect sizes across architectures to quantify transferability. [src: aromatic_catabolism_network]
- Expand comparative pangenome analysis across aromatic-degrading species to test whether Complex I retention and NDH-2 presence predict transferred fitness phenotypes. [src: aromatic_catabolism_network]
- Rebuild the ADP1 FBA model with PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints, then test whether architecture-aware constraints reduce the gap between predicted 0% essentiality and the observed defects in 10/13 Complex I subunits. [src: aromatic_catabolism_network]

## [[concepts/cross-tenant-data-bridging|Schema-Level Bridges and Validated Cross-Tenant Data Integration]]

- Execute UC2–UC5 on the live cluster with provenance, authority, currency, identifier, overlap, and evidence checks. [src: berdl_data_atlas]
- Add authority, tenant, scale, provenance, and `max(committed_at)` to inventory; compare `nmdc.metadata` and `nmdc.ncbi_biosamples` with upstream counts and repair NMDC schema, skill, documentation, aliases, and user copies. [src: nmdc_context_audit]
- Build a live-catalog harness for dotted/underscore namespaces, canonical identifiers, data types, plausible row counts, join overlap, and provenance; use Spark-native workflows, parquet checkpoints, explicit casts, and finalization logs. [src: pitfalls]
- For prophage ecology, validate eggNOG calls with geNomad or VIBRANT, quantify false positives and domesticated remnants, repeat NMDC burden inference against directly detected prophages, and test whether pH and other abiotic correlations persist within study and genus. [src: prophage_ecology]
- Test whether human-associated tail, head, and anti-defense enrichment reflects phage exposure or counter-defense by integrating direct phage detection, host range, and matched environmental metadata; characterize whether TerL specialists persist after finer taxonomy and sampling controls. [src: prophage_ecology]
- Combine NMDC metabolomics, proteomics, and lipidomics with UC4/UC5 and prophage-module bridges, preserving the distinction between occurrence, activity, and mechanism. [src: berdl_data_atlas, prophage_ecology]
- Ingest UC1 residue-level pLDDT and structural features and test them across the 55,454-gene cohort; restrict fitness-to-pangenome analyses to auxiliary-only pairs below 95% prevalence. [src: berdl_data_atlas, cofitness_coinheritance]
- Link the 129,823 PaperBLAST VIMSS cross-references to Fitness Browser values, stratify by organism and family literature coverage, and distinguish missing PMC coverage from missing biology. [src: paperblast_explorer]
- Reproduce ecotype analyses with downsampled and full-genome extraction, genome-count covariates, structured ENVO terms, study-aware validation, and within-substudy contrasts. [src: ecotype_env_reanalysis, pitfalls]
- Apply GTDB-Tk-verified identifiers, quantify the 12 collision-derived mismatches, and retest environmental profiles; compare GTDB and KBase assignments through `genome_id` and `ncbi_taxon_id`. [src: genotype_to_phenotype_enigma, berdl_data_atlas]
- Pair environmental occurrence with compound-specific enrichment and measured fitness; expand WoM–BacDive matching with InChIKey or CHEBI identifiers and test tryptophan cross-feeding. [src: enigma_carbon_census_1, fw300_metabolic_consistency]
- Use exact-name ModelSEED links separately from formula-only candidate sets, manually curate the 900 formula-expanded molecules, and quantify how compound ambiguity changes pathway and fitness conclusions. [src: webofmicrobes_explorer]
- Obtain the current GNPS2 or Northen laboratory WoM dataset, determine whether consumption actions are available, and repeat the production–utilization–fitness analysis with versioned provenance. [src: webofmicrobes_explorer]
- Test whether `E/(E+I)` metabolic novelty associates with pangenome openness or accessory gene content, using strain-to-genome mappings and species-level rather than genus-only joins. [src: webofmicrobes_explorer]
- Apply GroupKFold by study and within-study contrasts to NMDC eukaryotic-fraction models, harmonize classifier databases, and test replication outside NEON soil. [src: euk_in_prok_correlates]
- Extend field-versus-lab analyses to organisms with both environmental and gene-level fitness data; quantify gene-cluster prevalence and acquisition history for metal and antibiotic resistance. [src: field_vs_lab_fitness]
- Query INPHARED and IMG/VR for phages targeting *H. hathewayi*, *F. plautii*, and *M. gnavus*, validating host range against patient isolates. [src: ibd_phage_targeting]
- Reproduce the reduced IBD Tier-A list with held-out-feature clustering, leave-one-species-out refitting, study-aware validation, and within-substudy contrasts. [src: pitfalls]

## [[concepts/cultivation-collection-bias-in-ecological-genomics|Cultivation and collection bias constrain ecological genomic inference]]

- Match BacDive GCA accessions directly to pangenome genome_ids through `kbase_ke_pangenome.genome`, then test whether recovered strains change the contamination effect estimates and the 56.6% unmatched fraction. [src: bacdive_metal_validation]
- Integrate ENIGMA CORAL community data from the Oak Ridge metal-contaminated site and compare community-level metal-tolerance profiles with BacDive isolation-source predictions to test whether the culture-collection signal generalizes to field communities. [src: bacdive_metal_validation]
- Stratify matched BacDive strains by metal-tolerance gene families and contamination environment, using metals with sufficient representation including iron and manganese, to test whether specific functions predict specific environments. [src: bacdive_metal_validation]
- Expand BacDive phenotype extraction beyond the `metabolite_utilization` table to include MIC and growth-inhibition data, then test whether independently measured tolerance agrees with genome-derived scores. [src: bacdive_metal_validation]
- Reanalyze contamination effects within taxonomic strata and after genome-size normalization, using the small Bacillota and Bacteroidota groups to determine whether their null results reflect biology or limited power. [src: bacdive_metal_validation]

## [[concepts/data-landscape-ownership-and-coverage-bias|Agency and Tenant Ownership Shape Biological Data Coverage]]

- Re-audit all 66 BERIL projects using README files, notebooks, research plans, and workflow metadata to test whether the observed tenant breadth remains a lower bound and whether underused owners contribute more realized data sources than reported. [src: berdl_data_atlas]
- Recompute agency and tenant concentration after deduplicating shared records across refdata, KBase, ENIGMA, and genome-depot layers to determine how much of the apparent ownership imbalance reflects duplicated inventory. [src: berdl_data_atlas]
- Execute UC2–UC5 with value-space validation for their proposed join keys to test whether ownership-separated datasets provide usable biological coverage rather than only schema-level bridges. [src: berdl_data_atlas]
- Compare topic-level scientific conclusions with and without tenant or agency-stratified sampling to measure whether dominant owners alter observed associations, taxonomic coverage, or phenotype distributions. [src: berdl_data_atlas]
- Verify the evaluation and lambda agency mappings against program documentation and assess whether correcting the 4 affected tables changes agency concentration estimates. [src: berdl_data_atlas]

## [[concepts/ec-less-reaction-annotation|EC-Less Reactions Are a Distinct Annotation-Resolution Barrier]]

- Use the 50 EC-less reactions and their 201 reaction-organism records to compare alternative stoichiometric gapfilling solutions with gapseq reconstructions, asking which reactions remain stable across reconstruction methods. [src: annotation_gap_discovery]
- Combine sequence profiles, structure-based searches, and targeted biochemical assays for the 42 unresolved EC-less reaction-organism pairs, asking whether enzyme families can be assigned without an existing EC identifier. [src: annotation_gap_discovery]
- Reanalyze the 50 EC-less reactions with the 23 available GPR insertions and targeted gene-knockout or CRISPRi experiments, asking whether phenotype changes distinguish competing candidate genes without relying on circular model growth requirements. [src: annotation_gap_discovery]
- Expand the EC-less analysis from the 14-organism dataset to all 48 Fitness Browser organisms, asking whether the 16% EC-less resolution rate is reproduced across broader phylogenetic and annotation coverage. [src: annotation_gap_discovery]
- Integrate the 104 GapMind-gapfill pathway pairings with reaction-level annotation and additional pathway databases, asking whether step-level evidence can recover EC-less functions outside the approximately 80 pathways covered by GapMind. [src: annotation_gap_discovery]

## [[concepts/ecological-memory|Ecological memory preserves community differences across changing environments]]

- Increase replication to n>=5 per group and repeat the Round-1/Round-2 factorial design to test whether the history effect and the ~0.50 memory index remain stable. [src: lignin_community_enrichment]
- Use DADA2 amplicon sequence variants, phylogenetic diversity, and UniFrac distances on the existing 16S data to determine whether ecological memory persists beyond 97% OTU definitions. [src: lignin_community_enrichment]
- Cross-reference persistent Pseudomonas, Acinetobacter, and Comamonas lineages with [[entities/kbase-ke-pangenome|kbase_ke_pangenome]] and test whether retained gene-content differences explain the L-versus-LC legacy. [src: lignin_community_enrichment]
- Infer or measure beta-ketoadipate and protocatechuate pathway content in the retained bacterial taxa to test whether functional lignin-associated capacity predicts persistence across passages. [src: lignin_community_enrichment]
- Add intermediate passage time points and fit community trajectories to distinguish rapid restructuring from gradual historical persistence. [src: lignin_community_enrichment]
- Increase ITS sequencing depth, use UNITE-based taxonomy, and repeat the history experiment to test whether the absent fungal memory signal reflects biology or poor replicate structure. [src: lignin_community_enrichment]

## [[concepts/environmental-resistome|From Ecological Association to Causal Resistance Selection]]

- Use the existing per-genome AMR calls, NCBI environment metadata, and phylogenetically matched comparisons to perform environment-specific gene identification, then ask which resistance clusters remain enriched after controlling for lineage and sampling intensity. [src: amr_environmental_resistome]
- Use the AMR mechanism profiles and environmental classifications with PCoA and PERMANOVA, a permutation-based multivariate analysis of variance, to test whether environment explains multivariate resistance composition beyond taxonomic structure. [src: amr_environmental_resistome]
- Reanalyze the 293K-genome collection with metagenome-assembled genomes and isolate genomes separated, then ask whether the clinical-accessory AMR contrast persists when genome-recovery and isolate-sampling processes are modeled explicitly. [src: amr_environmental_resistome]
- Combine the 2,659 species with AlphaEarth embeddings and measured exposure metadata, using partial correlation or phylogenetically controlled models, to test whether interpretable environmental gradients account for the A34 association and the Mantel result of r = 0.098. [src: amr_environmental_resistome]
- Reconstruct within-species comparisons from per-genome AMR profiles rather than the species-level clinical-fraction proxy, then test whether genomes from environments with higher antibiotic or metal exposure contain more acquired resistance after matching on lineage. [src: amr_environmental_resistome]
- Expand mechanism annotation for the 15,550 unclassified clusters using independent annotation resources, then test whether the environment-dependent mechanism fractions change when the 18.7% unassigned fraction is included. [src: amr_environmental_resistome]

## [[concepts/ecotype-clustering-validity|Cluster assumptions and weak separation limit inference about bacterial gene-content ecotypes]]

- Recluster the 1,820 genome assignments with HDBSCAN and compare cluster membership, silhouette scores, and cluster number with the KMeans results to test whether ecotype structure is robust to cluster geometry and density assumptions. [src: ecotype_functional_differentiation]
- Add within-species core-genome trees to the 12 successful species and use phylogenetically controlled association tests to ask whether COG differentiation remains after accounting for clade structure. [src: ecotype_functional_differentiation]
- Scale the same PCA/KMeans and HDBSCAN comparison from the 15-species sample to all 456 eligible species to test whether weak separation and functional differentiation generalize across genome-count bins and phylogenetic diversity. [src: ecotype_functional_differentiation]
- Reanalyze the 62% of gene clusters lacking COG annotations with AlphaFold or domain analysis to ask whether unannotated genes improve separation or reveal adaptive functions hidden by annotation coverage. [src: ecotype_functional_differentiation]
- Join ecotype assignments to habitat metadata and test with phylogenetically controlled models whether the inferred groups predict environments rather than only gene-content or lineage structure. [src: ecotype_functional_differentiation]

## [[concepts/ecotype-environment-gene-content|Environmental Context and Functional Gene-Content Differentiation]]

- Recompute downsampled and full-genome environmental correlations with identical procedures to determine the 27x discrepancy in absolute values. [src: ecotype_env_reanalysis]
- Test openness against auxiliary fraction, Heap’s law alpha, and pangenome fluidity, stratified by gene function and lifestyle. [src: pangenome_openness]
- Reconcile latent capability (ρ = 0.69, p = 0.0004), variable pathway count (partial rho=0.530, p=2.83e-203), and environment/phylogeny effect sizes using matched species and hierarchical models. [src: metabolic_capability_dependency; pathway_capability_dependency; pangenome_openness]
- Test whether PGP enrichment persists with structured environment metadata, genome-size and sampling controls, broader annotations, and functionally validated gene clusters. [src: pgp_pangenome_ecology]
- Overlay core-genome phylogenies on the 12 functional ecotype assignments and scale to all 456 eligible species, comparing KMeans with HDBSCAN. [src: ecotype_functional_differentiation]
- Pair GapMind gene assignments with Fitness Browser experiments across matched media; calibrate condition-specific thresholds against known essentials. [src: metabolic_capability_dependency; pathway_capability_dependency]
- Add pH, temperature, total organic carbon, study random effects, taxonomic controls, Freshwater metabolomics, and metatranscriptomics to the NMDC analysis. [src: nmdc_community_metabolic_ecology]
- Reanalyze MicrobeAtlas with finer habitat categories, HGT burden, genome size, species count, site contamination metadata, species-level aggregation, and alternative phylogenetic models. [src: microbeatlas_metal_ecology]
- Repeat Harvard Forest sampling across dates and horizons with direct DNA/RNA, quantitative temperature, pH, nitrogen, NOM metadata, and TPM-based transcript quantification. [src: harvard_forest_warming]
- Expand plant-associated phylogenetic-tree coverage and test host-specific subclades with accessory-gene and gene-content trees, especially for the 47/65 candidate species lacking tree data. [src: plant_microbiome_ecotypes]
- Rebuild ecotype analyses with held-out-feature clustering, leave-one-feature-out refitting, and independent within-substudy contrasts; quantify how candidate lists change under leakage-resistant designs. [src: pitfalls]
- Validate prophage annotations with geNomad or VIBRANT, distinguish complete prophages from domesticated remnants, and repeat module–environment tests with matched species, genome-size controls, and structured ENVO metadata. [src: prophage_ecology]
- Test whether the prophage pH association persists after controlling for host taxonomy, genome size, sampling source, and environmental covariates, and determine whether pH predicts prophage expression or induction rather than annotation burden. [src: prophage_ecology]
- Compare module-level environmental associations with TerL lineages, host-defense genes, and contig-resolved prophage boundaries to test whether modular exchange or whole-lineage adaptation explains the signal. [src: prophage_ecology]
- Expand co-localization tests beyond 15 species and use long-read or closed genomes to determine whether anti-defense genes occupy defense islands separate from prophage backbones. [src: prophage_ecology]
- Cross-validate taxonomy-based NMDC prophage burden with sample-level prophage detection and metatranscriptomics before interpreting abiotic correlations mechanistically. [src: prophage_ecology]
- Re-run environment and pangenome analyses after live schema discovery, explicit type casting, NCBI-taxid/GTDB-version-aware synonym reconciliation, and genome_id-based joins; quantify the biological conclusions lost to ambiguous names or zero-as-missing metadata. [src: pitfalls]
- Stratify AlphaEarth analyses by coordinate quality and environment category, filter NaN embeddings, and test whether the geographic gradient persists after excluding human-associated samples. [src: pitfalls]
- Extend the *Pseudomonas* analysis with aromatic degradation modules, PGLS or phylogenetic logistic regression, and within-species analyses of *P. fluorescens* and *P. putida* to separate environmental effects from subgenus structure. [src: pseudomonas_carbon_ecology]
- Use the full 789K genome-pathway matrix and matched RB-TnSeq data to test whether carbon-pathway profiles predict condition-specific fitness within *Pseudomonas* lineages. [src: pseudomonas_carbon_ecology]
- Rerun the soil-metal associations with partial-correlation models, including COG ~ Cr | Cu + Zn + Pb, to distinguish metal-specific signals from multi-metal contamination. [src: soil_metal_functional_genomics]
- Report unconditional metal-only db-RDA R² alongside the conditional R² = 0.799, audit Spearman rho effect sizes, and test residuals with Moran’s I and SEVM if spatial autocorrelation is significant. [src: soil_metal_functional_genomics]
- Repeat copper genome–soil matching at 5 km and 20 km, classify significant COGs as resistance, stress, membrane, energy, or unknown, and test whether the copper-associated energetic trade-off persists. [src: soil_metal_functional_genomics]
- Rerun the soil-metal models from the kescience_mgnify and kbase_ke_pangenome Spark tables with dependence-aware FDR or other procedures that account for correlated metal predictors and COG tests. [src: soil_metal_functional_genomics]

## [[concepts/embedding-cluster-interpretation-limits|Dimensionality Reduction and Density Clustering Can Overstate Ecological Structure]]

- Recompute UMAP over the 79,449 genomes with valid values across all 64 dimensions while varying `n_neighbors` and `min_dist`; test whether the same environmental and taxonomic separations persist. [src: env_embedding_explorer]
- Re-run DBSCAN across a grid of `eps` values, compare the resulting cluster assignments with coarser alternatives, and ask which resolution best reproduces independently harmonized environment categories. [src: env_embedding_explorer]
- Compare UMAP and DBSCAN assignments with distances in the original 64-dimensional space; test whether cluster separation remains after removing projection effects. [src: env_embedding_explorer]
- Use the 50,109 genomes classified as Good coordinates and stratify by environmental versus human-associated categories; test whether cluster structure remains after controlling for geographic distance and sampling composition. [src: env_embedding_explorer]
- Compare keyword-based environment labels with `env_broad_scale` for the 42% of genomes covered by the structured field; test whether cluster–environment associations are robust to harmonization schema. [src: env_embedding_explorer]
- Reassess [[concepts/ecotype-environment-gene-content]] on stable, environmentally validated clusters and environmental-only samples; test whether genomic differences remain after controlling for phylogeny. [src: env_embedding_explorer]

## [[concepts/engraftability-proxy-validation|Prevalence and Transcriptional Activity Are Proxies Rather Than Measurements of Formulation Engraftment]]

- Administer barcoded or otherwise strain-resolvable versions of the candidate organisms in an airway-relevant model, then use longitudinal quantitative metagenomics to test whether the prevalence × log(activity ratio) score predicts recovery, persistence, and dose-normalized abundance. [src: cf_formulation_design]
- Measure candidate abundance and transcription before administration and at multiple post-administration time points in cystic-fibrosis airway samples to distinguish transient detection from sustained engraftment. [src: cf_formulation_design]
- Test the two-species and three-species formulations in structured biofilm or airway-mimetic systems against PAO1 and 3–5 mucoid clinical PA isolates to determine whether proxy-ranked candidates establish while retaining inhibition. [src: cf_formulation_design]
- Generate additional lung genomes and strain-resolved metagenomes for *N. mucosa*, *R. dentocariosa*, *S. salivarius*, *G. sanguinis*, and *M. luteus* to test whether genomic lung adaptation improves prediction beyond prevalence and transcriptional activity. [src: cf_formulation_design]
- Compare proxy scores with measured engraftment using mixed-effects or survival models that incorporate dose, sampling time, patient, formulation, and airway environment, thereby testing whether the score predicts establishment independently of these factors. [src: cf_formulation_design]

## [[concepts/environment-embedding-geography|Geographic and environmental structure in microbial genomic patterns]]

- Re-run [[concepts/ecotype-environment-gene-content]] on environmental-only samples, stratifying the 52.7% unknown-label burden and comparing keyword with species-majority assignments; test whether the median partial correlation increases. [src: env_embedding_explorer; pitfalls]
- Use coordinates, isolation_source homogeneity, suspicious-cluster flags, and alternative DBSCAN parameters to distinguish field sites, institutional addresses, and taxonomic composition. [src: env_embedding_explorer]
- Correlate A00–A63 with latitude, temperature, precipitation, NDVI, and land cover; compare keyword harmonization with env_broad_scale and analyze the 3,838 NaN-containing records. [src: env_embedding_explorer]
- Re-test environment signals with GroupKFold by study, within-study contrasts, pooled versus single-biosample NMDC runs, and carrier-versus-non-carrier controls. [src: euk_in_prok_correlates; functional_dark_matter]
- Refit ecotypes with held-out-feature clustering, leave-one-species-out refitting, and pathway/EC-number clustering; test whether E1 and E3 Jaccard values remain below 0.3 and whether the independent list remains at 3 candidates. [src: pitfalls]
- Reanalyze AlphaEarth-clade associations with leaf_consistency, rank-stratified scores, study-blocked validation, and broader phenotype coverage, especially Cyanobacteriia. [src: gene_function_ecological_agora]
- Reconcile ENIGMA and global profiles using GTDB-validated identifiers, ChEBI-ID condition canonicalization, and study/site-blocked validation. [src: genotype_to_phenotype_enigma; pitfalls]
- Reanalyze Harvard Forest with horizon-matched DNA, RNA, and metabolite contrasts, restored temperature, pH, and nitrogen covariates, and multi-site comparisons. [src: harvard_forest_warming]
- Match Oak Ridge assemblies to Fitness Browser organisms at species or strain level and test uranium-specific fitness while controlling for pH, redox, carbon, and date. [src: lab_field_ecology]
- Reanalyze xoxF/mxaF with phylogeny-aware models, ORF-integrity checks, Bakta validation, and expanded REE-AMD sampling. [src: lanthanide_methylotrophy_atlas]
- Complete the metal-resistance map, normalize hotspots by log(n_MAGs), check sample-accession prefixes, and stratify the 30.8% coordinate gap. [src: metal_resistance_global_biogeography]
- Reanalyze MicrobeAtlas with finer environment categories, phylogenetic mixed models, sampling-effort covariates, covered-read fractions, contamination metadata, and distinct accession prefixes. [src: microbeatlas_metal_ecology]
- For PHB, map PF00561/PF07167, reconstruct a phaC tree, and apply phylogenetic logistic regression to distinguish transfer, lineage, genome-size, and environmental effects. [src: phb_granule_ecology]
- Extend plant analyses with phylogenetic GLMMs, broader tree coverage, genome-size matching, independent metagenomes/transcriptomes, and reaction-level complementarity after recovering the 62/322 lost genera. [src: plant_microbiome_ecotypes]
- Test prophage effects with geNomad or VIBRANT, intact-versus-domesticated classification, lineage and genome-size controls, and assembly-level validation of the NMDC bridge. [src: prophage_ecology]
- Resolve module-versus-lineage effects by integrating module exchange, contig co-localization, TerL trees, host phylogeny, and defense-island analyses. [src: prophage_ecology]
- Extend Pseudomonas profiling with aromatic-degradation modules and PGLS or phylogenetic logistic regression; test within-species ecotypes in *P. fluorescens* and *P. putida* against [[entities/kescience-fitnessbrowser]]. [src: pseudomonas_carbon_ecology]
- Test SNIPE environmental association using PF13250/DUF4041 plus PF13455 rather than PF01541; quantify false positives from DUF4041-only calls, search divergent homologues, and compare SNIPE-bearing and non-bearing species within phylogenetically and coverage-matched strata. [src: snipe_defense_system]
- Test whether SNIPE status predicts selected AlphaEarth dimensions, measured pH, temperature, precipitation, land cover, or NMDC ecosystem metadata after controlling for lineage, genome size, sampling effort, and coordinate quality; determine whether the A19 effect generalizes beyond the 1,069 SNIPE-bearing and 13,977 non-SNIPE species. [src: snipe_defense_system]
- Test the proposed SNIPE–ManYZ trade-off experimentally in Klebsiella using strain-specific mutant libraries or curated Tn-Seq data, and compare phage susceptibility with mannose/glucosamine fitness; the current co-occurrence evidence cannot establish the mechanism. [src: snipe_defense_system]
- Decompose the soil negative R² using spatial blocking, train/test distribution-shift diagnostics, fold-level MSE leverage checks, and outlier sensitivity analyses to distinguish model failure from genuine unpredictability. [src: soil_frontier_genomics]
- Recompute GDI after uniform 16S rarefaction, report OTU richness and mean completeness separately, bootstrap biome-level 95% CIs, and test whether forest and cropland remain jointly highest. [src: soil_frontier_genomics]
- Control the +0.8 pH discovery gap for the number of 16S samples per pH bin and compare GDI with independent completeness and assembly-quality measures to distinguish sampling gaps from assembly or annotation gaps. [src: soil_frontier_genomics]
- For soil-metal associations, rerun Spearman and partial-correlation models from the `kescience_mgnify` and `kbase_ke_pangenome` Spark tables; test COG ~ Cr | Cu + Zn + Pb, report rho distributions and unconditional db-RDA R², and assess whether the 2,355 associations survive effect-size and dependence-aware FDR checks. [src: soil_metal_functional_genomics]
- Test copper proximity sensitivity at 5 km, 10 km, and 20 km, and apply Moran’s I to residuals with SEVM if spatial autocorrelation is significant; determine whether copper–COG associations persist after spatial and project controls. [src: soil_metal_functional_genomics]
- Classify significant metal-associated COGs into resistance, stress, membrane, energy, and unknown categories, and compare soil, marine, and wastewater models to distinguish metal-specific responses from generic multi-metal contamination. [src: soil_metal_functional_genomics]
- Build a provenance audit that discovers live BERDL namespaces and schemas, validates tenant and identifier mappings, uses genome_id and sample_id bridge keys, and records missingness before environmental joins. [src: pitfalls]

## [[concepts/environmental-embedding-ecological-validity|Ecological Validity of Environmental Embeddings]]

- Use the 13,381-genome metadata set and alternative environmental embedding distances to test whether non-AlphaEarth representations recover stronger associations with gene-content similarity. [src: ecotype_analysis]
- Combine direct environmental metadata with embedding distances and partial-correlation or nonlinear distance-based methods to ask whether environmental effects are hidden by linear modeling or coarse descriptors. [src: ecotype_analysis]
- Partition gene clusters into COG functional categories, including V-Defense and L-Mobile, and test whether category-specific associations with environment exceed the whole-genome signal. [src: ecotype_analysis]
- For species with identified ecotype clusters, compare gene content between clusters to determine whether environmental structure is detectable at the ecotype or locus level despite weak genome-wide correlations. [src: ecotype_analysis]
- Restrict host-associated analyses to metadata describing actual microenvironments rather than collection coordinates and test whether the environmental effect changes. [src: ecotype_analysis]

## [[concepts/environment-embedding-geography|Environmental Metadata Harmonization Can Reshape Ecological Genomic Inference]]

- Use isolation_source homogeneity, species composition, and coordinate precision to reclassify the 30,469 Suspicious cluster and 2,708 Low precision coordinates, then test whether the embedding–geographic-distance relationship changes. [src: env_embedding_explorer]
- For the 34,800 genomes with env_broad_scale and the 76,295 with isolation_source, compare keyword categories with structured classifications using confusion matrices and category-specific embedding distances, asking which schema preserves ecological separation with fewer ambiguous assignments. [src: env_embedding_explorer]
- Repeat the [[concepts/ecotype-environment-gene-content]] analysis on environmental-only samples, using phylogeny-controlled partial correlations, to test whether removing the 38% human-associated subset increases the median association above 0.0025. [src: env_embedding_explorer]
- Add clinical body-site terms, underground-laboratory terms, generic water-source terms, and env_broad_scale fallback values to the harmonization workflow, then measure how many of the 13,944 Other genomes move into interpretable categories. [src: env_embedding_explorer]
- Re-run UMAP and DBSCAN across alternative n_neighbors, min_dist, and eps values, then test whether environment-dominated clusters persist in the original 64-dimensional space rather than only in the projection. [src: env_embedding_explorer]
- Correlate embedding dimensions A00–A63 with latitude, temperature, precipitation, NDVI, and land-cover classifications to identify which environmental features drive the observed distance-decay pattern. [src: env_embedding_explorer]

## [[concepts/environmental-resistome|Environmental structuring of the bacterial resistome]]

- Use assembled per-genome environment metadata and AMR calls with stratified contingency analysis to test clinical versus environmental genomes within species. [src: amr_environmental_resistome]
- Apply PCoA and PERMANOVA to AMR mechanism profiles and reanalyze AlphaEarth dimensions with interpretable environmental covariates. [src: amr_environmental_resistome]
- Harmonize core/accessory thresholds, genome sampling, mechanism annotations, and the 21% versus 7.0% human-gut efflux estimates. [src: discoveries, amr_environmental_resistome]
- Map the 1,517 resistance islands to plasmids, chromosomes, integron boundaries, and insertion sequences. [src: amr_strain_variation]
- Match BacDive GCA accessions directly to pangenome genome_ids, expand MIC and growth-inhibition extraction, and apply PGLS or phylogenetic PCA. [src: bacdive_metal_validation, bacdive_phenotype_metal_tolerance]
- Resolve the metal-isolation tension by mapping cross-resistance gene signatures with KEGG/PFAM across 27K species and 42K strains using matched metadata and phylogenetic correction. [src: metal_cross_resistance]
- Normalize metal fitness by concentration relative to MIC, add non-metal stress controls, and repeat ICA with precomputed z-scored module activities to distinguish universal stress from chemistry-specific modules. [src: metal_cross_resistance, metal_specificity]
- Resolve the 40.7% locusId attrition, validate classifications against Fitness Browser `specificphenotype` annotations, and test whether the 5% threshold changes candidate rankings. [src: metal_specificity]
- Use AlphaFold predictions to examine candidate metal-binding sites in UCP030820, YebC, and DUF1043/YhcB. [src: metal_specificity]
- Complete the soil-metal validation by rerunning the Spearman analyses from the `kescience_mgnify` and `kbase_ke_pangenome` Spark tables, auditing rho values and effect sizes, and flagging associations with rho < 0.05. [src: soil_metal_functional_genomics]
- Fit partial-correlation models such as COG ~ Cr | Cu + Zn + Pb, classify significant COGs into resistance, stress, membrane, energy, and unknown categories, and report both conditional and unconditional db-RDA R² values. [src: soil_metal_functional_genomics]
- Test Moran’s I on model residuals and apply SEVM if spatial autocorrelation is significant; repeat the copper analysis with 5 km and 20 km genome–soil proximity thresholds. [src: soil_metal_functional_genomics]
- Validate global biogeography by checking distinct `sample_accession` prefixes, normalizing prevalence by log(n_MAGs), testing biome-specific coordinate missingness, and repairing the missing matplotlib import. [src: metal_resistance_global_biogeography]
- Bridge spatial and genomic context by testing whether hotspot MAGs are enriched for particular metal-resistance genes, resistance-island architectures, clades, or metal-diversity profiles after controlling for sampling effort. [src: metal_resistance_global_biogeography]
- Reanalyze MicrobeAtlas with finer marine, freshwater, and saline categories; fit alternative phylogenetic count or mixed models; quantify multi-primer detection; and test whether metal-type diversity predicts niche breadth after explicit sampling-effort correction. [src: microbeatlas_metal_ecology]
- Validate the MicrobeAtlas association experimentally using the 435 candidate OTUs and eight priority OTUs in 4–6 metal-stress treatments, 5 replicates, and 7- and 14-day time points, with relative-abundance fold-change as the primary endpoint. [src: microbeatlas_metal_ecology]
- Replace broad ENIGMA COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries, controlling for mapped abundance, depth, location, date, and compositional structure. [src: enigma_contamination_functional_potential]
- Load the 221 registered SSO geochemistry samples into CORAL, generate metagenomes at matching spatial resolution, and repeat profiling with AMR calls. [src: enigma_sso_asv_ecology]
- Apply the DvH condition classification and fitness–conservation analysis to other environmentally relevant organisms while controlling for gene length and essential-gene exclusion. [src: field_vs_lab_fitness]
- Execute value-space-validated NMDC–PROTECT and ENIGMA–PhageFoundry bridges and harmonize pangenome, AlphaEarth, BacDive, and environmental sample identifiers. [src: berdl_data_atlas]
- Test whether the PGP soil-enrichment signal and AMR mechanism profiles persist after matched phylum, genome-size, sampling-effort, and environment-label controls; compare acdS, pqqC, hcnC, and nifH distributions with AMR metal-resistance distributions without assuming shared causation. [src: pgp_pangenome_ecology]
- Analyze genomic neighborhoods and phylogenies for pqqC–acdS and hcnA–hcnC, and test whether their environmental associations reflect linkage, repeated acquisition, or lineage structure. [src: pgp_pangenome_ecology]
- Reanalyze all available genomes from [[entities/klebsiella-pneumoniae]], [[entities/acinetobacter-baumannii]], [[entities/pseudomonas-aeruginosa]], and [[entities/escherichia-coli]] with dedicated prophage predictors, scaffold-based distances, and explicit plasmid/ICE controls to test whether prophage-proximal AMR is enriched within species. [src: prophage_amr_comobilization]
- Apply geNomad or PHASTER to BERDL genomes and compare prophage-marker calls with Bakta/Pfam calls, testing false-positive rates from phage-defense systems and missed divergent prophages. [src: prophage_amr_comobilization]
- Use base-pair-resolution neighborhoods and exhaustive genome sampling to determine whether the species-level prophage-density association persists after controlling for pangenome openness, genome count, phylogeny, and plasmid or ICE mobilization. [src: prophage_amr_comobilization]
- Revisit prophage-proximal AMR fitness costs as Fitness Browser coverage expands, using matched organisms and condition-specific RB-TnSeq measurements. [src: prophage_amr_comobilization]
- Run the pending T4SS–CAZy synteny-threshold permutation test on unfiltered Spark data, validate Node_4915 by BLAST against NCBI nr, establish a housekeeping-gene null baseline, and calculate θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)] for biome enrichment. [src: t4ss_cazy_environmental_hgt]
- Use base-pair-resolution neighborhoods, explicit plasmid/ICE controls, and experimental transfer assays to test whether T4SS-proximal GT2–GH23 loci are transferred chromosomally or through integrative elements and whether their 11× metal-resistance association persists after phylogenetic and MGE-density adjustment. [src: t4ss_cazy_environmental_hgt]

See the project summaries: [[summaries/amr_environmental_resistome__REPORT]], [[summaries/amr_fitness_cost__REPORT]], [[summaries/amr_pangenome_atlas__REPORT]], [[summaries/amr_strain_variation__REPORT]], [[summaries/bacdive_metal_validation__REPORT]], [[summaries/bacdive_phenotype_metal_tolerance__REPORT]], [[summaries/berdl_data_atlas__REPORT]], [[summaries/discoveries]], [[summaries/enigma_contamination_functional_potential__REPORT]], [[summaries/enigma_sso_asv_ecology__REPORT]], [[summaries/field_vs_lab_fitness__REPORT]], [[summaries/gene_function_ecological_agora__REPORT]], [[summaries/lab_field_ecology__REPORT]], [[summaries/metal_cross_resistance__REPORT]], [[summaries/metal_resistance_global_biogeography__REPORT]], [[summaries/metal_specificity__REPORT]], [[summaries/microbeatlas_metal_ecology__REPORT]], [[summaries/pgp_pangenome_ecology__REPORT]], [[summaries/prophage_amr_comobilization__REPORT]], [[summaries/soil_metal_functional_genomics__REPORT]], and [[summaries/t4ss_cazy_environmental_hgt__REPORT]].

## [[concepts/essentiality-assay-discordance|Why transposon fitness and complete-knockout essentiality disagree]]

- Perform condition-matched RB-TnSeq and complete-knockout experiments, then test whether discordance remains after aligning media and growth conditions. [src: adp1_triple_essentiality]
- Analyze insertion positions, gene domains, transcriptional polarity, and truncated-protein potential for the 211 knockout-essential/RB-TnSeq-dispensable genes to test the proposed partial-function mechanisms. [src: adp1_triple_essentiality]
- Compare continuous fitness, essentiality fraction, knockout calls, and growth rates with a preregistered threshold-selection and multiple-testing procedure to determine which representation generalizes across conditions. [src: adp1_triple_essentiality]
- Fit combined FBA-plus-fitness-plus-proteomics models and evaluate whether multi-omic predictors improve knockout-essentiality classification over any single assay. [src: adp1_triple_essentiality]

## [[concepts/gene-essentiality|Prediction Targets and Evaluation Boundaries in Gene-Essentiality Analysis]]

- Perform condition-matched RB-TnSeq and complete-gene knockout experiments, then compare binary lethality, continuous fitness, and quantitative growth within the same media and genes to determine which discordances arise from assay modality. [src: adp1_triple_essentiality]
- Analyze insertion position, retained domains, and transcript structure for the 211 knockout-essential/TnSeq-dispensable genes to test whether partial gene products explain the discordance. [src: adp1_triple_essentiality]
- Add measured trace aromatic compounds to the FBA media definitions and rerun condition-specific flux simulations to test whether environmental assumptions explain the aromatic-degradation errors. [src: adp1_triple_essentiality]
- Fit combined FBA-plus-fitness-plus-proteomics predictors separately for lethal-versus-dispensable classification and quantitative growth ranking, then compare metrics appropriate to each target. [src: adp1_triple_essentiality]
- Reanalyze the eight-carbon-source data with explicitly condition-specific labels and dependence-aware aggregation to determine how inter-condition correlation changes essentiality estimates. [src: adp1_triple_essentiality]

## [[concepts/evidence-triangulation-for-functional-annotation|Evidence Triangulation Improves Functional Annotation Beyond Any Single Signal]]

- Use the 44 high-confidence assignments and targeted gene-knockout or CRISPRi experiments to ask which integrated candidates produce reproducible reaction- or carbon-source-specific phenotypes. [src: annotation_gap_discovery]
- Reconstruct the 38 false-negative cases with gapseq and compare the resulting reaction sets with default ModelSEED gapfilling to ask whether alternative gapfilling reduces the 330 baseline false positives without lowering recovery of growth-positive conditions. [src: annotation_gap_discovery]
- Characterize the 50 EC-less reactions with stoichiometric analysis, profile comparison, and experimental assays to ask which dark reactions can acquire testable enzyme-function hypotheses. [src: annotation_gap_discovery]
- Extend the pipeline from 14 organisms to all 48 Fitness Browser organisms and stratify resolution by phylogeny, annotation quality, and experiment count to ask whether the 47.8% resolution rate transfers beyond the Proteobacteria-heavy dataset. [src: annotation_gap_discovery]
- Integrate the 104 GapMind-gapfill pathway pairings with step-level pathway annotations to ask whether reaction-level concordance improves when pathway-level `not_present` or `steps_missing` calls are mapped to individual steps. [src: annotation_gap_discovery]
- Apply independent-component analysis (ICA), a method for decomposing correlated fitness profiles into latent components, to the 71 expanded fitness profiles and compare the resulting modules with candidate gene-reaction assignments to ask whether module-level evidence resolves currently unresolved pairs. [src: annotation_gap_discovery]

## [[concepts/experimental-prioritization-of-functional-dark-matter|Evidence-weighted experimental prioritization of unknown bacterial genes]]

- Re-run the NMDC carrier–trait analysis with full sample-label permutation tests to determine how much of the 441/449 exploratory-test signal remains after controlling for compositional coupling. [src: functional_dark_matter]
- Process equivalent annotated-accessory-gene controls through the complete biogeographic pipeline to test whether dark-gene environmental enrichments exceed the baseline produced by annotation and sampling structure. [src: functional_dark_matter]
- Use CRISPRi in the highest-ranked essential candidates and measure growth under standard, stress, nitrogen-source, and carbon-source conditions to test whether neighborhood- and domain-based predictions produce reproducible phenotypes. [src: functional_dark_matter]
- Combine EC matching, structure prediction, purified-protein enzymology, and pathway growth assays for the GapMind candidates to resolve organism-level pathway co-occurrence into direct gene-to-reaction assignments. [src: functional_dark_matter]
- Repeat the six-axis prioritization with expanded Fitness Browser condition coverage and more evenly distributed taxa to quantify how much candidate rank is driven by assay depth and Pseudomonadota representation. [src: functional_dark_matter]
- Compare conserved-synteny, co-fitness, and CRISPRi perturbation results for the 998 double-validated operon pairs to test whether network evidence predicts causal functional coupling. [src: functional_dark_matter]

## [[concepts/fitness-condition-coverage-prioritization-bias|Uneven Experimental Condition Coverage Biases Fitness-Based Gene Prioritization]]

- Use the Fitness Browser condition metadata to construct organism-by-condition coverage matrices, then apply inverse-probability weighting or matched-depth resampling to test whether candidate rankings change after equalizing condition opportunity. [src: functional_dark_matter]
- Recompute the 7,787 strong-fitness-effect count and the top-100 ranking after downsampling MR-1's 121 historical conditions to the coverage of less-profiled organisms, asking how much of MR-1's prioritization advantage is attributable to condition depth. [src: functional_dark_matter]
- Compare condition-class-balanced rankings for stress, carbon-source, and nitrogen-source assays, asking whether cross-organism concordance among the 65 ortholog groups changes when only shared condition classes are evaluated. [src: functional_dark_matter]
- Add a coverage penalty or an explicit untested-condition uncertainty term to the six-axis score, then compare top-50 retention against the reported 64% fitness-active retention under conservation-dominant or drop-tractability settings. [src: functional_dark_matter]
- Design targeted RB-TnSeq or CRISPRi experiments for high-priority genes from poorly profiled organisms, asking whether missing condition coverage explains their absence from the current top candidates rather than a lack of measurable phenotype. [src: functional_dark_matter]

## [[concepts/antimicrobial-resistance-fitness-cost|Network Breadth Does Not Necessarily Predict Fitness Cost]]

- Recompute cofitness separately for antibiotic-treatment and standard-growth conditions, then test whether network breadth predicts fitness cost in either condition-specific matrix. [src: amr_cofitness_networks]
- Apply a fitness-matched permutation using random non-AMR genes with the same mean-fitness distribution, including the −0.05 to +0.05 range, and ask whether the observed network-size–cost correlation differs from the matched null. [src: amr_cofitness_networks]
- Repeat the network-size–cost analysis at |r| > 0.4 and |r| > 0.5, then test whether stricter support-network definitions produce a correlation that is absent at |r| > 0.3. [src: amr_cofitness_networks]
- Quantify the variance of AMR fitness costs and use a power analysis or hierarchical model to ask whether the null result could reflect insufficient variation across genes, mechanisms, or organisms. [src: amr_cofitness_networks]
- Compare cofitness network breadth with direct regulatory evidence and Pfam-domain enrichment to test whether broad networks reflect shared cofitness, co-regulation, or common functional architecture. [src: amr_cofitness_networks]

## [[concepts/fitness-module-detection-sensitivity|Experimental Depth Limits the Reliability of Fitness-Module Inference]]

- Use matched experiment subsets and bootstrap or split-sample ICA to determine whether the 94.2% significant-module rate and 2.8x correlation enrichment remain stable as experiment count changes. [src: fitness_modules]
- Reanalyze organisms across a controlled range of experiment depths to test whether the approximately 100-experiment threshold predicts module stability and whether the 2.9x enrichment observed for Caulo reflects organism-specific biology or data composition. [src: fitness_modules]
- Vary the 40% component cap together with FastICA convergence diagnostics to quantify how many modules are missed under sparse experimental designs. [src: fitness_modules]
- Compare module recovery after balancing condition classes across organisms to determine whether experimental diversity, rather than experiment count alone, explains differences in module reliability. [src: fitness_modules]
- Test whether cross-organism module families remain detectable after downsampling every organism to the same number of experiments, using the 156 identified families as the reference set. [src: fitness_modules]

## [[concepts/gene-essentiality|Fitness Importance and Pangenome Conservation]]

- Combine the existing fitness and pangenome data with environmental-condition metadata and test, using stratified models, whether the 82% versus 66% conservation contrast persists outside rich media and standard stresses. [src: fitness_effects_conservation]
- Reanalyze singleton and novel genes after filtering or modeling transposon coverage, asking whether their near-zero mean fitness reflects true neutrality or callability failure. [src: fitness_effects_conservation]
- Use multi-gene perturbation or interaction datasets to test whether the observed conservation gradient changes when epistatic effects omitted by single-gene knockouts are included. [src: fitness_effects_conservation]
- Compare the conservation–fitness relationship across bacterial lineages beyond the primarily Proteobacteria representation in the 43-bacterium Fitness Browser coverage. [src: fitness_effects_conservation]
- Test whether core genes with heavier positive and negative fitness tails show reproducible condition-specific trade-offs across independent experiments rather than assay-specific effects. [src: fitness_effects_conservation]

## [[concepts/fitness-importance-versus-ecological-context|Fitness importance predicts genome conservation more strongly than field-versus-lab context]]

- Use Fitness Browser experiments and quantitative gene-cluster prevalence across additional environmentally relevant organisms to test whether the weak field-versus-lab effect generalizes beyond DvH. [src: field_vs_lab_fitness]
- Add the 678 essential genes through an essentiality-aware model and test whether including their 80.1% core fraction changes the comparison between conditional fitness and conservation. [src: field_vs_lab_fitness]
- Fit continuous-fitness prediction models with gene length, transposon insertion coverage, and pangenome prevalence to determine whether continuous fitness improves on the reported CV-AUC values of 0.517, 0.531, and 0.548. [src: field_vs_lab_fitness]
- Combine genomic-context analyses with resistance-gene calls to test whether the 73.4% core fraction for lab-antibiotic genes and 71.2% for heavy-metal genes is associated with mobile genetic elements. [src: field_vs_lab_fitness]
- Reanalyze the 52 ICA modules using functional annotation and environmental metadata to test whether the 52 unannotated genes in ecological modules mediate adaptation rather than merely co-varying with conserved genes. [src: field_vs_lab_fitness]
- Link the 4,346 ENIGMA CORAL field samples with geochemistry and 213,044 ASVs to test ecological associations for DvH or other organisms with both environmental data and gene-level fitness measurements. [src: field_vs_lab_fitness]

## [[concepts/fitness-matched-null-models|Fitness-Matched Null Models for Functional Enrichment]]

- Use the existing AMR and non-AMR fitness matrices, conservation classes, and mean-fitness values to run conservation- and fitness-matched permutations; test whether flagellar and amino acid-biosynthesis enrichment remains significant. [src: amr_cofitness_networks]
- Recompute cofitness separately for antibiotic-exposure and standard-growth conditions, then apply the matched null; ask whether enrichment is specific to resistance-relevant conditions or persists under general laboratory growth. [src: amr_cofitness_networks]
- Compare observed odds ratios and enriched-term counts with null distributions at |r| > 0.3, |r| > 0.4, and |r| > 0.5; ask whether the functional signal survives removal of weaker associations. [src: amr_cofitness_networks]
- Measure mean fitness directly for flagellar knockouts and other conditionally dispensable gene classes, then use those distributions in the null; ask whether their observed neighborhoods are predictable from dispensability alone. [src: amr_cofitness_networks]
- Extend the matched-null analysis to phage-defense and secondary-metabolite genes; ask whether enrichment of other conditionally dispensable classes is similarly explained by fitness structure. [src: amr_cofitness_networks]
- Replace the operon-exclusion row-index heuristic with coordinate-based genomic filtering before permutation testing; ask whether local-gene structure changes the enrichment estimates. [src: amr_cofitness_networks]

## [[concepts/fitness-module-detection-sensitivity|Fitness-Module Discovery Depends on Thresholds and Decomposition Constraints]]

- Re-run ICA across organisms after systematically varying the |weight| threshold, the 50-gene maximum, and the 40% component cap; test which settings preserve the 94.2% within-module significance rate, 2.8x correlation enrichment, and 22.7x genomic-adjacency enrichment. [src: fitness_modules]
- Use matched experiment subsampling and convergence diagnostics to quantify how module recovery changes below and above approximately 100 experiments, including the Caulo case with 198 experiments and 2.9x correlation enrichment. [src: fitness_modules]
- Compare PFam, KEGG KO, and other annotation layers at fixed module memberships to determine whether the increase from 8% to 80% annotation reflects genuine biological coverage or domain-level overcounting. [src: fitness_modules]
- Benchmark module-level predictions against independently measured phenotypes or perturbation data to test whether process-level predictions improve biological interpretation despite <1% strict KEGG KO precision. [src: fitness_modules]
- Reconstruct cross-organism module families under alternative orthology definitions and test whether the 156 families, including the family spanning 21 organisms, remain stable without assuming identical molecular functions. [src: fitness_modules]

## [[concepts/functional-dark-matter|Genomic under-representation limits inference about microbial functional potential]]

- Re-run the BERIL Observatory 16S tables and [[entities/kbase-ke-pangenome]] completeness data with rarefaction or uniform 16S sequencing-depth correction, then ask whether forest and cropland remain the highest-GDI biomes after sampling effort is equalized. [src: soil_frontier_genomics]
- Compute bootstrap 95% confidence intervals for biome-level GDI values and explicitly compare Forest GDI = 902.36 with Cropland GDI = 890.82, asking whether their apparent difference is distinguishable from resampling uncertainty. [src: soil_frontier_genomics]
- Control GDI for the number of 16S samples in each pH bin, asking whether the +0.8 pH unit gap between frontier and mapped areas persists after sampling intensity is accounted for. [src: soil_frontier_genomics]
- Use spatial blocking and decomposition of test-fold error to separate distributional shift, high-leverage outliers, and genuine unpredictability in the negative out-of-sample R² results, asking which mechanism explains the prediction failure. [src: soil_frontier_genomics]
- Report OTU richness and mean genome completeness as separate dimensions alongside GDI, asking whether the same locations are identified as underrepresented when the ratio-based index is not used. [src: soil_frontier_genomics]
- Extend pangenome linkage to the 17,479 unlinked dark genes and compare their Bakta, Pfam, KEGG, eggNOG, and orthology coverage with the 6,427 linked truly dark genes, asking how much of the residual functional gap is a linkage artifact. [src: truly_dark_genes]
- Link the 3,683 essential-auxiliary and 1,259 essential-unmapped genes to broader pangenomes and condition-specific Fitness Browser measurements, asking whether poor annotation reflects strain-specific compensation, divergent core functions, or growth-condition dependence. [src: conservation_vs_fitness]

## [[concepts/functional-marker-validation|Validating Functional Markers Before Ecological Inference]]

- Apply the corrected multi-heme cytochrome detector to the full clay-project branch and test whether the Bagnoud porewater comparison changes when PFAM, motif, and cluster-context evidence are evaluated together. [src: bacillota_b_subsurface_accessory]
- Reclassify the 462 “other_or_unannotated” enriched OGs with an LLM-based or manual functional scan, then test whether the estimated 80–100 anaerobic-respiration-related OGs resolve into reproducible marker sets. [src: bacillota_b_subsurface_accessory]
- Decompose corrected marker prevalence by genus and cohort, using the 10-genome anchor and 62-genome baseline design, to test whether apparent ecological signals are lineage markers. [src: bacillota_b_subsurface_accessory]
- Benchmark the same marker-validation workflow in other phylum-matched subsurface comparisons to determine whether marker correction repeatedly changes ecological conclusions. [src: bacillota_b_subsurface_accessory]

## [[concepts/functional-redundancy-under-environmental-selection|Functional Redundancy Can Mask Environmental Selection]]

- Replace COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries, then test whether contamination-associated functional shifts emerge after coverage adjustment. [src: enigma_contamination_functional_potential]
- Add species- or strain-level ENIGMA or metagenomic data and use higher-resolution pangenome mappings to ask whether contamination effects are hidden below genus resolution. [src: enigma_contamination_functional_potential]
- Fit mixed-effects or hierarchical models using depth, location cluster, sampling date, and compositional controls to determine whether exploratory defense associations persist after richer site-structure adjustment. [src: enigma_contamination_functional_potential]
- Quantify the contribution of the 862 unmapped genera and expand the genus-to-clade bridge to test whether missing taxa account for the weak broad functional signal. [src: enigma_contamination_functional_potential]

## [[concepts/gene-cooccurrence-ecological-guilds|Gene co-occurrence can reveal ecological guilds without proving physical linkage]]

- Use complete or well-assembled genomes from the pqqC–acdS-positive set, together with operon and genomic-island analysis, to test whether the two genes are physically linked or occur at separate loci. [src: pgp_pangenome_ecology]
- Apply phylogeny-aware co-occurrence models to the PGP gene matrix and ask whether the pqqC–acdS association persists after accounting for shared ancestry. [src: pgp_pangenome_ecology]
- Compare gene neighborhoods, synteny, mobile-element context, and gene-tree reconciliation for pqqC, acdS, hcnC, and ipdC to distinguish vertical conservation from repeated horizontal acquisition. [src: pgp_pangenome_ecology]
- Reanalyze nifH associations after stratifying by environment, lineage, and diazotrophic ecological context to determine whether the negative nifH–pqqC and nifH–hcnC associations reflect ecological separation or sampling structure. [src: pgp_pangenome_ecology]
- Functionally validate representative co-occurring clusters with transcript or phenotype data to test whether annotated pqqC, acdS, hcnC, and ipdC genes are active components of the proposed guild. [src: pgp_pangenome_ecology]

## [[concepts/gene-essentiality|Gene Essentiality Across Conditions and Predictors]]

- Reanalyze the 499 minimal-media-essential and 346 LB-essential genes with condition-matched FBA and TnSeq calls, focusing on the 177 genes whose flux classes changed. [src: acinetobacter_adp1_explorer]
- Test the 625 condition-specific genes with replicated growth measurements and an expanded carbon-source panel. [src: adp1_deletion_phenotypes]
- Compare universal, variable, orphan, and never-essential ortholog families across matched condition panels. [src: discoveries]
- Characterize the 7,084 orphan essentials and test whether their low 49.5% core fraction reflects lineage-specific innovation or missed orthology. [src: essential_genome]
- Extend the conservation analysis from binary essentiality to condition-specific fitness, especially genes with fitness < -2 under stress, and test whether their core/auxiliary fractions differ from viability-essential genes. [src: conservation_vs_fitness]
- Use the 177,863 Fitness Browser–pangenome links to correlate mean fitness effects, rather than only essential/non-essential status, with core fraction; analyze the 3,683 essential-auxiliary genes for compensation of missing core functions. [src: conservation_vs_fitness]
- Expand GapMind mapping from 7 to the remaining 38 organisms, including *Escherichia coli* K-12, and test whether completeness varies by phylogeny and ecology. [src: essential_metabolome]
- Fit combined FBA-plus-fitness-plus-proteomics predictors on held-out knockout data and analyze the 227 discordant genes. [src: acinetobacter_adp1_explorer] [src: adp1_triple_essentiality]
- Test Complex I, PQQ, iron-acquisition, and NADH-flux hypotheses with matched ADP1 perturbations. [src: aromatic_catabolism_network]
- Construct an ADP1 NDH-2 deletion mutant, measure NADH/NAD⁺ ratios on quinate, glucose, acetate, lactate, and urea, and test whether respiratory requirements follow flux rate rather than total NADH yield. [src: respiratory_chain_wiring]
- Expand K03885 and K00330–K00343 searches across 27K species using KO-based orthology, then test NDH-2/Complex I co-occurrence and the proposed compensation relationship. [src: respiratory_chain_wiring]
- Characterize ACIAD3522 biochemically and reanalyze quinate-versus-succinate proteomics for respiratory-chain proteins. [src: respiratory_chain_wiring]
- Stratify the 82%–66% conservation gradient by organism, condition type, gene length, transposon coverage, and pangenome sampling depth. [src: fitness_effects_conservation]
- Compare pathway-level conservation with gene-level essentiality after direct GapMind per-step gene mapping, and recompute latent rates across the 16 threshold combinations. [src: metabolic_capability_dependency]
- Independently calibrate condition-specific importance thresholds against known essentials and test whether all 66 Latent Capability reclassifications persist under a preregistered threshold. [src: pathway_capability_dependency]
- Expand the four-way capability–dependency analysis beyond the 7 matched organisms and quantify KEGG-mapping failures using direct per-step gene evidence. [src: pathway_capability_dependency]
- Compare variable pathway count and ecotype number with pangenome openness using phylogenetic independent contrasts and genome-count-matched resampling across the 2,810 species. [src: pathway_capability_dependency]
- Compare metabolic ecotypes with environment metadata using phylogenetic correction, especially for *Salmonella enterica* and *Phenylobacterium*. [src: metabolic_capability_dependency]
- Compare ICA modules with ortholog-transfer predictions while varying experiment count, component caps, membership thresholds, and Pfam/KEGG enrichment rules. [src: fitness_modules]
- Test whether the 38 accessory module families are enriched for mobile elements, operon structure, or niche-associated environments. [src: module_conservation]
- Test the 9,557 essential dark genes with CRISPRi and validate the 998 dark-gene operon pairs supported by conserved synteny and strong cofitness. [src: functional_dark_matter]
- Fold the 6,427 truly dark genes into the essentiality-prioritization workflow, beginning with structure prediction, Foldseek searches, and condition-matched growth assays for the 100 ranked candidates. [src: truly_dark_genes]
- Extend pangenome linkage to the 17,479 unlinked dark genes and test whether the estimated approximately 2,841 additional truly dark genes reproduce the linked-set essentiality and phenotype distributions. [src: truly_dark_genes]
- Test the Methanococcus-focused cofitness signal reported as r > 0.97 and characterize contiguous dark islands as possible prophage remnants or acquired metabolic cassettes. [src: truly_dark_genes]
- Refit genotype–condition models after ChEBI-based canonicalization and compare high-AUC substrates with condition-matched TnSeq and knockout essentiality. [src: genotype_to_phenotype_enigma]
- Reanalyze the metal atlas with organism-specific tolerance normalization, phylogenetic independent contrasts, and removal of genes important for non-metal stresses. [src: metal_fitness_atlas]
- Resolve locusId mismatches, validate classifications against `specificphenotype`, and repeat metal-specificity estimates across sick-rate thresholds from 1–20%. [src: metal_specificity]
- Rebuild all cross-project organism and strain joins with assembly accessions, genus checks, NCBI-taxid-backed synonymy, and explicit GTDB-version tracking. [src: pitfalls]
- Obtain current Web of Microbes or GNPS2/Northen laboratory data with consumption actions; test whether produced and consumed metabolites predict Fitness Browser gene importance after strain-resolved matching. [src: webofmicrobes_explorer]
- Curate exact compound identities for the 107 formula-only ModelSEED matches and build a pathway-to-metabolite lookup table for GapMind; then test the proposed E/(E+I) metabolic-novelty phenotype against accessory genes and pangenome openness. [src: webofmicrobes_explorer]
- Repeat environment-linked essentiality analyses after AlphaEarth NaN filtering and stratification by environmental versus human-associated samples, quantifying the effect of 52.7% unknown per-genome environment labels. [src: pitfalls]
- Execute large-scale joins with live catalog discovery, explicit casts, key-filtered Spark SQL, and checkpointed outputs; compare results against legacy namespace and REST workflows. [src: pitfalls]

## [[concepts/gene-function-acquisition-depth|Phylogenetic acquisition depth and ecological distribution of gene functions]]

- Combine per-CDS sequence data with composition-based donor detection and DTL reconciliation; complete deferred PSII, PUL, and mycolic-acid neighborhood scans; and bootstrap M22 gain events to test transfer histories and recent-to-ancient ratio stability. [src: gene_function_ecological_agora]
- Use matched species-clade pangenomes and fitness-tested strains to test whether the ρ = 0.69 openness association, partial rho=0.530 variable-pathway association, and partial ecotype rho=0.322 survive correction for species composition, sampling imbalance, genome count, and phylogeny. [src: metabolic_capability_dependency; pathway_capability_dependency]
- Extend pangenome linkage to the 17,479 unlinked dark genes, then test whether the estimated approximately 2,841 additional truly dark genes reproduce the linked set’s length, orthology, GC-deviation, mobile-element, and fitness patterns. [src: truly_dark_genes]
- Structure-predict the top 100 truly dark candidates with AlphaFold2 or ESMFold and search Foldseek; test PV4/5210953 by motility assays, ANA3/7026383 under nitrogen limitation, and selected candidates with mobile-CRISPRi. [src: truly_dark_genes]
- Test whether truly dark-gene operon-like cofitness and ICA-module associations predict functions by measuring neighboring genes, module-linked conditions, and polar-effect controls in the prioritized organisms. [src: truly_dark_genes]
- Reanalyze MicrobeAtlas with finer environment categories, alternative trees, discrete/count phylogenetic models, rarefaction, manual validation of 100 AMRFinderPlus clusters, and metal-stress microcosms. [src: microbeatlas_metal_ecology]
- Use PaperBLAST’s 129,823 VIMSS links to test whether sequence-family darkness predicts missing fitness measurements, and repeat acquisition-depth and ecological analyses after stratifying by literature coverage, organism research intensity, and 50% identity cluster size. [src: paperblast_explorer]
- Analyze PGP gene neighborhoods and operonic context, validate pqqC, acdS, hcnC, nifH, and pqqD with gene-integrity and expression tests, and determine whether the pqqC–acdS association reflects physical linkage, repeated ecological selection, or independently inherited loci. [src: pgp_pangenome_ecology]
- Replace defense-domain presence calls with PADLOC MacSyFinder-style multi-Pfam and gene-order rules for Retron, DISARM, and Gabija; quantify how refined calls alter accessory enrichment and defense-system prevalence. [src: phage_defense_arsenal]
- Reconstruct a phaC gene tree and use phylogenetic logistic regression or phylogenetic independent contrasts to test whether the 311 putative acquisition events, 278 putative losses, and elevated accessory fraction remain after shared ancestry is modeled. [src: phb_granule_ecology]
- Perform the pending T4SS–CAZy synteny-threshold permutation test using unfiltered Spark data, BLAST-validate Node_4915 against NCBI nr, construct a housekeeping-gene null baseline, and calculate θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)] for biome enrichment. [src: t4ss_cazy_environmental_hgt]
- Measure growth across environmental media for pathways classified as latent in Fitness Browser conditions, asking whether latent capability becomes condition-specific dependency and whether continuous performance remains poorly predicted by pathway presence alone. [src: pathway_capability_dependency]

## [[concepts/fitness-importance-versus-ecological-context|Gene length confounds fitness-based prediction of pangenome conservation]]

- Use the `gene_fitness_conservation.csv` data for the 2,725 analyzed genes, together with insertion counts or other transposon-callability measures, in nested cross-validated models to test how much of gene length's CV-AUC 0.645 contribution remains after measurement quality is modeled explicitly. [src: field_vs_lab_fitness]
- Add the 678 essential genes through a missing-fitness or two-stage model, then test whether gene length predicts core status similarly among essential genes and genes with recovered transposon mutants. [src: field_vs_lab_fitness]
- Replace binary core/auxiliary labels with quantitative gene-cluster prevalence and fit length-adjusted regression models to ask whether gene length primarily predicts the core boundary or also predicts intermediate prevalence across the pangenome. [src: field_vs_lab_fitness]
- Reanalyze fitness across the reported thresholds from -1 to -3 with gene length, insertion coverage, and fitness uncertainty as covariates to test whether length confounding changes condition-specific conservation patterns. [src: field_vs_lab_fitness]

## [[concepts/genetic-perturbation-coverage-bias|Perturbation-Collection Coverage Bias]]

- Re-sequence and re-annotate the 272 TnSeq-dispensable genes lacking deletion-collection growth data, then test whether annotation updates explain their missing perturbation phenotypes. [src: adp1_deletion_phenotypes]
- Compare deletion-mutant construction success and phenotype completeness against gene length, annotation status, pangenome frequency, and pseudogene indicators using a multivariable logistic model to separate technical and evolutionary predictors of coverage. [src: adp1_deletion_phenotypes]
- Replace the species-level core/accessory labels with population-level pangenome frequencies and test whether the coverage association remains after controlling for gene fragments and uncertain classifications. [src: adp1_deletion_phenotypes]
- Add the 316 genes with incomplete data and the 499 excluded essential genes where technically possible, then repeat condition-specific fitness analyses to quantify how collection composition changes the inferred essentiality landscape. [src: adp1_deletion_phenotypes]

## [[concepts/subsurface-bacillota-specialization|Genome Expansion Versus Streamlining in Specialized Microbes]]

- Partition the 547 enriched OGs by genus and phylogenetic background using genus-stratified enrichment or a phylogenetically controlled model to determine which signals persist beyond lineage structure. [src: bacillota_b_subsurface_accessory]
- Reclassify the 462 “other or unannotated” OGs with an LLM-assisted or manual functional scan, then test whether the inferred 80–100 anaerobic-respiration-related OGs remain enriched after standardized annotation. [src: bacillota_b_subsurface_accessory]
- Compare genome size, OG count, and functional categories across additional phylum-matched subsurface cohorts to test whether expansion is specific to these Bacillota_B lineages or recurs across subsurface specialists. [src: bacillota_b_subsurface_accessory]
- Add rock-attached Bacillota_B genomes and repeat the same pangenome comparison to test whether the observed expansion characterizes porewater-associated isolates specifically or deep-clay Bacillota_B more broadly. [src: bacillota_b_subsurface_accessory]
- Use pathway-level reconstruction and phenotype or growth data to test whether the additional genome content improves predicted self-sufficiency under anaerobic subsurface conditions rather than merely reflecting lineage-specific accessory genes. [src: bacillota_b_subsurface_accessory]

See the source-level discussion in [[summaries/bacillota_b_subsurface_accessory__REPORT]].

## [[concepts/genome-size-confounding-of-functional-scores|Genome Size and Annotation Breadth Can Confound Normalized Functional Scores]]

- Match BacDive GCA accessions directly to [[entities/kbase-ke-pangenome]] genome identifiers, recover more of the 56.6% unmatched strains, and test whether matching failure is associated with genome size or isolation environment. [src: bacdive_metal_validation]
- Refit the BacDive environment comparisons with genome size, annotated-cluster count, taxonomic group, and culture-source category as covariates, and ask whether the contamination effect remains after separating numerator and denominator effects. [src: bacdive_metal_validation]
- Compare absolute metal-tolerance cluster counts with the normalized score across the same matched strains, and test whether ecological rankings change when annotation breadth is held constant. [src: bacdive_metal_validation]
- Integrate [[entities/enigma-coral]] community data from the Oak Ridge metal-contaminated site and test whether field abundance associations agree with genome-size-adjusted metal-tolerance predictions. [src: bacdive_metal_validation]
- Expand BacDive metal-phenotype extraction beyond the current metabolite-utilization records to include MIC and growth-inhibition data, then test whether measured phenotypes track normalized scores independently of genome and annotation breadth. [src: bacdive_metal_validation]

## [[concepts/genome-wide-versus-locus-specific-ecological-adaptation|Genome-Wide Versus Locus-Specific Ecological Adaptation]]

- Use the existing 13,381-genome dataset and test COG functional categories, including V-Defense and L-Mobile, with the same distance-based correlation framework to determine whether specific functional subsets show stronger environmental effects than whole-genome gene content. [src: ecotype_analysis]
- Reanalyze the 172 species with alternative [[entities/alph-aearth]] embedding distances and direct environmental metadata to test whether the weak environmental signal is caused by representation or distance-choice limitations. [src: ecotype_analysis]
- For species with identified ecotype clusters, compare gene-cluster presence/absence profiles between clusters while controlling for phylogenetic similarity to test whether ecological differentiation is concentrated in particular loci. [src: ecotype_analysis]
- Quantify the effect of missing or imprecise geographic metadata by repeating the analysis on species and genomes with higher-resolution environmental records, asking whether environmental effects become stronger when microenvironment assignments improve. [src: ecotype_analysis]

## [[concepts/genomic-dispersal-functional-coupling|Physically Dispersed Genes Can Form Tightly Coupled Metabolic Systems]]

- Add benzoate, catechol, vanillate, iron limitation, and respiratory-inhibitor conditions to the ADP1 fitness matrix, then test whether the dispersed support network separates aromatic-substrate effects from iron, cofactor, and respiratory-load effects. [src: aromatic_catabolism_network]
- Search the ADP1 genome for NDH-2 and compare NDH-2 deletion fitness on quinate versus glucose to test whether alternative NADH dehydrogenase capacity explains condition-dependent Complex I coupling. [src: aromatic_catabolism_network]
- Test ACIAD3137 and ACIAD2176 with protein-protein interaction or co-purification assays to determine whether their r > 0.98 co-fitness relationships reflect physical Complex I association. [src: aromatic_catabolism_network]
- Add PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints to the ADP1 FBA model, then ask whether explicit support-system constraints reconcile the 0% predicted Complex I essentiality with the observed defects in 10/13 Complex I operon subunits. [src: aromatic_catabolism_network]
- Compare Complex I retention across aromatic-degrading species using pangenome data to test whether genomic dispersion and respiratory coupling are conserved beyond ADP1. [src: aromatic_catabolism_network]

## [[concepts/subsurface-hydrogeological-zonation|Groundwater–Sediment Community Partitioning]]

- Collect groundwater and sediment contemporaneously at the same wells and repeat paired Bray–Curtis comparisons to separate habitat partitioning from the 18-month sampling offset. [src: enigma_sso_asv_ecology]
- Load the 221 registered SSO geochemistry samples into CORAL and test whether nitrate, pH, and metal concentrations explain the groundwater–sediment taxonomic contrast. [src: enigma_sso_asv_ecology]
- Extract pump-test ASVs from Brick 460-462 for L8, M5, and U2 and test whether the predicted *Rhodanobacter* maximum occurs at M5. [src: enigma_sso_asv_ecology]
- Perform same-resolution metagenomic profiling of groundwater and sediment to test whether habitat-enriched taxa carry the inferred denitrification, iron-oxidation, iron-reduction, sulfur-oxidation, and methanotrophy functions. [src: enigma_sso_asv_ecology]
- Repeat groundwater and sediment sampling across seasons to determine whether the observed partitioning persists during plume and environmental change. [src: enigma_sso_asv_ecology]

Related source: [[summaries/enigma_sso_asv_ecology__REPORT]]

## [[concepts/homology-search-negative-evidence|Negative homology-search results require sensitivity validation]]

- Search named RefSeq proteomes with Pfam HMMs and sequence-based homology methods to determine whether unannotated paralogs explain the PaperBLAST negatives for LpxA, LpxC, LpxD, LpxB, and LpxK. [src: caulobacter_fur_lipida_loss]
- Build a sensitivity benchmark from the 11 NCBI LpxA hits, 15 NCBI LpxC hits, 15 NCBI LpxD hits, 18 NCBI LpxB hits, and 18 NCBI LpxK hits, then compare recall across PaperBLAST, NCBI annotation, and Pfam HMM searches. [src: caulobacter_fur_lipida_loss]
- Reanalyze *M. catarrhalis* with a complete, quality-controlled proteome because the PaperBLAST representation contained 162 genes total, and test whether the reported absence claims persist after improved coverage. [src: caulobacter_fur_lipida_loss]
- Compare the Caulobacter sphingolipid substitution route with PBP1A, Ld-transpeptidase, capsule-biosynthesis, and *lpxX/lpxL* alternatives using profile-HMM and synteny searches to ask whether replacement pathways are genuinely absent or merely poorly annotated. [src: caulobacter_fur_lipida_loss]

## [[concepts/horizontal-gene-transfer-driven-innovation|Horizontal Gene Transfer as a Driver of Bacterial Gene Novelty]]

- Expand the comparison beyond the 32 analyzed species and test with phylum-stratified models whether the +10.88% COG L, +2.83% COG V, and +1.64% COG S enrichments remain consistent across additional taxonomic groups. [src: cog_analysis]
- Reanalyze the novel and singleton genes with gene-tree/species-tree reconciliation and genomic-context methods to test whether COG L enrichment corresponds to directly inferred HGT events. [src: cog_analysis]
- Examine COG L and COG V genes as linked neighborhoods using synteny and module-level coinheritance analyses to test the hypothesis that mobile defense islands explain the +0.34% LV enrichment. [src: cog_analysis]
- Join COG assignments to environmental metadata and use habitat-stratified comparisons to ask whether mobile, defense, and unknown-function enrichment varies by habitat. [src: cog_analysis]
- Quantify how genes without COG annotation change the inferred novelty partition using alternative annotation resources and sensitivity analyses. [src: cog_analysis]

## [[concepts/intrinsic-versus-acquired-resistance|Intrinsic and Acquired Resistance Occupy Different Genomic Compartments]]

- Map AMR proteins to CARD ARO terms and re-estimate core, auxiliary, and singleton fractions by resistance mechanism; question: does ontology-based classification preserve the intrinsic-acquired compartment contrast after reducing the 22.2% Other/Unclassified category? [src: amr_pangenome_atlas]
- Infer AMR gene gain and loss rates from species phylogenies and gene-family distributions; question: do low-core AMR families show turnover rates consistent with repeated acquisition and loss? [src: amr_pangenome_atlas]
- Test co-localization of accessory AMR genes with genomic islands, insertion sequences, and integrons; question: are the least-conserved AMR genes physically associated with mobility features? [src: amr_pangenome_atlas]
- Extend Fitness Browser linking beyond 100% DIAMOND identity and measure fitness under antibiotic stress; question: do closely related acquired variants and mobile clinical resistance genes incur costs that are missed under the current laboratory and sequence-matching filters? [src: amr_pangenome_atlas]
- Use NMDC and MGnify environmental metagenomes with resolved isolation metadata; question: does the intrinsic-acquired genomic-compartment pattern persist in community-level environmental resistomes rather than genome databases alone? [src: amr_pangenome_atlas]

## [[concepts/lab-field-fitness-concordance|Testing whether laboratory fitness phenotypes predict environmental gene distributions]]

- Use full NMDC sample labels with within-sample permutation tests that preserve taxonomic structure to determine whether the 441 of 449 exploratory associations remain after compositional coupling is controlled. [src: functional_dark_matter]
- Run the complete carrier-versus-non-carrier biogeographic pipeline on matched annotated-accessory-gene controls to test whether dark-gene associations exceed the background rate for accessory genes. [src: functional_dark_matter]
- Expand environmental validation beyond the 5 of 6 matched carrier genera by integrating species-resolved or strain-resolved observations and asking whether laboratory phenotype–environment concordance persists below genus level. [src: functional_dark_matter]
- Increase environmental metadata coverage beyond the 28% AlphaEarth genome coverage and harmonize isolation-source fields to test whether the 29/47 concordance estimate changes with improved environmental resolution. [src: functional_dark_matter]
- Replicate the pre-registered pH, nitrogen-source, carbon-source, and anaerobic predictions in independent cohorts using partial-correlation or matched-sample models to distinguish ecological signal from study and taxonomic composition. [src: functional_dark_matter]

## [[concepts/laboratory-fitness-versus-natural-selection|Laboratory Fitness as an Imperfect Proxy for Natural Selection]]

- Combine the 5,526 costly-and-dispensable genes with mobile-element annotations and genome-loss histories, then test whether they show signatures of recent acquisition or ongoing loss. [src: conservation_fitness_synthesis]
- Link core trade-off genes to AlphaEarth environmental data and use comparative analysis to ask whether organisms from more variable environments have more trade-off genes in their core. [src: conservation_fitness_synthesis]
- Compare RB-TnSeq results across the 43 organisms and identify gene families that are essential in every organism, then test whether their conservation persists across additional environmental conditions. [src: conservation_fitness_synthesis]
- Characterize the 48 accessory modules containing co-regulated functions exclusively in the flexible genome, then test their fitness across environmental conditions and genetic backgrounds. [src: conservation_fitness_synthesis]
- Pair direct fitness assays in soil, biofilms, or host-associated conditions with pangenome conservation to determine which laboratory-burdened core genes provide context-dependent natural-environment benefits. [src: conservation_fitness_synthesis]

## [[concepts/metabolic-capacity-specialization|Utilization capacities are phylogenetically concentrated and specialist-dominated]]

- Combine the 3109-genome capacity matrix with GTDB phylogeny and a phylogenetically controlled permutation or trait-evolution model to test whether the observed specialist distribution exceeds lineage-based null expectations. [src: enigma_carbon_census_1]
- Recompute capacity co-occurrence after removing xanthine/R02107 and regenerating committed tables, then compare odds ratios and Jaccard indices with fitness-matched null models to determine which associations persist after the carbon-category correction. [src: enigma_carbon_census_1]
- Link the 569 utilizer prediction rows to the 3825 taxonomy-bearing NMDC metagenomes and use sample-aware models to test whether high-versatility genera are enriched in periphyton relative to soil, freshwater, sediment, and plant environments. [src: enigma_carbon_census_1]
- Experimentally test specialist and generalist isolates on multiple callable compounds using matched enrichment and growth assays to ask whether predicted capacity breadth corresponds to realized carbon utilization. [src: enigma_carbon_census_1]
- Extend the analysis to the 74 organism-dark compounds using targeted PaperBLAST, abstract-level literature mining, and pathway reconstruction to determine whether the apparent specialization persists after annotation gaps are reduced. [src: enigma_carbon_census_1]

## [[concepts/metabolic-competition-versus-direct-antagonism|Metabolic Overlap Explains Part but Not All of Microbial Antagonism]]

- Measure the complete 10-pair interaction matrix for the five-species core with RFU-based competition assays and substrate-resolved co-cultures to determine whether pairwise effects are additive, synergistic, or antagonistic. [src: cf_formulation_design]
- Repeat inhibition and carbon-utilization assays in biofilm models containing mucins, lipids, iron, polyamines, and the genomically nominated sugar alcohols to test whether the planktonic metabolic-overlap relationship transfers to airway-like conditions. [src: cf_formulation_design]
- Test PAO1 and 3–5 mucoid clinical PA isolates alongside PA14 to determine whether metabolic predictors and residual inhibitor rankings generalize across pathogen backgrounds. [src: cf_formulation_design]
- Expand the matched isolate cohort and use held-out validation to determine whether genus-level residuals predict direct antagonism after controlling for metabolic overlap, growth kinetics, and phylogenetic relatedness. [src: cf_formulation_design]
- Combine metabolite profiling, transcriptomics, and targeted inhibition assays for *S. salivarius* ASMA-737, *G. sanguinis* ASMA-3044, and *N. mucosa* ASMA-3643 to identify mechanisms underlying their +74.1%, +62.2%, and +57.2% positive residuals. [src: cf_formulation_design]

## [[concepts/metabolic-model-gapfilling|Metabolic Model Gapfilling and Prediction Reliability]]

- Join the 243 missing functions and 105,376 gap-dependent growth predictions to pangenome conservation and functional annotations, then test whether core versus accessory status predicts false-negative frequency and mean gap count. [src: acinetobacter_adp1_explorer]
- Re-run pathway enrichment on the 227 FBA-TnSeq-discordant genes; stratify 121,519 predictions by exact gap count, reaction conservation class, and phenotype; and compare rich- versus minimal-media flux changes for the 177 genes with condition-specific fitness. [src: acinetobacter_adp1_explorer]
- Build a matched-gene comparison of FBA, knockout lethality, TnSeq fitness, and growth rate; reconstruct the 38 false-negative cases with alternative gapfilling and curated media while testing whether 42.5% accuracy and 330 false positives improve without reducing recall of 86.5%. [src: adp1_triple_essentiality, annotation_gap_discovery]
- Prioritize the 44 high-confidence assignments and characterize the 50 EC-less reactions. [src: annotation_gap_discovery]
- Add measured trace aromatic compounds to FBA media, re-simulate beta-ketoadipate cases, and test whether the 9-of-11 aromatic discordance and FBA under-prediction enrichment are reduced. [src: adp1_triple_essentiality]
- Measure the ADP1 NDH-2 deletion phenotype, NADH/NAD⁺ ratios, respiratory-chain protein levels, and growth on quinate, glucose, acetate, lactate, and urea; characterize ACIAD3522 and add enzyme-capacity constraints to test whether flux-rate limits explain the Complex I and alternative-dehydrogenase profiles. [src: respiratory_chain_wiring]
- Expand the cross-species K03885 and K00330–K00343 search across 27K species using KO-based orthology, and perform the planned Acinetobacter pangenome co-occurrence analysis. [src: respiratory_chain_wiring]
- Re-run the 23 pathway-organism comparisons with explicit condition-specific fitness measurements and benchmark Bakta, eggNOG, and their union on unresolved gapfilled reaction-organism pairs. [src: discoveries]
- Check DvH for lower-confidence serine predictions and test growth on serine-free minimal medium with complementation or targeted pathway-gene validation. [src: essential_metabolome]
- For the 1,256 functional-dark-matter organism–pathway pairs, compare GapMind calls with condition-matched Fitness Browser phenotypes and test whether high-confidence EC-prefix matches predict growth better than Pfam-family or keyword matches. [src: functional_dark_matter]
- Map the 601 FW300-N2E3 fitness-active genes to GapMind pathway steps and distinguish biosynthetic, catabolic, regulatory, and housekeeping signals. [src: fw300_metabolic_consistency]
- Re-run the metabolic-capability/dependency analysis using direct GapMind per-step gene assignments, matched media, and explicit clade linkage; test whether the 15.8% latent fraction and the ρ = 0.69 pangenome association persist after correcting the taxonomy-field failure. [src: metabolic_capability_dependency]
- Measure growth, uptake, secretion, and flux for representative carbon-utilization pathways classified as latent, intermediate, and active, testing whether pathway class predicts FBA reliability under matched conditions. [src: metabolic_capability_dependency]
- Obtain the current WoM dataset from GNPS2 or the Northen laboratory, recover organism consumption actions, and re-test whether produced or consumed metabolites predict Fitness Browser gene fitness under matched conditions. [src: webofmicrobes_explorer]
- Build a WoM pathway-to-substrate/product lookup table, manually curate the 107 formula-only ModelSEED candidate sets, and test whether exact compound identity improves reaction-level gapfilling. [src: webofmicrobes_explorer]
- Test whether higher WoM `E/(E+I)` metabolic novelty fractions associate with pangenome openness or accessory genes, using strain-to-genome mappings rather than genus-level links. [src: webofmicrobes_explorer]
- Test whether the 10 metabolic ecotype clusters remain environment-associated after phylogenetic correction and finer metadata integration, then use validated environment-linked pathway differences as model constraints rather than direct evidence of flux. [src: metabolic_capability_dependency]
- Add measured metabolite concentrations and uptake bounds to NMDC-linked models, and use study-aware mixed models or sample-level permutations to distinguish environmental occurrence from utilization. [src: discoveries, enigma_carbon_census_1]
- Obtain metabolomics for the 33 Freshwater samples and add pH, temperature, and total organic carbon to study-aware partial-correlation or mixed-effects models; test whether the 11/13 negative pathway–metabolite directions persist after abiotic and study-level adjustment. [src: nmdc_community_metabolic_ecology]
- Pair community GapMind completeness with metatranscriptomics, measured uptake, secretion, and metabolite concentrations to test whether expression-weighted pathway completeness predicts flux more reliably than genomic potential alone. [src: nmdc_community_metabolic_ecology]
- Resolve the 61 Unknown-ecosystem samples through NMDC ENVO annotations and improve KEGG compound mapping for cysteine, histidine, and lysine before extending community-scale FBA constraints. [src: nmdc_community_metabolic_ecology]
- Calibrate the condition-specific importance score against an independent essentiality set, such as known essentials from essential_metabolome, then re-test the 66 Latent Capability pairs without a subset-defined median threshold. [src: pathway_capability_dependency]
- Re-run the pathway-variation and ecotype-openness analyses with phylogenetic independent contrasts, balanced genome sampling, and alternative clustering cutoffs; test whether rho=0.530 and rho=0.322 persist within genera and across species. [src: pathway_capability_dependency]
- Test the accessory-dependent amino-acid completeness gaps experimentally by comparing community composition, extracellular leucine, valine, arginine, lysine, and threonine, uptake, secretion, and expression; this would distinguish accessory capacity from demonstrated metabolite sharing. [src: pathway_capability_dependency]
- Recalculate plant-associated pathway completeness with less stringent core thresholds, direct GapMind gene assignments, and matched BacDive strains; test whether the 83.1% GapMind–BacDive consistency and 0% core-level completeness persist after taxonomic and annotation controls. [src: plant_microbiome_ecotypes]
- Pair plant-associated genomic markers with transcriptomics, measured uptake, secretion, and growth under defined root, rhizosphere, and phyllosphere conditions; test whether the 78.7% dual-nature classification predicts condition-specific activity rather than marker presence alone. [src: plant_microbiome_ecotypes]
- Reassess plant-community complementarity after restoring the 62/322 lost NMDC genera, using reaction-level pathway profiles and explicit metabolite exchange measurements rather than genus-level completeness alone. [src: plant_microbiome_ecotypes]
- Expand phylogenetic-tree coverage and apply accessory-gene or gene-content trees to the 65 plant-associated species; test whether the five Bonferroni-supported within-species signals and host segregation in *Xanthomonas campestris* and *Xanthomonas vasicola* predict transferable model constraints. [src: plant_microbiome_ecotypes]
- Extend GapMind with KEGG modules for toluene, naphthalene, benzoate, and other aromatic pathways, then test whether these additions improve environmental prediction beyond the 62 common pathways in *Pseudomonas*. [src: pseudomonas_carbon_ecology]
- Apply PGLS or phylogenetic logistic regression to the *Pseudomonas* pathway profiles using the GTDB species tree, balanced genome sampling, and finer source metadata; test whether the p = 0.006 environment association and the subgenus sugar-pathway differences persist after phylogenetic control. [src: pseudomonas_carbon_ecology]
- Use the 789,012-row genome-level carbon-pathway matrix to model within-species variation in *P. fluorescens* and *P. putida*, and cross-reference predicted ecotypes with RB-TnSeq fitness data from the `kescience_fitnessbrowser` collection. [src: pseudomonas_carbon_ecology]

## [[concepts/metabolic-model-gapfilling|Empirical validation reveals condition-dependent limits of metabolic-model predictions]]

- Use the 227 FBA–TnSeq-discordant genes with pathway enrichment and targeted inspection of regulatory annotations to ask whether discordance is concentrated in particular metabolic functions or reflects regulatory effects absent from the model. [src: acinetobacter_adp1_explorer]
- Refit and revalidate the ADP1 metabolic model separately on minimal media and LB using the 499-versus-346 essentiality calls and the 177 of 866 flux-class changes to ask which condition-specific constraints improve prediction agreement. [src: acinetobacter_adp1_explorer]
- Reassess the 121,519 growth phenotype predictions after removing or ranking the 243 missing functions by pangenome support, then test whether gapfill confidence reduces the false-negative excess associated with higher mean gap counts. [src: acinetobacter_adp1_explorer]
- Compare predictions across the eight carbon-source fitness conditions, prioritizing urea versus quinate and butanediol-acetate versus butanediol-lactate, to ask whether condition-specific mutant fitness can identify missing model reactions. [src: acinetobacter_adp1_explorer]

## [[concepts/metabolic-overflow-and-ecological-secretion|Metabolic Overflow and Ecological Secretion]]

- Map FW300-N2E3 Fitness Browser genes to individual GapMind pathway steps, using the deferred NB04 analysis, to separate biosynthetic, catabolic, and regulatory contributions to tryptophan-associated fitness. [src: fw300_metabolic_consistency]
- Build a community metabolic model for the Oak Ridge groundwater community to test whether FW300-N2E3 tryptophan release can support predicted auxotrophic recipients. [src: fw300_metabolic_consistency]
- Repeat Web of Microbes profiling across growth media to determine whether tryptophan and trehalose production is constitutive or medium-dependent. [src: fw300_metabolic_consistency]
- Expand metabolite matching with InChIKey or CHEBI identifiers to test whether currently unmatched Web of Microbes compounds contain additional production-versus-utilization discordances. [src: fw300_metabolic_consistency]
- Repeat the cross-database analysis for other ENIGMA isolates, including [[entities/pseudomonas-stutzeri-rch2]], to test whether the proposed ecological-secretion pattern is isolate-specific or recurrent. [src: fw300_metabolic_consistency]

## [[concepts/metabolic-pathway-support-networks|Auxiliary cofactor, respiratory, metal, and regulatory genes form pathway-support networks]]

- Measure Complex I and NDH-2 deletion fitness directly on quinate, glucose, acetate, and succinate to test whether the dependency follows aromatic chemistry or NADH-generating load. [src: aromatic_catabolism_network]
- Expand the ADP1 condition panel with benzoate, catechol, vanillate, iron limitation, and respiratory inhibitors, then recompute co-fitness to determine whether the 51-gene network separates into substrate-, iron-, and respiration-specific modules. [src: aromatic_catabolism_network]
- Test ACIAD3137 and ACIAD2176 by protein–protein interaction or co-purification experiments to distinguish direct Complex I accessory roles from indirect phenotypic correlations. [src: aromatic_catabolism_network]
- Add PQQ-biosynthesis, iron-homeostasis, and respiratory-chain capacity constraints to the ADP1 FBA model, then compare predicted essentiality with the observed defects for 10/13 Complex I operon subunits. [src: aromatic_catabolism_network]
- Compare Complex I retention across aromatic-degrading species using pangenome data to test whether respiratory-support architecture is conserved or lineage-specific. [src: aromatic_catabolism_network]

## [[concepts/environmental-resistome|Metadata Resolution Can Hide Within-Species Environmental Heterogeneity]]

- Use the 280,337 genomes with NCBI environment metadata and a per-genome AMR-by-environment contingency analysis, such as the originally planned Fisher's exact test or a scalable equivalent, to determine whether AMR enrichment remains after conditioning on species. [src: amr_environmental_resistome]
- Use the 823 species in the reported multi-environment subset and hierarchical or mixed-effects models to separate within-species environment effects from between-species clinical representation, asking whether the 72.9-versus-16.4 mean AMR-cluster contrast persists within species. [src: amr_environmental_resistome]
- Use deeply sampled species including *Klebsiella pneumoniae*, *Staphylococcus aureus*, and *Salmonella enterica*, with genome-level environment labels and accessory-cluster presence/absence matrices, to test whether the reported 99%, 99%, and 99% accessory fractions are concentrated in particular environments. [src: amr_environmental_resistome]
- Use per-genome environment metadata together with phylogeny and family-level stratification to test whether the 20 of 141 significant family-level effects reflect genuine within-family ecological structure or uneven environmental sampling. [src: amr_environmental_resistome]

## [[concepts/metal-cross-resistance|Metal cross-resistance across bacterial fitness landscapes]]

- Apply KEGG/PFAM mapping to cross-resistance gene signatures across 27K species, then test whether the signatures predict metal-associated isolation at pangenome scale and whether the result reproduces Cohen's d = +1.0. [src: metal_cross_resistance]
- Normalize fitness effects by metal concentration relative to MIC, then retest the 85 metal-pair associations to determine how much of the chemistry-specific magnitude layer is dose-driven. [src: metal_cross_resistance]
- Add non-metal stress controls and use ICA, or independent component analysis, of metal-condition modules to test whether the 98.1% positive correlation pattern is metal-specific or a general-stress axis. [src: metal_cross_resistance]
- Use phylogenetic independent contrasts or PGLS across the 28 organisms to test whether cross-resistance direction and metal-pair ranking remain conserved after accounting for shared ancestry. [src: metal_cross_resistance]
- Use AlphaFold-based structural analysis of the 318 conserved metal-shared ortholog groups to ask whether shared structural features explain their cross-metal importance. [src: metal_cross_resistance]
- Rebuild the BacDive validation with explicit species-level matching, the reported sample definitions, and independent species counts to determine whether environmental isolation is associated with multi-metal gene signatures. [src: metal_cross_resistance]
- Reanalyze atlas genes using a metal-specific definition that excludes genes important for other stresses, then compare core enrichment and cross-metal correlations with the three-tier classes. [src: metal_fitness_atlas]
- Test the atlas's 149 uncharacterized candidates with PaperBLAST, InterPro, and structural prediction, and evaluate whether regulatory or expression features outperform gene-presence scores for predicting metal fitness. [src: metal_fitness_atlas]
- Resolve the specificity-analysis locusId mismatches, validate classifications against Fitness Browser `specificphenotype` annotations, and repeat the counter-ion comparison using fit < -1 without the |t| > 4 requirement. [src: metal_specificity]
- Use precomputed z-scored Metal Atlas module activities and AlphaFold predictions for UCP030820, YebC, and DUF1043/YhcB to test whether candidate-specificity signals reflect coherent modules or plausible metal-binding structures. [src: metal_specificity]
- Reanalyze MicrobeAtlas with finer marine, freshwater, and saline categories, test alternative phylogenetic models, and relate metal type diversity to site-level contamination metadata to distinguish ecological breadth from sampling and habitat effects. [src: microbeatlas_metal_ecology]
- Test whether covered-read fraction biases Track B community-weighted metal diversity and whether the groundwater prevalence signal persists after species-level rarefaction and explicit genome-coverage correction. [src: microbeatlas_metal_ecology]
- Rerun the soil COG–metal models with partial correlation, including COG ~ Cr | Cu + Zn + Pb, to test whether apparent chromium associations remain after co-contaminating metals are controlled. [src: soil_metal_functional_genomics]
- Report unconditional and conditional db-RDA R² values, audit Spearman rho effect sizes including rho < 0.05, and test residual Moran’s I with SEVM if needed to separate metal, project, and spatial structure. [src: soil_metal_functional_genomics]
- Repeat copper genome–soil attribution at 5 km, 10 km, and 20 km, then compare mechanistically classified resistance, stress, membrane, energy, and unknown COGs across biomes. [src: soil_metal_functional_genomics]
- Validate the ≤10 kb T4SS–CAZy synteny threshold with permutation tests, test Node_4915 against NCBI nr and a housekeeping-gene null, and determine whether GT2-neighborhood metal-resistance enrichment persists after controlling for genome background and biome. [src: t4ss_cazy_environmental_hgt]

## [[concepts/subsurface-hydrogeological-zonation|Inferring subsurface redox gradients from microbial community composition]]

- Load the 221 SSO geochemistry samples into CORAL and test whether nitrate, pH, and metal concentrations form the predicted northeast-to-southwest gradient. [src: enigma_sso_asv_ecology]
- Extract pump-test ASVs from Brick 460-462 for L8, M5, and U2 and test whether [[entities/rhodanobacter]] is highest at M5 and lower at L8 and U2. [src: enigma_sso_asv_ecology]
- Generate metagenomes at the same spatial resolution and test whether genes for inferred denitrification, iron oxidation, sulfur oxidation, nitrification, methanotrophy, and fermentation occur in the predicted locations. [src: enigma_sso_asv_ecology]
- Analyze the 18 M6-C2 isolate genomes for anaerobic metabolisms and test the hypothesis that M6 represents an anaerobic zone. [src: enigma_sso_asv_ecology]
- Apply weighted UniFrac to ASV sequences from Bricks 457/460/477 and test whether phylogenetic community structure strengthens the inferred hydrogeological zonation. [src: enigma_sso_asv_ecology]
- Repeat 16S profiling across seasons and test whether the U3–M6–L7 corridor and the inferred redox hotspots persist through time. [src: enigma_sso_asv_ecology]

## [[concepts/mobile-element-associated-fitness-burden|Mobile genetic elements as measurable host fitness burdens]]

- Reanalyze Fitness Browser measurements with replicate-level models and a continuous burden score rather than the max_fit > 1 rule to test whether MGE-associated genes retain a fitness deficit after reducing single-experiment noise. [src: costly_dispensable_genes]
- Replace binary dispensable/core labels with per-gene genome prevalence and test whether MGE keyword enrichment and fitness burden vary continuously with prevalence. [src: costly_dispensable_genes]
- Re-link genes using lower-identity and profile-based homology searches, then quantify how many current orphan and singleton assignments disappear when recently acquired sequence is recovered. [src: costly_dispensable_genes]
- Compare long-read assemblies, element-boundary calls, and gene-neighborhood information for *Pseudomonas stutzeri* RCH2 to test whether its 21.5% costly+dispensable proportion reflects mobile-element invasion or strain-specific genomic expansion. [src: costly_dispensable_genes]
- Measure costly+dispensable candidates across environmental conditions not represented in the laboratory dataset to test whether the 14.1% condition-specific fraction underestimates context-dependent benefits. [src: costly_dispensable_genes]
- Integrate MGE annotation, ortholog prevalence, and phylogeny across a larger organism set to test whether the observed burden is general or concentrated in particular lineages. [src: costly_dispensable_genes]

## [[concepts/module-level-coinheritance|Multi-gene fitness modules predict pangenome co-inheritance better than pairwise links]]

- Restrict the pairwise and module analyses to auxiliary-only pairs in which both clusters are below 95% prevalence, then test whether the module advantage persists after removing the prevalence ceiling. [src: cofitness_coinheritance]
- Calculate co-fitness directly from raw genefitness data for Ralstonia UW163 and Ralstonia GMI1000, then repeat the module and pairwise comparisons to recover the two organisms excluded because they had zero precomputed co-fitness data. [src: cofitness_coinheritance]
- Resolve reference-genome mapping and apply stronger phylogenetic controls, then test whether module-level delta phi remains higher than pairwise delta phi after ancestry is accounted for. [src: cofitness_coinheritance]
- Build module co-transfer networks and test cross-module prediction to determine whether modules predict one another’s pangenome distributions beyond within-module co-occurrence. [src: cofitness_coinheritance]
- Expand the analysis to species with >30% auxiliary genes and existing co-fitness data, then test whether auxiliary-gene fraction predicts the size and reproducibility of the module-level signal. [src: cofitness_coinheritance]

## [[concepts/multi-heme-cytochrome-detection|Correcting Multi-Heme Cytochrome Markers for Iron-Reduction Comparisons]]

- Reapply the corrected detector to the clay-project branch and test whether the Bagnoud porewater comparison changes when PF02085, PF22678, and the CXXCH threshold are used instead of K07811, K17324, and K17323. [src: bacillota_b_subsurface_accessory] The new report indicates that this reanalysis has now been performed for the reported cohorts, so the remaining task is to verify marker definitions and compartment annotations in the underlying tables. [src: clay_confined_subsurface]
- Use gene-cluster context, protein-domain annotation, and targeted biochemical or expression data to determine which CXXCH-positive clusters are plausibly involved in iron reduction rather than other electron-transfer processes. [src: bacillota_b_subsurface_accessory]
- Increase the number of rock-attached and porewater genomes, then repeat the corrected Fisher tests to ask whether substrate association explains multi-heme cytochrome distribution. [src: bacillota_b_subsurface_accessory] Add deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge to test whether the cultured-cohort result generalizes beyond porewater isolates. [src: clay_confined_subsurface]
- Compare the corrected detector with independently curated iron-reduction markers and metatranscriptomic or proteomic measurements to test whether marker positivity predicts active iron reduction. [src: bacillota_b_subsurface_accessory]
- Resolve the sulfite-versus-sulfate terminology by auditing the retained marker set and linking genome presence to Bagnoud’s metaproteomic evidence. [src: clay_confined_subsurface]

## [[concepts/multi-omics-integration|Multi-Omics Integration]]

- Test metal fitness using concentration-relative-to-MIC normalization, phylogenetic independent contrasts, and genes important for metals but not other stresses; determine whether the 87.4% core enrichment persists after separating general stress from specialized resistance. [src: metal_fitness_atlas]
- Profile the 149 novel metal candidates with PaperBLAST, InterPro, and structural prediction, then validate conserved candidates experimentally across metals and organisms. [src: metal_fitness_atlas]
- Replace simple metal gene-presence scores with regulatory, expression, and module-activity models, using the 600 responsive module records and the UC1 structural-fitness cohort. [src: metal_fitness_atlas]
- Execute UC2–UC5 on the live cluster, validate the UC1 cohort with per-residue pLDDT or structural features, and quantify value-space overlap for `genome_id`, `ncbi_taxon_id`, `sample_id`, and `feature_id`. [src: berdl_data_atlas]
- Add live catalog/schema/type discovery, explicit identifier audits, and value-overlap checks to every cross-tenant integration; test whether dotted Iceberg and fallback underscore namespaces return equivalent records before analysis. [src: pitfalls]
- Join the 866 genes with FBA flux predictions and TnSeq calls to test whether pathway enrichment distinguishes the 227 discordant from 639 concordant genes; add measured trace aromatic compounds and test the 9-of-11 aromatic-degradation discordant set. [src: acinetobacter_adp1_explorer; adp1_triple_essentiality]
- Use cross-strain proteomics and engineered ΔaroF, ΔaroG, and dgoA genotypes to test pathway-localized effects, and validate [[entities/aciad3137]] and [[entities/aciad2176]] with interaction or co-purification experiments. [src: acinetobacter_adp1_explorer; aromatic_catabolism_network]
- Test whether the 625 condition-specific genes replicate across additional carbon sources and technical replicates, and map FW300 fitness-important genes to GapMind biosynthetic, catabolic, regulatory, and housekeeping steps. [src: adp1_deletion_phenotypes; fw300_metabolic_consistency]
- Use the 19 FW300 WoM–Fitness Browser metabolite matches to test gene fitness against explicitly produced metabolites, separating `E` emergence from `I` amplification and adding direct consumption measurements; determine whether production-associated fitness effects persist across media and strains. [src: webofmicrobes_explorer]
- Build the WoM pathway-to-substrate/product lookup table required for GapMind matching, curate the 107 formula-only ModelSEED candidate sets, and test whether `E/(E+I)` metabolic novelty associates with pangenome openness or accessory genes. [src: webofmicrobes_explorer]
- Experimentally test the respiratory wiring model with an NDH-2 deletion, NADH/NAD⁺ measurements on quinate, glucose, acetate, lactate, and urea, direct flux measurements, and KO-based K03885/K00330–K00343 searches across the 27K-species comparison. Characterize ACIAD3522 separately because its respiratory annotation remains uncertain. [src: respiratory_chain_wiring]
- Match BacDive GCA accessions directly to pangenome `genome_id` values, expand MIC and growth-inhibition extraction, and test whether genome-derived metal scores predict measured tolerance. [src: bacdive_metal_validation]
- Experimentally validate the 44 high-confidence annotation-gap assignments, reconstruct the 38 false-negative cases with alternative gapfilling and curated media, and characterize the 50 EC-less dark reactions. [src: annotation_gap_discovery]
- Repeat Caulobacter outer-membrane proteomics with biological replicates and targeted LptD, LptE, *lptC2*, Pal, Tol-Pal, and CCNA_01217 assays; perform iron-limitation, ferric-supplementation, and hemin RB-TnSeq experiments. [src: caulobacter_fur_lipida_loss]
- Reanalyze Harvard Forest with factorial treatment × horizon × incubation models, restore measured abiotic metadata, add direct organic DNA if available, and validate pmoA/pmoB, aceA/icl, and aceB/glcB with quantitative transcripts, proteomics, enzyme activity, and carbon-flux measurements. [src: harvard_forest_warming]
- Repeat the IBD CCA with pathway abundance and batch-aware metabolomics, test whether r = 0.964 survives held-out cohorts, and distinguish abundance, metabolite concentration, and pathway-flux contributions. [src: ibd_phage_targeting]
- Reanalyze the IBD ecotype result with held-out-feature clustering, leave-one-species-out refitting, and within-substudy contrasts; determine whether the three independently supported candidates replicate. [src: pitfalls]
- Reanalyze eukaryotic contamination with GroupKFold by study and within-study contrasts, adding extraction-kit, filtration, host-depletion, library-preparation, and measured-depth metadata. [src: euk_in_prok_correlates]
- Repeat the lignin experiment with n>=5 per group, intermediate passage points, DADA2 ASVs, matched technical metadata, UNITE-based ITS profiling, and functional measurements of beta-ketoadipate and protocatechuate pathways. [src: lignin_community_enrichment]
- Test whether the Round-1 memory index of ~0.50 persists under controlled inoculum, passage number, and carbon-history designs, and compare community-history effects with organism-level fitness measurements. [src: lignin_community_enrichment]
- Replicate the NMDC community BQH analysis across additional studies and paired Freshwater metabolomics, add pH, temperature, and total organic carbon to partial-correlation or mixed-effects models, and pair metatranscriptomics with metabolomics to test whether leucine and arginine associations reflect expressed pathway activity. [src: nmdc_community_metabolic_ecology]
- Improve KEGG compound annotation and replace string-based metabolite matching with identifier-based crosswalks, then test cysteine, histidine, lysine, glutamine, and proline pathways and resolve the 61 Unknown-ecosystem samples using NMDC ENVO annotations. [src: nmdc_community_metabolic_ecology]
- Reanalyze prophage ecology with dedicated prophage callers, genome-size-matched phylogenetic models, and independently validated TerL lineages to determine whether module-level environmental associations persist after separating intact prophages from domesticated remnants. [src: prophage_ecology]
- Test the prophage module–environment associations in NMDC samples with direct prophage detection, sample-level rather than genus-proxy burden estimates, and measured pH, temperature, depth, and nitrogen; determine whether the packaging–pH association is causal or habitat-confounded. [src: prophage_ecology]
- Compare structural, tail, and anti-defense modules with host defense inventories and experimentally measured phage susceptibility in human-associated and freshwater isolates to test the proposed arms-race interpretation. [src: prophage_ecology]

## [[concepts/nonrandom-missingness-in-comparative-genomics|Nonrandom Missingness in Comparative Genomics]]

- Use the complete species-by-genome table and a missingness model, such as logistic regression or inverse-probability weighting, to test whether genome count, environment category, and distance structure predict NaN status. [src: ecotype_env_reanalysis]
- Recalculate correlations after matched downsampling and full-genome extraction, then test whether the missingness-rate difference and the 27x overall correlation discrepancy persist. [src: ecotype_env_reanalysis]
- Add genome count as a covariate in the environment–gene-content association model to test whether unequal sampling depth explains part of the observed correlation pattern. [src: ecotype_env_reanalysis]
- Repeat the analysis using structured ENVO terms from env_broad_scale and compare missingness across ontology-defined environments to test whether coarse classification contributes to group-dependent loss. [src: ecotype_env_reanalysis]
- Analyze transport and secondary-metabolism gene subsets with the same missingness diagnostics to test whether whole-genome Jaccard distances mask environment-specific associations. [src: ecotype_env_reanalysis]

## [[concepts/occurrence-versus-catabolic-activity|Environmental occurrence does not establish compound catabolism]]

- Pair the 86 implicated genera and 83 census compounds with compound-resolved enrichment cultures, substrate depletion measurements, and transformation-product assays to test whether environmental occurrence predicts realized catabolism. [src: enigma_carbon_census_1]
- Use metatranscriptomics or metaproteomics on periphyton and soil samples enriched for the observed genera to test whether candidate catabolic pathways are expressed in the presence of specific census compounds; the current atlas measured occurrence but no compound activity. [src: enigma_carbon_census_1]
- Apply study-aware mixed models or sample-level permutations to the NMDC data to test whether environmental occurrence differences remain after accounting for sampling structure and compositional, zero-inflated abundances. [src: enigma_carbon_census_1]
- Experimentally test the 29 fully orphan compounds in periphyton-sited enrichments to determine whether the observed Burkholderiales/Comamonadaceae reservoir contains unrecognized utilizers. [src: enigma_carbon_census_1]
- Combine GTDB strain placement, pathway-completeness checks, and isotope tracing for selected callable compounds to distinguish genetic utilization potential from measured carbon incorporation. [src: enigma_carbon_census_1]

## [[concepts/ontology-and-category-schema-sensitivity|Ontology and Category-Schema Dependence of Biological Conclusions]]

- Re-run the 52 CD-up pathway analysis with the regex scheme, the curator-validated MetaCyc hierarchy, and a third ontology while holding the statistical model and multiple-testing procedure fixed; test which iron/heme-acquisition conclusion remains stable. [src: discoveries]
- Build a benchmark of independently validated lanthanide-dependent methanol-dehydrogenase genomes and compare preferred-name, KO, product-description, and profile-based markers; quantify precision, recall, and disagreement across marker definitions. [src: discoveries]
- Recompute the 32-species COG enrichment analysis with mutually exclusive versus multi-label category assignments; test whether the +0.34% LV enrichment and 76% consistency persist under each representation. [src: discoveries]
- Reconcile MetaPhlAn3 and Kaiju species namespaces before cross-cohort projection, then compare LDA and CLR-plus-PCA GMM using held-out samples; determine whether the Kuehl E3 assignment is a namespace artifact or a reproducible ecotype signal. [src: discoveries]
- Audit pathway and metabolite joins using explicit identifier dictionaries and collision tests, including leucine versus isoleucine; measure how many inferred pathway associations change after schema-to-value-space validation. [src: discoveries]

## [[concepts/organism-dark-compound-discovery|Organism-dark compounds define a resource-limited discovery frontier]]

- Use the 29 fully orphan compounds, with targeted PaperBLAST and PubMed or abstract-level searches, to ask how many are reclassified when gene-, pathway-, and literature-level evidence is expanded beyond the title-only screen. [src: enigma_carbon_census_1]
- Apply MIBiG and biosynthetic-literature searches to Tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid, and farnesol to ask whether biosynthetic evidence can distinguish catabolism-unknown compounds from genuinely unlinked compounds. [src: enigma_carbon_census_1]
- Regenerate the census tables after removing R02107 from the carbon allowlist and re-run the callable-versus-dark comparison to ask whether the xanthine category error changes the physicochemical or class-level conclusions. [src: enigma_carbon_census_1]
- Recompute callable status under alternative catabolic-direction filters and compare the resulting dark sets to ask how much the 74-compound frontier depends on reaction-selection rules. [src: enigma_carbon_census_1]
- Combine periphyton enrichment cultures with compound-resolved growth assays, genome sequencing, and pathway reconstruction to ask whether the observed Comamonadaceae/Burkholderiales reservoir actually transforms prioritized dark compounds. [src: enigma_carbon_census_1]
- Replace exploratory soil-versus-freshwater rank tests with a study-aware mixed model or sample-level permutation using the environmental atlas to ask whether source-associated occurrence remains after accounting for study structure and compositional, zero-inflated abundances. [src: enigma_carbon_census_1]
- Integrate chemical identity, reaction evidence, measured fitness, taxonomy, and environmental metadata through provenance-aware joins to ask which missing evidence layer most often blocks conversion from dark to callable status. [src: enigma_carbon_census_1]

## [[concepts/homology-search-negative-evidence|Orthogonal validation of gene absence]]

- Search named RefSeq proteomes with Pfam HMMs and profile-based homology methods to determine whether unannotated paralogs undermine the reported absence of *spt*, *cerR*, ChvG, and ChvI in comparator species. [src: caulobacter_fur_lipida_loss]
- Reanalyze the four comparator proteomes with consistent gene calling and annotation pipelines to test whether the *M. catarrhalis* result changes when its 162-gene PaperBLAST representation is replaced by a more complete proteome. [src: caulobacter_fur_lipida_loss]
- Combine genome-resolved pathway reconstruction with targeted lipidomics to test whether the annotated absence of comparator lipid A-loss alternatives corresponds to absence of the predicted biochemical products. [src: caulobacter_fur_lipida_loss]
- Perform cross-species genetic engineering or complementation to test whether the Caulobacter sphingolipid-substitution route is functionally distinct from the alternative routes identified in *A. baumannii* and *N. meningitidis*. [src: caulobacter_fur_lipida_loss]

## [[concepts/outer-membrane-lipid-homeostasis|Outer-membrane lipid homeostasis after lipid A loss]]

- Generate replicated outer-membrane proteomics and targeted *lptC2* and Pal assays to test whether the observed LptD/LptE decline, *lptC2* protein increase, CCNA_01217 increase, and Pal induction are reproducible and statistically supported. [src: caulobacter_fur_lipida_loss]
- Perform lipidomics in wild-type, Δ*fur* Δ*sspB*, and Δ*lpxc*-rescued backgrounds to determine whether sphingolipid abundance and lipid transport change despite the constitutive transcript-level biosynthesis pattern. [src: caulobacter_fur_lipida_loss]
- Measure Tol-Pal phospholipid transport directly and combine the assay with Pal perturbation to test whether Pal-Tol activity is required for outer-membrane lipid homeostasis after lipid A loss. [src: caulobacter_fur_lipida_loss]
- Conduct SigU-induction RNA-seq and genetic tests of the proposed dual-release model to determine whether SigU drives the late ChvI-associated envelope and transport cohort. [src: caulobacter_fur_lipida_loss]
- Add RB-TnSeq experiments under bipyridyl chelation, ferric supplementation, and hemin to test the unresolved iron axis of the rescue mechanism. [src: caulobacter_fur_lipida_loss]
- Use Pfam HMM searches against named RefSeq proteomes to resolve whether comparator species truly lack alternative lipid A-loss routes that may be missed by annotation-dependent searches. [src: caulobacter_fur_lipida_loss]

## [[concepts/pairwise-to-community-interaction-extrapolation|Sparse Pairwise Interaction Data Limit Prediction of Multi-Species Community Effects]]

- Measure all 10 pairwise interactions among the five proposed core species using the same RFU-based competition assay, then test whether the observed edges predict the k=3 and k=5 formulation outcomes. [src: cf_formulation_design]
- Repeat the complete pairwise matrix and the candidate formulations in structured biofilm models, asking whether planktonic synergy scores predict biofilm inhibition of *P. aeruginosa*. [src: cf_formulation_design]
- Separate per-substrate co-culture effects from endpoint carbon-utilization measurements by generating substrate-resolved co-culture data, asking whether competition is additive, synergistic, or antagonistic on the 22 tested substrates. [src: cf_formulation_design]
- Expand the isolate-by-isolate interaction design beyond the 3 A × 3 B combinations and use a hierarchical model to test whether interaction effects are species-level, isolate-specific, or condition-specific. [src: cf_formulation_design]
- Test the candidate formulations against PAO1 and 3–5 mucoid clinical *P. aeruginosa* isolates, asking whether pairwise and community effects transfer beyond PA14. [src: cf_formulation_design]

## [[concepts/pangenome-conservation-fitness-decoupling|Decoupling between pangenome conservation and fitness cost]]

- Use the 144 metal-resistance genes with fitness measurements and compare their standard-condition costs with responses in the metal fitness atlas, using metal-specific fitness analyses to ask whether genes that appear costly under standard conditions are protective under metal stress. [src: amr_fitness_cost]
- Recalculate core/accessory labels from expanded GTDB sampling and test the association with fitness using prevalence thresholds and species-stratified models, asking whether the null result persists when the median sample of 9 genomes is replaced by broader within-species coverage. [src: amr_fitness_cost]
- Analyze mechanism effects within organisms with many AMR genes, including Cup4G11 (77) and BFirm (50), using genetic-background-controlled comparisons to ask whether conservation–cost relationships emerge within species. [src: amr_fitness_cost]
- Extend the analysis from 25 Fitness Browser organisms to all 293K BERDL genomes by predicting AMR cost from gene-cluster conservation patterns, then test whether predicted cost varies with pangenome prevalence outside the lab-adapted strains. [src: amr_fitness_cost]

## [[concepts/pangenome-core-boundary-and-clade-size-bias|Pangenome Core Boundaries and Clade-Size Bias]]

- Recompute core fractions across controlled subsamples of each clade, using repeated genome down-sampling to ask how the essential-versus-non-essential odds ratio changes with clade size. [src: conservation_vs_fitness]
- Reanalyze the 10 organisms excluded for less than 90% DIAMOND coverage with identifier harmonization and orthology-based recovery, asking whether their exclusion changes the 82.0% core and 18.0% auxiliary proportions. [src: conservation_vs_fitness]
- Compare clades with different genome counts using confidence intervals or hierarchical models, asking whether essential-core enrichment remains after explicitly modeling clade size and coverage. [src: conservation_vs_fitness]
- Extend the comparison from binary essentiality to condition-specific fitness, especially genes with fitness < -2 under stress conditions, asking whether conditionally important genes show the same sampling-sensitive conservation pattern. [src: conservation_vs_fitness]

## [[concepts/pangenome-integration|Pangenome Integration Across Identifier Systems]]

- Test whether any of the 4,081 mapped ADP1 clusters split or merge relative to 4,891 BERDL clusters using cluster membership and representative sequences. [src: acinetobacter_adp1_explorer]
- Test fitness–conservation relationships with matched organisms and conditions, controlling for fitness magnitude, breadth, gene length, annotation coverage, and transposon coverage. [src: fitness_effects_conservation]
- Align the 156 fitness-module families and 974 mapped modules to pangenome prevalence, testing core status against organism, experiment count, operon adjacency, and phylogeny. [src: fitness_modules; module_conservation]
- Reconstruct essential-gene modules using measurements that do not require viable transposon insertions. [src: module_conservation]
- Extend pangenome linkage to the 17,479 unlinked dark genes and quantify how the estimated 2,841 additional truly dark genes alter prioritization. [src: truly_dark_genes]
- Test the top truly dark candidates with structure prediction, Foldseek searches, predicted-condition growth assays, mobile-CRISPRi, and genomic-island or prophage-remnant analyses. [src: truly_dark_genes]
- Join environmental AMR classifications to gene-level annotations and fitness, testing CARD ARO mapping, gene gain/loss, islands, insertion sequences, and integrons. [src: amr_environmental_resistome; amr_pangenome_atlas]
- Match BacDive GCA accessions directly to pangenome `genome_id` values and repeat the heavy-metal analysis with enough matched isolates to distinguish a robust effect from the current n=10 estimate. [src: bacdive_metal_validation]
- Reanalyze ecotype cohorts with matched species and genome sets, structured ENVO terms, genome-count covariates, and phylogenetic controls. [src: ecotype_env_reanalysis; ecotype_analysis]
- Directly map GapMind per-step genes to SEED and pangenome clusters and test whether latent-capability and pathway-variation associations persist after controls. [src: metabolic_capability_dependency; pathway_capability_dependency]
- Test whether openness predicts ecological effects only for particular gene-function classes, including PGP modules, by stratifying auxiliary fraction, Heap’s law alpha, pangenome fluidity, mobile/defense categories, and genome count. [src: pangenome_openness; pgp_pangenome_ecology]
- Reanalyze defense-system presence using PADLOC MacSyFinder-style multi-PFam and gene-order rules, including PF13250/DUF4041 plus PF13455 for SNIPE, then test whether syndrome and accessory-enrichment patterns persist after specificity-aware calls. [src: phage_defense_arsenal; snipe_defense_system]
- Apply geNomad or PHASTER to BERDL genomes and use scaffold sequences for base-pair-resolution distances to test whether the prophage–AMR association persists after dedicated prophage calls and separation of phage, plasmid, and ICE neighborhoods. [src: prophage_amr_comobilization]
- Classify the 11,792 phaC clusters after mapping eggNOG domain names to PF00561 and PF07167, then reconstruct a phaC gene tree to test the 311 putative acquisitions and 278 losses. [src: phb_granule_ecology]
- Build a plant-ecotype integration analysis with expanded phylogenetic-tree coverage, accessory-gene and gene-content trees, host-stratified models, and direct mobile-element annotations to test whether the five significant species generalize. [src: plant_microbiome_ecotypes]
- Extend the *Pseudomonas* analysis with KEGG aromatic-degradation modules and PGLS (phylogenetic generalized least squares) or phylogenetic logistic regression to test whether environment associations persist after ancestry control. [src: pseudomonas_carbon_ecology]
- Test the Web of Microbes hypothesis that E/(E+I) metabolic novelty associates with pangenome openness or accessory genes, using strain-resolved WoM records and species-matched pangenomes; separately test produced metabolites against Fitness Browser gene fitness. [src: webofmicrobes_explorer]
- Obtain a current GNPS2 or Northen laboratory WoM release, add consumption actions, and test whether consumed metabolites predict gene essentiality and pathway capability. [src: webofmicrobes_explorer]
- Validate T4SS–CAZy proximity with the pending synteny-threshold permutation test, BLAST Node_4915 against NCBI nr, and a housekeeping-gene null baseline; then factorize biome enrichment using θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)]. [src: t4ss_cazy_environmental_hgt]
- Test whether GT2–T4SS neighborhoods, IMEs, MGE density, and metal-resistance genes co-occur after controlling for genome quality, contig length, biome, and taxonomic structure, and determine whether transfer is chromosomal, integrative, or plasmid-associated. [src: t4ss_cazy_environmental_hgt]
- Build a live-catalog resolver that records dotted and underscore namespaces, tenant, dataset, schema version, and access outcome before every cross-tenant join. [src: pitfalls]
- Recompute strain and species bridges with genus checks, NCBI-taxid-backed synonymy, GTDB-version-aware reconciliation, and assembly-accession joins; quantify how many existing ecological and fitness associations change. [src: pitfalls]
- Benchmark Spark-side aggregation and key-filtered joins for billion-row pangenome tables, retaining only small final outputs and documenting schema/type checks, broadcast behavior, and checkpoint provenance. [src: pitfalls]

See the source reports: [[summaries/acinetobacter_adp1_explorer__REPORT]], [[summaries/alphafold_msa_annotation__REPORT]], [[summaries/amr_environmental_resistome__REPORT]], [[summaries/amr_fitness_cost__REPORT]], [[summaries/amr_pangenome_atlas__REPORT]], [[summaries/annotation_gap_discovery__REPORT]], [[summaries/bacdive_metal_validation__REPORT]], [[summaries/bacdive_phenotype_metal_tolerance__REPORT]], [[summaries/berdl_data_atlas__REPORT]], [[summaries/ecotype_analysis__REPORT]], [[summaries/ecotype_env_reanalysis__REPORT]], [[summaries/enigma_carbon_census_1__REPORT]], [[summaries/enigma_contamination_functional_potential__REPORT]], [[summaries/essential_genome__REPORT]], [[summaries/field_vs_lab_fitness__REPORT]], [[summaries/conservation_vs_fitness__REPORT]], [[summaries/conservation_fitness_synthesis__REPORT]], [[summaries/fitness_effects_conservation__REPORT]], [[summaries/fitness_modules__REPORT]], [[summaries/functional_dark_matter__REPORT]], [[summaries/gene_function_ecological_agora__REPORT]], [[summaries/lanthanide_methylotrophy_atlas__REPORT]], [[summaries/metabolic_capability_dependency__REPORT]], [[summaries/metal_cross_resistance__REPORT]], [[summaries/metal_fitness_atlas__REPORT]], [[summaries/module_conservation__REPORT]], [[summaries/pangenome_openness__REPORT]], [[summaries/pathway_capability_dependency__REPORT]], [[summaries/pgp_pangenome_ecology__REPORT]], [[summaries/phage_defense_arsenal__REPORT]], [[summaries/phb_granule_ecology__REPORT]], [[summaries/plant_microbiome_ecotypes__REPORT]], [[summaries/prophage_amr_comobilization__REPORT]], [[summaries/pitfalls]], [[summaries/pseudomonas_carbon_ecology__REPORT]], [[summaries/snipe_defense_system__REPORT]], [[summaries/t4ss_cazy_environmental_hgt__REPORT]], [[summaries/truly_dark_genes__REPORT]], and [[summaries/webofmicrobes_explorer__REPORT]].

## [[concepts/pangenome-openness-determinants|Metabolic and Sampling Determinants of Pangenome Openness]]

- Recalculate openness, variable-pathway content, and pathway completeness across the full 27,690-species catalog using coverage-aware regression and explicit genome-count adjustment; test whether the metabolic association remains when the 1,872-species AlphaEarth subset is expanded or weighted for sampling coverage. [src: discoveries]
- Repeat the environment-versus-phylogeny comparison with the same species set, predictor definitions, and covariate structure used in the variable-pathway analysis; test whether the null correlations rho=-0.05 and rho=0.03 persist under harmonized modeling. [src: discoveries]
- Model AlphaEarth missingness and coordinate crowding explicitly, including the 3,838 genomes with NaN dimensions and the 36.6% of genomes in densely shared coordinates; test whether pathway-completeness associations survive inverse-coverage weighting or leave-one-coordinate-out validation. [src: discoveries]
- Partition variable metabolic pathways into core metabolic, secondary metabolic, and transport categories using pathway-level annotations; test which categories account for the partial rho=0.530 association with openness. [src: discoveries]
- Compare species-level openness with independent sampling-depth measures and geographic-range estimates; test whether the correlations for niche breadth, embedding variance, and geographic range reflect biological ecological breadth or uneven genome and environment sampling. [src: discoveries]

## [[concepts/pathway-versus-reaction-evidence-resolution|Pathway-Level Evidence Does Not Map Directly to Reaction-Level Gene Assignments]]

- Reprocess the 104 GapMind–gapfill pathway pairings against step-level GapMind outputs and ask how many pathway-level concordances become exact reaction-level matches. [src: annotation_gap_discovery]
- Integrate GapMind step identities with the 201 gapfilled enzymatic reaction–organism pairs, pangenome clusters, and BLAST candidates, then test whether step-level evidence increases the 96 (47.8%) resolved-pair count without increasing unsupported assignments. [src: annotation_gap_discovery]
- Stratify the 105 (52.2%) unresolved pairs by GapMind coverage and EC-number status, using contingency or regression analysis to ask whether missing pathway coverage or EC-less reactions explains more of the unresolved set. [src: annotation_gap_discovery]
- Apply alternative gapfilling solutions to the 38 false-negative cases and compare their reaction sets with GapMind step deficits, asking whether non-uniqueness is responsible for pathway–reaction discordance. [src: annotation_gap_discovery]
- Experimentally test high-confidence reaction–gene candidates with targeted gene knockout or CRISPRi and compare the results with pathway-level GapMind predictions, asking whether pathway agreement predicts reaction-specific fitness effects. [src: annotation_gap_discovery]

## [[concepts/perturbation-modality-dependent-phenotypic-architecture|Genetic deletions and chemical perturbations may expose different phenotype architectures]]

- Compare matched ADP1 single-gene deletions and chemical perturbations across the same 8 carbon sources, using identical growth measurements and hierarchical clustering, to test whether chemical perturbations produce more discrete modules than the deletion collection. [src: adp1_deletion_phenotypes]
- Repeat the comparison across an expanded condition panel and apply independent component analysis, asking whether the approximately 5 dimensions inferred from the current matrix remain stable or increase with broader environmental coverage. [src: adp1_deletion_phenotypes]
- Integrate deletion phenotypes with RB-TnSeq, or random barcode transposon sequencing, measurements under matched conditions and compare condition-specificity scores, to test whether perturbation modality changes the apparent continuity of fitness effects. [src: adp1_deletion_phenotypes]
- Reanalyze the ADP1 deletion matrix with replicate-aware error models and FDR-controlled module detection, asking whether the 24-gene quinate module remains discrete after technical noise is modeled. [src: adp1_deletion_phenotypes]
- Compare ADP1 and *E. coli* using matched perturbation types, condition panels, and clustering metrics, asking whether organismal metabolic interconnectedness or perturbation modality better explains the difference between continuous and discrete architectures. [src: adp1_deletion_phenotypes]

## [[concepts/phage-defense-syndromes-and-arms-race|Defense-system syndromes and prophage-associated anti-phage arms races]]

- Apply PADLOC MacSyFinder-style multi-PFam and gene-order rules to Retron, DISARM, and Gabija, and test whether the R-M Type II × Gabija association remains at 2,429 observed co-occurrences versus a null mean of 1,555 after marker refinement. [src: phage_defense_arsenal]
- Expand the panel beyond seven systems to include Zorya, Thoeris, Wadjet, Druantia, pAgo, PARIS, ThsA-ThsB, and defense-associated antitoxin cassettes, then ask whether the 27-of-28 positive-pair pattern persists. [src: phage_defense_arsenal]
- Fit a GTDB-tree phylogenetic mixed-effects arms-race model using defense count, `n_prophage_clusters`, genome size, and phylum, and test whether the residual association remains after explicit phylogenetic correction. [src: phage_defense_arsenal]
- Apply geNomad or PHASTER to BERDL genomes and use scaffold sequences for base-pair-resolution distances, then test whether the species-level AMR breadth association persists after separating phage, plasmid, and ICE mobilization. [src: prophage_amr_comobilization]
- Re-call prophages with dedicated tools and test whether the environmental enrichment of tail, head morphogenesis, and anti-defense remains after excluding bacterial homologs and domesticated remnants. [src: prophage_ecology]
- Use sequence-resolved genomes and the 6,365-sample NMDC bridge to test whether pH-associated prophage burden reflects intact prophage abundance, genus-level inference, or pH-linked community composition. [src: prophage_ecology]
- Perform mechanistic phage-challenge experiments comparing R-M Type II-only species with R-M Type II-plus-Gabija species, and ask whether the predicted syndrome provides additional protection against the same phage challenges. [src: phage_defense_arsenal]
- Cross-reference defense syndromes and prophage burden with NCBI isolation-source metadata or AlphaEarth embeddings to test whether habitat-specific defense architectures explain variation not captured by phylum. [src: phage_defense_arsenal]
- Revisit prophage-proximal AMR fitness costs as fitness-browser coverage expands, including all available genomes from Klebsiella pneumoniae, Acinetobacter baumannii, Pseudomonas aeruginosa, and Escherichia coli. [src: prophage_amr_comobilization]
- Use PF13250/DUF4041 plus PF13455 gene-order and sequence-profile rules to distinguish complete SNIPE architectures from divergent or non-SNIPE DUF4041 proteins, then test whether SNIPE prevalence and accessory status remain at 4,572 clusters and 86.7% accessory-or-singleton after refinement. [src: snipe_defense_system]
- Generate ManYZ and SNIPE mutant fitness and phage-challenge measurements in *Klebsiella* and other phage-therapy targets, testing whether transporter preservation produces the predicted resistance-versus-metabolic-cost trade-off. [src: snipe_defense_system]

## [[concepts/phage-therapy-evidence-translation|Translating Phage Host-Range Evidence into Patient-Specific Therapy]]

- Match the five-phage and eight-phage designs against raw UC Davis isolates using adsorption, killing-curve, resistance-frequency, burst-size, and titer assays to determine patient-isolate coverage rather than extrapolating from the 188-strain PhageFoundry panel. [src: ibd_phage_targeting]
- Query INPHARED and IMG/VR for Hungatella hathewayi, Flavonifractor plautii, and Mediterraneibacter gnavus, then validate candidate host assignments and lytic activity experimentally to resolve the three gut-anaerobe coverage gaps. [src: ibd_phage_targeting]
- Add AIEC strain diagnostics and pks, Yersiniabactin, Enterobactin, and other strain-level markers to patient-matched susceptibility models to test whether phylogroup and virulence-gene status improve Escherichia coli cocktail selection. [src: ibd_phage_targeting]
- Prospectively follow patients every 3–6 months with metagenomics, qPCR, ecotype reassignment, bile-acid measurements, and phage-resistance assays to test whether the proposed reassessment interval and five-fold Mediterraneibacter gnavus trigger predict clinically relevant state transitions. [src: ibd_phage_targeting]
- Perform controlled longitudinal phage or hybrid-intervention studies with target abundance, metabolomics, resistance, and clinical outcomes to distinguish phage-mediated causality from the modest endogenous-phage associations observed in HMP2. [src: ibd_phage_targeting]
- Compare direct phage targeting, GAG-degrading enzyme inhibitors, bile-acid co-therapy, and engineered-phage approaches in patient-derived communities to determine whether hybrid treatment can address phage gaps without worsening bile-acid coupling costs. [src: ibd_phage_targeting]

## [[concepts/phased-envelope-stress-regulation|Phased regulatory programs coordinate envelope stress responses]]

- Perform SigU-induction RNA-seq during the relevant envelope-stress transition and test whether SigU-dependent expression explains the 49-gene late-consequence cohort. [src: caulobacter_fur_lipida_loss]
- Repeat time-resolved transcriptomics with replicated samples and ChvI/SigU perturbations to determine whether the 20 early-only, 10 both-phases, and 49 late-consequence genes follow a reproducible sequence. [src: caulobacter_fur_lipida_loss]
- Add replicated RB-TnSeq under bipyridyl chelation, ferric supplementation, and hemin to test whether the Fur-linked phases require iron-axis conditions absent from the existing 198-experiment compendium. [src: caulobacter_fur_lipida_loss]
- Combine replicated outer-membrane proteomics with lipidomics and targeted Pal-Tol assays to test whether the late cohort directly drives outer-envelope lipid remodeling after lipid A loss. [src: caulobacter_fur_lipida_loss]
- Genetically perturb ChvI, SigU, Pal, and representative late TBDTs in the Δ*fur* Δ*sspB* Δ*lpxc* background to determine which phase components are required for rescue rather than merely induced. [src: caulobacter_fur_lipida_loss]

## [[concepts/phb-granule-ecology|Polyhydroxybutyrate pathway ecology, genome size, and horizontal transfer]]

- Reconstruct a directly aligned phaC gene tree and test gene-tree/species-tree incongruence to distinguish horizontal acquisition from lineage sorting or annotation error. [src: phb_granule_ecology]
- Apply phylogenetic logistic regression or phylogenetic independent contrasts to the 27,690-species pangenome table to test whether environmental variability predicts phaC presence after shared ancestry and genome size are controlled. [src: phb_granule_ecology]
- Map PF00561 to Abhydrolase_1 and PF07167 to PhaC_N, then classify the 11,792 phaC clusters by PHA synthase class to test whether ecological distributions differ among synthase classes. [src: phb_granule_ecology]
- Combine repeated environmental measurements with NMDC taxonomic abundances and PHB inference scores to test temporal variability directly rather than using point-in-time abiotic measurements. [src: phb_granule_ecology]
- Reanalyze the AlphaEarth association after expanding embedding coverage beyond 83K/293K genomes and testing lineage-balanced sampling, asking whether the partial rho = -0.047 association is reproducible across underrepresented clades. [src: phb_granule_ecology]
- Use genome-quality filtering and independent pathway evidence to test whether the 46.5% precursors-only category reflects genuine partial PHB capability or pleiotropic phaA/phaB metabolism. [src: phb_granule_ecology]

## [[concepts/phenotype-database-coverage-bias|Coverage and Study Bias in Microbial Phenotype Databases]]

- Apply GCA accession matching to the BacDive and GTDB records, then quantify whether recovered species alter feature-level coverage and the estimated phenotype–metal-score associations. [src: bacdive_phenotype_metal_tolerance]
- Use PGLS (phylogenetic generalized least squares) or phylogenetic PCA on the matched 3,994-species set to test whether Gram stain, urease, catalase, and other phenotype associations persist after explicit removal of phylogenetic signal. [src: bacdive_phenotype_metal_tolerance]
- Reweight or stratify analyses by phenotype-test coverage and taxonomic representation, then test whether the model rankings and exact effect estimates change when well-studied lineages are prevented from dominating the comparison. [src: bacdive_phenotype_metal_tolerance]
- Add BacDive machine-learning-predicted phenotypes and compare their associations with experimentally recorded phenotypes to determine whether expanded coverage introduces model-dependent bias. [src: bacdive_phenotype_metal_tolerance]
- Assemble urease-positive and urease-negative organisms from the same taxonomic class and test them with RB-TnSeq (random barcode transposon sequencing) under nickel and other metals to distinguish nickel-specific effects from general tolerance. [src: bacdive_phenotype_metal_tolerance]
- Expand direct validation across Gram-positive and Gram-negative organisms, multiple oxygen-tolerance states, and balanced metal panels to determine whether the database associations reproduce in measured metal-tolerance phenotypes. [src: bacdive_phenotype_metal_tolerance]

## [[concepts/phylogenetic-confounding-of-pangenome-associations|Phylogenetic Confounding of Pangenome Associations]]

- Use the existing species-level openness, AMR-count, and taxonomic data with phylogenetic generalized least squares (PGLS), a regression method that models covariance among related species, to test whether the openness–AMR association remains after accounting for shared ancestry. [src: amr_pangenome_atlas]
- Combine the pangenome species table with a species phylogeny and fit within-phylum hierarchical models to ask whether the positive associations in 8/10 phyla share a common slope or instead arise from lineage-specific processes. [src: amr_pangenome_atlas]
- Reanalyze the six-category environmental comparison using taxonomic matching or lineage-stratified permutation tests to determine whether the clinical, soil, plant, aquatic, and animal contrasts persist after controlling for uneven taxonomic sampling. [src: amr_pangenome_atlas]
- Add environmental metadata and AlphaEarth embeddings for the currently under-covered genomes, then use phylogeny-aware partial association analyses to test whether environmental diversity predicts AMR count independently of lineage. [src: amr_pangenome_atlas]
- Estimate AMR gene gain and loss rates on a dated or calibrated species phylogeny, and test whether pangenome openness predicts transition rates rather than only present-day AMR counts. [src: amr_pangenome_atlas]

## [[concepts/phenotype-database-coverage-bias|Phylogenetic Confounding of Microbial Phenotype Associations]]

- Match BacDive records to GTDB species using GCA accessions, then repeat the species-level association and test whether the Gram-stain, urease, and catalase effects change after expanded coverage. [src: bacdive_phenotype_metal_tolerance]
- Apply PGLS, meaning phylogenetic generalized least squares, or phylogenetic PCA to the matched phenotype and metal-score data, and ask whether any phenotype retains an association after phylogenetic signal is removed. [src: bacdive_phenotype_metal_tolerance]
- Replace the composite Metal Fitness Atlas score with per-metal scores and use within-class regression to test whether catalase predicts copper tolerance, urease predicts nickel tolerance, and H₂S predicts zinc, copper, or cadmium tolerance. [src: bacdive_phenotype_metal_tolerance]
- Assemble urease-positive and urease-negative organisms from the same taxonomic classes and test them under nickel and other metals with RB-TnSeq, meaning random barcode transposon sequencing, to distinguish nickel-specific effects from general lineage differences. [src: bacdive_phenotype_metal_tolerance]
- Expand the direct Fitness Browser–BacDive validation with Gram-positive organisms, urease-positive organisms, and multiple anaerobes, then test whether phenotype associations replicate in directly measured metal-fitness data rather than genome-based scores. [src: bacdive_phenotype_metal_tolerance]

## [[concepts/environmental-resistome|Phylogenetic Structure of Within-Species Resistomes]]

- Subsample species with more than 500 genomes and repeat ANI extraction and Mantel testing to determine whether the 55.6% significant-species estimate changes when mega-species are included. [src: amr_strain_variation]
- Combine phylogeny-aware models with AMR presence/absence matrices to test whether non-core AMR associations persist after separating lineage inheritance from repeated acquisition and loss. [src: amr_strain_variation]
- Map resistance-island genes to plasmids, chromosomes, integron boundaries, and insertion sequences, then test whether genomic context explains the observed median Mantel correlations of 0.222 for non-core genes and 0.117 for core genes. [src: amr_strain_variation]
- Reanalyze AMR phylogenetic structure using curated environmental and collection-date metadata to test whether lineage effects differ between clinical, host-associated, terrestrial, and aquatic sampling contexts. [src: amr_strain_variation]
- Compare AMR phylogenetic structure with virulence-factor profiles and metabolic pathway variation to test whether AMR-defined lineages are broader genomic ecotypes. [src: amr_strain_variation]

[[summaries/amr_strain_variation__REPORT]]

## [[concepts/evidence-triangulation-for-functional-annotation|Functional Annotation Inference Varies Across Phylogenetic Contexts]]

- Reanalyze the full 48 Fitness Browser organisms with the same evidence pipeline, stratifying resolution by phylogenetic clade and asking whether the low resolution observed for *B. thetaiotaomicron* persists beyond the 14-organism, Proteobacteria-biased dataset. [src: annotation_gap_discovery]
- Reconstruct the models with gapseq and compare false-positive FBA rates and annotation-gap resolution against the default ModelSEED gapfilling results, asking how much apparent context dependence is caused by model construction. [src: annotation_gap_discovery]
- Experimentally validate the 44 high-confidence assignments, prioritizing rxn02185 and rxn03436 across 9 organisms, using targeted gene knockout or CRISPRi and asking whether transferability predicts cross-organism phenotype confirmation. [src: annotation_gap_discovery]
- Characterize the 50 EC-less reactions with sequence, structure, pathway, and phenotype evidence, asking whether improved reaction-level representation raises the 16% resolution rate for dark reactions. [src: annotation_gap_discovery]
- Compare organisms with matched numbers of carbon-source experiments and matched annotation quality, using the existing fitness and pangenome records to ask whether resolution differences remain after data-coverage effects are controlled. [src: annotation_gap_discovery]

See the source summary: [[summaries/annotation_gap_discovery__REPORT]].

## [[concepts/planktonic-to-biofilm-translation|Planktonic Competition Assays Do Not Directly Establish Biofilm Protection in Cystic-Fibrosis Airways]]

- Test the proposed k=2 and k=3 formulations in mixed-species biofilm models using PA14, PAO1, and 3–5 mucoid clinical PA isolates to determine whether planktonic inhibition predicts biofilm biomass reduction or PA exclusion. [src: cf_formulation_design]
- Expand carbon and airway-medium assays to include mucins, lipids, iron, polyamines, xylitol, myoinositol, xylose, and arabinose, then measure whether the predicted commensal-to-PA growth advantages persist under biofilm conditions. [src: cf_formulation_design]
- Measure the complete 10-pair interaction matrix for the five-species core in spatially structured co-cultures to test whether the provisional pairwise synergy estimates generalize to the full formulation. [src: cf_formulation_design]
- Track formulation species by strain-resolved metagenomics and metatranscriptomics during biofilm growth or an airway-relevant model to test whether inferred engraftability predicts actual establishment and activity. [src: cf_formulation_design]
- Compare planktonic and biofilm phenotypes across the 22-substrate panel and the genomically nominated sugar alcohols and pentoses to quantify which condition-specific fitness measurements transfer between assay formats. [src: cf_formulation_design]

## [[concepts/pooled-run-pseudoreplication-and-metadata-label-noise|Pooled sequencing runs complicate the statistical unit and metadata assignment]]

- Recover the complete set of biosamples and their contribution weights for the 1,067 pooled runs, then fit weighted or hierarchical models to test whether representative-biosample assignment changes effect estimates. [src: euk_in_prok_correlates]
- Compare `MIN(biosample_id)` labels with alternative pooled labels, such as majority environment or contribution-weighted environment, and quantify how much metadata-label noise changes association strength. [src: euk_in_prok_correlates]
- Reanalyze the eukaryotic-fraction models at the run level with cluster-robust or hierarchical uncertainty, using pooling structure as a grouping variable, to determine whether conclusions remain stable without biosample pseudo-replication. [src: euk_in_prok_correlates]
- Validate the run-to-biosample-to-study joins against explicit parent-child key audits and unresolved-record counts, asking whether the reported 99%+ linkage rate hides systematic failures among pooled or unusually structured records. [src: euk_in_prok_correlates]

## [[concepts/potential-versus-realized-data-integration|Potential Data Connectivity Often Exceeds Realized Cross-Dataset Use]]

- Execute UC2 on ENIGMA and PhageFoundry tables using its 11 shared keys, then test whether subsurface prophage, metal-resistance, and Oak Ridge contamination-gradient records overlap in value space. [src: berdl_data_atlas]
- Execute UC3 between KBase and refdata using its 11 shared keys, then quantify GTDB versus KBase species-pangenome disagreement after identifier harmonization. [src: berdl_data_atlas]
- Execute UC4 between NMDC and PROTECT using its 10 shared keys, combining environmental distribution records with pathogen and biogeochemical data to test whether clinically relevant pathogen signals are geographically and environmentally recoverable. [src: berdl_data_atlas]
- Execute UC5 between NMDC and refdata using its 9 shared keys, then measure ENVO ontology completeness in NMDC biosamples and assess whether missing annotations are recoverable from reference resources. [src: berdl_data_atlas]
- Re-audit project notebooks and research plans in addition to README files, then compare the expanded realized-use count with the current lower-bound estimate of 51 of 66 multi-tenant projects. [src: berdl_data_atlas]
- Add or compute per-residue pLDDT and structural features for the validated UC1 cohort, then test whether structure-derived variables explain condition-specific fitness patterns beyond the existing gene-level join. [src: berdl_data_atlas]

## [[concepts/prevalence-ceiling-in-pangenome-associations|Prevalence ceilings limit detection and interpretation of pangenome co-occurrence]]

- Use the existing pangenome presence matrices to restrict both members of each pair to clusters below 95% prevalence, then test whether the cofit-versus-random delta phi increases and whether the organism-level heterogeneity persists. [src: cofitness_coinheritance]
- Recompute co-fitness from raw genefitness data for Ralstonia UW163 and Ralstonia GMI1000, then repeat prevalence-matched association tests to determine whether their exclusion removed informative low-ANI diversity. [src: cofitness_coinheritance]
- Combine prevalence-stratified phi estimates with reference-resolved phylogenetic distances, then test whether co-fitness predicts co-occurrence after separately controlling for prevalence and shared ancestry. [src: cofitness_coinheritance]
- Build module co-transfer networks from the ICA modules and test whether cross-module prediction remains detectable after matching module prevalence and auxiliary content. [src: cofitness_coinheritance]
- Expand the analysis to species with >30% auxiliary genes and existing co-fitness data, then measure whether increased accessory variation improves pairwise and module-level detection. [src: cofitness_coinheritance]

## [[concepts/fitness-module-detection-sensitivity|Process-Level Context Does Not Establish Gene-Level Function]]

- Combine the 6,691 hypothetical-protein predictions with ortholog transfer, domain architectures, and targeted gene-level experiments to test which module-only predictions acquire specific molecular-function support. [src: fitness_modules]
- Reanalyze the held-out benchmark with process-level gold standards in addition to KEGG KO labels to ask whether Module-ICA has useful precision when evaluated against biological-process membership rather than gene-level identity. [src: fitness_modules]
- Use larger, condition-diverse RB-TnSeq datasets and compare module stability before and after the 40% component cap to determine which conserved modules are missed in organisms with fewer experiments. [src: fitness_modules]
- Test the 156 cross-organism module families with gene-neighborhood, domain-combination, and experimental perturbation data to determine whether shared module membership reflects conserved regulation, conserved pathway involvement, or recurrent genomic organization. [src: fitness_modules]

## [[concepts/provenance-aware-resource-discovery|Provenance, scale, and currency must be exposed during resource discovery]]

- Compare `nmdc.metadata` and `nmdc.ncbi_biosamples` with live upstream record counts using external API calls, and ask how much completeness lag each resource has. [src: nmdc_context_audit]
- Add provenance, authority, tenant, object-count, and `max(committed_at)` fields to inventory output, then test whether users can identify the appropriate NMDC-related resource without opening separate documentation. [src: nmdc_context_audit]
- De-duplicate dotted and underscore database aliases before inventory iteration, then verify whether reported resource counts and cross-tenant links become consistent. [src: nmdc_context_audit]
- Apply the proposed documentation and tooling fixes and measure subsequent NMDC project resource selection time and reuse patterns to test whether better context reduces selection errors. [src: nmdc_context_audit]
- Extend the provenance-audit method to other overloaded BERDL labels and ask whether the same combination of name collisions, tenant separation, scale traps, and hidden currency recurs. [src: nmdc_context_audit]
- Join the 129,823 PaperBLAST–Fitness Browser cross-references to resource cards, then test whether exposing source, text-mining coverage, and phenotype linkage changes selection of literature-to-fitness resources. [src: paperblast_explorer]
- Compare PaperBLAST’s PMC-derived coverage with curatedgene, GeneRIF, and SwissProt-only annotations to quantify which missing-literature patterns reflect access limitations versus genuinely unstudied proteins. [src: paperblast_explorer]
- Build live resource cards that record dotted and fallback namespace, tenant, access surface, schema-discovery time, row/object counts, and `max(committed_at)`, then test whether the cards prevent duplicate aliases and invalid historical references. [src: pitfalls]
- Evaluate identifier bridges using genus consistency and assembly-accession checks, and quantify how many cross-resource links remain valid after synonymy and taxonomy-version reconciliation. [src: pitfalls]
- Re-run the soil-frontier analysis with spatial blocking and leverage diagnostics to decompose negative out-of-sample R² into distributional shift, outliers, and true unpredictability; report rarefaction-corrected GDI, biome bootstrap 95% CIs, and 16S-sample-adjusted pH-bin comparisons to distinguish sampling gaps from completeness or assembly gaps. [src: soil_frontier_genomics]
- Re-ingest the current WoM or Northen laboratory dataset, record its snapshot and access path, and test whether consumption actions are present and whether the 2018 production-only patterns persist. [src: webofmicrobes_explorer]
- Add curated WoM compound-to-ModelSEED and GapMind pathway-to-metabolite bridges, preserving exact versus formula-only confidence, then test whether metabolite-production links support reproducible gene-fitness analyses. [src: webofmicrobes_explorer]

## [[concepts/relative-fitness-and-transposon-interpretation|Interpreting relative fitness costs from transposon perturbation data]]

- Use isogenic strains with direct growth-rate or competition assays to test whether the **+0.086** knockout-class contrast corresponds to an absolute cost of intact AMR genes rather than only a relative perturbation shift. [src: amr_fitness_cost]
- Reanalyze the **801** non-antibiotic per-gene fitness records with matched metal, osmotic, and carbon-limitation conditions to ask whether the baseline contrast changes across stress environments. [src: amr_fitness_cost]
- Model insertion position and operon context, using gene-neighborhood information to test how much of the measured AMR phenotype could arise from polar effects on downstream genes. [src: amr_fitness_cost]
- Incorporate the approximately **4.6%** putatively essential AMR genes through targeted essentiality assays or alternative perturbations to test whether their exclusion makes **+0.086** a lower bound. [src: amr_fitness_cost]
- Subclassify efflux systems and compare broad-spectrum RND systems with narrow-spectrum pumps using condition-matched antibiotic fitness data to test whether breadth predicts antibiotic-dependent importance. [src: amr_fitness_cost]

## [[concepts/research-attention-inequality|Research-Attention Inequality and Functional Darkness]]

- Compare PaperBLAST coverage with the full SwissProt and curated annotation sets using capture–recapture or stratified coverage analysis to test how many apparently dark families are dark because of missing PMC linkage rather than absent functional knowledge. [src: paperblast_explorer]
- Recompute organism- and gene-level Lorenz curves after formal taxonomy normalization and stratification by domain, pathogen status, and environmental origin to test whether the measured inequality is driven by classification uncertainty or research selection. [src: paperblast_explorer]
- Use MMseqs2 clusters at multiple identity thresholds and compare them with curated functional annotations to test whether the 5,218 literature-free multi-member families remain dark under alternative family definitions. [src: paperblast_explorer]
- Link the 129,823 VIMSS cross-references to Fitness Browser phenotypes and prioritize dark families with experimental fitness evidence for targeted functional characterization. [src: paperblast_explorer]
- Sample full-text and paywalled literature outside PubMed Central, then estimate false-negative rates for text-mined gene–paper links to quantify how much open-access availability contributes to the observed attention inequality. [src: paperblast_explorer]

## [[concepts/research-use-observability-bias|Project Documentation Makes Reported Data Reuse a Lower Bound]]

- Combine README files, research plans, notebook source, and query logs, then ask how many additional project–tenant and project–bridge uses are recovered beyond the documented baseline of 51 of 66 multi-tenant projects. [src: berdl_data_atlas]
- Execute UC2–UC5 on the live cluster and compare validated value-space overlap with the README-derived finding of zero realized use, asking whether the bridges are unused, undocumented, or merely unvalidated. [src: berdl_data_atlas]
- Build a provenance-aware project–dataset graph from project artifacts and deduplicate records by project, tenant, dataset, and canonical join key, asking whether tenant-use rankings change from the README audit. [src: berdl_data_atlas]
- Audit notebook and query artifacts for the 36 documented kbase × kescience projects, asking whether their pangenome-by-fitness joins are reproducible and whether additional join keys beyond genome_id and ncbi_taxon_id were used. [src: berdl_data_atlas]

## [[concepts/antimicrobial-resistance-fitness-cost|Compensation and the hidden cost of antimicrobial resistance]]

- Use matched genomes from the **25** lab-adapted organisms, comparative genomics, and fitness association analysis to ask whether specific compensatory mutations explain the residual **+0.086** AMR-versus-background shift. [src: amr_fitness_cost]
- Reconstruct newly acquired and compensated AMR genotypes in isogenic strains and measure growth and competition fitness to distinguish the original cost from the post-compensation cost. [src: amr_fitness_cost]
- Subclassify efflux genes into narrow-spectrum pumps and general RND systems such as AcrAB-TolC, then use condition-specific fitness assays to ask whether constitutive systems have lower baseline costs. [src: amr_fitness_cost]
- Cross-reference the **144** metal-resistance genes with the metal fitness atlas and test, using matched metal-stress fitness measurements, whether genes costly under standard conditions are protective under metal stress. [src: amr_fitness_cost]
- Expand GTDB sampling beyond the median of **9** genomes per Fitness Browser species and recompute the **≥95%** core/accessory labels to ask whether the core-versus-accessory cost null result persists with deeper pangenomes. [src: amr_fitness_cost]

## [[concepts/resistance-island-coinheritance|Resistance-Island Co-inheritance and Mechanistic Linkage]]

- Use the 1,517 island records together with genome assemblies and genomic-context mapping to plasmids, chromosomes, integron boundaries, and insertion sequences; determine which islands are physically linked and which are lineage-level co-occurrence patterns. [src: amr_strain_variation]
- Combine island membership with curated exposure metadata and phylogeny-aware models; test whether multi-mechanism islands are co-selected under shared antimicrobial environments rather than merely inherited together. [src: amr_strain_variation]
- Integrate resistance-island genes with virulence-factor profiles and metabolic pathway variation; test whether island composition predicts host-associated phenotypes or fitness beyond lineage background. [src: amr_strain_variation]
- Apply perturbation or competition experiments to representative multi-mechanism islands; test whether linked resistance genes produce additive, synergistic, or independent protection across drug classes. [src: amr_strain_variation]
- Use the reported phi coefficients with fitness and genomic-context data in predictive models; test whether high co-inheritance predicts future AMR gene co-acquisition. [src: amr_strain_variation]

## [[concepts/environmental-resistome|Resistome conclusions depend on gene-catalog scope and mechanism classification]]

- Map the 83,008 AMRFinderPlus hits to CARD ARO terms and compare mechanism counts, core fractions, and environmental contrasts with the keyword-based classification to determine how much of the 18,448-hit Other/Unclassified category is reclassified. [src: amr_pangenome_atlas]
- Separate classical antibiotic-resistance genes from mercury-, arsenic-, and other stress-response genes, then repeat the 30.3% versus 46.8% core comparison and the 2.2x auxiliary-genome enrichment test to quantify the effect of catalog scope. [src: amr_pangenome_atlas]
- Reanalyze AMR functional enrichment using the 77K AMR clusters and 86M-cluster baseline after stratifying by mechanism and catalog class, asking whether the 7.05x COG V and 1.93x COG P enrichments persist for antibiotic-only genes. [src: amr_pangenome_atlas]
- Validate singleton AMR clusters with broader homology, domain, and synteny analyses, asking whether the 55.4% singleton rate among sparsely annotated one-source clusters represents annotation artifacts or genuine species-specific resistance. [src: amr_pangenome_atlas]
- Compare the catalog-defined environmental gradients against AMR calls in NMDC and MGnify metagenomes, using CARD ARO harmonization and metadata-stratified models to test whether clinical, soil, aquatic, and plant differences persist under comparable sampling and classification. [src: amr_pangenome_atlas]

## [[concepts/respiratory-capacity-and-nadh-load|Respiratory-chain dependence tracks reducing-equivalent load rather than substrate identity]]

- Measure Complex I and NDH-2 deletion fitness in ADP1 on quinate, acetate, succinate, glucose, and lactate, using matched growth assays to ask whether fitness loss follows NADH-generating load rather than aromatic substrate identity. [src: aromatic_catabolism_network]
- Search the ADP1 genome for NDH-2 and test the deletion on quinate versus glucose to determine whether an alternative NADH dehydrogenase explains the reported dispensability pattern. [src: aromatic_catabolism_network]
- Expand the condition panel with benzoate, catechol, vanillate, iron limitation, and respiratory inhibitors, then recompute co-fitness and condition-specific fitness to separate aromatic chemistry, iron demand, and respiratory load. [src: aromatic_catabolism_network]
- Add PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints to the ADP1 FBA model, then compare predicted essentiality and flux with the observed defects in 10/13 Complex I operon subunits. [src: aromatic_catabolism_network]
- Compare Complex I retention and NDH-2 complements across aromatic-degrading species using pangenome data to test whether respiratory architecture predicts transferability of the NADH-load hypothesis. [src: aromatic_catabolism_network]

## [[concepts/shared-stress-versus-stressor-specific-fitness|Salt Chemistry Can Confound Fitness Assays Beyond the Intended Stressor]]

- Compare matched KCl and choline chloride controls with NaCl using RB-TnSeq to determine whether shared fitness signals track chloride, sodium, osmolarity, or the combined salt condition. [src: counter_ion_effects]
- Repeat CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ assays under identical aerobic conditions, metal concentrations, and media to isolate counter-ion effects from oxygen-regime confounding. [src: counter_ion_effects]
- Run DvH NaCl dose-response experiments at 0.1, 1, 10, 100, and 500 mM and compare gene-level profiles with metal dose responses to test whether correlation follows effective chloride exposure. [src: counter_ion_effects]
- Apply formal COG, KEGG, and PFAM enrichment tests to shared-stress and metal-specific gene sets to test the proposed cell-envelope, DNA-repair, and ion-homeostasis mechanisms. [src: counter_ion_effects]
- Use independent component analysis (ICA) and module-level comparisons to separate shared salt-stress programs from metal-specific fitness modules. [src: counter_ion_effects]
- Reanalyze metal fitness with condition-specific models and matched salt controls to determine which genes remain metal-associated after accounting for shared stress. [src: counter_ion_effects]

## [[concepts/sample-size-aware-phenotype-consensus|Species-level utilization claims require sample-size-aware strain consensus]]

- Extend the FW300-N2E3 crosswalk to additional isolates, including *Pseudomonas stutzeri* RCH2, and test whether BacDive utilization rates are reproducible across isolates rather than driven by the current strain composition. [src: fw300_metabolic_consistency]
- Expand WoM–BacDive matching with InChIKey or CHEBI identifiers, then reassess whether the observed 8/58 BacDive coverage and 3/7 utilization rate change when nomenclature-based missed matches are reduced. [src: fw300_metabolic_consistency]
- Reanalyze BacDive records with explicit per-strain consensus and sample-size thresholds, asking which utilization claims remain stable after duplicate records and low-n comparisons are separated. [src: fw300_metabolic_consistency]
- Compare strain-resolved BacDive phenotypes with isolate-specific Fitness Browser and WoM data, asking whether species-level non-utilization predicts or obscures FW300-N2E3-specific growth and secretion. [src: fw300_metabolic_consistency]

## [[concepts/environment-embedding-geography|Sampling Composition Confounding of Environmental Signal]]

- Restrict the AlphaEarth dataset to environmental categories, recompute partial correlations between embedding similarity and gene-content similarity, and test whether the median partial correlation differs from 0.0025. [src: env_embedding_explorer]
- Reweight or downsample Human clinical, Human gut, Human other, Soil, Marine, Freshwater, Extreme, and Plant categories, then repeat the geographic-distance analysis to test whether the reported 0.41-to-0.82 distance pattern changes with composition. [src: env_embedding_explorer]
- Compare keyword-based isolation_source categories with env_broad_scale for the 42% of genomes covered by the structured field, and test whether environment–gene-content associations are stable across classification schemes. [src: env_embedding_explorer]
- Use isolation_source homogeneity together with coordinate clustering to distinguish institutional addresses from legitimate field sites, then recompute embedding distance–geography relationships under each coordinate-quality definition. [src: env_embedding_explorer]
- Fit phylogeny-aware models to environmental-only samples and test whether similar AlphaEarth embeddings predict greater accessory-gene sharing after controlling for taxonomic relatedness. [src: env_embedding_explorer]

## [[concepts/sampling-depth-and-downsampling-effects|Sampling Depth and Downsampling Effects]]

- Use the same species and genome universe to compare diversity-maximizing downsampling with full-genome extraction, then test whether sampling strategy or genome-set composition explains the partial-correlation discrepancy. [src: ecotype_env_reanalysis]
- Add genome count as a covariate to the species-level correlation model, then test whether unequal sampling depth inflates correlations in species with more genomes. [src: ecotype_env_reanalysis]
- Recompute correlations after matched-depth downsampling across species, then test whether the environmental-versus-human-associated comparison remains null when statistical power is balanced. [src: ecotype_env_reanalysis]
- Analyze functional gene subsets, including transport and secondary-metabolism categories, with identical downsampling and extraction settings, then test whether whole-genome Jaccard distances mask sampling-depth effects on specific functions. [src: ecotype_env_reanalysis]
- Reassess species with NaN correlations using alternative missing-data and minimum-sample thresholds, then test whether the higher Environmental NaN rate changes the group comparison. [src: ecotype_env_reanalysis]

## [[concepts/scale-dependent-mobile-element-associations|Scale-Dependent Mobile-Element Associations and Mobilization Inference]]

- Apply geNomad or PHASTER to BERDL genomes and compare dedicated prophage calls with keyword/Pfam calls to quantify false positives, missed divergent prophages, and the contribution of phage-defense systems to the observed associations. [src: prophage_amr_comobilization]
- Recompute AMR–prophage distances from scaffold sequences at base-pair resolution and test whether the threshold-dependent odds ratios persist when ordinal gene-position errors are removed. [src: prophage_amr_comobilization]
- Analyze all available genomes from Klebsiella pneumoniae, Acinetobacter baumannii, Pseudomonas aeruginosa, and Escherichia coli to determine whether the local and species-level associations are robust to the 20-genomes-per-species sampling design. [src: prophage_amr_comobilization]
- Partition prophage, plasmid, and integrative-conjugative-element signals and fit comparative models that test whether prophage density predicts AMR breadth independently of other mobile elements. [src: prophage_amr_comobilization]
- Revisit the fitness comparison as fitness-browser coverage expands, testing whether prophage-proximal and distal AMR genes differ in RB-TnSeq fitness effects. [src: prophage_amr_comobilization]

## [[concepts/potential-versus-realized-data-integration|Schema Compatibility Does Not Establish Valid Biological Joins]]

- Execute UC2 on the enigma and phagefoundry live-cluster tables, using the 11 candidate keys plus identifier and duplicate audits, to determine whether subsurface prophage, metal-resistance, and Oak Ridge contamination-gradient records share a valid biological value space. [src: berdl_data_atlas]
- Execute UC3 across kbase and refdata with genome and species-pangenome identifiers, using overlap, namespace, and representative-record checks, to test the proposed GTDB–KBase species-pangenome disagreement analysis. [src: berdl_data_atlas]
- Execute UC4 across nmdc and protect with sample, genome, and taxonomic validation, then cross-check environmental distributions against biogeochemical records, to determine whether clinically relevant pathogen observations can be joined without identifier conflation. [src: berdl_data_atlas]
- Execute UC5 across nmdc and refdata with ENVO ontology identifiers, measuring annotation coverage and semantic validity, to test whether NMDC biosample metadata support the proposed ontology-completeness analysis. [src: berdl_data_atlas]
- Extend the validated UC1 cohort with per-residue pLDDT and structural-feature data from PDB files, because kescience_alphafold.alphafold_entries lacks those fields, to test structure–fitness relationships after the identifier join has been validated. [src: berdl_data_atlas]

## [[concepts/selection-on-outcome-leakage|Selection-on-outcome leakage in microbiome and genomic inference]]

- Re-run the IBD ecotype analysis with held-out-species clustering and compare Tier-A membership, CLR-Δ estimates, and confidence intervals with the original 33-species list; determine which associations persist without direct feature reuse. [src: pitfalls]
- Apply leave-one-species-out refitting to every candidate rather than only *C. scindens*; quantify how often significance, effect direction, and ecotype-specific estimates change. [src: pitfalls]
- Cluster the same samples using pathways or EC numbers instead of taxa, then test taxon-level associations; determine whether a feature representation that is independent of the tested taxa reduces the leakage signal. [src: pitfalls]
- Combine the four IBD sub-studies with at least 10 CD and 10 nonIBD samples using within-substudy contrasts and inverse-variance meta-analysis; compare the resulting candidates with the ecotype-derived list. [src: pitfalls]
- Recalculate stability across the reported Jaccard values of 0.230 for E1 and 0.064 for E3 under alternative feature-holdout partitions; determine whether the observed instability is specific to the cited partitioning procedure. [src: pitfalls]

## [[concepts/shared-stress-versus-stressor-specific-fitness|Separating Shared Stress Responses from Stressor-Specific Fitness Requirements]]

- Compare matched choline chloride and NaCl datasets to ask whether the shared component follows chloride specifically or instead reflects sodium and osmotic stress; choline chloride would provide a more specific chloride control than NaCl. [src: counter_ion_effects]
- Perform formal COG, KEGG, and PFAM enrichment tests on shared-stress versus metal-specific genes to test whether cell-envelope, DNA-repair, and ion-homeostasis categories are genuinely overrepresented. [src: counter_ion_effects]
- Apply independent component analysis (ICA), a method that decomposes correlated measurements into latent components, to metal and NaCl fitness profiles to ask whether shared and stressor-specific axes can be separated at the module level. [src: counter_ion_effects]
- Run matched CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ RB-TnSeq experiments—random barcode transposon sequencing—under identical oxygen and culture conditions to test counter-ion effects without aerobic/anaerobic confounding. [src: counter_ion_effects]
- Generate DvH NaCl dose-response data at 0.1, 1, 10, 100, and 500 mM to match effective chloride doses and test whether the metal–NaCl correlation hierarchy changes with dose. [src: counter_ion_effects]
- Reanalyze the 10,821 metal-important records with stricter and more permissive NaCl-importance thresholds to quantify how much the estimated 39.8% shared-stress fraction depends on classification rules. [src: counter_ion_effects]

## [[concepts/spatial-sampling-effort-confounding|Spatial Sampling Effort and Geographic Hotspot Confounding]]

- Use the MAG coordinate table and ENA sample records to classify distinct `sample_accession` prefixes within each reported hotspot, then test whether hotspot significance persists after removing or stratifying dominant studies; this would address the report's single-study or expedition-level artefact concern. [src: metal_resistance_global_biogeography]
- Recompute the 5°-grid Fisher's exact tests after normalising or modelling sampling effort with **log(n_MAGs)**, and ask whether the **11** hotspots and **3** coldspots remain significant under the effort-adjusted analysis. [src: metal_resistance_global_biogeography]
- Combine MAG resistance status, biome labels, grid-cell counts, and coordinate completeness in a stratified or matched model, and ask whether the Atacama/Andean, USA, and East/Southeast Asia signals persist after controlling for biome composition. [src: metal_resistance_global_biogeography]
- Compare the **22,356** coordinate-bearing MAGs with the **30,497-MAG** filtered set by biome and sample source, and ask whether the **30.8%** per-sample coordinate gap disproportionately excludes particular environmental categories. [src: metal_resistance_global_biogeography]
- Repeat hotspot analysis using study-aware resampling across the **532** represented grid cells, and ask whether regional enrichment is reproducible when no single accession family or sampling campaign dominates a cell. [src: metal_resistance_global_biogeography]

## [[concepts/spatial-structure-versus-short-term-temporal-stability|Persistent spatial structure despite short-term groundwater community stability]]

- Load the 221 registered SSO geochemistry samples into CORAL and use spatial gradient analysis to test whether nitrate, pH, and metal concentrations follow the predicted northeast-to-southwest community pattern. [src: enigma_sso_asv_ecology]
- Add groundwater ASVs from the available Brick 460-462 pump-test data and compare M5, L8, and U2 with the existing wells to test whether the predicted *Rhodanobacter* maximum occurs at M5. [src: enigma_sso_asv_ecology]
- Repeat groundwater 16S sampling across seasons and apply variance partitioning to ask whether well identity continues to dominate date and seasonal effects. [src: enigma_sso_asv_ecology]
- Collect sediment and groundwater contemporaneously and use paired within-well Bray–Curtis comparisons to determine whether their separation reflects material-specific communities or the existing 18-month sampling offset. [src: enigma_sso_asv_ecology]
- Standardize filter size and apply PERMANOVA with filter, well, depth, and date terms to determine how much of the apparent spatial structure is attributable to sampling configuration. [src: enigma_sso_asv_ecology]
- Generate metagenomes at the same spatial resolution and compare functional genes with ASV-based assignments to test whether the persistent spatial pattern corresponds to measured metabolic capacity. [src: enigma_sso_asv_ecology]

## [[concepts/statistical-significance-versus-effect-size|Statistical Significance Versus Effect Size]]

- Use the existing 1,820 genome-to-ecotype assignments and 257 COG differentiation-test results with confidence intervals or bootstrap resampling to determine how stable the small effect sizes are across genomes and species. [src: ecotype_functional_differentiation]
- Extend the analysis from the 15-species sample to all 456 eligible species and model effect size against genome count to test how comparative dataset size influences detection of significant functional differences. [src: ecotype_functional_differentiation]
- Overlay within-species core-genome phylogenies on ecotype assignments and repeat the category tests with phylogenetic controls to test whether significant small effects persist after accounting for phylogenetic or demographic structure. [src: ecotype_functional_differentiation]
- Integrate the 62% of gene clusters lacking COG annotations with AlphaFold or domain analysis to test whether unannotated genes contain additional ecotype-specific effects that are absent from the current effect-size estimates. [src: ecotype_functional_differentiation]

## [[concepts/structural-annotation-gap|Sequence-space depth predicts functional annotation richness]]

- Stratify the 38,051,842 gene cluster–UniProt pairs by core, auxiliary non-singleton, and auxiliary+singleton status, then recompute Spearman correlations and domain-richness curves to determine whether the global ρ = 0.7563 is consistent across pangenome classes. [src: alphafold_msa_annotation]
- Use the full 132,531,501-cluster table, including the 70.7% without an AlphaFold bridge, to compare InterProScan coverage and hypothetical-protein rates between bridged and unbridged clusters; test whether the unbridged population has a larger annotation gap. [src: alphafold_msa_annotation]
- Replace representative-sequence MSA depth with within-cluster depth distributions and compare domain annotations across cluster members to measure how much representative choice obscures sequence-space heterogeneity. [src: alphafold_msa_annotation]
- Join the 415,603 low-MSA-depth core clusters to [[entities/kescience-fitnessbrowser]] fitness measurements and test whether low-depth status predicts condition-specific or essential phenotypes. [src: alphafold_msa_annotation]
- Reweight or stratify the analysis across the 293K genomes by phylogeny and organismal abundance, then test whether the 2.89× and 2.77× core–accessory median-depth ratios persist in a phylogenetically balanced dataset. [src: alphafold_msa_annotation]

## [[concepts/study-batch-confounding-of-environmental-associations|Study and batch confounding can reverse environmental generalization]]

- Use additional NMDC studies with overlapping biome categories, apply study-held-out GroupKFold, and test whether environmental prediction remains above the R²=−0.30 observed in the original cross-study analysis. [src: euk_in_prok_correlates]
- Obtain extraction, filtration, size-fractionation, host-depletion, and library-preparation metadata, then fit hierarchical or batch-adjusted models to test whether these measured workflow factors explain the residual study effect. [src: euk_in_prok_correlates]
- Reanalyze the 1,186-run NEON soil subset with sampling campaign or field-collection batch as held-out groups, testing whether the within-study R²=+0.17 ± 0.06 survives sub-batch validation. [src: euk_in_prok_correlates]
- Separate pooled and unpooled workflow runs and compare representative-biosample metadata with biosample-resolved metadata, testing how the 1,067 pooled runs affect environmental effect estimates. [src: euk_in_prok_correlates]
- Repeat eukaryotic-fraction estimation with classifiers whose reference databases include comparable eukaryotic and plastid coverage, testing whether the observed environment-by-study pattern is robust to the GOTTCHA2-specific measurement scale. [src: euk_in_prok_correlates]

## [[concepts/subsurface-bacillota-specialization|Subsurface Bacillota_B specialization and genome expansion]]

- Reanalyze the 547 enriched OGs with an LLM-based functional scan and manual curation to determine whether the estimated 80–100 anaerobic-respiration-related OGs can be resolved into reproducible functional categories. [src: bacillota_b_subsurface_accessory]
- Decompose enrichment by genus or lineage, using the existing 10-anchor and 62-baseline cohorts, to test which OGs persist after reducing phylogenetic confounding. [src: bacillota_b_subsurface_accessory]
- Localize the accessory functions responsible for the genome-size difference by partitioning anchor and baseline OGs into respiratory, persistence, mineral-attachment, regulatory, and osmoadaptation modules. [src: bacillota_b_subsurface_accessory]
- Apply the same phylum-matched enrichment framework to additional subsurface comparisons to test whether larger genomes and the identified accessory-function profile recur beyond this borehole- and porewater-dominated cohort. [src: bacillota_b_subsurface_accessory]
- Apply the corrected multi-heme cytochrome detector to the clay-project branch and compare its results with the retained sulfite-reduction signal to determine which parts of the porewater-bias interpretation remain supported. [src: bacillota_b_subsurface_accessory]
- Test the genome-expansion/self-sufficiency tension with finer-grained amino-acid EC-number completeness from eggNOG and with MAG-augmented Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge cohorts; determine whether accessory expansion and extreme biosynthetic independence co-occur outside the cultured cohort. [src: clay_confined_subsurface]
- Compare BRC-3 and BIC-A1 directly and resolve Bacillota_B differences at genus level, linking genome presence to Bagnoud’s metaproteomic evidence to distinguish porewater cultivation bias from broader community specialization. [src: clay_confined_subsurface]
- Load the 221 SSO geochemistry samples into CORAL and test whether nitrate, pH, and metal concentrations form the predicted northeast-to-southwest gradient; pair these measurements with metagenomics and genome-resolved Bacillota_B analysis to determine whether the inferred environmental gradients explain the accessory functions. [src: enigma_sso_asv_ecology]
- Extract the available pump-test ASVs from Brick 460-462 and compare them with the 16S spatial pattern, especially the predicted groundwater enrichment of Rhodanobacter at M5; this would test whether the SSO community signal reaches the critical hotspot wells excluded from the current groundwater dataset. [src: enigma_sso_asv_ecology]

## [[concepts/subsurface-bacillota-specialization|Subsurface metabolic signatures depend on porewater versus rock-attached compartment]]

- Add deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge, then apply the same sulfate-reduction and corrected iron-reduction detectors to ask whether the porewater signature persists when rock-attached and uncultivated lineages are represented. [src: clay_confined_subsurface]
- Compare BRC-3 and BIC-A1 genomes directly using compartment-resolved marker analysis to test whether borehole source explains part of the deep-cohort signal. [src: clay_confined_subsurface]
- Link genome-predicted sulfate-reduction markers to Bagnoud’s metaproteomic evidence to test whether the inferred porewater signature is expressed in situ. [src: clay_confined_subsurface]
- Resolve Bacillota_B differences at genus level and repeat the WL, NiFe, and SR comparisons to distinguish lineage-specific metabolism from a compartment effect. [src: clay_confined_subsurface]
- Apply the sulfate-reduction and corrected iron-reduction diagnostic to other subsurface settings to test whether the compartment distinction generalizes beyond the Mont Terri and bentonite-associated cohorts. [src: clay_confined_subsurface]

## [[concepts/subsurface-hydrogeological-zonation|Hydrogeological depth and flow structure subsurface microbial communities]]

- Load the 221 SSO geochemistry samples into CORAL and use spatial-gradient analysis to test whether nitrate, pH, and metal concentrations follow the predicted northeast-to-southwest pattern. [src: enigma_sso_asv_ecology]
- Extract pump-test ASVs from Brick 460-462 and compare M5, L8, and U2 to test whether Rhodanobacter is highest at M5. [src: enigma_sso_asv_ecology]
- Add groundwater samples from M5 and U3 and use matched-well community comparisons to determine whether the inferred hotspots are represented in groundwater. [src: enigma_sso_asv_ecology]
- Sequence metagenomes at the same spatial resolution and compare gene-level metabolic capacity with the 16S-derived redox and process assignments. [src: enigma_sso_asv_ecology]
- Analyze the 18 M6-C2 isolate genomes for anaerobic metabolisms and compare their capacities with the inferred M6 anaerobic-dead-zone hypothesis. [src: enigma_sso_asv_ecology]
- Apply weighted UniFrac to ASV sequences from Bricks 457/460/477 to test whether phylogenetic community structure reinforces the Bray–Curtis spatial pattern. [src: enigma_sso_asv_ecology]
- Repeat 16S profiling across seasons and include sediment temporal replication to distinguish persistent hydrogeological structure from seasonal or plume-driven dynamics. [src: enigma_sso_asv_ecology]

## [[concepts/taxonomic-nomenclature-reconciliation|Taxonomic nomenclature and identifier reconciliation across databases]]

- Combine `ncbi_strain_identifiers`, assembly accessions, NCBI taxids, and GTDB taxonomy versions, then measure how many historical pangenome links change genus or species assignment under a validated reconciliation graph. [src: pitfalls]
- Apply the synonym layer to all MetaPhlAn3 cohort taxonomies and compare abundance, prevalence, and differential-effect estimates before and after reconciliation to determine which findings depend on naming mismatches. [src: pitfalls]
- Test `genome_id`, `gtdb_taxonomy_id`, and accession-based joins against manually reviewed genus-consistent matches, using rank-specific precision and recall to identify safe join keys for each pangenome table. [src: pitfalls]
- Quantify cross-species agreement when gene-cluster identifiers are replaced by COG categories, KEGG orthologs, or Pfam domains, and determine which representation best preserves the biological question without species-specific identifier leakage. [src: pitfalls]

## [[concepts/taxonomic-resolution-dependent-functional-inference|Taxonomic Resolution Controls Detectable Functional Associations]]

- Obtain species- or strain-level ENIGMA or metagenomic data and repeat the strict, relaxed, and unique-clade bridge analyses to test whether contamination-linked functional associations emerge below Genus resolution. [src: enigma_contamination_functional_potential]
- Replace broad COG-fraction proxies with curated metal-stress gene sets and pathway-level summaries, then test whether higher-resolution functional definitions distinguish taxonomic turnover from functional redundancy. [src: enigma_contamination_functional_potential]
- Quantify the contribution of the 862 unmapped genera and expand the genus-to-clade bridge, then evaluate whether missing abundance explains the difference between mapping modes. [src: enigma_contamination_functional_potential]
- Fit mixed-effects or hierarchical models including depth, location cluster, sampling date, and compositional controls to test whether the relaxed-mode defense association persists under richer site structure. [src: enigma_contamination_functional_potential]
- Compare aggregate, within-fraction, and high-coverage analyses using the same resolution-specific samples and bootstrap procedure to determine whether coverage or taxonomic ambiguity is the dominant source of sensitivity. [src: enigma_contamination_functional_potential]

## [[concepts/transcript-protein-discordance|Transcript–protein discordance reveals post-transcriptional control]]

- Collect replicated outer-membrane proteomes across the rescued, intermediate, and wild-type strains, then test whether LptD, LptE, CCNA_01226, CCNA_01217, and Pal show reproducible RNA–protein discordance. [src: caulobacter_fur_lipida_loss]
- Measure targeted *lptC2*, CCNA_01217, LptD, LptE, and Pal abundance with targeted proteomics or immunoblotting, then ask whether the observed protein changes persist after normalization to wild-type baseline. [src: caulobacter_fur_lipida_loss]
- Pair RNA-seq with ribosome profiling and protein half-life measurements, then distinguish translational control from differential protein stability as explanations for the opposing transcript and protein directions. [src: caulobacter_fur_lipida_loss]
- Perform lipidomics and Tol-Pal phospholipid-transport assays, then test whether the protein-level changes restore outer-membrane lipid homeostasis after loss of lipid A. [src: caulobacter_fur_lipida_loss]

## [[concepts/transposon-callability-bias|Transposon Callability Bias in Essentiality Inference]]

- Reanalyze the 41,059 essential genes using gene length, AT content, scaffold position, insertion density, and local library coverage to test which features predict apparent essentiality. [src: essential_genome]
- Compare insertion-depleted genes with independent CRISPRi knockdown or targeted-deletion results to estimate the fraction of calls attributable to technical non-callability. [src: essential_genome]
- Recalculate essentiality rates after excluding low-callability loci and ask whether the range from 12.2% in Pedo557 to 29.7% in Magneto narrows. [src: essential_genome]
- Test whether the 7,084 orphan essentials remain orphaned after sensitive homology searches and synteny-aware comparisons, distinguishing true lineage-specific genes from missed homologs. [src: essential_genome]
- Repeat RB-TnSeq under stress conditions and compare with rich-medium results to separate condition-specific essentiality from missed essentiality caused by the original assay environment. [src: essential_genome]

## [[concepts/two-speed-bacterial-genome|Two-Speed Bacterial Genomes Separate Conserved Metabolism from Accessory Innovation]]

- Add additional taxonomic groups and repeat the COG comparison to test whether the reported +10.88%, +2.83%, +1.64%, -4.65%, -2.09%, -2.06%, -1.81%, and -1.75% contrasts remain consistent across a broader phylogenetic sample. [src: cog_analysis]
- Examine COG L and COG V genes with gene-neighborhood, mobility, and defense-system analyses to test whether their enrichment reflects transferred elements, independently evolving defense loci, or both. [src: cog_analysis]
- Join novel-gene COG assignments to environmental metadata and use habitat-stratified comparisons to test whether accessory functions vary by environment. [src: cog_analysis]
- Reanalyze unassigned genes with complementary functional annotation and compare the result with the approximately 70% COG-annotated fraction to determine how annotation gaps affect the two-speed pattern. [src: cog_analysis]
- Compare gene-level counting of composite COG assignments with component-split counting to test how representation choices affect the reported LV and other composite-category signals. [src: cog_analysis]

## [[concepts/study-batch-confounding-of-environmental-associations|Missing laboratory-protocol metadata leaves residual confounding in environmental metagenomics]]

- Recover DNA-extraction kit, filtration, size-fractionation, host-depletion, and library-preparation records from laboratory information systems, then fit hierarchical models or batch-stratified models to test which protocol variables explain residual eukaryotic-fraction variation. [src: euk_in_prok_correlates]
- Reanalyze the 2,759 runs with classifier-compatible reference databases and a common taxonomic estimator, then test whether environmental associations persist after database effects are controlled. [src: euk_in_prok_correlates]
- Use the 1,186-run NEON subset with sampling-campaign identifiers and restricted permutations or mixed-effects models to test whether the vegetation and geography signal survives sub-batch control. [src: euk_in_prok_correlates]
- Resolve pooled-run heterogeneity by retaining all biosample-level protocol and environmental labels, then compare run-level models with measurement-error or partial-pooling models to quantify label-noise attenuation. [src: euk_in_prok_correlates]
- Expand the analysis to additional studies with recorded sequencing depth and laboratory metadata, then use GroupKFold by study to ask whether protocol-aware models generalize beyond the dominant NEON soil study. [src: euk_in_prok_correlates]

## [[concepts/within-species-conservation-between-species-functional-divergence|Conserved Within-Species Functions Can Coexist with Between-Species Functional Divergence]]

- Match BacDive GCA accessions directly to `kbase_ke_pangenome.genome` genome IDs and test whether the environmental score gradient persists after recovering part of the 56.6% unmatched set. [src: bacdive_metal_validation]
- Compare within-species strain variation and between-species score differences using accession-linked pangenome genomes, and test whether species-level divergence explains more variance than strain-level heterogeneity. [src: bacdive_metal_validation]
- Fit genome-size- and metabolic-complexity-adjusted models using the BacDive isolation metadata and pangenome annotations to test whether contamination association remains after controlling for correlated functional capacity. [src: bacdive_metal_validation]
- Expand matched metal phenotypes beyond the 24 existing utilization records with MIC and growth-inhibition data, then test whether specific metal-tolerance gene families distinguish contamination environments. [src: bacdive_metal_validation]
- Integrate ENIGMA CORAL community data from the Oak Ridge metal-contaminated site and compare field distributions with species-level pangenome scores to test whether the pattern generalizes beyond culture collections. [src: bacdive_metal_validation]

## [[concepts/environmental-resistome|Within-Species Resistome Heterogeneity]]

- Use the 1,305 genome-by-AMR presence/absence matrices and genomic-context mapping to test whether the 1,517 resistance islands reside on plasmids, chromosomes, integron boundaries, or insertion sequences, and whether physical context predicts persistence across lineages. [src: amr_strain_variation]
- Subsample species with >500 genomes and repeat ANI–AMR Mantel analyses to determine whether the phylogenetic signal generalizes to mega-species excluded by the current computational cap. [src: amr_strain_variation]
- Curate collection dates and isolation_source metadata, then apply temporal regression and adequately powered within-species association tests to distinguish AMR change through time from sampling composition. [src: amr_strain_variation]
- Combine AMR ecotype assignments with virulence-factor profiles and metabolic pathway variation to test whether resistance-defined lineages also differ in pathogenicity-associated or ecological functions. [src: amr_strain_variation]
- Apply predictive modeling to the per-gene prevalence records and resistance-island records to ask whether existing co-inheritance patterns predict future AMR gene co-acquisition. [src: amr_strain_variation]
- Reanalyze AMR repertoires with resistance databases beyond AMRFinderPlus to quantify how database scope changes estimates of rare, variable, and fixed within-species resistance. [src: amr_strain_variation]

