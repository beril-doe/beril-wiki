---
type: "Summary"
description: "Summary of the project Metabolic Capability vs Metabolic Dependency."
doc_type: "short"
full_text: "sources/metabolic_capability_dependency__REPORT.md"
---
# Metabolic Capability vs Metabolic Dependency

This page summarises the project Metabolic Capability vs Metabolic Dependency. In 48 Fitness Browser organisms, 15.8% of genomically complete pathway-organism pairs were latent capabilities, meaning they showed no detectable fitness importance under the conditions tested. [src: metabolic_capability_dependency] Across 22 species clades, the latent fraction correlated positively with pangenome openness. Pathway-level conservation did not separate latent from active pathways. [src: metabolic_capability_dependency] The latent fraction depends on classification thresholds and on tested conditions. [src: metabolic_capability_dependency] The report also claims, to its knowledge, the first systematic quantification of the latent capability fraction across diverse bacterial species using genome-wide fitness data. [src: metabolic_capability_dependency]

## Key Findings

### Latent capabilities in the Fitness Browser

Genomic completeness is an imperfect proxy for functional importance: 15.8% of 1,695 pathway-organism pairs were latent. [src: metabolic_capability_dependency] Pathway fitness metrics covered 48 Fitness Browser organisms spanning proteobacteria, firmicutes and other phyla. [src: metabolic_capability_dependency] SEED subsystem annotations served as a proxy to map GapMind pathway members to Fitness Browser genes. [src: metabolic_capability_dependency] The report defines the latent capability fraction as the fraction of complete-but-fitness-neutral pathways. [src: metabolic_capability_dependency] The report classified pathways as follows:
- Active dependency: mean |t-score| > 2.0 OR >20% essential genes. [src: metabolic_capability_dependency]
- Latent capability: mean |t-score| < 1.0 AND <5% essential genes. [src: metabolic_capability_dependency]
- Intermediate: between the two thresholds. [src: metabolic_capability_dependency]

Of 1,695 pairs, 881 (51.9%) were active, 547 (32.3%) intermediate and 267 (15.8%) latent. [src: metabolic_capability_dependency] The latent fraction varied by organism from 0 to 31.6%, with mean 15.0%. It was highest in *Pseudomonas syringae* strains and [[entities/klebsiella-michiganensis|Klebsiella michiganensis]]. [src: metabolic_capability_dependency]

### Pathway category

Pathway category strongly predicted dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴). [src: metabolic_capability_dependency] Carbon source utilization pathways were 3.7× more likely to be latent than amino acid biosynthesis pathways (24.3% vs 6.5%). [src: metabolic_capability_dependency] The report interprets the difference as reflecting distinct selective pressures. [src: metabolic_capability_dependency] It predicts that organisms in nutrient-rich environments should disproportionately lose carbon-pathway genes over evolutionary time, while amino acid biosynthesis genes stay under stronger purifying selection. [src: metabolic_capability_dependency]

| Category | Active | Intermediate | Latent | Total |
|---|---|---|---|---|
| Amino acid biosynthesis | 467 (63.5%) | 220 (29.9%) | 48 (6.5%) | 735 [src: metabolic_capability_dependency] |
| Carbon source utilization | 355 (39.8%) | 320 (35.9%) | 217 (24.3%) | 892 [src: metabolic_capability_dependency] |
| Other | 59 (86.8%) | 7 (10.3%) | 2 (2.9%) | 68 [src: metabolic_capability_dependency] |

The report explains the amino acid result as follows: organisms cannot scavenge all amino acids from the environment in all tested growth conditions. [src: metabolic_capability_dependency] It also notes that the result is consistent with Ramoneda et al. (2023), who found amino acid auxotrophies widespread but concentrated in nutrient-rich environments such as host-associated ones. [src: metabolic_capability_dependency] According to the report, Ramoneda et al. mapped amino acid auxotrophies across >26,000 genomes using GapMind. [src: metabolic_capability_dependency] The report cites D'Souza et al. (2014) for a ~13% fitness benefit from biosynthetic gene loss when neighbours supply the metabolites. [src: metabolic_capability_dependency] It suggests that many genomically complete pathways in nutrient-rich environments may already be functionally neutral. [src: metabolic_capability_dependency]

### Black Queen tests

The pathway-level test did not support the hypothesis (H2a). Conservation, defined as the fraction of species genomes carrying a complete pathway, did not differ between latent and active pathways. [src: metabolic_capability_dependency] Here conservation_rate captures whether the pathway is complete in each genome in the species clade. [src: metabolic_capability_dependency]

| Class | n | Mean conservation | Median |
|---|---|---|---|
| Active dependency | 755 | 0.829 | 1.000 [src: metabolic_capability_dependency] |
| Intermediate | 508 | 0.907 | 1.000 [src: metabolic_capability_dependency] |
| Latent capability | 248 | 0.869 | 1.000 [src: metabolic_capability_dependency] |

Latent pathways had slightly higher mean conservation than active ones. The active > latent test gave Mann-Whitney U p = 0.94 and rank-biserial r = 0.052. [src: metabolic_capability_dependency] The report cites Schakel et al. (2025), who showed that cross-feeding-based gene loss requires spatial structuring and is not straightforwardly predicted by the fitness cost of gene retention alone. It presents this as consistent with why simple conservation-rate ratios do not discriminate latent from active pathways. [src: metabolic_capability_dependency]

The clade-level test (H2b) supported the framework. The report aggregated 41 organisms to 22 unique species clades, because strains of one clade share a single pangenome openness value. [src: metabolic_capability_dependency] Latent capability fraction correlated positively with [[entities/pangenome-openness|pangenome openness]] (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [src: metabolic_capability_dependency] The report reads this as clades with more fitness-neutral complete pathways having more dynamic, less-conserved pangenomes, consistent with [[entities/black-queen-hypothesis|Black Queen]] at the species level. [src: metabolic_capability_dependency] It suggests that the signal operates at the level of genome dynamics and community context rather than in per-pathway cross-genome conservation ratios. [src: metabolic_capability_dependency] The report cites Morris et al. (2012) as proposing selection-driven gene loss in Prochlorococcus and Pelagibacter. [src: metabolic_capability_dependency]

The report notes that this contrasts with D'Souza et al. (2014) and Morris et al. (2012), who demonstrated gene loss in experimental and natural populations respectively. [src: metabolic_capability_dependency] It suggests the discrepancy may arise because its analysis works at the species level across many taxa, while the Black Queen signal may be strongest within single evolving lineages or communities. [src: metabolic_capability_dependency]

Pangenome openness data came from `kbase_ke_pangenome.pangenome` for 7,334 species. [src: metabolic_capability_dependency] Among well-sampled pathogens (>2,500 genomes), [[entities/klebsiella-pneumoniae|Klebsiella pneumoniae]] was most open (99.05% open; 0.95% core genes). [src: metabolic_capability_dependency] [[entities/mycobacterium-tuberculosis|Mycobacterium tuberculosis]] was most closed (97.4% open; 2.6% core genes). [src: metabolic_capability_dependency]

### Within-species metabolic ecotypes

All 10 target species (≥50 genomes, ≥15 variable pathways) showed meaningful metabolic clustering, with all silhouette scores > 0.2. [src: metabolic_capability_dependency] The report takes this as showing that within-species metabolic pathway heterogeneity is a general feature, not an exception. [src: metabolic_capability_dependency] Scores ranged from 0.35 (PALSA-747 sp.) to 0.89 (*Salmonella enterica*), so ecotype boundaries differ in sharpness. [src: metabolic_capability_dependency]

| Species | Genomes | Clusters | Silhouette |
|---|---|---|---|
| *Salmonella enterica* | 11,396 | 6 | 0.894 [src: metabolic_capability_dependency] |
| *Stutzerimonas stutzeri* | 149 | 2 | 0.780 [src: metabolic_capability_dependency] |
| *Alteromonas macleodii* | 56 | 2 | 0.738 [src: metabolic_capability_dependency] |
| *Acetatifactor intestinalis* | 59 | 6 | 0.657 [src: metabolic_capability_dependency] |
| *Ruminococcus* E sp. | 53 | 2 | 0.609 [src: metabolic_capability_dependency] |
| *Phenylobacterium* sp. | 51 | 2 | 0.544 [src: metabolic_capability_dependency] |
| *Limivicinus* sp. | 50 | 2 | 0.528 [src: metabolic_capability_dependency] |
| *Pelagibacter* sp. | 79 | 2 | 0.430 [src: metabolic_capability_dependency] |
| *Prochlorococcus* A sp. | 74 | 2 | 0.429 [src: metabolic_capability_dependency] |
| PALSA-747 sp. | 51 | 2 | 0.349 [src: metabolic_capability_dependency] |

Metabolic clusters correlated with isolation environment in [[entities/salmonella-enterica|Salmonella enterica]] (χ²=1570.2, df=25, p<0.0001) and in *Phenylobacterium* sp. (χ²=12.2, df=1, p=0.0005). [src: metabolic_capability_dependency] In *Salmonella enterica* (silhouette=0.89, k=6), clusters strongly correlated with clinical, food, and environmental isolation sources. [src: metabolic_capability_dependency] The report relates this to the established epidemiological serovars of Salmonella and to Van Rossum et al. (2020), who highlighted strain-level metabolic differentiation in human microbiome species. [src: metabolic_capability_dependency]

Clusters did not correlate with environment in the marine organisms *Stutzerimonas* and *Alteromonas*. [src: metabolic_capability_dependency] Environment-cluster associations were non-significant in the marine organisms Stutzerimonas, Alteromonas, Pelagibacter, and Prochlorococcus. [src: metabolic_capability_dependency] The report offers three possible explanations: insufficient resolution of NCBI isolation-source metadata for marine isolates [src: metabolic_capability_dependency]; clusters that track depth or nutrient zone rather than discrete source categories [src: metabolic_capability_dependency]; and metabolic differences driven by gene-content differences that GapMind pathway annotations do not capture at the relevant resolution. [src: metabolic_capability_dependency] It cites Nowinski et al. (2023), who found that ecological divergence in marine bacteria is shaped by gene content and expression, a signal pathway-level clustering may partly miss. [src: metabolic_capability_dependency] It also cites Tschoeke et al. (2020), on the Prochlorococcus collective, and Nowinski et al. (2023) as describing marine metabolic ecotypes defined by gene-content differences. [src: metabolic_capability_dependency]

The most heterogeneous pathways across species were all amino acid biosynthesis pathways: valine/leucine (heterogeneity=0.60), tryptophan (0.51) and lysine/threonine (0.49). [src: metabolic_capability_dependency] The report interprets these as pathways where some populations retained biosynthetic independence and others lost it, consistent with Ramoneda et al. (2023) across 26,277 bacterial genomes. [src: metabolic_capability_dependency]

## Data and Methods

The report used `kbase_ke_pangenome` tables gapmind_pathways, pangenome and gtdb_metadata, for pathway completeness predictions (305M rows, 80 pathways, 293K genomes), pangenome openness and NCBI taxonomy for organism matching. [src: metabolic_capability_dependency] It used `kescience_fitnessbrowser` tables genefitness, gene and seedannotation, for gene-level fitness scores (48 organisms), essentiality inference and SEED subsystem proxies for pathway membership. [src: metabolic_capability_dependency]

## Caveats and Open Work

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

## Slots Into

- [[concepts/latent-metabolic-capability-versus-fitness-dependency]]: 15.8% of complete pathways were latent, and carbon pathways were most affected. [src: metabolic_capability_dependency]
- [[concepts/gene-loss-and-black-queen-hypothesis-tests]]: the pathway-level conservation test was null (p = 0.94), while the clade-level pangenome openness correlation was ρ = 0.69. [src: metabolic_capability_dependency]
- [[concepts/within-species-metabolic-ecotypes-from-pathway-variation]]: all 10 target species clustered, with silhouette scores from 0.349 to 0.894. [src: metabolic_capability_dependency]
- [[concepts/pangenome-openness-and-its-correlates]]: latent fraction correlated positively with pangenome openness across 22 clades. [src: metabolic_capability_dependency]
- [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]]: amino acid pathways were only 6.5% latent, yet they were the most heterogeneous pathways across species. [src: metabolic_capability_dependency]
