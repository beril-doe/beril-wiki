---
type: "Summary"
description: "Summary of the project Within-Species AMR Strain Variation."
doc_type: "short"
full_text: "sources/amr_strain_variation__REPORT.md"
---
# Within-Species AMR Strain Variation

This report asks how antimicrobial resistance (AMR) gene content varies among strains of the same species. Its answer is that over 90% of AMR gene occurrences are variable or rare across strains, and that this variation is structured by resistance islands, phylogeny and, in some species, ecotypes. [src: amr_strain_variation] It claims to be the first systematic simultaneous quantification across >1,300 species, enabled by the KBase Data Lakehouse pangenome resource. [src: amr_strain_variation] Its environment and temporal tests are limited by sparse metadata. [src: amr_strain_variation]

## Key Findings

### Prevalence of AMR genes within species

Most AMR gene-species occurrences are not fixed within a species. Across 1,305 species and 180,025 genomes, 51.3% are rare (present in <=5% of strains) [src: amr_strain_variation], 41.3% are variable (5-95%) [src: amr_strain_variation], and only 7.5% are fixed (>=95%). [src: amr_strain_variation] The report states that 51% of AMR genes are rare within any given species. [src: amr_strain_variation] It says this quantifies, at unprecedented scale, the complexity noted by Sanchez-Buso et al. (2020), who described pangenomic perspectives on AMR emergence and maintenance and the complexity strain-specific mechanisms add. [src: amr_strain_variation] The median variability index is 0.526, which the report reads as over half of a species' AMR genes falling in the variable zone. [src: amr_strain_variation] The median pairwise Jaccard distance between strains is 0.435, so strains share less than 60% of their AMR repertoire. [src: amr_strain_variation]

The report concludes that variable AMR repertoires, resistance islands and phylogenetic signal are general features of bacterial AMR biology, not limited to well-studied clinical species. [src: amr_strain_variation]

The atlas conservation classes track within-species prevalence, and the report reads this as validating the classification at strain resolution. [src: amr_strain_variation] The analysis covers 37,444 AMR gene-species records. [src: amr_strain_variation] Core genes are 77.3% fixed, 22.7% variable and 0.0% rare. [src: amr_strain_variation] Auxiliary genes are 0.0% fixed, 57.3% variable and 42.7% rare. [src: amr_strain_variation] Singleton genes are 0.0% fixed, 21.3% variable and 78.7% rare. [src: amr_strain_variation]

Median variability index by phylum:

| Phylum | Median index | Species |
|---|---|---|
| Bacillota | 0.487 [src: amr_strain_variation] | 248 |
| Bacillota_C | 0.500 [src: amr_strain_variation] | 21 |
| Bacteroidota | 0.509 [src: amr_strain_variation] | 100 |
| Pseudomonadota | 0.533 [src: amr_strain_variation] | 591 |
| Actinomycetota | 0.533 [src: amr_strain_variation] | 133 |
| Bacillota_A | 0.600 [src: amr_strain_variation] | 184 |

AMR variability weakly anti-correlates with pangenome openness (Spearman rho = -0.193, p = 2.2e-12). [src: amr_strain_variation] The report proposes that open-pangenome species accumulate rare or singleton AMR genes below the 5% threshold, which deflates the index. [src: amr_strain_variation] This is an explanation, not a tested result.

### Resistance islands

Resistance islands are tight co-occurring gene sets. The report detected 1,517 islands across 705 species (54% of those analyzed). [src: amr_strain_variation] The mean island size is 6.2 genes (median 4, max 43) [src: amr_strain_variation], and the mean phi coefficient is 0.827, indicating very tight co-occurrence. [src: amr_strain_variation] The report interprets the high phi as suggesting islands are inherited as intact units rather than randomly assembled. [src: amr_strain_variation] It calls this consistent with the role of transposons, integrons and genomic islands in co-mobilizing resistance determinants (Partridge et al. 2018). [src: amr_strain_variation] The report concludes that AMR genes are frequently co-inherited as multi-gene modules. [src: amr_strain_variation]

Of the islands, 88% (1,343/1,517) contain genes from multiple resistance mechanisms. [src: amr_strain_variation] The report suggests this composition gives coordinated defense against several drug classes at once. [src: amr_strain_variation] It also reads the 88% as suggesting selection for co-maintenance of complementary strategies. [src: amr_strain_variation] Both readings are interpretation. Co-occurrence in islands does not prove co-selection. It may reflect linkage on one mobile element without functional synergy. [src: amr_strain_variation]

Number of islands containing each mechanism:

| Mechanism | Islands |
|---|---|
| Other/Unclassified | 1,026 [src: amr_strain_variation] |
| Efflux | 954 [src: amr_strain_variation] |
| Enzymatic inactivation | 698 [src: amr_strain_variation] |
| Oxidoreductase | 694 [src: amr_strain_variation] |
| Regulatory | 502 [src: amr_strain_variation] |
| Beta-lactamase | 341 [src: amr_strain_variation] |
| Target modification | 293 [src: amr_strain_variation] |
| Cell wall modification | 137 [src: amr_strain_variation] |

### Phylogenetic signal

AMR content follows phylogeny. Mantel tests (which compare average nucleotide identity, ANI, distance matrices with AMR Jaccard distance matrices) across 1,261 species found significant signal in 55.6% (701 species) at false discovery rate (FDR) < 0.05. [src: amr_strain_variation] The median Mantel r is 0.247 [src: amr_strain_variation], and 87.8% of species show a positive correlation. [src: amr_strain_variation] Closely related strains therefore tend to share more AMR genes. [src: amr_strain_variation]

The result is counter-intuitive for acquired genes. Non-core (putatively acquired) genes show stronger signal (median r = 0.222) than core (intrinsic) genes (median r = 0.117). The paired t-test gave t = -8.35, p = 7.0e-16, n = 489. [src: amr_strain_variation] The report calls this its most surprising finding. [src: amr_strain_variation] It suggests acquired genes are more often inherited clonally within lineages than randomly acquired by horizontal transfer. [src: amr_strain_variation] It proposes that acquired elements are stably maintained and vertically transmitted, creating lineage-specific signatures. [src: amr_strain_variation] In its model, a lineage that acquires resistance genes, likely via mobile genetic elements, keeps them stably integrated and vertically inherited, creating clonal AMR lineages. [src: amr_strain_variation]

This limits the contrast: core genes are nearly universal (>=95% prevalence by definition), so their Jaccard distances are near zero with little variance. That suppresses distance-based metrics such as Mantel r and partially explains their lower signal independent of biology. [src: amr_strain_variation]

The report links the result to Maier et al. (2025), who found AMR transfer largely confined to closely related lineages and a negative effect of genetic compatibility on cross-species transfer. [src: amr_strain_variation] It says the finding has not been shown at this scale and suggests that tracking clonal lineages may be more informative for AMR surveillance than tracking individual resistance genes. [src: amr_strain_variation]

### AMR ecotypes

Of 974 species with >=15 genomes, 190 (19.5%) form >=2 distinct AMR ecotypes. The clustering used uniform manifold approximation and projection (UMAP) plus DBSCAN on AMR Jaccard distances. [src: amr_strain_variation] The report finds distinct AMR subtypes in 19.5% of species. [src: amr_strain_variation] It calls this consistent with the clinical versus community-associated dichotomy in Klebsiella pneumoniae (Holt et al. 2015), where distinct lineages have different AMR and virulence profiles tied to different niches. [src: amr_strain_variation] The median silhouette score is 0.620, which the report calls good cluster quality. [src: amr_strain_variation]

Case-study UMAP plots for K. pneumoniae, S. aureus and S. enterica show visible environmental structuring. [src: amr_strain_variation] The formal test is underpowered. 52.7% of genomes lack a classifiable isolation_source, and only 2 species met the criteria for chi-squared testing. [src: amr_strain_variation] The report cautions that this does not mean ecotypes are unrelated to environment. [src: amr_strain_variation] E. coli was excluded from the case studies because it exceeds the 500-genome computational cap. [src: amr_strain_variation]

### Temporal and environmental patterns

Temporal trends were a null result. Of 513 species with >=20 genomes spanning >=3 years (post-1990), none show significant trends in AMR gene count after Benjamini-Hochberg FDR correction. [src: amr_strain_variation] Slopes are roughly symmetric around zero, with 251 positive and 262 negative. [src: amr_strain_variation] The report suggests the null reflects sparse, noisy NCBI BioSample collection dates, not a true absence of trends. It cites well-documented expansions in S. aureus and K. pneumoniae. [src: amr_strain_variation] It attributes the null likely to incomplete date metadata, with only 70% of genomes having parseable dates. [src: amr_strain_variation]

Environment shows a consistent pattern. Under both a rule-based classifier approximating BacDive categories and an NCBI keyword classifier, host-associated species carry more AMR genes per genome than terrestrial or aquatic species (Kruskal-Wallis, p < 0.05). [src: amr_strain_variation] The NCBI classifier assigns environments to 91% of species (1,190/1,307). [src: amr_strain_variation] The BacDive approximation classifies 35% (459/1,307). [src: amr_strain_variation] Both agree in direction, with human-clinical isolates showing the highest AMR burden. [src: amr_strain_variation]

## Data and Methods

The report draws on the kbase_ke_pangenome tables gene, gene_genecluster_junction, genome, genome_ani and ncbi_env for genome-level AMR presence/absence, ANI distances and environmental metadata. [src: amr_strain_variation] Eligible species had >=10 genomes, >=5 AMR genes and >=1 non-core gene, giving 1,307 species. [src: amr_strain_variation]

## Caveats and Open Work

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

## Slots Into

- [[concepts/within-species-variation-of-antimicrobial-resistance-gene-content]]: 51.3% rare, 41.3% variable and 7.5% fixed occurrences. [src: amr_strain_variation]
- [[concepts/resistance-islands-and-co-occurrence-of-amr-genes]]: 1,517 islands with mean phi 0.827. [src: amr_strain_variation]
- [[concepts/amr-ecotypes-and-environmental-association]]: 190 of 974 species form ecotypes. [src: amr_strain_variation]
- [[concepts/phylogenetic-signal-of-gene-content-and-traits]]: 55.6% of species show significant Mantel signal. [src: amr_strain_variation]
- [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]]: acquired genes show stronger signal than core genes. [src: amr_strain_variation]
- [[concepts/pangenome-openness-and-its-correlates]]: weak negative correlation between variability and openness. [src: amr_strain_variation]
- [[concepts/sampling-bias-and-metadata-sparsity-in-amr-resistome-surveys]]: sparse metadata limits environment tests. [src: amr_strain_variation]
- [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance]]: host-associated species carry more AMR genes. [src: amr_strain_variation]
