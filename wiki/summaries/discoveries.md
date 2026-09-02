---
type: "Summary"
description: "Cross-project discoveries on microbial fitness, ecology, pangenomes, and analytical rigor"
doc_type: "short"
full_text: "sources/discoveries.md"
---
# Discoveries Log

## Overview

This log consolidates cross-project findings from 2026 spanning microbial fitness, pangenome evolution, ecological specialization, metabolic modeling, antimicrobial resistance, subsurface microbiology, microbiome analysis, and research-quality practice. It includes direct measurements, methodological corrections, validation results, contradictions, and reusable analytical rules. [src: discoveries]

## Key Findings

### Evolution, gene function, and pangenomes

M22 Sankoff parsimony attribution of 17M gain events on the GTDB-r214 species tree produced function-class acquisition-depth signatures: CRISPR-Cas had a 24.5× recent/ancient ratio, strict housekeeping genes were approximately 1×, and mixed regulatory-plus-metabolic KOs had 2× the Innovator-Exchange rate of pure regulatory or pure metabolic KOs. Leaf consistency independently validated the depth trend, with species-with-KO fractions declining from 0.34 for recent gains to 0.20 for ancient gains. [src: discoveries]

Within-clade heterogeneity can be hidden by family-level aggregation. For Mycobacteriaceae mycolic-acid KOs, family-rank producer-side Cohen's d was 0.31, while median leaf consistency was 0.15; restricting analysis to the mycolic-positive sub-clade increased producer d to +0.394 versus +0.309 at family rank, with 10 of 13 genera having mean leaf consistency ≥ 0.5. [src: discoveries]

A robust clade-level innovation claim should converge across three independent substrates: atlas Cohen's d, ecology-based clade-by-biome Fisher enrichment, and curated phenotype or model-organism evidence. The referenced workflow used p<10⁻¹¹ for an ecology enrichment and relied on BERDL coverage of 88.8% for `kbase_ke_pangenome.ncbi_env`, 28.4% for `kescience_mgnify`, 32% for BacDive through GCF→GCA fallback, and approximately 30 organisms for the Fitness Browser. [src: discoveries]

Across 32 species and 9 phyla, novel or singleton genes were enriched in COG L mobile elements by +10.88%, COG V defense mechanisms by +2.83%, and COG S unknown function by +1.64%; core genes were depleted in J translation by -4.65%, F nucleotide metabolism by -2.09%, H coenzyme metabolism by -2.06%, E amino acid metabolism by -1.81%, and C energy production by -1.75%. Composite assignments such as LV showed +0.34% enrichment and 76% consistency, indicating that multi-function assignments can represent real mobile-defense modules rather than annotation noise. [src: discoveries]

Across 27,690 species, 55.9% of dark-gene ortholog groups were kingdom-level, with species counts ranging from 1 to 27,482 and median 135. In a 57,011-gene darkness spectrum, only 4,273 genes (7.5%) were T1 Void, whereas 22,500 (39.5%) were T4 Penumbra with 3–4 converging evidence lines. Across 47 testable dark-gene clusters, 29 (61.7%) showed directional concordance between laboratory fitness conditions and carrier-genome environments, with Fisher's combined p=0.031; NMDC validation confirmed all 4 pre-registered abiotic predictions and all 7 pre-registered trait predictions. [src: discoveries]

Fitness Browser dark genes were substantially reclassified by Bakta v1.12.0: of 39,532 dark genes with pangenome links, 33,105 (83.7%) were reclassified and 6,427 remained truly dark. Truly dark genes were shorter (121 versus 194 aa), less conserved (43% versus 73% core), had fewer orthologs (29% versus 64%), and had higher GC deviation (d=0.247); 41% of their neighbors were also hypothetical and 12% were within 2 genes of mobile elements. Only 246/6,427 (3.8%) had zero annotation clues. [src: discoveries]

Bakta and eggNOG are complementary across 132.5M gene clusters: eggNOG had higher COG coverage (51% versus 8.2%), KEGG coverage (38.5% versus 17.3%), and Pfam coverage (63% versus 7.7%), while Bakta had higher GO coverage (15% versus 7.4%), product descriptions (71.2% versus 70.4%), and unique UniRef50 links covering 79.2%. Their union increased any-functional-annotation coverage to 77.3%, and Bakta rescued 11.2M clusters among 39.2M missed by eggNOG. Only 33.3% of Bakta's 17.6M distinct UniRef50 IDs existed in the BERDL UniProt identifier table. [src: discoveries]

Pangenome openness had no significant relationship with environment or phylogenetic effects in one analysis (rho=-0.05, p=0.54 and rho=0.03, p=0.73), but variable metabolic pathways strongly predicted openness in another: rho=0.327, p=7.2e-71, and partial rho=0.530, p=2.83e-203 after controlling for genome count. Across 1,872 species with sufficient AlphaEarth coverage, niche breadth predicted pathway completeness at r=0.392, p=7.1e-70, embedding variance at r=0.412, p=1.8e-77, and geographic range at r=0.360, p=1.8e-58; only 6.8% of species (1,872/27,690) had sufficient coverage. [src: discoveries]

### Essentiality, fitness, and cofitness

Across 48 bacteria, 15 gene families were essential in every organism, including ribosomal proteins, groEL, pyrG, fusA, valS, and SelGGPS. Of 17,222 ortholog families, 859 (5.0%) were universally essential, 4,799 (27.9%) variably essential, and 11,564 (67.1%) never essential. Orphan essential genes numbered 7,084 and were 58.7% hypothetical, while universally essential genes were 8.2% hypothetical. [src: discoveries]

Universally essential genes were 91.7% core versus 80.7% for non-essential genes, and 71% of universally essential families were 100% core within species; orphan essentials were only 49.5% core. Module transfer from non-essential orthologs generated 1,382 function predictions for hypothetical essential genes across 48 organisms. [src: discoveries]

Across 33 bacteria, putative essential genes were 86.1% core versus 81.2% for non-essential genes, with median OR=1.56 and 18/33 organisms significant after BH-FDR. Across 194,216 genes in 43 bacteria, core fractions formed a continuous gradient from 82% for essential genes to 66% for always-neutral genes. [src: discoveries]

Fitness modules derived by robust ICA and DBSCAN were stable at 17–52 modules per organism across 32 bacteria; 94.2% had significantly elevated within-module cofitness, with mean |r|=0.34 versus background 0.12 and mean genomic-adjacency enrichment of 22.7×. Absolute module-membership thresholding improved cofitness enrichment from 59% to 94.2% and within-module |r| from 0.047 to 0.34. Cross-organism alignment found 156 module families spanning at least 2 organisms, including 28 spanning 5+ organisms and one spanning 21 of 32 organisms. [src: discoveries]

Ortholog scope changed cross-organism results from 27 to 156 module families, from 0 to 28 families spanning 5+ organisms, and from 31 to 493 family-backed predictions. Pfam domains increased module annotation from 92/1,116 (8.2%) to 890/1,116 (79.7%), increased predictions from 878 to 6,691, and raised annotated families from 32 to 145 of 156. Ortholog transfer achieved 95.8% precision and 91.2% coverage for gene-level KO prediction, whereas Module-ICA had <1% KO-level precision but captured process-level co-regulation. [src: discoveries]

Across 25,271 true trade-off genes, 17.8% of genes were important in some conditions and burdensome in others; trade-offs were 1.29× more likely to be core (OR=1.29, p=1.2e-44). Core genes were ever beneficial after deletion in 24.4% of cases versus 19.9% for auxiliary genes (OR=0.77, p=5.5e-48), and condition-specific genes were 77.3% core versus 70.3% without specific phenotypes (OR=1.78, p=1.8e-97). There were 28,017 costly-plus-conserved genes, 5,526 costly-plus-dispensable genes, and 21,886 neutral-plus-dispensable genes. [src: discoveries]

### Condition-specific metabolism and model limitations

In ADP1, each of 8 carbon sources required a distinct respiratory configuration. Quinate required only Complex I, acetate required Complex I plus cytochrome bo3 and ACIAD3522 among other components, and glucose had no specifically required component. Quinate produced 0.57 NADH per carbon versus 1.50 for glucose, yet Complex I was more essential because simultaneous β-ketoadipate products created a concentrated NADH burst. [src: discoveries]

ADP1 expressed its three NADH dehydrogenases at similar levels under standard conditions: Complex I mean 27.6, NDH-2 mean 27.0, and ACIAD3522 mean 26.2, around a genome median of 26.4. ACIAD3522 had a growth ratio of 0.013 on acetate and 1.39 on both quinate and glucose, making it the most condition-specific gene in the 2,034-gene matrix. The cross-species NDH-2 compensation hypothesis was not supported after annotation correction: Complex I aromatic deficits were -0.297 with validated NDH-2 versus -0.156 without, p=0.52. [src: discoveries]

The ADP1 aromatic-catabolism support network contained 8 pathway genes but 51 quinate-specific genes: 21 Complex I genes, 7 iron-acquisition genes, and 2 PQQ-biosynthesis genes. FBA lacked reaction mappings for 30/51 genes (59%) and predicted 0% Complex I essentiality despite predicting 1.76× higher aromatic flux. Cross-species data showed larger Complex I defects on acetate (-1.55) and succinate (-1.39) than on aromatics, supporting a high-NADH-flux bottleneck interpretation. ACIAD3137 and ACIAD2176 correlated with Complex I genes at r > 0.98 across 8 conditions. [src: discoveries]

Across 7 Fitness Browser organisms and 23 GapMind pathways, 35.4% of pathway-organism pairs were Active Dependencies, 41.0% Latent Capabilities, 14.9% Incomplete but Important, and 8.7% Missing. All Latent Capabilities became fitness-important under condition-specific analyses. In FW300-N2E3, all 13 Web of Microbes metabolites that could be mapped to GapMind had complete pathways and all 13 showed growth in Fitness Browser experiments, but the overall 94% four-database concordance was structurally driven: Fitness Browser was 21/21, GapMind 13/13, and BacDive only 3/7. [src: discoveries]

Community-scale NMDC metabolomics supported the Black Queen Hypothesis: 11/13 amino-acid pathways trended in the predicted direction, with a binomial sign-test p=0.011; leucine had r=-0.390, q=0.022, n=62, and arginine had r=-0.297, q=0.049, n=80. Methionine had r=-0.496 but q=0.117 with n=18, while tyrosine was an anti-BQH outlier at r=+0.42. Carbon utilization, rather than amino-acid biosynthesis, dominated metabolic differentiation: PC1 explained 49.4% of variance and separated Soil from Freshwater at p<0.0001, while amino-acid pathways loaded more strongly on PC2, which explained 16.6%. [src: discoveries]

### Antimicrobial resistance and defense

Across 14,723 species, efflux pumps constituted 21% of AMR in human-gut species but 1% in aquatic species (η²=0.127), while metal resistance constituted 45% in soil/aquatic species but 6% in human-gut species (η²=0.107). Clinical species had 68% accessory AMR versus 43% in soil. Within 823 multi-environment species, clinical strain fraction predicted total AMR at rho=0.465, p=2.2e-45. *Klebsiella pneumoniae* had 1,115 AMR clusters, only 7 of them core, across 13,637 genomes. [src: discoveries]

Across 801 AMR genes in 28 organisms, cofitness neighborhoods were enriched for flagellar motility in 5 organisms, flagellum assembly in 5, histidine biosynthesis in 3, and tryptophan biosynthesis in 3 at FDR<0.05. InterProScan GO annotations detected these signals whereas legacy Fitness Browser SEED annotations detected 0/280 significant enrichments. AMR genes occurred in larger ICA modules than background genes, with median 46 versus 27 (p=1.7e-8). [src: discoveries]

Random-effects meta-analysis of 801 AMR genes across 25 organisms found a pooled knockout fitness shift of +0.086 [+0.074, +0.098], with all 25/25 organisms positive. The cost was mechanism-independent (KW p=0.89), conservation-independent (p=0.33), and tier-independent (p=0.26). Efflux genes showed a stronger antibiotic-dependent fitness flip than enzymatic inactivation genes, +0.094 versus -0.001, MWU p=0.007. [src: discoveries]

Acquired AMR genes had stronger phylogenetic signal than core AMR genes across 1,261 species: median Mantel r=0.222 versus 0.117, paired t-test p=7.0e-16. Across 180,025 genomes and 1,305 species, 51.3% of within-species AMR occurrences were rare (≤5% prevalence), 41.3% variable, and 7.5% fixed; median strain pairwise Jaccard distance was 0.435. Resistance islands occurred in 705/1,305 species (54%), with 1,517 islands, mean phi=0.827, 88% containing multiple resistance mechanisms, and a maximum of 43 genes. [src: discoveries]

The SNIPE defense system occurred in 4,572 gene clusters across 1,696 species and 33 phyla, with 86.7% accessory or singleton. Its nuclease domain is PF13455 (Mug113), not PF01541, although both belong to the GIY-YIG clan. The PhageFoundry strain-modelling database contained 17,672 binary infection outcomes from 188 *E. coli* strains and 96 phages, with an ML model AUC=0.883; lambda infected 1/188 strains (0.5%) versus 43.4% for Myoviridae. [src: discoveries]

Fitness Browser evidence showed that ManXYZ is a mannose/glucosamine transporter rather than a fructose transporter: *E. coli* K-12 ManXYZ knockouts had fitness -3.93 on D-mannose and -2.75 on D-glucosamine, but +0.18 to +0.66 on D-fructose. A full two-domain SNIPE protein with 129 experiments was found in *Methanococcus maripaludis* JJ, and Klebsiella had 1 DUF4041 annotation across 3 proteins plus 4,619 PTS_EIIC annotations, making it the only PhageFoundry species with both SNIPE and the ManX-family PTS domain. [src: discoveries]

### Microbiome and multi-cohort analysis

Pooling HMP2 and Franzosa metabolomics on 122 m/z-bridge metabolites caused PCA plus K-means K=4 clusters to separate completely by cohort rather than diagnosis; PC1 explained 79% of variance and cross-cohort LOSO ARI was 0.000 versus 0.113 for taxonomic ecotypes. Relative-abundance spaces were cross-cohort-portable because they are unitless and compositional, whereas absolute-intensity metabolomics requires explicit batch correction such as ComBat, SVA, RUV, or quantile normalization. [src: discoveries]

A K=4 LDA-GMM consensus on 8,489 curatedMetagenomicData samples produced E0 diverse commensal (n=3,604), E1 Bacteroides2 transitional (n=2,601), E2 Prevotella copri enterotype (n=920), and E3 severe Bacteroides-expanded (n=1,364). Healthy samples concentrated in E0 plus E2 at 84% combined, whereas CD and UC distributed across E1 and E3. Cross-method ARI selected K=4 because ARI was 0.131, within 0.02 of the peak at K=7 with ARI=0.140. [src: discoveries]

Classifier and projection validation exposed several portability failures. A pooled classifier achieved macro OvR AUC=0.80 but only 41% agreement on UC Davis patients, where `is_ibd=1` was constant and 19/22 patients were predicted E1. LDA projection across MetaPhlAn3 and Kaiju namespaces produced plausible Kuehl proportions of 27/42/31% across ecotypes, whereas CLR-plus-PCA GMM projected all 26 Kuehl samples to E3 at confidence >0.97 because Kuehl detected only 54% of training species. [src: discoveries]

A preliminary pooled analysis called *C. scindens* CD-enriched at log₂FC=+2.67, but independent evidence showed this was a compositional and stratification artifact. After leakage repair, *C. scindens* was genuinely CD-increased under within-substudy analysis, with pooled CLR-Δ +1.18, FDR=1e-8, and 4/4 sign concordance. The original 33 within-ecotype Tier-A candidates collapsed to 3 passing independent evidence gating: *Mediterraneibacter gnavus*, *Flavonifractor plautii*, and *Blautia wexlerae*, all in E3; 0/18 E1 candidates passed. [src: discoveries]

Pathway category schemas can reverse conclusions. Regex-based categories yielded 3 of 52 CD-up pathways in 7 themes and a structurally degenerate failure, whereas a MetaCyc hierarchy assigned 262/409 pathways to at least one of 12 IBD themes and supported iron/heme acquisition with OR=8.1, FDR=7e-6, and 15/52 CD-up pathways. The log therefore recommends curator-validated ontology hierarchies as primary and regex as sensitivity analysis. [src: discoveries]

Multi-line cross-corroboration was demonstrated for iron acquisition and bile-acid 7α-dehydroxylation using per-target lookup, cohort differential abundance, sample-level correlation, genomic content, metabolomics, strain-level nulls, and literature. For intervention design, each target should also be annotated for iron/AIEC mechanism, bile-acid coupling cost, and whether the signal is species-abundance-mediated or strain-content-mediated. [src: discoveries]

### Environmental, plant, and subsurface ecology

In a 3×3 SSO well grid spanning approximately 6 m, community similarity showed distance decay with Mantel rho=0.323 and p=0.029, driven by the east-west axis; a U3-M6-L7 diagonal followed the inferred plume flow path, and a *Rhodanobacter* hotspot reached 7.7%. Groundwater communities were temporally stable, with well R²=49.9% and date R²=0.8% over 9 days. *Candidatus Nitrosotalea* and *Sideroxydans* co-occurred at rho=+0.95, concentrated at U3. [src: discoveries]

The SSO campaign registered 221 METALS/ICTOC/ISOTOPES/NH3NO2 sample tubes in ENIGMA CORAL, but zero Assay Geochemistry processes were linked, so the analytical geochemistry values were not ingested. This limits validation of the contamination-plume model. [src: discoveries]

Among 25,660 plant-associated species, 60–85% were classified as dual-nature, carrying both beneficial and pathogenic markers. Plant compartment explained 53% of functional-profile variance (R²=0.53, pseudo-F=235, p=0.001); PGP genes were 64.6% core versus 45.2% for pathogenic genes (Mann–Whitney p=3.4e-125); and ACC deaminase had an odds ratio of 69.3 for root association. [src: discoveries]

Co-occurring plant-associated genera showed functional redundancy rather than complementarity, with permutation p=1.0 and Cohen's d=-7.54. After phylogenetic control, 50 novel eggNOG ortholog groups distinguished plant-associated species, led by COG3569 at OR=6.01. Singleton marker-gene clusters co-occurred with transposase/integrase singletons at OR=15.95, p=8.8e-20. [src: discoveries]

The pqqC–acdS pair co-occurred across 27K GTDB species at OR=7.24; acdS and pqqC were enriched in soil/rhizosphere environments at OR=7.0 and OR=2.9, respectively. All 13 PGP genes were predominantly core, with 29.7% mean accessory versus 53.2% genome-wide, rejecting the tested HGT hypothesis in favor of vertical inheritance. [src: discoveries]

Within Bacillota_B, deep-clay specialization was associated with expansion rather than streamlining: anchor genomes had 4.3 Mbp versus 3.2 Mbp in 62 phylum-matched soil genomes (d=+1.37, p=0.013) and 2,771 versus 2,233 eggNOG ortholog groups (d=+1.32, p=0.009), with comparable completeness of 94.7 versus 94.3 (p=0.93). Corrected multi-heme-cytochrome detection changed deep, shallow, and soil rates to 56%, 40%, and 41%; all cohort comparisons had Fisher p≥0.46, invalidating the original iron-reduction interpretation. [src: discoveries]

The clay cohort was enriched for sulfate-reduction markers relative to the Mitzscherling rock-attached null: 5/9 deep-clay genomes were SR-positive, with binomial p=4×10⁻¹². However, within Bacillota_B, Wood-Ljungdahl and group 1 [NiFe]-hydrogenase were not enriched in deep clay, with 5/5 versus 15/19 and 5/5 versus 14/19, respectively, both p=0.54; only sulfate reduction survived correction at p_BH=0.04. [src: discoveries]

### Metal tolerance and metabolic ecology

Across 7,609 metal-important gene records, 4,177 (55%) were genuinely metal-specific, 38% were general sick, and 7% were metal-plus-stress. Metal-specific genes were 84.8% core versus 90.2% for general-sick genes, with Cochran–Mantel–Haenszel p=0.011. UCP030820/OG01015, YebC/OG01383, and DUF1043-YhcB/OG03264 were the most metal-specific novel candidates at 67%, 58%, and 50%, respectively. [src: discoveries]

Counter-ion analysis found that 39.8% of metal-important genes overlapped NaCl-important genes across 19 organisms and 14 metals, but zinc sulfate, which contains 0 mM chloride, had 44.6% overlap and the highest DvH profile correlation, r=0.715. After shared-stress correction, core enrichment persisted for 12 of 14 metals; SynE was an experiment-count outlier with 88.6% overlap, and excluding it reduced the overall rate to 36.7%. [src: discoveries]

BacDive metal-tolerance scores predicted isolation from heavy-metal-contaminated environments at d=+1.00, p=0.006, n=10; the dose pattern was heavy metal +1.00, waste/sludge +0.57, all contamination +0.43, and industrial +0.20. Host-associated bacteria unexpectedly scored higher than environmental bacteria at d=+0.14, p<0.0001, likely because host-associated samples were enriched for large-genome Pseudomonadota pathogens. [src: discoveries]

### Analytical rigor and data-quality lessons

Across 9 adversarial review rounds, two citation failures recurred: PMID hijacking, where real PMIDs pointed to unrelated papers, and hallucinated author lists. Load-bearing citations require verification of author, title, journal, PMID, and DOI through PubMed, not merely DOI resolution. [src: discoveries]

Methodology revisions M1–M26 are not automatically a multiple-testing family. The referenced project had 4 pre-registered hypotheses, for which Bonferroni α=0.0125 was appropriate and all 4 survived; only M14, M21, and M23 were genuine post-hoc metric corrections. Family-wise error correction should be applied to actual hypothesis-test families, not to transparent documentation of methodological changes. [src: discoveries]

Standard review and adversarial review identified different classes of problems. Standard review called one project exceptionally sophisticated with no critical issues, whereas adversarial review found 5 critical and 6 important issues, including feature leakage, hard-coded positive interpretations of non-significant results, absent confounder adjustment, missing null distributions, and sample-size overclaims. Plan revisions and load-bearing notebooks should receive both review modes before downstream claims are accepted. [src: discoveries]

Large BERDL catalogs should be discovered through access-aware helpers rather than historical inventories, using `get_databases()`, `get_tables()`, and `get_table_schema()`. The live catalog included `kescience_mgnify`, PhageFoundry GenomeDepot databases, `kescience_interpro`, `kescience_pubmed`, `pangenome_bakta`, `arkinlab_microbeatlas`, `protect_integration`, and user-owned Klebsiella databases that were absent from older snapshots. [src: discoveries]

Local data marts benefit from `lineage.yaml`, `schema_overview.yaml`, per-table YAML dictionaries, and sentinel-code tables distinguishing pending data from true NULL values. Large Spark joins touching the 2.5B-row UniProt identifier table should disable broadcast joins with `SET spark.sql.autoBroadcastJoinThreshold = -1`; notebooks executed through nbconvert should cache large Spark outputs as CSV because direct `toPandas()` calls can cause DeadKernelError. [src: discoveries]

## Caveats

Several results are explicitly exploratory, coverage-limited, or dependent on analytical specification. The SSO geochemical model lacks ingested measurement values; AlphaEarth analyses had 3,838/83,287 genomes with NaN dimensions and 36.6% of genomes clustered at coordinates with more than 50 genomes of more than 10 species; only 6.8% of species had sufficient embedding coverage. [src: discoveries]

The NMDC metabolomics dataset was dominated by one study: 125/131 samples (95%) came from `nmdc:sty-11-r2h77870`. Only approximately 2% of compounds had KEGG IDs, substring matching risked collisions such as leucine versus isoleucine, and three amino-acid pathways—cysteine, histidine, and lysine—were untestable because compounds were absent. [src: discoveries]

BacDive species matching linked 42,227 strains (43.4% of 97K) to 6,426 GTDB pangenome species, leaving 56.6% unmatched because GTDB species boundaries differ from LPSN/DSMZ taxonomy. Phenotype-only metal-tolerance models were phylogenetically confounded: adding phenotype features changed R² by -0.009, while the full genome-resistance model reached R²=0.63. [src: discoveries]

Annotation proxies require source-specific validation. EggNOG `Preferred_name='lanM'` produced 505 additional hits with zero overlap with 62 Bakta-validated Lanmodulin genomes, eggNOG KO K02030 produced 46,369 nonspecific hits, and only 418 of 5,092 genomes with any xoxF marker hit both eggNOG K00114 and Bakta lanthanide-dependent methanol-dehydrogenase products. Results should therefore report marker definitions explicitly and avoid treating generic KOs or stale preferred names as definitive. [src: discoveries]

## Slots Into

- [[concepts/gene-essentiality]] — universal, variable, orphan, and module-transferred essentiality findings provide cross-organism evidence for the structure of bacterial essential genomes. [src: discoveries]
- [[concepts/pangenome-integration]] — pangenome conservation, accessory-gene innovation, dark matter, plant-associated genes, and ecological breadth findings extend cross-source genome-content synthesis. [src: discoveries]
- [[concepts/condition-specific-fitness]] — ADP1 respiratory wiring, metabolic dependencies, trade-offs, AMR costs, and pathway-capability findings refine condition-specific fitness interpretation. [src: discoveries]
- [[concepts/cofitness-network-architecture]] — ICA module stability, cross-organism module families, annotation granularity, and AMR support networks add architecture and validation evidence. [src: discoveries]
- [[concepts/metabolic-model-gapfilling]] — FBA blind spots, GapMind-versus-fitness comparisons, and pathway completeness versus dependency directly identify model gaps. [src: discoveries]
- [[concepts/multi-omics-integration]] — metabolite pools versus pathway capacity, NMDC community metabolomics, and multi-line microbiome corroboration support cross-modal integration. [src: discoveries]
- [[concepts/environmental-resistome]] — environment-dependent AMR composition, phylogenetic retention, resistance islands, and metal-specificity findings expand the environmental resistome synthesis. [src: discoveries]
- [[concepts/subsurface-bacillota-specialization]] — clay cohort bias, Bacillota_B genome expansion, sulfate-reduction enrichment, and corrected iron-reduction markers refine subsurface specialization. [src: discoveries]
- [[concepts/multi-heme-cytochrome-detection]] — corrected multi-heme cytochrome detection overturns the clay iron-reduction signal and establishes a marker-validation requirement. [src: discoveries]
- [[concepts/cross-tenant-data-bridging]] — live catalog discovery, BacDive-to-GTDB matching, PhageFoundry data, and BERDL data-mart conventions provide cross-tenant integration lessons. [src: discoveries]
- [[concepts/condition-specific-fitness]] — microbiome ecotype leakage, classifier mismatch, and cohort-batch effects define limits on transferring condition-specific models across cohorts. [src: discoveries]
