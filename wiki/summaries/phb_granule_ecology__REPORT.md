---
type: "Summary"
description: "Summary of the project Polyhydroxybutyrate Granule Formation Pathways — Distribution Across Clades and Environmental Selection."
doc_type: "short"
full_text: "sources/phb_granule_ecology__REPORT.md"
---
# Polyhydroxybutyrate Granule Formation Pathways — Distribution Across Clades and Environmental Selection

This page summarises the project Polyhydroxybutyrate Granule Formation Pathways — Distribution Across Clades and Environmental Selection. The report asks how polyhydroxybutyrate (PHB) synthesis genes are distributed across clades and whether environmental variability selects for them. PHB capacity is common (21.9% of 27,690 species carry phaC) but uneven across clades, with Pseudomonadota at 60.9% and several phyla at zero. [src: phb_granule_ecology] Enrichment in variable environments is strongly supported statistically (chi2 = 1,656.36) [src: phb_granule_ecology], and the report concludes it is independent of genome size. [src: phb_granule_ecology]

## Key Findings

### Prevalence and phylogenetic concentration

PHB capacity is widespread but uneven across clades. Across 27,690 GTDB species, 21.9% carry phaC, the polyhydroxyalkanoate (PHA) synthase and committed step of PHB biosynthesis. [src: phb_granule_ecology] 21.7% have a complete pathway (phaC + phaA/phaB). [src: phb_granule_ecology] The report reads this near-identity as meaning virtually all phaC carriers also have the upstream enzymes. [src: phb_granule_ecology] See [[concepts/phylogenetic-distribution-of-phb-synthesis-across-bacteria-and-archaea]].

Phylum prevalence varies widely:
- Pseudomonadota: 60.9% (4,544/7,456 species). [src: phb_granule_ecology]
- Myxococcota: 52.9% (83/157). [src: phb_granule_ecology]
- Thermoproteota: 27.9% (65/233). [src: phb_granule_ecology]
- Desulfobacterota: 21.9% (70/319). [src: phb_granule_ecology]
- Patescibacteria: near zero at 0.4% (4/981), which the report calls consistent with reduced genomes and limited metabolic capacity. [src: phb_granule_ecology]
- No PHB was found in Campylobacterota (0/271) [src: phb_granule_ecology], Gemmatimonadota (0/102) [src: phb_granule_ecology] or Marinisomatota (0/90). [src: phb_granule_ecology]

At order level, Azospirillales and Rhodospirillales have 100% phaC prevalence [src: phb_granule_ecology], and Sphingomonadales has 95.9%. [src: phb_granule_ecology] 117 orders fall below 10%. [src: phb_granule_ecology]

### Environmental selection (feast/famine hypothesis, H1a)

Hypothesis H1a was that PHB genes are enriched in temporally variable environments and depleted in stable or host-associated ones. The report finds strong support. PHB presence is associated with environmental variability category (chi2 = 1,656.36, p ~ 0, dof = 2). [src: phb_granule_ecology] By primary environment, phaC prevalence is:

| Environment | Species | phaC prevalence | Expected variability |
|---|---|---|---|
| Plant-associated | 625 | 44.0% | High [src: phb_granule_ecology] |
| Soil | 1,484 | 43.6% | High [src: phb_granule_ecology] |
| Freshwater | 3,263 | 25.5% | Moderate [src: phb_granule_ecology] |
| Sediment | 1,020 | 20.1% | Moderate [src: phb_granule_ecology] |
| Human associated | 1,237 | 11.1% | Low [src: phb_granule_ecology] |
| Human clinical | 2,472 | 7.4% | Low [src: phb_granule_ecology] |

See [[concepts/environmental-variability-and-storage-polymer-pathway-enrichment-feast-famine-hypothesis]].

### Niche breadth and the genome-size confounder

Niche breadth used 64-dimensional AlphaEarth environmental embeddings for 2,008 species with sufficient genome representation. [src: phb_granule_ecology] PHB-negative species (phaC absent) have median embedding variance 0.2472 (n = 1,477) [src: phb_granule_ecology], and the PHB-positive versus PHB-negative comparison gives Mann-Whitney U = 446,546, p = 1.88 x 10^-6. [src: phb_granule_ecology] Genome size is a confounder: genome size correlates with niche breadth (rho = 0.302, p = 1.5e-43). [src: phb_granule_ecology] After partial Spearman control for genome size, the association largely disappears (partial rho = -0.047, p = 0.037). That is a 56.3% reduction with a sign reversal from raw rho = 0.106, p = 1.77e-06. [src: phb_granule_ecology] The report notes that larger genomes encode more pathways generally. [src: phb_granule_ecology] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

The categorical environmental enrichment is a separate matter. Within genome-size quartiles, high-variability environments keep higher phaC prevalence than low-variability ones:
- Q1 (0.4–1.8 Mbp): 10.7% vs 2.5%, 4.4x, p = 1.18 x 10^-11. [src: phb_granule_ecology]
- Q2 (1.8–2.5 Mbp): 18.5% vs 4.0%, 4.6x, p = 3.25 x 10^-47. [src: phb_granule_ecology]
- Q4 (3.7–14.0 Mbp): 50.9% vs 37.4%, 1.4x, p = 3.21 x 10^-14. [src: phb_granule_ecology]

The report concludes that the environmental enrichment signal is independent of genome size. [src: phb_granule_ecology]

### Subclade enrichment

The subclade analysis classified 41 families as enriched [src: phb_granule_ecology] and 62 as depleted. [src: phb_granule_ecology] Enriched families are concentrated in Pseudomonadota, including Burkholderiaceae, Rhodocyclaceae, Caulobacteraceae and Sphingomonadaceae. [src: phb_granule_ecology] They also appear in Actinomycetota (Mycobacteriaceae, Nocardioidaceae) [src: phb_granule_ecology], Thermoproteota (Nitrosopumilaceae) [src: phb_granule_ecology] and Cyanobacteriota (Microcystaceae). [src: phb_granule_ecology] Enriched families skew toward freshwater (5/41) and wastewater (3/41). [src: phb_granule_ecology] Depleted families skew toward marine (18/62) and host-associated (12/62) environments. [src: phb_granule_ecology]

### Horizontal transfer

The report flags 311 potential phaC acquisition events, in species of families with <20% phaC prevalence. [src: phb_granule_ecology] It also flags 278 potential loss events, in species lacking phaC in families with >80% prevalence. [src: phb_granule_ecology] Families with putative acquisitions:
- Lachnospiraceae: 38 acquisitions, family prevalence 3.1%. [src: phb_granule_ecology]
- Chitinophagaceae: 22, 12.4%. [src: phb_granule_ecology]
- Pelagibacteraceae: 13, 5.3%. [src: phb_granule_ecology]
- Planococcaceae: 10, 12.8%. [src: phb_granule_ecology]

High accessory fractions suggest SAR324, Bacillota_A and Eremiobacterota are active recipients of phaC via horizontal gene transfer (HGT). [src: phb_granule_ecology] This is an inference, not a direct observation. See [[concepts/horizontal-transfer-of-storage-pathway-genes-inferred-from-pangenome-core-accessory-status]].

### Metagenomic cross-validation (NMDC)

The report mapped 3,014/3,492 (86.3%) NMDC taxon columns to GTDB genera with known PHB status. [src: phb_granule_ecology] It used two tiers: 2,336 columns via an NCBI taxid-to-GTDB genus bridge, and 678 more by direct genus matching. [src: phb_granule_ecology] NMDC PHB inference scores correlate with depth (rho = -0.119, p = 1.14 x 10^-21) [src: phb_granule_ecology], temperature (+0.088, p = 1.86 x 10^-12) [src: phb_granule_ecology], minimum depth (-0.055, p = 1.05 x 10^-5) [src: phb_granule_ecology] and pH (+0.049, p = 7.95 x 10^-5). [src: phb_granule_ecology] The report reads the depth result as consistent with feast/famine, since surface carbon inputs vary more. [src: phb_granule_ecology] It reads the temperature result as consistent with higher metabolic turnover in warmer environments. [src: phb_granule_ecology] These are interpretations. Genus-level cross-validation matched 693 genera, and PHB-high genera (>=50% phaC prevalence) were more abundant in NMDC than PHB-low genera (Mann-Whitney p = 8.41 x 10^-22). [src: phb_granule_ecology] Top PHB-high genera by NMDC abundance were Mycobacterium, Pseudomonas, Cupriavidus, Burkholderia and Methylobacterium, described as well-characterized PHB producers. [src: phb_granule_ecology] See [[concepts/metagenome-based-cross-validation-of-genomic-trait-predictions]].

## Key Findings: Finding 1: PHB pathways are widespread but phylogenetically concentrated

This part of the report shows that PHB (polyhydroxybutyrate) pathways are common but concentrated in particular clades and environments. The environmental signal holds after genome-size stratification, but the niche-breadth association does not. [src: phb_granule_ecology]

### Overall prevalence

Across 27,690 [[entities/gtdb|GTDB]] species, 21.9% carry phaC (PHA synthase, the committed step for PHB biosynthesis). 21.7% have a complete PHB pathway (phaC + phaA/phaB). [src: phb_granule_ecology] The report reads this near-identical pair as showing that virtually all phaC-carrying species also have the upstream biosynthetic enzymes. [src: phb_granule_ecology] Using eggNOG annotations, it found 118,513 PHB-related gene clusters across 19,496 species. [src: phb_granule_ecology]

The report says the large "precursors-only" category (46.5%) reflects pleiotropy. phaA (beta-ketothiolase, K00626) and phaB (acetoacetyl-CoA reductase, K00023) also take part in general fatty acid and thiolase metabolism. [src: phb_granule_ecology] phaR (K18080) was absent from all 27K species in the eggNOG annotations. The report suggests poor annotation coverage or misassignment. [src: phb_granule_ecology]

### Phylum and order level

PHB prevalence differs sharply among phyla:

| Phylum | Prevalence | Species |
|---|---|---|
| Pseudomonadota | 60.9% | 4,544/7,456 [src: phb_granule_ecology] |
| Myxococcota | 52.9% | 83/157 [src: phb_granule_ecology] |
| Halobacteriota | 34.4% | 89/259 [src: phb_granule_ecology] |
| Thermoproteota | 27.9% | 65/233 [src: phb_granule_ecology] |
| Desulfobacterota | 21.9% | 70/319 [src: phb_granule_ecology] |
| Actinomycetota | 18.5% | 587/3,172 [src: phb_granule_ecology] |
| Patescibacteria | 0.4% | 4/981 [src: phb_granule_ecology] |

The report describes the near-zero Patescibacteria value as consistent with reduced genomes and limited metabolic capacity. [src: phb_granule_ecology] Four phyla had no PHB at all: Campylobacterota (0/271), Gemmatimonadota (0/102), Nanoarchaeota (0/135) and Marinisomatota (0/90). [src: phb_granule_ecology]

At order level, 23 orders with >20 species exceed 50% phaC prevalence. [src: phb_granule_ecology] The leaders are Azospirillales and Rhodospirillales (both 100%), Caulobacterales (99.3%) and Sphingomonadales (95.9%). [src: phb_granule_ecology] In contrast, 117 orders fall below 10%. [src: phb_granule_ecology]

### Environmental enrichment

phaC prevalence varies with primary environment across 27,690 species with classified primary environments. [src: phb_granule_ecology] Each environment was assigned an expected variability category, and prevalence tracks that category:

| Environment | Species | phaC prevalence | Expected variability |
|---|---|---|---|
| Plant-associated | 625 | 44.0% | High [src: phb_granule_ecology] |
| Soil | 1,484 | 43.6% | High [src: phb_granule_ecology] |
| Wastewater/engineered | 1,124 | 34.5% | High [src: phb_granule_ecology] |
| Freshwater | 3,263 | 25.5% | Moderate [src: phb_granule_ecology] |
| Sediment | 1,020 | 20.1% | Moderate [src: phb_granule_ecology] |
| Marine | 3,010 | 18.7% | Low [src: phb_granule_ecology] |
| Human associated | 1,237 | 11.1% | Low [src: phb_granule_ecology] |
| Human clinical | 2,472 | 7.4% | Low [src: phb_granule_ecology] |
| Animal associated | 3,711 | 3.3% | Low [src: phb_granule_ecology] |

PHB presence is associated with variability category (chi2 = 1,656.36, p ~ 0, dof = 2). The report says this strongly supports H1a: PHB pathway genes are enriched in clades from temporally variable "feast/famine" environments and depleted in stable or host-associated ones. [src: phb_granule_ecology]

### Niche breadth and the genome-size confound

The niche-breadth analysis uses [[entities/alphaearth-environmental-embeddings|AlphaEarth environmental embeddings]], 64-dimensional vectors capturing environmental context, for 2,008 species with sufficient genome representation. [src: phb_granule_ecology] PHB-positive species (phaC present) have median embedding variance 0.3295 (n = 531). PHB-negative species (phaC absent) have 0.2472 (n = 1,477). The Mann-Whitney U is 446,546, p = 1.88 x 10^-6. [src: phb_granule_ecology]

Genome size confounds this result, so H1b does not stand on its own. PHB-positive species have larger genomes (median 4.34 Mbp vs 2.44 Mbp, rank-biserial r = -0.592, p ~ 0). Genome size itself correlates with niche breadth (rho = 0.302, p = 1.5e-43). [src: phb_granule_ecology] After partial Spearman control for genome size, the association largely disappears. Partial rho is -0.047 (p = 0.037), a 56.3% reduction in effect size with a sign reversal from the raw rho = 0.106 (p = 1.77e-06). [src: phb_granule_ecology] The report concludes that H1b is substantially confounded by genome size and cannot be independent evidence for the feast/famine hypothesis. [src: phb_granule_ecology] It notes that larger genomes encode more metabolic pathways generally, and PHB is one of many enriched in larger-genome species. [src: phb_granule_ecology]

### Environmental signal within genome-size quartiles

The environmental signal survives stratification by genome size. In every quartile, phaC prevalence is higher in high-variability than in low-variability environments. [src: phb_granule_ecology]

| Quartile (Mbp) | High variability | Low variability | Enrichment | p |
|---|---|---|---|---|
| Q1, 0.4 – 1.8 | 10.7% | 2.5% | 4.4x | 1.18 x 10^-11 [src: phb_granule_ecology] |
| Q2, 1.8 – 2.5 | 18.5% | 4.0% | 4.6x | 3.25 x 10^-47 [src: phb_granule_ecology] |
| Q3, 2.5 – 3.7 | 34.3% | 10.9% | 3.1x | 4.17 x 10^-70 [src: phb_granule_ecology] |
| Q4, 3.7 – 14.0 | 50.9% | 37.4% | 1.4x | 3.21 x 10^-14 [src: phb_granule_ecology] |

The report concludes that the environmental enrichment signal is independent of genome size. [src: phb_granule_ecology]

## Key Findings: Finding 6: NMDC metagenomic cross-validation supports pangenome PHB …

Family-level tests found 41 enriched, 62 depleted and 145 non-significant families among 248 tested. [src: phb_granule_ecology] Enriched families are concentrated in Pseudomonadota but also occur in five other phyla. [src: phb_granule_ecology] Inferred phaC transfer rests on discordance between species and family prevalence, with 311 potential acquisitions and 278 potential losses. [src: phb_granule_ecology] The report treats a higher accessory-genome rate among the discordant species as strong support for horizontal acquisition. [src: phb_granule_ecology] A genus-level check against NMDC metagenomes gave stronger support than the weak abiotic correlations did. [src: phb_granule_ecology]

### Family-level enrichment

Of 248 families tested (Fisher's exact test, Bonferroni-corrected at alpha = 0.05), 41 were enriched, 62 were depleted and 145 were not significant. [src: phb_granule_ecology] Enriched families are concentrated in Pseudomonadota: Burkholderiaceae, Burkholderiaceae_B, Rhodocyclaceae, Caulobacteraceae, Sphingomonadaceae, Xanthobacteraceae, Rhodanobacteraceae and Legionellaceae. [src: phb_granule_ecology] They also appear in other phyla:
- Actinomycetota: Mycobacteriaceae and Nocardioidaceae. [src: phb_granule_ecology]
- Halobacteriota: Haloarculaceae and Natrialbaceae. [src: phb_granule_ecology]
- Thermoproteota: Nitrosopumilaceae. [src: phb_granule_ecology]
- Cyanobacteriota: Microcystaceae. [src: phb_granule_ecology]
- Bacillota: Bacillaceae_G. [src: phb_granule_ecology]

Enriched families skew toward freshwater (5/41) and wastewater (3/41). [src: phb_granule_ecology] Depleted families skew toward marine (18/62) and host-associated (12/62) environments. [src: phb_granule_ecology] The "other_unknown" category dominates (30/41 enriched, 26/62 depleted) because species environmental metadata are sparse, so these environmental readings are limited. [src: phb_granule_ecology]

### Inferred horizontal gene transfer of phaC

The report flagged 311 potential acquisition events, meaning species that carry phaC in families with <20% phaC prevalence. [src: phb_granule_ecology] It also flagged 278 potential loss events, meaning species that lack phaC in families with >80% prevalence. [src: phb_granule_ecology] Among the 311 discordant phaC-positive species, 60.1% carry phaC as accessory genome, against 32.3% across all phaC-carrying species. The report reads this as strong support for horizontal acquisition. [src: phb_granule_ecology] Overall, 5,371 species carry core phaC and 1,959 carry accessory phaC, and some species carry both. [src: phb_granule_ecology]

Families with the most putative acquisitions:

| Family | Putative acquisitions | Family phaC prevalence |
|---|---|---|
| Lachnospiraceae | 38 | 3.1% [src: phb_granule_ecology] |
| Chitinophagaceae | 22 | 12.4% [src: phb_granule_ecology] |
| Pelagibacteraceae | 13 | 5.3% [src: phb_granule_ecology] |
| Enterobacteriaceae | 11 | 2.3% [src: phb_granule_ecology] |
| Planococcaceae | 10 | 12.8% [src: phb_granule_ecology] |

High accessory fractions in SAR324, Bacillota_A and Eremiobacterota suggest, as an interpretation, that these lineages are active recipients of phaC through HGT (horizontal gene transfer). [src: phb_granule_ecology]

### NMDC metagenome cross-validation

The report mapped 3,014/3,492 (86.3%) NMDC taxon columns to GTDB genera with known PHB status. [src: phb_granule_ecology] Tier 1 used a gtdb_metadata NCBI taxid-to-GTDB-genus bridge for 2,336 columns. Tier 2 used direct genus matching through taxonomy_dim for 678 more columns. [src: phb_granule_ecology] Per-sample PHB inference scores for 6,365 NMDC samples were abundance-weighted sums of genus-level phaC prevalence. A median 87.2% of abundance matched pangenome genera. [src: phb_granule_ecology]

The scores correlated weakly with abiotic variables (Spearman rho):

| Variable | rho | p |
|---|---|---|
| Depth | -0.119 | 1.14 x 10^-21 [src: phb_granule_ecology] |
| Temperature | +0.088 | 1.86 x 10^-12 [src: phb_granule_ecology] |
| Maximum depth | +0.076 | 1.15 x 10^-9 [src: phb_granule_ecology] |
| Minimum depth | -0.055 | 1.05 x 10^-5 [src: phb_granule_ecology] |
| pH | +0.049 | 7.95 x 10^-5 [src: phb_granule_ecology] |
| Ammonium nitrogen | +0.044 | 4.49 x 10^-4 [src: phb_granule_ecology] |

The report reads the negative depth correlation as consistent with the feast/famine hypothesis. On that reading, surface environments have more variable carbon inputs. [src: phb_granule_ecology] It reads the positive temperature correlation as consistent with higher metabolic turnover in warmer environments. [src: phb_granule_ecology] Effect sizes are modest (|rho| < 0.12). The report suggests this is because NMDC abiotic measurements are point-in-time snapshots, not measures of temporal variability. [src: phb_granule_ecology]

A genus-level cross-validation gave stronger support. It matched 693 genera between pangenomes and NMDC. PHB-high genera (>=50% phaC prevalence) had higher NMDC abundance than PHB-low genera (Mann-Whitney p = 8.41 x 10^-22). [src: phb_granule_ecology] The top PHB-high genera by NMDC abundance were Mycobacterium, Pseudomonas, Cupriavidus, Burkholderia and Methylobacterium, which the report describes as well-characterized PHB producers. [src: phb_granule_ecology]

### Limitation: PHA synthase classes

The PHA (polyhydroxyalkanoate) synthase class analysis assigned all 11,792 phaC clusters to "other_pfam". eggNOG supplied domain names (Abhydrolase_1, PhaC_N) instead of the Pfam accession IDs (PF00561, PF07167) that the code expected. The report says this remains a limitation. [src: phb_granule_ecology]

## Results: PHB Gene Discovery (NB01)

This part of the report searched the KBase Data Lakehouse pangenome annotations for PHB pathway genes, classified species by pathway completeness, and tested whether PHB prevalence tracks environmental variability. Five of six pathway KOs were detected. The environmental enrichment held within genome-size quartiles, but the niche-breadth association did not survive control for genome size. [src: phb_granule_ecology]

### Gene detection

Querying pangenome eggNOG annotations for six PHB pathway KEGG orthologs (KOs) found 118,513 gene clusters across 19,496 species. [src: phb_granule_ecology] Counts per gene:

| Gene | KO | Clusters | Species | Role |
|---|---|---|---|---|
| phaA | K00626 | 86,318 | 17,969 | beta-ketothiolase (pleiotropic) [src: phb_granule_ecology] |
| phaC | K03821 | 11,792 | 6,067 | PHA synthase, committed step [src: phb_granule_ecology] |
| phaB | K00023 | 9,617 | 6,977 | acetoacetyl-CoA reductase (pleiotropic) [src: phb_granule_ecology] |
| phaP | K14205 | 6,130 | 4,571 | phasin granule protein [src: phb_granule_ecology] |
| phaZ | K05973 | 4,656 | 3,151 | PHB depolymerase [src: phb_granule_ecology] |
| phaR | K18080 | 0 | 0 | transcriptional regulator [src: phb_granule_ecology] |

The report suggests that the missing phaR (5 of 6 KOs detected) may reflect K18080 being underrepresented in eggNOG annotations. [src: phb_granule_ecology]

### Pathway completeness

Species were classed by pathway completeness: 6,005 complete (phaC plus phaA/phaB) [src: phb_granule_ecology], 62 synthase-only [src: phb_granule_ecology], 12,869 precursors-only (phaA/phaB without phaC) [src: phb_granule_ecology], 555 accessory-only (phaP/phaZ/phaR without synthase) [src: phb_granule_ecology] and 8,199 with the pathway absent. [src: phb_granule_ecology]

### Taxonomic distribution

The 6,067 phaC-carrying species span 95 of 142 GTDB phyla but concentrate in a few lineages. [src: phb_granule_ecology] Pseudomonadota holds 74.9% of them (4,544/6,067), driven by high prevalence across Alpha- and Gammaproteobacteria orders. [src: phb_granule_ecology] Five phyla (Pseudomonadota, Myxococcota, Halobacteriota, Thermoproteota, Desulfobacterota) hold 85.5% of phaC-positive species but make up 30.4% of total species diversity. [src: phb_granule_ecology]

Within Pseudomonadota (60.9% overall prevalence), Azospirillales and Rhodospirillales reach 100%, and several orders fall below 10%. [src: phb_granule_ecology] Within-phylum Fisher's exact tests on 248 families with at least 10 species found 41 enriched and 62 depleted families after Bonferroni correction. [src: phb_granule_ecology]

### Environmental selection

Environment metadata covered 293,050 genomes spanning all 27,690 species. [src: phb_granule_ecology] The report harmonized NCBI isolation_source, env_broad_scale, env_local_scale and host fields into 11 categories. [src: phb_granule_ecology] PHB prevalence was more than 10-fold higher in high-variability environments (plant 44%, soil 43.6%) than in low-variability ones (clinical 7.4%, animal 3.3%), with chi2 = 1,656.36 and p ~ 0. [src: phb_granule_ecology]

AlphaEarth embeddings gave an independent niche-breadth measure for 2,008 species with at least 5 embedded genomes each. [src: phb_granule_ecology] Embedding variance captures within-species variation in environmental context and serves as a niche-breadth proxy. [src: phb_granule_ecology] PHB-positive and PHB-negative species differed in niche breadth (Mann-Whitney p = 1.88e-06), and the difference persisted when restricted to phyla containing both groups. [src: phb_granule_ecology]

### Genome-size confound

This confound limits the niche-breadth result. PHB-positive species have larger genomes than PHB-negative ones (median 4.34 Mbp vs 2.44 Mbp, rank-biserial r = -0.592). [src: phb_granule_ecology] Genome size correlates with niche breadth (rho = 0.302, p = 1.5e-43). [src: phb_granule_ecology] Controlling for it changed the PHB–niche breadth Spearman association from rho = 0.106 (p = 1.77e-06) to rho = -0.047 (p = 0.037). That is a 56.3% reduction with sign reversal, so genome size is the primary driver of the apparent association. [src: phb_granule_ecology]

The environmental enrichment is more robust. PHB stayed enriched in high-variability environments across all four genome-size quartiles (fold enrichment 1.4–4.6x, all p < 1e-11). The report reads this as environmental selection independent of genome size. [src: phb_granule_ecology]

### Horizontal transfer

The pangenome analysis calls a gene cluster core if it is present in more than 90% of genomes within a species, and accessory otherwise. [src: phb_granule_ecology] The report interprets the higher phaC accessory rate in phylogenetically discordant species (60.1% vs 32.3%) as pangenome-scale evidence for ongoing horizontal transfer, consistent with earlier single-species case studies. [src: phb_granule_ecology]

## Interpretation: The Feast/Famine Hypothesis at Pangenome Scale

This part of the report reads its pangenome-scale PHB (polyhydroxybutyrate) patterns against the feast/famine hypothesis and earlier literature. The report says its data strongly support the hypothesis. The main caveat is that genome size confounds the niche-breadth result, while the environmental enrichment survives genome-size stratification. [src: phb_granule_ecology]

### The hypothesis and the environmental gradient

The classical feast/famine hypothesis (Dawes & Senior 1973) proposes that PHB is most advantageous under temporal carbon fluctuation. [src: phb_granule_ecology] The report calls its analysis across 27,690 species the first pan-bacterial genomic test of this hypothesis. [src: phb_granule_ecology] PHB prevalence falls along an environmental gradient from high-variability to low-variability environments. [src: phb_granule_ecology]

| Environment | PHB prevalence |
|---|---|
| Plant | 44% [src: phb_granule_ecology] |
| Soil | 43.6% [src: phb_granule_ecology] |
| Wastewater | 34.5% [src: phb_granule_ecology] |
| Marine | 18.7% [src: phb_granule_ecology] |
| Clinical | 7.4% [src: phb_granule_ecology] |
| Animal | 3.3% [src: phb_granule_ecology] |

PHB-enriched families skew toward freshwater/wastewater environments. Depleted families skew toward marine/host-associated environments. [src: phb_granule_ecology] The NMDC (National Microbiome Data Collaborative) cross-validation points the same way. Inferred PHB capacity correlates negatively with sample depth (rho = -0.12, p = 1.1e-21) and positively with temperature (rho = 0.09, p = 1.9e-12). The report reads this as consistent with higher PHB prevalence in shallower, warmer environments with more dynamic carbon cycling. [src: phb_granule_ecology]

### Genome size as a confounder

The niche-breadth result is confounded by genome size, but the environmental enrichment is not. PHB-positive species appear to occupy broader environmental niches in the unadjusted analysis (raw p = 1.88e-06). [src: phb_granule_ecology] That association is largely explained by genome size, with partial rho = -0.047 after controlling for it. [src: phb_granule_ecology] The report gives the raw rho as 0.106, so the association collapses after the control. [src: phb_granule_ecology] Niche breadth, measured by AlphaEarth embedding variance, scales with genome size (rho = 0.302). [src: phb_granule_ecology] The report therefore names genome size, not PHB specifically, as the primary correlate of niche breadth. [src: phb_granule_ecology]

The report cites Vieira-Silva & Rocha 2010 for a linear scaling of genome size with metabolic enzyme count (r > 0.9). It cites Barberán et al. 2014 for genome size predicting habitat breadth in soil bacteria. [src: phb_granule_ecology] It cites Bentkowski et al. 2015 for fluctuating environments selecting larger genomes. It cites Giovannoni et al. 2005, 2014 for stable oligotrophic environments selecting streamlined genomes that shed optional pathways, including PHB, glycogen and polyphosphate storage. [src: phb_granule_ecology] From this the report proposes a causal chain: environment variability → genome size → metabolic pathway count → PHB presence. In this chain PHB presence is partly a downstream consequence of genome size, not an independent adaptation. [src: phb_granule_ecology]

The environmental enrichment, which the report calls the more direct test of the hypothesis, holds across all four genome size quartiles with 1.4–4.6x enrichment. [src: phb_granule_ecology] In those quartiles all p < 1e-11. The report interprets this as environmental selection for PHB acting above and beyond the general genome-size effect. It says this supports feast/famine as a specific selective force, not a mere consequence of metabolic versatility. [src: phb_granule_ecology] The report presents this as genomic evidence that environmental variability has been a major selective driver of PHB pathway maintenance and acquisition. It extends the framework from individual-species experiments, such as *Cupriavidus necator* competition experiments. [src: phb_granule_ecology]

### Relation to earlier literature

**Census and environment.** Anderson & Dawes (1990) catalogued PHB occurrence qualitatively across bacterial genera. [src: phb_granule_ecology] The report extends this to a quantitative census of 27,690 species with 21.9% phaC prevalence. [src: phb_granule_ecology] Mason-Jones et al. (2023) demonstrated that intracellular carbon storage, including PHB, in soil is a significant carbon pool (0.19-0.46x extractable microbial biomass). [src: phb_granule_ecology] Viljakainen & Hug (2021) mapped PHA (polyhydroxyalkanoate) depolymerase genes across 3,078 metagenomes. They found the highest frequency in wastewater and the lowest in marine environments. [src: phb_granule_ecology] The report states that its synthesis-gene analysis shows the same gradient from the production side. [src: phb_granule_ecology]

**Stress protection and generalism.** Obruca et al. (2018, 2020) and Muller-Santos et al. (2021) documented PHB-mediated resistance to UV, osmotic, oxidative, temperature and freezing stresses, beyond carbon storage. [src: phb_granule_ecology] The report proposes that PHB may enable broader niche occupation through general stress protection, not just carbon buffering. [src: phb_granule_ecology] This is a proposed explanation. It rests on the niche-breadth association, which the genome-size control largely removed. [src: phb_granule_ecology] Gibbons et al. (2021) showed that metabolically flexible habitat generalists dominate frequently disturbed ecosystems. [src: phb_granule_ecology] The report suggests PHB may contribute to the metabolic flexibility that enables environmental generalism. [src: phb_granule_ecology]

**Lineage specificity and horizontal transfer.** Pieja et al. (2011) found all Type II methanotrophs PHB-positive and all Type I negative. [src: phb_granule_ecology] Kalia et al. (2007) and Catone et al. (2014) documented phaC horizontal gene transfer (HGT) in individual species. [src: phb_granule_ecology] The report identifies 311 potential phaC acquisition events with a 60.1% accessory rate versus 32.3% overall. It describes this as the first systematic quantification of phaC HGT frequency. [src: phb_granule_ecology] Cai et al. (2011) showed distinct HGT patterns for different PHA pathway genes in *Halomonas*. [src: phb_granule_ecology] The report finds extensive HGT across Lachnospiraceae, Chitinophagaceae, Pelagibacteraceae and Enterobacteriaceae. It interprets this as a widespread phenomenon. [src: phb_granule_ecology]

**Archaea and methods.** Han et al. (2010) identified PHA synthase diversity in haloarchaea. [src: phb_granule_ecology] The report finds 34.4% phaC prevalence in Halobacteriota, which it says quantifies the scale of archaeal PHA capacity. [src: phb_granule_ecology] The report applies the GTDB-based functional trait mapping of Mendler et al. (2019, AnnoTree) and the pangenome core/accessory analysis of Szabo et al. (2023) to PHB. [src: phb_granule_ecology]

## Interpretation; Data

This part of the report interprets the survey as a pangenome-scale analysis of PHB (polyhydroxybutyrate) pathways. It then lists the report's stated limits and the data tables it used. The report claims novelty and a feast/famine signal in the environmental gradient. [src: phb_granule_ecology]

### Interpretation: what the report claims

The report calls this the first comprehensive pangenome-scale survey of PHB pathway distribution across the bacterial tree of life. It covers 27,690 species from the KBase Data Lakehouse pangenome and integrates phylogeny, environmental ecology, niche breadth and horizontal gene transfer (HGT). [src: phb_granule_ecology] It says prior work was qualitative, limited to single clades, focused on degradation rather than synthesis, or confined to single-species HGT case studies. [src: phb_granule_ecology]

The report draws these main points:
- **Prevalence.** 21.9% of all bacterial species carry phaC. The report calls this the first precise estimate across the full tree. [src: phb_granule_ecology]
- **Environmental gradient.** PHB prevalence differs more than 10-fold between plant (44%) and animal (3.3%) environments. The report reads this as genomic evidence for the feast/famine hypothesis at evolutionary timescales. [src: phb_granule_ecology]
- **Genome size.** PHB+ species have genomes 1.9 Mbp larger on average. [src: phb_granule_ecology] The median is 4.34 Mbp for PHB+ and 2.44 Mbp for PHB-. [src: phb_granule_ecology] Genome size largely explains the PHB–niche breadth association (H1b). The report calls that association largely an artefact, with a 56.3% effect reduction after controlling. [src: phb_granule_ecology]
- **Environmental enrichment.** Enrichment (H1a) holds within all genome size quartiles. The report takes this to show that feast/famine selection operates independently of genome size. [src: phb_granule_ecology]
- **HGT.** The report identifies 311 putative phaC acquisition events with elevated accessory rates (60.1%). It calls this the first systematic pan-bacterial quantification of ongoing phaC transfer. [src: phb_granule_ecology]

The report supports the feast/famine hypothesis but does not regard it as necessarily the sole driver. [src: phb_granule_ecology] It notes that PHB serves functions beyond carbon storage, including stress resistance, redox balance and cryoprotection. [src: phb_granule_ecology] It also notes that phaA and phaB participate in general metabolism beyond PHB. [src: phb_granule_ecology]

### Limits stated by the report

**Cross-validation and environment data**
- The NMDC metagenomic cross-validation (H1c) gave statistically significant but small abiotic correlations (|rho| < 0.12). [src: phb_granule_ecology]
- NMDC abiotic measurements are point-in-time values, not measures of temporal variability. This limits direct tests of feast/famine. [src: phb_granule_ecology]
- NMDC studies are biased toward terrestrial/soil environments. [src: phb_granule_ecology]
- 34.9% of species have "other_unknown" as primary environment, so the enrichment results may underestimate the true signal. [src: phb_granule_ecology]

**Failed analysis**
- The PHA (polyhydroxyalkanoate) synthase class analysis failed. All phaC clusters were classified as "other_pfam" because eggNOG PFAMs use domain names rather than accession IDs. [src: phb_granule_ecology]
- The report proposes mapping PF00561 to Abhydrolase_1 and PF07167 to PhaC_N to enable Class I-IV classification. [src: phb_granule_ecology]

**Coverage and bias**
- Only 28% of genomes (83K/293K) have AlphaEarth embeddings. This may skew the niche breadth analysis toward better-sampled lineages. [src: phb_granule_ecology]
- The 2,008 species analysed represent 7.2% of total species diversity. [src: phb_granule_ecology]
- The "precursors_only" category (46.5% of species) likely overestimates partial PHB capability. [src: phb_granule_ecology]
- The pangenome includes both complete genomes and metagenome assembled genomes (MAGs), which may have variable gene detection rates. [src: phb_granule_ecology]

**Phylogeny**
- H1a enrichment is robust to genome size stratification. The report says phylogenetic logistic regression or other phylogenetically controlled analyses would strengthen it by accounting for shared ancestry. [src: phb_granule_ecology]

### Data

The report draws on two data sources.

**kbase_ke_pangenome**
- The tables eggnog_mapper_annotations, gene_cluster, gtdb_species_clade, pangenome, genome, ncbi_env and alphaearth_embeddings_all_years supplied PHB gene identification, taxonomy, environment metadata and environmental embeddings. [src: phb_granule_ecology]
- gtdb_metadata bridged NCBI taxid to GTDB genus for NMDC cross-validation. [src: phb_granule_ecology]

**nmdc_arkin**
- The tables study_table, abiotic_features, taxonomy_features, taxonomy_dim, kegg_ko_terms, metabolomics_gold, trait_features and embedding_metadata supported PHB inference from taxonomic composition and abiotic correlations. [src: phb_granule_ecology]

The report's output tables, with row counts:

| Table | Rows | Content |
|---|---|---|
| phb_gene_clusters.tsv | 118,513 | All PHB-related gene clusters with KEGG KO (KEGG ortholog), species, core/accessory status [src: phb_granule_ecology] |
| phb_species_summary.tsv | 19,496 | Species-level PHB pathway status (complete/partial/absent) [src: phb_granule_ecology] |
| phb_by_taxonomy.tsv | 27,690 | All species with taxonomy and PHB status [src: phb_granule_ecology] |
| phb_by_order.tsv | 1,058 | PHB prevalence by taxonomic order [src: phb_granule_ecology] |
| species_environment.tsv | 27,690 | Primary environment classification and PHB status [src: phb_granule_ecology] |
| phb_embedding_analysis.tsv | 2,008 | AlphaEarth embedding variance, genome size, PHB status [src: phb_granule_ecology] |
| species_genome_size.tsv | 27,690 | Genome size (Mbp), protein count, PHB status [src: phb_granule_ecology] |
| subclade_enrichment.tsv | 248 | Family-level Fisher's exact test results (enriched/depleted/ns) [src: phb_granule_ecology] |
| phaC_class_distribution.tsv | 6,067 | phaC-carrying species with attempted class (all "other_pfam") [src: phb_granule_ecology] |
| nmdc_phb_prevalence.tsv | 6,365 | NMDC sample PHB inference scores (mean=201.5, median=137.7, 87.2% median coverage) [src: phb_granule_ecology] |
| nmdc_abiotic_correlations.tsv | 21 | Spearman correlations of PHB score with abiotic variables (6 significant at p<0.001) [src: phb_granule_ecology] |
| pangenome_vs_metagenome.tsv | 693 | Genus-level pangenome phaC prevalence vs NMDC mean abundance [src: phb_granule_ecology] |

## Supporting Evidence; Future Directions

This part of the report lists the notebooks behind the analyses and the follow-up work the authors propose. The proposals are plans, not results. They aim at gaps in PHA synthase classification, phylogenetic control, horizontal gene transfer (HGT) inference, fitness evidence, environmental embeddings and NMDC environment labels. [src: phb_granule_ecology]

### Future directions: classification and phylogenetic control

The report proposes fixing the PHA (polyhydroxyalkanoate) synthase class analysis. This means mapping Pfam accession IDs to eggNOG domain names: PF00561 to Abhydrolase_1 for Class I/II, and PF07167 to PhaC_N for Class III/IV. That would allow proper classification of the 11,792 phaC clusters. [src: phb_granule_ecology] A Pfam naming issue in the subclade enrichment notebook is the reason this fix is needed. [src: phb_granule_ecology]

The report proposes phylogenetic logistic regression or phylogenetic independent contrasts. These would separate environmental selection from phylogenetic inertia in the distribution of PHB (polyhydroxybutyrate). [src: phb_granule_ecology] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]] for the wider confounding problem.

The report also proposes reconstructing a phaC gene tree and comparing it with the species tree topology. This would identify incongruent HGT branches directly, instead of relying on a core/accessory proxy. [src: phb_granule_ecology] See [[concepts/horizontal-transfer-of-storage-pathway-genes-inferred-from-pangenome-core-accessory-status]].

### Future directions: fitness and environment

The report proposes querying the Fitness Browser in the KBase Data Lakehouse for phaC mutant fitness phenotypes. The test is whether phaC gives a measurable fitness advantage under carbon-variable conditions. [src: phb_granule_ecology]

For AlphaEarth embeddings, the report proposes using all 64 dimensions instead of variance alone. Dimensionality reduction would then map PHB+ and PHB- species in environmental space and show which environmental axes separate them. [src: phb_granule_ecology] See [[entities/alphaearth-environmental-embeddings]].

For NMDC samples, the report proposes using the study_table columns ecosystem, ecosystem_category, ecosystem_type, ecosystem_subtype and specific_ecosystem. It would also use the env_triads_flattened ENVO (Environment Ontology) terms. The goal is richer environmental classification. [src: phb_granule_ecology] See [[entities/nmdc-integrated-collections]].

### Supporting evidence: notebooks

The report ties its analyses to six notebooks.

- Notebook 01 identifies PHB gene clusters from eggNOG annotations and explores the NMDC schema. [src: phb_granule_ecology]
- Notebook 01b completes the NB01 cells that errored on the first run, covering NMDC metabolomics and environment metadata. [src: phb_granule_ecology]
- Notebook 02 maps PHB pathway completeness across GTDB taxonomy and calculates prevalence by phylum and order. [src: phb_granule_ecology]
- Notebook 03 correlates PHB with environment type and AlphaEarth embedding variance. It also runs a genome size confound analysis. [src: phb_granule_ecology]
- Notebook 04 cross-validates against NMDC metagenomes. It uses two-tier taxonomy mapping, PHB inference scores and abiotic correlations. [src: phb_granule_ecology]
- Notebook 05 runs family-level enrichment tests, HGT signal analysis, NMDC cross-validation and the PHA synthase class analysis, which has the Pfam naming issue. [src: phb_granule_ecology]

## Caveats and Open Work

- The "precursors-only" category (46.5%) reflects the pleiotropy of phaA (beta-ketothiolase, K00626) and phaB (acetoacetyl-CoA reductase, K00023). Both act in general fatty acid and thiolase metabolism beyond PHB synthesis. [src: phb_granule_ecology] See [[concepts/pathway-completeness-inference-from-ko-annotations-and-pleiotropic-enzymes]].
- phaR (K18080) was absent from all 27K species in the eggNOG annotations. This suggests poor annotation coverage or misassignment. [src: phb_granule_ecology]
- The raw niche-breadth association is largely explained by genome size. [src: phb_granule_ecology]
- The NMDC mapping covered 3,014/3,492 (86.3%) of taxon columns, so the rest were unmapped. [src: phb_granule_ecology]

## Slots Into

- [[concepts/phylogenetic-distribution-of-phb-synthesis-across-bacteria-and-archaea]]: phaC is found in 21.9% of 27,690 GTDB species and is concentrated in Pseudomonadota. [src: phb_granule_ecology]
- [[concepts/environmental-variability-and-storage-polymer-pathway-enrichment-feast-famine-hypothesis]]: chi-squared support for H1a, with enrichment persisting in genome-size quartiles. [src: phb_granule_ecology]
- [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]]: the niche-breadth correlation reverses sign after controlling for genome size. [src: phb_granule_ecology]
- [[concepts/pathway-completeness-inference-from-ko-annotations-and-pleiotropic-enzymes]]: pleiotropic phaA and phaB underlie the precursors-only category. [src: phb_granule_ecology]
- [[concepts/metagenome-based-cross-validation-of-genomic-trait-predictions]]: 693 genera matched, with higher NMDC abundance for PHB-high genera. [src: phb_granule_ecology]
- [[concepts/horizontal-transfer-of-storage-pathway-genes-inferred-from-pangenome-core-accessory-status]]: 311 putative phaC acquisitions and 278 putative losses. [src: phb_granule_ecology]
