---
type: "Summary"
description: "Summary of a KBase Data Lakehouse pangenome analysis of plant-growth-promoting gene co-occurrence, soil/rhizosphere enrichment, core/accessory status and tryptophan-pathway coupling to ipdC."
doc_type: "short"
full_text: "sources/pgp_pangenome_ecology__REPORT.md"
---
# PGP Gene Distribution Across Environments & Pangenomes

## Overview

This report analyzes plant-growth-promoting (PGP) gene distribution, co-occurrence, environmental enrichment, and core/accessory status across the KBase Data Lakehouse pangenome. Among 27,702 total species, 11,272 carried at least one of 13 PGP gene markers; the analysis included 32,736 PGP gene clusters, 27,690 species with GapMind tryptophan-completeness scores, and 291,279 genomes with isolation-source metadata. [src: pgp_pangenome_ecology]

## Key Findings

### PGP co-occurrence and ecological guilds

A symmetric co-occurrence heatmap in the report shows log2 odds ratios among the five focal PGP genes. Asterisks mark pairs significant at false-discovery-rate (FDR, the expected share of false positives among significant calls) q < 0.05. [src: pgp_pangenome_ecology]

Across 11,272 species with at least one PGP gene, eight of 10 focal-gene pairs were significantly associated after Benjamini–Hochberg FDR (BH-FDR) correction: five pairs showed positive co-occurrence and three showed negative co-occurrence. The strongest positive association was pqqC × acdS, with odds ratio (OR) = 7.24, n = 286 co-occurring species, and q = 1.2e-83. The report links the two markers to phosphate solubilization (PQQ cofactor biosynthesis) and ethylene reduction (ACC deaminase). It also says the two are "nearly always found together when either is present". That wording overstates the data: 286 co-occurring species is far fewer than the 3,028 pqqC-bearing species reported elsewhere. OR = 7.24 shows a positive association, not near-universal joint carriage. pqqC also co-occurred significantly with hcnC (OR = 1.91) and ipdC (OR = 1.55), forming a putative rhizosphere-effectiveness module. [src: pgp_pangenome_ecology]

nifH was negatively associated with hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19), and showed no significant association with ipdC (OR = 1.13, q = 0.54). These results support ecological separation between diazotrophs and pqqC/acdS-bearing rhizobacteria, with the classical PGPB suite appearing primarily non-diazotrophic in this dataset. [src: pgp_pangenome_ecology]

Only 157 species (1.4%) carried at least three focal traits. The report names pqqC + acdS (n = 153) as the most common multi-trait genotype, followed by nifH + pqqC (n = 225). This ranking is internally inconsistent because the second-ranked count is larger than the first, and the report does not resolve the discrepancy. nifH and pqqC were also negatively associated overall; the report says they nonetheless co-occur in some generalist lineages. A second, separate inconsistency concerns the pqqC–acdS count. The co-occurrence section gives n = 286 co-occurring species, but the trait-combination section gives pqqC + acdS as n = 153. The report does not explain the difference. A bar chart in the report shows the top 15 multi-trait combinations across species. [src: pgp_pangenome_ecology]

### Environmental enrichment

An environmental-enrichment figure in the report compares the prevalence of each PGP gene in soil/rhizosphere versus other environments and shows log2 odds ratios. [src: pgp_pangenome_ecology]

Comparing 1,039 soil/rhizosphere species with 10,233 species from other environments, three of five focal genes (acdS, pqqC, and hcnC) were significantly enriched in soil (BH-FDR q < 0.05). acdS prevalence was 15.8% in soil/rhizosphere species versus 2.6% in other species (OR = 7.02, q = 5.1e-62); pqqC prevalence was 43.8% versus 21.2% (OR = 2.90, q = 2.8e-53); and hcnC prevalence was 11.3% versus 6.4% (OR = 1.85, q = 6.1e-08). [src: pgp_pangenome_ecology]

nifH was depleted in soil-classified species, with prevalence of 12.9% in soil/rhizosphere species versus 19.7% in other species (OR = 0.60, q = 5.5e-08). ipdC was not significantly enriched in the raw comparison (soil prevalence 1.5%, other prevalence 1.9%, OR = 0.79, q = 0.47). [src: pgp_pangenome_ecology]

The acdS enrichment remained strong after phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61) and in a strict rhizosphere-only sensitivity analysis using genomes with “rhizosphere” or “root nodule” in their isolation source (OR = 10.6, q = 7.6e-38). Bacillota_A was an exception for nifH, showing enrichment in soil (OR = ∞, q = 2.5e-4). The report attributes this to soil-specific anaerobic diazotrophs such as clostridia. [src: pgp_pangenome_ecology]

The report attributes the overall soil depletion of nifH partly to database composition. In its account, most nitrogen fixers in the database are aquatic/marine (cyanobacteria, Azotobacter) or host-associated (rhizobia). This is an interpretation of sampling composition, not a separately tested result. [src: pgp_pangenome_ecology]

### Core, accessory, and singleton status

A report figure shows the core, auxiliary and singleton fractions for each PGP gene against a genome-wide baseline of 46.8% core. [src: pgp_pangenome_ecology]

The hypothesis that PGP genes are predominantly horizontally transferred accessory genes was rejected. All 13 PGP genes had significantly higher core fractions than the genome-wide baseline of 46.8% core (chi-square test against the baseline), with BH-FDR q < 0.05 for all genes. pqqC was 81.5% core, 7.8% auxiliary, and 10.7% singleton (q = 0.0); pqqB was 78.1% core, 8.9% auxiliary, and 13.0% singleton (q = 3.0e-247); hcnA was 78.5% core, 10.8% auxiliary, and 10.8% singleton (q = 9.2e-37); ipdC was 76.5% core, 9.7% auxiliary, and 13.7% singleton (q = 3.4e-19); acdS was 70.4% core, 13.4% auxiliary, and 16.2% singleton (q = 7.9e-25); nifH was 63.8% core, 15.1% auxiliary, and 21.0% singleton (q = 4.3e-71); and pqqD was 55.5% core, 17.0% auxiliary, and 27.5% singleton (q = 2.2e-86). [src: pgp_pangenome_ecology]

The mean accessory fraction across all PGP genes was 29.7%, compared with 53.2% genome-wide. The report treats this as rejecting its accessory/HGT-dominated hypothesis (H3). It does not treat it as ruling out every horizontal gene transfer (HGT) event. Pangenome openness, measured by singleton fraction, correlated negatively with PGP gene richness (Spearman ρ = −0.195, p = 2.0e-97, n = 11,272 species with ≥2 genomes), consistent with PGP-rich species having more closed pangenomes. [src: pgp_pangenome_ecology]

A report figure uses a scatter plot and boxplots to show a negative correlation between singleton fraction, the openness measure, and PGP-gene richness. [src: pgp_pangenome_ecology]

The report notes that the core-inheritance finding aligns with Nascimento et al. (2014). That phylogenetic analysis showed acdS to be predominantly vertically inherited despite documented HGT in some Proteobacteria. Rejecting H3 therefore concerns predominance and does not establish that transfer never occurs. [src: pgp_pangenome_ecology]

pqqD was an outlier, with 55.5% core versus 63–81% for other PGP genes, and the highest singleton fraction (27.5%), which the report takes to suggest that it occasionally spreads horizontally as a standalone gene. This is a suggestion; the report documents no specific transfer event; the functional pqqB–pqqC unit was predominantly core in this analysis. [src: pgp_pangenome_ecology]

By prevalence, pqqD (55.5% core, present in 11,040 species) was the most widespread PGP gene. The report calls it the most promiscuous pqq gene and says it appears as a single-gene orphan in many species that lack other pqq genes. Excluding pqqD, pqqC was the most prevalent focal trait (3,028 species, 26.8% of species with any PGP gene). ipdC was the rarest focal gene (214 species, 1.9%). The figure of 226 counts ipdC gene clusters, whereas 214 counts species carrying at least one such cluster. [src: pgp_pangenome_ecology]

### Tryptophan completeness and ipdC

A report figure shows tryptophan-pathway completeness versus ipdC presence, both as a contingency heatmap and as prevalence by environment. [src: pgp_pangenome_ecology]

Completeness of the tryptophan biosynthesis pathway, assessed with GapMind (a computational pathway-completeness predictor), predicted ipdC presence: ipdC occurred in 2.5% of species with a complete pathway (GapMind score ≥ 0.9) versus 0.9% of species with an incomplete pathway (Fisher OR = 2.81, p = 6.3e-10). A logistic model using tryptophan completeness alone gave OR = 2.81, 95% CI 1.97–4.01, p = 1.4e-08, n = 11,272; adding soil status gave OR = 2.87, p = 7.0e-09. [src: pgp_pangenome_ecology]

The tyrosine pathway, which the report intended as a negative control, also predicted ipdC presence at a similar effect size (OR = 3.62, p = 2.3e-11), so the result does not support a tryptophan-specific mechanism. The report interprets this as consistent with TyrR regulation of ipdC in Enterobacter cloacae, because TyrR responds to tryptophan, tyrosine, and phenylalanine. In this account TyrR induces ipdC in Enterobacter cloacae. The account is cited background from Ryu & Patten (2008, J Bacteriol 190:7200–7208), who studied Enterobacter cloacae UW5, and is not a result of this project. [src: pgp_pangenome_ecology]

The tryptophan–ipdC association reversed within soil/rhizosphere species (n = 1,039), where the OR was 0.30 (p = 0.02), while remaining positive in non-soil species (n = 10,233; OR = 3.56, p = 7.7e-13). The report treats the soil reversal as hypothesis-generating and suggests that soil PGPB may obtain aromatic amino acids from plant exudates while retaining ipdC for indole-3-acetic-acid production from plant-supplied substrate. [src: pgp_pangenome_ecology]

A phylum-plus-soil logistic model failed because of quasi-complete separation caused by the rarity of ipdC, which occurred in 214 species (1.9%). Conclusions therefore rest on the tryptophan-only model and the tryptophan-plus-soil model. [src: pgp_pangenome_ecology]

In the raw soil comparison, ipdC was not significantly enriched (OR = 0.79, ns). A phylum-controlled logistic model instead showed soil depletion (OR = 0.56, p = 0.027). The report connects this to the stratified result: the tryptophan–ipdC positive coupling held only in non-soil species (OR = 3.56) and reversed in soil species (OR = 0.30). [src: pgp_pangenome_ecology]

### Overall interpretation

Together, the co-occurrence and environmental analyses support a non-diazotrophic pqqC + acdS module as a stable, specialized rhizosphere niche marker: pqqC and acdS were tightly co-selected (OR = 7.24), acdS was strongly soil-enriched (OR = 7.02), and PGP genes were predominantly core rather than accessory. nifH represented a separate ecological guild with different co-occurrence partners and environmental distribution. [src: pgp_pangenome_ecology]

The report identifies pqqD as a partial exception to the vertical-inheritance pattern and notes that the nifH gene-cluster count was 2,756, rather than the approximately 1,913 nifH clusters estimated in the research plan (43% higher), reflecting incremental growth in the GTDB r214 pangenome; the discrepancy did not affect the analyses. [src: pgp_pangenome_ecology]

## Caveats

Environment classification was conservative and noisy: only 1,637 species (5.9% of species with an environment label) were classified as soil/rhizosphere dominant, while 291,279 genomes had isolation-source metadata and 93.5% were classifiable. The report states that NCBI is biased toward clinical and host-associated sampling and that the acdS and pqqC enrichment effects may therefore underestimate true rhizosphere enrichment. [src: pgp_pangenome_ecology]

PGP detection relied on Bakta gene annotations matching exact gene names such as nifH, acdS, and pqqC. Product-only annotations and variant gene names could be missed, particularly for less-characterized PGP genes. [src: pgp_pangenome_ecology]

Gene-cluster annotations were not functionally validated: truncations, frameshifts, and pseudogenization were not filtered, so a cluster annotated as pqqC was not necessarily functional. [src: pgp_pangenome_ecology]

ipdC was rare, occurring in only 214 of 11,272 species (1.9%), which limited statistical power for the stratified H4 analysis; the soil reversal (OR = 0.30, p = 0.02) should therefore be treated as hypothesis-generating rather than conclusive. [src: pgp_pangenome_ecology]

GapMind tryptophan and tyrosine completeness scores may proxy for overall metabolic pathway completeness. The report states that genome size, COG (Clusters of Orthologous Groups functional-category) coverage, or total pathway count should be controlled to separate aromatic-pathway-specific effects from general metabolic capacity. [src: pgp_pangenome_ecology]

The report also notes that co-occurrence does not establish physical linkage: whether pqqC and acdS occupy the same genomic island, operon, or separate loci remains unresolved. It proposes operonic-context analysis, deeper nifH ecological stratification, a controlled ipdC model, focused hcnA–hcnC phylogeny, and comparison with commercial inoculant strains as next steps. [src: pgp_pangenome_ecology]

## Proposed Next Steps

Operonic context: the report proposes testing whether pqqC and acdS are physically co-located on the chromosome, in the same genomic island or operon, or instead co-occur between separate loci. This would distinguish functional operon linkage from independent co-selection; the question is unresolved. [src: pgp_pangenome_ecology]

nifH ecological stratification: the report proposes comparing three groups of diazotrophs in genome structure and PGP-trait co-occurrence. The groups are marine/aquatic diazotrophs (cyanobacteria, Azotobacter), legume-symbiotic rhizobia, and free-living soil diazotrophs. This comparison was proposed but not performed. [src: pgp_pangenome_ecology]

Controlled H4 test: the report proposes regressing ipdC presence on tryptophan completeness while controlling for genome-wide pathway completeness, measured as the number of complete pathways or as genome size. This would isolate an aromatic-amino-acid-specific signal from global metabolic capacity. [src: pgp_pangenome_ecology]

HCN production ecology: hcnC was significantly soil-enriched (OR = 1.85) and co-occurred with pqqC (OR = 1.91). The report reads this as suggesting that the hcnA–hcnC operon is part of a rhizosphere niche toolkit. That role is an inference; the report proposes a focused study of hcnA-C phylogeny and its co-occurrence with biocontrol phenotypes. [src: pgp_pangenome_ecology]

Agronomic relevance: the report proposes cross-referencing species that carry the pqqC + acdS + hcnC combination with commercially used inoculant strains. Whether this genomic signature predicts inoculant efficacy remains untested. [src: pgp_pangenome_ecology]

## Data Sources and Outputs

Input tables [src: pgp_pangenome_ecology]:
- The `bakta_annotations` and `gene_cluster` tables supplied PGP gene-cluster extraction with core/auxiliary/singleton flags.
- `gtdb_metadata` supplied per-genome ncbi_isolation_source for environment classification.
- `gtdb_taxonomy_r214v1` in `kbase_ke_pangenome` supplied phylum/family/genus taxonomy for the phylogenetic controls.
- `gapmind_pathways` in `kbase_ke_pangenome` supplied GapMind tryptophan and tyrosine pathway-completeness scores.

GapMind, an automated annotator of amino-acid biosynthesis, is cited as Price, Deutschbauer & Arkin (2021), mBio 12:e00019-21. [src: pgp_pangenome_ecology]

Output files and row counts [src: pgp_pangenome_ecology]:
- `data/genome_environment.csv`: 291,279 rows of per-genome isolation source, environment class and taxonomy.
- `data/species_environment.csv`: 27,690 species-level dominant environment labels, assigned by majority vote.
- `data/pangenome_stats.csv`: 27,702 rows of species-level core/accessory/singleton fractions.
- `data/trp_completeness.csv`: 27,690 rows of GapMind trp and tyr completeness per species.
- `data/pgp_cooccurrence.csv`: 10 pairwise Fisher's exact results for 5 focal PGP genes.
- `data/env_enrichment_results.csv`: 66 rows of soil-enrichment ORs, phylum-stratified results and logit results.
- `data/pgp_core_accessory.csv`: 13 per-gene rows of core/aux/singleton counts with chi-square tests against the baseline.
- `data/trp_iaa_results.csv`: 1 row of Fisher's exact and logit results for trp → ipdC coupling.
- `data/trp_iaa_stratified.csv`: 2 rows of trp → ipdC results, stratified as soil vs non-soil.

Analysis notebooks [src: pgp_pangenome_ecology]:
- `02_pgp_cooccurrence.ipynb` (H1): pairwise Fisher's exact tests, the OR heatmap and trait combinations.
- `03_environmental_selection.ipynb` (H2): soil enrichment, phylum stratification, logistic fixed effects and the sensitivity analysis.
- `04_core_accessory_status.ipynb` (H3): core/aux/singleton fractions, chi-square tests against the baseline and the openness correlation.
- `05_tryptophan_iaa.ipynb` (H4): the trp → ipdC Fisher test, logit models, stratification by environment and a negative control. The notebook listing itself does not report the negative-control result.

## Slots Into

- [[concepts/pangenome-integration]] — PGP genes were predominantly core, and PGP gene richness correlated negatively with pangenome openness, providing evidence about genome organization and inheritance. [src: pgp_pangenome_ecology]
- [[concepts/ecotype-environment-gene-content]] — Soil/rhizosphere environments enriched acdS, pqqC, and hcnC while depleting nifH, linking environment to gene content and ecological guild structure. [src: pgp_pangenome_ecology]
- [[concepts/gene-function-acquisition-depth]] — Core/accessory distributions and the openness correlation constrain whether PGP traits are vertically inherited or laterally acquired. [src: pgp_pangenome_ecology]
- [[concepts/environmental-resistome]] — The report extends environment-stratified gene-distribution analysis to plant-growth-promoting traits, especially the soil enrichment of acdS, pqqC, and hcnC. [src: pgp_pangenome_ecology]
- [[concepts/gene-cooccurrence-ecological-guilds]] — pqqC × acdS was strongly positively associated (OR = 7.24), while nifH was negatively associated with hcnC and pqqC. This separates a diazotroph guild from a pqqC/acdS rhizobacterial guild. [src: pgp_pangenome_ecology]
- [[concepts/two-speed-bacterial-genome]] — All 13 PGP genes exceeded the 46.8% genome-wide core baseline, and pqqD leaned most toward the accessory genome. [src: pgp_pangenome_ecology]
- [[concepts/horizontal-gene-transfer-driven-innovation]] — The accessory/HGT-dominated hypothesis for PGP genes was rejected, but the report acknowledges some HGT events for acdS. [src: pgp_pangenome_ecology]
- [[concepts/pangenome-openness-determinants]] — PGP-gene richness correlated negatively with singleton fraction (Spearman ρ = −0.195). [src: pgp_pangenome_ecology]
- [[concepts/computational-pathway-prediction-validation]] — GapMind tryptophan completeness predicted ipdC, but so did the intended tyrosine negative control, which limits pathway-specific inference. [src: pgp_pangenome_ecology]
- [[concepts/biosynthetic-prototrophy-and-auxotrophy]] — The tryptophan–ipdC association reversed in soil species. The plant-exudate explanation offered for this reversal is a hypothesis. [src: pgp_pangenome_ecology]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — acdS enrichment survived phylum fixed effects. Phylum control turned the ipdC result into soil depletion, and a phylum-plus-soil model failed from quasi-complete separation. [src: pgp_pangenome_ecology]
- [[concepts/cultivation-collection-bias-in-ecological-genomics]] — NCBI clinical/host-associated sampling bias and the composition of nifH carriers in the database shape the environmental contrasts. [src: pgp_pangenome_ecology]
- [[concepts/phenotype-database-coverage-bias]] — Conservative soil/rhizosphere labeling (1,637 species) likely makes the enrichment estimates underestimates. [src: pgp_pangenome_ecology]
- [[concepts/sampling-depth-and-downsampling-effects]] — The nifH gene-cluster count grew from the planned ~1,913 to 2,756 as the GTDB r214 pangenome grew. [src: pgp_pangenome_ecology]
- [[concepts/homology-search-negative-evidence]] — Exact Bakta gene-name matching misses product-only or variant-name annotations, so absence calls are incomplete. [src: pgp_pangenome_ecology]
- [[concepts/functional-marker-validation]] — Annotated PGP clusters were not screened for truncation, frameshift or pseudogenization. [src: pgp_pangenome_ecology]
- [[concepts/confirmatory-exploratory-ecological-association-discordance]] — Because ipdC is rare, the report labels the soil reversal (OR = 0.30, p = 0.02) hypothesis-generating. [src: pgp_pangenome_ecology]
- [[concepts/capability-versus-kinetic-predictability]] — Whether the pqqC + acdS + hcnC genomic signature predicts inoculant efficacy is untested. [src: pgp_pangenome_ecology]
