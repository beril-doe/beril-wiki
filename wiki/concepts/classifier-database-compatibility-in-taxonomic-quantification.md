---
type: "Concept"
description: "How differences in taxonomic classifiers, reference databases, feature namespaces and taxon-name keys limit cross-study comparison of taxonomic abundances and the conclusions drawn from them."
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/ecotype_analysis__REPORT.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pitfalls.md"]
---
# Classifier database compatibility limits cross-study taxonomic quantification

Cross-study taxonomic quantification is only comparable when classifiers have sufficiently compatible reference databases, taxonomic scopes, and reporting behavior. The same biological reads can produce very different apparent taxonomic abundances when one database represents eukaryotes or plastids and another is restricted primarily to prokaryotes. [src: euk_in_prok_correlates]

This issue is distinct from ordinary classifier disagreement: a database that cannot represent a taxon cannot provide evidence that the taxon is absent. Consequently, cross-study comparisons should treat classifier identity and database composition as analytical variables, not merely software metadata. [src: euk_in_prok_correlates]

## Evidence from the NMDC eukaryotic-read analysis

The [[summaries/euk_in_prok_correlates__REPORT]] analysis quantified eukaryotic reads across 2,759 NMDC ReadbasedAnalysis runs from 9 studies using native `nmdc.results` classifications. [src: euk_in_prok_correlates]

GOTTCHA2 detected eukaryotic reads in 77% of the 2,759 runs, with a median eukaryotic fraction of 2.7%, a mean of 13.3%, and 20% of runs exceeding 20% eukaryotic reads. [src: euk_in_prok_correlates]

Among runs with detectable eukaryotic signal, plastid sequences represented a median 100% of that signal, indicating that the observed environmental eukaryotic component was dominated by plant or algal chloroplast DNA rather than animal-host DNA. [src: euk_in_prok_correlates]

Kraken2 and Centrifuge produced approximately 0 domain-level Eukaryota signal because their NMDC reference databases were prokaryote-restricted; Kraken2's only eukaryotic kingdom was Metazoa/human. This left GOTTCHA2 as the only usable estimator of eukaryotic fraction in this collection. [src: euk_in_prok_correlates]

This result supports the interpretation that the near-absence of a metazoan or host signal in the Kraken2 and Centrifuge outputs was not interchangeable with GOTTCHA2's eukaryotic estimate, because the classifiers had different representational coverage. [src: euk_in_prok_correlates]

GOTTCHA2 was therefore the only usable estimator of eukaryotic fraction in this analysis. Its absolute values are database-dependent and should be interpreted as relative or ordinal rather than calibrated absolute contamination. The report proposes absolute calibration of the GOTTCHA2 eukaryotic fraction against a spike-in or SPF estimate as the step needed to move from ordinal to calibrated contamination estimates. [src: euk_in_prok_correlates]

## Consequences for environmental comparisons

The apparent environmental pattern was strong in the GOTTCHA2-derived response: aquatic freshwater samples had 99.5% eukaryotic detection and a plastid share of 1.00, terrestrial soil samples had 55.7% detection and a plastid share of 0.43, and plant-root samples had 100% detection and a plastid share of 0.03. [src: euk_in_prok_correlates]

These findings support [[concepts/environment-embedding-geography]] only after classifier and database compatibility are established, because an environmental contrast can reflect differences in detectable taxonomic space rather than differences in biological composition. [src: euk_in_prok_correlates]

The [[summaries/ecotype_analysis__REPORT]] analysis **refines** this safeguard: environmental representation can also be incomplete before taxonomic classification, because AlphaEarth embeddings covered only 28.4% of genomes in an analysis of 13,381 genomes across 224 species, yielding correlation results for 172 species. [src: ecotype_analysis]

The [[summaries/ecotype_env_reanalysis__REPORT]] **refines** that limitation further: using genome-level environmental classifications and a consistent full-embedding methodology, environmental species did not have stronger environment–gene-content correlations than human-associated species (one-sided Mann–Whitney U, U=1536, p=0.83). The fraction of environmental genomes likewise showed no relationship to partial-correlation strength (rho=-0.085, p=0.25), indicating that the confirmed clinical sampling bias did not explain the weak signal. [src: ecotype_env_reanalysis]

The eukaryotic fraction differed by matrix in a Kruskal–Wallis test with H=77.8 and p=1.3×10⁻¹⁷, and all pairwise matrix contrasts were significant after BH-FDR, where BH-FDR denotes the Benjamini–Hochberg false-discovery-rate procedure. [src: euk_in_prok_correlates]

However, these statistical results describe variation in one classifier-derived response and do not establish that the reported fractions are absolute or directly comparable across independently processed datasets. [src: euk_in_prok_correlates]

The report summarizes its cross-study modeling as showing that environment explained no more variance than `study_id` alone. Its own table is not fully consistent with that wording: random cross-validation gave R²=0.35 for environment and R²=0.24 for a `study_id`-only model labelled the batch ceiling. The report's argument rests instead on environment being ~80–100% nested within a single study and on held-out-study performance: GroupKFold out-of-study validation gave R²=−0.30 for environment and R²=−0.39 for environment plus sequencing. [src: euk_in_prok_correlates]

GroupKFold is a cross-validation design in which complete studies are held out as groups, so these results show that cross-study environmental prediction was not portable even when sequencing metadata were added. [src: euk_in_prok_correlates]

The out-of-study detection AUC was 0.56, approximately chance, further weakening the interpretation of the cross-collection environmental association as a transferable biological rule. [src: euk_in_prok_correlates]

This refines [[concepts/cross-cohort-microbiome-portability]]: portability requires not only comparable sample metadata and validation splits, but also compatible classifier reference databases and taxonomic scopes. [src: euk_in_prok_correlates]

The ecotype analysis **supports** this portability caution at a different measurement layer: phylogeny dominated whole-genome gene-content similarity in most species, while significant environment effects were uncommon, suggesting that environmental signal may be confined to particular gene subsets rather than being reliably recoverable from genome-wide similarity. [src: ecotype_analysis]

The reanalysis **supports** the within-method version of this caution but changes the interpretation of sampling bias: environmental species had a median partial correlation of 0.051 versus 0.084 for human-associated species, while Mixed/Other species had the highest median, 0.109. The report presents unequal genome counts and heterogeneous sampling campaigns as possible explanations, not demonstrated causes. [src: ecotype_env_reanalysis]

## Database compatibility is part of the measurement model

A classifier-derived abundance is a measurement produced jointly by sequencing reads, the classifier, its reference database, and its taxonomic reporting scheme. [src: euk_in_prok_correlates]

In this analysis, the response was GOTTCHA2 relative eukaryotic abundance, defined as Eukaryota plus plastid abundance at superkingdom rank for each ReadbasedAnalysis run. [src: euk_in_prok_correlates]

Because Kraken2 and Centrifuge were prokaryote-restricted in this NMDC deployment while GOTTCHA2 was plastid- and eukaryote-aware, their outputs could not be treated as interchangeable measurements of eukaryotic fraction. [src: euk_in_prok_correlates]

This supports [[concepts/taxonomic-resolution-dependent-functional-inference]] and [[concepts/environmental-resistome]] at the measurement level: downstream ecological or functional conclusions inherit the representational limits of the upstream database. [src: euk_in_prok_correlates]

The ecotype analysis **refines** this claim by showing that environmental conclusions also inherit limitations in environmental embeddings and metadata: geographic coordinates were often missing or imprecise, and partial correlations assume linear relationships between distance matrices. [src: ecotype_analysis]

The ecotype reanalysis **supports** the need to separate measurement layers: its environmental-versus-human comparison remained null within one methodology, but it reports an overall median partial correlation of 0.081 versus 0.003 in the original analysis, a reported 27x difference. The original ecotype analysis report itself gives the median environment partial correlation as 0.0025. That discrepancy is recorded here, not reconciled. The reanalysis lists several key methodological differences: no downsampling (all genomes with embeddings rather than diversity-maximizing downsampling), larger sample sizes, and different genome sets. It does not isolate which of these produces the gap. Absolute correlations therefore cannot be compared across the two methodologies, even though the within-method group comparison is valid. [src: ecotype_env_reanalysis, ecotype_analysis]

The same limitation applies to negative evidence: an approximately 0 Eukaryota signal from a prokaryote-restricted database cannot by itself demonstrate that eukaryotic reads were absent. [src: euk_in_prok_correlates]

## Cross-classifier projection in gut-microbiome cohorts

The [[summaries/ibd_phage_targeting__REPORT]] project **extends** the compatibility problem from eukaryotic-fraction estimation to ecotype projection. Its ecotype reference was trained on 8,489 MetaPhlAn3 samples (`fact_taxon_abundance`, CMD_HEALTHY + CMD_IBD cohorts), where MetaPhlAn3 supplies marker-gene relative abundance. [src: ibd_phage_targeting, discoveries]

The held-out Kuehl_WGS cohort was processed with a different taxonomic classifier, Kaiju NCBI-NR read classification. Projecting it onto the MetaPhlAn3-trained embedding therefore crossed classifier namespaces. [src: discoveries, ibd_phage_targeting]

All 26 Kuehl_WGS samples (23 unique patients) were projected onto the K = 4 reference through a synonymy layer that normalized 262 unique Kaiju-classified species to 97 canonical species in the training feature space. Under LDA on pseudo-counts (latent Dirichlet allocation, a topic model), the UC Davis samples were distributed as follows: E0 (diverse commensal) 7 samples (27 %), E1 (Bacteroides2 transitional) 11 samples (42 %), E2 (*Prevotella copri* enterotype) 0 samples, and E3 (severe Bacteroides-expanded) 8 samples (31 %). The digest describes these as plausible biological proportions despite the classifier mismatch. [src: ibd_phage_targeting, discoveries]

The same mismatch exposed an asymmetry between ecotype methods (see [[concepts/ecotype-clustering-validity]]). LDA on pseudo-counts was robust because absence is treated as not-detected; the project report describes it as handling the 54 % of Kuehl feature rows outside the training feature space. GMM on CLR + PCA (a Gaussian mixture model on centred-log-ratio-transformed, principal-component-reduced abundances) was fragile. The digest states that Kuehl detects only 54 % of training species, that 70 % of training species have no Kuehl detection, and that the CLR transform imputes these zeros with a small pseudocount. All 26 Kuehl samples then projected to E3 at GMM confidence > 0.97, which the sources call an artifact, not biology. [src: discoveries, ibd_phage_targeting]

The project therefore made LDA the primary Kuehl projection call and treated GMM as advisory, and it lists the Kaiju vs MetaPhlAn3 classifier mismatch as a limitation on confidence in UC Davis ecotype calls. The digest generalizes this into a recommendation: when projecting across classifier namespaces, pseudo-count or sparse-data-robust methods (LDA, MMvec, etc.) should be primary and CLR-based methods (ANCOM-BC projection, GMM on CLR) advisory at best. It applies this to any pairing, such as MetaPhlAn ↔ Kraken, MetaPhlAn ↔ Kaiju, or 16S ↔ WGS. That generalization is extrapolated from a single Kaiju-to-MetaPhlAn3 projection rather than tested across those pairings, so it should be read as a hypothesis for the other pairings. [src: ibd_phage_targeting, discoveries]

This **refines** the NMDC eukaryotic-read lesson. There, a scope-restricted database produced near-zero signal for a whole taxon class. Here, incomplete feature overlap between classifier namespaces distorted a downstream compositional transform, so the robustness of the analysis method to sparse, non-overlapping features becomes part of the compatibility check. [src: euk_in_prok_correlates, ibd_phage_targeting, discoveries]

Downstream patient-level calls inherit the mismatch. Per-patient target presence used Kuehl_WGS Kaiju Tier-A pathobiont presence at ≥0.001 relative abundance, and the report flags these Kaiju-based Tier-A presence calls as lower confidence than the MetaPhlAn3-based CMD analyses. [src: ibd_phage_targeting]

Classifier repeatability is a separate question from cross-classifier compatibility. Patient 1112's 2 resequencing replicates of the same biological sample gave Tier-A Spearman ρ = 1.000, which the report uses as a Kaiju reliability validation of the technical-noise floor rather than as a longitudinal comparison. This single-patient check **supports** within-classifier repeatability but does not address the Kaiju–MetaPhlAn3 namespace mismatch. [src: ibd_phage_targeting]

Held-out cohorts that share the training classifier avoid this layer of mismatch. HMP2 was absent from the CMD_IBD training set (`HMP_2019_ibdmdb` was not in the CMD_IBD substudy list), making it a genuinely held-out cohort in the same MetaPhlAn3 classifier namespace as the training data. This **refines** [[concepts/cross-cohort-microbiome-portability]] by separating cohort hold-out from classifier hold-out. [src: ibd_phage_targeting]

Reference coverage also limits viral taxonomy. HMP2 viromics left 80 % of observations at an "Unknown" family classification under VirMAP, so most phage observations could not be linked to a target host. In-vivo phage-family correlations were modest (all |ρ|≤0.18). *H. hathewayi* and *M. gnavus* showed negative correlation with the dominant "Unknown" phage family, a category that reflects the family-classification gap rather than a single biological family. The Tier-A × phage-family correlations (*E. coli* × Podoviridae +0.18, × Myoviridae +0.13) are restricted to the classifiable 20 %. The report treats re-running VirMAP/MARVEL with newer phage reference databases as out of scope. This limits the evidence available to [[concepts/phage-therapy-evidence-translation]]. [src: ibd_phage_targeting]

## Reference coverage and taxonomy-key reconciliation

The [[summaries/lignin_community_enrichment__REPORT]] project shows the same representational limit for fungal amplicons. Because the standard UNITE ITS database could not be downloaded, ITS taxonomy was assigned by BLAST against NCBI ITS_RefSeq_Fungi (19,375 reference sequences). The report considers genus-level assignments more reliable than finer assignments and notes that this reference may underrepresent environmental taxa and may miss rare or novel taxa. This **supports** the negative-evidence principle above: taxa absent from the reference cannot be shown absent from the community. [src: lignin_community_enrichment]

In [[summaries/microbeatlas_metal_ecology__REPORT]], the community-weighted mean (CWM) metal-resistance metric covered only the 16.8% of reads from OTUs whose genus-level SILVA taxonomy could be matched to GTDB AMR annotations; the remaining ~83% of reads were excluded. If uncovered genera have systematically different metal resistance profiles (e.g., if they are predominantly metal-sensitive), CWM would be biased upward. The report's results give 1.01–1.83 as the CWM range, although its coverage-limitation note refers to the same values as between-sample variance in CWM. The report describes this between-sample spread and the correlation with known contamination status (FW215/FW216 in plume) as consistent with real biology. However, robustness to covered-read fraction has not been formally tested, and the report recommends correlating per-sample CWM with per-sample covered-read fraction as a diagnostic before further use. [src: microbeatlas_metal_ecology]

*Citrobacter* and *Thermodesulfovibrio* were not detected in that analysis. The report offers detection limits or mismatched genus names under SILVA nomenclature as possible explanations, so this null result cannot distinguish biological absence from a naming incompatibility (see [[concepts/taxonomic-nomenclature-reconciliation]]). [src: microbeatlas_metal_ecology]

By contrast, [[summaries/nmdc_community_metabolic_ecology__REPORT]] reported high taxonomy-bridge quality to GTDB pangenome species: mean bridge coverage was 94.6%, all 220 samples passed the 30% QC threshold, and 92% of samples mapped ≥85% of community abundance. [src: nmdc_community_metabolic_ecology]

That bridge still involved a resolution choice. For ~1,352 Centrifuge taxa matching multiple GTDB clades (same genus, multiple species), one representative clade was selected by alphabetical tiebreaking on `gtdb_species_clade_id`. The report bounds the sensitivity of community completeness scores by noting that these genus-proxy-ambiguous taxa account for ~6.5% of mapped abundance. The project also summarized the 3 NMDC read-based classifiers (kraken, centrifuge, gottcha) by total rows, species-rank fraction, and file counts. [src: nmdc_community_metabolic_ecology]

Even within one classifier, database vintage matters. The pitfalls digest reports that cross-cohort analyses pivoting on `taxon_name_original` or any string key can silently segregate the same species into two non-overlapping rows when cohorts use different MetaPhlAn3 DB vintages or curatedMetagenomicData processing stages. In the `~/data/CrohnsPhage` integrated mart, three divergences were observed. First, short names and full-lineage strings were exported from the same database. Second, GTDB r214+ genus renames such as `Bacteroides vulgatus` (CMD_HEALTHY lineage) ↔ `Phocaeicola vulgatus` (CMD_IBD short name) caused the same NCBI taxid to be treated as separate species. Third, other reclassification splits included `Eubacterium rectale` → `Agathobacter rectalis`, `Ruminococcus gnavus` → `Mediterraneibacter gnavus`, several *Clostridium* species → *Enterocloster* / *Hungatella* / *Erysipelatoclostridium*, and `Lactobacillus mucosae / ruminis` → *Limosilactobacillus / Ligilactobacillus*. [src: pitfalls]

Because CMD_IBD uses modern names and CMD_HEALTHY uses legacy names in that mart, a naive pivot gives log₂FC ≈ 28 (≈ 2.68 × 10⁸ fold) for every renamed species, as one cohort's mean abundance collapses to pseudocount. This **supports** treating database version and name normalization as part of the measurement model. It is relevant to any analysis that combines those two cohorts, including the ecotype training set described above. [src: pitfalls, ibd_phage_targeting]

Taxonomic rank of the abundance key is a further compatibility variable. Both the NMDC `covstats_taxonomy_rollup` and Planet Microbe `run_to_taxonomy` abundance tables key on a `taxonomy.name` that is species-level, not genus-level, which bears on [[concepts/taxonomic-resolution-dependent-functional-inference]]. [src: pitfalls]

## Analytical safeguards

Cross-collection contamination or eukaryotic-signal analyses should control for study or batch using GroupKFold by study, or should rely on within-study contrasts where classifier, database, and laboratory processing are held approximately constant. [src: euk_in_prok_correlates]

The report's within-study NEON analysis provides the stronger design: among 1,186 runs from one sampling program with a constant protocol and batch, local vegetation was associated with eukaryotic fraction at H=119.1 and p=7.6×10⁻²¹, and geography differed across 47 sites at H=310.4 and p=2.4×10⁻⁴⁶. [src: euk_in_prok_correlates]

A model using local environment and geography achieved within-study five-fold R²=+0.17 ± 0.06, contrasting with the cross-study out-of-study R²=−0.30; this supports a fine-scale environmental signal under approximately constant measurement conditions, while leaving possible sub-batch confounding. [src: euk_in_prok_correlates]

The analysis also avoided biosample-level pseudo-replication by working at the `workflow_run_id` level, because 1,067 of 2,759 runs were pooled from multiple biosamples. [src: euk_in_prok_correlates]

This data-structure choice complements [[concepts/cross-tenant-data-bridging]], where correct joins between workflow results, biosamples, and studies are necessary before classifier compatibility can be evaluated. [src: euk_in_prok_correlates]

For environmental-genome comparisons, the ecotype analysis **supports** the analogous use of direct environmental metadata and alternative embedding distances, and recommends testing specific COG categories rather than relying only on whole-genome gene content. [src: ecotype_analysis]

## Tensions

The data show both a strong matrix association and poor cross-study generalization: matrix contrasts were statistically significant, but the out-of-study environment model had R²=−0.30 and detection AUC=0.56. [src: euk_in_prok_correlates]

This is not a contradiction between the classifier and the ecological result; it is a tension between within-collection association and transportable inference, with classifier/database compatibility and study structure among the factors that must be controlled. [src: euk_in_prok_correlates]

The ecotype analysis presents a related but non-identical limitation: it found that phylogeny generally dominated environmental similarity as a predictor of genome-wide gene-content similarity, whereas the present analysis detected strong within-matrix classifier-derived environmental associations. These results cannot be directly reconciled because they use different responses, data structures, and environmental representations. [src: ecotype_analysis, euk_in_prok_correlates]

The ecotype reanalysis **refines** this tension rather than resolving it: its genome-level environmental comparison also found no stronger correlations for environmental species (p=0.83), but it reported a 27x higher overall median partial correlation than the original analysis. It lists full-genome extraction without downsampling among several methodological differences rather than demonstrating it as the cause. Its 0.003 comparator also differs from the 0.0025 median that the original ecotype analysis reports. The discrepancy remains open, so the absolute correlation difference must not be interpreted as a biological contradiction. [src: ecotype_env_reanalysis, ecotype_analysis]

The two IBD sources describe the Kuehl feature overlap differently. The project report states that 54 % of Kuehl feature rows fell outside the training feature space, whereas the discoveries digest states that Kuehl detects only 54 % of training species and that 70 % of training species have no Kuehl detection. The denominators differ (Kuehl features versus training species), and the digest's two percentages are not obviously compatible with each other; the discrepancy is recorded here rather than resolved. [src: ibd_phage_targeting, discoveries]

## Open Directions

- Reclassify the same raw reads with matched, eukaryote-aware Kraken2, Centrifuge, and GOTTCHA2 databases, then use paired agreement analyses to determine which environmental contrasts persist after database scope is harmonized. [src: euk_in_prok_correlates]
- Build a study-held-out benchmark using the 9 NMDC studies and GroupKFold, with classifier identity and reference-database version as recorded covariates, to test whether environmental prediction improves after measurement compatibility is controlled. [src: euk_in_prok_correlates]
- Compare classifier-derived eukaryotic fractions with targeted plastid, fungal, and protist markers in the 1,186-run NEON subset, using within-study models to ask whether the GOTTCHA2 signal tracks distinct biological sources or database-specific detection. [src: euk_in_prok_correlates]
- Reconstruct pooled-run metadata from all contributing biosamples rather than the representative `MIN(biosample_id)` record, then test whether metadata-label uncertainty changes the within-study vegetation and geography associations. [src: euk_in_prok_correlates]
- In the 172-species ecotype subset, compare direct environmental metadata and alternative embedding distances with classifier-compatible taxonomic measures, then test whether specific COG categories recover environmental effects missed by whole-genome similarity. [src: ecotype_analysis]
- Compare downsampled and full-genome gene-cluster extraction on the same species, controlling genome count and missingness, to identify the source of the 27x partial-correlation discrepancy before comparing absolute environmental effects. [src: ecotype_env_reanalysis]
- Recompute the Kuehl–training feature overlap with explicit denominators (Kuehl features, training species, abundance-weighted) to reconcile the reported 54 % and 70 % figures. Then re-classify HMP2 with Kaiju and rerun LDA and GMM projection to test whether the GMM E3 artifact is attributable to classifier namespace rather than cohort. [src: ibd_phage_targeting, discoveries]
- Correlate per-sample CWM with covered-read fraction in the metal-ecology samples, as the report recommends. Separately, search the raw OTU taxonomy for *Citrobacter* and *Thermodesulfovibrio* under alternative SILVA genus names to test whether their non-detection reflects naming mismatches or detection limits. [src: microbeatlas_metal_ecology]
- Re-score community completeness under alternative tiebreaks for the ~1,352 genus-proxy-ambiguous Centrifuge taxa to test sensitivity directly rather than relying on the ~6.5% abundance bound. [src: nmdc_community_metabolic_ecology]
- Re-assign the lignin-enrichment ITS reads against UNITE when available and compare genus- and finer-level calls with the NCBI ITS_RefSeq_Fungi assignments to estimate how many rare or novel taxa the substitute reference missed. [src: lignin_community_enrichment]
