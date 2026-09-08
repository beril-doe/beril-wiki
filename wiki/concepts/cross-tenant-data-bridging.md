---
type: Concept
description: Schema bridges require provenance, identifier, value-space, and observability
  validation before reuse claims are interpretable.
sources:
- id: berdl_data_atlas
  resource: ../summaries/berdl_data_atlas__REPORT.md
  title: berdl data atlas
- id: caulobacter_fur_lipida_loss
  resource: ../summaries/caulobacter_fur_lipida_loss__REPORT.md
  title: caulobacter fur lipida loss
- id: cofitness_coinheritance
  resource: ../summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
- id: ecotype_env_reanalysis
  resource: ../summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
- id: enigma_carbon_census_1
  resource: ../summaries/enigma_carbon_census_1__REPORT.md
  title: enigma carbon census 1
- id: euk_in_prok_correlates
  resource: ../summaries/euk_in_prok_correlates__REPORT.md
  title: euk in prok correlates
- id: field_vs_lab_fitness
  resource: ../summaries/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: genotype_to_phenotype_enigma
  resource: ../summaries/genotype_to_phenotype_enigma__REPORT.md
  title: genotype to phenotype enigma
- id: ibd_phage_targeting
  resource: ../summaries/ibd_phage_targeting__REPORT.md
  title: ibd phage targeting
- id: nmdc_context_audit
  resource: ../summaries/nmdc_context_audit__REPORT.md
  title: nmdc context audit
- id: paperblast_explorer
  resource: ../summaries/paperblast_explorer__REPORT.md
  title: paperblast explorer
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
- id: prophage_ecology
  resource: ../summaries/prophage_ecology__REPORT.md
  title: prophage ecology
- id: webofmicrobes_explorer
  resource: ../summaries/webofmicrobes_explorer__REPORT.md
  title: webofmicrobes explorer
title: Schema-Level Bridges and Validated Cross-Tenant Data Integration
---
# Schema-Level Bridges and Validated Cross-Tenant Data Integration

## Scope

Cross-tenant integration has four evidence states: shared schema keys, overlapping values, an executable join, and a scientifically interpretable result. Schema-level bridges indicate structural compatibility, not valid identifier overlap, biological equivalence, or documented use. [^berdl_data_atlas] A shared column or declared join key may differ in meaning, format, provenance, namespace, or value space; a syntactically executable SQL join is therefore only a validation starting point. [^berdl_data_atlas]

The [berdl_data_atlas__REPORT](../summaries/berdl_data_atlas__REPORT.md) inventories 1,740 deduplicated tables across 119 databases, 17 tenants, and 10 funding agencies or programs, identifying 536 unordered cross-tenant bridges at tenant-by-topic-cell granularity through 29 canonical keys. [^berdl_data_atlas] The keys span genome, taxonomy, sample, annotation, pathway, biochemistry, protein, phage, literature, and workspace relationships. `sample_id` occurs across 10 tenants; `genome_id` and `ncbi_taxon_id` across 9; `feature_id` across 9; and `ec_number` across 8. [^berdl_data_atlas] Some bridges share up to 7 keys, including `kbase.pathway`–`kescience.pathway`, `kescience.pathway`–`phagefoundry.mobile_phage`, and `refdata.structural`–`kescience.structural`. [^berdl_data_atlas] These counts describe potential connectivity, not demonstrated value overlap or realized analytical use.

The [pitfalls](../summaries/pitfalls.md) **refines** this framework into provenance, identifier integrity, value-space compatibility, and evidence or study-design validity checks. BERDL's Delta-to-Iceberg migration means live discovery should prefer `catalog.namespace.table` addresses such as `kbase.ke_pangenome.genome`, fall back to underscore-form addresses only when necessary, and inspect live schemas rather than archived SQL. [^pitfalls] `data_lakehouse_ingest` is a governance-group name rather than a database prefix; confusing tenant and dataset names can cause access failures or wrong database paths. [^pitfalls]

The [nmdc_context_audit__REPORT](../summaries/nmdc_context_audit__REPORT.md) **supports** the provenance requirement: 20 NMDC-named entries resolve to 7 maintained resources across three tenants and six provenance classes, including genuine NMDC resources, NCBI and Pfam re-hosts, Arkin and NMDC-derived KBase products, and a NEON namesake collision. [^nmdc_context_audit] The `nmdc` tenant does not contain every NMDC-related resource. [^pitfalls] A resource name, tenant, shared column, or successful query is therefore only an entry point to validation.

The [webofmicrobes_explorer__REPORT](../summaries/webofmicrobes_explorer__REPORT.md) **supports** the same framework through a metabolite-to-fitness bridge across Web of Microbes (WoM), Fitness Browser, ModelSEED, GapMind, and pangenome resources. The 2018 WoM snapshot contains 37 organisms and 589 metabolites, but absent consumption data, ambiguous compound matching, and limited organism coverage constrain interpretation. [^webofmicrobes_explorer] Cross-collection reachability does not establish that a metabolite is consumed, that a compound identifier is unique, or that a metabolite-to-gene inference is biologically testable.

The [prophage_ecology__REPORT](../summaries/prophage_ecology__REPORT.md) **supports** extending validation from schema access to biological evidence through a join of eggNOG-annotated gene modules, environmental and phylogenetic metadata, TerL sequences, contig localization, and NMDC metagenomic samples. The analysis covered 27,702 bacterial species, 4,005,537 gene clusters, and 6,365 NMDC samples, but NMDC prophage burden was inferred indirectly from taxonomy and was not independently validated for prophage genes. [^prophage_ecology] A technically executable pangenome-to-NMDC bridge can therefore require qualified interpretation.

The [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md) **supports** extending validation to biological value space: Fitness Browser co-fitness, KBase pangenome presence/absence, phylogenetic distances, independent component analysis (ICA; a decomposition of multivariate covariance) modules, and SEED annotations were joined and tested. Pairwise co-fitness produced delta = +0.003 with Mann-Whitney p=1.66e-29, whereas coordinated ICA modules produced delta phi=+0.053. [^cofitness_coinheritance] The [ecotype_env_reanalysis__REPORT](../summaries/ecotype_env_reanalysis__REPORT.md) likewise integrated environment classifications, AlphaEarth embeddings, ANI distances, and gene-cluster memberships; environmental species did not have stronger partial correlations than human-associated species (U=1536, p=0.83). [^ecotype_env_reanalysis] A validated join can establish a defensible null result.

The [enigma_carbon_census_1__REPORT](../summaries/enigma_carbon_census_1__REPORT.md) **supports** this value-space criterion with a tiered compound-to-environment workflow: 83 compounds were structure-resolved, 54 linked to KEGG, 9 callable through ENIGMA-isolate predictions or measured fitness, and 74/83 (89%) remained organism-dark. [^enigma_carbon_census_1] The [euk_in_prok_correlates__REPORT](../summaries/euk_in_prok_correlates__REPORT.md) similarly linked 99%+ of classified runs and analyzed 2,759 workflow runs at run level, avoiding pseudo-replication from 1,067 pooled runs; environmental associations were largely study-confounded, while within-study vegetation and geography remained predictive. [^euk_in_prok_correlates]

The [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md) **refines** the framework by showing that tenant access is not organism-level coverage: ENIGMA CORAL contained 47 tables, 6,705 genomes, 15,015 genes, 4,346 field samples across 596 Oak Ridge locations, and 213,044 ASVs, but no *Desulfovibrio vulgaris* Hildenborough gene-level fitness data. Its single TnSeq library was FW300-N2E2 (*Pseudomonas*), while DubSeq covered *E. coli*, *P. putida*, and *B. thetaiotaomicron*. [^field_vs_lab_fitness]

The [fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md) **supports** organism-level four-resource validation: Web of Microbes exometabolomics, Fitness Browser gene fitness, BacDive utilization phenotypes, and GapMind predictions were joined for *Pseudomonas* FW300-N2E3. Of 21 testable metabolites, 17/21 (81%) were fully concordant, 4/21 (19%) partially concordant, none fully discordant, and mean concordance was 0.94; 37 metabolites (64%) were WoM-only. [^fw300_metabolic_consistency] The WoM exploration **refines** this bridge by identifying 19 WoM-produced metabolites for `pseudo3_N2E3` also present in Fitness Browser carbon- or nitrogen-source experiments: 5 were de novo products and 14 amplified metabolites. [^webofmicrobes_explorer] This is an actionable metabolite-to-gene path, but absent organism consumption actions prevent the stronger inference that production predicts utilization or gene essentiality. [^webofmicrobes_explorer]

The [genotype_to_phenotype_enigma__REPORT](../summaries/genotype_to_phenotype_enigma__REPORT.md) **refines** the framework by aligning growth curves, Genome Depot, RB-TnSeq (random barcode transposon sequencing), WoM, Carbon Source Phenotypes, pangenomes, and global 16S into 46,389 genome × condition pairs across 727 genomes and 363 conditions, including 4,293 shared [kegg](../entities/kegg.md) orthologs. Binary capability was predicted, but continuous kinetics were not under genus-blocked holdout. [^genotype_to_phenotype_enigma]

The [ibd_phage_targeting__REPORT](../summaries/ibd_phage_targeting__REPORT.md) **supports** value-space validation across 8,489 curatedMetagenomicData samples, HMP2 and FRANZOSA metabolomics, PhageFoundry susceptibility pairs, viromics, and 23 UC Davis patient profiles. Its dominant taxonomy–metabolite canonical correlation had r = 0.964, but clinical efficacy and treatment rules remained hypotheses requiring prospective validation. [^ibd_phage_targeting]

## Potential Connectivity, Documented Use, and Observability

Cross-tenant reuse is common but its measured extent is partly an observability problem: the atlas mined project README files, so mentions located only in research plans, notebook source, query histories, or other artifacts may have been missed. [^berdl_data_atlas] Consequently, reported tenant breadth and reuse are lower bounds, not complete measurements. The audit found that 51 of 66 BERIL projects, or 77%, spanned multiple tenants; KBase appeared in 53/66 (80%) and KEScience in 35/66 (53%). The KBase × KEScience bridge accounts for 36 projects, mostly pangenome-by-fitness joins through `genome_id` and `ncbi_taxon_id`. [^berdl_data_atlas] These are documented-use counts, not a census of all activity.

This observability limitation **refines** interpretation of the comparison between availability and use. ENIGMA contained 36% of BERDL tables but appeared in 6 projects, PhageFoundry contained 14% of tables but appeared in 5 projects, and PROTECT contained 4% but appeared in 2 projects. [^berdl_data_atlas] The ratios may reflect genuine differences in research use, incomplete documentation, or both; the audit does not distinguish those explanations. DOE-BER accounted for 63% of BERDL tables, so documentation gaps could alter conclusions about tenant centrality as well as bridge activity. [^berdl_data_atlas]

Five high-leverage bridges had zero realized use at audit time: UC1 between KEScience and refdata with 12 shared keys; UC2 between ENIGMA and PhageFoundry with 11; UC3 between KBase and refdata with 11; UC4 between NMDC and PROTECT with 10; and UC5 between NMDC and refdata with 9. [^berdl_data_atlas] They concern structural fitness signatures; subsurface prophages, metal resistance, and the Oak Ridge contamination gradient; GTDB–KBase species-pangenome disagreement; environmental distributions of clinically relevant pathogens and associated biogeochemistry; and ENVO ontology completeness in NMDC biosamples, respectively. [^berdl_data_atlas] “Zero realized use” means zero use found in audited documentation, not proof that no researcher used the bridge in unobserved notebooks, plans, or other materials. [^berdl_data_atlas] The atlas **refines** the apparent zero-use gap because UC1 was later sample-validated, whereas UC2–UC5 still require live execution. [^berdl_data_atlas]

The distinction is therefore among schema compatibility, documented project use, technically validated value-space overlap, and scientifically interpretable evidence. [^berdl_data_atlas] A bridge may be technically possible yet undocumented, documented yet unvalidated, or validated through an executed join. README mining provides a reproducible lower-bound inventory, but not a census of data reuse. [^berdl_data_atlas] Reliable reuse discovery **supports** [provenance-aware-resource-discovery](provenance-aware-resource-discovery.md) by requiring records of notebooks, research plans, executed queries, and other artifacts in addition to README descriptions; otherwise tenant-use rankings may be biased toward projects with more complete or standardized documentation. [^berdl_data_atlas]

The atlas **supports** [pangenome-integration](pangenome-integration.md): `kbase_ke_pangenome` contains 293,059 genomes, 27,690 GTDB species clades or pangenomes, and 132.5M gene clusters. [^berdl_data_atlas] Relevant tables are large—gene and gene-genecluster junction approximately 1B rows, `genome_ani` approximately 421M, eggNOG annotations approximately 93M, InterProScan domains approximately 833M, Bakta cross-references approximately 572M, and GapMind pathways approximately 305M—so Spark-native filtering and aggregation are required; a 1 GB driver cap makes large `.toPandas()` collections unsafe. [^pitfalls]

The WoM exploration **supports** the realized-bridge pattern while **refining** its expected scope. WoM has two direct Fitness Browser strain matches—*Pseudomonas* FW300-N2E3 and GW456-L13—and two same-strain or genus-level matches, including *E. coli* BW25113/Keio and *Synechococcus* PCC7002/SynE. [^webofmicrobes_explorer] For `pseudo3_N2E3`, 19 produced metabolites matched Fitness Browser carbon- or nitrogen-source experiments, including de novo lactate and valine production and amplified amino acids and nucleotides. [^webofmicrobes_explorer] The bridge is actionable for three organisms, but the *E. coli* WoM record contains only 12 observations focused on sulfur metabolism in ZMMG medium despite the richness of Keio data. [^webofmicrobes_explorer]

The [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md) **supports** a realized pathway across 9 organisms: 2,253,491 cofit pairs versus 22,534,910 prevalence-matched random pairs; 7/9 organisms had positive pairwise effects, but the across-organism Wilcoxon test was not significant (W=9, p=0.13). ICA modules had mean delta phi +0.053, with 21/195 significant at q<0.05; accessory modules had mean delta phi +0.108 versus +0.059 for core modules, with p=0.051. [^cofitness_coinheritance]

The ENIGMA census produced 569 isolate-utilizer rows across 8 compounds, placing 494 records representing 359 strains on GTDB taxonomy: 64 high-certainty, 387 medium-certainty Tier-2, and 43 medium-certainty Tier-3. [^enigma_carbon_census_1] Its atlas detected 83/86 genera in 1,719 NMDC metagenomes and used 3,825 taxonomy-bearing NMDC metagenomes plus 302 Planet Microbe runs, but measured occurrence rather than catabolic activity. [^enigma_carbon_census_1]

The eukaryotic-contamination project **supports** controlled NMDC results-to-metadata joins: native results keyed by `data_object_id` or `workflow_run_id` were connected through biosample/workflow and study tables, and approximately 29M-row Kraken2 results were aggregated to one row per workflow run. [^euk_in_prok_correlates] Classifier and metabolomics file IDs (`nmdc:dobj-11-*` and `nmdc:dobj-12-*`) require a `sample_id` bridge through `omics_files_table`, which has 385,562 rows; wide `taxonomy_features` and zero-coded `abiotic_features` require reshaping and zero-to-NaN conversion. [^pitfalls]

The [prophage_ecology__REPORT](../summaries/prophage_ecology__REPORT.md) **supports** this integration pattern while **refining** its evidential requirements. Across 1,773 species, PERMANOVA (permutational multivariate analysis of variance) on Bray-Curtis module composition found significant genome-size, environment, and family-phylogeny effects (each p=0.01), with F=212.99, 30.04, and 6.17 respectively; genome size correlated with cluster count at rho=0.717. Environment remained significant within every genome-size quartile (all p < 6.5e-78), and AlphaEarth niche breadth correlated with module count after genome-size control (rho=0.468, p=8.41e-110). [^prophage_ecology] However, only 28% of genomes had AlphaEarth embeddings, and environmental categories plus the indirect NMDC taxonomy bridge limit causal interpretation. [^prophage_ecology]

The same study found 57 significant module–abiotic correlations in 6,365 NMDC samples at FDR (false discovery rate) < 0.05: packaging–pH rho=0.519, all-modules–pH rho=0.474, all-modules–temperature rho=0.399, all-modules–depth rho=0.361, and all-modules–total-nitrogen rho=0.333. [^prophage_ecology] Concordance between pangenome enrichment and NMDC correlations was strongest for head morphogenesis, tail, and anti-defense, providing independent module-level value-space support but not direct prophage detection or causal validation. [^prophage_ecology]

The field-versus-lab study found 2,725 genes with pangenome and fitness links; 76.3% of non-essential genes with fitness were core, while 678 essential genes were 80.1% core but lacked transposon data. Field-stress-important genes were 83.6% core, field-core-important 82.4%, heavy-metal-important 71.2%, and lab-antibiotic-important 73.4%. [^field_vs_lab_fitness] Field-plus-lab prediction had AUC 0.548 versus 0.645 with gene length, supporting [condition-specific-fitness](condition-specific-fitness.md) and [pangenome-integration](pangenome-integration.md) while limiting ecological inference. [^field_vs_lab_fitness]

The FW300 bridge found 601 unique genes and 4,764 total significant gene-condition hits using |fit| > 1 and |t| > 4; comparisons were concordant for 21/21 matched metabolites with Fitness Browser and 13/13 with GapMind, but only 3/7 with BacDive. [^fw300_metabolic_consistency] Malate was utilized by 49/49 BacDive strains, arginine by 40/48, and valine by 1/1, illustrating why strain counts must be retained. [^fw300_metabolic_consistency]

The ENIGMA LightGBM model achieved binary-growth AUC 0.620 under genus-blocked holdouts; KO × condition interactions raised mean AUC to 0.653 in 80 of 106 held-out genera, while continuous µmax, lag, and max_A had negative R². [^genotype_to_phenotype_enigma] The IBD bridge likewise requires scope controls: PhageFoundry contained 96 phages, 188 *E. coli* strains, and 17,672 susceptibility pairs; 3,929 were susceptible and a five-phage cocktail covered 94.7% of tested strains, not UC Davis isolates or in-vivo efficacy. [^ibd_phage_targeting]

## Identifier, Provenance, and Semantic Validation

The atlas **refines** bridge counts because `genome_id` can encode different identifiers in KBase, NCBI, and MAG pipelines. [^berdl_data_atlas] The [pitfalls](../summaries/pitfalls.md) **supports** this warning with concrete failures: ENIGMA MT20 was *Rhodanobacter glycinis*, whereas GTDB MT20 was *Streptococcus pneumoniae*; the erroneous match involved 8,434 genomes, including 1,751 clinical genomes, and 12 of 32 pangenome linkages through `ncbi_strain_identifiers` were incorrect genus matches. Genus checks and `GCF_*` assembly accessions are required. [^pitfalls]

Pangenome taxonomy must use `genome_id`, not `gtdb_taxonomy_id`; GapMind `clade_name` uses the full `gtdb_species_clade_id`; species-specific gene-cluster IDs require COG, KEGG ortholog, or Pfam representations; `eggnog_mapper_annotations.query_name` joins to `gene_cluster.gene_cluster_id`; and `ncbi_env` requires entity-attribute-value extraction and pivoting. [^pitfalls]

The NMDC audit **supports** the same warning: `nmdc.ncbi_biosamples` contains 51,711,888 biosamples and 756,112,544 attribute rows, versus 16,640 samples in genuine `nmdc.metadata.biosample_set`; `kbase.nmdc_mags` contains 62,346 MAGs. [^nmdc_context_audit] This is a ~3,000× scale trap. [^nmdc_context_audit] MetaPhlAn3 synonymy also requires taxid-backed, GTDB-version-aware reconciliation: failures involving *Bacteroides vulgatus*/*Phocaeicola vulgatus*, *Eubacterium rectale*/*Agathobacter rectalis*, and *Ruminococcus gnavus*/*Mediterraneibacter gnavus* produced log₂FC approximately 28, equivalent to approximately 2.68 × 10⁸ fold. [^pitfalls]

WoM evidence **supports** compound-level identifier validation. Of 257 identified, non-unknown compounds, 69 (26.8%) had definitive ModelSEED links through exact name matching; 107 (41.6%) had formula-only matches, yielding 176 compounds with any link (68.5%) and leaving 81 unmatched (31.5%). Formula-only matching expanded those 107 compounds to 900 ModelSEED molecules, an average of 8.4 candidates per WoM compound; these are candidate sets for manual curation, not definitive identifications. [^webofmicrobes_explorer]

The PaperBLAST analysis **supports** evidence-provenance validation: its 12.4 million rows span 14 tables; *Homo sapiens* accounts for 46.7% of gene-paper records, the top five organisms 72.8%, and 65.6% of 841K genes with text-mined links have exactly one paper. [^paperblast_explorer] At 50% sequence identity, 31,653 protein families had zero papers and 159,046 exactly one; 5,218 multi-member families had no literature. [^paperblast_explorer] PaperBLAST covers 1951–2026, with 845K genes linked to 1.1M papers through 3.2M associations, but 25.6% of genes have no text-mined link. [^paperblast_explorer]

The ENIGMA census **supports** validating biological direction as well as identifiers: it linked PubChem, KEGG, ModelSEED, Fitness Browser, Genome Depot, GTDB, SSO, NMDC, and Planet Microbe, but 74 compounds were not linkable to organismal utilization determinants. Xanthine's reaction R02107 represented purine nitrogen acquisition rather than carbon catabolism, reducing the effective carbon-callable set from 9 to 8. [^enigma_carbon_census_1]

The [caulobacter_fur_lipida_loss__REPORT](../summaries/caulobacter_fur_lipida_loss__REPORT.md) **supports** this distinction: it bridged Fitness Browser, PaperBLAST, published datasets, transcript measurements, and proteomics, but PaperBLAST returned false negatives for known Caulobacter lipid A genes while NCBI supported absence claims. [^caulobacter_fur_lipida_loss] GOTTCHA2, unlike Kraken2 and Centrifuge, was usable for eukaryotic-fraction estimation because the latter reference databases were prokaryote-restricted. [^euk_in_prok_correlates]

Database semantics also require validation. WoM uses `I` for increased, `E` for emerged, `N` for no change, and sometimes `D` for decreased; “produced” means `action IN ('I','E')`, except that for “The Environment” `D` means detected. [^pitfalls] In the 2018 export, `D` occurred only for the control, with 742 detected and 1,023 not-detected control observations; organism actions included 1,338 increased, 1,155 emerged, and 7,509 with no significant change across 10,744 observations, with no organism consumption or decreased action recorded. [^webofmicrobes_explorer] The discrepancy with the valid “decrease” action described by Kosina et al. (2018) indicates that the archived export may be incomplete or older than a GNPS2 version, rather than proving that consumption is absent from WoM generally. [^webofmicrobes_explorer]

BacDive utilization is four-valued; for *Pseudomonas fluorescens*, indole had 60 “produced” entries but 1 actual utilization test, so only explicit `+` and `-` observations belong in utilization percentages. [^pitfalls] Fitness Browser, GapMind, and Carbon Source Phenotypes are also non-equivalent observables: matched-condition AUCs were 0.800 and 0.646, with approximately 76% of ENIGMA conditions lacking either GapMind coverage or training data. [^genotype_to_phenotype_enigma]

Cross-tenant deduplication is another interpretive constraint: the atlas did not perform it, and notes that Refdata and KBase may contain the same UniProt entries through different cluster indices, while ENIGMA and genome-depot tables share genome records with the ENIGMA SDT layer. [^berdl_data_atlas] Joined counts must therefore distinguish matched records, distinct biological entities, and duplicated representations.

## Validated UC1 Integration

UC1 links FitnessBrowser measurements to AlphaFold models through SwissProt best hits. The validated path uses composite `orgId`, `locusId` between `genefitness` and `besthitswissprot`, then `sprotAccession` to `uniprot_accession` in `alphafold_entries`; FitnessBrowser does not expose `protein_id`. [^berdl_data_atlas] SQL probing corrected the proposed join by identifying this composite route. [^berdl_data_atlas]

Live validation found 27,410,721 measurements, 79,180 genes with SwissProt hits, 241,070,489 AlphaFold entries, and 78,753/79,180 hits represented in AlphaFold. The cohort contains 55,454 genes across 48 organisms and 22,303 models, including 6,635 essential genes (`min_fit ≤ −4`), 8,271 strong-defect, 10,950 moderate-defect, 29,467 mild-defect, and 131 no-defect genes, tested under an average of 121–187 conditions. [^berdl_data_atlas]

UC1 **supports** [condition-specific-fitness](condition-specific-fitness.md) and [gene-essentiality](gene-essentiality.md) as a sample-validated route from condition-specific fitness to structure, but not residue-level structure-function analysis because per-residue pLDDT and structural features are absent. [^berdl_data_atlas] Fitness fields may be strings and require casting; `orgId` is case-sensitive; KO mapping is a two-hop `besthitkegg`–`keggmember` join; essential genes are absent from transposon records, so genefitness-only analyses miss approximately 14.3% of protein-coding genes. [^pitfalls]

## Tensions

The atlas exposes a tension between 536 schema-level bridges and evidential validation: the original audit recorded five high-leverage bridges with zero realized use, but UC1 was subsequently sample-executed and UC2–UC5 remained untested. [^berdl_data_atlas] The realized-use count is also a lower bound because README mining may miss plans and notebooks. [^berdl_data_atlas] Thus “zero documented use” and “zero use” are not equivalent claims.

The NMDC audit **contradicts** any assumption that a catalog prefix, tenant, or name proves common authority: 20 entries resolve to 7 resources, with `kbase.nmdc_neon` a NEON namesake collision. [^nmdc_context_audit]

The WoM snapshot introduces a related tension with broad cross-collection integration claims: the 19-metabolite Fitness Browser bridge is directly actionable, but missing consumption actions mean production cannot be treated as utilization, and 107 formula-only ModelSEED matches expand to 900 candidate molecules. [^webofmicrobes_explorer] This **refines** rather than overturns the framework: a join may be technically valid while its biological direction and chemical identity remain uncertain.

The prophage study **refines** this tension: module-level pangenome and NMDC associations were concordant, but prophage annotations came from eggNOG rather than geNomad or VIBRANT, so near-universal prevalence may include domesticated remnants, bacterial homologs, and integrases; the false-positive rate is uncharacterized. [^prophage_ecology] Its environmental effect exceeded family-level phylogeny in the reported PERMANOVA, but genome size was dominant (rho=0.717), only 28% of genomes had embeddings, and genus-level NMDC inference assumed conserved prophage content. [^prophage_ecology]

The study also **supports** [phage-defense-syndromes-and-arms-race](phage-defense-syndromes-and-arms-race.md) while limiting mechanism: human-associated environments enriched tail (log2(OR)=2.21), head morphogenesis (1.98), and anti-defense (1.70), whereas anti-defense was depleted in freshwater (-0.74) and animal-associated environments (-0.24); these are consistent with arms-race theory but do not demonstrate coevolution. [^prophage_ecology] TerL lineages did not show independent enrichment in 0/500 FDR-corrected tests; among 824 lineages with at least 5 species, 325 were specialists and 499 generalists. [^prophage_ecology]

Other tensions remain. PaperBLAST's organism-level Gini coefficient is 0.967 and gene-level Gini 0.669; 9.2% of 50%-identity families have zero papers, 46.1% exactly one, and 4.3% at least 20, contradicting paper count as a uniform evidence proxy. [^paperblast_explorer] The ecotype analysis found p=0.83 and rho=-0.085, p=0.25, while its median partial correlation was 0.081 across 183 species versus 0.003 originally, a reported 27x difference caused by different sampling. [^ecotype_env_reanalysis]

The co-fitness bridge had weak pairwise but stronger module-level effects; co-fitness strength was anti-correlated with co-occurrence (rho=-0.109, p<1e-300 across 1.04M pairs), requiring auxiliary-only comparisons below 95% prevalence. [^cofitness_coinheritance] The field-versus-lab study likewise found weak condition-only prediction (AUC 0.548; field-only 0.517; lab-only 0.531) and no significant module-conservation correlation with field activity (rho=0.071, p=0.62). [^field_vs_lab_fitness]

Semantic tensions persist: tryptophan increased in WoM and had 231 significant Fitness Browser genes and a complete GapMind pathway, yet 0/50 *P. fluorescens* strains used it as carbon; production therefore does not imply utilization. [^fw300_metabolic_consistency] Binary growth could be predicted for tryptophan (AUC 0.933), phenylalanine (0.932), and valine (0.927), while continuous phenotypes had negative R². [^genotype_to_phenotype_enigma]

The IBD CCA result (r=0.964) and PhageFoundry coverage are hypothesis-generating rather than clinical validation; HMP2/FRANZOSA clustering had cross-cohort LOSO ARI=0.000, and the cocktail covered only tested strains. [^ibd_phage_targeting] In ecotype analyses, pooled diagnosis was structurally unidentifiable because 45 sub-studies had at least 10 HC samples, 5 had at least 10 CD, and 0 had at least 10 of both; selection-on-outcome leakage reduced independent Tier-A candidates from 33 to 3. [^pitfalls]

## Open Directions

- Combine README files, research plans, notebook source, and query logs, then ask how many additional project–tenant and project–bridge uses are recovered beyond the documented baseline of 51 of 66 multi-tenant projects; preserve the original README-derived counts and deduplicate evidence at project–tenant–dataset and project–bridge levels. [^berdl_data_atlas]
- Build a provenance-aware project–dataset graph and audit notebook and query artifacts for the 36 documented kbase × kescience projects, asking whether their pangenome-by-fitness joins are reproducible and whether additional join keys beyond `genome_id` and `ncbi_taxon_id` were used. [^berdl_data_atlas]
- Execute UC2–UC5 on the live cluster with provenance, authority, currency, identifier, overlap, representative-record, duplicate, and evidence checks; compare validated value-space overlap with the README-derived finding of zero realized use, asking whether the bridges are unused, undocumented, or merely unvalidated. Use UC2's 11, UC3's 11, UC4's 10, and UC5's 9 candidate keys to test their proposed prophage, fitness, pathogen, biogeochemical, species-pangenome, and ENVO analyses. [^berdl_data_atlas]
- Add authority, tenant, scale, provenance, and `max(committed_at)` to inventory; compare `nmdc.metadata` and `nmdc.ncbi_biosamples` with upstream counts and repair NMDC schema, skill, documentation, aliases, and user copies. [^nmdc_context_audit]
- Build a live-catalog harness for dotted/underscore namespaces, canonical identifiers, data types, plausible row counts, join overlap, provenance, and biological representative records; use Spark-native workflows, parquet checkpoints, explicit casts, and finalization logs. [^pitfalls]
- For prophage ecology, validate eggNOG calls with geNomad or VIBRANT, quantify false positives and domesticated remnants, repeat NMDC burden inference against directly detected prophages, and test whether pH and other abiotic correlations persist within study and genus. [^prophage_ecology]
- Test whether human-associated tail, head, and anti-defense enrichment reflects phage exposure or counter-defense by integrating direct phage detection, host range, and matched environmental metadata; characterize whether TerL specialists persist after finer taxonomy and sampling controls. [^prophage_ecology]
- Combine NMDC metabolomics, proteomics, and lipidomics with UC4/UC5 and prophage-module bridges, preserving the distinction between occurrence, activity, and mechanism. [^berdl_data_atlas][^prophage_ecology]
- Ingest UC1 residue-level pLDDT and structural features and test them across the 55,454-gene cohort; restrict fitness-to-pangenome analyses to auxiliary-only pairs below 95% prevalence. [^berdl_data_atlas][^cofitness_coinheritance]
- Link the 129,823 PaperBLAST VIMSS cross-references to Fitness Browser values, stratify by organism and family literature coverage, and distinguish missing PMC coverage from missing biology. [^paperblast_explorer]
- Reproduce ecotype analyses with downsampled and full-genome extraction, genome-count covariates, structured ENVO terms, study-aware validation, and within-substudy contrasts. [^ecotype_env_reanalysis][^pitfalls]
- Apply GTDB-Tk-verified identifiers, quantify the 12 collision-derived mismatches, and retest environmental profiles; compare GTDB and KBase assignments through `genome_id` and `ncbi_taxon_id`. [^genotype_to_phenotype_enigma][^berdl_data_atlas]
- Pair environmental occurrence with compound-specific enrichment and measured fitness; expand WoM–BacDive matching with InChIKey or CHEBI identifiers and test tryptophan cross-feeding. [^enigma_carbon_census_1][^fw300_metabolic_consistency]
- Use exact-name ModelSEED links separately from formula-only candidate sets, manually curate the 900 formula-expanded molecules, and quantify how compound ambiguity changes pathway and fitness conclusions. [^webofmicrobes_explorer]
- Obtain the current GNPS2 or Northen laboratory WoM dataset, determine whether consumption actions are available, and repeat the production–utilization–fitness analysis with versioned provenance. [^webofmicrobes_explorer]
- Test whether `E/(E+I)` metabolic novelty associates with pangenome openness or accessory gene content, using strain-to-genome mappings and species-level rather than genus-only joins. [^webofmicrobes_explorer]
- Apply GroupKFold by study and within-study contrasts to NMDC eukaryotic-fraction models, harmonize classifier databases, and test replication outside NEON soil. [^euk_in_prok_correlates]
- Extend field-versus-lab analyses to organisms with both environmental and gene-level fitness data; quantify gene-cluster prevalence and acquisition history for metal and antibiotic resistance. [^field_vs_lab_fitness]
- Query INPHARED and IMG/VR for phages targeting *H. hathewayi*, *F. plautii*, and *M. gnavus*, validating host range against patient isolates. [^ibd_phage_targeting]
- Reproduce the reduced IBD Tier-A list with held-out-feature clustering, leave-one-species-out refitting, study-aware validation, and within-substudy contrasts. [^pitfalls]
- Extend the validated UC1 cohort with per-residue pLDDT and structural-feature data from PDB files, because `kescience_alphafold.alphafold_entries` lacks those fields, then test whether structure-derived variables explain condition-specific fitness patterns beyond the existing gene-level join. [^berdl_data_atlas]

[^berdl_data_atlas]: [berdl data atlas](../summaries/berdl_data_atlas__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
[^nmdc_context_audit]: [nmdc context audit](../summaries/nmdc_context_audit__REPORT.md)
[^webofmicrobes_explorer]: [webofmicrobes explorer](../summaries/webofmicrobes_explorer__REPORT.md)
[^prophage_ecology]: [prophage ecology](../summaries/prophage_ecology__REPORT.md)
[^cofitness_coinheritance]: [cofitness coinheritance](../summaries/cofitness_coinheritance__REPORT.md)
[^ecotype_env_reanalysis]: [ecotype env reanalysis](../summaries/ecotype_env_reanalysis__REPORT.md)
[^enigma_carbon_census_1]: [enigma carbon census 1](../summaries/enigma_carbon_census_1__REPORT.md)
[^euk_in_prok_correlates]: [euk in prok correlates](../summaries/euk_in_prok_correlates__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../summaries/field_vs_lab_fitness__REPORT.md)
[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
[^genotype_to_phenotype_enigma]: [genotype to phenotype enigma](../summaries/genotype_to_phenotype_enigma__REPORT.md)
[^ibd_phage_targeting]: [ibd phage targeting](../summaries/ibd_phage_targeting__REPORT.md)
[^paperblast_explorer]: [paperblast explorer](../summaries/paperblast_explorer__REPORT.md)
[^caulobacter_fur_lipida_loss]: [caulobacter fur lipida loss](../summaries/caulobacter_fur_lipida_loss__REPORT.md)
