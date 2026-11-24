---
type: "Summary"
description: "Summary of the project Environmental Resistome at Pangenome Scale."
doc_type: "short"
full_text: "sources/amr_environmental_resistome__REPORT.md"
---
# Environmental Resistome at Pangenome Scale

Summary of the project Environmental Resistome at Pangenome Scale. The report's central finding is that ecological niche is a strong predictor of antimicrobial resistance (AMR) gene content across 14,723 bacterial species. [src: amr_environmental_resistome] Effect sizes are modest, and environment and phylogeny stay entangled. [src: amr_environmental_resistome] See [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance]] for the wider topic.

## Key Findings

### Species AMR diversity by environment

Environment explains a modest but highly significant share of species AMR diversity. Clinical species have a median of 5 AMR gene clusters, against 2 for soil, aquatic and host-associated species (Kruskal-Wallis H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056). [src: amr_environmental_resistome] Human gut species are similar to clinical (median 5). [src: amr_environmental_resistome] Of 15 pairwise environment comparisons, 13 are significant after false discovery rate (FDR) correction. [src: amr_environmental_resistome] The largest effect is clinical vs aquatic (rank-biserial r = −0.49). [src: amr_environmental_resistome] The effect holds at 50%, 60%, 75% and 90% majority-vote thresholds (η² = 0.044–0.056). [src: amr_environmental_resistome] The report states that clinical and human gut species carry 2.5× more AMR clusters than soil or aquatic species, with the excess almost entirely accessory. [src: amr_environmental_resistome] The report presents this as extending Gibson et al. (2015, ISME J), who studied ~6,000 genomes, to 14,723 species across 293K genomes, a 50× increase in scale. [src: amr_environmental_resistome] It says the pattern holds within phyla and families and is not a phylogenetic artifact. [src: amr_environmental_resistome]

### Core versus accessory AMR

Mean core and accessory shares by environment:

| Environment | Core | Accessory |
|---|---|---|
| Soil | 57.1% [src: amr_environmental_resistome] | 42.9% [src: amr_environmental_resistome] |
| Aquatic | 54.4% [src: amr_environmental_resistome] | 45.6% [src: amr_environmental_resistome] |
| Host-associated | 49.7% [src: amr_environmental_resistome] | 50.3% [src: amr_environmental_resistome] |
| Other environmental | 40.4% [src: amr_environmental_resistome] | 59.6% [src: amr_environmental_resistome] |
| Clinical | 32.4% [src: amr_environmental_resistome] | 67.6% [src: amr_environmental_resistome] |
| Human gut | 19.7% [src: amr_environmental_resistome] | 80.3% [src: amr_environmental_resistome] |

The report reads this as confirming, at pangenome scale, Jiang et al. (2024) river-metagenome observations (PMID: 38039820). In that reading the core resistome is chromosomal and intrinsic, and the rare/accessory resistome is mobile and acquired. [src: amr_environmental_resistome] It asserts that clinical and gut species acquired AMR mainly through horizontal gene transfer (HGT), while soil and aquatic species keep more ancient chromosomal resistance. [src: amr_environmental_resistome]

### Mechanism composition

All four AMR mechanisms show significant environment-dependent composition (all q ~ 0 after Benjamini-Hochberg false discovery rate, BH-FDR). [src: amr_environmental_resistome] The assembled resistome includes 26,220 enzymatic-inactivation, 22,223 metal-resistance, 11,067 target-modification and 5,224 efflux gene clusters. [src: amr_environmental_resistome] Kruskal-Wallis (KW) H values are 1498.4 for metal resistance, 1394.9 for target modification, 768.0 for efflux and 266.0 for enzymatic inactivation. [src: amr_environmental_resistome] Metal resistance has the largest effect. It makes up 45% of aquatic AMR and 44% of soil AMR, but 6% of human gut AMR. [src: amr_environmental_resistome] Target modification makes up 44% of human gut AMR, 28% of clinical AMR and 6% of aquatic AMR. [src: amr_environmental_resistome] Fractions by environment:

| Mechanism | Clinical | Human gut | Host-assoc. | Soil | Aquatic | Other env. | η² |
|---|---|---|---|---|---|---|---|
| Efflux | 6.1% | 7.0% | 3.7% | 2.0% | 1.1% | 2.7% | 0.055 [src: amr_environmental_resistome] |
| Enzymatic inactivation | 28.2% | 24.1% | 44.1% | 34.3% | 41.2% | 33.6% | 0.019 [src: amr_environmental_resistome] |
| Metal resistance | 19.7% | 6.1% | 12.7% | 44.0% | 45.0% | 24.9% | 0.107 [src: amr_environmental_resistome] |
| Target modification | 27.5% | 43.6% | 22.8% | 10.1% | 6.2% | 25.1% | 0.100 [src: amr_environmental_resistome] |

The report interprets these patterns as niches selecting fundamentally different resistance strategies. [src: amr_environmental_resistome] It says soil and aquatic bacteria devote 44-45% of AMR to metal resistance, reflecting natural heavy-metal exposure, and that these genes are more often core, suggesting ancient adaptation. [src: amr_environmental_resistome] It also says clinical and gut bacteria devote 15-21% of AMR to efflux pumps and 19-29% to target modification, reflecting antibiotic selection pressure, and that these genes are more often accessory, reflecting recent HGT-driven accumulation. [src: amr_environmental_resistome] These stated ranges disagree with the report's own table: the table gives efflux of 6.1% (clinical) and 7.0% (human gut), and target modification of 27.5% and 43.6%, and the text above gives 44% of human gut AMR as target modification. [src: amr_environmental_resistome] The report does not reconcile the two sets of figures, so the table values and the narrative ranges should each be read as stated. Its summary states that metal resistance peaks in soil/aquatic at 45% and target modification in gut/clinical at 28-44%. [src: amr_environmental_resistome] It describes enzymatic inactivation, including beta-lactamases, as the most uniformly distributed mechanism, present in all environments but dominant in none. [src: amr_environmental_resistome]

The report links this to the amr_fitness_cost finding that metal resistance is 44% accessory while efflux is 13% core. [src: amr_environmental_resistome] It argues that efflux is core because it serves host-associated organisms constitutively, and that metal resistance is accessory because it varies with environmental metal exposure. [src: amr_environmental_resistome]

Limits on these fractions: 18.7% of AMR clusters (15,550) could not be classified from gene name or product annotation and are excluded. This could bias results if unclassified genes are non-randomly distributed across environments. [src: amr_environmental_resistome] The report splits tetracycline resistance between efflux (tet(A-E,K,L)) and target modification (tet(M,O,Q,W) ribosomal protection proteins). [src: amr_environmental_resistome]

### Clinical exposure and species case studies

The report states that AMR accumulation varies within species depending on where strains are found. [src: amr_environmental_resistome] A species-level proxy supports the clinical–AMR link, but it is not a true per-genome within-species comparison, which would need billion-row joins. [src: amr_environmental_resistome] It tests whether species with mostly clinical-source genomes carry more AMR than species with mostly environmental-source genomes. [src: amr_environmental_resistome] Among 823 species with genomes in ≥2 environments (≥5 genomes each), clinical genome fraction predicts total AMR cluster count (Spearman rho = 0.465, p = 2.2×10⁻⁴⁵). [src: amr_environmental_resistome] The report calls this its strongest evidence that AMR accumulation tracks antibiotic exposure at the strain level. [src: amr_environmental_resistome] Clinical-dominated species have 4.4× more AMR clusters (mean 72.9 vs 16.4, Mann-Whitney U, MWU, p = 2×10⁻¹⁸). [src: amr_environmental_resistome] They also have a higher accessory fraction in a grouped comparison (93.6% vs 81.7%, MWU p = 0.004). [src: amr_environmental_resistome] The continuous correlation of clinical fraction with % accessory is only borderline (rho = 0.065, p = 0.064). [src: amr_environmental_resistome]

Case-study species are nearly all accessory:

| Species | Genomes | AMR clusters | Core | Accessory | Dominant environment |
|---|---|---|---|---|---|
| K. pneumoniae | 13,637 | 1,115 | 7 | 1,108 (99%) | Clinical (80%) [src: amr_environmental_resistome] |
| S. aureus | 13,274 | 642 | 9 | 633 (99%) | Clinical (85%) [src: amr_environmental_resistome] |
| S. enterica | 10,097 | 836 | 11 | 825 (99%) | Host-associated (31%) [src: amr_environmental_resistome] |
| S. pneumoniae | 7,944 | 59 | 1 | 58 (98%) | Clinical (99.6%) [src: amr_environmental_resistome] |
| M. tuberculosis | 6,673 | 44 | 4 | 40 (91%) | Clinical (98%) [src: amr_environmental_resistome] |

The report interprets the K. pneumoniae pattern as massive within-species AMR variation driven by HGT in clinical settings. [src: amr_environmental_resistome]

### Phylogeny check

The environment effect is not only a proxy for phylogeny. Five of 6 major phyla (Pseudomonadota, Bacillota_A, Actinomycetota, Bacteroidota, Bacillota) show significant within-phylum environment effects on AMR. [src: amr_environmental_resistome] Only Chloroflexota is non-significant. [src: amr_environmental_resistome] Bacteroidota has the largest within-phylum effect (η² = 0.130). [src: amr_environmental_resistome] At family level, 20 of 141 testable families (14%) are significant after FDR correction. [src: amr_environmental_resistome] The top families are Enterobacteriaceae (q = 3×10⁻²¹) [src: amr_environmental_resistome], Bacteroidaceae (q = 1.3×10⁻¹⁷) [src: amr_environmental_resistome], Lachnospiraceae (q = 2.5×10⁻¹²) [src: amr_environmental_resistome] and Pseudomonadaceae (q = 3.9×10⁻¹²). [src: amr_environmental_resistome] The report concludes that even within the same family, species in different environments carry different AMR profiles. [src: amr_environmental_resistome] It regards the 14% of families as its most convincing evidence, but most families span too few environments to test. [src: amr_environmental_resistome]

### AlphaEarth embeddings

Among 2,659 species with AMR data and AlphaEarth environmental embeddings, 52 of 64 embedding dimensions correlate significantly with AMR diversity (FDR < 0.05; top A34, rho = +0.24). [src: amr_environmental_resistome] A Mantel test finds that cosine distance of embeddings predicts Bray-Curtis distance of mechanism fractions (r = 0.098, p = 0.001). [src: amr_environmental_resistome] Coupling is strongest for clinical species (r = 0.177), moderate for soil (r = 0.129) and weakest for aquatic (r = 0.061). [src: amr_environmental_resistome]

### Relation to earlier literature

The report says it replicates the ecology-clustered resistomes of Gibson, Forsberg & Dantas (2015, PMID: 25003965; ~6,000 genomes) at 50× scale. It adds that efflux and metal resistance are the most environment-discriminating mechanisms. [src: amr_environmental_resistome] It sees its core soil and accessory clinical AMR as aligning with Forsberg et al. (2014, PMID: 24847883), who found phylogeny-structured soil resistomes with rare mobility elements. [src: amr_environmental_resistome] It reads soil's fewer, more intrinsic genes as an ancient baseline resistome (Surette & Wright 2017, PMID: 28657887), with clinical enrichment reflecting anthropogenic selection. [src: amr_environmental_resistome] Soil species averaging 2 AMR clusters, mostly core, is consistent with Van Goethem et al. (2018, PMID: 29471872), who found resistance genes in pristine Antarctic soils. [src: amr_environmental_resistome] Forsberg et al. (2012, PMID: 22936781) found soil genes identical in nucleotides to clinical ones; the report did not test nucleotide identity. [src: amr_environmental_resistome]

## Data and Methods

The dataset has 82,908 AMR gene clusters across 14,723 species out of 27,700 total. [src: amr_environmental_resistome] There are 280,337 genomes with ncbi_env data, 93.5% classified per genome. [src: amr_environmental_resistome] Majority-vote environment assignment covers 95% of species (13,981). [src: amr_environmental_resistome] In data assembly, 884 species qualify for within-species analysis (≥5 genomes in ≥2 environments). [src: amr_environmental_resistome]

The report drew on the KBase Data Lakehouse collection kbase_ke_pangenome, using its bakta_amr, gene_cluster, pangenome, ncbi_env, genome, gtdb_taxonomy_r214v1 and alphaearth_embeddings_all_years tables. These supplied AMR clusters, species structure, environment metadata, phylogeny and continuous environment embeddings. [src: amr_environmental_resistome]

Output tables include species AMR profiles (14,723 rows) [src: amr_environmental_resistome], species majority-vote environments (26,715 rows) [src: amr_environmental_resistome], per-genome environments from ncbi_env (280,337 rows) [src: amr_environmental_resistome], 15 pairwise Mann-Whitney U environment tests [src: amr_environmental_resistome], Kruskal-Wallis results for 4 mechanisms [src: amr_environmental_resistome], 6 within-phylum tests [src: amr_environmental_resistome], 141 within-family tests [src: amr_environmental_resistome], 823 within-species clinical-fraction rows [src: amr_environmental_resistome] and 64 per-dimension embedding-AMR correlations. [src: amr_environmental_resistome]

The analysis is organised in four notebooks. The first covers Spark extraction, environment and mechanism classification, and validation. [src: amr_environmental_resistome] The second covers H1-H3: species-level AMR versus environment, phylogenetic control and sensitivity analysis. [src: amr_environmental_resistome] The third covers H4: within-species AMR variation by clinical fraction, plus case studies. [src: amr_environmental_resistome] The fourth is supplementary, with continuous embedding-AMR correlations and a Mantel test. [src: amr_environmental_resistome]

## Caveats and Open Work

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
