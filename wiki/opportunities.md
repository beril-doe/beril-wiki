# Research Opportunities

Concrete next analyses this corpus makes possible — every concept page's
Open Directions, gathered in one place. Follow a link for the evidence.

## [[concepts/abiotic-correlates-of-prophage-burden-in-metagenomes|Abiotic correlates of prophage burden in metagenomes]]

- Validate taxonomy-based burden against prophages detected directly in NMDC metagenome assemblies. This would close the gap that the inference is unvalidated for prophage genes.
- Test sensitivity to genus-level conservation by repeating the analysis at lower taxonomic resolution or excluding genera with variable prophage content.
- Cross-reference environment-enriched modules with induction triggers to explain the pH and temperature correlations.
- Use NMDC longitudinal samples, if available, to test within-site changes in burden over time.

## [[concepts/accessory-conservation-of-metal-and-antibiotic-resistance-genes|Accessory conservation of metal and antibiotic resistance genes]]

- Characterize accessory resistance genes in DvH for mobile elements, recent acquisition, and sharing with Oak Ridge species, closing the gap left by the unexamined mobile-element hypothesis.
- Test antibiotic-important genes across many organisms with the atlas design, to see whether the DvH antibiotic trend holds.
- Separate annotated efflux and czc-type genes from other metal-important genes within the atlas, to test whether the accessory signal sits in annotated resistance genes.

## [[concepts/accessory-gene-content-enrichment-in-subsurface-lineages-relative-to-soil-congeners|Accessory gene-content enrichment in subsurface lineages relative to soil congeners]]

- Run the per-genus H1 analysis, adding clay-isolated Bacillota_B genomes to raise power. This would identify which of the 547 OGs recur across genera and which are lineage-marker noise.
- Run an LLM-based pass over the 462-OG other bucket. This would test the estimate of 80–100 H1-relevant OGs.
- Retarget the NB01–04 pipeline to Bacteroidota, Pseudomonadota and Acidobacteriota. This would show whether the functional-category signal is specific to Bacillota_B.
- Add rock-attached genomes to the anchor, if they become available. This would close the porewater-bias gap.

## [[concepts/active-learning-for-selecting-growth-experiments-from-model-errors|Active learning for selecting growth experiments from model errors]]

- Run the retrospective subsampling test: add held-out labeled pairs in ranked versus random order and compare accuracy gain per pair. This would turn H6 from partially supported into a measured result.
- Separate the three proposed causes of confident errors (missing feature, regulatory mismatch, biological oddity) for the Methylobacterium, Sphingomonas and Microbacterium cells. For example, check whether the relevant gene families are absent from the KO ontology. This would show which errors new growth data can fix.
- Test the sensitivity of the ranking to the doubled field-relevance weight. This would show how much the top 50 depends on that choice.
- After wet-lab results arrive, compare observed outcomes with the 7,844-failure projection toward the ~78% ceiling.

## [[concepts/adsorption-receptors-versus-defense-systems-as-determinants-of-phage-host-range|Adsorption receptors versus defense systems as determinants of phage host range]]

- Test whether ManYZ gene presence or loss predicts lambda infection of the 188 E. coli strains. This would turn the 0.5% infection rate from an interpretation into a tested link.
- Check whether SNIPE-like genes occur in the E. coli panel and whether they predict infection beyond receptor features. The SHAP importances for the 1,582 gene cluster features would show this. It would address whether defense systems add predictive power.
- Build transposon libraries in K. pneumoniae NCTC9140 or HS11286 and screen for phage susceptibility. This would close the Klebsiella fitness gap.
- Pair Klebsiella phage infection data with the genomes' DUF4041 status, to test whether SNIPE carriage changes therapy outcomes.

## [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline|Adversarial review, pre-registration and multiple-testing discipline]]

- Run paired standard and adversarial reviews on several more projects, and record issue counts by type. This would show whether the gap on ibd_phage_targeting is typical.
- Add a PubMed metadata check (author, title, journal, PMID/DOI) as an automated step for reviewer-cited, load-bearing papers. This targets the author-list hallucinations that DOI checks miss.
- For amr_pangenome_atlas, compute FDR-adjusted q-values for the per-gene and per-phylum tests. This would test the claim that correction changes no conclusion, and it would show which exploratory tests survive.
- Log every post-hoc metric change, as in M14, M21 and M23, in a registry separate from pre-registration corrections. Test families could then be enumerated automatically.
- Re-run other degenerate or FAIL verdicts under an ontology-based schema. This would show how many are schema artefacts, as with v1.7 versus v1.8.
- Run null controls for functional_dark_matter's biogeographic and lab-field concordance analyses, as NB10 did for NMDC. This would test whether the marginal 29/47 result exceeds chance once compositional coupling is controlled.
- Re-run the gene_function_ecological_agora M14/M21/M23 metrics with the original and revised definitions side by side. This would show how much those post-hoc changes moved the p-values.
- Repeat the microbeatlas_metal_ecology metal-diversity test on a held-out or newly collected dataset with the hypothesis and analysis plan preregistered. This would turn the post-hoc confirmatory label into a true confirmation.
- Complete the three-method R-native differential-abundance consensus (ANCOM-BC, MaAsLin2, LinDA) for ibd_phage_targeting. This would close the partial-consensus gap.
- Re-run the plant_microbiome_ecotypes within-genus shuffle with many more permutations and a correction across all 15 markers. This would settle whether T3SS survives.
- Add a column-detection check to multiple-testing code so that all p-value columns are corrected. This would prevent the enigma_contamination_functional_potential miss.

## [[concepts/alternative-routes-to-tolerating-lipid-a-or-lps-loss-across-gram-negatives|Alternative routes to tolerating lipid A or LPS loss across Gram-negatives]]

- Run Pfam HMM searches against the named RefSeq proteomes, such as GCF_000196795.1 for A. baumannii ATCC 17978. This would replace annotation-based presence/absence with sequence-based calls. See [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]].
- Express the Caulobacter sphingolipid pathway in A. baumannii and measure colistin-resistant escaper rates. This tests the two-route prediction.
- Count lpxX/lpxL homologs in M. catarrhalis. Genomic support for acylation truncation there is not yet shown.
- Test whether the capsule locus count predicts LPS-loss tolerance across more Neisseria strains.

## [[concepts/amr-ecotypes-and-environmental-association|AMR ecotypes and environmental association]]

- Curate isolation-source metadata for the 190 ecotype-forming species, then rerun the chi-squared tests. This would close the power gap that left only 2 testable species.
- Produce the proposed UMAP and heatmap figures with clinical metadata overlays for the six case-study species. This would turn the visual impression of structuring into tested associations.
- Handle *E. coli* with subsampling or a higher genome cap, so the species with the most genomes is not left out.
- Link ecotypes to virulence factor profiles and metabolic pathway variation. This would show whether ecotypes reflect wider lineage differences.

## [[concepts/amr-genes-in-ica-fitness-modules|AMR genes in ICA fitness modules]]

- Test why only 24% of AMR genes (192/801) enter modules. Compare module-assigned and unassigned AMR genes by mechanism, organism and gene fitness variance.
- Check whether the larger module size holds against a size-matched null. Draw random gene sets from non-AMR modules and compare them with AMR modules.
- Ask what the 136 module families do. Annotate their non-AMR members to name the "broad cellular programs" the report infers.
- Examine the 1 of 209 assignments outside conserved families. Test whether it is organism-specific resistance wiring, and compare with [[concepts/organism-specific-versus-mechanism-specific-wiring-of-amr-support-networks]].

## [[concepts/annotation-and-environmental-metadata-table-gaps-in-the-data-lakehouse|Annotation and environmental-metadata table gaps in the Data Lakehouse]]

- Query per-workflow coverage of pfam_annotation_gff and annotation_enzyme_commission for NEON soil workflows. This would show whether they fill the soil-genus gap left by annotation_kegg_orthology.
- Repeat the H4 cohort analysis with coverage-stratified weighting by habitat. This would separate real photosystem enrichment from habitat skew.
- Recover the Harvard Forest abiotic measurements from NMDC source records, or add the nmdc_arkin gold layers. This would give a covariate beyond the treatment label.
- Rerun the community metabolic ecology matrix with zeros converted to NaN and a check for any real abiotic values. This would show whether partial correlations are possible.
- Ingest the 221 SSO sample-tube geochemistry values, so the registered samples have linked assays.

## [[concepts/annotation-and-pangenome-correlates-of-gene-essentiality|Annotation and pangenome correlates of gene essentiality]]

- Compare ADP1 minimal-medium-only essentials (499 versus 346 on LB) against core membership, to test whether condition-dependent essentials are less conserved.
- Test whether the Protein Metabolism enrichment survives after controlling for annotation density, since essential genes are better annotated.
- Characterize the ~8% of ADP1 essential genes without KO, and the essential-unmapped genes, by ortholog transfer or guilt-by-association (see [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]]).
- Repeat the penetrance versus core-fraction test with a definition that separates mobile-element essentials from core-machinery variants.

## [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches|Annotation-based false negatives in comparative presence/absence searches]]

- Run the proposed Pfam HMM searches against the three named proteomes. This would test the residual concern that an unannotated spt paralog was missed in a comparator.
- Rerun the NCBI count with locus-tag and product-description synonyms for genes like msbA and lptA. This would test how many other false zeros are naming artifacts.
- Measure PaperBLAST false-negative rates in other organisms, to test whether the ~80% figure is specific to Caulobacter.

## [[concepts/annotation-based-gene-detection-limits-in-pangenome-trait-surveys|Annotation-based gene detection limits in pangenome trait surveys]]

- Score xoxF with a curated hit list that includes "Putative dehydrogenase XoxF" products. Then check how many of the 3,272 eggNOG-only genomes are real xoxF, which would settle the 418 versus 5,092 gap.
- Rerun the PGP gene survey with product-text and KO-based detection alongside exact gene names. This would measure how many genes the name-only approach missed.
- Screen annotated pqqC and xoxF clusters for truncation and frameshifts. This would give a functional-validity rate for gene-call presence.
- Test whether eggNOG under-calls phaR (K18080) by searching phaR with a profile-based method in PHB-bearing genomes.
- Repeat ipdC models with penalized (Firth-type) logistic regression to recover a phylum-adjusted estimate despite separation.

## [[concepts/annotation-based-prophage-detection-prevalence-and-domesticated-remnants|Annotation-based prophage detection, prevalence and domesticated remnants]]

- Run geNomad or VIBRANT on representative genomes and compare calls per module with the annotation proxy. This would close the uncharacterized false positive rate and test whether A, D and F prevalence reflects remnants.
- Ingest geNomad or PHASTER output as a Lakehouse table and recompute the AMR-prophage co-location with base-pair distances.
- Repeat the arms-race regression using only strict markers. This would test whether over-counting by broad terms changes the result.

See also [[concepts/limits-of-keyword-and-marker-based-functional-annotation]] and [[concepts/modular-architecture-and-co-occurrence-of-prophage-genes]].

## [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment|Annotation coverage and annotation-density bias in functional enrichment]]

- Run the LLM-based pass over eggNOG Description and bakta product text for the Bacillota_B "other" bucket. This would test the 80–100 of 547 estimate against the scanner's 42.
- Repeat COG enrichment on the Bakta/eggNOG union, to see whether the 70% to 77.3% coverage gain changes essential-versus-dispensable enrichment.
- Apply D2-style residualization to the ecotype analysis. This would test whether the 62% unannotated clusters bias results toward housekeeping functions.
- Report the paralog-fallback sensitivity analysis, with and without the fallback.
- Re-run cog_analysis on more than 32 species to look for phylum-specific patterns.
- Audit zero-coverage marker Pfams in other domain tables, as was done for bakta_pfam_domains, before any new marker-based hypothesis test.

## [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis|Annotation coverage and resolution in genome-wide cofitness analysis]]

- Run Pfam domain-level enrichment on the AMR support networks, where Pfam coverage is 88% versus 68% for GO. This would test whether it finds more specific functions than GO. [src: amr_cofitness_networks]
- Rerun the AMR enrichment with old annotations under a threshold matched to their granularity. This would separate the effect of coverage from that of the overlap threshold.
- Rerun fitness_modules enrichment with PFam added but min_annotated=3, and with min_annotated=2 but without PFam. This would separate the two changes.
- Check Pfam-based fitness-module enrichments against an independent functional benchmark. This would measure the overcounting risk. [src: fitness_modules]
- Examine why old KEGG found lipoprotein and toluene-tolerance terms that InterProScan GO did not. [src: amr_cofitness_networks]

## [[concepts/annotation-coverage-bias-in-chemical-class-callability|Annotation-coverage bias in chemical-class callability]]

- Repeat the class and descriptor tests after adding callables from measured fitness or other independent evidence, to raise power beyond n=9.
- Test descriptors against annotation depth (for example, the number of KEGG or ModelSEED reactions per compound) to separate coverage from biology.
- Run the comparison within the aromatic class, where annotation is deep, to see whether simplicity still predicts callability.
- Test whether callability in alkaloids and terpenoids rises after targeted curation of their catabolic pathways.

## [[concepts/annotation-pipeline-concordance-for-kegg-ortholog-calls|Annotation pipeline concordance for KEGG ortholog calls]]

- Run Genome Depot, eggNOG-mapper and bakta on the same genomes, to measure bakta concordance directly. That would close the gap left by the Depot-versus-eggNOG comparison.
- Recompute per-genome concordance with a metric that does not depend on union size, such as recall of Depot KOs by eggNOG. This would test whether the low median Jaccard reflects breadth only.
- Repeat the cultured–MAG comparison after restricting both cohorts to KOs called by both pipelines. This would show how much of the result depends on pipeline sensitivity.
- Characterise the 1,505 Depot-only KOs by pathway. This would show whether the sensitivity differences concentrate in particular functions.

## [[concepts/annotation-source-disagreement-and-coverage|Annotation source disagreement and coverage]]

- Test whether the Bakta-product advantage for specialty markers holds beyond lanmodulin and XoxJ. One approach is to calibrate other rare, curated markers against eggNOG Preferred_name and KO. This would check whether the "generalizable pattern" claim holds.
- Re-run the xoxF comparison with a regex that includes "Putative dehydrogenase XoxF". Then split the 3,272 eggNOG-only genomes into true xoxF and generic dehydrogenases.
- Import full UniProt into the KBase Data Lakehouse. Measure how many GO, EC, InterPro and Pfam annotations it adds through the UniRef50 bridge, which currently matches only 33.3% of Bakta IDs.
- Check whether the stale eggNOG lanM label traces to specific seed orthologs, then report it upstream.
- Quantify how Bakta's HMMER-on-hypotheticals-only design biases Pfam-based marker detection. Compare against a full Pfam scan on a sample of clusters.
- Re-test the Bakta over-calling of pqqA-E (50–90K Bakta-only genomes) against a stricter product filter, to see how many calls survive.

## [[concepts/antibiotic-dependent-fitness-flip-of-resistance-genes|Antibiotic-dependent fitness flip of resistance genes]]

- Run the expansion proposed above: test AMR fitness costs under antibiotic stress across the full link table. This would close the gap left by the small matched set.
- Add matched experiments for macrolide, glycopeptide and polymyxin classes, which currently lack them. Then test whether narrow-spectrum genes flip only under their matching antibiotic.
- Fit a per-organism model of the flip to quantify the heterogeneity behind the nonsignificant class-matched result.
- Separate carbenicillin from other beta-lactams in the beta-lactam pairs. This would test the explanation for their 50% flip rate.

## [[concepts/aromatic-amino-acid-biosynthesis-and-auxin-pathway-gene-coupling|Aromatic amino acid biosynthesis and auxin pathway gene coupling]]

- Regress ipdC presence on trp completeness with genome size or total complete-pathway count as covariates, to test whether the aromatic-specific signal survives general metabolic capacity.
- Add phenylalanine biosynthesis and combined aromatic pathways as predictors, to see whether TyrR-linked coupling is shared across all three amino acids.
- Repeat the soil stratification with a finer habitat definition and exact or penalised logistic regression, to address ipdC rarity and the quasi-complete separation that sank Model 3.
- Check whether trp-incomplete soil species that carry ipdC also carry tryptophan uptake genes or TyrR, to test the root-exudate hypothesis directly.

## [[concepts/attached-versus-planktonic-communities-in-groundwater-and-sediment|Attached versus planktonic communities in groundwater and sediment]]

- Pair sediment and groundwater samples collected at the same time from the same wells. This would remove the 18-month confound in the BC comparison.
- Test the plume-transport explanation by relating per-well enrichment ratios of Rhodanobacter, Gallionella and Sideroxydans to plume geochemistry.
- Compare the 16S patterns with the 77 sediment and 33 groundwater ORR metagenomes to check that the attached-versus-planktonic pattern holds.
- Expand beyond 5 paired wells to test whether the 0.364–0.450 BC range holds.

## [[concepts/audit-blind-spots-in-inventories-of-data-and-its-use|Audit blind spots in inventories of data and its use]]

- Verify the evaluation and lambda tenant-to-agency mappings against program documentation, to close the 4-table gap.
- Scan research plans and notebook source, not only READMEs, for data-source mentions. This would turn the lower bound on tenant breadth into a measured value.
- Recompute depth counts with COUNT(DISTINCT) on the entity key, to compare rows with entities.
- Compare UniProt entries across refdata and kbase, and genome records across ENIGMA and genome-depot, to size the cross-tenant overlap.
- Group the inventory by database-name family as well as catalog prefix, so that nmdc_* databases in kbase link back to NMDC.
- Test value-space overlap for joins beyond UC1.

## [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species|Bile-acid 7α-dehydroxylation deficit and the ecological cost of targeting bile-acid-transforming species]]

- Measure per-patient bile-acid panels in a CD cohort that also has taxon abundances. This would test the ecotype-level cost prediction at patient level.
- Check bai-operon presence and expression across F. plautii strains. This would test the core-gene hypothesis behind the "no strain escape" inference.
- Repeat the paired substrate–product correlations in a second paired cohort with diet and antibiotic covariates. This would address confounding and the single-cohort limit.
- Model a phage-depletion scenario with and without UDCA or cholestyramine on the tauro-conjugated:secondary bile-acid ratio.
- Relate the network to [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]] to ask whether commensal 7α-dehydroxylators could compensate.

## [[concepts/biocatalyst-potential-of-uncultured-soil-bacterial-enzymes|Biocatalyst potential of uncultured soil bacterial enzymes]]

- Express the Toolik K14731 candidates at 15 °C and measure temperature optima and activity. This would test whether habitat-based "cold-active" labels hold.
- Check the JP12 genome and cultivate Toolik enrichments at 5–10 °C. This would link the MAG genes to a living source organism.
- Run integron-cassette or Pfam PF03157/PF12697 searches in peat or permafrost data. This would test the hypothesis of unannotated LEH-family folds in Acidobacteriota.
- Test the white-space sub-niche by assaying candidates on ε-caprolactone polymer (PCL) at sub-ambient temperature.

## [[concepts/biome-abundance-atlases-as-a-proxy-for-catabolic-potential|Biome abundance atlases as a proxy for catabolic potential]]

- Pair the atlas with metatranscriptomes or metabolite measurements from periphyton and soil samples, to test whether the implicated genera express the relevant pathways. This would close the abundance-versus-activity gap.
- Run enrichment cultures from freshwater-biofilm inocula on the aromatic census compounds. They would test the Comamonadaceae reservoir as a source of utilizers.
- Find a literature anchor for periphyton Burkholderiales prevalence, or replicate it in an independent metagenome collection.
- Add gene-level or pathway-level marine data. This would let the marine arm do more than serve as a negative contrast.
- Re-run the soil-versus-freshwater contrast with a defined statistical test, since it is currently exploratory.

## [[concepts/biome-level-carbohydrate-active-enzyme-repertoire-differentiation|Biome-level carbohydrate-active enzyme repertoire differentiation]]

- Repeat the analysis at CAZy family level (GH1, GH2, etc.) as arkinlab_dbcan grows. This would show which substrate-degradation pathways are enriched in each biome.
- Test whether the GT/GH ratio predicts biome of origin in a held-out genome set. This would check whether the ratio is a usable ecological metric.
- Test whether the GT/GH ratio correlates with measured EPS production or polysaccharide degradation phenotypes. This would check the functional interpretation.
- Compare lineages that have colonized new environments with their relatives. This would address the cross-sectional limit and the causal question.

## [[concepts/biosynthetic-self-sufficiency-as-a-deep-subsurface-adaptation|Biosynthetic self-sufficiency as a deep-subsurface adaptation]]

- Ingest the deep-subsurface MAGs named above and re-run the comparisons. This would test whether the signal emerges once uncultivated lineages are present.
- Add the EC-number metric from eggNOG to get past the GapMind ceiling.
- Enlarge the CheckM-passing deep cohort (currently 6 genomes) so that moderate effects become detectable.

## [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis|Black Queen dynamics in amino acid biosynthesis]]

- Replicate the analysis in additional NMDC studies with paired taxonomy and metabolomics. This would test whether the leucine and arginine signals generalise beyond the current, nearly single-study cohort.
- Obtain or generate metabolomics for the 33 Freshwater NMDC samples, to test whether BQH dynamics differ between aquatic and terrestrial communities.
- Expand metabolomics coverage to power methionine and isoleucine, which have n = 18.
- Score phenylalanine and tyrosine biosynthesis jointly, to test whether hydroxylation explains the tyrosine outlier.
- Link strain-level accessory pathway variation to the community signals, for example for leucine and arginine, using the GapMind core-versus-all gaps.
- Test whether the soil ipdC reversal reflects exudate-supplied tryptophan, by pairing species-level tryptophan completeness with measured root exudate or soil tryptophan.

## [[concepts/calibration-and-denominators-in-environmental-abundance-contrasts|Calibration and denominators in environmental abundance contrasts]]

- Replace the per-sample rank test with a study-aware mixed model, or a sample-level permutation that respects study structure. This would give defensible enrichment statistics in place of the current exploratory ranking.
- Re-run the marine Planet Microbe contrast after species-to-genus rollup, and check that the 0/68 result no longer appears. This would confirm the fix.
- Recompute NMDC relative abundances with both denominators (3825 and ~6700) on a few genera. This would show how large the ~1.75× deflation is in practice.
- Compare the label-dependent contrast with the label-free outlier mode. This would show how much label noise matters.
- Check denominators, label coverage and test calibration in other atlas projects. This would show whether these weak points recur beyond enigma_carbon_census_1.

## [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background|Calibration of fitness-phenotype thresholds against genome background]]

- Recompute the Caulobacter background rate on other condition subsets (carbon, nitrogen, oxidative). Then test whether a single enrichment criterion holds across axes. This addresses the fact that the 33.25% background was measured only for envelope stress.
- Add bipyridyl, ferric salt and hemin RB-TnSeq experiments in Caulobacter. This would let the iron arm of H2 be tested against its own background and would close the preflight failure.
- Run a permutation or random-gene-set null for the burden definition max_fit > 1. This would measure how often one noisy experiment classifies a gene as burdensome.
- Re-evaluate Path A, which is only marginally enriched (fold 1.60×, p = 0.016), with a stricter multiple-testing or sensitivity analysis. Vary the |t| and experiment-count cutoffs to see whether the verdict is stable.

## [[concepts/carbon-pathway-profiles-as-predictors-of-environment-and-lifestyle|Carbon pathway profiles as predictors of environment and lifestyle]]

- Replace majority-vote labels with multi-label or proportion-based environment assignments. This would test whether generalist species such as P. fluorescens and P. putida explain part of the modest accuracy.
- Merge soil and rhizosphere, or add more rhizosphere species (only 6 now). Then repeat the Random Forest to see whether class size and overlap limit accuracy.
- Add finer-resolution pathway or gene-level features beyond 62 GapMind pathways. Compare their accuracy with the 0.408 baseline.
- Test whether D-serine, arabinose, rhamnose and fucose still discriminate environments after accounting for phylogeny. This needs a phylogenetic model, which this page does not cover.
- Repeat the analysis in other genera to see whether the modest signal is specific to Pseudomonas.

## [[concepts/carrier-weighted-versus-binary-metrics-for-sparse-pangenome-events|Carrier-weighted versus binary metrics for sparse pangenome events]]

- Re-run the pilot with the binary flag and the weighted rate under the same category split. This would separate the metric's effect from the category refinement's effect.
- Apply carrier-weighted rates to another sparse pangenome event, such as rare gene gains, to test whether the principle generalises beyond copy number.
- Compare binary and weighted effect sizes across increasing genome counts. This would show whether the 1.4×, 3.3× and 8.1× progression comes from scale or from the metric.
- Test sensitivity to a minimum-carrier threshold on clusters, to quantify how much the rare accidental clusters drive the binary result.

## [[concepts/catabolic-direction-filtering-and-mis-scored-carbon-calls|Catabolic-direction filtering and mis-scored carbon calls]]

- Regenerate the NB03→NB04→NB08 tables with R02107 removed. This would confirm the carbon-callable count of 8 and show how the dark set changes.
- Audit every allowlisted and KEGG-map reaction for carbon-versus-nitrogen role. This would find other errors like xanthine.
- Re-score the callable/dark boundary under alternative direction filters. This would measure how far the dark fraction depends on the filter.
- Replace normalized completeness with raw n_sig_carried / n_required, or weight it by signature size. This would make certainty comparable across compounds.
- Add the anaerobic purine carbon gene cluster to the signature set. This would test whether xanthine becomes legitimately callable.

## [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes|Census and evidence-depth classification of functionally dark genes]]

- Reconcile the T1 Void count (4,273 genes) with the 41.5% "true knowledge gap" share, by cross-tabulating the two schemes over the same 57,011 genes. This would show which evidence types account for the difference.
- Re-estimate the truly dark residual-evidence rates after excluding COG "S" assignments. This would show how much of the 43.5% eggNOG coverage carries real functional information.
- Test the Shewanella K03306 paralog trio (199738, 203545, 202450) with single and combined mutants under nitrogen conditions. This would test the redundancy and subfunctionalization hypotheses.
- Run broad phenotypic screens on the 2,038 darkest genes. This would show whether any gain a testable hypothesis.
- Re-rank the top 100 after normalizing for the number of conditions tested per organism. This would show how much of MR-1's 25 candidates reflects condition depth.
- Re-check the 57,011 dark genes against UniProt, InterPro and current NCBI annotations. This would show how many are already annotated.
- Run AlphaFold2/ESMFold and Foldseek on the 100 top truly dark candidates. This would test whether structure gives annotation clues where sequence homology is absent.

## [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure|ChvG-ChvI envelope-stress regulon phase structure]]

- Run SigU-induction RNA-seq with ectopic vanillate-inducible SigU, then genome-wide differential expression. This would resolve whether SigU drives the 49-gene late cohort, which the coherence test could not settle.
- Compare the SigU-induced genes with the late cohort. This would turn the cohort from a candidate list into a tested regulon.
- Test the regulator-to-structural theme shift with finer functional annotation or a larger cohort, since p=0.243 leaves it undiscriminated.
- Test whether the both-phase genes, including *chvI* and CCNA_03997, depend on ChvG-ChvI directly, for example by profiling a ChvI mutant across the same contrasts.

## [[concepts/clade-level-innovation-signals-and-their-rank-dependence|Clade-level innovation signals and their rank dependence]]

- Rerun the PSII test at intermediate ranks (for example, restricting to Cyanobacteria sub-clades that carry the full PSII repertoire). This would show whether the class-rank-only signal comes from pooling many clades with variable content.
- Replace the 11-KO mycolic panel with a panel tuned to shorter-chain mycolates. This would test whether g__Mycobacterium's low LC reflects panel calibration rather than biology.
- Rerun the mycolic test with a strict mycolic-acid KO set that excludes general fatty-acid pathways. This would show whether the order-rank d=0.288 rises above 0.3 or sample size becomes limiting.
- Apply sub-clade-restricted recomputation to Bacteroidota PUL (LC 0.41). This would test whether a positive sub-clade has a stronger Innovator-Exchange signal than the falsified phylum-level test.
- Correct for phylogenetic non-independence and quantify error propagation across phases, both listed as unresolved. This would test whether the PSII n=21 effect survives.
- Obtain reference consumer data at phylum rank. This would settle whether the PSII phylum-rank reversal is purely a data artifact.

## [[concepts/classifier-and-database-limits-for-estimating-eukaryotic-read-fraction|Classifier and database limits for estimating eukaryotic read fraction]]

- Calibrate GOTTCHA2 against a spike-in or SPF estimate, to close the ordinal-only gap. [src: euk_in_prok_correlates]
- Compute eukaryotic fraction across the SPF corpus, to break the batch confound and allow a properly powered cross-study analysis. [src: euk_in_prok_correlates]

## [[concepts/clay-content-as-a-protective-modifier-of-soil-microbial-functional-potential|Clay content as a protective modifier of soil microbial functional potential]]

- Repeat the shield efficiency test with spatially blocked cross-validation. This would show whether spatial autocorrelation drives the negative R².
- Test within single sampling campaigns or sequencing batches. This would separate batch effects from any clay effect.
- Test the clay-by-stressor interaction at regional scale, where soil type and climate vary less. This would address the unmeasured confounders.
- Add covariates such as pH, organic carbon and climate to the models. This would test whether the weak interaction signal survives adjustment.

## [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections|Clinical and human-associated sampling bias in genome collections]]

- Rerun the environment–gene content comparison with human-associated genomes removed or downweighted, and with matched sample sizes per environment class. This would test directly whether the dilution hypothesis holds. See [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]].
- Compare the human fraction in the AlphaEarth subset with the fraction in all NCBI genomes using one classification scheme. This would show whether the 38% is specific to the subset.
- Reclassify the 17% "Other" genomes with expanded keywords. This would show how many are hidden clinical genomes.
- Estimate AMR prevalence per species after stratifying or reweighting by sampling intensity. This would separate true clinical enrichment from sequencing preference.

## [[concepts/clinical-sampling-bias-in-environment-embedding-analyses|Clinical sampling bias in environment embedding analyses]]

- Add genome count as a covariate in the stratified partial-correlation comparison, to test whether sampling depth explains why human-associated species have higher medians (0.084 vs 0.051).
- Run the proposed environmental-only ecotype analysis directly, to test whether the signal strengthens when clinical genomes are excluded.
- Test whether regional epidemiological lineage structure in Klebsiella and Enterococcus drives the human-associated correlations, for example by comparing within-region and across-region lineage composition.
- Repeat the stratification with a non-majority-vote scheme, such as thresholds on the human fraction, to check sensitivity beyond the continuous Spearman tests.

## [[concepts/co-contamination-and-multiple-testing-confounding-in-metal-function-associations|Co-contamination and multiple-testing confounding in metal-function associations]]

- Run the partial correlation models for each metal against COGs, controlling for the other co-varying metals. This tests whether associations are metal-specific.
- Complete the ρ audit, then recompute the count of associations above a minimum effect size. This shows how many of the 2,355 are biologically meaningful.
- Fit the metals-only db-RDA without project conditioning and report it with the conditional R² = 0.799. Also report how much variance project alone explains.
- Use a permutation scheme or an FDR method that allows for dependence among tests, and compare its count with the Benjamini-Hochberg count. This quantifies the anti-conservative bias.
- Permutation-test the variance-partitioning R² values in comprehensive_metal_ecology.

## [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes|Co-fitness as a predictor of gene co-inheritance in pangenomes]]

- Repeat the pairwise test with a phylogeny-aware null, such as pairs matched on both prevalence and tree distance. This would show whether the small positive delta survives population structure.
- Stratify pairs by prevalence, for example accessory-only against core. This would test the prevalence-ceiling explanation for the negative rho.
- Add organisms with large accessory genomes. This would test whether gene-content diversity predicts effect size.
- Recompute Korea with more genomes or a better-powered statistic. This would tell noise from a true null.

## [[concepts/co-occurrence-and-modularity-of-catabolic-capacities-across-genomes|Co-occurrence and modularity of catabolic capacities across genomes]]

- Test whether the phenylethylamine×aromatic enrichment survives a phylogenetically controlled test, for example within Burkholderiales only. This would separate clade structure from true module linkage.
- Repeat the Haldane OR and Jaccard analysis on a larger capacity set with more non-aromatic pathways. The cross-block test has only 15 pairs and few genomes with both module types (25/3109).
- Go beyond genome-level presence. Check gene proximity or operon context for the paa and funnel genes, to ask whether co-occurring capacities are physically linked and so portable.

## [[concepts/co-occurrence-network-structure-and-metal-tolerance-guilds|Co-occurrence network structure and metal-tolerance guilds]]

- Regress partner count on KO density with B_std as a covariate in each stratum. This would show whether the signal is independent of niche breadth or mediated by it.
- Compute mean phylogenetic distance between focal genera and their partners against a random null from the same network. This would test whether the guild is phylogenetically structured.
- Repeat the partner characterisation with a stricter or rank-based edge threshold. This would address the near-saturated networks, where the φ > 0.3 filter keeps only 0.91% of pairs.
- Test whether the Firmicutes partner bias holds when focal genera are matched to controls on niche breadth as well as phylum.

## [[concepts/co-occurrence-of-plant-growth-promoting-genes-and-trait-guilds|Co-occurrence of plant-growth-promoting genes and trait guilds]]

- Locate pqqC and acdS on assembled genomes to test operon linkage against independent co-selection, which gene-level presence/absence cannot do.
- Stratify nifH-bearing species by lifestyle (marine, symbiotic, free-living soil) and compare their PGP co-occurrence, to explain the aquatic depletion in soil.
- Examine the generalist lineages carrying both nifH and pqqC, to see what lets them escape the negative association.
- Link pqqC + acdS + hcnC species to inoculant strain lists to check the module against known effective inoculants.

## [[concepts/coarse-cog-fraction-proxies-versus-pathway-level-stress-evidence|Coarse COG-fraction proxies versus pathway-level stress evidence]]

- Build curated metal-stress gene sets and pathway-level summaries, then rerun the gradient analysis. This would test whether the null result reflects the proxy or the biology.
- Repeat the gradient analysis at species or strain resolution where the taxonomy bridge allows. This would test whether fine-scale adaptation is masked by genus aggregation.
- Compare pathway-level and COG-level results on the same samples. This would show how much signal broad categories dilute.

## [[concepts/community-function-of-rare-earth-acid-mine-drainage-mags|Community function of rare-earth acid mine drainage MAGs]]

- Assemble a larger, independent collection of REE-impacted metagenomes. This would test whether the stress-dominated, methylotroph-poor pattern holds beyond one bioproject.
- Characterize the f__REEB76 clade. Place it phylogenomically, predict its metabolism, and check for xoxF or lanmodulin.
- Examine the 4 xoxF-carrying MAGs. Identify their lineages and test whether they are the rare methylotrophs.

## [[concepts/community-level-niche-coverage-and-resource-depletion-for-competitive-exclusion|Community-level niche coverage and resource depletion for competitive exclusion]]

- Measure resource depletion directly in co-culture: grow PA14 with the k=3 consortium on single amino acids and test whether the pathogen becomes resource-limited as the depletion argument predicts.
- Test the lag window experimentally by adding commensals before PA14, with and without prebiotic pre-loading, and compare PA14 yield with simultaneous inoculation.
- Check the 1.5× collective depletion argument by measuring consumption rates of consortium members rather than inferring them from growth rates.
- Repeat the coverage and kinetics analysis in CF sputum-like medium and with more PA strains. This would show whether the 100% coverage depends on PA14 and on defined substrates.

## [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria|Compartment-specific functional differentiation of plant-associated bacteria]]

- Re-run the Fisher enrichments with the genus-level logistic-regression phylogenetic control. This would test which of the 69 significant combinations survive beyond the 3 of 15 markers that passed the label-shuffling null.
- Repeat the location-versus-dispersion decomposition on each marker separately. This would show which functions drive the 84% location share.
- Validate compartment labels against metagenomic evidence. This would limit the effect of weak isolation_source metadata. See [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa]].
- Add more endophyte genomes to pass the 30-species threshold. This would allow a four-compartment decomposition.

## [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry|Complexity hypothesis: regulatory versus metabolic gene transfer asymmetry]]

- Test the architecture-to-exchange link with an independent structural check. This could use AlphaFold confidence scores or domain-shuffling literature, which would close the gap that the finding is exploratory.
- Split the regulatory category by sub-class (TCS-HK, transcription factors, translation-related). This would show which sub-classes drive the d=−0.21 signal and which drive the TCS-HK d = 0.65 signal.
- Run the regulatory/metabolic comparison within MGE-excluded KOs. This would show whether the 4.13% MGE rate in regulatory KOs masks a stronger vertical-inheritance signal.
- Model exchange rate jointly on architectural promiscuity and the regulatory/metabolic/mixed class. This would separate the mixed-class effect from the promiscuity effect.
- Compare NB11 clumping with Burch-style connectivity values for the same KOs. This would test whether the two scales rank genes alike.

## [[concepts/compositional-coupling-in-metagenomic-validation-of-carrier-abundance|Compositional coupling in metagenomic validation of carrier abundance]]

- Run the full NMDC permutation test, shuffling sample labels on the raw per-sample matrices. This would replace the partial nulls, the sign test and Fisher combination, with a proper null for the coupling.
- Re-test the carrier-trait correlations after removing or adjusting for the abundant ubiquitous genera (Pseudomonas, Klebsiella, Bacteroides). This would show how much signal remains beyond coupling.
- Correlate carrier abundance with NMDC metabolite and protein profiles. This would give more direct functional evidence.
- Check whether the abundance advantage of PHB-high genera in NMDC survives the same abundance adjustment.
- Test at species resolution where the bridge allows. This would address the genus-level blind spot.

## [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models|Compound identifier ambiguity in linking metabolites to metabolic models]]

- Rebuild the WoM–ModelSEED link using InChIKey and CHEBI instead of names. This would test how many of the 107 formula-only compounds resolve to one molecule.
- Build the GapMind pathway-to-metabolite table and count how many WoM compounds then link. This closes the failed WoM–GapMind link.
- Fill the sparse NMDC KEGG IDs by mapping on `inchikey` or `chebi`, and compare the results with the substring-based pathway assignments.
- Audit the other NMDC name patterns for collisions like leucine/isoleucine, and report each one's effect on the results.

## [[concepts/concordance-between-cross-genus-predictive-genes-and-within-strain-gene-fitness|Concordance between cross-genus predictive genes and within-strain gene fitness]]

- Expand each top-SHAP KO to all KOs in its KEGG module and recompute concordance. This would separate "wrong feature, right pathway" from "wrong pathway".
- Clarify which correlation-group expansion was run for the 1.19× result and which remains undone, to resolve the inconsistency in the report's status for H3.
- Examine the per-strain spread (1.72x to 0.83x) against strain features such as pathway redundancy, to test whether redundancy explains missing fitness defects.
- Compare concordance for SHAP-highlighted KOs with that for their correlated neighbors, to test whether credit dilution hides the causal gene.

## [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers|Concordance between laboratory fitness phenotypes and field environments of gene carriers]]

- Run the annotated accessory-gene null through the same carrier pipeline, to test whether 61.7% exceeds what ordinary accessory genes give.
- Repeat the NMDC check with a control for compositional coupling, to see how much of the 76/105 significant correlations survives.
- Expand condition classes beyond broad stress, for example by splitting metal, osmotic and oxidative stress, to test whether concordance differs by stress type.
- Add environment metadata for genomes without AlphaEarth coverage, to raise power beyond the 28% of genomes covered.
- Examine the reversed-direction hits (odds ratios below 1 in B. thetaiotaomicron and K. oxytoca) as possible non-concordant cases.
- Test the 511 accessory, strong-fitness dark genes beyond the 47 testable clusters, to see whether the P. putida N2C3 candidates reach FDR < 0.05 with more carrier genomes.

## [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data|Concordance of genome-scale metabolic model predictions with experimental data]]

- Test the discordant genes for pathway or regulatory enrichment. This would show whether the errors are metabolic or regulatory. See [[concepts/pangenome-conservation-of-metabolic-model-discordant-genes]].
- Assess gapfill confidence with pangenome conservation data, since 87% of growth predictions depend on gapfilling.
- Rebuild the initial models with gapseq and recompute carbon-source precision. This would show whether false positives fall.
- Compare knockout validation with gapfilled reactions fixed against validation without them. This would address the circularity problem.
- Add reactions or constraints for the 30 unmapped quinate-specific genes and for Complex I subunit loss, then test whether predicted Complex I essentiality changes from 0%.

## [[concepts/condition-dependent-fitness-trade-offs-of-core-versus-accessory-genes|Condition-dependent fitness trade-offs of core versus accessory genes]]

- Connect laboratory fitness to AlphaEarth environmental data to ask whether organisms from more variable environments have more trade-off genes in their core.
- Test the pathway-participation explanation. Compare trade-off enrichment after controlling for the number of pathways per gene.
- Check whether detectability drives the core enrichment. Compare effect sizes after matching core and accessory genes on expression or annotation depth.

## [[concepts/condition-dependent-respiratory-chain-configuration|Condition-dependent respiratory chain configuration]]

- Measure NADH flux or the NADH/NAD⁺ ratio directly on quinate, acetate and glucose. This would test the flux explanation, which so far rests on inference.
- Obtain growth data for NDH-2 and the ATP synthase subunits. This would fill the 26-gene gap.
- Test whether ACIAD3522 oxidizes NADH into the quinone pool. This would show whether it is a respiratory enzyme.
- Repeat the carbon-source deletion screen in another organism that has both Complex I and NDH-2. This would test the species-specificity caveat.

## [[concepts/condition-specific-fitness-correlation-across-carbon-sources|Condition-specific fitness correlation across carbon sources]]

- Identify the ADP1 urea-specific genes and test their pangenome conservation. This would show whether the independence of urea is a conserved trait.
- Recompute the ADP1 correlations after removing the housekeeping and biosynthesis genes that are important in every condition. This would show how much of the moderate mean r (0.44) comes from shared core genes.
- Test the metabolic entry-point hypothesis by relating correlation between carbon-source pairs to the distance between their entry points in central metabolism.
- Run the same pairwise analysis on Fitness Browser organisms with many carbon sources. This would test whether ADP1's pattern holds outside one organism.

## [[concepts/condition-specific-fitness-of-dark-genes|Condition-specific fitness of dark genes]]

- Re-run the condition-class comparison after removing genes in operons with strongly fit neighbours. This would test how much polar effects drive the nutrient, community and iron enrichment.
- Reconcile the two stress percentages by matching gene sets and condition definitions.
- Test the novel-metabolism hypothesis directly. Follow up the nitrogen-source and mixed-community genes with targeted growth or interaction assays.
- Compare the condition profiles of dark genes in ICA modules and outside them, to see whether module membership changes the stress depletion.

## [[concepts/condition-specific-gene-importance-across-carbon-sources|Condition-specific gene importance across carbon sources]]

- Test whether the genes defective only on urea form a distinct pathway set. Use gene-level enrichment on the urea-specific defects against the other 7 conditions.
- Recompute all pairwise correlations with one shared definition (defect call versus growth ratio). This would explain the gap between 0.38, 0.44 and the median of 0.25.
- Examine the 10 genes defective in all 8 conditions. Ask whether they are general growth genes and whether they overlap TnSeq essentials.
- Check whether the demanding-tier conditions (urea, acetate, butanediol) share genes beyond the acetate–butanediol–lactate group.

## [[concepts/condition-specific-gene-phenotypes-and-functional-annotation-yield|Condition-specific gene phenotypes and functional annotation yield]]

- Compare ADP1 specificity profiles with Fitness Browser RB-TnSeq data for organisms grown on glucose and lactate, to test cross-species pathway specificity.
- Use co-specific gene sets to infer shared regulators, and test the predictions against known regulons such as the quinate operons.
- Measure replicate variation in the growth ratios, to test the assumption that cross-condition variation is biological.
- Recompute the 31% figure against both denominators (complete matrix and dispensable genes), to show whether they agree.
- Compare the Complex I subunits in the quinate-specific set with other carbon sources. See [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].

## [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association|Confounding and robustness in environmental metabolomics–genomics association]]

- Replicate H1 on additional NMDC studies with paired taxonomy and metabolomics, using study-level random effects, to close the single-study gap.
- Populate abiotic variables for the overlap samples and rerun H1 and H2 with partial correlation or mixed models, to test environmental confounding.
- Add paired metabolomics for Freshwater samples to test whether Black Queen signals extend beyond soil.
- Rerun amino acid tests with PC1-residualized carbon substrate range to separate carbon availability from biosynthesis capacity.
- Audit all compound-name matching for substring collisions, as with isoleucine and leucine.

## [[concepts/confounding-of-compound-source-with-chemical-class|Confounding of compound source with chemical class]]

- Add necromass-sourced compounds from non-aromatic classes, such as fatty acids and sugars, that have ENIGMA-isolate utilizers. This would break the phthalate confound and allow a source contrast among callable compounds.
- Add groundwater-sourced phthalate-class aromatics or close analogs. Source and class would then vary independently within one chemical class.
- Check whether the necromass skew among orphan compounds (13/24 versus 16/59) reflects annotation coverage or real chemistry. Test it by comparing KEGG linkage across chemical classes.
- Use measured fitness data ([[concepts/measured-fitness-as-independent-evidence-of-carbon-utilization]]) to extend callability beyond the 8 isolate-callable compounds, then rerun the H3 test.

## [[concepts/conservation-of-amino-acid-biosynthesis-pathways-across-bacteria|Conservation of amino acid biosynthesis pathways across bacteria]]

- Check lower-confidence GapMind predictions for DvH, to see whether a serine pathway is listed with "steps_missing" status.
- Review the literature to find out whether D. vulgaris serine auxotrophy has been documented experimentally.
- Grow DvH on serine-free minimal media to confirm or refute auxotrophy.
- Repeat the GapMind completeness count on a phylogenetically broader genome set, to test whether 17 of 18 pathways stay near-universal beyond Proteobacteria.
- Relate the serine gap to [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]], which would test the genomic economy explanation.

## [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms|Conservation of cofitness modules across genomes and organisms]]

- Test whether the module-versus-null delta persists when core modules are compared against nulls matched on both prevalence and core status. This would show whether the Korea null result is a ceiling effect.
- Extend the co-inheritance test beyond 6 organisms, and add more accessory modules to settle the p=0.051 trend.
- Identify the co-regulated functions of the 48 accessory modules in the flexible genome.
- Ask whether universally essential gene families exist across all 43 organisms.
- Test family breadth against core fraction within a stricter set of non-core modules, where the high baseline cannot hide a gradient.
- Integrate module predictions with core, auxiliary and singleton pangenome classes, and test which modules are enriched in accessory genes.

## [[concepts/conservation-of-cofitness-modules-in-the-core-genome|Conservation of cofitness modules in the core genome]]

- Annotate the 48 accessory modules and the 38 accessory module families by function. This would show what co-regulated functions live only in the flexible genome.
- Repeat the enrichment test against a baseline that excludes the ceiling effect, for example within accessory-rich organisms. This would test whether the lack of a breadth gradient is purely a ceiling effect.
- Vary the ICA membership threshold (|r| and the 50-gene cap) and the 90%/50% class cutoffs. This would show how robust the core, mixed and accessory proportions are.
- Test DvH-style lab versus conserved module classes in other organisms. This would check whether accessory modules tend to respond to lab-type conditions beyond one organism.

## [[concepts/conserved-metal-phenotype-gene-families-and-novel-metal-tolerance-candidates|Conserved metal-phenotype gene families and novel metal-tolerance candidates]]

- Characterize the 89 truly unknown and 43 DUF-domain families with PaperBLAST, InterPro and AlphaFold. This would fill the annotation gap. See also [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]].
- Use AlphaFold to look for metal-binding sites in UCP030820, YebC and DUF1043.
- Test the two organisms with 54 novel candidate genes each against the standard metal panel, since they have so far been tested only against iron.
- Re-estimate novel versus annotated specificity with experiment count controlled. This would test the report's explanation for the lower specificity of novel candidates.
- Test the YebC translation-bottleneck hypothesis. One option is to measure expression of proline-rich metal transporters under metal and non-metal conditions.

## [[concepts/conserved-multi-metal-tolerance-gene-families|Conserved multi-metal tolerance gene families]]

- Run ICA on metal conditions only and check whether members of the 318 families fall into the same modules. This would show whether they form regulatory units.
- Compare AlphaFold structures of proteins in the broadest families, those spanning up to 14 organisms, for metal binding sites or membrane interfaces.
- Test one or two of the broadest families, such as a DNA-repair or ion-homeostasis family, by overexpression in a single host. This would check the engineering proposal.

## [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations|Constitutive versus inducible gene classes in niche-breadth associations]]

- Expand the cofactor set beyond 7 KOs (only 4 assignable in the jackknife), then rerun the association test and the leave-one-out test. This would show whether the signal generalises beyond Fe–S, molybdopterin and cobalamin genes.
- Run the partial R² regression of niche breadth on cofactor density, controlling for primary-set density, to settle collinearity with broader metal-gene investment.
- Test whether the HGT-decoupling explanation holds by comparing resistance KOs on mobile elements with chromosomal ones against niche breadth.
- Apply the split-magnitude permutation to further non-metal families, so the largest-split claim rests on more than three comparators.
- Probe why efflux pumps are significantly positive while other AMR subcategories are not, using finer subcategory models.

## [[concepts/construction-and-validity-of-cofitness-gene-groups|Construction and validity of cofitness gene groups]]

- Replace the row-index operon exclusion with a begin/end/strand-based one. Then test whether the 0.6% excluded fraction and the AMR partner counts change.
- Recompute AMR cofitness with pairwise-complete Pearson correlation on a few organisms. This would check the claim that zero-filling does not affect conclusions.
- Test the 40% component cap on organisms with fewer than ~100 experiments, for example by comparing module recovery at several ratios. This would show how many modules the cap misses.
- Repeat the threshold comparison (|r| ≥ 0.3 against other cutoffs) and record how module membership shifts. This would show how sensitive downstream conservation results are to it.

## [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential|Contamination and metal gradients as drivers of community functional potential]]

- Run the ENIGMA confirmatory tests at pathway or gene level, not broad COG categories. This would test whether the genus-level null reflects coarse mapping.
- Repeat the coverage-aware defense models on a larger set of samples with high mapped-abundance fraction. This would show whether the signal survives global FDR control.
- Run the soil metal-function analysis with individual metals, covariates for co-occurring metals, and the pending spatial validation. This would test whether the strong soil signal is specific to one metal.
- Apply the ENIGMA index variants to the plume-well CWM metal-diversity contrast. This would test whether plume status and measured metal gradients give the same signal.

## [[concepts/continuous-versus-binary-predictors-of-gene-essentiality|Continuous versus binary predictors of gene essentiality]]

- Recompute essentiality fraction using only conditions matched to the medium of the essentiality call. This would test whether mixing diverse conditions explains its AUC below 0.5.
- Score fitness and proteomics on the same gene set in minimal medium. This would make their AUC comparison like-for-like.
- Repeat the comparison in other organisms to test whether the ranking holds beyond ADP1.

## [[concepts/continuous-versus-discrete-structure-of-condition-dependent-gene-essentiality|Continuous versus discrete structure of condition-dependent gene essentiality]]

- Add nitrogen-source and stress conditions to the ADP1 deletion panel, then re-run PCA to test whether the ~5 dimensions grow with the panel.
- Run ICA on the 2,034×8 matrix to test whether it finds latent factors that hierarchical clustering misses.
- Compare deletion and chemical-perturbation profiles in one organism, to separate method effects from metabolic architecture as the cause of the ADP1–*E. coli* difference.
- Test whether other single-entry-point pathways form discrete modules when a matching condition is present, as quinate does.

## [[concepts/contrast-design-and-confounding-in-testing-a-putative-lipid-a-processing-enzyme|Contrast design and confounding in testing a putative lipid A-processing enzyme]]

- Run replicated outer-membrane proteomics. Detection in a single-replicate proteome is the gap.
- Add an isolating contrast with more transcript replicates, since pvalue 0.048 and FDR 0.109 sit near the threshold.
- Test directly for the predicted CPG headgroup by lipid analysis.
- Run contrasts that separate Δfur from Δlpxc, to test whether CtpA induction follows Fur regulation.
- Fix thresholds, including borderline handling, before any new contrast is run.

## [[concepts/coordinate-quality-and-institutional-address-artifacts-in-genome-geolocation|Coordinate quality and institutional-address artifacts in genome geolocation]]

- Compute isolation_source homogeneity (for example, the entropy of source terms) at each of the 11,765 locations. Then check whether it separates Rifle, Saanich Inlet and the Siberian soda lakes from Pittsburgh. This tests the proposed refinement.
- Compare AlphaEarth-based environment signals for the Good, Suspicious cluster and Low precision classes. This would show whether flagged coordinates distort downstream results, as in [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].
- Quantify how often ncbi_lat_lon is NULL, malformed or low precision across gtdb_metadata. This would size the loss before coordinate-based analyses.
- Check integer-degree locations such as Lima against any finer-grained source metadata. This would show whether the coordinates are only approximate or actually wrong.

## [[concepts/core-gene-prevalence-ceiling-on-co-occurrence-signal|Core-gene prevalence ceiling on co-occurrence signal]]

- Run the auxiliary-only re-analysis described above, to test whether the cofit-versus-random phi difference reappears once the ceiling is removed.
- Stratify the co-fitness-strength versus phi correlation by pair prevalence, to test whether the rho of -0.109 is driven by core-gene pairs.
- Add co-fitness data for the two Ralstonia organisms, or other high-diversity species, to test the signal where auxiliary content is large.
- Report the number of computable (non-NaN) pairs next to every delta, so that results like Korea's are not read as biology.

## [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes|Core-genome enrichment of metal-stress fitness genes]]

- Re-run the shared-stress correction for cadmium, iron and manganese with more organisms. This would test whether the cadmium and iron reversals survive adequate power.
- Test whether DvH's below-baseline heavy-metal core fraction recurs in other organisms using one baseline and one gene definition. This would show whether DvH is an exception or reflects a field-versus-lab difference.
- Combine the NaCl-corrected gene classes with the three-tier classification. This would show whether the specificity gradient in core fraction survives shared-stress removal.
- Compare the 82%-core essential genes with the corrected metal gene sets. This would test whether the exclusion affects conclusions per metal.
- Add organisms for uranium and cadmium, and test manganese and tungsten outside DvH. This would show whether their weak or single-organism enrichment is true neutrality or low power.

## [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes|Core versus accessory partitioning of gene functions and trait genes]]

- Compare nucleotide identity of AMR clusters shared between soil and clinical species, to close the gap left by status-only inference.
- Test the accessory AMR fraction over time in densely sampled species such as S. aureus and K. pneumoniae.
- Combine environment-AMR profiles with amr_fitness_cost to separate recent-acquisition cost from selection.
- Test plasmid, transposon and integrative-element association of accessory AMR clusters once mobile-element calls exist.
- Recompute core/accessory labels with a genome-count-aware threshold, to check how much small-genome-count imprecision shifts the environment contrasts.
- Run the acquisition-depth gain-ratio analysis on PGP genes, to test directly whether their core status reflects vertical inheritance rather than inferring it from core/accessory labels.
- Repeat the metal analysis with a lower prevalence threshold, since no metal KO reaches 95% and coreness could not be tested.
- Recompute DISARM core/accessory classes with a more specific anchor than PF00176, to see whether DISARM becomes accessory like the other defense systems.
- Repeat the beneficial-versus-pathogenic core comparison within Pseudomonas only, to test whether taxonomic scope explains the contrast with Loper et al.
- Test whether prophage modules with high core fractions (lysis, packaging) are domesticated remnants rather than active prophages, using the module-level conservation classes.

## [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation|Costly but conserved genes: laboratory burden versus conservation]]

- Use the fraction of species genomes carrying each gene cluster instead of the binary core/accessory call. This tests whether the costly-and-conserved quadrant holds at graded conservation.
- Redo the burden classification with a replicate-robust criterion instead of a single experiment with max_fit > 1. This tests whether the 28,017 count is sensitive to noise.
- Compare costly-and-conserved genes with fitness data from ecologically relevant conditions such as soil or host-like media. This would test the natural-selection explanation directly.
- Test whether the core-burden excess reflects trade-offs. Check whether costly core genes are also strongly beneficial in other conditions.

## [[concepts/counter-ion-confounding-in-metal-fitness-assays|Counter-ion confounding in metal fitness assays]]

- Compare metal–choline chloride overlap with metal–NaCl overlap in Fitness Browser organisms that have choline chloride experiments. Choline chloride supplies Cl⁻ without Na⁺ or osmotic effects, so this would separate chloride from osmotic confounding.
- Run matched metal chloride and sulfate RB-TnSeq in a single organism under identical growth conditions. This removes the aerobic/anaerobic confound of the psRCH2 comparison. Zinc and cobalt pairs in DvH or MR-1 are natural first tests.
- Run NaCl dose-response in DvH to dose-match NaCl stress to the chloride delivered by metal salts. This would test directly what the zero-chloride controls only imply.
- Test the dropped H1d by comparing functional profiles of chloride and oxyanion metals.

## [[concepts/coverage-and-bias-in-linking-strain-phenotype-databases-to-pangenomes|Coverage and bias in linking strain phenotype databases to pangenomes]]

- Implement GCA accession matching alongside name matching. Compare the species recovered with the suggested 10–30% gain, and re-run the match-rate comparison between the two bridges.
- Reconcile the 43.4% and 38.4% match rates by running both bridges on the same BacDive snapshot and GTDB release, and tracing where strains drop out.
- Compute post-matching sample sizes and power for each BacDive category, such as heavy-metal-contamination strains, before any hypothesis test.
- Add ML-predicted Gram stain, motility and oxygen tolerance as a flagged sensitivity analysis. Measure how far coverage rises and how much model-dependent bias enters.
- Check whether phenotype coverage tracks how well-studied a genus is. This would test the testing-bias concern directly.

## [[concepts/coverage-gaps-in-deletion-collections-and-their-link-to-pangenome-conservation|Coverage gaps in deletion collections and their link to pangenome conservation]]

- Repeat the missing-versus-present comparison in another species with a deletion collection and a Lakehouse pangenome. This would test whether the bias is general or specific to ADP1.
- Redo the core-membership comparison using population-level or multi-genome data for ADP1. This would address the species-level resolution limit.
- Fit a model with length, annotation and conservation as joint predictors of missingness. This would separate the contributions of each.
- Check whether the uncertain-class genes map to fragments or pseudogenes in the genome. This would test the report's interpretation.

## [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification|Cross-cohort portability and batch dominance in microbiome and metabolomic stratification]]

- Rebuild ecotypes on functional pathway or KEGG feature matrices to break taxonomic-feature leakage. This would test whether E1 yields a usable target list.
- Run within-substudy CD-vs-nonIBD analysis stratified by ecotype, first checking that substudy × ecotype × diagnosis cells have ≥ 10 samples.
- Combine UC-vs-HC and CD-vs-HC as IBD-vs-control for power.
- Rerun the HMP2 and Franzosa pooled clustering after ComBat or quantile normalization, and compare LOSO ARI to 0.000 and 0.113. Also test K=2 against K=4. This would show whether the m/z bridge can be rescued.
- Replicate the polyamine enrichment in Franzosa using name-annotated supplementary tables, since the m/z bridge cannot reach it.
- Repeat the K-selection by cross-method ARI in a second cohort. This would test whether K=4 generalizes.

## [[concepts/cross-database-concordance-of-metabolite-evidence|Cross-database concordance of metabolite evidence]]

- Compare the 28 WoM–FB matches with the 19 curated matches for FW300-N2E3 item by item. This would show whether the counts differ by matching rule, condition type or data subset.
- Rebuild the WoM–BacDive crosswalk with InChIKey and CHEBI identifiers instead of names. This would test whether the overlap grows beyond 8 metabolites.
- Build a GapMind pathway-to-substrate/product lookup table. This would let WoM–GapMind concordance be tested for more than 13 metabolites.
- Compare WoM profiles across growth media. This would separate constitutively produced metabolites from medium-dependent ones, and so address the R2A versus minimal-medium gap.
- Run the same crosswalk on other organisms. This would show whether FB and GapMind concordance stays at 100%, or whether that was an artifact of FW300-N2E3.

## [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs|Cross-organism fitness concordance of dark gene orthologs]]

- Run the proposed stress experiments in MR-1 and P. putida N2C3, plus nitrogen experiments, to test OG01997, OG02907 and OG01383 across genetic backgrounds.
- Extend ortholog calls to the 16 organisms without bidirectional best hit coverage. This would test whether truly dark genes are non-concordant or just unmeasured.
- Use a test sensitive to ceiling effects, since both medians are 1.0. This would check whether the dark-versus-annotated null hides differences.
- Test motility-concordant groups such as OG10428 and OG10455 for chemotaxis roles by targeted assays.

## [[concepts/cultivation-bias-in-genome-collections-versus-uncultivated-lineages|Cultivation bias in genome collections versus uncultivated lineages]]

- Repeat the cultured-versus-MAG KO test with Patescibacteria removed from the MAG cohort. This would test the prediction that the gap narrows, and it would show which of the 813 MAG-enriched KOs survive.
- Cross-reference the 554 MAG-only KOs with the HGT analysis of Gios et al. (2025) to see which were horizontally acquired.
- Annotate the unknown-function MAG-enriched KOs and test for Patescibacteria-specific novel metabolisms.
- Ingest deep-subsurface MAGs from the clay report's sites into the pangenome and re-run its H1/H2/H3 framework. This would test whether the self-sufficiency signal appears once rock-attached lineages are present.
- Compare KO prevalence within matched genome-size bins, to separate genome-size effects from selection by cultivation.

## [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities|Cultivation bias toward porewater versus rock-attached subsurface communities]]

- Add MAG-based rock-attached Mont Terri genomes and rerun the SR/IR diagnostic, to test whether the genuine community matches the literature.
- Match the Opalinus genomes to Bagnoud's MAGs by ANI. Then ask whether gene presence matches expression-validated activity.
- Rerun the IR-side comparison with corrected multi-heme cytochrome markers, to see how much of the porewater narrative is recovered.
- Re-annotate compartments from curated metadata, to bound the effect of keyword inference.

## [[concepts/defense-and-mobile-element-gene-content-as-drivers-of-ecotype-differences|Defense and mobile-element gene content as drivers of ecotype differences]]

- Test V and L directly as subsets, as the ecotype_analysis report proposes, to see whether these categories show stronger environment effects than others.
- Measure whether V genes lie near L genes (defense islands) in the ecotype-differentiating gene sets. This would test the Millman-based hypothesis.
- Look for prophage or phage-host data in the species with significant V differentiation. This would test the phage-pressure hypothesis.
- Compare L effects after separating transposases and integrases from other repair genes. This would show whether mobile elements drive the L signal.

## [[concepts/defense-system-burden-scaling-with-prophage-load-anti-phage-arms-race|Defense-system burden scaling with prophage load (anti-phage arms race)]]

- Refit the negative-binomial GLM with the GTDB tree as a phylogenetic covariance structure, for example with phyr::pglmm. This would test whether the arms race holds independent of shared ancestry, which the current categorical phylum control cannot do.
- Re-estimate negative-binomial dispersion from the data instead of fixing alpha=1.0, and check whether the standard errors change.
- Repeat the analysis with species that have fewer than 5 genomes, including environmental MAGs, to test whether the pattern extends beyond well-sampled, culturable species.
- Model effect-size heterogeneity across phyla, for example Actinomycetota against Campylobacterota, using candidate covariates.
- Run within-genus analyses to check whether part of the signal is a within-genus pattern that only appears cross-phylum.

## [[concepts/defense-system-co-occurrence-syndromes-and-defense-islands|Defense-system co-occurrence syndromes and defense islands]]

- Run the proposed comparison of R-M Type II-only species against species with both systems, then phage-challenge experiments in E. coli or B. subtilis. This would test the layered-defense hypothesis.
- Check whether the co-occurring pairs sit physically near each other in genomes. Species-level co-occurrence does not show co-location, so this would link the syndromes to defense islands.
- Repeat the CRISPR-Cas × CBASS test at finer taxonomic levels. This would show whether the lack of association holds beyond phylum-level stratification.

## [[concepts/depth-and-hydrogeological-zonation-of-subsurface-microbial-communities|Depth and hydrogeological zonation of subsurface microbial communities]]

- Test the plume explanation directly. Add measured contaminant concentrations per segment as a covariate in a PERMANOVA that includes zone. This would show whether zone adds explanatory power beyond contamination.
- Re-fit the well term with a design that nests depth within well. This would check whether the non-significant well effect is only a small-sample result, given 37 segments.
- Compare VZ and VSZ directly with SZ1 and SZ2 in pairwise zone contrasts. This would show which boundaries drive the zone effect.
- Check the shallow versus deep phylum trends in an independent set of cores. Only one dataset supports them.

## [[concepts/disagreement-among-deltag-estimation-methods|Disagreement among deltaG estimation methods]]

- Check whether the 840 sign-reversing and 311 extreme-change reactions cluster in multi-protic compounds. This would link the tail to the pKa divergence pattern.
- Compare the Marvin–OPAM2 and eQuilibrator–dGPredictor differences on the same reaction set. That would make the 7x ratio directly comparable.
- Validate OPAM2 and Marvin pKa values against experimental pKa measurements, which this study did not do.
- Test whether the sign-reversing reactions change flux predictions under realistic concentration bounds.

## [[concepts/distance-decay-of-environmental-embeddings-with-geographic-distance|Distance-decay of environmental embeddings with geographic distance]]

- Fit decay curves per environment category (soil, marine, freshwater, gut, clinical) rather than two groups, to see whether the 3.4x and 2.0x ratios hide further structure. This addresses the coarse two-way split.
- Add pair counts or confidence intervals for the stratified ratios. Only the pooled bins have reported pair counts, so the stratified ratios cannot be assessed for uncertainty.
- Compare embedding decay with community-composition decay for the same sites, to test whether embeddings track what selects microbes.
- Test whether the >5,000 km plateau comes from embedding saturation or from real environmental convergence, for example by controlling for latitude or biome.

## [[concepts/dna-versus-rna-pool-sensitivity-to-environmental-perturbation|DNA versus RNA pool sensitivity to environmental perturbation]]

- Repeat the paired DNA/RNA design across several seasons. This would test whether a transient RNA lead exists that a single timepoint cannot show. [src: harvard_forest_warming]
- Collect direct (non-incubated) organic-horizon DNA and RNA. This would remove the horizon × incubation confound that limits the organic DNA analysis. [src: harvard_forest_warming]
- Quantify transcripts by read mapping (TPM) instead of contig annotation counts. This would test whether assembly bias hides RNA treatment variance. [src: harvard_forest_warming]
- Apply the same pipeline to the Roy Chowdhury et al. data. This would test whether the tension with their larger transcript effect comes from method or from sampling. [src: harvard_forest_warming]
- Compare unheated and recently heated plots. This would test whether the compositional-turnover explanation depends on warming duration. [src: harvard_forest_warming]

## [[concepts/documentation-discovery-and-currency-gaps-in-lakehouse-catalogs-and-tooling|Documentation, discovery and currency gaps in lakehouse catalogs and tooling]]

- Apply the schema page and the `berdl` NMDC module, then measure whether new NMDC projects reach the right resource faster. This would test whether the documentation fixes work.
- Add currency and provenance annotations to `berdl_inventory.py` output, so disambiguation is dynamic rather than only documentary.
- Diff `nmdc.metadata` and `nmdc.ncbi_biosamples` against live upstream record counts to quantify completeness lag. This would close the snapshot-only caveat.
- Check whether the dangling `protocol_id` and the partial `enigma_coral` schemas have comparable catalog-level flags. This would show whether gaps beyond NMDC need the same fixes.

## [[concepts/domain-based-marker-detection-and-annotation-method-bias|Domain-based marker detection and annotation-method bias]]

- Re-run DISARM, Gabija and retron calls with multi-Pfam plus gene-order rules. Compare core, accessory and singleton fractions with the single-Pfam results, to test the prediction that the qualitative conclusions hold.
- Repeat the 96 % versus ~55 % CRISPR comparison for other defense systems. This would show which eggNOG description classes over-count.
- Tabulate stored ID formats (versioned, unversioned, names) for every domain table in the lakehouse, to prevent zero-hit queries.
- Test the reduced-profile-set explanation for the bakta gap by comparing the Pfam HMM versions and set sizes each tool uses.
- Rebuild the PHA synthase class analysis with the accession-to-name mapping, then check it against InterProScan.
- Search the 4,572 DUF4041 clusters for PF13455 with InterProScan instead of eggNOG, to test whether the 54 Mug113 co-annotations undercount SNIPE nuclease domains.
- Re-score nitrogen fixation and CWDE presence per species as the union of InterProScan and Pfam LIKE hits, to see how the 4,217 added species shift the core/accessory fractions.

## [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts|Dual-nature plant-associated bacteria and the validity of marker-based cohorts]]

- Add near-pure beneficial and near-pure pathogenic organisms to the validation panel. This would test whether any marker panel can separate the classes.
- Enlarge the ground-truth panel beyond 7 vs 7, and re-test the pathogenicity ratio with genome size and phylogeny as covariates. This would show whether p = 0.027 survives.
- Run RNAseq or use existing transcriptomes for dual-nature species under beneficial and pathogenic conditions, to separate real lifestyle flexibility from annotation artifacts.
- Compare dual-nature rates under several alternative scoring weights for NB07. This would measure how much the 25.2% depends on arbitrary weights.
- Re-run the non-plant negative controls and the neutral ground-truth species with the refined 17-marker panel, to see whether the misclassification of neutral species persists.

## [[concepts/ecological-and-phenotypic-grounding-of-gene-flow-signatures|Ecological and phenotypic grounding of gene-flow signatures]]

- Query MGnify per-sample taxa-coverage matrices to test the biome associations at finer resolution. This addresses the 28% categorical coverage limit.
- Re-test the mycobacterial soil null with a species set less skewed toward clinical isolates. This would check the explanation given for the failure.
- Add phenotype data for Cyanobacteriia beyond BacDive's n=4 species. This would close the one clade lacking a phenotype anchor.
- Test the direction of causation, for example by comparing gain timing with niche occupancy. This targets the unresolved causal question.

## [[concepts/ecological-memory-and-historical-contingency-in-serially-passaged-communities|Ecological memory and historical contingency in serially passaged communities]]

- Add more replicates or Round 3 passages to the fungal ITS design. This would test whether the p=0.090 result reflects low power or absent memory.
- Run a reciprocal switch or longer passage series. This would show whether the roughly 0.50 memory index decays with further passaging.
- Compare taxon-level changes between L and LC histories. This would test whether retained R1 OTUs carry the history signal.
- Inoculate copiotroph-enriched communities into lignin-only conditions. This would test the priority-effect hypothesis directly.

## [[concepts/ecosystem-differentiation-of-community-metabolic-potential|Ecosystem differentiation of community metabolic potential]]

- Resolve the habitat of the 61 Unknown samples using ENVO annotations or study-level metadata, then test whether finer niche structure appears.
- Re-run the amino acid pathway comparisons after residualizing PC1, or within ecosystem strata. This would show whether the 17/18 differences survive control for carbon range.
- Test whether PC2 sub-clusters within Soil correspond to soil subtypes. This would give the amino acid loadings an ecological label.
- Compare genome-predicted completeness with measured metabolites or activity in the same samples. This would address the limit that the analysis stops at predicted potential.

## [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing|Ecotype-aware per-patient phage cocktail design and state-dependent dosing]]

- Run a prospective cohort with serial samples, paired M. gnavus qPCR and metagenomics. This would test the 5-fold trigger and the n=1 drift rule, and give visit timing.
- Query INPHARED and IMG/VR for H. hathewayi and M. gnavus lytic phages, to close the phage gaps behind the hybrid design.
- Add AIEC strain-resolution diagnostics for E. coli-positive patients, to test the assumed AIEC prevalence.
- Measure per-patient bile acids, to replace the ecotype-level F. plautii cost.
- Compare calprotectin cutoffs around 250 μg/g against pilot clinical response.
- Replicate the strategy distribution in a larger multi-center CD cohort.

## [[concepts/effect-of-pka-source-on-flux-predictions-across-diverse-organisms|Effect of pKa source on flux predictions across diverse organisms]]

- Repeat the 10-organism comparison on minimal-media gapfilled models, to test whether the complete-media caveat hides larger Marvin-versus-OPAM2 effects.
- Report LP-relaxed FVA blocked-reaction counts for all 10 organisms in a table. Only E. coli and B. subtilis are tabulated, and this would settle the apparent mismatch with the newly blocked reactions seen in P. putida.
- Enumerate alternate optima, for example by sampling, for E. coli and P. putida. This would test whether the 1–10 kJ/mol deltaG shifts only select between equivalent optima.
- Check rxn00499 and the transport-coupled reactions in non-Proteobacteria. This would test whether the recurring affected reactions are specific to one lineage.

## [[concepts/engraftability-and-lung-adaptation-of-candidate-commensals|Engraftability and lung adaptation of candidate commensals]]

- Measure persistence directly, for example by sampling patients after a probiotic trial. This would test whether the prevalence-based score predicts colonization.
- Add respiratory isolation-source metadata for more genomes. This would test whether the 33–38% lung fractions hold beyond 21 lung genomes.
- Test whether the 8-genome Neisseria mucosa clade, with 1 respiratory genome, differs in airway fitness from the other genomes of the species.
- Look for engraftment-supporting strategies or substitutes for Micrococcus luteus. This would address the coverage-versus-persistence tension.

## [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform|Entity-class depth and data volume of a biological data platform]]

- Re-count each headline table with COUNT(DISTINCT) on its natural key. This would show which row totals overstate distinct entities, a gap left by the COUNT(*) approach.
- Add a distinct-genome count for each sample and community table. This would show how much of the 293,059-genome pangenome the community data can be linked to.
- Repeat the inventory at a later date. This would show how fast each class grows, since the UniRef counts are tied to a 2026-01 snapshot.
- Check the report's data_volume rows against the pitfalls row counts for tables such as genome_ani, eggnog_mapper_annotations and genefitness. This would confirm that the two sources use the same counting rules.

## [[concepts/environment-dependent-resistance-mechanism-composition|Environment-dependent resistance mechanism composition]]

- Recompute the efflux fractions and η² from the species-level data to settle the gap between 7.0% and 21% for human gut. This would show which definition of efflux each figure uses.
- Rerun the mechanism fractions with the 15,550 unclassified clusters as a separate category, or reclassify them with sequence-based annotation. This would test whether the exclusion biases the environment contrasts.
- Test whether the soil and aquatic metal-resistance signal holds after controlling for sampling depth and phylogeny. This would separate selection from taxonomic composition.
- Compare site-level metal and antibiotic concentrations with mechanism fractions, where the metadata exist. This would test the selective-pressure interpretation directly.

## [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance|Environmental and clinical distribution of antimicrobial resistance]]

- Use nmdc_arkin metagenome taxonomic profiles to infer community AMR load from species AMR profiles. This would test whether species-level findings hold in real environmental communities.
- Map AMR gene prevalence in NMDC/MGnify communities. This would show whether the accessory AMR genes seen in isolates are also prevalent in community DNA.
- Redo the clinical-exposure test per genome with Fisher's exact test within species. This would replace the species-level proxy.
- Repeat the environment comparisons with sampling-bias correction, for example down-weighting over-sampled pathogens. This would show how much of the clinical excess is a database artefact.

## [[concepts/environmental-association-of-lanthanide-dependent-methanol-oxidation-genes|Environmental association of lanthanide-dependent methanol oxidation genes]]

- Recruit REE-mining tailings, leachate and bioreactor metagenomes from existing sequence archives. This would test whether REE supply per se selects for the cassette and could make the REE-impacted signal inferential.
- Fit a phylogeny-aware mixed model of xoxF carriage on environment class, using that larger REE-impacted collection. This would replace the within-phylum stratification.
- Run a coverage-restricted AlphaEarth embedding analysis on the 1,457 xoxF genomes that have coordinates. This would show whether embedding-based niches agree with the text-mined classes.
- Re-run the class tests with a finer split of host_associated (gut, skin, oral, infection). This would check whether the broad class hides any methylotrophic niches.

## [[concepts/environmental-biome-enrichment-of-mobile-cazy-gene-content|Environmental biome enrichment of mobile CAZy gene content]]

- Run the housekeeping gene null baseline to test whether biome ORs exceed those expected for non-mobile genes.
- Compute θ for each biome (marine sediment, barley rhizosphere, maize rhizosphere). This would separate joint T4SS-CAZy enrichment from the enrichment of each component alone.
- Run the synteny threshold permutation test on Spark unfiltered data. This would show whether the ORs depend on the threshold chosen.
- Report q-values for the rhizosphere ORs, and compare the pattern with [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs]].

## [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density|Environmental drivers of genus niche breadth and metal-gene density]]

- Test the latitude suppressor with bedrock and temperature covariates together in one PGLS model, to see whether they jointly absorb the latitude effect. This addresses the fact that models B and C were fitted separately.
- Re-run NB28 variance partitioning with permutation testing and adjusted R², to see whether the metal-unique fraction (0.064) really exceeds pH+climate (0.041).
- Add the six missing TIER1 KOs (for example cusB, merR, cueR) from another annotation source to the per-KO driver analysis, to test metal specificity for Cu and Hg.
- Test the speciation hypothesis for pH niche by overlaying genus pH optima on metal-speciation pH curves, and by fitting metal-density × pH-specific bedrock interactions, including serpentine soils. Run it with SOM in the model, to separate speciation from SOM chelation.
- Expand the ore-deposit cross-reference beyond 18–19 regions, to see whether the weak correlations hold with more power.
- Repeat the SoilTemp model with more matched genera, to see whether β_metal regains significance.
- Test the Cr and Co signals against a direct redox measure in a region with Cr(VI) or mobile-fraction data, such as Europe (GEMAS) or Australia (NGSA).
- Test the serpentine/ultramafic mechanisms for the Cr signal (Ca/Mg ratio, soil structure, weathering rate) as covariates, since soil moisture did not mediate it.

## [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere|Environmental enrichment of plant-growth-promoting genes in soil and rhizosphere]]

- Re-run the soil comparison with a within-genus shuffle null, as was done for plant association, to see which soil-enriched genes (acdS, pqqC, hcnC) are species-level rather than genus-level signals. This closes the gap that only the plant-association study had that test.
- Refine soil labels using environmental ontology or metagenome-source metadata, to test whether the predicted underestimate of acdS and pqqC ORs holds.
- Stratify nifH by phylum and lifestyle (free-living versus symbiotic) to test the proposed explanations for soil depletion.
- Check ipdC depletion with alternative phylogenetic controls to see whether the phylum-level result is stable.

## [[concepts/environmental-niche-association-of-defense-system-carriers|Environmental niche association of defense-system carriers]]

- Map the 22 significant dimensions, starting with A19, to named variables using the AlphaEarth documentation. This would show which environmental factors separate SNIPE carriers from non-carriers.
- Repeat the carrier versus non-carrier test for the other defense systems and for whole defense repertoires, as the phage_defense_arsenal report proposes. This would show whether the SNIPE shift is typical or specific.
- Cross-reference defense repertoires with NCBI-env isolation source. This would test habitat specificity for genomes that AlphaEarth does not cover.
- Rerun the NMDC metagenome ecosystem breakdown with interactive queries. This would replace the 2-sample result with a usable independent check.
- Test whether the shift persists when restricted to environmental isolates. This would show whether the coverage bias drives the result.

## [[concepts/environmental-specificity-of-prophage-terminase-lineages|Environmental specificity of prophage terminase lineages]]

- Repeat the constrained-permutation test at several AAI thresholds between 50% and 80%. This would show whether the null result depends on lineage granularity.
- Rerun the test without host-family constraints, so the result can be compared directly with Paez-Espino-style habitat specificity.
- Test whether the 325 specialist lineages are enriched for their environments within host families. This would separate host ecology from environmental effects.
- Run the same enrichment test on modules and lineages with matched host controls, to check the proposed modular-exchange explanation.

## [[concepts/environmental-structuring-of-antimicrobial-resistance-gene-content|Environmental structuring of antimicrobial-resistance gene content]]

- Fit models with phylogeny and environment together, for example within-genus contrasts, to measure how much of the 2–13% environment effect survives. This addresses the modest η² and the phylogeny caveat.
- Rerun the planned PCoA and PERMANOVA on AMR mechanism composition. These were planned but not executed.
- Reclassify the Other/Unknown species, using AlphaEarth embeddings where available, to test whether the gradient holds beyond the well-classified half.
- Run the MAG versus isolate comparison and an archaea-specific analysis, to check for sampling-source bias.
- Use longitudinal or within-species strain data to test whether exposure or co-selection explains the clinical excess.

## [[concepts/environmental-structuring-of-prophage-gene-modules-beyond-host-phylogeny|Environmental structuring of prophage gene modules beyond host phylogeny]]

- Repeat the PERMANOVA with more than 99 permutations and the full species set, since 99 permutations on a 1,773-species subsample limits p to 0.01.
- Run the constrained null with finer taxonomic strata (genus instead of family) to test whether the human-associated enrichments survive.
- Test whether the human-associated enrichment reflects sampling of well-studied clinical taxa, by controlling for genome sampling depth per species.
- Test the modular-exchange hypothesis directly by comparing module phylogenies with host phylogenies for tail, head and anti-defense modules.

## [[concepts/environmental-variability-and-storage-polymer-pathway-enrichment-feast-famine-hypothesis|Environmental variability and storage-polymer pathway enrichment (feast/famine hypothesis)]]

- Run phylogenetic logistic regression of PHB presence on variability category, to test whether the association survives shared ancestry. This closes the gap named in the report's caveat.
- Re-annotate the "other_unknown" species using [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]], then repeat the chi-squared test to see whether the gradient sharpens.
- Replace the assigned high/moderate/low variability labels with measured temporal carbon-fluctuation data, for example from metagenome or soil time series. This tests variability directly.
- Compare PHB synthesis and depolymerase gene co-occurrence within the same genomes. This tests whether storage and mobilisation track together.
- Separate stress-resistance from feast/famine explanations by comparing PHB prevalence in stressful but nutrient-stable habitats against fluctuating but mild ones.

## [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content|Environmental versus phylogenetic drivers of gene content]]

- Repeat the partial-correlation analysis using embeddings only from environmental genomes, with NaN and institutional-address genomes filtered. This would test whether the weak environment effect is partly an artifact of the proxy.
- Subset gene content by function (COG categories such as V-Defense and L-Mobile). This would test the gene-subset hypothesis. See [[concepts/defense-and-mobile-element-gene-content-as-drivers-of-ecotype-differences]].
- Compare gene content between ecotype clusters within species. This would test adaptation within species.
- Repeat the reanalysis with ENVO terms from env_broad_scale. This would test whether classification error hides an environment effect.
- Test whether pathway variability explains within-species gene-content variation after phylogeny is removed. This would link the openness results to the environment/phylogeny decomposition.
- Use isolation_source homogeneity to separate field sites from institutional addresses in the flagged locations. This would close the heuristic gap noted in the report.

See also [[concepts/genome-gc-content-as-an-ecological-signal]].

## [[concepts/essential-genes-and-core-genome-conservation|Essential genes and core genome conservation]]

- Rerun the essential_genome analysis on expanded Fitness Browser coverage to test the 15 pan-essential families.
- Reconcile the 7,084 no-ortholog genes with the 4,683 orphan essentials by tracing which genes fall in each set. This would clarify the orphan definition.
- Recompute essential-gene core percentages for every report with both denominators (all genes versus mapped genes only), to separate real differences from denominator effects.
- Check whether the 49.5% core rate of orphan essentials reflects true accessory status or poor core classification in small clades, by comparing against clade size.
- Test whether essential-unmapped genes are divergent core-function variants or acquired genes, by comparing their sequences with core homologs.
- Repeat the enrichment test in the 15 organisms where it was not significant, to separate low power from a true absence of effect.

## [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens|Essential genes as a blind spot of transposon fitness screens]]

- Run CRISPRi knockdowns for the top 10 candidates (for example Keio:14796 in [[entities/escherichia-coli]]). This tests whether operon-context hypotheses predict phenotypes, which none of the evidence here has done.
- Repeat the weight-sensitivity analysis with orthogonal evidence. Rankings change substantially when neighbor context or tractability is dropped, and held-out knockdown results would show which dimensions carry real signal.
- Add the excluded essential genes to the conservation baselines as a separate category. This would quantify the core-enrichment bias directly, instead of only stating its direction.
- Find a way to give the 4,385 orphan hypothetical essentials a prediction route beyond module transfer, for example domain or neighborhood evidence.

## [[concepts/essentiality-and-annotation-caveats-in-transposon-based-resistance-gene-fitness-analysis|Essentiality and annotation caveats in transposon-based resistance gene fitness analysis]]

- Re-run the fitness comparison with fosfomycin and tellurite genes reclassified, to see whether the "unknown" mechanism group changes. This addresses the ~25 misclassified genes.
- Compute the essential-gene rate for AMR and non-AMR genes within the same organism set, to replace the cross-analysis comparison of 4.6% with ~14%.
- Test AMR genes inside operons against single-gene transcription units, to estimate how much polar effects contribute.
- Add fitness data from clinical pathogens carrying acquired mobile resistance, to close the environmental-strain gap.

## [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes|Field-only accessory gene content absent from cultured pangenomes]]

- Run the Mantel-like test described above, to separate uniform divergence from habitat-stratified gain or loss within genera.
- Annotate per-gene KOs for soil MAGs, starting with the five fully attrited genera. This would close the habitat-biased annotation gap and test the worst-case scenario directly.
- Repeat the module enrichment on a habitat-balanced cohort, or per habitat, to see which enriched modules persist outside water MAGs.
- Rerun enrichment excluding ribosomal KOs, to check that the niche-specific transport modules (rhamnose, nickel, oligopeptide) remain enriched without the is_core artifact.
- Test the 15 top candidate MAGs against [[entities/kbase-ke-pangenome]] cultured accessory content with other pangenome definitions. Check whether the broad ribosome and housekeeping enrichments are artifacts of incomplete cultured-pangenome coverage. See [[concepts/module-level-enrichment-artifacts-from-broad-substrate-enzymes]].

## [[concepts/field-relevant-versus-laboratory-fitness-as-a-predictor-of-gene-conservation|Field-relevant versus laboratory fitness as a predictor of gene conservation]]

- Repeat the stratified analysis in other organisms with field-like conditions to test whether the DvH result generalises. This closes the single-organism gap.
- Enlarge the specific gene sets, for example with a looser sickness threshold, and rerun the field-versus-lab test. This addresses the low power at n=50-52.
- Regress core status on fitness magnitude and condition class together, to separate magnitude from context given the r ~ 0.7 correlation.
- Re-run the classification with an independent second labeller to measure the effect of subjective edge-case calls.

## [[concepts/field-validation-of-metal-diversity-genera-in-contaminated-groundwater|Field validation of metal-diversity genera in contaminated groundwater]]

- Correlate per-sample CWM with covered-read fraction in PRJNA1084851. This closes the untested coverage bias.
- Run a power analysis, or use a larger groundwater set, for the fold-enrichment test. This would separate a breadth effect from low power.
- Run the proposed site-level test on MicrobeAtlas metadata for mining-impacted, biosolid-amended and estuarine samples against clean references.
- Improve SILVA-to-GTDB genus matching, then re-check the Citrobacter and Thermodesulfovibrio non-detections. See [[concepts/taxonomy-bridging-between-metagenomic-classifiers-and-reference-pangenomes]].

## [[concepts/fitness-cost-of-antimicrobial-resistance-genes|Fitness cost of antimicrobial resistance genes]]

- Measure the same AMR knockouts under sub-inhibitory antibiotics, to test the cost-versus-benefit flip that this page does not cover. See [[concepts/antibiotic-dependent-fitness-flip-of-resistance-genes]].
- Repeat the core-versus-accessory comparison only in species with hundreds of genomes (such as K. michiganensis, B. thetaiotaomicron, S. meliloti). This would remove the sampling-depth caveat.
- Add fosfomycin and tellurite rules to the Tier 2 classifier and re-run the mechanism tests. This would show whether the ~25 "unknown" genes change the null.
- Compare cost in recently acquired plasmid or prophage-borne genes with chromosomal ones, to test the compensation and donor-optimization hypotheses and to revisit H3 as fitness coverage grows.
- Calibrate RB-TnSeq differences against isogenic competition assays for a few resistance genes. This would close the measurement-scale gap.
- Relax the 100% identity link threshold, for example to near-identical alleles, and check whether AMR fitness effects change.

## [[concepts/fitness-data-coverage-gaps-for-defense-genes|Fitness-data coverage gaps for defense genes]]

- Curate the external K. pneumoniae Tn-Seq datasets from the report's plan, and test whether any covers a natural SNIPE carrier. This would close the Klebsiella gap.
- Rerun the PF13250 and PF13455 queries against the Fitness Browser tables in the KBase Data Lakehouse now that the API outage may be over. This would confirm that M. maripaludis is the only full-architecture carrier.
- Check whether the six PF13455-only organisms show nuclease-domain phenotypes. This would add comparators to the single archaeal gene.
- Build mutant libraries in K. pneumoniae NCTC9140 or HS11286 to test SNIPE and ManYZ phenotypes under phage challenge. See [[concepts/adsorption-receptors-versus-defense-systems-as-determinants-of-phage-host-range]].

## [[concepts/fitness-measurement-of-novel-singleton-genes-and-assay-limits|Fitness measurement of novel singleton genes and assay limits]]

- Test whether singleton genes with poor transposon coverage differ in mean fitness from well-covered ones. This would separate missing data from true neutrality.
- Repeat the singleton analysis with gene length as a covariate or in length-matched sets. This would show how much of the near-zero signal comes from short genes.
- Check strong phenotypes of dark genes for polar effects by looking at neighbouring genes in the same operon.
- Extend the analysis to organisms outside Proteobacteria and to niche-relevant conditions. This would address the coverage and condition biases.

## [[concepts/fitness-modules-essential-genes-and-condition-specific-gene-function|Fitness modules, essential genes and condition-specific gene function]]

- Measure NDH-2 mutant growth on glucose and acetate in ADP1. This would replace the prediction with data (the gap in the NDH-2 claim).
- Test whether ACIAD3137 and ACIAD2176 physically interact with Complex I, for example by co-purification, to follow up on their cofitness.
- Rerun the cross-species NDH-2 test with sequence-validated NDH-2 calls, such as profile-based ones, to check the null result against the earlier misannotation problem.
- Profile ACIAD3522 on more acetate-related and NADH-linked conditions to narrow its unknown reaction.
- Add respiratory-chain and cofactor reactions to the FBA model, then test whether threshold effects can be captured.
- Test whether the 1,382 module-transfer predictions for hypothetical essential genes hold up, for example by conditional knockdowns, to check a result that has no direct validation here.
- Rebuild module families with ortholog graphs from additional organisms, to see whether the 156 families keep growing as the graph densifies.

## [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer|Function prediction for uncharacterized genes by guilt-by-association and ortholog transfer]]

- Characterize the orphan essentials (mobile elements, recent acquisition, evolutionary rate), since orphans are the group this method cannot reach.
- Test the module-transfer predictions by CRISPRi knockdown under module-predicted conditions. This would show whether diverged function limits them.
- Benchmark module-based predictions at the biological-process level, for example with pathway-level labels. The KO-level benchmark cannot credit modules.
- Extend the held-out benchmark to essential-gene transfer, which these reports do not benchmark on withheld labels.

## [[concepts/function-specific-burden-of-core-genes|Function-specific burden of core genes]]

- Test the natural-environment hypothesis directly. Compare burden in the motility, RNA and protein categories across lab conditions that approximate natural settings. This would show whether the offsetting benefit exists.
- Explain the cell wall reversal. Find which non-core cell wall genes carry the burden and whether they are mobile or strain-specific.
- Extend the category analysis to more functional categories and organisms. Check whether the three enriched categories hold beyond the Fitness Browser set.
- Compare burden in core AMR genes with the three enriched categories in one model. This would show whether AMR neutrality is a category effect.

## [[concepts/functional-annotation-of-amr-genes-and-mechanism-classification|Functional annotation of AMR genes and mechanism classification]]

- Map bakta_db_xrefs cross-references to CARD ARO terms, replacing the keyword scheme. Then measure how far the 22% Other/Unclassified fraction falls.
- Test whether the 15,550 unclassified clusters in the environmental resistome report are distributed non-randomly across environments. This would show whether the exclusion biases the H3 mechanism fractions.
- Add fosfomycin and tellurite rules to the Tier 2 classifier and rerun the mechanism-level fitness comparison.
- Cross-reference AMR proteins with AlphaFold/PDB structures to identify novel resistance folds among poorly annotated clusters.

## [[concepts/functional-characterization-of-plant-enriched-gene-families|Functional characterization of plant-enriched gene families]]

- Measure oxygen tolerance ranges in plant-associated versus non-plant strains. This would test the microaerobic-adaptation hypothesis for COG1845 and COG0843.
- Run AlphaFold structural prediction, or cross-reference pathway databases, for COG3569, COG1845, COG0843 and COG0316. This would turn their broad classifications into testable plant-interaction mechanisms.
- Test the 19 category-S OGs experimentally, for example with mutants in root colonization assays. This would address the missing mechanism for characterized domains.
- Compare enrichment of the cbb3 oxidase OGs between nodule-forming and other plant-associated species. This would show whether the signal tracks microaerobic niches.

## [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks|Functional composition of antimicrobial-resistance cofitness support networks]]

- Repeat the enrichment at |r| > 0.4 and 0.5, where networks are smaller, to test whether the flagellar and biosynthesis signals survive removal of weak associations.
- Compare AMR partners with non-AMR genes matched for dispensability, to separate shared lab dispensability from co-regulation.
- Test histidine-biosynthesis specificity for efflux genes in more organisms, since the q = 0.18 result is not significant.
- Add organisms from varied ecologies, and non-Pseudomonas lineages, to check whether the pattern generalizes.
- Measure proton motive force directly in motility and biosynthesis mutants, to test the competition hypothesis.

## [[concepts/functional-differentiation-of-gene-content-ecotypes-across-cog-categories|Functional differentiation of gene-content ecotypes across COG categories]]

- Test whether specific categories such as V (defense) and L (mobile) show stronger environment effects, using environment metadata per genome. This would show whether category-level differences track environment.
- Compare gene content between ecotype clusters within species that have identified ecotypes, linking clusters to isolation source. This would show whether ecotypes are ecological.
- Repeat the adaptive-versus-housekeeping contrast with alternative clustering methods and a silhouette threshold. This would show whether the 2.1x ratio survives different cluster separation.
- Compare effects with and without categories S and L, which have the largest effects but are not classed adaptive. This would show whether the contrast depends on category assignment.
- Compare these results with [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]]. This would separate phylogenetic from ecological structure.

## [[concepts/functional-gene-responses-to-soil-warming|Functional gene responses to soil warming]]

- Run the cross-study meta-analysis with the SPRUCE peatland and Alaskan permafrost NMDC studies. This closes the single-site gap for the methanotrophy signature.
- Track pmoA/pmoB to specific MAGs in the 298-MAG cohort. This would show which taxa carry the signal.
- Test the ruderal-subset hypothesis against Choudoir et al. 2025 pangenome data.
- Test the methanotrophy and glyoxylate KOs as a pre-specified small set rather than across 14K KOs. This would reduce the multiple-testing burden that blocks FDR significance.

## [[concepts/functional-redundancy-versus-complementarity-among-co-occurring-genera|Functional redundancy versus complementarity among co-occurring genera]]

- Re-run the complementarity test at reaction level or on substrate-specific subsets, to see whether the small redundancy effect hides complementarity that 80 pathways cannot resolve.
- Run the deferred sensitivity analysis on the 62 unmatched NMDC genera, for example by testing alternative taxonomy bridges. This would show whether missing partners make the redundancy signal artifactual.
- Test complementarity with a relaxed or graded GapMind completeness threshold, to see whether the 0% core-level result changes the effect.
- Apply the same corrected formula (raw pair-level SD) and prevalence-weighting to other habitats or datasets. This would show whether |d| ≈ 0.4 is general or specific to NMDC soil.
- Use a dataset with more PGP-only genera to run the PGP–pathogen C-score test, since NMDC cannot power it.

## [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform|Funding-agency and topic coverage of a shared data platform]]

- Verify the evaluation and lambda tenant-to-agency mappings against program documentation. This would close the only unmapped gap.
- Re-run the agency × topic analysis weighting by rows or data volume rather than table count. This would test whether ENIGMA SDT/DDT structure inflates field_observational.
- Run a DOE-BER-anchored analysis and validate it on Planet Microbe, NETL and USGS samples. This would test the proposed external-validation role.
- Compare the tenant synergy scores with actual cross-tenant queries. This would test whether high-entropy tenants are used more broadly.

## [[concepts/fungal-community-responses-to-lignin-and-labile-carbon|Fungal community responses to lignin and labile carbon]]

- Rerun the Round 2 fungal enrichments with more replicates, to test whether Pleurotus in LC-LC and Malassezia dominance recur. This would address the 0.99–1.00 within-group BC.
- Add a quantitative fungal measure alongside ITS relative abundance, such as qPCR or lignin-loss assays. This would show whether Fusarium and Fusicolla, or Chrysosporium and Aspergillus, actually degrade lignin, rather than inferring lifestyle from genus.
- Sequence deeper or pool replicates to see whether the 3–8 OTU groups reflect real selection or stochastic sampling.

## [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion|Fur derepression and transcript buffering by regulator co-deletion]]

- Make the two Δlpxc crosses above (Δfur alone, ΔsspB alone) in the Ryan-lab background to test both arms of the switch directly.
- Measure fitness or transcripts under iron limitation to separate real iron-limitation responses from constitutive derepression.
- Perturb the cbb3/fix respiratory chain genetically in the rescued strain to test the respiratory-ATP hypothesis, which the existing fitness data cannot.
- Test whether iron-uptake transporters such as ChvT and HutA take part in CPG trafficking, which the report does not demonstrate.

## [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation|Gene fitness importance as a predictor of pangenome conservation]]

- Test the 5,526 costly and dispensable genes for mobile-element annotation and recent acquisition, to settle whether they are genes being lost. See mobile element origin of costly non conserved genes.
- Link laboratory fitness to AlphaEarth environmental data, to ask whether organisms from more variable environments carry more core trade-off genes.
- Repeat the module-breadth test in a set with a lower baseline core rate, to see whether the ceiling effect hides a gradient.
- Compare lab-defined costly-conserved genes with field-relevant fitness, to test the purifying-selection interpretation. See [[concepts/field-relevant-versus-laboratory-fitness-as-a-predictor-of-gene-conservation]].
- Rerun the DvH analysis with the fraction of genomes carrying each gene cluster and with continuous fitness scores, to see whether the weak prediction (CV-AUC near 0.5) reflects coarse binary inputs.
- Rerun the pathway condition-type stratification against a null that permutes condition labels, to separate real triggers from inevitable threshold crossing.

## [[concepts/gene-loss-and-black-queen-hypothesis-tests|Gene loss and Black Queen hypothesis tests]]

- Run a per-gene presence/absence analysis across a phylogeny for latent pathways. It would close the gap left by the pathway-level measure, which cannot see partial erosion.
- Compare costly+dispensable gene presence across strains of one species with close relatives. It would show whether these genes are being lost or only acquired.
- Join ENIGMA CORAL community composition to per-organism counts of costly+dispensable genes. It would test the public-goods premise directly.
- Repeat the latent-fraction versus openness test within single lineages. It would check whether the species-level null hides a within-lineage signal.
- Annotate the 5,526 genes for mobile-element features. It would settle whether they are selfish elements or metabolic genes.

## [[concepts/gene-metabolite-association-discovery-in-small-exometabolomic-datasets|Gene-metabolite association discovery in small exometabolomic datasets]]

- Run permutation tests on the 940 associations at n=6 to estimate how many |r| > 0.7 hits arise by chance. This would show how many associations are real.
- Check whether associated KOs are confounded with strain phylogeny. This would separate mechanism from relatedness.
- Test the associations on a larger exometabolomic dataset with more strains. This would show whether they hold beyond six strains.
- Compare the 156-KO Fitness Browser-cognate feature set with an unrestricted KO set. This would show what the filter contributes.

## [[concepts/generalizability-limits-of-planktonic-single-strain-inhibition-assays|Generalizability limits of planktonic single-strain inhibition assays]]

- Repeat the inhibition assays with ExoS+ CF *P. aeruginosa* isolates alongside PA14. This would show how far the minority-variant result transfers.
- Run the proposed CFBE biofilm challenge with 48-hour CFU and biomass readouts. It would test whether planktonic inhibition predicts biofilm disruption.
- Extend the substrate panel to N-acetylglucosamine, polyamines, iron limitation and pH 6.5. It would close the nutrient gap.
- Collect growth kinetics beyond the 32 isolates, rather than endpoint OD, to replace the GC-confounded CUB proxy.
- Refit the overlap–inhibition model on a cohort balanced for genus. It would show how R² changes for under-represented taxa.

## [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance|Genome-encoded metal resistance repertoire versus phenotype as predictor of metal tolerance]]

- Test the gene-count model against measured tolerance (for example MIC or growth data) to remove the circularity of genome-derived scores.
- Add regulatory or expression features to the gene-count model and check whether they improve on the repertoire in fitness data.
- Repeat the model comparison in other datasets and with other phylogenetic blocking levels, to see if the +0.28 gain holds.
- Recompute the gene-count-only versus phenotype-only comparison to resolve the gap between the table and the variance statement.

## [[concepts/genome-gc-content-as-an-ecological-signal|Genome GC content as an ecological signal]]

- Rerun the test with sampling geography or study of origin as a random effect in more species. Only 16 species had enough geo-bearing genomes, so this would test the confounding caveat. [src: gc_ecotype_ecology]
- Run the GC and gene-content tests on the same species with matched controls. This would show whether the contrast comes from the trait or from the species sets. [src: gc_ecotype_ecology]
- Test whether the largest effects, such as in *Klebsiella quasipneumoniae*, track recombination rate or oxidative niche. This would turn the proposed explanation in [src: gc_ecotype_ecology] into a measured one.
- Expand the jointly testable set beyond 17 species, so the 59% overlap of the two environment definitions is better estimated. [src: gc_ecotype_ecology]
- Repeat the *B. vietnamiensis* two-definition test in other ecotype-spanning species, such as *V. parahaemolyticus*, to see whether the agreement of isolation source and embeddings holds beyond one species. [src: gc_ecotype_ecology]

## [[concepts/genome-predicted-pathway-completeness-and-community-metabolite-chemistry|Genome-predicted pathway completeness and community metabolite chemistry]]

- Pair metatranscriptomics with metabolomics in a subset of NMDC samples. Compare expressed pathway completeness, genomic potential, and metabolite abundance to test whether expression, not just gene presence, drives the BQH signal.
- Improve KEGG compound annotations in metabolomics_gold for cysteine, histidine, and lysine. This would expand the H1 test set from 13 to 16 testable pathways and add statistical power.
- Add samples with methionine measurements. The strongest effect (n = 18) is underpowered, and more samples would show whether it holds.
- Measure chorismate or downstream products directly. This would replace the upstream intermediate proxies and settle the near-zero chorismate result.
- Rerun the correlations under alternative representative-clade choices and with frac_likely_complete. This would check the robustness of the signal.

## [[concepts/genome-sampling-depth-and-downsampling-effects-on-partial-correlation-estimates|Genome sampling depth and downsampling effects on partial correlation estimates]]

- Compare downsampled and full-genome extraction on the same species to explain the 27x magnitude discrepancy.
- Add genome count as a covariate to test whether species with more genomes have inflated correlations.
- Re-extract Klebsiella pneumoniae in chunks to avoid the Spark limit, to test whether the largest clinical species changes the group comparison.

## [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations|Genome sampling depth, genome size and phylogeny as confounders of gene-content and pangenome associations]]

- Run PGLS or phylogenetic mixed models on a GTDB species tree for the CAZyme biome effects, to replace within-phylum stratification and test independence from phylogeny.
- Redo the CAZyme cloud-fraction analysis with rarefaction to equal genome counts per species, to test whether any biological openness signal remains beyond ρ = 0.101.
- Build the rarefaction curve over several species-per-genus thresholds from a genome-count-stratified AMR table, to quantify the coverage-depth effect.
- Add genus-level pangenome openness alongside metal type diversity, to test whether the accessory genome drives both niche breadth and metal diversity.
- Add genome count as a covariate in the ecotype reanalysis, and compare the downsampled (max 250) and full (up to 3,505) sets.
- Replace connected-components control with an alternative phylogenetic control for species with few clusters but many genomes, such as E. faecium.
- Repeat the PHB niche-breadth and enrichment tests with phylogenetic logistic regression alongside genome size, to see whether the sign reversal and quartile enrichment hold beyond Spearman partial correlation and stratification.
- Fit a tree-based phylogenetic mixed model for the plant-association markers using a reduced or sparse covariance, to test the cassette-level tier against the genus-cluster approximation.
- Rerun the within-genus label shuffle with several thousand permutations and a multiple-testing correction, to settle whether T3SS survives.
- Run a partial PERMANOVA on the prophage module data with phylogeny and genome size entered together, to estimate the unique variance explained by environment.

## [[concepts/genome-size-and-taxonomic-composition-confounding-of-cultured-versus-mag-functional-comparisons|Genome-size and taxonomic composition confounding of cultured-versus-MAG functional comparisons]]

- Rerun the KO enrichment test within shared phyla (for example Pseudomonadota) with size-matched genomes. This would show how many of the 7,669 cultured-enriched KOs survive once genome size is controlled.
- Recompute the 813 MAG-enriched KOs after dropping Patescibacteria. This would test the prediction that the functional gap narrows.
- Re-score KO absence using only MAGs above a high completeness threshold, or with a completeness-weighted model. This would bound the false-positive and conservative-estimate effects of incompleteness.
- Annotate the 623 ORFRC MAGs and compare them with the ENIGMA isolates. This would separate geography from cultivation bias.

## [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists|Genome streamlining and genome size in ecological specialists]]

- Break down the extra Bacillota_B gene fraction by COG and KEGG pathway to see whether it is mobile-element accessory operons, sporulation regulons or anaerobic-respiration accessories. This would close the open question of where the extra ~1 Mbp sits.
- Repeat the per-Mb niche-breadth analysis within Bacillota_B alone, so the genus-level streamlining baseline can be compared with the within-phylum expansion.
- Use a larger or independent deep-clay anchor set than n=10 to test whether the size difference holds.
- Rerun the genome-size attenuation permutation with a more informative design, since the current CI [43.9%, 318.2%] is too wide to be decisive.
- Fit the proposed compaction-index model to partition the metal-gene β into streamlining-driven and metal-content-specific parts, which would test the selective-retention interpretation.
- Run a genome-size-partitioned analysis of carbohydrate KO density and GapMind breadth together, and a size-matched-phyla cultured-versus-MAG comparison, to close the gaps the reports leave.

## [[concepts/genome-type-and-sampling-bias-in-metagenome-assembled-genome-surveys|Genome-type and sampling bias in metagenome-assembled genome surveys]]

- Run the quality-restricted copy-number rerun described above, to close the gap that completeness and N50 are not conditioned on.
- Repeat the isolate-versus-MAG comparison on individual CAZyme families, not just totals, to test whether absolute undercounting exists.
- Fill the missing per-gene coverage for soil MAGs, or reweight by habitat, to test whether the NEON H4b enrichment list survives outside the water-skewed cohort.
- Compare ORFRC isolates with MAGs from the same site, to separate geography from cultivation bias.
- Sample the rare biomes more deeply, or use resampling, to find which biome contrasts have adequate power.

## [[concepts/genomic-discovery-gap-indices-and-database-representation-bias|Genomic discovery gap indices and database representation bias]]

- Rerun GDI from raw data with rarefied 16S depth and bootstrap CIs. This would show whether the biome differences exceed the noise in the index.
- Plot richness against completeness per 1° bin as a 2D scatter. This would show whether the richness term alone drives the high-GDI bins.
- Stratify by the number of 16S samples per pH bin before computing GDI. This would test whether the alkaline gap reflects sampling effort or real assembly gaps.
- Test the index on a case with zero genomes to define its floor behaviour. This addresses the formula's value of 902 at zero completeness.

## [[concepts/genus-level-aggregation-tree-choice-and-trait-distribution-assumptions-in-phylogenetic-comparative-analyses|Genus-level aggregation, tree choice and trait distribution assumptions in phylogenetic comparative analyses]]

- Refit the PGLS and Pagel's λ analyses on an NCBI tree, a SILVA-based 16S tree and a different GTDB release. This would close the untested tree-sensitivity gap. A 16S tree would also show whether matching the niche breadth data changes the results.
- Compare genus-representative pruning with species-level or multi-tip-per-genus trees. This would show how much within-genus structure matters.
- Inspect PGLS residuals for normality. Then fit the reverse regression with `MCMCglmm` or `phylolm` using Poisson or negative binomial families.
- Compare Brownian-motion λ for metal_types with Mk or threshold models. This would test how much the Gaussian approximation distorts the integer trait.
- Run the M19 Pfam-family cluster bootstrap. Then check whether the 95% CIs on per-leaf Sankoff Cohen's d support dropping PIC.

## [[concepts/genus-level-amplicon-resolution-and-rare-taxon-limits-in-matching-reference-organisms-to-field-data|Genus-level amplicon resolution and rare-taxon limits in matching reference organisms to field data]]

- Test whether metagenomic data in ENIGMA CORAL genome or assembly tables allow species- or strain-level matching to FB organisms. This would address the genus-only limit.
- Repeat the *Desulfovibrio*–uranium test with deeper or targeted sequencing, since rarity currently makes it unreliable.
- Extend species-level biogeography beyond the 20 verified pangenome-linked strains by widening verified GTDB matches.
- Add *Rhodanobacter* to the FB and compare its fitness with its field abundance. See [[concepts/laboratory-fitness-as-a-predictor-of-field-abundance]].

## [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits|Genus-level taxonomy bridging to pangenome clades and its coverage limits]]

- Quantify how much the unmapped ENIGMA genera (862 of 1,392) contribute to contamination gradients, to size the gain from expanding the bridge.
- Build a species or strain-level bridge from metagenomes or an ASV reclassification pipeline, and measure gains over genus and species-proxy modes.
- Run the deferred sensitivity analysis of the 80.7% NMDC genus match in the plant microbiome work, including whether the 62 lost genera hold complementary partners that would change the H3 redundancy signal.
- Test whether the choice of representative clade for ambiguous genera such as pseudomonas shifts results beyond the ~6.5% bound.

## [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure|Geochemical and contamination-plume control of subsurface community structure]]

- Load the 221 registered SSO geochemistry samples into CORAL and test the predicted NE→SW gradient directly. This closes the gap that all environmental inference is currently from community composition.
- Obtain EU/ED well metals and pump-test ASV data from L8, M5 and U2. These test the northeast plume source and the M5 Rhodanobacter peak with groundwater rather than sediment.
- Annotate the 18 M6-C2 isolate genomes for fermentation and sulfate reduction, to test the M6 plume-core interpretation.
- Repeat 16S profiling across seasons, and test whether community change over time tracks geochemical change in the ENIGMA samples.
- Fit CCA or RDA models of Oak Ridge communities on several geochemical variables at once. This would separate uranium from its co-varying geochemistry.

## [[concepts/geographic-and-biome-distribution-of-environmental-metal-resistance|Geographic and biome distribution of environmental metal resistance]]

- Count distinct sample_accession prefixes per hotspot, to test whether the Atacama and USA clusters are single-study artefacts.
- Re-run the grid test with sampling-effort normalisation by log(n_MAGs), to see which hotspots and coldspots survive.
- Check whether the soil enrichment holds within grid cells, to separate biome effects from geography.
- Check how metadata gaps shape the cohort (see [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]]).

## [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness|Guilt-by-association inference of dark gene function from modules, operons, synteny and co-fitness]]

- Repeat the synteny test beyond the 48 Fitness Browser genomes, using thousands of genomes. This would test whether the 0.95 median conservation, a lower bound, rises, and would remove the sampling limit.
- Add gene-fusion and shared-phylogenetic-profile scoring to the 21,011 pairs. This would bring the analysis closer to STRING and EFI-GNT.
- Compare the single-genome heuristic operons with DOOR or ProOpDB predictions. This would show how many of the 30,190 dark-gene operon assignments hold.
- Test experimentally a sample of the 998 double-validated pairs. This would turn guilt-by-association leads into validated assignments.
- Check module-only predictions (4,236) against ortholog transfer. This would show which are process-level context only.

## [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility|Gut microbiome ecotype stability and cross-study reproducibility]]

- Fit LDA and GMM on a second, independent pooled cohort and test whether ARI again peaks at K=4. This would give the external replication of the framework that is currently missing.
- Re-run the LOSO test with a consensus baseline that avoids the 48.9 % LDA↔GMM disagreement, to separate baseline error from true sub-study variance.
- Recompute the Kuehl species-detection fraction against the training species list, to resolve the 54 % versus 70 % discrepancy.
- Project Kuehl onto the reference with a Kaiju-matched reference or restricted to commonly detected species, to check whether the E0/E1/E3 split holds.
- Evaluate the clinical classifier within IBD only (is_ibd fixed) on a second IBD cohort, to measure real patient-level agreement.
- Examine why E3 is less recoverable (30.7 %) from pathway features, using additional multi-study E3 samples.
- Check how many of the 45 HMP2-concordant E1 candidates are among the 3 that survive the independent-stream gate, to separate replication of ecotype markers from replication of CD drivers.

## [[concepts/habitat-and-soil-chemistry-structuring-of-metagenomic-functional-gene-content|Habitat and soil-chemistry structuring of metagenomic functional gene content]]

- Fit a nested or interaction PERMANOVA (pH × horizon) on the soil workflows to test whether the interaction recovers the variance that horizon alone misses.
- Repeat the habitat enrichment after adjusting for taxonomic composition, for example by stratifying by taxon. This would show how much housekeeping-module enrichment is only an abundance shift.
- Fill the kegg_module_terms name and category fields, then re-label the enriched modules.
- Run a per-MAG functional contrast of the 40 soil archaeal MAGs (Methanobacterium, Methanosarcina, Nitrososphaera).
- Test whether the habitat and pH patterns replicate in a study other than NEON.

## [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata|Harmonizing free-text isolation source and environment metadata]]

- Add the missing keyword classes and an env_broad_scale fallback, then re-measure the 17% "Other" share. [src: env_embedding_explorer]
- Compare ENVO-based classes with keyword classes for genomes with env_broad_scale, to measure accuracy. [src: env_embedding_explorer]
- Repeat the ecotype analysis with ENVO terms. [src: ecotype_env_reanalysis]
- Add BacDive or GTDB environmental labels and test whether they resolve the marine null associations. [src: metabolic_capability_dependency]

See also [[entities/ncbi-env-environmental-metadata]] and [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].

## [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes|Horizontal gene transfer and mobile elements as a source of novel and dark genes]]

- Test proximity to mobile elements for the novel/singleton genes enriched in L and V, to see whether the category signal and the dark-gene neighbourhood signal pick out the same genes.
- Combine GC deviation, mobile-element proximity and phylogenetic patchiness per gene, controlling for membrane-protein composition, to reduce the proxy ambiguity.
- Characterize dark islands for prophage markers versus metabolic cassettes, and check whether island genes carry composite LV assignments.
- Compare mobile-element proximity in truly dark versus annotation-lag genes to separate novelty from lag.

## [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration|Horizontal gene transfer inference metrics and control-class calibration]]

- Benchmark M22 gain attribution against a DTL reconciliation (Liu 2021 DTLOR or Bansal SPR-based) on a representative GTDB subset. This would close the missing-benchmark gap.
- Run M22 and López Sánchez 2026's Sankoff-Rousseau algorithm on a shared substrate and compare gain-depth calls.
- Quantify gene-tree rooting uncertainty on a sample of families and propagate it to depth-bin assignments.
- Test the M18 gate (d ≥ 0.3) at KO level with per-phylum Sankoff, using the holdout as the producer-null validation.
- Rebuild the AMR positive control from a set that is not Pseudomonadota-biased, and rerun the Sankoff comparison.
- Rebuild a ribosomal control from universal r-proteins only, using current KEGG assignments rather than the K-number range, and test whether it meets n_neg ≥ 20.
- Cross-validate the CRISPR-Cas and tRNA-synth recent-to-ancient ratios against an independent HGT dataset.

## [[concepts/horizontal-transfer-of-carbohydrate-active-enzymes-via-conjugative-machinery|Horizontal transfer of carbohydrate-active enzymes via conjugative machinery]]

- Run the pending BLAST of Node_4915 against NCBI nr to check the 8-phylum event independently of the gene tree.
- Complete the threshold validation, testing whether the 92 families at ≤10 kb hold at other distance cut-offs.
- Test whether T4SS-adjacent GT2 genes sit within IME/ICE boundaries. This would test the integrative interpretation against other mechanisms, including plasmid mobilisation.
- Check whether GH23 and other cell wall remodelling genes co-locate with GT2–T4SS loci more often than in matched control neighbourhoods.
- Test transfer experimentally, for example by conjugation assays with a candidate GT2 cassette, since all current evidence is observational.

## [[concepts/horizontal-transfer-of-storage-pathway-genes-inferred-from-pangenome-core-accessory-status|Horizontal transfer of storage-pathway genes inferred from pangenome core/accessory status]]

- Build a phaC gene tree and test it for incongruence with the species tree. This replaces the core/accessory proxy with direct evidence.
- Test whether accessory phaC in discordant species sits on mobile elements or in genomic islands. This would separate recent transfer from other causes of accessory status.
- Check whether the 278 putative loss events in high-prevalence families are real losses or annotation gaps.
- Compare accessory rates for other PHA pathway genes, following the gene-specific patterns Cai et al. reported in *Halomonas*.

## [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes|Horizontal transfer signatures of metal-resistance genes]]

- Test gesA, gesB and nrsD for plasmid association with a larger plasmid collection. At most one genome per database carried gesA or gesB, so the plasmid test could not run.
- Repeat the plasmid enrichment test on all 13 double-signal KOs with a permutation or gene-level model. Only 2–3 resistance KOs had n ≥ 50, so the test is underpowered and merD dominates it.
- Re-run the BV-BRC cross-category comparison after moving resistance-classified efflux genes (aph, czcA, czcB) out of Transport. This would test whether the report's inflation explanation accounts for the NCBI–BV-BRC discordance.
- Build true gene trees for merD, merE, nikB and nicC and compare them with the species tree. This would test whether D is a valid proxy for gene-tree/species-tree discordance.
- Check golS for chromosomal mobile elements such as integrons or genomic islands. This would test the report's suggestion that its HGT was chromosomal.
- Add nrsD, merE, merD, shp and doxDA to the MGnify enrichment dataset so all 13 KOs can be scored for environmental enrichment.

## [[concepts/host-adaptation-pathway-loss-in-pseudomonas-carbon-catabolism|Host-adaptation pathway loss in Pseudomonas carbon catabolism]]

- Test whether the sugar losses are tied to one clade or arose repeatedly. Map the pathway calls onto a species phylogeny and use phylogenetic comparative methods. The 7 *Pseudomonas* s.s. species are too few to separate lineage from ecology.
- Check the predictions by growth assays of *P. aeruginosa* and *P. fluorescens* group isolates on xylose, arabinose, myo-inositol and galacturonate.
- Compare isolates from early and late infection with environmental isolates. This would show whether any further loss accrues during infection beyond the ancestral loss.
- Repeat the rhamnose and fucose comparison with more *P. aeruginosa* species or genomes to see whether the non-significant difference becomes resolvable.

## [[concepts/housekeeping-versus-substrate-specific-fitness-genes|Housekeeping versus substrate-specific fitness genes]]

- Remove the genes significant in 3 or more conditions, then recount genes per metabolite. This would show how much of the carnitine, alanine, arginine and tryptophan complexity is housekeeping. [[concepts/condition-specific-gene-phenotypes-and-functional-annotation-yield]] covers the related annotation question.
- Repeat the 1–2 versus 3+ condition split in other organisms in the Fitness Browser. This would test whether the split generalizes beyond FW300-N2E3.
- Compare WoM Emerged and Increased metabolites using only substrate-specific genes. This could clarify the slight, high-variance difference. See also [[concepts/condition-specific-fitness-correlation-across-carbon-sources]].

## [[concepts/independent-continuous-environment-embeddings-versus-categorical-isolation-source|Independent continuous environment embeddings versus categorical isolation source]]

- Repeat the GC test with a nonlinear association measure on the AlphaEarth embeddings, to see whether species missed by PCA plus Pearson appear.
- Enlarge the jointly testable set beyond 17 species, for example by relaxing the genome-count threshold, to test whether 59% agreement holds.
- Re-cluster the embeddings with a coarser DBSCAN setting and compare the clusters to isolation categories, to address the 320-cluster fragmentation.
- Test whether the 75% of principal components that do not discriminate isolation category align with geographic or climate variables.

## [[concepts/interpreting-negative-out-of-sample-r-in-environmental-predictive-models|Interpreting negative out-of-sample R² in environmental predictive models]]

- Rerun the models with spatial blocking and decompose the negative R² into shift, leverage and true unpredictability. This is the step the report lists as pending.
- Refit with outlier-robust metrics, such as median absolute error, or drop the highest-leverage test samples. This would show whether a few samples dominate the MSE.
- Compare spatially blocked and random folds on the same data. This would show how much of the negative R² comes from distributional shift.
- Repeat the shield efficiency comparison once the model has a positive baseline R². The current CI includes zero, and both R² values are negative.

## [[concepts/intrinsic-versus-acquired-resistance-gene-conservation|Intrinsic versus acquired resistance gene conservation]]

- Test whether "core" intrinsic genes sit in chromosomal backbone context and accessory ones near mobile elements. Use gene-neighborhood data on the same atlas clusters. This would turn the intrinsic/acquired labels from inference into measurement.
- Repeat the soil versus clinical core fraction comparison after excluding singleton clusters. This would show how much annotation artifacts drive the accessory excess.
- Fit mechanism, environment and phylum jointly in one model of core status. This would separate the ecological explanation from the mechanism effect.
- Compare costs of recently transferred and long-resident accessory genes. This would test the donor cost-optimization hypothesis.
- Re-run the phylogenetic-signal comparison with a metric not suppressed by near-universal genes. This would settle whether acquired genes truly carry stronger signal.
- Test the vertical-inheritance reading of core metal AMR by comparing MGE association of core and accessory metal AMR clusters in the 606 genera with signal. This would close the gap between λ ordering and direct mobility evidence.

## [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease|Iron acquisition as an AIEC-specific genomic specialization in Crohn's disease]]

- Genotype E. coli isolates or metagenome-assembled strains for pks, Yersiniabactin and Enterobactin loci, and test whether CD association tracks these loci. This would replace the correlational narrowing with a strain-resolved test.
- Recompute the iron-siderophore and genotoxin enrichment against a matched-niche comparator (gut Proteobacteria plus CD-associated Firmicutes). This would give a defensible effect size.
- Obtain species-stratified per-sample BGC abundance from raw reads to run the species-by-BGC interaction test for H3c.
- Test whether the 8 menaquinol pathways drive the iron-theme enrichment, by rerunning it without them.
- Measure siderophores with targeted metabolomics, since LC-MS undersampled them.

## [[concepts/iron-and-sulfate-reduction-signatures-in-clay-subsurface-porewater-versus-rock-attached-communities|Iron- and sulfate-reduction signatures in clay subsurface porewater versus rock-attached communities]]

- Test the corrected IR detector on a larger deep-clay set. With n=9, an OR of 1.88 cannot be told apart from no difference.
- Compare the corrected IR rates against the Mitzscherling rock-attached profile directly, as was done for SR, to see whether any IR contrast with the rock-attached community survives.
- Control for phylum when comparing cohorts (see [[concepts/phylum-level-confounding-of-habitat-specific-anaerobic-gene-content]]), to check whether the SR enrichment is a lineage effect.
- Re-run the marker-class breakdown with the corrected IR detector, so the IR_only, SR_only, both and neither classes are on the corrected markers.

## [[concepts/isolation-environment-validation-of-genome-predicted-metal-tolerance|Isolation-environment validation of genome-predicted metal tolerance]]

- Collect more heavy-metal-contaminated isolates with genomes, beyond the 10 matched, to estimate the effect size precisely.
- Improve species-name matching to recover more of the 31 planned heavy metal isolates.
- Add contamination isolates from Bacillota and Bacteroidota, from sources other than BacDive, to separate real biology from low power.
- Model genome size explicitly, for example with annotated-cluster count as a covariate, to test the host-associated anomaly.
- Repeat the FB-scale test with more species to see whether the null persists.

## [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa|Isolation-metadata versus metagenomic cross-validation of plant-associated taxa]]

- Test whether the 390 pangenome-only plant genera are opportunists. Compare their detection in MGnify soil with their isolation_source categories. This would check the explanation offered for the 11.7% Jaccard overlap.
- Check whether the 341 MGnify-only rhizosphere genera lack GTDB representatives. This would test the uncultured-lineage explanation.
- Recompute concordance with a stricter plant definition, such as rhizosphere-only isolation terms. This would show how much the low overlap depends on how plant association is defined. See [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]].
- Obtain rhizosphere BGC, mobilome and defense annotations for MGnify. This would allow a direct rhizosphere versus bulk soil comparison.
- Test the 17 core genera and the host-specific genera in additional crops. This would show whether they hold beyond tomato, maize and barley.

## [[concepts/join-key-validity-and-identifier-format-mismatches|Join key validity and identifier-format mismatches]]

- Run value-space overlap probes for UC2–UC5, then compare the results to the schema-level bridge list. This would show how many of the 536 bridges return rows.
- Build a library of identifier normalizers (GTDB prefix stripping, clade-ID suffix handling, locus-tag reconciliation, type casting). Test each against every bridge that shares genome_id or feature_id.
- Add a check that flags zero-row joins and silently dropped organisms. Run it over past analyses to find other null results caused by plumbing, as in NB12.
- Run a deduplication audit of refdata versus kbase UniProt entries, to quantify the overlap that the atlas leaves unmeasured.
- Test ADP1 cluster mapping edge cases by looking for clusters that split or merge between the two pangenome analyses.

## [[concepts/labile-carbon-effects-on-lignin-degrading-community-structure|Labile carbon effects on lignin-degrading community structure]]

- Measure lignin degradation rates in L, LC and LC-LC cultures. This would test whether the copiotrophic shift lowers, preserves or raises degradation, which the community profiles cannot show.
- Isolate Acinetobacter, Aeromonas and Enterobacter, then test them on lignin-derived aromatics alone and with labile carbon. This would show whether they depend on labile carbon or also use aromatics.
- Run a labile-carbon dose series with Round 2 transfers. This would show how much labile carbon is needed for the shift to persist, and whether evenness recovers.
- Check whether Flavobacterium and Comamonas decline when labile carbon is added. This would test the specialist reading of those taxa.

## [[concepts/laboratory-fitness-as-a-predictor-of-field-abundance|Laboratory fitness as a predictor of field abundance]]

- Match FB organisms to metagenome-assembled data at species or strain level, which would address the genus-level mismatch.
- Replace the aggregate score with per-metal fitness scores correlated with each site's metal concentration.
- Add pH, dissolved oxygen and carbon sources as covariates, to test whether confounding hides or creates the trend.
- Add *Rhodanobacter* to the FB so the dominant contaminated-site genus can be tested.
- Extend the test to more genera or sites, to raise power beyond n=12.

## [[concepts/lakehouse-namespace-migration-tenancy-and-authentication|Lakehouse namespace migration, tenancy and authentication]]

- Inventory which collections are still Delta-only by running live catalog discovery across all accessible catalogs. This would replace the current "may still be Delta-only" guess with a list.
- Scan archived project files for underscore-form names and report which ones resolve against the migrated catalog. This would show how many historical queries break.
- Test whether other principals see the same split between DESCRIBE DATABASE EXTENDED and COUNT(*). This would show whether the ForbiddenException pattern is general.
- Add a pre-flight check that calls get_group_sql_warehouse and validates the tenant and dataset pair before ingestion. This would catch the two misconfigurations listed above.

## [[concepts/lanmodulin-clade-restriction-and-xoxf-co-occurrence|Lanmodulin clade restriction and xoxF co-occurrence]]

- Run the multiple-sequence alignment of M. extorquens lanmodulin proteins described above, to settle diversification versus invariance.
- Re-survey lanmodulin in a much larger genome set. This would test whether the 100 % clade restriction survives beyond 62 genomes.
- Inspect the 13 lanmodulin-without-xoxF genomes for missed xoxF calls or other lanthanide-handling genes. This would separate annotation incompleteness from alternative pathways.

## [[concepts/latent-metabolic-capability-versus-fitness-dependency|Latent metabolic capability versus fitness dependency]]

- Calibrate the importance threshold against known essentials from [[summaries/essential_metabolome__REPORT]]. This would replace the median rule that forces a 50/50 split.
- Rerun the condition-type reclassification with a fixed, non-median threshold and a permutation control. This would test whether 100% reclassification exceeds chance.
- Apply the 48-organism threshold scheme to the 7-organism set, and the reverse. This would show how much of 41.0% versus 15.8% is definition rather than data.
- Check whether Incomplete but Important pairs are annotation gaps or salvage routes by targeted gene curation. See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].

## [[concepts/limits-of-keyword-and-marker-based-functional-annotation|Limits of keyword and marker-based functional annotation]]

- Run the proposed LLM pass over eggNOG Description and bakta product text for the 462-OG bucket. Compare category counts with the keyword scan to measure the undercount.
- Rerun the clay project's iron-reduction comparison with PFAM plus CXXCH detection. This would test whether the shallow-clay rock-attached signature survives.
- Audit other KO-based markers for generic-family KOs like K02030. Compare each against bakta product calls.
- Replace the ribosomal KO range with a curated universal r-protein list. Check whether the bimodality disappears.
- Compare gene-name-only PGP detection against product-description matching to quantify the missed genes.

## [[concepts/limits-of-transposon-based-essentiality-calls|Limits of transposon-based essentiality calls]]

- Measure how far gene length alone predicts "essential" calls. Fit a length-adjusted model across Fitness Browser organisms, using the 675 bp versus 885 bp medians as a baseline. This would separate insertion bias from biology.
- Test the partial-function hypothesis for the 211 ADP1 genes. Check where insertions fall within each gene for knockout-essential, TnSeq-dispensable genes.
- Check the AMR cost lower-bound claim. Recompute the +0.086 estimate with the 4.6% absent genes under bounding assumptions.
- Cross-reference the Database of Essential Genes to address the taxonomic bias of the 48 organisms.
- Test whether variable essentiality tracks metabolic pathway completeness. This would separate condition-driven from artifactual calls.
- Rerun orphan-essential calls with a more sensitive orthology method to estimate how many are missed by BBH.

## [[concepts/lineage-novelty-and-reference-database-culture-bias-across-environmental-gradients|Lineage novelty and reference-database culture bias across environmental gradients]]

- Build the curated full-length 16S phylogeny against SILVA NR99. Ask whether NEON OTUs (operational taxonomic units) from alkaline soils are genuinely more divergent or only less GTDB-represented. This would separate biological novelty from coverage gap.
- Compare novelty against the number of cultured isolates or reference genomes per phylum across pH bins. This would check whether acid-soil groups are better represented.
- Repeat the per-record OLS or logistic test with site or region as a grouping term, since the soil MAG records are probably not independent. This would show whether the slope survives.
- Test the pH slope in other soil MAG collections and against other GTDB releases. This would show whether the pattern is specific to NEON.

## [[concepts/linking-exometabolic-phenotypes-to-pangenome-gene-content|Linking exometabolic phenotypes to pangenome gene content]]

- Run the proposed test at genus level: correlate the E/(E+I) de novo production ratio with pangenome openness and accessory gene counts. This tests the hypothesis in the report.
- Build a strain-to-genome mapping for WoM organisms. This would allow species-level comparisons and close the mapping gap.
- Account for genome depth, since the listed entries range from 2 to 2,557 genomes. Restrict to well-sampled entries before comparing openness.
- Compare WoM-observed production with pathway predictions from `gapmind_pathways` to link gene content to metabolite output.

## [[concepts/linking-fitness-assay-genes-to-pangenome-clusters|Linking fitness-assay genes to pangenome clusters]]

- Re-run the link at several identity thresholds, for example 90%, 95% and 100%. Compare the number of links and AMR genes recovered. This would measure what the strict cutoff misses. [src: amr_pangenome_atlas, core_gene_tradeoffs, costly_dispensable_genes]
- Repeat the core/auxiliary comparison on species with at least 20 genomes only. Check whether the null result holds. [src: amr_fitness_cost]
- Add a locus-tag overlap check for every organism before joining. List any other organisms with partial mismatches. [src: discoveries, pitfalls]
- Rebuild the pangenome clade for E. coli so that Keio maps with high coverage. [src: conservation_vs_fitness]
- Test whether the 10 organisms below 90% coverage differ in taxonomy from the 33 retained. [src: conservation_vs_fitness]

## [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases|Linking isolate and strain records to reference genome databases]]

- Run the proposed query of `kbase_ke_pangenome.genome` to match BacDive GCA accessions to pangenome genome_ids. Measure how many of the 55,107 unmatched strains it recovers.
- Re-run the 10-of-31 metal-isolate subset after accession matching. This would show whether small validation subsets regain power.
- Apply the genus-consistency check to every name-based ENIGMA linkage. Compare the result with the 20 verified links.
- Attempt strain-to-genome mapping for WoM organisms to test species-level linkage beyond genus.

## [[concepts/literature-coverage-bias-and-text-mining-limits|Literature coverage bias and text-mining limits]]

- Apply the NCBI taxonomy lookup to the 14,798 Unknown organisms, to replace the heuristic domain shares with exact ones and settle the 35% discrepancy.
- Run the temporal trend analysis over the 1951–2026 span, to test whether concentration is growing.
- Build a negative-control set of genes known to be studied but absent from PMC-derived links. It would estimate how many "unstudied" genes are really missed literature.
- Compare PaperBLAST links with full SwissProt entries to measure how much curated knowledge open-access restriction hides.

## [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments|Matching exometabolite profiles to gene-fitness experiments]]

- Run the proposed gene-fitness test on self-produced carbon sources in pseudo3_N2E3 and pseudo13_GW456_L13, using the 19 FW300-N2E3 matches and equivalent GW456-L13 matches.
- Build a curated crosswalk for GW456-L13 like the FW300-N2E3 one, with match-quality flags. This would show whether the approximate-match pattern repeats.
- Add WoM data on consumption, or newer exometabolomics, to test consumed metabolites against fitness. This would close the production-only gap.
- Extend WoM sampling of E. coli BW25113 beyond sulfur metabolism, to use the Keio strain match.

See also [[summaries/fw300_metabolic_consistency__REPORT]], [[summaries/webofmicrobes_explorer__REPORT]], [[summaries/discoveries]], [[entities/web-of-microbes]] and [[entities/fitness-browser]].

## [[concepts/measured-fitness-as-independent-evidence-of-carbon-utilization|Measured fitness as independent evidence of carbon utilization]]

- Test whether ENIGMA isolates grow on lauric acid. This would turn the reference-organism call into an isolate-level call.
- Run the InChIKey re-match across all Tier-1 Fitness Browser carbon-source experiments for other compound classes. The census found only one match, so this would show whether lauric acid is unusual.
- Compare measured-fitness calls with annotation-filtered calls for the same compounds in shared reference organisms. This would check how independent the two routes are.

## [[concepts/mechanisms-and-confounders-of-copy-number-variation-in-pangenomes|Mechanisms and confounders of copy-number variation in pangenomes]]

- Split COG L into IS-element and true DNA repair loci to test whether the L signal is transposase-driven.
- Rerun NB03 on high-quality genomes (checkm_completeness ≥ 95, checkm_contamination ≤ 2) to test assembly inflation.
- In species with 200+ high-quality genomes, compare copy-count distributions conditional on cluster presence between adaptive and housekeeping clusters, to look for heavier tails.
- Correlate paralog copy count with fitness across the ~30 Fitness Browser-linked species.
- Compute dN/dS on paralog pairs with mobile-element context to separate purifying selection, neutral tolerance and mechanistic bias.

## [[concepts/mechanisms-of-ecology-linked-gc-shifts|Mechanisms of ecology-linked GC shifts]]

- Measure recombination rates per niche within the species that show the largest GC effects, and test whether GC offsets track them. This would test the gBGC hypothesis.
- Compare mutation spectra, especially the G→T rate, between aerobic and anaerobic lineages of the same species. This would test the oxidative-damage hypothesis.
- Test whether GC-increasing and GC-decreasing substitutions differ in codon and amino-acid usage across niches, in light of nitrogen availability. This would test the codon-usage hypothesis.
- Estimate divergence times for the lineage pairs to check the few-hundred to few-thousand-generation estimate against the proposed rates.

## [[concepts/metabolic-capability-versus-fitness-dependency|Metabolic capability versus fitness dependency]]

- Redo the pathway-to-fitness mapping with GapMind per-step gene assignments. Compare Latent Capability and Incomplete but Important counts against the SEED and KEGG proxies, to measure the false-positive dilution.
- Calibrate the importance threshold against known essentials from essential_metabolome. Then test whether the Latent Capability fraction survives a non-median cutoff.
- Run the deferred NB04 analysis on FW300-N2E3 tryptophan genes, to classify them as biosynthetic, catabolic or regulatory.
- Fix the taxonomy join between FB organisms and GapMind clades, to enable clade-level conservation comparisons. See [[concepts/join-key-validity-and-identifier-format-mismatches]].
- Extend the analysis beyond the 7 organisms with GapMind data, to test generalization across taxa.

## [[concepts/metabolic-competition-versus-direct-antagonism-in-pathogen-inhibition|Metabolic competition versus direct antagonism in pathogen inhibition]]

- Run the comparative genomics of top antagonists versus low-inhibition conspecifics described above, to test whether the residuals have a genetic basis.
- Test the direct-antagonism-versus-niche-coverage hypothesis in the proposed mouse model.
- Add biofilm, pH, iron and quorum-sensing measurements to the model, to test whether they account for the unexplained variance.
- Validate the model on isolates held out from the 142-isolate cohort, to replace the cross-validated estimate (0.145 ± 0.142) with an independent one.

## [[concepts/metabolic-guild-co-occurrence-and-redox-driven-segregation|Metabolic guild co-occurrence and redox-driven segregation]]

- Test whether the nitrifier–iron oxidizer coupling survives after removing U3, to see whether one well drives ρ = +0.95.
- Measure O₂, nitrate, NH₄⁺ and Fe²⁺ in the same wells and model guild abundance against them. This would separate redox exclusion from other spatial effects.
- Look for the same guild correlations in other well sets or time points, to check that they replicate.
- Check whether syntroph and fermenter genera carry the genes for H₂ or formate exchange, a test of the syntrophy interpretation of ρ = +0.55.

## [[concepts/metabolic-model-prediction-of-growth-defects-among-dispensable-genes|Metabolic model prediction of growth defects among dispensable genes]]

- Regress continuous FBA flux against growth rate rather than using binary essentiality class, to see whether quantitative effects appear.
- Run FBA simulations whose carbon source matches each growth assay, and test whether per-condition predictions improve.
- Examine the glucarate model, where the sign was opposite to prediction, to find the source of the condition-specific error.
- Repeat the class-versus-defect test in organisms where genes span essential and dispensable classes, to check whether the null result is specific to ADP1's all-dispensable set.

## [[concepts/metabolic-pathway-gap-filling-by-unannotated-genes|Metabolic pathway gap-filling by unannotated genes]]

- Match the 5,398 high-confidence EC-prefix candidates to the specific missing step in each gapped pathway. This would turn organism-level co-occurrence into gene-to-step hypotheses.
- Run AlphaFold structure prediction on the top candidates in Marinobacter, D. desulfuricans ME-23 and P. stutzeri, which have the most gapped pathways. This tests the proposed link to missing steps.
- Test growth on gapped carbon sources, such as fucose, rhamnose and sorbitol, in strains with candidate dark genes. Pair this with the existing fitness data to check enzymatic function directly.
- Compare the dark-gene candidate rate in gapped pathways with a background set of non-gapped pathways. This would test whether the enrichment is specific.
- Extend the pathway mappings to regulatory and structural functions. This would address the coverage gap.

## [[concepts/metabolic-versatility-oxygen-tolerance-and-metal-tolerance|Metabolic versatility, oxygen tolerance and metal tolerance]]

- Run the proposed sulfate-reducing bacteria zinc/copper challenge, to replace the 8-negative BacDive estimate with direct measurements.
- Repeat the oxygen-tolerance comparison with more anaerobes in Fitness Browser–BacDive validation, to address the n = 1 limit.
- Re-test enzyme breadth while controlling for relatedness, as discussed in [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]], to see whether its small association survives.

## [[concepts/metabolite-production-versus-utilization-discordance|Metabolite production versus utilization discordance]]

- Classify the 231 tryptophan fitness genes by GapMind pathway step, to separate overflow from active catabolism.
- Repeat the WoM and FB comparison in Pseudomonas stutzeri RCH2 and other ENIGMA isolates, to test whether the pattern is general.
- Compare WoM profiles of FW300-N2E3 across media, to test whether trehalose release is constitutive.
- Parameterize a community model of tryptophan cross-feeding with known auxotrophs, to test the cross-feeding interpretation.

## [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts|Metadata and annotation coverage gaps biasing environmental genome cohorts]]

- Compare ENVO-based labels with keyword-harmonized labels on the 42% of genomes that have env_broad_scale. This would measure the accuracy of keyword classification.
- Test whether the 3,838 genomes lost to NaN embeddings differ by region or isolation source from the 79,449 valid ones. This would show whether filtering adds bias.
- Run the pending expedition-level clustering and log(n_MAGs) sampling-effort checks on the Atacama and USA hotspots.
- Tabulate per-biome coordinate loss in public archives, to answer which biomes are most underrepresented.
- Extract finer isolation-source categories and rerun the GC ecology model, to see whether the coarse scheme hides signal.
- Repeat the species-level environment tests with environmental metadata directly rather than embeddings.
- Run the PySpark per-workflow coverage scan of pfam_annotation_gff and annotation_enzyme_commission, to learn whether they fill the soil-genera gap.
- Stratify the AlphaEarth distance–embedding curves by environmental versus human-associated samples in other reports that pool them.
- Recompute the NEON attrition figure from the workflow counts to settle whether 53% or the 246-to-73 reduction is the right denominator.
- Rerun the Pseudomonas environment prediction at genome level with genome-specific isolation sources, and compare it with the majority-vote species result to see how many generalist species the vote hides.

## [[concepts/metadata-introspection-versus-data-read-access-in-spark-based-catalogs|Metadata introspection versus data-read access in Spark-based catalogs]]

- Test whether DESCRIBE succeeds for other principals on the nmdc_* databases. This would show whether the ForbiddenException is specific to the kesciencero/microbialdiscoveryforge principal.
- Compare Iceberg-metadata COUNT(*) against full scans on a few large tables. This would confirm that metadata counts match the data.
- Add deduplication of dotted and underscore aliases to audit scripts, then check earlier inventories for double-counted tables (see [[concepts/audit-blind-spots-in-inventories-of-data-and-its-use]]).

## [[concepts/metagenome-based-cross-validation-of-genomic-trait-predictions|Metagenome-based cross-validation of genomic trait predictions]]

- Test whether the carrier-abundance correlations survive after removing the shared genera from the trait scores. This would separate compositional coupling from real signal.
- Compare observed correlations with a permutation null that preserves genus abundance structure. This would replace the sign tests, which have few directions to test.
- Test PHB capacity against temporal-variability measures, not point-in-time values. This would test the feast/famine hypothesis directly.
- Repeat the analyses in non-soil NMDC subsets to address the terrestrial bias.
- Validate taxonomy-based prophage burden inference against measured prophage content in metagenome assemblies. This would test the genus-level conservation assumption.

## [[concepts/metal-coverage-gaps-and-proposed-validation-experiments|Metal coverage gaps and proposed validation experiments]]

- Run manganese RB-TnSeq in Shewanella MR-1 and at least one non-reducer. This would test whether DvH's 100% core enrichment is universal and whether metal reducers differ.
- Test uranium in MR-1, ANA3, PV4 and Cup4G11. This would settle whether the non-significant delta (+0.035) reflects neutrality or low power.
- Screen chromate in the Oak Ridge FW300 Pseudomonas strains. This would test strains isolated from Cr-contaminated groundwater.
- Run La and Ce panels in Putida, Cup4G11, Keio and Marino. This would produce the first REE-tolerance gene sets and show whether they are shared.
- Run tungsten and nickel panels in both M. maripaludis strains. This would test whether W dependence is specific to sulfate reducers and show strain differences.
- Rerun the overlap statistics after new organisms are added. This would replace the single-organism (DvH) results with cross-organism replication.

## [[concepts/metal-fitness-breadth-and-magnitude-across-metals-and-organisms|Metal-fitness breadth and magnitude across metals and organisms]]

- Test the rare metals (U, Cr, Hg, Cd, Se, Mn) in at least 5 organisms each. This would separate general conservation from DvH- and psRCH2-specific patterns.
- Run metal experiments in *P. putida* KT2440, the only FB organism without them, to fill the largest organism gap.
- Compare important-gene fractions at matched numbers of metals per organism. This would show whether DvH's 49.8% and SynE's 33.6% reflect biology or sampling depth.
- Apply the atlas thresholds to the 37-organism cross-resistance set. This would show how organism selection changes the breadth counts.
- See [[concepts/organism-coverage-and-attrition-in-cross-organism-fitness-conservation-analyses]] for how attrition affects such comparisons.

## [[concepts/metal-gene-density-and-ecological-niche-breadth|Metal-gene density and ecological niche breadth]]

- Finish the pending BacDive culture-based niche-breadth replication, to give an independent breadth measure.
- Increase archaeal sample size beyond n = 95 and run a power analysis, to test whether the non-significant β = −0.014 reflects low power or a true absence of effect.
- Pre-register and run the inverse PGLS (niche breadth predicting metal-gene density), to settle the direction of the association.
- Repeat the Australia-only test with a different breadth definition, to see why NGSA is near zero while Northern hemisphere and soil subsets are stronger.
- Obtain ENIGMA data with more than 3 wells, so the within-site analysis can say something.

## [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs|Metal resistance co-occurrence with mobile gene-transfer hubs]]

- Test whether the GT2-hub enrichment holds in the 22,356 coordinate-bearing MAGs. Compare metal resistance in GT2–T4SS genomes with T4SS+ genomes that lack GT2 neighbours. This would separate a GT2-hub effect from a general T4SS effect.
- Control the 376-versus-260,276 comparison for biome and genome completeness. This would show whether the difference comes from environment or assembly quality.
- Check whether metal resistance genes lie on the same MGEs as the GT2–T4SS loci. This would test the hub interpretation directly.
- Test the niche-breadth hypothesis with biome range per genome against metal resistance count in hub and non-hub genomes.

## [[concepts/metal-resistance-genes-within-amr-catalogs|Metal resistance genes within AMR catalogs]]

- Recompute AMR prevalence per environment with metal and stress-response classes excluded, to show how much of the environment contrast is due to metal genes.
- Run the proposed co-localization analysis to test whether metal and antibiotic resistance genes really co-occur on mobile elements.
- Check whether removing the weaker hits in the "other" metal category changes the metal share.

## [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth|Metal resistance repertoire breadth and ecological niche breadth]]

- Use time-series genomic data that track metal resistance evolution alongside range shifts. This would test whether repertoire expansion precedes or follows range expansion.
- Run longitudinal metal-enrichment experiments on defined communities. This would separate scenario 1 from scenario 2.
- Add candidate shared drivers (metabolic versatility, biofilm capacity) as covariates beyond genome size. This would test scenario 3.
- Validate the inferred metal tolerance against measured physiology in a subset of genera. This would close the gap noted in the caveat on inferred traits.

## [[concepts/metal-responsive-ica-fitness-modules|Metal-responsive ICA fitness modules]]

- Apply ICA to metal conditions and test whether cross-resistance genes cluster into coherent modules (see [[summaries/metal_cross_resistance__REPORT]]).
- Compare the 0.826 mean core fraction with non-metal modules, to test whether the core enrichment is specific to metal modules.
- Check how sensitive the 3.1% responsive fraction is to the |z| threshold and to the share of metal experiments per organism.

## [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification|Metal-specific versus pleiotropic stress gene classification]]

- Run the COG, KEGG and PFAM enrichment test described above. It closes the gap that only descriptive SEED comparisons exist.
- Rerun the specificity classification with fit < -1 without |t| > 4, to see whether the osmotic overlap gap closes.
- Validate the classes against the Fitness Browser specificphenotype annotations.
- Repeat the conservation analysis on condition-specific genes only, to separate the core stress signal from metal-resistance evolution.

## [[concepts/metal-tolerance-determinants-and-shared-stress-confounding|Metal tolerance determinants and shared-stress confounding]]

- Run per-metal phenotype analysis, such as catalase against copper and urease against nickel, instead of composite scores. This tests whether any phenotype predicts a specific metal. [src: bacdive_phenotype_metal_tolerance]
- Run per-metal fitness profiling of urease+ and urease- bacteria from the same class, ideally Gammaproteobacteria. This tests whether urease+ organisms are nickel-specific rather than generally metal-tolerant. [src: bacdive_phenotype_metal_tolerance]
- Use RB-TnSeq on matched urease+/- strains under nickel versus other metals. This would directly test nickel-specific tolerance. [src: bacdive_phenotype_metal_tolerance]
- Repeat the conservation analysis using only genes important for metals but not for other stresses. This separates the core stress response from metal-resistance gene evolution. [src: metal_fitness_atlas]
- Test the YebC translation-bottleneck hypothesis, for example by measuring expression of proline-rich metal transporters under metal stress in yebC mutants. [src: discoveries]
- Recompute the general-stress keyword rates for metal-specific and general sick genes from the underlying gene lists. This would settle the text-versus-table conflict. [src: metal_specificity]
- Check whether keyword-free metal-specific genes (most of the 3,344) fall into the accessory tier, by testing their accessory-genome enrichment. [src: metal_fitness_atlas, metal_specificity]

## [[concepts/meter-scale-spatial-structure-and-distance-decay-of-subsurface-communities|Meter-scale spatial structure and distance-decay of subsurface communities]]

- Resample the grid at several times to test whether the east-west axis and the U3-M6-L7 corridor persist. This would close the single-timepoint gap.
- Link the residuals to measured plume geochemistry at each well. This would test whether the corridor tracks the flow path.
- Add wells along the east-west axis, or use a denser grid, to see whether the borderline directional Mantel result (p = 0.092) strengthens.
- Recompute the full pairwise Bray-Curtis matrix to settle whether U3–M4 or U3–L9 is the most dissimilar pair.
- Repeat the analysis at larger spacings to compare meter-scale decay with kilometer-scale studies.

## [[concepts/mobile-element-origin-of-costly-non-conserved-genes|Mobile-element origin of costly, non-conserved genes]]

- Run the genomic context analysis the report proposes. This would test the mobile-element claim directly, beyond keywords. [src: costly_dispensable_genes]
- Repeat the burden classification with a replicated-experiment or noise-aware threshold. This would address the single-experiment sensitivity. [src: costly_dispensable_genes]
- Test the unannotated genes, for example by domain search for mobile-element signatures. This would address the annotation gap. [src: costly_dispensable_genes]
- Re-link with a more permissive similarity threshold and a wider organism set. This would check the orphan and recent-acquisition calls. [src: costly_dispensable_genes]
- Compare the retained condition-specific phenotypes with gene-loss rates to test whether fitness effects slow loss. [src: costly_dispensable_genes]

## [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes|Mobile elements and horizontal transfer of plant-interaction genes]]

- Replace the proxies with direct geNomad mobile-element predictions, once available. This would test H4 and the genus-versus-genome signal.
- Run a genome-level mobilome comparison inside the same MGnify genera. This would test whether strains shed elements while genus totals stay high.
- Test whether the 15 adjacent marker-transposase pairs sit within annotated mobile elements, and compare the 498,677 shared-contig pairs with a baseline. This would separate real mobility from chance proximity.
- Obtain mobilome annotations for rhizosphere biomes. This would remove the soil-only limitation.

## [[concepts/mobile-genetic-element-context-of-horizontally-acquired-gene-families|Mobile genetic element context of horizontally acquired gene families]]

- Run batched or sampled PUL and mycolic neighborhood scans, using Spark-side aggregation instead of pandas merges. This would close the gap left by the scale failures.
- Ingest genomad_mobile_elements or an equivalent MGE caller, to replace product-keyword matching with a detector independent of annotation text.
- Add ICE-specific detection, such as relaxase and integrase near PUL loci, to test ICE transfer directly.
- Test whether elevated PSII subunits (for example PsbZ at 22.1%) differ from baseline, using per-subunit Poisson expectations.
- Run genomic-island, tRNA-proximity and scaffold-edge analysis for costly+dispensable genes.

## [[concepts/mobile-genetic-element-retention-in-cultured-isolates-versus-episomal-loss|Mobile genetic element retention in cultured isolates versus episomal loss]]

- Compare plasmid-borne and prophage-borne accessory content between cohorts, using the pangenome's bakta annotations. This tests whether MGE-borne metal resistance is specifically depleted in isolates. [src: oak_ridge_cultivation_gap]
- Classify each arsC and virB4/virD4 hit as chromosomal or plasmid-contig. This would show whether the enrichment sits in integrated elements, as the hypothesis requires.

## [[concepts/modular-architecture-and-co-occurrence-of-prophage-genes|Modular architecture and co-occurrence of prophage genes]]

- Test several species within a few well-sampled phyla. This would show whether the one-species-per-phylum pattern holds within phyla. [src: prophage_ecology]
- Run the proposed split analysis: core backbone (A, D, F) against accessory functions (B, C, E, G). [src: prophage_ecology]
- Validate the E and G module definitions, for example with curated integrase and anti-defense gene sets. This would show whether their weak co-occurrence reflects biology or definition. [src: prophage_ecology]
- Pool sparse head morphogenesis (B) data across more genomes to test whether its weak signal is due to sparsity. [src: prophage_ecology]

## [[concepts/module-level-enrichment-artifacts-from-broad-substrate-enzymes|Module-level enrichment artifacts from broad-substrate enzymes]]

- Re-run the module enrichment for other KEGG modules with per-KO step assignment. Flag modules where one KO accounts for most of the signal. This would show how often the limonene pattern recurs.
- Weight each KO by how many pathways it appears in, and test whether enrichment survives after removing the top shared KO. This would give a systematic filter for housekeeping-driven hits.
- Check whether the K14731-carrying Acidobacteriota MAGs encode other lactone-processing or plant-litter degradation genes. This would test the proposal that they use supplied lactones.
- Redefine "core" for ribosomal and other universal KOs in the field-only comparison. This would show how many of the 52 of 54 hits disappear.

## [[concepts/multi-criterion-design-of-protective-microbiome-formulations|Multi-criterion design of protective microbiome formulations]]

- Measure the full 10-pair interaction matrix for the five-species core and rescore with it. This replaces the additive assumption.
- Run the proposed mouse comparison of k=2, k=3 and k=5. It would settle whether coverage or engraftability drives efficacy.
- Screen Kocuria, Dermacoccus and other Micrococcaceae for a lung-adapted M. luteus replacement. This closes the coverage-engraftability gap.
- Repeat the bootstrap with more isolates, or with other pathogen strains. This would test whether the k=2 to k=5 overlap persists beyond PA14.

## [[concepts/multi-evidence-triangulation-of-metabolic-annotation-gaps|Multi-evidence triangulation of metabolic annotation gaps]]

- Knock out the genes behind the 44 high-confidence assignments on the relevant carbon sources, starting with rxn02185 and rxn03436. This would show whether the confidence tiers predict true gene function.
- Run DeepEC and CLEAN on the 50 EC-less reactions, then follow up with biochemistry. This targets the dark-reaction gap, where only 16% resolved.
- Apply the pangenome-conservation confidence assessment to ADP1's gapfilled reactions, to test whether it improves prediction reliability.
- Characterize the 105 unresolved pairs experimentally, to find what evidence the current streams miss.

## [[concepts/nadh-flux-rate-versus-nadh-yield-as-determinant-of-complex-i-dependence|NADH flux rate versus NADH yield as determinant of Complex I dependence]]

- Measure NADH/NAD⁺ ratios in quinate- and glucose-grown ADP1 by metabolomics, to test the predicted higher ratio on quinate.
- Reanalyze respiratory chain proteins in the Stuani et al. (2014) proteomics, to test whether the wiring is regulated or passive.
- Replace the theoretical stoichiometry with measured flux distributions, for example from isotope tracing, to test the concentrated-burst assumption.
- Test other substrates predicted to give concentrated reducing equivalents, to check whether the principle generalizes.

See also [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].

## [[concepts/ndh-2-compensation-for-complex-i-loss-across-species|NDH-2 compensation for Complex I loss across species]]

- Re-identify NDH-2 in FB organisms by KO (K03885) instead of text matching, then repeat the aromatic-deficit comparison. This would remove the annotation false positives that reversed the first result.
- Run the pangenome co-occurrence query for K03885 and K00330-K00343 across the 27K species. This would replace the 14-organism sample.
- Run the unperformed Acinetobacter co-occurrence analysis to test whether NDH-2 and Complex I co-occur.
- Measure Complex I fitness on aromatic, acetate, succinate, glucose and lactate substrates in single organisms with and without validated NDH-2. This avoids mixed architectures.
- Collect ADP1 growth data for NDH-2 on glucose to test the predicted backup role.

## [[concepts/notebook-provenance-and-session-isolation-in-agent-assisted-analysis|Notebook provenance and session isolation in agent-assisted analysis]]

- Audit all projects with `git log --all -- projects/*/notebooks/NB*.ipynb` against the NB references in their READMEs and plans. This would show how common the missing-history gap is beyond genotype_to_phenotype_enigma.
- Add a pre-commit check that flags committed notebooks with empty outputs. This would catch both the script-prototyping and the `--inplace` loss cases.
- Compare notebook outputs before and after `--inplace` and `--output` runs on JupyterHub. This would show when `--inplace` drops outputs, since only one project reported it.
- Test whether per-session git worktrees remove the wrong-branch commits, by logging branch mismatches at commit time across concurrent sessions.
- Test the `/submit` reviewer with an absolute repo-root path. This would confirm whether it stops the nested REVIEW.md.

## [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests|Ontology versus name-pattern categorization in pathway enrichment tests]]

- Re-run v1.8 with a regex-derived category set as a sensitivity check, to see which themes are robust to schema (closes the single-schema gap).
- Apply the hierarchy test species by species (NB07b) to see whether the iron/heme signal is attributable to specific species such as E. coli.
- Test KEGG BRITE or GO biological-process categories on KEGG/EC-level data, to check whether the reversal generalizes beyond MetaCyc.
- Reconcile the 357/409 and 514/575 coverage counts by documenting the denominators.
- Test the proposed broadened literature categories (electron acceptors, iron, fat use) against the hierarchy result.

## [[concepts/operon-organization-versus-functional-coupling-of-pathway-support-genes|Operon organization versus functional coupling of pathway support genes]]

- Repeat the cross-category operon and clustering test in other aromatic degraders. This would show whether the lack of co-localization is specific to ADP1.
- Compare transcript data for PQQ, iron and Complex I genes under quinate and non-aromatic substrates. This would test whether separate loci share regulation despite their distance.
- Test whether the 0.89 nearest-neighbour ratio differs from a permutation null that accounts for operon structure. This would show whether the 9 clusters are more than chance.

## [[concepts/organism-coverage-and-attrition-in-cross-organism-fitness-conservation-analyses|Organism coverage and attrition in cross-organism fitness conservation analyses]]

- Fix the locusId format for the seven excluded organisms and rerun specificity, to test whether the 40.7% attrition changes the results.
- Rerun conservation estimates with a phylogenetic control, such as independent contrasts, in place of the single duplicate-strain removal.
- Normalize fitness by metal concentration relative to MIC, then test whether the rare-metal results (cadmium, uranium) survive.
- Test additional organisms for manganese, chromium, uranium and tungsten, to replace single-organism results with replicated ones.
- Rerun the NaCl overlap with a per-organism experiment-count correction, to test whether SynE's outlier status is a threshold artifact.

## [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes|Organism selection and taxonomic coverage bias for experimental characterization of dark genes]]

- Rerun the extended covering set with an objective that rewards cross-phylum concordance, so that Bacillota such as B. subtilis are selected. This would test whether the unique-OG criterion undervalues Gram-positive organisms.
- Redo the non-FB OG mapping at species or strain level rather than genus level. This would show how much the 98.7% coverage is overestimated.
- Check the tractability weights, such as 0.3 for B. thetaiotaomicron, by sensitivity analysis. This would show how far the rankings depend on those values.
- Test the roadmap's ~100 universal dark gene families in B. subtilis and S. coelicolor RB-TnSeq libraries. This would show whether the cross-phylum predictions hold.
- Compare Route A and Route B picks against later reannotation, as in [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]]. This would show whether Route B finds genes that are truly unannotatable.

## [[concepts/organism-specific-versus-mechanism-specific-wiring-of-amr-support-networks|Organism-specific versus mechanism-specific wiring of AMR support networks]]

- Test whether the 0.375 versus 0.207 gap holds after matching organisms for the number of AMR genes and for genome size. This would show whether the gap reflects wiring or sampling.
- Compare cofitness partners of the same mechanism in closely related versus distant organisms. This would show whether organism specificity scales with phylogenetic distance.
- Check whether partners of efflux genes are enriched for energy metabolism in organisms with measured costs. This would test the PMF-drain compensation hypothesis directly.
- Relate overlap with [[concepts/amr-genes-in-ica-fitness-modules]] to see whether module membership follows the organism.

## [[concepts/pairwise-interaction-among-commensals-in-competition-assays|Pairwise interaction among commensals in competition assays]]

- Measure all 10 pairwise combinations of the 5 core species in the PA14 competition assay. This would close the gap of 5 untested pairs.
- Use the complete matrix to validate or correct the additive formulation scores, flag combinations to avoid, and choose the 3- and 4-member subsets for mouse models.
- Clarify from the raw assay records how the "3 pairs", "5 unique pairs" and "8 comparisons" counts relate. This would settle the scope of the current data.
- Replicate the existing pairs to test whether the −5.8% mean and the N. mucosa near-additivity hold beyond 8 comparisons. This addresses the underpowered sample.
- Obtain a distinct co-culture dataset, or repair the duplicated table, so per-substrate interactions can be assessed.

## [[concepts/pan-bacterial-prevalence-phylum-distribution-and-mobility-of-anti-phage-defense-systems|Pan-bacterial prevalence, phylum distribution and mobility of anti-phage defense systems]]

- Rerun the CRISPR-Cas prevalence and core/accessory split using Pfam Cas1 and other specific Cas Pfams alongside eggNOG descriptions. This would show how much of the mild-accessory result depends on permissive matching.
- Run the SNIPE versus non-SNIPE COG V defense-density comparison in Spark Connect. This would close the gap left by the REST API limit.
- Test mobility directly. Check whether accessory and singleton defense clusters sit near mobile-element markers in the same genomes, rather than inferring transfer from singleton fractions alone.
- Reconcile the InterPro 1,373-species set with the pangenome 1,696-species set. This would show which species each method misses.
- Add per-phylum core/accessory splits for each family. The phylum prevalence results do not give them.

## [[concepts/pangenome-conservation-of-metabolic-model-discordant-genes|Pangenome conservation of metabolic-model discordant genes]]

- Test the 227 discordant genes for pathway and regulatory-function enrichment. This would show whether discordance follows function even though no pangenome enrichment was detected.
- Run the multi-species extension. ADP1 genes are almost all core, so species with more accessory genes would test the null better.

## [[concepts/pangenome-openness-and-its-correlates|Pangenome openness and its correlates]]

- Re-run the AMR–openness and CAZyme–openness correlations with genome-count-matched subsampling, to separate biology from the sampling artifact.
- Estimate AMR gene gain and loss rates from tree distances, to test whether resistance genes are gained faster than lost.
- Compare CAZyme gain and loss across related species in different biomes, to separate adaptive acquisition from ancestral retention.
- Test the rare-AMR-gene explanation for the negative variability–openness link by recomputing variability at thresholds below 5%.
- Compare the openness metrics of the different reports on the same species set, to see why pathway variability predicts openness while environment and phylogeny effects do not.
- Recompute the environment and phylogeny null with alternative openness metrics and with gene-function strata (L mobile, V defense).
- Test an openness × lifestyle interaction, such as open pathogens versus open environmental species.
- Compute phylogenetic independent contrasts for the pathway–openness relationship, to close the gap the report leaves.

## [[concepts/pangenome-scale-prediction-of-metal-tolerance-from-gene-content|Pangenome-scale prediction of metal tolerance from gene content]]

- Run the H3 validation against BacDive polymetallic isolation environments, to close the gap left by the null result. See [[concepts/validating-metal-tolerance-predictions-against-culture-collection-metadata]].
- Replace count-based scores with per-species hypergeometric enrichment tests, to remove the genome-size confound.
- Test the Pseudomonas putida prediction with a full metal panel (Co, Ni, Cu, Zn, Al, Cr, U). See [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]].
- Build a regulatory or expression-based model, since presence/absence failed.

## [[concepts/paralog-expansion-and-gene-copy-number-constraint|Paralog expansion and gene copy-number constraint]]

- Rerun the HPK correlation on a subset of well-annotated cultivated genomes of about 207. This would test whether annotation density and taxonomic breadth explain the drop from r ≈ 0.74.
- Count per-genome HPK paralogs directly, as Alm did, and compare with M22 gains. This would separate the metric difference from the scale difference.
- Apply a tree-aware reconciliation such as Sankoff parsimony to the UniRef50 and architecture data. This would test whether the absent UniRef50 producer signal reflects the metric rather than the substrate.
- Extend the core/accessory stratification to the "other" 80% of clusters and to categories J and C. This would show whether near-single-copy core and expanding accessory hold beyond the F, H, L, V, M, K partition.
- Test whether phylum-level ratios (4.0× to 15.4×) track measured accessory-genome size across more species per phylum. The report only interprets this link.

## [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals|Pathobiont co-occurrence modules versus cross-feeding with commensals]]

- Test the E3 hub result (butyrate producers inside the pathobiont module) with paired metabolomics in an E3 cohort. NB09c rests on HMP2 only, so this would show whether E3 differs.
- Run in vitro co-culture of A. caccae with E. bolteae and F. plautii on lactate. This tests directly what the opposite-sign correlations only imply.
- Model post-cocktail re-equilibration by simulating hub removal in the NB06 networks. This tests the claim that the module re-forms around a remaining hub.
- Build a module-anchor framework for E3 patients, where oral-gut co-trafficking dominates.

## [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy|Pathobiont target prioritization for IBD phage therapy]]

- Ingest HMP2 raw data and rerun the E3 meta-analysis with a second study, to test whether the three trustworthy Tier-A species replicate.
- Reformulate E1 differential abundance so it excludes ecotype-markers, then re-score E1 with the confound-free filters.
- Run the three repair filters on the six NB05 actionable targets, to show which of them pass.
- Add per-candidate cross-cohort support columns to NB05 scoring so replication is visible next to each score.
- Search other BGC catalogs for E. bolteae to test whether the missing BGC hit is a real blind spot.
- Check phage availability for the repaired Tier-A list (the page's stopping point), starting with M. gnavus and F. plautii.

## [[concepts/pathogen-metabolic-adaptation-in-the-lung-and-stability-of-competition-targets|Pathogen metabolic adaptation in the lung and stability of competition targets]]

- Test the inhibition assay against ExoS+/PAO1-type strains. This would close the gap between genome-predicted and measured transfer across virulence types.
- Culture representatives of the 53-genome TCA-deficient cluster in synthetic CF sputum medium. This would test whether they depend more on external metabolites and are more easily excluded.
- Measure expression of amino acid catabolic genes, not only biosynthesis, in the exacerbation metatranscriptomes. The reported down-regulation covers pathways broadly, so this would show whether the exclusion targets stay expressed in vivo.
- Run the same GapMind lung versus non-lung comparison for A. baumannii and K. pneumoniae. This would test whether pathogen-specific formulations are needed.

## [[concepts/pathway-completeness-inference-from-ko-annotations-and-pleiotropic-enzymes|Pathway completeness inference from KO annotations and pleiotropic enzymes]]

- Re-run the class assignment after mapping Pfam accessions to eggNOG domain names. This would show whether Class I–IV can be recovered for the 11,792 phaC clusters.
- Search for phaR by sequence homology or domain in a sample of complete-pathway genomes. This would separate true absence from annotation failure for K18080.
- Test whether requiring phaC and excluding phaA/phaB-only calls changes downstream ecological associations. This would measure the effect of the precursors-only inflation.
- Examine the 62 synthase-only species for missing precursor annotations. This would show whether they are real exceptions or gaps.

## [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss|Peptidoglycan remodeling and Tol-Pal engagement after outer-membrane LPS loss]]

- Run the pulse-chase lipidomics with fluorescent phospholipid in rescued cells versus controls. This closes the gap between Pal-up expression data and the transport inference.
- Test Tol-Pal in conditional-depletion strains. This would separate the phospholipid-transport role from the Pal-PG contact role.
- Rerun the H4 test with CCNA_00565 and CCNA_01833 removed. This would confirm that the 28-locus result and its direction summary do not depend on them.

## [[concepts/ph-driven-niche-partitioning-and-genus-co-occurrence-in-contaminated-subsurface-communities|pH-driven niche partitioning and genus co-occurrence in contaminated subsurface communities]]

- Run SparCC on the full 100WS ASV matrix to test whether the two clusters hold up beyond Spearman correlation.
- Finish sample-to-location name resolution, then join per-well geochemistry to the community data.
- Link strain-isolation wells to per-well geochemistry to test the local origin of Cluster B strains.
- Measure pH-dependent growth for Cluster A and Cluster B strains, and test whether genomic features separating the clusters predict pH tolerance.

## [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap|Phage availability for gut pathobionts and the gut-anaerobe phage gap]]

- Query INPHARED and IMG/VR for H. hathewayi, F. plautii and M. gnavus phages, to close the external-data gap the report left out of scope.
- Cross-reference the 188 PhageFoundry strains with literature AIEC annotation and pks-island status. This would give true AIEC coverage and show whether the 26 escape strains matter clinically.
- Run AIEC strain-resolution diagnostics on patient stool isolates and test the 5-phage cocktail against them. This closes the gap between PhageFoundry and patient strains.
- Reclassify the 80 % "Unknown"-family HMP2 phage observations to link them to hosts.
- Test lytic activity and burst size for the cocktail phages, and test in-vivo delivery, since the HMP2-PhageFoundry overlap is 0.

## [[concepts/phage-resistance-versus-metabolic-cost-trade-off-at-receptor-transporters|Phage resistance versus metabolic cost trade-off at receptor transporters]]

- Measure growth on D-mannose and D-glucosamine in SNIPE-bearing strains against isogenic man knockouts. This would test directly whether SNIPE carries no metabolic cost.
- Test for SNIPE across the strains behind the 1/188 lambda infection figure. This would check whether ManYZ loss and SNIPE presence are alternative routes to lambda resistance.
- Test whether phages that evolve alternative injection mechanisms also escape SNIPE. This would show whether pore defense is more durable than receptor loss.

## [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes|Phylogenetic breadth and pangenome conservation of dark genes]]

- Map the bacterial paradox clusters onto the GTDB phylogeny to find phyla and families with the highest density of conserved-yet-novel proteins. This would add a phylogenetic view to the OG-level tiers above.
- Compute tier distributions separately for truly dark and annotation-lag genes. This would test whether the narrow breadth of truly dark genes persists under full-pangenome counts, not just FB ortholog breadth.
- Test whether top Route B knowledge gaps (COG0468, COG0443, COG0491) are essential, for example in essentiality data. This would check the suggestion that they lack differential fitness signal.
- Re-rank with the species-count metric at full-pangenome scale. This would show how much the top-50 and top-100 lists change when counts are not capped at 33.

## [[concepts/phylogenetic-confounding-of-environment-amr-associations|Phylogenetic confounding of environment-AMR associations]]

- Test family-level effects only in families that span several environments, and report how many families reach that threshold. This addresses the finding that most families cannot be tested.
- Partition AMR composition variance between phylogeny and environment, for example by variance partitioning. This would check the statement that phylogeny likely explains much more than the 2-13% attributed to environment.
- Repeat the within-family tests after excluding clinical isolates, to see whether the Enterobacteriaceae result depends on clinical sampling.
- Test finer taxonomic levels, such as genus, with the same approach used for metals, to see whether the effects persist.

## [[concepts/phylogenetic-confounding-of-gene-co-occurrence|Phylogenetic confounding of gene co-occurrence]]

- Resolve the reference-genome mapping so that distance stratification can be computed for all 9 organisms, closing the gap left by the 2 organisms without it.
- Add genomes from more distant relatives for species lacking a far stratum, then test whether the near-versus-medium drop in phi continues into the far stratum.
- Run Coinfinder, which controls for phylogeny, on the same pairs. Compare its associations with fitness-measured coupling.

## [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations|Phylogenetic confounding of phenotype–metal tolerance associations]]

- Run PGLS or phylogenetic PCA on the BacDive phenotype–metal data to replace class stratification with a continuous phylogenetic control. See [[entities/phylogenetic-generalized-least-squares]].
- Profile per-metal fitness of urease-positive versus urease-negative bacteria within one class, ideally Gammaproteobacteria, where the pooled urease effect is near zero. This would test nickel-specific tolerance.
- Compare the BacDive taxonomy result with phylogeny-blocked cross-validation ([[entities/xgboost-with-phylogenetic-blocked-cross-validation]]). This would show whether phenotypes add anything for unseen lineages.
- Test Gram stain on data that include Gram-positive Proteobacteria or other cross-lineage contrasts, if such data exist. The current data lack them.

## [[concepts/phylogenetic-distribution-of-phb-synthesis-across-bacteria-and-archaea|Phylogenetic distribution of PHB synthesis across bacteria and archaea]]

- Repeat the family tests with a phylogenetically aware model, to check that enrichment is not just shared ancestry within Pseudomonadota.
- Compare the 0% phyla (Campylobacterota, Gemmatimonadota, Nanoarchaeota, Marinisomatota) against genome completeness, to separate true absence from missing annotation.
- Improve environmental metadata for the "other_unknown" species, then re-test the freshwater/wastewater versus marine/host skew. See [[concepts/environmental-variability-and-storage-polymer-pathway-enrichment-feast-famine-hypothesis]].
- Test the Pieja et al. methanotroph split (Type I versus Type II) across GTDB methanotroph genomes.

## [[concepts/phylogenetic-signal-of-gene-content-and-traits|Phylogenetic signal of gene content and traits]]

- Run ANI-based Mantel tests on species with >500 genomes, such as E. coli and K. pneumoniae, using subsampling. This would test whether the acquired-over-core pattern holds in the largest species.
- Repeat the core-versus-acquired comparison with a metric that is not suppressed by near-zero variance, such as a permutation-calibrated or prevalence-matched test. This would separate the artifact from the biology.
- Measure Pagel's λ for core versus accessory AMR fractions within the same genera, and compare it with the within-species Mantel r. This would reconcile the scale difference.
- Expand archaeal genus coverage beyond 132 genera, and beyond short-read amplicon surveys. This would check whether the low archaeal B_std λ is a sampling effect.

## [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns|Phylogenetic structure versus ecological adaptation in gene-content patterns]]

- Overlay core-genome phylogenetic trees on ecotype assignments to separate adaptation from demographic substructure.
- Rerun ecotype clustering with HDBSCAN to test how sensitive the ecotype definitions are to the clustering method.
- Scale to all 456 eligible species, off-peak or with optimized queries, to address the breadth limit of the small sample.
- Test whether ecotype-defining COG categories correlate with environmental source in species with soil, host-associated or aquatic metadata.
- Apply a stricter phylogenetic control to species with few ANI clusters, such as E. faecium, and extend geographic testing beyond the 16 species.
- Run PGLS or phylogenetic logistic regression on Pseudomonas lifestyle-pathway associations with the GTDB species tree, to test whether they persist beyond relatedness.

## [[concepts/phylum-level-confounding-of-habitat-specific-anaerobic-gene-content|Phylum-level confounding of habitat-specific anaerobic gene content]]

- Run the proposed within-phylum deep-clay versus soil comparisons for Bacteroidota, Pseudomonadota and Acidobacteriota. This would show whether the functional signal generalizes or is Bacillota_B-specific.
- Run a genus-level Bacillota_B pangenome analysis (Desulfosporosinus, BRH-c8a, BRH-c4a). It would resolve the granularity hidden by n=5 vs 19 and could surface a deep-clay-specific accessory genome.
- Check the sulfate-reduction result with operon-level or strain-level marker checks, for example for non-functional dsrA. This would address the cluster-level annotation propagation caveat.
- Add more deep Bacillota_B genomes. The 5/5 vs 4/19 result, with p_BH=0.04, is near the threshold.

## [[concepts/porewater-bias-as-a-general-signature-of-cultivation-based-subsurface-collections|Porewater bias as a general signature of cultivation-based subsurface collections]]

- Apply the SR/IR marker framework to Olkiluoto, Oak Ridge basalt and salt-cavern cohorts, to test lithologies beyond clay and aquifer.
- Run cultivation_bias_diagnostic() at every Lakehouse site holding both cultured and MAG collections, to test universality.
- Compare isolation-source metadata (porewater versus rock-attached sampling) with marker enrichment within a site, to test the porewater interpretation directly.

## [[concepts/pqq-cofactor-biosynthesis-support-in-xoxf-bearing-genomes|PQQ cofactor biosynthesis support in xoxF-bearing genomes]]

- Score the 897 no-PQQ xoxF genomes for ORF integrity and CheckM2 completeness, to separate assembly fragmentation, pseudogenization and community-PQQ acquisition.
- Apply sequence-level genome-quality filtering to the remaining ~24 % of xoxF carriers.
- Check bakta-only PQQ calls against sequence evidence, such as gene synteny and homology, to see how much bakta over-calling affects the 899 bakta-only strong genomes.
- Re-run the xoxF–PQQ co-occurrence survey with the eggNOG and bakta union.

## [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content|Predictability of binary growth phenotypes from gene content]]

- Test whether interaction features lift nitrogen and antibiotic classes, which sit near or below chance. This needs per-class AUC with and without the features.
- Add curated condition-specific pathway annotations for metals, antibiotics and nitrogen, the classes with no GapMind or CSP coverage.
- Rerun the metals class on data with more non-growth labels, since the 98% growth rate makes its AUC uninformative.
- Combine GapMind calls with GBDT scores in one stacked model, and score it on the 118 testable pairs.
- Explain the worst substrates, such as turanose and adonitol, by checking whether the relevant KOs are rare across genomes.

## [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content|Predictability of continuous growth kinetics from gene content]]

- Compute gRodon S-value or ENC from the CGCMS GenBank CDS sequences. Then test whether CUB predicts µmax under genus-blocked holdout, which closes the missing-feature gap.
- Check GC content variation among the ENIGMA genomes and include GC% as a covariate or stratifier in the CUB test, given the GC confounding of CUB reported elsewhere.
- Test whether expression data, where available, improves lag and yield prediction over the KO model.
- Clarify which genomes had GC% in the bulk-feature regression, and repeat it with GC% for all 727 genomes.

## [[concepts/production-versus-consumption-coverage-in-exometabolomic-databases|Production versus consumption coverage in exometabolomic databases]]

- Check whether the current GNPS2 version of WoM carries a decrease action. Compare its codes with the 2018 snapshot, which has none. This would settle whether the gap is only in the export.
- Re-run the ingestion pipeline once newer data are available. This enables the consumption analyses that are now blocked.
- Once consumption exists, test whether consumed metabolites predict gene essentiality. This is the question the 2018 snapshot cannot answer.
- Recompute the novelty rate (E share of changes) with consumption included. This would show whether the 15–32% range holds across a larger organism panel.

## [[concepts/prophage-anti-defense-genes-and-host-phage-arms-races|Prophage anti-defense genes and host-phage arms races]]

- Test whether module G anti-defense genes co-localize with defense system genes in the same genomes. This would check the defense-island reading, which currently rests on low co-localization of 0.281 and on prior literature.
- Compare defense-system repertoire and anti-defense repertoire per genome across human-associated and freshwater bacteria. This would test whether the enrichment tracks defense diversity, as the pan-immune model predicts.
- Measure how the enrichment varies within lineages that are high (Campylobacterota) or low (Patescibacteria) in module G prevalence. This would show whether the environmental signal holds within single clades.

## [[concepts/prophage-density-and-amr-repertoire-breadth-across-species|Prophage density and AMR repertoire breadth across species]]

- Test whether AMR genes sit on or next to prophage regions within genomes. This would separate direct transduction from shared accumulation.
- Add pangenome openness as a covariate, or stratify by it, to test the open-pangenome explanation.
- Repeat the analysis with a phylogenetic comparative method, such as phylogenetic generalized least squares, to test the phylogenetic-confounding argument directly.
- Explain why Actinomycetota (rho=0.29) is weaker than Bacteroidota (rho=0.59). Check whether the cause is marker detection or biology.

## [[concepts/prophage-proximity-and-amr-gene-conservation|Prophage proximity and AMR gene conservation]]

- Repeat the analysis with base-pair distances in place of gene ordinals. This would test whether the 3-5 gene reversal survives a physical distance scale.
- Run all genomes per species instead of 20. This would check whether the modest pooled OR and the species heterogeneity are sampling effects.
- Model species-level ORs against species traits, such as prophage density or pangenome openness. This could explain why only 33 of 74 species have OR>1.
- Annotate genes at 3-5 genes from prophage markers as phage-core or cargo. This would test the core-phage-component hypothesis directly.
- Check whether the 15-50 gene signal falls on annotated genomic islands. This would test the island hypothesis.

## [[concepts/provenance-overloading-of-dataset-labels-in-the-data-lakehouse|Provenance overloading of dataset labels in the data lakehouse]]

- Extend the provenance-audit method to other overloaded labels, to test whether the six-class framework generalizes.
- Trace actual queries or notebooks to see whether users picked the wrong NMDC-named resource. This would replace the inferred link with a direct observation.
- Obtain or build an ingestion manifest and compare it with the inferred classes.
- Group the inventory by provenance class rather than catalog prefix. Then test whether the kbase-tenant NMDC-related databases become findable.
- See [[concepts/audit-blind-spots-in-inventories-of-data-and-its-use]] and [[concepts/documentation-discovery-and-currency-gaps-in-lakehouse-catalogs-and-tooling]] for related gaps.

## [[concepts/pseudomonas-aeruginosa-strain-diversity-and-representativeness-of-reference-strains|Pseudomonas aeruginosa strain diversity and representativeness of reference strains]]

- Run the PAO1 and mucoid PROTECT isolate assays to test whether the invariance prediction holds in ExoS+ strains.
- Annotate the 1,358-gene accessory genome against virulence, biofilm and resistance traits measured across the 15 strain groups.
- Improve T3SS annotation for the 45% of PROTECT genomes lacking clear effector calls, to firm up the 86% PAO1-like estimate.
- Test whether the species-level conservation of sugar pathway losses holds across the 15 PROTECT strain groups, given the mosaic-genome view.

## [[concepts/realized-versus-theoretical-cross-collection-data-reuse|Realized versus theoretical cross-collection data reuse]]

- Re-run the audit on research plans and notebook source, not only READMEs. This would test whether the five zero-use bridges are truly idle, closing the lower-bound gap.
- Pilot one analysis per idle bridge, starting with kbase ↔ refdata through gtdb_taxonomy and kescience ↔ refdata through AlphaFold IDs. This would show whether the zeros reflect missing demand or missing awareness.
- Model projects per tenant against table share and documentation quality. This would test the report's explanations for concentration on kbase × kescience.
- Use the ibd_phage_targeting and cf_formulation_design patterns as templates for projects joining PhageFoundry or PROTECT to other tenants. This would test whether coordination, not technology, limits use.

## [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes|Reannotation lag versus genuinely unannotatable dark genes]]

- Extend pangenome linkage to the unlinked dark genes, then run Bakta on them, to close the coverage gap in the truly dark list.
- Break the reclassification rate down by phylum, including archaeal genomes such as [[entities/methanococcus-maripaludis]], to test database-coverage bias.
- Check whether Bakta product names for the 33,105 reclassified genes are specific or generic, for example by the share of "S"/unknown COGs.
- Test whether the 6,427 truly dark genes sit in genomic islands by comparing island and mobile-element proximity against a background gene set.
- Re-annotate the truly dark set with newer database versions to measure how fast the residue shrinks.

## [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates|Reference-database coverage and phylogenetic bias in annotation-gap estimates]]

- Re-estimate the gap with genomes resampled to equal taxa (for example one per genus). This would show how far Pseudomonas and E. coli over-representation shifts core gene counts and MSA depth.
- Compare annotation and MSA depth for clusters with and without UniProt accessions, stratified by phylum. This would test whether the uncovered 70.7% really has a larger gap.
- Extend the resolution pipeline to all 48 Fitness Browser organisms and add non-Proteobacteria. This would test whether the low Bacteroides rate reflects phylogenetic distance.
- Compute MSA depth for several members per cluster, not only the representative. This would measure the representative bias.
- Re-check "hypothetical" calls against UniProt, InterPro and newer Bakta databases. This would measure over-counting of dark genes, especially in archaea.

## [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries|Reference-database table choice and Pfam versioning in Lakehouse queries]]

- Re-run earlier bakta_pfam_domains-based absence calls with LIKE 'PFxxxxx%' patterns and compare them to interproscan_domains. This would show how many "missing function" conclusions came from the table or the ID format.
- Add the version-free versus versioned accession mismatch to the shared pitfalls documentation for kbase_ke_pangenome, with a tested join recipe that strips versions.
- Measure why bakta_pfam_domains lacks PSII and Cas1 Pfams, for example by comparing coverage per Pfam against InterProScan. This would show whether the gap is systematic.
- Report both the eggNOG record count and the post-join species-cluster count in future defense-marker tables, to close the ambiguity about which is reported.

## [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions|Reliability and coverage limits of GapMind pathway predictions]]

- Rerun the essential-metabolome analysis with E. coli included, using the eggNOG route for all 45 Fitness Browser organisms. Compare it with GapMind on the 7 covered organisms. This would close the coverage gap.
- Test a hybrid of pathway-level GapMind and gene-level eggNOG, and direct essential-gene-to-pathway mapping.
- Add aromatic-degradation KEGG modules to the Pseudomonas carbon analysis. This would test whether niche-specific signal is hidden by GapMind's 62 carbon pathways.
- Analyze within-Pseudomonas-species pathway variation, at strain level where possible. This would test whether metabolic ecotypes exist that species-level completeness hides.
- Compare genus-level max-aggregation with core-level scoring across plant compartments. This would settle the core-level threshold question.
- Resolve the "Incomplete but Important" pathways with step-level calls. This would separate annotation gaps from salvage routes.
- Test whether pathway gaps cluster by phylogeny or ecology, using species-level best-score aggregation.

## [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction|Reliability of KEGG ortholog markers for multi-heme cytochrome iron reduction]]

- Validate the triple-signal detector against genomes with known iron-reducing phenotypes, such as Geobacter and Shewanella. This would estimate its false-positive rate, which matters because PF22678 is a nitrite-reductase family.
- Test each signal separately (PF02085, PF22678, CXXCH count ≥4). This would show which signal drives the cohort rates and whether the threshold of 4 is arbitrary.
- Re-test the shallow-clay versus soil-baseline IR enrichment with the corrected detector, to settle whether the earlier 3.7-fold result survives.
- Audit other KO-based markers in the corpus for the same mismatch, by checking each KO's name against its intended function.
- Increase the anchor_deep sample beyond n=9. The null comparisons have low power, so absence of significance is not evidence of equality.

## [[concepts/reliability-of-species-level-bacdive-consensus-phenotypes|Reliability of species-level BacDive consensus phenotypes]]

- Place each BacDive compound call in a confidence tier (n and pct_positive) across other organisms, to see how many reported discordances survive a minimum-n filter.
- Split P. fluorescens records by GTDB sub-clade and recompute trehalose and other rates, to test whether strain variation tracks phylogeny.
- Test FW300-N2E3 directly on trehalose and lysine, the cases with small or variable BacDive support.
- Recompute the 3/7 versus 22/80 comparison with more produced metabolites, since the current test has few compounds.

## [[concepts/representativeness-of-reference-genome-collections-for-environmental-field-isolates|Representativeness of reference genome collections for environmental field isolates]]

- Compare phenotype predictions for Pseudomonas_E and Rhodanobacter isolates when the training set is clinical-heavy and when it is environment-matched. This would measure the transfer-learning bias that the report only raises.
- Repeat the environmental profiling at species or strain level, for example with shotgun data. This would test whether the genus-level clinical share hides niche differences.
- Compute the clinical share for each of the 14 ENIGMA genera, as was done for Pseudomonas and Rhodanobacter. This would show which genera are most affected.

## [[concepts/resistance-islands-and-co-occurrence-of-amr-genes|Resistance islands and co-occurrence of AMR genes]]

- Map islands to plasmid versus chromosome location, integron boundaries and IS elements. This would test the mobile-element reading, which is currently inferred only from phi values.
- Build a PanKA-style model on island co-occurrence to test whether it predicts future co-acquisition.
- Compare islands with and without shared mobile-element context against functional complementarity. This would separate linkage from co-selection.

## [[concepts/resource-darkness-of-compound-catabolism|Resource-darkness of compound catabolism]]

- Run an abstract-level PaperBLAST pass on the 74 dark compounds, starting with the alkaloids and terpenoids. This tests how many the title-only screen missed.
- Query MIBiG for the six biosynthesis-known compounds. This would show whether any has a known catabolic route.
- For the 33 KEGG-linked compounds with no reaction in genomes, search for homologs of reactions in the linked KEGG entries. This would show whether the gap lies in the genomes or in the annotation.
- Test whether the necromass skew in the orphan bucket holds once chemical class is controlled for.

## [[concepts/robustness-and-replication-of-niche-breadth-associations|Robustness and replication of niche-breadth associations]]

- Replicate the density–breadth association in a genuinely independent genus panel with different MAG sources. This would close the gap left by P5 being a subset of P1.
- Run a targeted replication with a northern-hemisphere soil amplicon survey. This would test the Australian-null explanation.
- Replace the 16S OTU–genus bridge with niche breadth computed directly from MGnify metagenomic genus-level classifications. This would remove the OTU-matching noise.
- Test the reduced-phylogenetic-diversity explanation directly. Subsample P1 to match the Proteobacteria/Firmicutes mix of the Australian panel, and check whether β rises to −0.052.
- Rerun the EMP PGLS with finer habitat resolution than EMPO level 2, or with more genera. This would show whether the nonsignificant result reflects coarse resolution or a weaker true effect.
- Apply formal multiple-testing control across all exploratory checks, as in [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].
- Add a power analysis for the Firmicutes and Bacteroidetes within-phylum tests. It would show whether their nonsignificant results reflect low power.
- Rerun the metal-types analysis at a 1–2% within-environment prevalence threshold. This would test whether the lost significance at 5% reflects power (n = 379) or a weaker effect.
- Split "aquatic" into marine, freshwater and estuarine using MicrobeAtlas sample metadata, and repeat the exclusion test. This would show whether the one weak case (q = 0.061) comes from category heterogeneity.

## [[concepts/robustness-of-exploratory-associations-to-coverage-fraction-and-site-covariate-specification|Robustness of exploratory associations to coverage, fraction and site covariate specification]]

- Fit mixed-effects models with well/location random effects on the 212 sample-fraction rows. This tests whether the relaxed coverage-adjusted defense signal (q=0.046) survives richer site structure.
- Add sampling date and location cluster covariates with compositional controls. This separates contamination from spatial and temporal confounding.
- Re-run the global BH-FDR with an explicit p-column allowlist. This confirms that no adjusted p-values were missed.
- Repeat the high-coverage analysis at several coverage thresholds. This checks whether the n=68 subset result depends on the 0.25 cutoff.

## [[concepts/sampling-bias-and-metadata-sparsity-in-amr-resistome-surveys|Sampling bias and metadata sparsity in AMR resistome surveys]]

- Re-run the environment comparison with clinical species down-sampled or weighted to match soil and aquatic genome counts. This would test how much of the "clinical species carry more AMR" signal comes from sampling.
- Compare AMRFinderPlus calls with a database-independent homology or novelty screen on environmental genomes. This would estimate how much novel resistance is missed.
- Rerun the species-level environment tests with within-species per-genome labels for a few well-sampled species. This would show whether majority-vote collapse changes the results.
- Redo the temporal trend test on the subset of genomes with curated collection dates, and add power calculations. This would separate a true null from date noise.
- Improve isolation_source classification, for example by curation or text mining, and report how many more species reach the chi-squared criteria.

## [[concepts/sampling-scope-and-generalizability-of-pangenome-wide-tests|Sampling scope and generalizability of pangenome-wide tests]]

- Repeat the copy-number test on the tightest-quality genome subset, filtered by checkm_completeness and contig N50. This would close the gap left by the missing quality conditioning. [src: gene_copy_number_variation]
- Add species from CPR, Patescibacteria, Spirochaetota and archaea, and test whether the direction of the class effect holds. This would address the phylum gap.
- Sample less-studied taxa alongside the clinically important ones, to check whether the species-selection bias changes the effect.
- Refine the functional partition so that some of the "other" clusters can be tested. This would show whether the effect extends beyond the classes now tested.
- Compare results at clustering thresholds other than 90% AAI. This would show how much the merging of recent paralogs shapes the counts.

## [[concepts/selective-filtering-of-communities-by-lignin-enrichment|Selective filtering of communities by lignin enrichment]]

- Test whether the Pseudomonas/Acinetobacter takeover persists or changes over further rounds. Only one round is characterized here, and a multi-round time series would show it.
- Run a no-lignin carrier or passage control to separate lignin selection from selection by serial transfer alone.
- Isolate Pseudomonas, Acinetobacter and Flavobacterium and test growth on lignin-derived aromatics. This would check the inferred aromatic metabolism against [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]].
- Explain why Sphingomonas is not enriched, for example by competition or by growth conditions. Compare with [[concepts/labile-carbon-effects-on-lignin-degrading-community-structure]].
- Reconcile the Lignin-condition percentages in the differential-abundance table with the group L means.

## [[concepts/selective-prebiotics-for-commensal-consortia|Selective prebiotics for commensal consortia]]

- Run the sole-carbon-source growth assays on the six substrates, and compare the resulting selectivity ratios with the expected >10. This closes the gap between prediction and measurement.
- Run the mouse infection arms with and without xylitol + xylose. This tests whether prebiotics help in vivo.
- Test single prebiotics against cocktails matched to the species that carry each pathway. This addresses the species-specific carriage.
- Relate the results to [[concepts/multi-criterion-design-of-protective-microbiome-formulations]] and [[concepts/engraftability-and-lung-adaptation-of-candidate-commensals]].

## [[concepts/sequence-clustering-resolution-and-protein-family-definition|Sequence clustering resolution and protein family definition]]

- Re-cluster at intermediate thresholds (for example 40% and 70%) and plot cluster count against identity. This would show whether any threshold marks a natural break, which tests the arbitrariness caveat.
- Compare 50% clusters with curated family databases such as Pfam. This would show how often the cutoff splits or merges real families.
- Repeat the singleton analysis with a different clustering tool or coverage setting. This would show how much of the 62.8–83.3% singleton share depends on the method.
- Test whether the unstudied-family conclusions change when the family threshold moves from 50% to 30%.

## [[concepts/sequence-composition-and-conservation-of-unannotatable-genes|Sequence composition and conservation of unannotatable genes]]

- Refit the ortholog, core and GC comparisons with gene length as a covariate, or within length-matched strata. This would show how much of each effect survives the length confound.
- Extend ortholog detection to the 16 uncovered Fitness Browser organisms. This would test whether the narrow-breadth result holds across all organisms.
- Compare GC deviation with direct mobile-element proximity per gene. This would test the horizontal-transfer explanation.
- Check whether the higher essential fraction persists after length matching, using [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]] to separate real essentiality from measurement limits.

## [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes|Shallow AlphaFold MSA depth and annotation of conserved core genes]]

- Compute per-class correlations (core, auxiliary, singleton) to close the stratification gap in the pooled ρ.
- Compare ESMFold pLDDT with MSA depth on the same clusters to separate sequence novelty from foldability.
- Map the paradox clusters onto GTDB to locate lineages enriched for conserved-yet-novel proteins.
- Join the paradox list to Fitness Browser fitness data to find essential members and give them first functional evidence.

## [[concepts/shared-dispensability-as-a-confound-in-cofitness-enrichment|Shared dispensability as a confound in cofitness enrichment]]

- Run the mean-fitness-matched permutation (−0.05 to +0.05) on the AMR support networks. This closes the gap left by matching on conservation class only.
- Split cofitness by antibiotic and standard-growth experiments. This tests whether AMR–flagella cofitness depends on the condition.
- Tabulate flagellar knockout mean fitness across Fitness Browser experiments. This checks the premise of the dispensability reading.
- Apply the same cofitness and permutation analysis to other condition-specific gene classes. This tests whether the signal is specific to AMR.

## [[concepts/shared-metal-and-osmotic-stress-fitness-determinants|Shared metal and osmotic stress fitness determinants]]

- Re-run the overlap with both studies' thresholds, and with thresholds scaled to NaCl experiment count (for example n_sick >= 2 or mean_fit), to see how far the 39.8% versus 14.7% gap is a threshold effect.
- Profile Mn, Cd, Se, Hg, Fe, Mo and W in more organisms to test whether the DvH hierarchy holds beyond one organism.
- Run hypergeometric enrichment tests on shared-stress versus metal-specific genes to test the proposed envelope, DNA-repair and ion-homeostasis functions.
- Add NaCl dose-response experiments for more organisms, as for *Synechococcus elongatus*, to separate dose effects from metal effects.

## [[concepts/single-metal-dominance-versus-distributed-metal-type-diversity-effects|Single-metal dominance versus distributed metal-type diversity effects]]

- Rerun the leave-one-out test with a larger metal vocabulary, or with a power-matched design that drops a random category of equal size. This would show whether the loss of significance reflects the 7-to-6 range compression or a real contribution from each metal.
- Run a leave-one-out analysis on the MAG metal-specific sets, dropping each metal's KOs from a pooled score. This would check whether the uniform signal holds in a combined index as well as in separate sets.
- Test the "other" category directly by excluding it, which gives the 6-metal analysis, and compare it with the original. This would show whether weaker annotation hits shape the result.
- See [[concepts/validity-of-curated-metal-gene-annotation]] and [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations]] for related annotation and gene-class questions that these tests could be combined with.

## [[concepts/small-cohort-and-phylogenetic-confounding-in-lineage-level-comparisons|Small-cohort and phylogenetic confounding in lineage-level comparisons]]

- Add clay-isolated Bacillota_B through new BacDive linkage or later pangenome ingests. Then rerun the per-genus analysis to see whether it moves beyond the n=10 resolution limit.
- Rerun the enrichment test with genus-level resampling, or with one genome per genus. This would show how much of the 547 enriched OGs depends on clumping.
- Map GTDB Bacillota_B genomes onto NCBI-based eggNOG levels to find finer OG tiers than root. This would address the coarse-tier problem.
- Add rock-attached Bacillota_B genomes or metagenomes to the anchor. This would test the porewater-bias caveat.

## [[concepts/small-sample-limits-in-community-amplicon-statistics|Small-sample limits in community amplicon statistics]]

- Collect n>=5 per group in a repeat enrichment. This would test whether pairwise PERMANOVA and OTU-level tests can pass the permutation floor.
- Re-sequence the ITS libraries at higher depth. Compare Round 2 within-group BC before and after, to separate depth from true stochasticity.
- Record extraction and library-preparation batches. This would let batch effects be modeled in the next run.
- Rerun the Procrustes concordance test once ITS replicate BC drops well below 1.0.
- Test dispersion separately from location, to split the two components of the PERMANOVA signal.

## [[concepts/soil-metabolite-richness-under-warming-and-substrate-depletion|Soil metabolite richness under warming and substrate depletion]]

- Add the quantitative NOM, metabolomics and proteomics layers from nmdc_arkin. This would test whether the richness drop reflects real depletion rather than detection limits.
- Resolve ChEBI labels for the top differential hits, then run KEGG module enrichment to see which pathways the heated-only and control-only metabolites belong to.
- Check whether the organic-horizon trend (p=0.209) becomes significant with more samples, and whether any per-metabolite hit survives BH-FDR.

## [[concepts/sources-and-prevalence-of-eukaryotic-contamination-in-prokaryote-targeted-metagenomes|Sources and prevalence of eukaryotic contamination in prokaryote-targeted metagenomes]]

- Test whether the algal-plastid versus root-fungal source split holds within batch-controlled aquatic and plant-associated cohorts. This would show whether the matrix differences survive study confounding.
- Extend the within-study design to aquatic and plant-associated studies, to test whether the vegetation and geography effect generalizes beyond soil.
- Re-test the depth association within single studies that record depth. This would show whether the cross-study ρ=−0.29 is real or a study artifact.

## [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses|Spark query scale limits and notebook-session constraints in Lakehouse analyses]]

- Benchmark joins with and without autoBroadcastJoinThreshold = -1 on uniprot_identifier and on mid-size tables. This would show when the setting helps and when it hurts.
- Measure the actual idle-kill threshold on JupyterHub with controlled sleep jobs. This would test whether ~17–25 min is a fixed scheduler limit.
- Rerun the Bacteroidota PUL neighborhood analysis with a full-Spark spatial filter that collects only per-feature aggregates. This would recover the deferred analysis.
- Rerun the ecotype analysis off-peak for all 456 eligible species, logging query time against cluster load.
- Test whether the Parquet read-back path stays under the result-size cap for results well above 1.5 GB.
- Time the presence-matrix extraction on a copy of the gene and junction tables partitioned by genome_id and gene_cluster_id. This would test how much scan time partitioning removes.

## [[concepts/spatial-matching-of-environmental-samples-to-genomes|Spatial matching of environmental samples to genomes]]

- Rerun the copper analysis at 5 km and 20 km. Compare the 116 COGs and the 7,566-sample set with the 10 km result. This tests whether the associations depend on the threshold.
- Export the Spearman ρ values and model residuals to local files. This removes the Spark dependency that blocks the pending checks.
- Compute Moran's I on the residuals. If it is significant, refit with SEVM and see which COG-copper associations survive.
- Report how the share of genomes truly co-located with copper measurements changes with threshold. This addresses the co-location concern at 10 km.

## [[concepts/species-level-conservation-of-metabolic-pathways-across-pangenomes|Species-level conservation of metabolic pathways across pangenomes]]

- Rerun the conservation table for every species with clade assignments anchored to the PROTECT reference genomes, as done for N. mucosa. This would show how far clade definition shifts the figures.
- Add genomes for G. sanguinis, whose 7-genome pangenome is too small to judge conservation. Test whether 7/18 AA conservation holds.
- Compare core-only and all-gene completeness for each of the five species. This would show whether the accessory contribution seen in other reports weakens the strain-equivalence claim.
- Test conserved predictions against growth or fitness data in more than 48 organisms. This would check the untested-clade inflation.

## [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria|Sphingolipid and shared Lpt transport in lipid A-deficient bacteria]]

- Replicate the proteomics with several biological replicates, to test whether lptC2 and CCNA_01217 protein increases hold statistically.
- Run targeted lipidomics with lipid A precursor quantification in 4599, to test whether the sphingolipid pool is maintained or increased without biosynthesis induction.
- Measure LptB ATPase occupancy or competition directly, to test the shared-component mechanism behind the protein accumulation.

## [[concepts/statistical-power-and-database-coverage-gap-for-archaeal-trait-analyses|Statistical power and database coverage gap for archaeal trait analyses]]

- Add environmental archaeal MAGs, especially Thaumarchaeota and Woesearchaeota, to the pangenome. Then re-run the PGLS to test whether the cultured-lineage bias changes the estimate.
- Re-run the power analysis after each coverage increase. Use the updated SE and λ, not the single β of +0.0145, so the required n is not tied to one noisy effect size.
- Report effective N per clade for archaea, as the D3 reporting does for CPR and DPANN, so each analysis states what it can conclude.
- Run phylogenetic-signal analyses on traits that already have more archaeal data, such as niche breadth with 132 genera. This gives interim results while AMR coverage grows.

## [[concepts/structure-fitness-integration-of-mutant-fitness-data-with-predicted-protein-structures|Structure–fitness integration of mutant fitness data with predicted protein structures]]

- Compute per-residue pLDDT and structural features for the 22,303 distinct AF models, then add them as a derived collection. This closes the gap in the entries table.
- Compare structural features of essential genes (6,635) with those of mild-defect genes (29,467) in the 55,454-gene cohort. This is the first direct test of the UC1 question.
- Check whether results hold within single organisms across the 48, to separate organism effects from structural effects.
- Examine the SwissProt-hit genes without an AlphaFold entry to see whether they share a property that biases the cohort.

## [[concepts/study-and-batch-confounding-of-cross-collection-metadata-correlates|Study and batch confounding of cross-collection metadata correlates]]

- Import a many-study raw-read resource, or compute eukaryotic fraction across a broader collection. This would give a properly powered cross-study analysis and close the gap of about 9 studies.
- Fit study-level random effects once multi-study coverage exists. This would test whether power improves over GroupKFold alone.
- Repeat the GroupKFold-by-study comparison for aquatic and host-associated studies. This would test whether the soil-only within-study result extends.
- Rerun the models at workflow_run_id level, excluding pooled runs. This would check how pseudoreplication and label noise affect the estimates.

## [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation|Substrate-dependent Complex I requirement and NDH-2 compensation]]

- Search the ADP1 genome for NDH-2 genes and compare their deletion phenotypes on quinate and glucose. This closes the gap that ADP1 has no NDH-2 growth data.
- Run the `eggnog_mapper_annotations` test of Complex I retention in pca-carrying versus non-aromatic-degrading Acinetobacter species, to ask whether Complex I tracks aromatic catabolism across genomes.
- Measure Complex I fitness on aromatics, acetate, succinate, glucose and lactate within a single organism. This avoids the mixed-architecture problem of ortholog transfer.
- Re-run the NDH-2 presence comparison with more organisms, to see whether the non-significant result (p = 0.52) reflects low power.

## [[concepts/substrate-specificity-of-the-mannose-pts-manxyz-from-genome-wide-fitness|Substrate specificity of the mannose PTS ManXYZ from genome-wide fitness]]

- Run fitness assays of manXYZ and fruA double mutants on mixed fructose and mannose media. This would test whether any cross-talk exists that single-mutant data miss.
- Check the 6 to 10 conditions per gene with fit < -1 beyond the sugars, such as trehalose and sodium chlorite. This would show whether the non-sugar defects are real or polar effects.
- Compare ManXYZ homologs in other bacteria with RB-TnSeq data on mannose and fructose. This would test whether the specificity holds outside E. coli K-12.
- Submit a correction for the GO:0005354 annotation of ManX. This would resolve the annotation conflict.

## [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons|Substudy nesting and feature leakage in pooled-cohort microbiome comparisons]]

- Rebuild ecotypes on a functional (pathway or KEGG) feature matrix, then repeat the held-out-species Jaccard test. This tests whether taxonomic-feature leakage is broken.
- Count substudy × ecotype × diagnosis cells with ≥ 10 samples. This shows whether the stratified within-substudy analysis can be primary.
- Re-verify the substudy count for pathway data before any meta-analysis. This closes the 4-versus-3+1 discrepancy.
- Apply leave-one-species-out refits to other cluster-then-test analyses. See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]] and [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

## [[concepts/support-gene-networks-around-catabolic-pathways|Support-gene networks around catabolic pathways]]

- Run co-purification with Complex I for ACIAD3137 and ACIAD2176 to separate physical accessory roles from indirect connections.
- Add benzoate, catechol and vanillate, plus iron limitation and respiratory inhibitors. This would refine subsystem boundaries and test the NADH-flux hypothesis directly.
- Repeat the support-gene count for other substrates and organisms. This would show whether the 7:1 ratio is general or specific to ADP1 and quinate.

## [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements|Systematic blind spots of flux balance models for condition-specific requirements]]

- Add trace aromatic compounds to the ADP1 minimal-media definition, using measured media composition, and test whether the aromatic-degradation and beta-ketoadipate discordance resolves. This would separate the media explanation from moonlighting.
- Add PQQ biosynthesis, iron homeostasis and respiratory-chain capacity constraints to the ADP1 model and check whether condition-dependent essentiality predictions improve. This addresses the 30/51 quinate-specific genes without mappings.
- Build an NDH-2 deletion mutant in ADP1 and test whether Complex I becomes essential on glucose. This would close the gap left by missing NDH-2 growth data.
- Model Complex I as an all-or-nothing multi-subunit unit, to test whether the threshold effect explains the 0% essentiality prediction.

## [[concepts/taxonomic-and-single-laboratory-coverage-limits-of-exometabolomic-data|Taxonomic and single-laboratory coverage limits of exometabolomic data]]

- Re-run the strain-level tests on the GNPS2 version or Northen lab datasets to see whether multivariate models work once n grows beyond 6.
- Hold medium fixed and compare organisms, or hold organism fixed and compare media, to separate medium from taxon effects.
- Repeat the association analysis with Unk_ metabolites excluded.
- Add consumption data to test how much the production-only record limits conclusions.
- Expand E. coli BW25113 coverage beyond the 12 sulfur-focused observations so it can be matched to Fitness Browser data.

## [[concepts/taxonomic-distribution-and-relative-prevalence-of-xoxf-and-mxaf-methanol-dehydrogenases|Taxonomic Distribution and Relative Prevalence of xoxF and mxaF Methanol Dehydrogenases]]

- Rerun the comparison with a tree-based method, such as phylogenetic generalised least squares on the GTDB tree. This would test whether the GLMM's ~143 : 1 figure holds when phylogeny is modelled explicitly, since the report's correction used only taxonomic random effects. See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].
- Check the xoxF-only phyla for mxaF with a sequence-based search. This would show whether the zero mxaF counts reflect real absence or annotation gaps.
- Look in Acidobacteriota and Gemmatimonadota for the other parts of the lanthanide cassette, to see whether xoxF calls there indicate lanthanide use.
- Resolve Methylomirabilota (3.3 : 1) and Verrucomicrobiota (3.8 : 1) with more genomes, since their ratios are far below the global value.

## [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism|Taxonomic distribution of aromatic-compound catabolism]]

- Run the pangenome mapping and the PICRUSt2 or Tax4Fun prediction proposed above. They would test whether lignin enrichment matches genome-encoded aromatic capacity.
- Recompute per-clade conservation over all genomes of each genus, not only genomes with a catabolic call, to get absolute prevalence. This addresses the denominator limit.
- Test whether Actinomycetota-heavy phthalate-class utilizers separate from Burkholderiales once compound source is controlled. This addresses the source-versus-class confound.

See also [[concepts/co-occurrence-and-modularity-of-catabolic-capacities-across-genomes]], [[summaries/enigma_carbon_census_1__REPORT]] and [[summaries/lignin_community_enrichment__REPORT]].

## [[concepts/taxonomic-resolution-and-reference-database-limits-in-amplicon-profiling|Taxonomic resolution and reference database limits in amplicon profiling]]

- Re-run the lignin-enrichment data with DADA2 exact variants and compare genus assignments to the 97% OTU results. This would show how many OTUs merge distinct species.
- Reclassify the ITS OTUs against UNITE and compare with the NCBI ITS_RefSeq_Fungi assignments. This would test how many environmental taxa the NCBI database misses.
- Run shotgun metagenomics on the SSO samples at the same spatial resolution. This would test taxonomy-based functional inferences and cover the reads lacking genus assignment.
- Compare 16S genus assignment against a second reference database for the SSO reads. This would show whether the 44% genus coverage reflects the database or the short amplicon.

## [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching|Taxonomic synonymy and strain-name collisions in cross-database matching]]

- Compare suffix-stripping with GCA-accession matching on the same BacDive strains. This would show how much of the unmatched strains is a naming artifact and how much is a real absence from GTDB.
- Add the legacy Bacteroides_X rows to ref_taxonomy_crosswalk by name. Then test whether a synonymy layer removes all log₂FC ≈ 28 artifacts across the full taxonomy.
- Audit the other ENIGMA short names for collisions. Use the genus-consistency check against CORAL brick 522 to see how many of the 12 lost linkages can be recovered by accession.
- Test whether a GTDB-version-aware rename table gives the same species set for CMD_IBD and CMD_HEALTHY under successive GTDB releases.

## [[concepts/taxonomy-based-functional-inference-of-biogeochemical-processes-and-the-redox-ladder|Taxonomy-based functional inference of biogeochemical processes and the redox ladder]]

- Run shotgun metagenomics on the same 3×3 grid and test whether denitrification genes peak at M5 and fermentation genes at L9. This would replace trait-based inference with genomic evidence.
- Pair the inferred hotspots with measured nitrate, Fe(II)/Fe(III), sulfate and oxygen at each well. This would test the plume mixing-zone and dead-zone interpretations.
- Quantify how the class-level (78% coverage) and genus-level (21% coverage) redox patterns differ per well. This would size the effect of the coverage gap.
- Extend the trait dictionary to the unclassified 56% of reads, using genome-based traits for the taxa found. This would test whether the genus-level estimates are only lower bounds.

## [[concepts/taxonomy-bridging-between-metagenomic-classifiers-and-reference-pangenomes|Taxonomy bridging between metagenomic classifiers and reference pangenomes]]

- Rerun the ENIGMA community-weighted scores with each ambiguous genus (such as prevotella) resampled across its candidate clades. This would show whether the 380 ambiguous genera change results, as the ~6.5% bound does for NMDC.
- Estimate the PRJNA1084851 bias by comparing the metal resistance of matched genera with a sample of unmatched ones. This would test the upward-bias hypothesis.
- Obtain ENIGMA labels below genus, such as isolate genomes, so species-level bridge testing becomes possible.
- Compare the two NMDC bridge coverage figures on one common sample set and one common unit.

## [[concepts/temporal-stability-of-groundwater-communities|Temporal stability of groundwater communities]]

- Resample the same wells over months to years. This would test whether the 9-day stability holds across seasons and plume shifts.
- Collect repeat sediment cores from the same wells. This would give within-well temporal variance for sediment, which is currently missing.
- Sample sediment and groundwater in the same campaign. This would remove the 18-month confound between material type and time.
- Repeat the Mantel and variance-partitioning analysis with more than two dates. This would show whether the between-well similarity pattern persists.

## [[concepts/thermodynamic-constraint-formulation-in-flux-balance-models|Thermodynamic constraint formulation in flux balance models]]

- Run full MILP TMFA on the 10 diverse organisms. This would test whether the LP relaxation hides direction-locking effects.
- Replace the default 1 µM – 10 mM bounds with organism-specific metabolomics. This would show which reactions cross the feasibility boundary.
- Re-solve the TMFA models with a commercial solver. This would check whether degenerate optima change the result.
- Rerun the carbon-source panel under TMFA with more than 12 conditions. This would resolve why TMFA is reported to block alternative carbon sources despite preserved growth.

## [[concepts/training-set-size-and-the-shift-from-genome-scale-to-gene-specific-predictive-features|Training-set size and the shift from genome-scale to gene-specific predictive features]]

- Train on subsamples of the 46K-pair corpus (for example 7, 100, 1,000 and 10,000 pairs) and track the genome-scale share of grouped SHAP. This would replace the two-point comparison with a curve and locate the transition.
- Test cross-genus generalization and per-condition prediction quality in the large model, since the initial analysis tested neither. Compare the splits with [[entities/xgboost-with-phylogenetic-blocked-cross-validation]].
- Apply the |r|>0.8 grouping to the NB07 model, so that the condition-specific KOs are also reported at group level.
- Examine why concordance with Fitness Browser is weak (1.19× enrichment), for example by restricting to conditions with many genomes.

## [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits|Transcript-protein discordance and single-replicate proteomics limits]]

- Analyse the replicated outer-membrane proteome planned for summer 2026. It would give per-protein variance and tell us whether the LptD and LptE declines and the lptC2 increase exceed noise.
- Run Western blots on lptC2-tagged and Pal-tagged strains. This would test the lptC2 and Pal-Tol protein changes without relying on proteomics alone.
- Compare lptC2 across all three strains with replicates. This would settle how much of the +1.08 is recovery from the earlier -0.42 and how much is net induction.
- Obtain a wild-type value for MsbA-like CCNA_00307. At present it was detected only in one strain, so no direction can be computed.

## [[concepts/transposon-insertion-fitness-versus-gene-deletion-lethality|Transposon insertion fitness versus gene deletion lethality]]

- Examine the 211 knockout-essential/TnSeq-dispensable genes to learn which tolerate partial function. This tests the partial-function explanation.
- Compare insertion position within genes against fitness. This tests the truncated-protein and upstream-domain mechanism.
- Run condition-matched TnSeq against the knockout media. This would separate condition effects from method effects.
- Replace the binary threshold with a continuous predictor, such as essentiality_fraction or fitness, and compare it with knockout lethality directly. No threshold gave positive kappa, so this tests whether the binary cut is the problem.

## [[concepts/universal-positivity-and-chemistry-specific-magnitude-of-metal-cross-resistance|Universal positivity and chemistry-specific magnitude of metal cross-resistance]]

- Fit PGLS or independent-contrast models to the pair-by-organism correlations. This would test whether the moderate conservation (Mantel r = 0.23) survives phylogenetic non-independence.
- Add non-metal stress conditions (for example osmotic or oxidative) from the same organisms. This would separate universal metal cross-resistance from general stress response. See [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].
- Model concentration as a covariate, or restrict to matched doses. This would test the dose-response caveat.
- Subsample organisms to equal experiment counts. This would show whether the 3-to-112 range drives per-organism deviations from the consensus.
- Test whether the iron-sulfur cluster explanation for Fe-Zn holds. Compare iron-sulfur biogenesis gene fitness in the six organisms with the pair. See also [[concepts/organism-coverage-and-attrition-in-cross-organism-fitness-conservation-analyses]].

## [[concepts/universal-versus-variable-gene-essentiality-across-bacteria|Universal versus variable gene essentiality across bacteria]]

- Test whether the 859 universal families remain essential in organisms outside the 48 (the synthesis report poses this for 43 organisms [src: conservation_fitness_synthesis]). Use RB-TnSeq or essentiality calls from other collections. This would show whether the set is truly universal or specific to this panel.
- For the 4,799 variable families, link essential versus non-essential calls to paralog counts, pathway redundancy and accessory-gene presence. This would test the context explanation, which the report proposes.
- Compare the 859 families with computational minimal sets such as Gil et al. (2004) and Duffield et al. (2010) family by family. This would show which differences come from the experimental criterion and which from genome size.
- Check the 839 single-copy universal families against known antibiotic targets and human homologs. This would test the broad-spectrum target claim.
- Look at the 7,084 essential genes with no orthologs in other FB organisms. They may be orphan essentials, or they may reflect orthology-calling limits.

## [[concepts/unknown-function-genes-in-niche-differentiated-accessory-genomes|Unknown-function genes in niche-differentiated accessory genomes]]

- Run the AlphaFold or domain analysis on the S-category genes, as the report proposes, to learn what the largest-effect category does.
- Re-run the ecotype test on the 62% of gene clusters without COG annotations, using an independent annotation source. This would show whether the housekeeping bias hides adaptive genes.
- Check whether the 462 unannotated Bacillota_B OGs overlap the S-category genes that differ between ecotypes. This would link the two lines of evidence.

## [[concepts/unmeasured-wet-lab-metadata-as-a-limit-on-contamination-correlates|Unmeasured wet-lab metadata as a limit on contamination correlates]]

- Acquire per-study protocols (extraction kit, host-depletion method, size fraction), either supplied by users or from a collection that records them, and rerun the correlate analysis with them. This closes the gap left by the unmeasured residual. [src: euk_in_prok_correlates]
- Check whether other collections on the Data Lakehouse record filtration or library-prep fields, since NMDC's `has_filtration` is uniformly false.
- Test extraction kit and sample matrix together on a subset with known kits, to compare against the Sobolev et al. finding.

## [[concepts/unstudied-protein-families-and-the-literature-defined-dark-proteome|Unstudied protein families and the literature-defined dark proteome]]

- Cross-reference the VIMSS links with Fitness Browser data to find fitness-important genes that lack literature. This would connect dark families to phenotype evidence.
- Use AlphaFold structure prediction and domain annotation on the 5,218 dark families. This would move from identifying dark families to inferring function.
- Repeat the dark-family count at other identity thresholds. This would show how far the 5,218 figure depends on the 50% cutoff.
- Check a sample of dark families against full-text literature searches. This would estimate how many are missed by text mining.

## [[concepts/untapped-cross-program-synergy-use-cases-for-environmental-and-clinical-microbiology|Untapped cross-program synergy use cases for environmental and clinical microbiology]]

- Validate UC2–UC5 against the live cluster with short SQL probes. This would confirm value-space overlap and expose join-recipe corrections, and UC3 is the cheapest to start.
- Promote UC1 into its own project, seeded with the validated 55,454-gene cohort, to test structural signatures of high-fitness-impact genes.
- Run UC5 as a coverage census of ENVO terms on NMDC biosamples. It would show where ontology coverage breaks and would support UC4's environmental context.
- Check the "largely untapped" NMDC multi-omics claim with a direct usage count, since it now rests on agent memory.

## [[concepts/validating-metal-tolerance-predictions-against-culture-collection-metadata|Validating metal-tolerance predictions against culture-collection metadata]]

- Re-run the heavy-metal comparison with a larger contamination set, or with a better species bridge, to narrow the interval on d=1.00 (gap: n=10, at the detection limit).
- Predict multi-metal tolerance across 27K species with the KEGG/PFAM mapping approach and validate it against BacDive polymetallic isolation environments. This closes the n=20 power gap.
- Pull MIC and growth-inhibition records from the BacDive API to replace the 24-record utilization subset.
- Measure how many of the 55,107 unmatched strains a synonym-aware bridge would recover, and whether the recovered strains differ in isolation environment.

## [[concepts/validity-of-curated-metal-gene-annotation|Validity of curated metal-gene annotation]]

- Draw 100 random annotated gene clusters and check them by BLAST against reference sequences. Report the false-positive rate for each metal type. This closes the gap left by the absence of manual validation.
- Rerun the main analysis without the "other" category. This would show how much the weaker hits drive the result.
- Add substrate-binding-aware evidence for ZnuA- and MntH-type importers, such as curated transporter families. This would close the clan gap, since only 10/140 primary KOs have clan support.

## [[concepts/warming-response-of-soil-microbial-community-composition|Warming response of soil microbial community composition]]

- Test the mineral horizon with more samples or a genus-level test, to see whether the absence of phylum-level change reflects low power or a true lack of response.
- Test the near-threshold phyla (Verrucomicrobia, Cyanobacteria, Proteobacteria) in a larger sample set.
- Resolve Actinobacteria to sub-clade level and compare it with the published isolate pangenome results, to test the sub-clade selection hypothesis.
- Fit a treatment-within-horizon PERMANOVA, to separate the treatment effect from the large horizon effect.

## [[concepts/within-species-metabolic-ecotypes-from-pathway-variation|Within-species metabolic ecotypes from pathway variation]]

- Test ecotype-environment association with phylogenetic correction, for example within-clade tests in *Salmonella* and *Phenylobacterium*. This would address the phylogenetic confounding caveat.
- Replace NCBI isolation source with BacDive or GTDB environmental labels, and retest the marine species. This would show whether the null results come from metadata resolution.
- Run the planned AlphaEarth niche-breadth analysis (H2) on the 28% of genomes with embeddings. Check first that the sample is large enough.
- Repeat the ecotype count at several dendrogram cut thresholds and check whether the openness correlation holds. This would address the fixed 50% threshold.
- Compare gene-content clustering with pathway clustering in marine species. This would test whether GapMind misses the signal.
- Carry out the proposed within-species *Pseudomonas* pathway analysis to look for niche-adapted subpopulations.

## [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization|Within-species subclade segregation of plant association and host specialization]]

- Populate or rebuild GTDB tree distances for the 47 missing species, such as *Bradyrhizobium japonicum* and *Xylella taiwanensis*, and rerun the subclade scan to estimate the effect across all 65 species.
- Run accessory-gene-content tests inside the significant subclades of Xanthomonas, Mesorhizobium and Agrobacterium to check whether accessory cassettes track subclades.
- Pull gene-cluster-by-genome data to build gene-content trees and compare them with species trees, to find HGT-driven incongruences.
- Add host annotation for the species that were too sparsely annotated for the host test, and test whether *Ralstonia solanacearum* gains Bonferroni support.
- Add automatic ID-format validation to subclade joins so that all-NaN merges fail loudly.

## [[concepts/within-species-variation-of-antimicrobial-resistance-gene-content|Within-species variation of antimicrobial resistance gene content]]

- Test the openness hypothesis by recomputing variability after removing genes below the 5% threshold, or by using a fixed-size genome subsample per species. This would show whether rare-gene accumulation causes the negative correlation.
- Re-estimate rare-class fractions after excluding singleton clusters supported by one annotation source. This would show how much of the 51.3% rare share is annotation artifact.
- Compare prevalence-class fractions within the clinically dominated species against less-sampled species. This would separate biology from sampling skew.
- Add a validation set of resistance mechanisms missing from AMRFinderPlus to estimate how much variation goes undetected.

## [[concepts/within-study-environmental-drivers-of-eukaryotic-dna-in-soil-metagenomes|Within-study environmental drivers of eukaryotic DNA in soil metagenomes]]

- Repeat the within-study design in the aquatic and plant-associated NMDC studies. This tests whether the effect generalizes beyond soil, and whether the algal-plastid versus root-fungal source split holds within batch-controlled cohorts.
- Test whether sampling campaign explains the vegetation and site effects. Add campaign as a covariate or stratum in the NEON study. This addresses the sub-batch confounding caveat.
- Compare the Arctic tundra sites with other cold or peat sites, to see whether the high fraction follows vegetation or climate.

