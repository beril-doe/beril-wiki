---
type: "Summary"
description: "Summary of the project Gene-Resolution Metal Cross-Resistance Across Diverse Bacteria."
doc_type: "short"
full_text: "sources/metal_cross_resistance__REPORT.md"
---
# Gene-Resolution Metal Cross-Resistance Across Diverse Bacteria

This report asks whether bacterial genes that protect against one metal also protect against others, and how that cross-resistance is organised across organisms. Its main answer is that cross-resistance is almost universally positive, while its magnitude is only moderately conserved across organisms. [src: metal_cross_resistance] The evidence comes from gene-level fitness correlations in 28 organisms. [src: metal_cross_resistance] External validation against BacDive gave a null result. [src: metal_cross_resistance] The report reads the results as two layers: a universal directional layer, and a chemistry-specific layer of magnitude. [src: metal_cross_resistance]

## Key Findings

### Cross-resistance is universally positive

Across 317 organism-metal pair observations (28 organisms, 85 unique metal pairs), 98.1% of gene-level fitness correlations were positive (311/317). [src: metal_cross_resistance]

Also, 99.1% were statistically significant (p < 0.05). [src: metal_cross_resistance]

All 15 metal pairs tested in ≥5 organisms showed >90% sign consistency, and no metal pair was systematically negative in any organism. [src: metal_cross_resistance] The report says this was suspected but never shown at scale. [src: metal_cross_resistance]

The report interprets the universal directional layer as shared tolerance machinery. All metals disrupt protein stability, DNA integrity, membrane function and cofactor insertion, and the repair machinery for these processes is shared. [src: metal_cross_resistance] This is an interpretation, not a tested result.

One caveat limits it. All tested metal pairs are positive, so without non-metal stress controls the report cannot distinguish "universal cross-resistance" from "all metals cause general stress". The counter_ion_effects project partly addresses this. [src: metal_cross_resistance]

### Which metal pairs are strongest

The report defines the consensus matrix as the mean Pearson r across organisms. [src: metal_cross_resistance] It describes the magnitude layer as chemistry-specific. Divalent cations that compete for the same binding sites (Co, Ni, Zn) show the strongest cross-resistance. Metals with unique toxicity mechanisms (Al, Mo) show the weakest. [src: metal_cross_resistance]

Co-Ni was the strongest pair (median r ≈ 0.58) across 28 organisms spanning Proteobacteria, Bacteroidetes, Firmicutes, and Actinobacteria. [src: metal_cross_resistance]

The consensus matrix gave Co-Ni mean r = 0.56 across 28 organisms with 100% sign consistency. [src: metal_cross_resistance] The report takes Ni-Co (r = 0.56, n = 28) as validating the classic divalent cation pair at gene resolution across diverse phyla. [src: metal_cross_resistance] It cites Nies (1999, 2003) as describing Co-Ni-Zn cross-resistance mediated by CzcCBA efflux systems. [src: metal_cross_resistance] Its gene-level data extend this: the entire genome responds similarly to Co and Ni, not just efflux genes. [src: metal_cross_resistance]

Fe-Zn had mean r = 0.61 across 6 organisms with 100% sign consistency. [src: metal_cross_resistance] The report calls this unexpectedly strong and suggests it likely reflects shared disruption of iron-sulfur cluster proteins. [src: metal_cross_resistance]

Cu-U had r = 0.51 (n = 5), and the report states that both cause membrane/oxidative damage. [src: metal_cross_resistance]

Other consensus pairs (mean Pearson r, organisms, sign consistency):

- Co-Zn: 0.52, 18 organisms, 100%. [src: metal_cross_resistance]
- Ni-Zn: 0.51, 18 organisms, 100%. [src: metal_cross_resistance]
- Cu-Zn: 0.48, 16 organisms, 100%. [src: metal_cross_resistance]
- Cu-Fe: 0.45, 7 organisms, 100%. [src: metal_cross_resistance]
- Co-Fe: 0.45, 7 organisms, 100%. [src: metal_cross_resistance]
- Al-Zn: 0.44, 13 organisms, 100%. [src: metal_cross_resistance]
- Co-Cu: 0.43, 24 organisms, 96%. [src: metal_cross_resistance]
- Cu-Ni: 0.43, 24 organisms, 96%. [src: metal_cross_resistance]
- Al-Fe: 0.38, 5 organisms, 100%. [src: metal_cross_resistance]
- Fe-Ni: 0.38, 7 organisms, 100%. [src: metal_cross_resistance]
- Al-Cu: 0.34, 17 organisms, 94%. [src: metal_cross_resistance]
- Al-Ni: 0.34, 20 organisms, 95%. [src: metal_cross_resistance]
- Al-Co: 0.30, 20 organisms, 95%. [src: metal_cross_resistance]

Aluminum was the most independent metal (mean r = 0.34), consistent with its unique trivalent toxicity mechanism. [src: metal_cross_resistance] Al-Co and Al-Ni were the weakest pairs (median r ≈ 0.30). [src: metal_cross_resistance] Individual organism heatmaps showed positive cross-resistance throughout, with the Ni-Co/Co-Zn block consistently among the strongest. [src: metal_cross_resistance] DvH, with 13 metals, gave the richest single-organism view, with Mo the most independent metal. [src: metal_cross_resistance]

The report says the counter_ion_effects project found that DvH's metal-NaCl correlation hierarchy follows toxicity mechanism, not counter ion identity. Its own metal-metal correlations across 28 organisms reproduce the same mechanistic grouping. [src: metal_cross_resistance]

### Conservation across organisms

Direction is universal, but magnitude is moderately conserved (leave-one-out consensus prediction r = 0.41, Mantel mean r = 0.23). [src: metal_cross_resistance]

Spearman correlations of rankings on the 10 common metal pairs across 12 organisms with ≥5 metals were mostly positive. [src: metal_cross_resistance] Mantel tests across 351 organism pairs gave mean r = 0.23 with 62% positive, which the report calls moderate but consistent conservation. [src: metal_cross_resistance]

The metal-label permutation test was non-significant (p = 0.42). [src: metal_cross_resistance] The report attributes this to all metal pairs being positive, so shuffling labels does not change the mean. [src: metal_cross_resistance] It reads this as showing that the signal lies in universal positivity, not in specific pair identities. [src: metal_cross_resistance]

Leave-one-out prediction had mean r = 0.41, which the report calls a useful predictor of individual organism patterns. [src: metal_cross_resistance] However, only 2/28 organisms reached individual significance, so individual organisms deviate meaningfully from the average. [src: metal_cross_resistance]

The 28 organisms are not phylogenetically independent. The report says formal comparative methods (PGLS, phylogenetic generalized least squares, or independent contrasts) would strengthen the conservation claim. [src: metal_cross_resistance]

### Three tiers of metal-important genes

The report classified 8,162 metal-important genes across 28 organisms into three tiers. [src: metal_cross_resistance] General-stress genes are pleiotropic and important across many conditions. Metal-shared genes are important for ≥2 metals. Metal-specific genes are important for exactly 1 metal. [src: metal_cross_resistance]

- General stress: 1,484 genes, 18.2% of total, mean core 92.0%, fully core (≥95%) 57.2%. [src: metal_cross_resistance]
- Metal-shared: 2,306 genes, 28.3% of total, mean core 91.0%, fully core 50.4%. [src: metal_cross_resistance]
- Metal-specific: 4,372 genes, 53.6% of total, mean core 89.8%, fully core 45.7%. [src: metal_cross_resistance]

General-stress genes were the most pangenome-conserved, metal-shared intermediate, and metal-specific least conserved. [src: metal_cross_resistance] The fully core gradient (57.2% → 50.4% → 45.7%) is an 11.5 percentage point spread. [src: metal_cross_resistance] The report reads this as supporting an evolutionary model running from ancestral general-stress defense, through slower-evolving shared metal defense, to faster-evolving, more accessory metal-specific resistance. [src: metal_cross_resistance]

This extends the Metal Fitness Atlas, which showed metal genes are 87.4% core. [src: metal_cross_resistance] Within metal genes the report describes a finer gradient, general stress (92%) > shared (91%) > specific (90%), which it interprets as reflecting the evolutionary history of metal tolerance. [src: metal_cross_resistance] It proposes the decomposition and gradient as a new framework for metal tolerance evolution. [src: metal_cross_resistance]

Keyword analysis found general-stress genes enriched for energy/respiration and cell-envelope functions. [src: metal_cross_resistance] Metal-specific genes were enriched for transporters/efflux and iron/metal-related functions, consistent with dedicated transport systems. [src: metal_cross_resistance]

### Conserved cross-resistance gene families

NB05 identified 318 ortholog groups (OG) that were metal-shared in ≥2 organisms. [src: metal_cross_resistance] The most broadly conserved families span up to 14 organisms and encode cell-envelope, energy-metabolism, DNA-repair, and ion-homeostasis functions. [src: metal_cross_resistance] The report characterizes them as core machinery of multi-metal tolerance, consistently required against multiple metals across diverse bacteria. [src: metal_cross_resistance] It proposes them as candidates for engineering enhanced metal tolerance or for bioremediation. [src: metal_cross_resistance]

### External validation was null

Multi-metal tolerance scores did not correlate with BacDive isolation from metal environments at the Fitness Browser (FB) species scale (Spearman rho ~ -0.02, p > 0.8). [src: metal_cross_resistance] The report notes this validation (n = 26) lacks the power of the Metal Fitness Atlas at pangenome scale (42K strains). [src: metal_cross_resistance]

The validation set excluded 2 organisms without tier data (azobra and BFirm, with <3 metals). [src: metal_cross_resistance] It also collapsed multiple FB strains of a species into one entry, for example 5 P. fluorescens strains sharing one BacDive pool. [src: metal_cross_resistance] The effective sample was 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance] Matching used genus+species substring search, which is imprecise for genus-only names such as Acidovorax sp., so fuzzy matches need caution. [src: metal_cross_resistance]

The report expects this null, because the prior bacdive_metal_validation project showed that metal-tolerance prediction needs pangenome-scale analysis (42K strains, Cohen's d = +1.0). [src: metal_cross_resistance] A proper H3 test would apply the Metal Fitness Atlas KEGG/PFAM mapping to cross-resistance gene signatures across 27K species. [src: metal_cross_resistance]

### Novelty relative to prior work

The report contrasts prior MIC (minimum inhibitory concentration) studies on 1-5 model organisms with its gene-level fitness analysis across 28 organisms and 13 metals, claiming a 100× increase in resolution and 5× in taxonomic breadth. [src: metal_cross_resistance] It presents this as the first gene-resolution cross-resistance analysis, since prior work used binary resistant/sensitive MIC data. [src: metal_cross_resistance] It describes Pal et al. (2015) as using resistance-gene presence/absence across genomes to show metal-antibiotic co-occurrence. [src: metal_cross_resistance] The fitness data complement this by quantifying partial gene importance for metals. [src: metal_cross_resistance]

## Data and Methods

The report classified 452 metal experiments across 37 organisms and 14 metals (Al, Cd, Co, Cr, Cu, Fe, Hg, Mn, Mo, Ni, Se, U, W, Zn). [src: metal_cross_resistance] It extracted metal fitness data for 119,561 genes for 28 organisms with ≥3 metals (30 extracted, 2 excluded for having <3 metals). [src: metal_cross_resistance] The correlation analysis used 317 organism-pair observations across 85 unique metal pairs. [src: metal_cross_resistance]

It drew on the KBase Data Lakehouse collection kescience_fitnessbrowser (experiment, genefitness, gene, organism tables) for metal experiment classification, fitness extraction and annotations. [src: metal_cross_resistance] It used kbase_ke_pangenome via ortholog groups for core/accessory classification. [src: metal_cross_resistance] It used the strain and isolation tables of kescience_bacdive for validation metadata. [src: metal_cross_resistance]

## Caveats and Open Work

- Different experiments used different metal concentrations, so dose-response effects could influence cross-resistance estimates. [src: metal_cross_resistance]
- Organisms range from 3 to 112 metal experiments, affecting the reliability of per-organism matrices. [src: metal_cross_resistance]
- Phylogenetic non-independence and the underpowered BacDive validation are described above. [src: metal_cross_resistance]
- The absence of non-metal stress controls is described above. [src: metal_cross_resistance]

The report proposes these next steps:

- Pangenome-scale H3 validation across 27K species using the Metal Fitness Atlas KEGG/PFAM mapping, checked against BacDive polymetallic isolation environments. [src: metal_cross_resistance]
- PGLS or phylogenetic PCA (principal component analysis) to control for phylogenetic non-independence. [src: metal_cross_resistance]
- Normalizing fitness effects by metal concentration relative to MIC. [src: metal_cross_resistance]
- Applying ICA (independent component analysis) from the fitness_modules project to metal conditions, to test whether cross-resistance genes cluster into coherent regulatory units. [src: metal_cross_resistance]
- Using AlphaFold structures to test whether metal binding sites or membrane interfaces in metal-shared proteins explain multi-metal sensitivity. [src: metal_cross_resistance]

## Slots Into

- universal positivity and chemistry specific magnitude of metal cross resistance: 98.1% of correlations were positive, with magnitude strongest for Co, Ni and Zn and weakest for Al and Mo. [src: metal_cross_resistance]
- [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]]: core enrichment is layered, general stress (92%) > shared (91%) > specific (90%). [src: metal_cross_resistance]
- [[concepts/counter-ion-confounding-in-metal-fitness-assays]]: the mechanistic grouping from counter_ion_effects is reproduced across 28 organisms. [src: metal_cross_resistance]
- [[concepts/metal-responsive-ica-fitness-modules]]: ICA on metal conditions is proposed to find co-regulated modules. [src: metal_cross_resistance]
