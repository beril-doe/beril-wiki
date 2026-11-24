---
type: "Summary"
description: "Summary of the project Prophage Gene Modules and Terminase-Defined Lineages Across Bacterial Phylogeny and Environmental Gradients."
doc_type: "short"
full_text: "sources/prophage_ecology__REPORT.md"
---
# Prophage Gene Modules and Terminase-Defined Lineages Across Bacterial Phylogeny and Environmental Gradients

This page summarises the project on prophage gene modules and terminase-defined lineages across bacterial phylogeny and environmental gradients. Prophage module content tracked genome size most strongly, then environment, then phylogeny. [src: prophage_ecology] Environment affected module composition beyond phylogeny (PERMANOVA F=30.04 vs phylogeny F=6.17, both p=0.01), so the report rejects phylogeny alone as an explanation. [src: prophage_ecology] Module enrichment in human-associated bacteria survived a phylogeny-and-genome-size null model. [src: prophage_ecology] No individual TerL (terminase large subunit) lineage showed environment-specific enrichment after FDR (false discovery rate) correction. [src: prophage_ecology] The report's prophage calls are annotation-based proxies, so prevalence is likely inflated. [src: prophage_ecology] Residual genome-size confounding, sparse environment metadata and taxonomy-based metagenome inference also limit the results. [src: prophage_ecology]

## Key Findings

### Prophage modules are near-universal in annotations

All 27,702 species carry prophage-associated gene clusters, 4,005,537 in total, found by querying 93M eggNOG annotations with 112 WHERE clause conditions. [src: prophage_ecology] Touchon et al. (2016) estimated that ~46% of bacterial genomes harbor prophages. [src: prophage_ecology] The report attributes its higher figure likely to identifying individual prophage-associated gene clusters, including domesticated remnants, rather than intact prophages. [src: prophage_ecology] Packaging (A), lysis (D) and lysogenic regulation (F) are near-universal at 100%, 99.9% and 100% of species. [src: prophage_ecology] This is consistent with Bobay et al. (2014), who showed that defective prophages under purifying selection often retain core regulatory and lysis functions. [src: prophage_ecology] Modules A, D and F were all ≥99% prevalent in the top 15 of 142 GTDB phyla. [src: prophage_ecology] The report suggests these modules include many domesticated prophage remnants. [src: prophage_ecology] Head morphogenesis (B, 56.1%), tail (C, 55.6%) and anti-defense (G, 64.3%) vary most. [src: prophage_ecology] The report treats B, C and G as more informative for prophage ecology because their presence indicates more complete prophage elements. [src: prophage_ecology] In this analysis, 34.9% of species carry all 7 modules. [src: prophage_ecology]

| Module | Gene clusters | Species with module |
|---|---|---|
| A. Packaging | 707,217 | 100.0% [src: prophage_ecology] |
| B. Head Morphogenesis | 87,336 | 56.1% [src: prophage_ecology] |
| C. Tail | 189,271 | 55.6% [src: prophage_ecology] |
| D. Lysis | 724,499 | 99.9% [src: prophage_ecology] |
| E. Integration | 773,417 | 99.1% [src: prophage_ecology] |
| F. Lysogenic Regulation | 1,682,902 | 100.0% [src: prophage_ecology] |
| G. Anti-Defense | 63,508 | 64.3% [src: prophage_ecology] |

Prevalence of the variable modules differs widely across groups. Head morphogenesis (B) ranged from 10.2% in Thermoplasmatota to 81% in human_associated species. [src: prophage_ecology] Tail (C) ranged from 6.5% in Thermoplasmatota to 82% in food-associated species. [src: prophage_ecology] Anti-defense (G) ranged from 3.1% in Patescibacteria to 97.8% in Campylobacterota. [src: prophage_ecology]

Conservation differs by module. Lysis (D) was 62.6% core and packaging (A) 57.0% core. [src: prophage_ecology] Integration (E) was 59.3% singleton and head morphogenesis (B) 56.0% singleton. [src: prophage_ecology] Validation found all 7 modules in each of 8 well-characterized prophage-carrying species: Escherichia coli, Salmonella enterica, Staphylococcus aureus, Pseudomonas aeruginosa, Mycobacterium tuberculosis, Bacillus subtilis, Vibrio cholerae and Streptococcus pyogenes. [src: prophage_ecology]

### Genome size, environment and phylogeny

PERMANOVA (permutational multivariate analysis of variance) on Bray-Curtis distances used a subsample of n=1,773 species and 99 permutations. [src: prophage_ecology] All three predictors were significant at p=0.01, with very different effect sizes: genome size quartile F=212.99 (4 groups), environment F=30.04 (10 groups) and family phylogeny F=6.17 (294 groups). [src: prophage_ecology] Genome size was the dominant predictor, with rho=0.717 against prophage cluster count, followed by environment, then phylogeny. [src: prophage_ecology] The report notes that residual confounding by genome size cannot be excluded, because larger genomes have more genes of all types, not just prophage genes. [src: prophage_ecology] Within each genome size quartile, Kruskal-Wallis tests still found an environmental effect on module count (all p < 6.5e-78). The report reads this as excluding a genome size artifact. [src: prophage_ecology] AlphaEarth embeddings for 2,008 species with ≥5 embedded genomes gave a partial Spearman correlation of niche breadth with module count, controlling for genome size, of rho=0.468 (p=8.41e-110). [src: prophage_ecology] Only 28% of genomes have these embeddings, which biases that subsample toward clinically and environmentally well-sampled lineages. [src: prophage_ecology]

Environment was classified from NCBI isolation_source metadata for 293,050 genomes, giving 10 categories with ≥30 species. [src: prophage_ecology] Chi-squared tests found significant environment associations for B_head (chi2=1,051, p=1.72e-220), C_tail (chi2=1,749, p≈0) and G_anti_defense (chi2=818, p=2.58e-170). [src: prophage_ecology] The metadata are sparse and inconsistently labeled, and the 10 categories collapse substantial within-category variation. [src: prophage_ecology] The "other_unknown" category holds 9,659 species (35%), which limits statistical power. [src: prophage_ecology]

### Environment-specific enrichment beyond phylogeny

Constrained null models (500 permutations preserving host family × genome size quartile strata, 18,031 species) found 8 significant module × environment enrichments at FDR < 0.05. [src: prophage_ecology] Human-associated and clinical environments had higher prevalence of tail and head morphogenesis modules and anti-defense genes than freshwater, marine and animal-associated environments, after controlling for host family composition and genome size. [src: prophage_ecology] Anti-defense was the most environmentally responsive module. [src: prophage_ecology] Ubiquitous modules (A, D, F) varied little by environment, while B, C and G carried the signal. [src: prophage_ecology]

| Module | Environment | log2(OR) | Z | Direction |
|---|---|---|---|---|
| Tail | human_associated | 2.21 | 10.86 | Enriched [src: prophage_ecology] |
| Head Morphogenesis | human_associated | 1.98 | 10.00 | Enriched [src: prophage_ecology] |
| Anti-Defense | human_associated | 1.70 | 8.76 | Enriched [src: prophage_ecology] |
| Anti-Defense | human_clinical | 0.14 | 5.14 | Enriched [src: prophage_ecology] |
| Tail | human_clinical | 0.77 | 3.90 | Enriched [src: prophage_ecology] |
| Head Morphogenesis | human_clinical | 0.70 | 3.59 | Enriched [src: prophage_ecology] |
| Anti-Defense | freshwater | -0.74 | -4.74 | Depleted [src: prophage_ecology] |
| Anti-Defense | animal_associated | -0.24 | -8.77 | Depleted [src: prophage_ecology] |

The null model used 200 permutations for z-score estimation in the co-occurrence analysis, which the report calls adequate but not exhaustive in precision. [src: prophage_ecology]

The report sees the human-associated enrichment as consistent with Low et al. (2024), who demonstrated enrichment of prophage-encoded cargo genes in human-impacted environments across 38,605 genomes. [src: prophage_ecology] Tesson et al. (2024) found that 89% of anti-defense systems localize in mobile genetic elements, predominantly prophages. [src: prophage_ecology] Bernheim & Sorek (2020) proposed a pan-immune system model in which defense system diversity drives counter-defense evolution. [src: prophage_ecology] The Piggyback-the-Winner framework predicts higher lysogeny at high microbial densities in host-associated environments. [src: prophage_ecology] The report says its results extend this: the increase is specifically in structural completeness and anti-defense repertoire, not merely lysogeny. [src: prophage_ecology] It suggests that human-associated bacteria face more intense phage-mediated selective pressure, driving retention of complete lytic machinery and counter-defense genes, and that host-phage arms races are most intense there. These are interpretations, not direct measurements. [src: prophage_ecology]

## Module co-occurrence and modularity

Across 15 phylogenetically stratified species (one per phylum, max 300 genomes each, 200 null permutations), 44/95 module-species tests (46.3%) showed significantly higher within-module gene co-occurrence than chance (z > 1.96, one-tailed). [src: prophage_ecology] Testing one species per phylum gives broad phylogenetic coverage but limited within-phylum replication. [src: prophage_ecology] Mean contig co-localization across all tests was 0.769. [src: prophage_ecology] Packaging, lysis and lysogenic regulation were strongest; integration did not co-occur. [src: prophage_ecology]

| Module | Significant species tests | Mean Z | Mean contig co-localization | Report's reading |
|---|---|---|---|---|
| A. Packaging | 11/15 | 3.40 | 0.986 | Strong; same contig [src: prophage_ecology] |
| B. Head Morphogenesis | 1/6 | -0.44 | 0.474 | Weak; sparse across species [src: prophage_ecology] |
| C. Tail | 5/12 | 1.43 | 0.752 | Moderate [src: prophage_ecology] |
| D. Lysis | 13/15 | 4.45 | 0.901 | Strongest of any module [src: prophage_ecology] |
| E. Integration | 1/15 | -1.93 | 0.420 | Not co-occurring, expected for integrases [src: prophage_ecology] |
| F. Lysogenic Regulation | 10/15 | 2.16 | 1.000 | Significant; perfect co-localization [src: prophage_ecology] |
| G. Anti-Defense | 3/11 | 1.50 | 0.281 | Weak; scattered placement [src: prophage_ecology] |

Head morphogenesis (B) was testable in only 6 species because of sparsity. [src: prophage_ecology] The report reads the core modules A, D and F as physically linked functional units, not independently distributed annotations. [src: prophage_ecology] It explains the missing integration signal as expected, because integrases sit at different insertion sites and many are domesticated remnants. [src: prophage_ecology] This is consistent with Bobay et al. (2014), cited as showing that domesticated remnants are more common than intact prophages and often retain only integrases. [src: prophage_ecology] The low anti-defense co-localization (0.281) is read as consistent with defense islands separate from the core backbone, in line with Pinilla-Redondo et al. (2020) and Rahimian et al. (2026). [src: prophage_ecology] The report states that these results suggest integration (E) and anti-defense (G) behave differently from the core prophage modules. [src: prophage_ecology] Together, the report says this supports a two-tier model: a core backbone plus scattered accessory functions. [src: prophage_ecology] It calls NB03 the first large-scale empirical validation of the modular theory of phage evolution at the pangenome level. [src: prophage_ecology]

## TerL lineages

MMseqs2 clustering of 38,085 TerL sequences from 11,789 species at 70% amino acid identity gave 10,991 lineages. [src: prophage_ecology] The size distribution is highly skewed, with median=1 and a maximum of 1,094 across 869 species; the 869 species refers to the largest lineage, not to the whole clustering input. [src: prophage_ecology] The largest lineage, L_SFJM01000051.1_13, has 1,094 members across 869 species and is described as a cosmopolitan prophage type. [src: prophage_ecology] There were 6,921 singleton lineages (63%), described as species-specific. [src: prophage_ecology] Lineage counts ranged from 4,001 at 50% AAI to 16,283 at 80% AAI. [src: prophage_ecology]

No individual TerL lineage showed significant environment-specific enrichment after FDR correction (0/500 tests), so the H1b hypothesis was not supported at the individual lineage level. [src: prophage_ecology] The report concludes that lineage-level adaptation does not exceed what host phylogeny predicts. [src: prophage_ecology] Under constrained permutations preserving host family composition, lineage distribution is well explained by host phylogeny alone, consistent with Mavrich & Hatfull (2017), who showed that temperate phage evolution is primarily shaped by host range rather than environmental selection. [src: prophage_ecology] This contrasts with Paez-Espino et al. (2016), who found strong habitat-type specificity for most viral groups. [src: prophage_ecology] Shannon entropy analysis of 824 lineages with ≥5 species found 325 specialist lineages (Shannon < 1.0 or dominant environment > 80%), concentrated in animal_associated, freshwater and marine environments. [src: prophage_ecology] It also found 499 generalist lineages spread across 3+ environments. [src: prophage_ecology] The report says this shows niche breadth varies substantially even though no single lineage exceeds the constrained null. [src: prophage_ecology] It reads lineage ecology as largely mirroring host ecology, consistent with the two gene-flux modes of Mavrich & Hatfull (2017). [src: prophage_ecology] Module-level effects beyond phylogeny but no lineage-level effects suggest modular exchange rather than whole-phage adaptation to environments. [src: prophage_ecology]

## Metagenome cross-validation

Genus-level pangenome-derived prophage burden scores were applied to 6,365 NMDC metagenomic samples through two-tier taxonomy mapping (a GTDB metadata bridge plus taxonomy_dim genus matching). [src: prophage_ecology] Coverage was 87.2% median matching, and the analysis gave 57 significant module-abiotic correlations at FDR < 0.05, with pH and temperature the strongest predictors, so H1d was supported. [src: prophage_ecology] Spearman correlations included packaging with pH (rho 0.519), and all-module burden with pH (0.474), temperature (0.399), depth (0.361) and total nitrogen (0.333). [src: prophage_ecology] The report suggests alkaline environments may favor lysogeny, consistent with pH-sensitive stress-induced prophage induction. [src: prophage_ecology] Modules B, C and G were significant in both the pangenome enrichment and the NMDC analyses, and cross-validation confirmed concordance for them. [src: prophage_ecology] A, D, E and F were NMDC-significant but not pangenome-enriched beyond phylogenetic expectation. The report attributes this to their near-universal presence masking environment-specific variation. [src: prophage_ecology] This inference assumes genus-level conservation of prophage content, which may fail for recently acquired or lost prophages, and the approach was validated for the PHB (polyhydroxybutyrate) granule ecology project but not independently for prophage genes. [src: prophage_ecology]

## Data and Methods

Prophage gene identification, taxonomy, environment metadata, genome size and co-occurrence came from the kbase_ke_pangenome collection in the KBase Data Lakehouse. [src: prophage_ecology] Its source tables were eggnog_mapper_annotations, gene_cluster, genome, gtdb_species_clade, gtdb_taxonomy_r214v1, gtdb_metadata, pangenome, ncbi_env, alphaearth_embeddings_all_years, gene and gene_genecluster_junction. [src: prophage_ecology] Metagenomic cross-validation of prophage burden used the nmdc_arkin tables taxonomy_features, taxonomy_dim, abiotic_features and study_table. [src: prophage_ecology]

## Novelty claim

The report claims the first systematic module-level analysis of prophage architecture across >27,000 bacterial species and 10 environment categories. [src: prophage_ecology] Previous studies examined whole-prophage presence/absence (Touchon et al. 2016) or specific phage types (Camarillo-Guerrero et al. 2021). [src: prophage_ecology]

## Caveats and Open Work

The module calls rest on eggNOG functional annotations used as proxies, not dedicated tools such as geNomad or VIBRANT. [src: prophage_ecology] This likely inflates prevalence by including domesticated remnants and bacterial homologs such as integrases, and the false positive rate is uncharacterized. [src: prophage_ecology] Near-universal modules A, D and F may therefore reflect domesticated remnants rather than active prophages. [src: prophage_ecology] Module definitions are validated for the core backbone (A, D, F) but less so for accessory functions (E, G). [src: prophage_ecology] Genome size is the dominant predictor, and residual confounding cannot be excluded despite stratification and partial correlations. [src: prophage_ecology] The PERMANOVA used a 1,773-species subsample with only 99 permutations. [src: prophage_ecology] The NMDC burden is inferred from taxonomy, not measured directly, and rests on untested genus-level conservation. [src: prophage_ecology] Environment metadata are sparse, coarse and 35% "other_unknown". [src: prophage_ecology] The embedding subsample covers only 28% of genomes. [src: prophage_ecology] The co-occurrence tests have limited within-phylum replication, and module B was testable in only 6 species. [src: prophage_ecology] The 200-permutation null gives adequate but not exhaustive precision. [src: prophage_ecology] The null TerL result means lineage-level environmental adaptation was not detected beyond host phylogeny. [src: prophage_ecology]

The report proposes these next analyses:
- Run geNomad or VIBRANT on representative genomes to estimate false positive and negative rates of the annotation-based approach and calibrate module prevalence. [src: prophage_ecology]
- Use sequential or partial PERMANOVA to quantify the unique environmental variance after controlling for phylogeny and genome size together, instead of testing each predictor independently. [src: prophage_ecology]
- Split future analysis into a core prophage backbone (A, D, F) and accessory functions (B, C, E, G). [src: prophage_ecology]
- Test the "arms race" hypothesis by asking whether anti-defense genes (Module G) co-localize with defense system genes in the same genomes. [src: prophage_ecology]
- Cross-reference environment-enriched modules with prophage induction triggers (SOS response, pH stress, temperature shifts) to explain the NMDC pH and temperature correlations. [src: prophage_ecology]
- Use NMDC longitudinal samples, if available, to test within-site changes in prophage burden over time, giving causal evidence beyond cross-sectional correlations. [src: prophage_ecology]

## Slots Into

- [[concepts/environmental-structuring-of-prophage-gene-modules-beyond-host-phylogeny]]: environment effects on modules exceeded phylogeny, with 8 significant enrichments. [src: prophage_ecology]
- [[concepts/annotation-based-prophage-detection-prevalence-and-domesticated-remnants]]: eggNOG-based calls likely inflate prevalence. [src: prophage_ecology]
- [[concepts/modular-architecture-and-co-occurrence-of-prophage-genes]]: modules A, D and F co-occur and co-localize. [src: prophage_ecology]
- [[concepts/prophage-anti-defense-genes-and-host-phage-arms-races]]: anti-defense was the most environment-responsive module. [src: prophage_ecology]
- [[concepts/abiotic-correlates-of-prophage-burden-in-metagenomes]]: 57 NMDC module-abiotic correlations. [src: prophage_ecology]
- [[concepts/environmental-specificity-of-prophage-terminase-lineages]]: no lineage passed FDR. [src: prophage_ecology]
