---
type: "Summary"
description: "Summary of the project Metal-Gene Density Predicts Ecological Niche Breadth in Prokaryotes."
doc_type: "short"
full_text: "sources/comprehensive_metal_ecology__REPORT.md"
---
# Metal-Gene Density Predicts Ecological Niche Breadth in Prokaryotes

This page summarises the project "Metal-Gene Density Predicts Ecological Niche Breadth in Prokaryotes". The report asks whether genera that carry more metal-related genes occupy narrower ecological niches. Its main answer is yes for bacteria: higher metal-gene density goes with narrower niche breadth, though the effect is small. The statistical evidence is strong (a phylogenetically controlled test across 1,574 genera). Specificity to metal genes is not demonstrated, because the pre-specified housekeeping control gene sets also showed significant negative associations. [src: comprehensive_metal_ecology]

## Key Findings

### Main association and its robustness

Across 1,574 bacterial genera matched between the GTDB phylogeny and global MGnify MAG data, per-Mb Tier 1+2 metal-gene KO (KEGG ortholog) density was negatively associated with standardised Levins' niche breadth: β = −0.021, SE = 0.0037, t = −5.63, p = 2.1×10⁻⁸, FDR joint p = 6.4×10⁻⁸, Pagel's λ = 0.757, ΔAIC = −29.4, r² = 0.046. [src: comprehensive_metal_ecology] The functional-landscape table lists this reference as 140 KOs across 1,574 genera. [src: comprehensive_metal_ecology] See [[concepts/metal-gene-density-and-ecological-niche-breadth]] and [[entities/levins-niche-breadth]].

The signal survived several checks, so it is not tied to one confounder or one estimate:
- Adding dominant biome as a covariate changed the coefficient magnitude from 0.021 to 0.020, a 5.8% attenuation with p <10⁻⁴, classed as robust. [src: comprehensive_metal_ecology]
- Adding MAG contamination gave β(density) = −0.023 (p = 5.4×10⁻⁸), with <1.2% change in β. [src: comprehensive_metal_ecology]
- Bootstrap mean niche breadth correlated almost perfectly with the original genus estimate (Pearson r = 0.99869; max |Δ| per genus = 0.064). [src: comprehensive_metal_ecology]
- Restricting to ≥20 MicrobeAtlas samples gave n = 1,570 genera, β = −0.021, SE = 0.00368, p = 1.69×10⁻⁸. [src: comprehensive_metal_ecology]
- The report reads agreement between the independent EMP (Earth Microbiome Project) and MicrobeAtlas niche metrics as showing that MicrobeAtlas B_std captures genuine ecological breadth. [src: comprehensive_metal_ecology]
- The soil-specialist result is described as consistent with the predecessor project's MicrobeAtlas association (β = −0.023, n = 603, p = 0.0002). [src: comprehensive_metal_ecology]

The report reads latitude control as removing a between-latitude composition effect and revealing a stronger within-latitude association. [src: comprehensive_metal_ecology] See [[concepts/robustness-and-replication-of-niche-breadth-associations]].

### Replication limits

Replications are weaker than the primary test. The archaeal replication is directionally consistent but non-significant, which the report attributes to low power at n = 95 and a small effect size. [src: comprehensive_metal_ecology] The distinct-biome-count metric gave a concordant but non-significant trend (ρ = +0.044, p = 0.165). [src: comprehensive_metal_ecology] Within Firmicutes, PGLS (phylogenetic generalized least squares) was borderline: n = 334, λ = 0.629, β = −0.015, CI [−0.031, +0.000], q_BH = 0.073. [src: comprehensive_metal_ecology] The Australian replication (P4) tests only 5 metals: Cu, Zn, Pb, Ni and Co. [src: comprehensive_metal_ecology] The AusMicrobiome P5 analysis is not independent, because its 482 genera are a subset of P1 and the predictor is identical. [src: comprehensive_metal_ecology] A z-test found P5 > P1-full (z = −4.24, p = 2.2×10⁻⁵). [src: comprehensive_metal_ecology] The report links the larger P5 β to the Proteobacteria-enriched genus panel [src: comprehensive_metal_ecology] and notes a lower λ in P5 (0.734 vs 0.757 in P1). [src: comprehensive_metal_ecology]

### Controls are not true nulls

The pre-specified negative controls (ribosomal proteins, amino acid biosynthesis, DNA repair) all showed highly significant negative associations with niche breadth, not the near-zero values expected. [src: comprehensive_metal_ecology] For amino acid biosynthesis, 38 KOs across 1,073 genera gave β = −0.034, p = 9.5×10⁻¹⁵. [src: comprehensive_metal_ecology] These results mean specificity of the signal to metal genes is not demonstrated. See [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]].

### Functional landscape: constitutive versus inducible classes

In the functional-landscape analysis, 14/19 categories had significantly negative associations (q < 0.05). [src: comprehensive_metal_ecology] Replication and repair (60 KOs; 1,073 genera) gave β = −0.035, q_BH = 1.0×10⁻¹¹. [src: comprehensive_metal_ecology] Cofactors and vitamins (382 KOs) gave β = −0.029, q_BH = 1.4×10⁻¹⁰. [src: comprehensive_metal_ecology] Non-metal ABC (ATP-binding cassette) transporters (475 KOs) were null: β = −0.006, q_BH = 0.457. [src: comprehensive_metal_ecology] Beta-lactam AMR (antimicrobial resistance; 112 KOs) was a confirmed true negative: β = −0.004, q_BH = 0.505, characterised as HGT-mobile and condition-acquired. [src: comprehensive_metal_ecology] See [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations]].

Within the metal set, Resistance/Detoxification (106 KOs) was null: β = +0.003, SE = 0.006, FDR p = 0.656. [src: comprehensive_metal_ecology] The report ties this to the ubiquity of resistance genes and their susceptibility to HGT (horizontal gene transfer), which decouples abundance from specialisation. [src: comprehensive_metal_ecology] It classes metal resistance genes as a near-null category. [src: comprehensive_metal_ecology] Exploratory AMR target modification was positive but non-significant (β = +0.009, q = 0.19). [src: comprehensive_metal_ecology] All ABC substrates other than Lipid/LPS export were near-zero or positive (q > 0.25). [src: comprehensive_metal_ecology] The ABC Lipid/LPS-versus-others Δβ of 0.032 was smaller than the metal-set Δβ of 0.035. [src: comprehensive_metal_ecology]

Metal-specific subsets were also negative. The Tl set (45 KOs) gave β = −0.027, BH-FDR p = 1.1×10⁻⁸. [src: comprehensive_metal_ecology] The S set (74 KOs) gave β = −0.021, BH-FDR p = 4.9×10⁻⁵. [src: comprehensive_metal_ecology] In an exploratory cofactor jackknife, excluding K01772 gave β = −0.016 (p = 0.000222), while excluding K02225, K03635 or K22225 gave β between −0.027 and −0.029. [src: comprehensive_metal_ecology]

### Environmental correlates

Metal-gene density did not predict temperature range: n = 1,195 genera, β = +0.079, SE = 0.886, p = 0.929 (exploratory). [src: comprehensive_metal_ecology] The report states that Cr and Co bedrock enrichment, both linked to mafic geology, positively predicts niche breadth after controlling for metal genes. [src: comprehensive_metal_ecology] The exploratory per-KO driver analysis tested 9 TIER1 KOs against 22 environmental niche-breadth responses. [src: comprehensive_metal_ecology] Of 198 models, 32 were significant at p < 0.05 (16.2%) and 28 at FDR q < 0.1. [src: comprehensive_metal_ecology] cusR (K07665) had 2 significant responses. [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].

### Horizontal transfer signatures

The report applied a two-scale framework: genome-level Fritz & Purvis D (GTDB 18,961-tip tree; 309 KOs with ≥20 genomes; D = 1 random/HGT-like, D = 0 Brownian/vertical) and genus-level Pagel's λ (275 KOs). [src: comprehensive_metal_ecology] Example candidates:
- merE (K19059, Resistance): D = 0.728, λ = 0.102, n = 154 genomes. [src: comprehensive_metal_ecology]
- shp (K25119, Resistance): D = 0.385, λ = 0.000, n = 123. [src: comprehensive_metal_ecology]
- nicC (K14974, Transport): D = 0.224, λ = 0.000, n = 382. [src: comprehensive_metal_ecology]

Plasmid evidence is modest. Double-signal resistance KOs had a median NCBI Entrez plasmid fraction of 0.0042 versus 0.0004 for background resistance KOs (n = 3 vs 51; MWU p = 0.045). [src: comprehensive_metal_ecology] The three tested KOs were merD 4.3%, aoxB 0.4% and norB 0.1%. [src: comprehensive_metal_ecology] The report calls the test conservative because high-plasmid background KOs (pcoB 6.8%, merA 4.5%, tetA 4.1%) fail the double-signal threshold. [src: comprehensive_metal_ecology] Median NCBI mobile-element fractions were 0.000 in both groups (DS n=13 vs ctrl n=10; p = 0.062). [src: comprehensive_metal_ecology] The report says the plasmid-fraction gradient resistance > transport ≈ sensing > metabolism > cofactor mirrors the λ ordering. [src: comprehensive_metal_ecology] In the NCBI cross-category table, Metal-dependent Metabolism had n = 14 and median 0.00016. [src: comprehensive_metal_ecology] In the BV-BRC table (n≥50), it had n = 12 and median 0.00033 [src: comprehensive_metal_ecology], and resistance was not significantly above Sensing (p=0.103). [src: comprehensive_metal_ecology] Among double-signal KOs with MGnify data, 5/8 showed environmental metal enrichment at FDR q < 0.1, including gesA (q = 9.4×10⁻⁵). [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

### Co-occurrence partners

In the MicrobeAtlas ENV stratum, metal-gene density positively predicted significant positive partners (n genera 3,382 → 1,572; β = 134.0, SE = 13.8, t = 9.74, p = 8.5×10⁻²², λ = 0.625). [src: comprehensive_metal_ecology] The negative-partner coefficient was lowest in soil (sig_neg β = 27.4 vs all = 39.5 vs env = 45.3). [src: comprehensive_metal_ecology] Among soil partners, 56.1% were in the top quartile for top-50 focal genera versus 26.3% for Control-50. [src: comprehensive_metal_ecology] Metal-gene-rich focal genera preferentially paired with Firmicutes in soil, although Proteobacteria make up 43% of genera in the full PGLS table. [src: comprehensive_metal_ecology] See [[concepts/co-occurrence-network-structure-and-metal-tolerance-guilds]].

### Annotation validity

Among KOs without metal-coordination clans, 113 carry ABC transporter scaffolds, MerR/CusR/ZntR sensor Pfams and outer-membrane efflux proteins. The report calls them mechanistically correct metal-processing proteins whose domains are transport or substrate-binding scaffolds. [src: comprehensive_metal_ecology] See [[concepts/validity-of-curated-metal-gene-annotation]].

## Key Findings: Finding 3 — Genome streamlining is pervasive; metal-gene investment sits in …

This part of the report tests whether bacterial genera with higher metal-gene density have narrower niches. The primary test confirms it, but the effect is small, replications are mixed, and the negative controls show that most gene sets share the same negative association. [src: comprehensive_metal_ecology]

### Primary association (P1)

In 1,574 bacterial genera matched across the GTDB phylogeny and global MGnify MAG (metagenome assembled genome) data, per-Mb Tier 1+2 metal-gene KO (KEGG ortholog) density was negatively associated with standardised Levins' niche breadth. The estimates were β = −0.021, SE (standard error) = 0.0037, t = −5.63, p = 2.1×10⁻⁸, FDR (false discovery rate) joint p = 6.4×10⁻⁸, Pagel's λ = 0.757, ΔAIC = −29.4 and r² = 0.046. [src: comprehensive_metal_ecology] The report treats the pre-registered hypothesis H1 (β < 0) as confirmed. [src: comprehensive_metal_ecology] It reads the moderate λ as meaning shared ancestry explains the relationship partly but not entirely. [src: comprehensive_metal_ecology] Niche breadth came from MicrobeAtlas Env_Level_1 habitat categories, not soil chemistry. This keeps the niche-breadth and metal-concentration axes independent. [src: comprehensive_metal_ecology]

### Replication and sensitivity

- **Archaea (P2):** With the GTDB archaeal tree (n = 95), β = −0.014 (p = 0.119). This is directionally consistent with P1 but non-significant. [src: comprehensive_metal_ecology] The report suggests low power and a small effect size likely explain this. [src: comprehensive_metal_ecology]
- **Australia only (P3):** In the NGSA replication (n = 482), the association was near zero (β = −0.002, p = 0.755). [src: comprehensive_metal_ecology]
- **Sensitivity analyses:** Across 8 pre-specified analyses, the report states that 6/7 directionally confirm H1 (all β < 0, 5 significant at p < 0.05). [src: comprehensive_metal_ecology]
- **Phylogenetic correction:** The signal persisted under λ = 0 (OLS, ordinary least squares: β = −0.032, p ≈ 0). [src: comprehensive_metal_ecology] It also persisted under λ = 1 Brownian motion (β = −0.018, p = 3.7×10⁻⁶). The report concludes it is not an artefact of any single phylogenetic correction assumption. [src: comprehensive_metal_ecology]

### Negative controls reveal a streamlining baseline

The pre-specified negative controls did not behave as nulls. Ribosomal proteins, amino acid biosynthesis and DNA repair each showed a highly significant negative association with niche breadth, not the near-zero association anticipated. [src: comprehensive_metal_ecology] The report interprets this as a pervasive genome-streamlining baseline. Specialist genera have smaller genomes, so any conserved, near-universal gene set is denser per Mb. [src: comprehensive_metal_ecology]

### Functional-landscape analysis (NB18, exploratory)

NB18 tested 19 KEGG functional categories at the same per-Mb density resolution with BH-FDR (Benjamini-Hochberg false discovery rate) correction. [src: comprehensive_metal_ecology] Of the 19 categories, 14 were significantly negative (q < 0.05). [src: comprehensive_metal_ecology] The constitutive housekeeping and information-processing categories define a baseline of β ≈ −0.029 to −0.035. [src: comprehensive_metal_ecology]

| Category | KOs | Genera | β | q_BH |
|---|---|---|---|---|
| Replication and repair | 60 | 1,073 | −0.035 | 1.0×10⁻¹¹ [src: comprehensive_metal_ecology] |
| Nucleotide metabolism | 123 | 1,073 | −0.032 | 2.3×10⁻¹⁰ [src: comprehensive_metal_ecology] |
| Amino acid metabolism | 242 | 1,073 | −0.031 | 3.7×10⁻¹² [src: comprehensive_metal_ecology] |
| Translation (ribosome) | 206 | 1,073 | −0.030 | 1.2×10⁻⁹ [src: comprehensive_metal_ecology] |
| Protein folding/degradation | 49 | 1,073 | −0.030 | 1.4×10⁻¹⁰ [src: comprehensive_metal_ecology] |
| Cofactors and vitamins | 382 | 1,073 | −0.029 | 1.4×10⁻¹⁰ [src: comprehensive_metal_ecology] |
| Secondary metabolism | 2,326 | 1,073 | −0.028 | 3.1×10⁻¹⁰ [src: comprehensive_metal_ecology] |
| Transcription (RNA polymerase) | 66 | 1,071 | −0.028 | 6.3×10⁻⁸ [src: comprehensive_metal_ecology] |
| Carbohydrate metabolism | 387 | 1,073 | −0.026 | 3.1×10⁻⁹ [src: comprehensive_metal_ecology] |
| Lipid metabolism | 84 | 1,069 | −0.021 | 5.8×10⁻⁶ [src: comprehensive_metal_ecology] |
| Metal Tier 1+2 (P1 reference) | 140 | 1,574 | −0.021 | none supplied [src: comprehensive_metal_ecology] |
| Quorum sensing | 283 | 1,073 | −0.017 | 1.1×10⁻³ [src: comprehensive_metal_ecology] |
| Xenobiotics biodegradation | 1,449 | 1,073 | −0.017 | 1.1×10⁻³ [src: comprehensive_metal_ecology] |
| Energy metabolism | 224 | 1,073 | −0.015 | 3.5×10⁻³ [src: comprehensive_metal_ecology] |
| Terpenoids and polyketides | 66 | 665 | −0.010 | 4.9×10⁻² [src: comprehensive_metal_ecology] |

Five categories were non-significant:

| Category | KOs | Genera | β | q_BH |
|---|---|---|---|---|
| ABC (ATP-binding cassette) transporters (non-metal) | 475 | 1,073 | −0.006 | 0.457 [src: comprehensive_metal_ecology] |
| AMR (antimicrobial resistance, beta-lactam) | 112 | 1,073 | −0.004 | 0.505 [src: comprehensive_metal_ecology] |
| Glycan biosynthesis (peptidoglycan) | 73 | 1,050 | +0.001 | 0.767 [src: comprehensive_metal_ecology] |
| Cell motility | 153 | 1,063 | +0.004 | 0.505 [src: comprehensive_metal_ecology] |
| Two-component systems | 521 | 1,073 | +0.006 | 0.457 [src: comprehensive_metal_ecology] |

### Where the metal-gene signal sits

The metal-gene P1 association (β = −0.021) ranks 11th of 19, roughly tied with lipid metabolism. It is 30–60% weaker than the housekeeping baseline, so it is not anomalously strong. [src: comprehensive_metal_ecology] The report interprets this as selective retention of metal-processing functions. On this reading, specialists keep higher per-Mb metal-gene density than uniform genome compaction would predict. [src: comprehensive_metal_ecology] The report therefore argues that the appropriate null for the metal-gene signal is the housekeeping β (≈ −0.029 to −0.035), not zero. [src: comprehensive_metal_ecology] See [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]] and [[concepts/metal-gene-density-and-ecological-niche-breadth]].

## Key Findings: Finding 4 — Cofactor biosynthesis carries the strongest signal; resistance …

In the bacterial global MGnify MAG (metagenome assembled genomes) niche-breadth analysis, cofactor biosynthesis has the strongest negative association with niche breadth. Transport/Homeostasis, Sensing/Regulation and Metal-dependent Metabolism are also negative, and Resistance/Detoxification shows no association. [src: comprehensive_metal_ecology] The follow-up tests below, including the permutation test and the cofactor jackknife, are labelled exploratory. [src: comprehensive_metal_ecology] See also [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations]].

### Category effects

Four of five metal functional categories have significant negative β, and Resistance/Detoxification is the null, as the report expected. [src: comprehensive_metal_ecology] Each row below gives KOs (KEGG orthologs), β, SE (standard error) and FDR (false discovery rate) p.

| Category | KOs | β | SE | FDR p |
|---|---|---|---|---|
| Resistance/Detoxification [src: comprehensive_metal_ecology] | 106 | +0.003 | 0.006 | 0.656 |
| Transport/Homeostasis [src: comprehensive_metal_ecology] | 213 | −0.022 | 0.005 | 2.8×10⁻⁵ |
| Sensing/Regulation [src: comprehensive_metal_ecology] | 48 | −0.018 | 0.005 | 9.1×10⁻⁴ |
| Cofactor Biosynthesis [src: comprehensive_metal_ecology] | 7 | −0.033 | 0.005 | 5.2×10⁻⁹ |
| Metal-dependent Metabolism [src: comprehensive_metal_ecology] | 54 | −0.021 | 0.005 | 1.2×10⁻⁴ |

Cofactor biosynthesis has the largest effect, and it equals the housekeeping baseline (β = −0.033). [src: comprehensive_metal_ecology] Its 7 KOs encode Fe–S cluster assembly, molybdopterin synthesis and cobalamin pathway genes. These are constitutively required for core metabolism that depends on metal cofactors, such as nitrogen fixation, anaerobic respiration and methanogenesis. [src: comprehensive_metal_ecology] The report reads the resistance null as consistent with the ubiquity of resistance genes and their susceptibility to horizontal gene transfer (HGT). It proposes that this decouples their abundance from ecological specialisation. [src: comprehensive_metal_ecology]

### Split-magnitude permutation test (exploratory)

A permutation test randomly split the 140-KO metal set into groups of 106 and 7, matching the resistance and cofactor group sizes, in 1,000 partitions. [src: comprehensive_metal_ecology] The observed Δβ = 0.035259 exceeded all 1,000 null splits (p < 0.001). The null median Δβ was −0.006 with SD (standard deviation) 0.007, so the observed split sits about 6 SD above null. [src: comprehensive_metal_ecology] The report concludes that the contrast is not an artefact of unequal group sizes or sampling variance. [src: comprehensive_metal_ecology]

The report calls the resistance-null/constitutive-significant split mechanistically specific to metal genes. It argues that the split requires constitutive metabolic coupling to the predictor category, which inducible resistance and regulatory gene sets lack. [src: comprehensive_metal_ecology]

### Comparison families (exploratory)

Comparison gene families show smaller internal splits than the metal set. Their Δβ values were 0.032 for ABC (ATP-binding cassette) transporters (Lipid/LPS versus all others), 0.012 for AMR (antimicrobial resistance) and 0.006 for TCS (two-component systems). All are smaller than the metal gene set Δβ of 0.035. [src: comprehensive_metal_ecology]

- Among ABC transporters, Lipid/LPS (lipopolysaccharide) export is the only significantly negative subcategory (16 KOs, β = −0.030, q = 3.3×10⁻⁵). That is comparable to the metal cofactor signal, and the report says it likely reflects constitutive outer-membrane lipid maintenance. [src: comprehensive_metal_ecology]
- All other ABC substrates are near zero or positive (q > 0.25). [src: comprehensive_metal_ecology]
- AMR subcategories are all positive, but only efflux pumps are significant (β = +0.018, q = 0.016). [src: comprehensive_metal_ecology]
- AMR enzymatic inactivation (β = +0.006, q = 0.21) and target modification (β = +0.009, q = 0.19) are not significant. [src: comprehensive_metal_ecology]
- TCS sensor kinases (β = +0.008, q = 0.25), response regulators (β = +0.009, q = 0.25) and phosphotransfer (β = +0.003, q = 0.68) are all positive and nonsignificant. [src: comprehensive_metal_ecology]

### Cofactor jackknife (exploratory)

Three of the seven cofactor KOs were absent from the MGnify MAG dataset and contributed zero density. The leave-one-out jackknife therefore used only the four detectably represented KOs, which limits how far it tests the full 7-KO category. [src: comprehensive_metal_ecology] Every 3-KO remainder stayed highly significant (β range −0.016 to −0.029, all p < 0.001), with no sign changes. [src: comprehensive_metal_ecology]

| KO excluded | β | SE | p |
|---|---|---|---|
| K01772 [src: comprehensive_metal_ecology] | −0.016 | 0.00441 | 0.000222 |
| K02225 [src: comprehensive_metal_ecology] | −0.027 | 0.00444 | 1.4×10⁻⁹ |
| K03635 [src: comprehensive_metal_ecology] | −0.029 | 0.00443 | 1.3×10⁻¹⁰ |
| K22225 [src: comprehensive_metal_ecology] | −0.028 | 0.00478 | 8.2×10⁻⁹ |

The report concludes that the signal is distributed across the Fe–S cluster, molybdopterin and cobalamin pathway rather than concentrated in one gene. [src: comprehensive_metal_ecology] See [[entities/iron-sulfur-cluster-biogenesis]].

### Per-metal sets

Every metal-specific set has a significant negative association, and the effects are similar in size. [src: comprehensive_metal_ecology] The global panel includes all metals with ≥34 KOs: Cu, Zn, Fe, Ni, Co, Mn, Tl, Al and S. [src: comprehensive_metal_ecology]

| Metal | KOs | β | BH-FDR (Benjamini-Hochberg false discovery rate) p |
|---|---|---|---|
| Tl [src: comprehensive_metal_ecology] | 45 | −0.027 | 1.1×10⁻⁸ |
| Fe [src: comprehensive_metal_ecology] | 98 | −0.025 | 1.2×10⁻⁷ |
| Ni [src: comprehensive_metal_ecology] | 84 | −0.025 | 1.9×10⁻⁷ |
| Zn [src: comprehensive_metal_ecology] | 67 | −0.023 | 1.1×10⁻⁶ |
| Al [src: comprehensive_metal_ecology] | 34 | −0.023 | 8.8×10⁻⁶ |
| Co [src: comprehensive_metal_ecology] | 101 | −0.022 | 3.9×10⁻⁶ |
| S [src: comprehensive_metal_ecology] | 74 | −0.021 | 4.9×10⁻⁵ |
| Cu [src: comprehensive_metal_ecology] | 71 | −0.019 | 7.7×10⁻⁵ |
| Mn [src: comprehensive_metal_ecology] | 34 | −0.017 | 3.8×10⁻⁴ |

The report argues that this uniformity across chemically diverse metals argues against any single element driving the signal. [src: comprehensive_metal_ecology] Two inclusions need context. S-associated KOs predominantly encode the Fe–S cluster biogenesis proteins iscS, iscU, sufB and nifU, which are metal-cofactor systems. [src: comprehensive_metal_ecology] The report justifies including Al by its documented bacterial toxicity and dedicated resistance systems. [src: comprehensive_metal_ecology]

The Australian replication (P4) tests only the 5 metals available in NGSA geochemistry: Cu, Zn, Pb, Ni and Co. [src: comprehensive_metal_ecology]

## Key Findings: Finding 7 — No pre-specified confounder eliminates the signal

This part of the report separates gene categories that scale with genome streamlining from those that do not. It names five true-negative functional categories, then tests the metal-gene signal against coreness-matched nulls, an AusMicrobiome comparison, covariates, MAG (metagenome assembled genome) quality and niche-breadth bootstrapping. [src: comprehensive_metal_ecology] The metal-gene signal survives most checks, but it cannot be told apart from random conserved gene sets in overall magnitude. [src: comprehensive_metal_ecology]

### Negative controls: housekeeping genes are not true negatives

The report says the three named housekeeping controls are streamlining indicators, not true negatives. A valid negative control must have a per-Mb density that does not scale with specialisation. [src: comprehensive_metal_ecology] Each housekeeping set shows a significant negative coefficient, as the primary bacterial metal-gene analysis does. [src: comprehensive_metal_ecology]

| Category | KOs (KEGG orthologs) | Genera | λ | β | SE | p |
|---|---|---|---|---|---|---|
| Ribosomal proteins | 52 | 1,073 | 0.791 | −0.029 | 0.00474 | 7.6×10⁻¹⁰ [src: comprehensive_metal_ecology] |
| Amino acid biosynthesis | 38 | 1,073 | 0.794 | −0.034 | 0.00427 | 9.5×10⁻¹⁵ [src: comprehensive_metal_ecology] |
| DNA repair | 24 | 1,073 | 0.789 | −0.033 | 0.00476 | 4.0×10⁻¹² [src: comprehensive_metal_ecology] |
| Metal genes Tier 1+2 (P1) | 140 | 1,574 | 0.757 | −0.021 | 0.00370 | 2.1×10⁻⁸ [src: comprehensive_metal_ecology] |

### Five confirmed true negatives

In the functional-landscape analysis (NB18), five categories show no significant association. [src: comprehensive_metal_ecology] The report calls all five variable, inducible or horizontally acquired gene sets that are not constitutively coupled to genome size. [src: comprehensive_metal_ecology]

| Category | KOs | β | q_BH | Character |
|---|---|---|---|---|
| ABC (ATP-binding cassette) transporters, non-metal | 475 | −0.006 | 0.457 | Inducible; substrate-specific [src: comprehensive_metal_ecology] |
| AMR (antimicrobial resistance), beta-lactam | 112 | −0.004 | 0.505 | HGT-mobile; condition-acquired [src: comprehensive_metal_ecology] |
| Peptidoglycan glycan biosynthesis | 73 | +0.001 | 0.767 | Near-universal; niche-independent [src: comprehensive_metal_ecology] |
| Cell motility | 153 | +0.004 | 0.505 | Environment-dependent expression [src: comprehensive_metal_ecology] |
| Two-component systems | 521 | +0.006 | 0.457 | Inducible regulatory network [src: comprehensive_metal_ecology] |

Metal resistance genes (β ≈ 0) share this character. The report classifies them as a near-null category within the metal-gene set. [src: comprehensive_metal_ecology] See [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations]].

### Permutation tests and phylogenetic artefact

A permutation test with 1,000 predictor-permutations gave empirical p < 0.001. The report reads this as showing the primary signal is not a phylogenetic artefact. [src: comprehensive_metal_ecology] A coreness-matched permutation (NB20) used 1,000 KO sets matched on KO count and pan-genome prevalence decile distribution. It gave emp_p = 0.298, so 29.8% of null sets produced β ≤ −0.021. [src: comprehensive_metal_ecology] The metal-gene set is therefore not distinguishable in overall magnitude from randomly selected conserved gene sets of equal coreness structure. [src: comprehensive_metal_ecology] The report says this contextualises the result without invalidating it: β = −0.021 is part of a pervasive streamlining landscape, and the distinctive finding is the internal functional split. [src: comprehensive_metal_ecology]

### AusMicrobiome replication (P5)

P5 is not an independent replication, because all 482 genera are a subset of P1 and the density predictor is identical. [src: comprehensive_metal_ecology] P5 has β = −0.052 (SE = 0.0063, t = −8.20, p = 2.2×10⁻¹⁵, partial R² = 0.194, ΔAIC = −61.2, λ = 0.734). It confirms the primary direction. [src: comprehensive_metal_ecology] Its β is 2.5× larger than P1 (z ≈ 4.1, p < 0.001), and the report says soil enrichment alone cannot explain the difference. [src: comprehensive_metal_ecology] A separate exploratory z-test gave P5 > P1-full (z = −4.24, p = 2.2×10⁻⁵). P5 also differs from P3-soil (z = −2.29, p = 0.022). [src: comprehensive_metal_ecology]

Exploratory NB21 diagnostics trace the difference to genus composition:
- B_std is identical in both datasets because both use the same MicrobeAtlas Env_Level_1 computation. This rules out a response-variable artefact. [src: comprehensive_metal_ecology]
- Restricting P1 to the 482 shared genera gives β = −0.052 (SE = 0.0063, n = 482), identical to P5. The report attributes the larger β entirely to the continental subset's phylogenetic composition. [src: comprehensive_metal_ecology]
- The AusMicrobiome subset is Proteobacteria-enriched and Firmicutes-depleted. The report says this reduces effective phylogenetic diversity and concentrates the signal. [src: comprehensive_metal_ecology]
- Both P1 and P5 use the same per-Mb density from the same MGnify MAG dataset, so the predictor is consistent by construction. [src: comprehensive_metal_ecology]

The report's likely explanation is that reduced phylogenetic diversity concentrates the signal among closely related specialist/generalist genus pairs and amplifies β. [src: comprehensive_metal_ecology] It reads the lower λ in P5 (0.734 vs 0.757 in P1) as slightly less residual phylogenetic structure after controlling for the predictor. [src: comprehensive_metal_ecology]

### Covariate adjustment

The table gives the effect of each covariate on the metal-gene coefficient. Genome size, GC content, isolation source and dominant biome attenuated it but left it robust, and mean latitude amplified it. [src: comprehensive_metal_ecology]

| Covariate | β magnitude change | Attenuation | p | Class |
|---|---|---|---|---|
| Genome size | 0.021 → 0.011 | 46.7% | 0.006 | Robust, below 50% threshold [src: comprehensive_metal_ecology] |
| GC content | 0.021 → 0.016 | 23.7% | 7.5×10⁻⁵ | Robust [src: comprehensive_metal_ecology] |
| Isolation source | 0.021 → 0.018 | 14.5% | 3×10⁻⁶ | Robust [src: comprehensive_metal_ecology] |
| Mean latitude | 0.021 → 0.031 | −51.8% (amplified) | <10⁻⁴ | Amplified [src: comprehensive_metal_ecology] |
| Dominant biome | 0.021 → 0.020 | 5.8% | <10⁻⁴ | Robust [src: comprehensive_metal_ecology] |

The genome-size result is close to the 50% threshold. The report reads significance after genome-size correction (p = 0.006) as showing the association is not simply a proxy for the small-genome specialist pattern. [src: comprehensive_metal_ecology]

For latitude, the report says adding the covariate increases the coefficient. This is the opposite of confounding, and it indicates collinearity that partially suppresses β in the unadjusted model. [src: comprehensive_metal_ecology] Its interpretation is that metal-gene-rich genera occur disproportionately at lower latitudes, where genera are also more ecologically specialised. [src: comprehensive_metal_ecology] The report hypothesises that higher geochemical heterogeneity and stable climate let narrow-niche specialists persist without metabolic versatility. [src: comprehensive_metal_ecology] Controlling for latitude would then remove a between-latitude composition effect and reveal a stronger within-latitude association. [src: comprehensive_metal_ecology] The report calls this consistent with the streamlining interpretation. [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]] and [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]].

### MAG quality (exploratory, NB22)

MAG quality covariates were mean completeness and mean contamination per genus. They came from kescience_mgnify.genome for n = 1,107 genera with quality metadata. [src: comprehensive_metal_ecology]
- Adding completeness left β(density) = −0.023 (p = 2.9×10⁻⁸), unchanged from baseline. The completeness coefficient was β = −0.003 (p = 0.43, NS, not significant). [src: comprehensive_metal_ecology]
- Adding contamination gave β(density) = −0.023 (p = 5.4×10⁻⁸), with <1.2% change in β. [src: comprehensive_metal_ecology]
- The contamination coefficient was β = +0.007 (p = 0.042), a slight positive association of higher-contamination genera with broader niches. [src: comprehensive_metal_ecology]
- Restricting to high-quality MAGs (completeness ≥ 90%, contamination ≤ 5%, n = 511 genera) gave β = −0.018 (SE = 0.0063, p = 0.005). The report reads this as showing the signal is not driven by low-quality MAGs. [src: comprehensive_metal_ecology]

### Niche-breadth sensitivity (exploratory, NB24)

The NB24 checks tested whether Levins' B_std niche breadth, the response variable, is robust to measurement choices. [src: comprehensive_metal_ecology] For each genus, the report parametrically bootstrapped the mean B_std 100 times. It drew n_otus (operational taxonomic unit) values from N(mean, SD), clipped them to [0, 1], and held single-OTU genera fixed. [src: comprehensive_metal_ecology] The bootstrap mean correlated almost perfectly with the original estimate (Pearson r = 0.99869; max |Δ| per genus = 0.064), and boundary effects in extreme-valued genera drove the largest changes. [src: comprehensive_metal_ecology] Re-running the primary PGLS (phylogenetic generalized least squares) on the bootstrap mean gave β = −0.01987 (SE = 0.00365, p = 6.1×10⁻⁸, λ = 0.756, n = 1,574). This differs from P1 by |Δβ| = 0.00083 (4.0%). [src: comprehensive_metal_ecology] The report concludes the signal is not sensitive to OTU-level aggregation uncertainty. [src: comprehensive_metal_ecology]

## Key Findings: Finding 12 — Two-scale phylo-D framework identifies 13 KOs with …

This part of the report checks whether the primary negative association between metal-gene density and niche breadth holds up under further tests. These tests are sample-depth restrictions, independent niche metrics, within-phylum models and a soil-specialist subset. It also audits the metal gene list structurally and screens the metal genes for horizontal gene transfer (HGT) signals. The audit and the screen do not test the association itself. The association held under every sample-depth threshold and was directionally consistent across phyla. The independent Earth Microbiome Project (EMP) test was nonsignificant. [src: comprehensive_metal_ecology]

### Sample-depth sensitivity

The report worried that genera detected in few MicrobeAtlas samples have less reliable niche-breadth estimates. [src: comprehensive_metal_ecology] Restricting the primary bacterial phylogenetic generalized least squares (PGLS) model to deeper-sampled genera left the estimate unchanged. [src: comprehensive_metal_ecology]

- ≥10 samples: n = 1,572 genera, β = −0.021, SE = 0.00368, p = 1.38×10⁻⁸. [src: comprehensive_metal_ecology]
- ≥20 samples: n = 1,570 genera, β = −0.021, SE = 0.00368, p = 1.69×10⁻⁸. [src: comprehensive_metal_ecology]
- ≥50 samples: n = 1,559 genera, β = −0.021, SE = 0.00370, p = 2.22×10⁻⁸. [src: comprehensive_metal_ecology]

The report concludes that sparse MicrobeAtlas detection does not drive the primary result. [src: comprehensive_metal_ecology]

### Independent niche metrics

The MGnify check agreed only weakly with the primary niche metric. The EMP metric correlated significantly with it, yet its own PGLS was nonsignificant. [src: comprehensive_metal_ecology]

The first check used per-genus Shannon entropy of biome_name across MGnify metagenome-assembled genomes (MAGs), for 1,006 genera with both metrics. [src: comprehensive_metal_ecology] Genera classed as specialists by Levins B_std tended to have lower MAG biome entropy (Spearman ρ = +0.063, p = 0.046). [src: comprehensive_metal_ecology] The distinct-biome-count version was concordant but nonsignificant (ρ = +0.044, p = 0.165). [src: comprehensive_metal_ecology] The report attributes the weak agreement to the expected imprecision of mapping between a 16S survey and MAGs. [src: comprehensive_metal_ecology]

The second check used EMP 16S data. EMP-derived and MicrobeAtlas B_std niche breadth correlated across 539 overlapping genera (Spearman ρ = 0.211, p = 7.7×10⁻⁷). [src: comprehensive_metal_ecology] The report reads this as showing that B_std captures genuine ecological breadth rather than database bias. [src: comprehensive_metal_ecology]

A PGLS on EMP niche breadth (EMPO level-2 habitat categories, 539 genera) gave β = −0.019 (SE = 0.012, p = 0.099, λ = 0.055). This is nonsignificant at α = 0.05. [src: comprehensive_metal_ecology] The report notes that the effect size is virtually identical to the primary estimate (−0.019 vs −0.021). [src: comprehensive_metal_ecology] It suggests that the near-zero λ reflects limited phylogenetic signal in EMPO-2 niche breadth at this coarse resolution. [src: comprehensive_metal_ecology]

### Within-phylum models

The signal appears within clades, not only between them. [src: comprehensive_metal_ecology] PGLS was run within each of the four most speciose bacterial phyla. [src: comprehensive_metal_ecology]

- Proteobacteria: n = 677, λ = 0.778, β = −0.021, 95% CI [−0.031, −0.011], q_BH = 0.00018, significant. [src: comprehensive_metal_ecology]
- Actinobacteria: n = 204, λ = 0.779, β = −0.035, 95% CI [−0.057, −0.014], q_BH = 0.0025, significant. [src: comprehensive_metal_ecology]
- Firmicutes: n = 334, λ = 0.629, β = −0.015, CI [−0.031, +0.000], q_BH = 0.073, borderline and nonsignificant. [src: comprehensive_metal_ecology]
- Bacteroidetes: n = 183, λ = 0.917, β = −0.009, CI [−0.029, +0.011], q_BH = 0.397, nonsignificant. [src: comprehensive_metal_ecology]

All four coefficients are negative. [src: comprehensive_metal_ecology] Heterogeneity across phyla was not significant (Cochran's Q = 3.60, df = 3, p = 0.309, I² = 16.6%). [src: comprehensive_metal_ecology] The report reads this as a signal not confined to one clade and consistent with a common underlying effect. [src: comprehensive_metal_ecology]

### Soil specialists

Among MicrobeAtlas soil-specialist genera (n = 162, defined as more than 50% of OTUs with a soil/agricultural dominant environment), the association strengthened to β = −0.033 (SE = 0.012, p = 0.007, λ = 0.471). [src: comprehensive_metal_ecology] The report calls this consistent with the predecessor project's MicrobeAtlas result (β = −0.023, n = 603, p = 0.0002). [src: comprehensive_metal_ecology] It proposes that soil's greater chemical complexity and metal heterogeneity, relative to the global MGnify MAG corpus, likely explains the stronger effect. [src: comprehensive_metal_ecology]

### Structural audit of the gene list

A structural audit of all 140 primary KEGG orthologs (KOs) used KEGG representational state transfer (REST), UniProt and InterPro application programming interface (API) lookups. It confirmed metal-binding clan membership or metal-binding singleton Pfams for 10/140 KOs (7.1%). [src: comprehensive_metal_ecology] The clans were HMA CL0704, 4Fe-4S CL0344, Fer2/2Fe-2S CL0486, C2H2-zf CL0361 and MBB CL0193. [src: comprehensive_metal_ecology]

The remaining 130 KOs had Pfam annotations but no metal-coordination clan. [src: comprehensive_metal_ecology] Of these, 113 carry ATP-binding cassette (ABC) transporter scaffolds (PF00005/PF00950/PF01032), MerR/CusR/ZntR sensor Pfams and outer-membrane efflux proteins. The report calls these mechanistically correct metal-processing proteins whose domains are substrate-binding or transport scaffolds. [src: comprehensive_metal_ecology]

Two examples lack clan evidence. ZnuA (K02035) is a Zn²⁺ ABC importer substrate-binding component with PF13377/PF12838 Zn-binding clusters but no curated metal-binding clan. [src: comprehensive_metal_ecology] MntH (K03322) is a Mn²⁺/Fe²⁺ NRAMP transporter with a PF07690 MFS scaffold and no metal-coordination motif in its Pfam record. [src: comprehensive_metal_ecology] The report treats this as an annotation gap for substrate-binding metal transporters, not a gene-list problem. [src: comprehensive_metal_ecology] It concludes that the pattern validates the gene-list architecture. [src: comprehensive_metal_ecology]

### HGT signal of metal genes

The report used two scales. Genome-level Fritz & Purvis D was computed on a GTDB 18,961-tip tree for 309 KOs with ≥20 genomes. D = 1 is random/HGT-like and D = 0 is Brownian/vertical. [src: comprehensive_metal_ecology] Genus-level PGLS Pagel's λ was computed for 275 KOs. λ = 1 is strong phylogenetic signal and λ = 0 is none. [src: comprehensive_metal_ecology]

Across the 275 shared KOs, D and λ were weakly and nonsignificantly negatively correlated (Spearman ρ = −0.041, p = 0.49). The report reads them as partially independent signals. [src: comprehensive_metal_ecology] Thirteen KOs met the double-signal criterion of D > 0.2 and λ < 0.3. [src: comprehensive_metal_ecology]

- nrsD (K07785, Resistance): D = 0.821, λ = 0.089, n = 59 genomes. [src: comprehensive_metal_ecology]
- merE (K19059, Resistance): D = 0.728, λ = 0.102, n = 154. [src: comprehensive_metal_ecology]
- merD (K19057, Resistance): D = 0.701, λ = 0.165, n = 156. [src: comprehensive_metal_ecology]
- gesB (K19594, Resistance): D = 0.597, λ = 0.156, n = 89. [src: comprehensive_metal_ecology]
- aoxB (K08356, Resistance): D = 0.562, λ = 0.000, n = 259. [src: comprehensive_metal_ecology]
- gesA (K19595, Resistance): D = 0.458, λ = 0.161, n = 103. [src: comprehensive_metal_ecology]
- shp (K25119, Resistance): D = 0.385, λ = 0.000, n = 123. [src: comprehensive_metal_ecology]
- iucD (K03897, Other): D = 0.354, λ = 0.237, n = 362. [src: comprehensive_metal_ecology]
- golS (K19592, Sensing): D = 0.265, λ = 0.135, n = 144. [src: comprehensive_metal_ecology]
- doxDA (K05908, Other): D = 0.254, λ = 0.000, n = 241. [src: comprehensive_metal_ecology]
- norB (K08170, Other): D = 0.239, λ = 0.033, n = 315. [src: comprehensive_metal_ecology]
- nicC (K14974, Transport): D = 0.224, λ = 0.000, n = 382. [src: comprehensive_metal_ecology]
- nikB (K15585, Transport): D = 0.202, λ = 0.000, n = 448. [src: comprehensive_metal_ecology]

See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]] and [[concepts/robustness-and-replication-of-niche-breadth-associations]] for related evidence.

## Key Findings: Finding 14 — Per-KO environmental drivers: emrB shows broadest multi-metal …

Metal-gene density predicts narrower pH and composite environmental niches but not temperature range, and it predicts more co-occurrence partners, though that last association is not independent of niche breadth. [src: comprehensive_metal_ecology] This part also closes the phylo-D framework and reports an exploratory per-KO driver analysis. KO means KEGG ortholog. [src: comprehensive_metal_ecology]

### Phylo-D framework: what the double-signal KOs are

All 13 double-signal KOs fall in resistance, transport or sensing categories. None is a cofactor biosynthesis KO, which the report reads as consistent with cofactor genes being constitutively required and vertically inherited. [src: comprehensive_metal_ecology] The high-λ control KOs (cusA, cusC, cobN, cobT, zntR, oprJ, mexI, cnrR, cbiH60, fre) all have λ > 0.7 and D < 0.3. They are dominated by metal homeostasis and cofactor-related genes. [src: comprehensive_metal_ecology] The report also proposes that resistance genes with the highest D values are the most likely to be horizontally acquired. It presents this as a gene-level complement to its class-level null for resistance genes, and it says this further decouples gene abundance from ecological specialisation history. [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

### Environmental-axis niche breadth (exploratory)

The report labels this PGLS (phylogenetic generalized least squares) analysis exploratory. [src: comprehensive_metal_ecology] The predictor is z-scored primary KO density (ko_per_mb_primary_z), as in P1. [src: comprehensive_metal_ecology] Genus pH niche width is max(soil pH) − min(soil pH) across MicrobeAtlas 16S sampling sites. [src: comprehensive_metal_ecology] Temperature range is the max − min of mean annual temperature across sites. The composite gradient is the first principal component of standardised pH, temperature and precipitation site coordinates. [src: comprehensive_metal_ecology]

| Response | n genera | β | SE | p | λ |
|---|---|---|---|---|---|
| Temperature range (°C) [src: comprehensive_metal_ecology] | 1,195 | +0.079 | 0.886 | 0.929 | — |
| Soil pH niche width (pH units) [src: comprehensive_metal_ecology] | 1,195 | −0.760 | 0.233 | 0.001 | 0.11 |
| Composite environmental gradient [src: comprehensive_metal_ecology] | 1,172 | −0.064 | 0.017 | <0.001 | — |

The report calls the composite result the strongest, narrower across all axes. [src: comprehensive_metal_ecology] It proposes that pH-dependent metal speciation (for example Cr(VI)/Cr(III) redox and Cu²⁺/CuOH⁺ hydrolysis) constrains metal-specialist genera to pH conditions where their genes give effective homeostasis. [src: comprehensive_metal_ecology] It attributes temperature tolerance mainly to membrane composition and chaperone repertoire rather than metal processing. [src: comprehensive_metal_ecology] These are interpretations, not tests.

The report links the pH signal to its GeoROC finding: Cr and Co bedrock enrichment, both associated with mafic geology, positively predicts niche breadth after controlling for metal genes. [src: comprehensive_metal_ecology] It suggests that pH and mafic geology may reflect a shared soil-chemistry axis. Serpentine/ultramafic soils are Mg/Ca-rich, Ca-dominated and often alkaline. [src: comprehensive_metal_ecology] Pagel's λ for pH niche (0.11–0.20) is much lower than for Levins' B_std (0.757). The report reads this as environmental-axis niches being shaped mostly by ecology rather than phylogeny. [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].

### Per-KO environmental drivers (exploratory)

Per-KO signals are modest and uneven across KOs. The analysis tested the frequency of 9 TIER1 KOs detectable in the KBase Data Lakehouse pangenome against 22 environmental niche-breadth responses. These responses are metal concentrations from GeoROC, NGSA-ICP and NGSA-MMI, and the report labels the analysis exploratory. [src: comprehensive_metal_ecology] Of 198 models (9 KOs × 22 responses), 32 were significant at p < 0.05 (16.2%) and 28 at FDR q < 0.1 (FDR = false discovery rate). [src: comprehensive_metal_ecology]

| KO | Gene | Significant responses | Strongest association |
|---|---|---|---|
| K03446 [src: comprehensive_metal_ecology] | emrB | 11 | Ni (GeoROC), β = 8.45, t = 5.01, p = 6.0×10⁻⁷ |
| K17686 [src: comprehensive_metal_ecology] | copA | 8 | — |
| K07787 [src: comprehensive_metal_ecology] | cusA | 6 | Hg (NGSA-MMI), t = 3.14, p = 0.002 |
| K07785 [src: comprehensive_metal_ecology] | nrsD | 3 | Cr (NGSA-MMI), t = 4.36, p = 1.4×10⁻⁵ |
| K07665 [src: comprehensive_metal_ecology] | cusR | 2 | — |
| K03325 [src: comprehensive_metal_ecology] | ACR3 | 1 | — |
| K15726 [src: comprehensive_metal_ecology] | czcA | 1 | — |
| K19594 [src: comprehensive_metal_ecology] | gesB | 0 | — |
| K19595 [src: comprehensive_metal_ecology] | gesA | 0 | — |

KO–metal pairs matching the annotated target metal had higher t-statistics than mismatched pairs (matched mean t = 0.263 vs mismatched mean t = −0.253; Mann-Whitney U test p = 0.035). The report calls this a modest metal-specific signal. [src: comprehensive_metal_ecology] The top performer, emrB, is a multi-drug efflux pump with broad substrate range, annotated as a Cu/Tl transporter. [src: comprehensive_metal_ecology] The report suggests its diverse metal associations reflect broad efflux selectivity rather than primary metal resistance. It also suggests its prevalence may track metal-stress environments non-specifically. [src: comprehensive_metal_ecology] See [[entities/efflux-pumps]].

Six TIER1 KOs are absent from the pangenome database: cusB/K07798, merR/K08365, czcC/K15725, czcB/K15727, czcD/K16264 and cueR/K19591. They include core Cu efflux and Hg sensing components, which limits interpretation of per-KO environmental specificity. [src: comprehensive_metal_ecology]

### Co-occurrence networks (exploratory)

Networks came from MicrobeAtlas (3,149–3,389 genera), using hypergeometric tests (Veech 2013, FDR < 5%) and phi coefficients. [src: comprehensive_metal_ecology] The strata were all samples (n = 462,716), environmental (n = 382,483) and soil (n = 162,022). [src: comprehensive_metal_ecology] Z-scored ko_per_mb_primary was regressed against positive partner counts per genus with PGLS. [src: comprehensive_metal_ecology]

| Stratum | Genera (full → analysed) | β | SE | t | p | λ |
|---|---|---|---|---|---|---|
| ALL [src: comprehensive_metal_ecology] | 3,389 → 1,572 | 138.4 | 13.7 | 10.08 | 3.4×10⁻²³ | 0.599 |
| ENV [src: comprehensive_metal_ecology] | 3,382 → 1,572 | 134.0 | 13.8 | 9.74 | 8.5×10⁻²² | 0.625 |
| SOIL [src: comprehensive_metal_ecology] | 3,149 → 1,547 | 210.5 | 15.3 | 13.78 | 8.2×10⁻⁴¹ | 0.570 |

Weighted phi-degree was also significant in all three strata (β = 15.2–16.5, p = 3.5×10⁻³²–9.9×10⁻³²). [src: comprehensive_metal_ecology] So were negative partners (all β = 27–45, p = 1.6×10⁻⁵–2.2×10⁻⁴). [src: comprehensive_metal_ecology] Soil had the strongest positive-partner effect. The report describes it as a 2.5× larger β than the all-sample stratum. [src: comprehensive_metal_ecology] The tabulated coefficients (210.5 vs 138.4) do not match that ratio, and the report gives no reconciliation. [src: comprehensive_metal_ecology] Soil's negative-partner β was lower (soil 27.4 vs all 39.5 vs env 45.3). [src: comprehensive_metal_ecology] The report reads this, together with the P1 soil enrichment (Finding 10; β = −0.033, p = 0.007), as suggesting that metal-gene-rich genera sit in more cooperative, less competitive soil networks. [src: comprehensive_metal_ecology] See [[concepts/co-occurrence-network-structure-and-metal-tolerance-guilds]].

Two caveats limit these results. First, B_std correlates with positive partner count (Spearman ρ = 0.33–0.37, p < 10⁻⁴⁰). The association is therefore not independent of the primary P1 predictor, and partial analyses controlling for B_std are needed. [src: comprehensive_metal_ecology] Second, all strata were extremely dense (38–42% significant positive pairs, mean ≥ 1,200 partners per genus). [src: comprehensive_metal_ecology] Clustering coefficients, betweenness centrality and MPD/SES analysis were precluded because these metrics degenerate in near-complete networks. [src: comprehensive_metal_ecology] The positive-partner signal reflects relative enrichment within a near-saturated network, not exclusive associations. Weighted phi-degree and partner count remain informative. [src: comprehensive_metal_ecology]

## Key Findings: Finding 17 — Direct genomic evidence for HGT is concentrated in resistance …

This part of the report shows that, in soil, partners of metal-gene-rich genera carry more metal genes than partners of matched controls. It then gives an exploratory horizontal gene transfer (HGT) analysis of double-signal metal KOs (KEGG orthologs). The partner result is supported by several tests. The HGT evidence is mixed, and the plasmid tests are marginal and underpowered. [src: comprehensive_metal_ecology]

### Soil partners of metal-gene-rich genera

The top-50 soil focal genera by ko_per_mb_primary (mean = 20.32 ko/Mb) were compared with 50 controls of similar ko/Mb (±0.5 SD of median = 7.95, phylum-matched). SD is standard deviation. [src: comprehensive_metal_ecology] Strong partners were defined as φ > 0.3. Only 0.91% of significant positive pairs passed this cutoff, which the report reads as a network nearly saturated for moderate associations. [src: comprehensive_metal_ecology]

Partners of the top-50 focal genera had higher metal-gene density than partners of controls. [src: comprehensive_metal_ecology]

| Metric | Top-50 focal | Control-50 | Claim |
|---|---|---|---|
| Mean partner ko/Mb | 12.776 ± 3.884 | 8.903 ± 1.792 | [src: comprehensive_metal_ecology] |
| % partners in top quartile | 56.1% | 26.3% | [src: comprehensive_metal_ecology] |
| Dominant partner phylum | Firmicutes (40.4%) | Proteobacteria (39.9%) | [src: comprehensive_metal_ecology] |

The Mann-Whitney U (MWU) test for partner ko/Mb (top-50 > control-50) gave U = 2005, p = 1.98×10⁻⁷. [src: comprehensive_metal_ecology] Partner phylum distributions also differed (χ² = 113.74, p = 2.77×10⁻¹³). [src: comprehensive_metal_ecology] Across all 100 genera, focal ko/Mb correlated with mean partner ko/Mb (Spearman ρ = 0.604, p = 2.82×10⁻¹¹). [src: comprehensive_metal_ecology]

The Firmicutes bias stands out. Proteobacteria make up 43% of genera in the full PGLS (phylogenetic generalized least squares) table, yet metal-gene-rich focal genera associated preferentially with Firmicutes in soil. [src: comprehensive_metal_ecology] The report offers a metal-tolerance guild interpretation. It notes that Firmicutes such as Bacillus and Clostridium are well represented in metal-contaminated soils and carry substantial metal-resistance gene arsenals. [src: comprehensive_metal_ecology]

The guild is not strictly assortative. Within the top-50 genera the correlation was weaker (ρ = 0.284, p = 0.045) than across all 100 (ρ = 0.604). Some high-KO focal genera still associate with lower-KO partners. [src: comprehensive_metal_ecology] See [[concepts/co-occurrence-network-structure-and-metal-tolerance-guilds]].

### Exploratory HGT evidence for double-signal KOs

The report characterised 13 double-signal KOs (D > 0.2, λ < 0.3) along four evidence lines, against 10 high-λ control KOs (λ > 0.7, D < 0.3). [src: comprehensive_metal_ecology]

**Phylogenetic randomness (D).** Double-signal KOs had a higher Fritz & Purvis D than controls (median 0.385 vs −0.077; MWU U = 123, p = 1.81×10⁻⁴). [src: comprehensive_metal_ecology] The report treats this as its strongest HGT evidence. D was measured on the same GTDB tree used for the primary PGLS, and it reflects genome-level phylogenetic randomness equivalent to gene-tree/species-tree discordance. [src: comprehensive_metal_ecology]

**Plasmid fractions.** Double-signal resistance KOs had higher plasmid fractions than background resistance KOs in both databases. [src: comprehensive_metal_ecology]
- NCBI Entrez: n = 3 vs background n = 51, medians 0.0042 vs 0.0004, p = 0.045. The three KOs were merD 4.3%, aoxB 0.4% and norB 0.1%. [src: comprehensive_metal_ecology]
- BV-BRC (84,446 plasmid accessions): n = 2 (merD 7.2%, norB 0.3%) vs background n = 48 after arsC KO deduplication, medians 0.0049 vs 0.0005, p = 0.044. [src: comprehensive_metal_ecology]

The report calls this marginal significance. It is driven mainly by merD (Tn21-family mer operon) and is underpowered because few double-signal resistance KOs have n ≥ 50. [src: comprehensive_metal_ecology] gesA, gesB (n = 1 in both databases) and nrsD (n = 16) are untestable. [src: comprehensive_metal_ecology] golS is effectively chromosomal in both databases (NCBI fraction 0.000017) despite meeting the threshold, and the report suggests its HGT may have occurred chromosomally. [src: comprehensive_metal_ecology] High-plasmid background KOs (pcoB 6.8%, merA 4.5%, tetA 4.1%) fail the D or λ threshold, which makes the test conservative. [src: comprehensive_metal_ecology] For merD, see [[entities/mercury-resistance-mer-genes]].

**Mobile elements.** NCBI mobile-element co-annotation was directionally consistent but not significant (double-signal n = 13 vs control n = 10; MWU p = 0.062). Both medians were 0.000. [src: comprehensive_metal_ecology]

**Environmental enrichment (MGnify).** 5 of 8 double-signal KOs with MGnify data were significant for environmental metal enrichment at FDR (false discovery rate) q < 0.1. [src: comprehensive_metal_ecology] The q values were:
- nicC, 5.6×10⁻⁵ [src: comprehensive_metal_ecology]
- nikB, 2.8×10⁻⁵ [src: comprehensive_metal_ecology]
- gesA, 9.4×10⁻⁵ [src: comprehensive_metal_ecology]
- iucD, 1.1×10⁻⁴ [src: comprehensive_metal_ecology]
- norB, 7.1×10⁻² [src: comprehensive_metal_ecology]

Median |ρ| between double-signal KO presence and bioavailable metals was 0.034 (Spearman). [src: comprehensive_metal_ecology] Five double-signal KOs (nrsD, merE, merD, shp, doxDA) were absent from the MGnify dataset and could not be assessed. [src: comprehensive_metal_ecology]

### Plasmid fraction across functional categories

NCBI plasmid fractions were higher for resistance KOs than for other categories. Resistance KOs (n = 54, median 0.00043) exceeded metal-dependent metabolism KOs (n = 14, median 0.00016; MWU p = 0.023). They also exceeded all non-resistance KOs (n = 86, median 0.00022; p = 0.020). [src: comprehensive_metal_ecology] The analysis queried all 275 metal KOs and restricted comparisons to n_total ≥ 50. [src: comprehensive_metal_ecology]

| Category (NCBI Entrez) | n | Median plasmid_frac | Claim |
|---|---|---|---|
| Resistance/Detoxification | 54 | 0.00043 | [src: comprehensive_metal_ecology] |
| Transport/Homeostasis | 48 | 0.00021 | [src: comprehensive_metal_ecology] |
| Sensing/Regulation | 21 | 0.00020 | [src: comprehensive_metal_ecology] |
| Metal-dependent Metabolism | 14 | 0.00016 | [src: comprehensive_metal_ecology] |
| Cofactor Biosynthesis | 2 | 0.00012 | [src: comprehensive_metal_ecology] |

Only hemH and MOCS2B met n ≥ 50 in the cofactor group. cobC1 (n = 45) and ahbAB (n = 2) were excluded. [src: comprehensive_metal_ecology] The resistance-versus-cofactor comparison was underpowered and not significant (p = 0.082). [src: comprehensive_metal_ecology] The report reads cofactor plasmid fractions ≤ 0.023% as consistent with strict chromosomal location. [src: comprehensive_metal_ecology] It says the gradient (resistance > transport ≈ sensing > metabolism > cofactor) mirrors the λ ordering. [src: comprehensive_metal_ecology]

The BV-BRC cross-category comparison did not replicate the NCBI difference. Resistance (n = 51) and non-resistance KOs (n = 82) had medians of 0.00057 and 0.00052 (p = 0.118). [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

## Key Findings; Discoveries

This part of the report covers the main niche-breadth result, the split between resistance and cofactor genes, the plasmid and horizontal gene transfer (HGT) checks, and several exploratory analyses. Metal-gene density tracks narrower niche breadth, but the signal is part of a broad genome-streamlining pattern. Resistance genes carry none of it. [src: comprehensive_metal_ecology]

### Niche breadth and genome streamlining

Across 1,574 bacterial genera, per-Mb density of 140 Tier 1+2 metal KOs (KEGG orthologs) negatively predicts standardised Levins' niche breadth (β = −0.021, FDR (false discovery rate) p = 6.4×10⁻⁸, PGLS (phylogenetic generalized least squares) Pagel's λ = 0.757). The result survives correction for genome size, GC content, isolation source and dominant biome. [src: comprehensive_metal_ecology] The effect is uniform across 9 metals (Tl, Fe, Ni, Zn, Al, Co, S, Cu, Mn), all FDR-significant. The report reads this as a general genomic specialisation strategy. [src: comprehensive_metal_ecology]

The signal is not metal-specific. 14/19 KEGG functional categories show significantly negative per-Mb density associations with niche breadth (β range −0.035 to −0.010). [src: comprehensive_metal_ecology] The metal-gene β sits in the lower-middle of that landscape, 30–60% weaker than the housekeeping baseline. [src: comprehensive_metal_ecology] A coreness-matched permutation test (NB20, 1,000 sets) finds the overall β unexceptional (emp_p = 0.298). The report therefore treats the association as part of pervasive streamlining. [src: comprehensive_metal_ecology]

### Resistance versus cofactor genes

Within the metal set, resistance/detoxification genes (106 KOs) show no association (β ≈ 0, p = 0.66). [src: comprehensive_metal_ecology] Cofactor biosynthesis (7 KOs, Fe–S cluster/molybdopterin) shows the strongest signal (β = −0.033, FDR p = 5.2×10⁻⁹), equal to the housekeeping baseline. [src: comprehensive_metal_ecology] The report states that this contrast is not a general feature of functionally heterogeneous gene categories. [src: comprehensive_metal_ecology]

Two tests support the split. Its magnitude (Δβ = 0.035259) exceeds all 1,000 random partitions of matching size (p < 0.001, NB25). [src: comprehensive_metal_ecology] The cofactor signal also survives removal of any single KO. All 4 KOs stay stable, with β from −0.016 to −0.029 and all p < 0.001 (NB26 jackknife). [src: comprehensive_metal_ecology]

### HGT and plasmid evidence

An exploratory framework combines genome-level Fritz & Purvis D with genus-level Pagel's λ across 275 overlapping KOs. It identifies 13 "double-signal" genes (D > 0.2, λ < 0.3) as the most likely HGT-mobile subset. [src: comprehensive_metal_ecology] D and λ are near-orthogonal (Spearman ρ = −0.041, p = 0.49). The report says this shows they capture independent signals. [src: comprehensive_metal_ecology] All 13 double-signal KOs are resistance, transport or sensing genes. [src: comprehensive_metal_ecology] No cofactor biosynthesis KO is among them, which the report considers consistent with constitutive vertical inheritance. [src: comprehensive_metal_ecology] The report concludes that HGT-mobile resistance genes are decoupled from ecological specialisation at both the category level and the individual-KO level. [src: comprehensive_metal_ecology]

The BV-BRC plasmid cross-category dataset has 154 rows (66 original resistance KOs plus 88 non-resistance KOs). Large-n genes were estimated by 4-page sampling. [src: comprehensive_metal_ecology] Restricted to n≥50, median plasmid fractions were:

- Resistance/Detoxification: n = 51, median fraction 0.00057. [src: comprehensive_metal_ecology]
- Transport/Homeostasis: n = 46, median fraction 0.00052. [src: comprehensive_metal_ecology]
- Sensing/Regulation: n = 21, median fraction 0.00055. [src: comprehensive_metal_ecology]
- Metal-dependent Metabolism: n = 12, median fraction 0.00033. [src: comprehensive_metal_ecology]
- Cofactor Biosynthesis: n = 2, median fraction 0.00035. [src: comprehensive_metal_ecology]

The cofactor row rests on only hemH (n=346,821) and cobT. Four other cofactor KOs were excluded. [src: comprehensive_metal_ecology]

The plasmid enrichment of resistance genes was not significant in this dataset. The one-sided Mann-Whitney test against all non-resistance KOs gave U=2347, p=0.118 (n=51 vs n=82). [src: comprehensive_metal_ecology] Against individual categories, p was 0.129 for Metabolism, 0.103 for Sensing and 0.271 for Transport. [src: comprehensive_metal_ecology] The confirmatory double-signal versus background resistance test gave U=84, p=0.047 (n=2 vs n=49), consistent with the original focused test p=0.044. [src: comprehensive_metal_ecology] The comparison does not replicate the NCBI p=0.020 signal. [src: comprehensive_metal_ecology] The report attributes this partly to BV-BRC Transport/Homeostasis containing functional resistance genes (aph at 7.1%, and czcA/czcB), which collapses the Transport–Resistance median gap. [src: comprehensive_metal_ecology] It also says sampling estimates for large-n genes add noise. [src: comprehensive_metal_ecology]

### Exploratory environmental and community analyses

**pH, temperature and composite gradient.** PGLS finds that per-Mb metal-gene density predicts narrower pH niche width (β = −0.760, p = 0.001; λ = 0.11). [src: comprehensive_metal_ecology] It also predicts the composite environmental gradient (β = −0.064, p < 0.001). [src: comprehensive_metal_ecology] It does not predict temperature niche (p = 0.929). [src: comprehensive_metal_ecology] The report attributes the pH specificity to pH-dependent metal speciation. It notes that the temperature null contrasts with its primary thermal-stability framework. [src: comprehensive_metal_ecology]

**Community variance partitioning (NB28).** This analysis partitioned centered log-ratio (CLR) abundances of the top-200 genera in 5,000 subsampled MicrobeAtlas samples across metals (Cu, Zn, Pb, Ni log-ppm) and pH+climate axes. [src: comprehensive_metal_ecology] All environmental variables together explain R²=0.110. [src: comprehensive_metal_ecology] Unique metals conditional on pH+climate explain R²=0.064, against R²=0.041 for unique pH+climate and R²=0.005 shared. [src: comprehensive_metal_ecology] The metal-unique fraction is 58% larger, which the report calls a reversal of the conventional expectation that pH dominates. [src: comprehensive_metal_ecology] The R² values are unadjusted, come from a linear model, and were not permutation-tested, so the report reads them descriptively. [src: comprehensive_metal_ecology]

**Environmental prediction (NB29).** XGBoost with spatial 5-fold block cross-validation (CV) predicted community weighted mean (CWM) metal-gene density (trait mean=12.7, SD (standard deviation)=8.2) from environmental variables. [src: comprehensive_metal_ecology] Held-out performance was poor. Mean CV RMSE (root mean square error) was 11.89 (Block 0=19.37 to Block 3=6.20), comparable to the within-sample SD. [src: comprehensive_metal_ecology] Cu+Zn+Pb+Ni contribute 45.9% of mean |SHAP| (Shapley additive explanations), and log_Ni_ppm is the top predictor (mean |SHAP|=2.23). [src: comprehensive_metal_ecology] The report reads this as consistent with NB28: metals structure communities, but spatial heterogeneity limits transfer across regions. [src: comprehensive_metal_ecology] It calls the hypothesis only partially supported, because predictive power is low (RMSE ≈ SD). [src: comprehensive_metal_ecology]

**Co-occurrence partners.** PGLS of positive partner count on metal-gene KO density gives β = 138.4–210.5 across ALL/ENV/SOIL strata (all p < 3.4×10⁻²²). [src: comprehensive_metal_ecology] The soil effect (β = 210.5, p = 8.2×10⁻⁴¹) is 2.5× the all-strata effect. The report says this converges with the stronger primary PGLS signal in soil specialists. [src: comprehensive_metal_ecology] All three networks are near-saturated (38–42% significant positive pairs), which makes clustering and betweenness metrics degenerate. [src: comprehensive_metal_ecology]

## Discoveries; Results

This part of the report covers four things: soil co-occurrence partners, horizontal transfer and plasmid signals, the main confirmatory tests of metal-gene density against niche breadth, and sensitivity and replication checks. The primary bacterial test is significant. Several replications are null or only directionally consistent. [src: comprehensive_metal_ecology]

### Soil partners (exploratory)

Partners of metal-gene-rich soil genera look like a metal-tolerance guild, but the analysis is exploratory. Top-50 soil focal genera (mean 20.32 ko/Mb) attract partners with higher mean KEGG ortholog (KO) density than controls (12.776 vs 8.903 ko/Mb; Mann-Whitney U (MWU) p = 1.98×10⁻⁷). [src: comprehensive_metal_ecology] Of these partners, 56.1% sit in the top KO-density quartile, against 26.3% for controls. The report calls this consistent with a metal-tolerance guild assembly pattern. [src: comprehensive_metal_ecology] Partner phyla shift from Proteobacteria dominance in controls to Firmicutes, which make up 40.4% of focal partner instances (χ² = 113.74, p = 2.77×10⁻¹³). [src: comprehensive_metal_ecology] See [[concepts/co-occurrence-network-structure-and-metal-tolerance-guilds]].

### Horizontal transfer and plasmids

Double-signal KOs show more transfer-like and plasmid-linked behaviour than background genes. The report treats the HGT (horizontal gene transfer) analysis as exploratory. [src: comprehensive_metal_ecology]

- D-statistics are higher in double-signal KOs than in high-λ controls (MWU p = 1.81×10⁻⁴; median 0.385 vs −0.077). [src: comprehensive_metal_ecology]
- Among resistance-subcategory KOs with n_total ≥ 50, NCBI Entrez plasmid fractions are enriched in double-signal resistance KOs (n=3: merD 4.3%, aoxB 0.4%, norB 0.1%) against background resistance (n=51; MWU p = 0.045). [src: comprehensive_metal_ecology]
- Independent BV-BRC validation gives p = 0.044 (n_double=2, n_background=48, arsC deduplicated). [src: comprehensive_metal_ecology] The within-BV-BRC comparison gives p=0.047, which the report calls confirmatory. [src: comprehensive_metal_ecology]
- Across all 275 KOs with n_total ≥ 50 in NCBI, resistance exceeds metal-dependent metabolism (MWU p=0.023) and all non-resistance KOs (MWU p=0.020). [src: comprehensive_metal_ecology]
- The BV-BRC cross-category comparison (154 rows) is not significant (p=0.118). The report attributes this to resistance-classified metal efflux genes inflating the transport category. [src: comprehensive_metal_ecology]
- Cofactor biosynthesis KOs have near-zero plasmid fractions in both databases (hemH ≤ 0.07%). [src: comprehensive_metal_ecology]
- The NCBI gradient (resistance > transport ≈ sensing > metabolism > cofactor) mirrors the phylogenetic λ signal gradient. [src: comprehensive_metal_ecology]
- All 13 double-signal KOs are resistance, transport or sensing genes, and none is cofactor biosynthesis. [src: comprehensive_metal_ecology]
- Of the double-signal KOs with MGnify data, 5/8 show significant metal-environment associations at FDR q < 0.1. [src: comprehensive_metal_ecology]

The double-signal plasmid tests rest on very few KOs (n=3 NCBI, n=2 BV-BRC). [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

### Confirmatory tests

The primary bacterial test supports the hypothesis that metal-gene density is negatively associated with niche breadth. The archaeal and Australian tests do not reach significance. [src: comprehensive_metal_ecology]

| Test | n | λ | β | Raw p | Joint-FDR p | Outcome |
|---|---|---|---|---|---|---|
| P1 Bacteria (140 KOs) | 1,574 | 0.757 | −0.021 | 2.1×10⁻⁸ | 6.4×10⁻⁸ | significant [src: comprehensive_metal_ecology] |
| P2 Archaea (140 KOs) | 95 | 0.726 | −0.014 | 0.119 | 0.178 | NS, directionally consistent [src: comprehensive_metal_ecology] |
| P3 NGSA/Australia | 482 | 0.346 | −0.002 | 0.755 | 0.755 | NS, near-zero [src: comprehensive_metal_ecology] |

### Sensitivity checks

Most sensitivity variants agree with the primary result, and the BacMet-only set is borderline. The report applies no within-family multiplicity correction to these raw p-values. [src: comprehensive_metal_ecology]

- Alternative KO sets: the all-non-ambiguous set (444 KOs, 1,073 genera) gives β = −0.027, p = 5.0×10⁻⁸. [src: comprehensive_metal_ecology] The BacMet-only set (188 KOs) gives β = −0.011, p = 0.050, which is borderline. [src: comprehensive_metal_ecology]
- Tree and sample variants: λ = 0 gives β = −0.032 (stronger). [src: comprehensive_metal_ecology] λ = 1 gives β = −0.018, p = 3.7×10⁻⁶. [src: comprehensive_metal_ecology] Minimum n of 50 or 150 gives identical results (β = −0.021, p = 2.1×10⁻⁸). [src: comprehensive_metal_ecology]
- Archaea with min n=5: β = −0.018, p = 0.084, which is directionally consistent but underpowered. [src: comprehensive_metal_ecology]
- Raw Levins' B gives β = −0.286, p = 1.1×10⁻¹¹. [src: comprehensive_metal_ecology]
- Region and habitat: Australia only gives β = −0.002, p = 0.755, directionally consistent but null. [src: comprehensive_metal_ecology] The Northern hemisphere gives β = −0.030, p = 3.2×10⁻⁶. [src: comprehensive_metal_ecology] Soil-restricted gives β = −0.033, p = 0.007. [src: comprehensive_metal_ecology]

The primary set (Tier 1+2) has 140 KOs in 1,574 genera. [src: comprehensive_metal_ecology]

### Replication with soil metal concentrations and other datasets

Replication is partial. In P4 (n = 482), copper and zinc concentrations are significant after Benjamini-Hochberg false discovery rate (BH-FDR) correction. Lead, nickel and cobalt are not. [src: comprehensive_metal_ecology]

- Cu: β = −0.011, p = 0.016 (q=0.041), λ = 0.319. [src: comprehensive_metal_ecology]
- Zn: β = −0.011, p = 0.016 (q=0.041), λ = 0.318. [src: comprehensive_metal_ecology]
- Pb: β = −0.009, p = 0.034 (q=0.057). [src: comprehensive_metal_ecology]
- Ni: β = −0.009, p = 0.049 (q=0.061). [src: comprehensive_metal_ecology]
- Co: β = +0.001, p = 0.776, in the wrong direction. [src: comprehensive_metal_ecology]

The report classifies P4 as partial replication, with λ = 0.32–0.35, substantially lower than P1. [src: comprehensive_metal_ecology]

The Earth Microbiome Project (EMP) 16S replication (n = 539) gives β = −0.019, p = 0.099, which is not significant but directionally consistent. [src: comprehensive_metal_ecology] The ENIGMA field-site analysis (29 MAGs, 3 wells) gives ρ = −0.41, p = 0.029. The report deems it uninformative because of a data coverage failure. [src: comprehensive_metal_ecology]

P5 restricts the phylogenetic generalized least squares (PGLS) model to the 482 AusMicrobiome genera. It gives β = −0.052 (SE = 0.0063, t = −8.20, p = 2.2×10⁻¹⁵, partial R² = 0.194, ΔAIC vs null = −61.2, λ = 0.734). [src: comprehensive_metal_ecology] This effect is 2.5× larger than P1 and consistent in direction with EMP. It differs from P1 with z ≈ 4.1, p < 0.001. [src: comprehensive_metal_ecology] The report suggests that reduced phylogenetic diversity in the continental subset likely explains the larger β. [src: comprehensive_metal_ecology] It classifies P5 as consistent within-dataset, not independent replication, because the 482 genera are a subset of P1 with the same density predictor. [src: comprehensive_metal_ecology] See [[concepts/robustness-and-replication-of-niche-breadth-associations]].

## Results: Negative controls

This part of the report asks whether geological proxies and a series of permutation, control and sensitivity tests support the metal-gene density association with niche breadth. The ore-deposit cross-reference is exploratory and null. The main association survives a predictor permutation test and quality restrictions, but it is not distinguishable from coreness-matched KO sets (KO = KEGG ortholog). [src: comprehensive_metal_ecology]

### Ore-deposit proximity (exploratory)

Cross-referencing KO density against ore-deposit proximity (CMMI database, n = 18–19 regions) gave weak, non-significant correlations. The report calls this exploratory only. Copper gave r = 0.34 (p = 0.17), zinc r = 0.34 (p = 0.17) and lead r = 0.01 (p = 0.99). [src: comprehensive_metal_ecology]

### Is the overall association distinct from null expectations?

The predictor permutation test (n = 1,000) supports a real association. The null β had mean ≈ 0 and SD (standard deviation) = 0.0029. The observed β = −0.0207 lay 7.14 SD below the null mean, with empirical p = 0/1000 (< 0.001). [src: comprehensive_metal_ecology] The baseline conditional PGLS (phylogenetic generalized least squares) model gave β = −0.0207 with p = 2.1×10⁻⁸. [src: comprehensive_metal_ecology]

The coreness-matched test limits this result. In NB20, 1,000 KO sets matched on count and coreness decile gave a null β median of −0.018 (range −0.039 to +0.012). The observed β = −0.021 gave emp_p = 0.298. [src: comprehensive_metal_ecology] The report concludes that the overall association is not distinguishable from coreness-matched alternatives. [src: comprehensive_metal_ecology] It locates the distinctive feature of the metal-gene set in its internal functional split, not in overall β magnitude. That split is resistance β ≈ 0 against cofactor biosynthesis β = −0.033. [src: comprehensive_metal_ecology]

Across 293,059 prokaryotic genomes, the core fraction at the 95% prevalence threshold was 0 for all five metal functional categories. No metal KO meets the near-universal threshold. [src: comprehensive_metal_ecology]

### Negative controls

All three named housekeeping controls in NB17 showed strongly negative β (−0.029 to −0.034). The report says they set a streamlining baseline and are not true nulls. [src: comprehensive_metal_ecology] NB18 confirmed five true-negative categories, all with |β| < 0.006 and q > 0.45. They are non-metal ABC (ATP-binding cassette) transporters, beta-lactam AMR (antimicrobial resistance), glycan biosynthesis, cell motility and two-component systems. [src: comprehensive_metal_ecology]

### Internal split of the metal-gene set

The report concludes that the resistance-null / constitutive-significant split is distinctive to metal genes. [src: comprehensive_metal_ecology] Three results support this.

- **Sub-functional resolution (NB19).** All AMR and TCS (two-component system) subcategories are positive, which the report describes as inducible/HGT (horizontal gene transfer) character. [src: comprehensive_metal_ecology] The sole significantly negative ABC subcategory is Lipid/LPS (lipopolysaccharide) export (β = −0.030, q = 3.3×10⁻⁵). The report reads this as consistent with constitutive outer-membrane maintenance. [src: comprehensive_metal_ecology]
- **Random partitions (NB25).** The 140-KO metal-gene set was randomly split into groups of 106 and 7, matching the resistance and cofactor group sizes. The observed Δβ = 0.035259 exceeded all 1,000 null splits (p < 0.001). The null median was −0.006 and the SD was 0.007. [src: comprehensive_metal_ecology]
- **Family comparison (NB25).** Comparison families gave Δβ = 0.032 for ABC, 0.012 for AMR and 0.006 for TCS. [src: comprehensive_metal_ecology] The metal-gene set has the largest internal split. [src: comprehensive_metal_ecology]

A leave-one-KO-out analysis of 4 assignable cofactor KOs (NB26) kept all 4 models significant. β ranged from −0.016 to −0.029, all p < 0.001, with no sign changes. No single KO drives the cofactor association. [src: comprehensive_metal_ecology]

### Confounders and sensitivity

Genome size is the only true confounder the report identifies. It reduces β by 46.7%, which lies within the coreness-permutation CI (confidence interval). [src: comprehensive_metal_ecology] Adding genome size gave β = −0.0110 (p = 0.006), a −46.7% true attenuation. [src: comprehensive_metal_ecology] The NB20 Block 4 comparison places the observed 46.7% attenuation within the permuted 95% CI [43.9%, 318.2%] (permuted median 94.9%). The report calls this weak evidence because the interval is wide. [src: comprehensive_metal_ecology]

Adding annotation depth (n_ko_ann_z) gave β = −0.0304 (p = 7.9×10⁻¹¹), a +46.7% amplification identified as a suppressor effect. [src: comprehensive_metal_ecology] The report explains this as follows. Genera with richer annotations have fewer apparent metal-gene specialists, so controlling for annotation bias strengthens the signal. [src: comprehensive_metal_ecology] The covariates n_ko_ann_z and ko_breadth_z are perfectly collinear, because both derive from n_ko_primary. Either gives the same conditional result. [src: comprehensive_metal_ecology]

The NB22 MAG-quality sensitivity analysis found a non-significant completeness covariate (p = 0.43) and an unchanged density β. [src: comprehensive_metal_ecology] Contamination showed a slight positive association (p = 0.042), with density β changed by <1.2%. [src: comprehensive_metal_ecology] In the high-quality subset (≥90%/≤5%, n = 511), the signal persisted with β = −0.018 and p = 0.005. [src: comprehensive_metal_ecology]

## Interpretation: Contextualising the metal-gene signal within the genome-streamlining …

The report reads the metal-gene signal as part of a broad genome-streamlining effect: per-Mb densities fall with niche breadth in most gene categories, and the metal-gene signal is weaker than the housekeeping baseline but not absent. [src: comprehensive_metal_ecology] It treats this section as mechanistic interpretation, not a new confirmatory test. [src: comprehensive_metal_ecology] See [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]].

### Status of the analyses behind the interpretation

Findings 1–8 and 10–11 (Notebooks 01–05, 12, 15–17) were fully pre-specified with directional hypotheses and decision rules before data inspection. [src: comprehensive_metal_ecology] Finding 9 and all NB17–NB24 exploratory analyses were designed after the P1 result was seen. They contribute to mechanistic interpretation only and cannot shift the H1 classification. [src: comprehensive_metal_ecology]

### A pervasive streamlining frame

The report reads 14/19 KEGG functional categories with significantly negative per-Mb density associations with niche breadth (Finding 3) as a pervasive genome-streamlining effect. [src: comprehensive_metal_ecology] Its explanation is that ecological specialists reduce their genomes across the board, so any conserved gene set becomes denser per Mb. [src: comprehensive_metal_ecology] Classic null controls show the streamlining signature at the same or greater magnitude as the metal-gene set. The values are ribosomal proteins β = −0.029 [src: comprehensive_metal_ecology], amino acid biosynthesis β = −0.034 [src: comprehensive_metal_ecology] and DNA repair β = −0.033. [src: comprehensive_metal_ecology]

The coreness-matched permutation (NB20; emp_p = 0.298) indicates that the overall metal-gene β = −0.021 is not unusual for a conserved gene set of its size and prevalence structure. [src: comprehensive_metal_ecology] This is a null result for the claim that metal genes are special.

### The residual gap from the housekeeping baseline

The metal-gene signal is 30–60% weaker than the housekeeping baseline: P1 β = −0.021 against housekeeping β ≈ −0.029 to −0.035. [src: comprehensive_metal_ecology] The report reads this gap as genuine gene-content signal. In its view, specialists do not compact all genes equally and are specifically enriched in metal-processing genes beyond what genome-size-driven compaction predicts. [src: comprehensive_metal_ecology] It treats the housekeeping comparison as mechanistically motivated. The coreness permutation asks a different question, whether the overall β is extreme within the null, so its negative result (emp_p = 0.298) does not negate the housekeeping gap. [src: comprehensive_metal_ecology]

### True negatives and constitutive categories

Resistance/detoxification genes have β ≈ 0 and fall among the five confirmed true-negative categories. [src: comprehensive_metal_ecology] The report describes these as variable, inducible, HGT-mobile gene sets with no constitutive coupling to genome size. [src: comprehensive_metal_ecology] It stresses that they lie among the true negatives, not between the streamlining baseline and the true null, so the null is precise, not intermediate. [src: comprehensive_metal_ecology] In contrast, cofactor biosynthesis (β = −0.033) matches the housekeeping baseline exactly, which the report reads as constitutive, irreversible genomic investment. [src: comprehensive_metal_ecology] See [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations]].

The metal-gene set also has an internal contrast of Δβ ≈ 0.036 across five functional subcategories. [src: comprehensive_metal_ecology] This contrast is not replicated in the three comparison categories tested at the same resolution (AMR, antimicrobial resistance; TCS, two-component system; and ABC, ATP-binding cassette transporters; NB19). All subcategories in those categories share the same directional character. [src: comprehensive_metal_ecology]

### Horizontal gene transfer and the resistance null

The report explains the resistance/detoxification null by horizontal gene transfer (HGT) decoupling resistance-gene content from ecological specialisation (Pal et al. 2015; Gios et al. 2025). [src: comprehensive_metal_ecology] It also attributes the non-significant resistance category (β ≈ 0) to HGT decoupling resistance content from vertical inheritance (Pal et al. 2015). [src: comprehensive_metal_ecology] It cites Gios et al. (2025) as showing that per-Mb HGT rates in Patescibacteria are independent of genome size (1.1 HT genes/Mb regardless of genome scale) [src: comprehensive_metal_ecology], and that metal-linked ABC cation transporters are preferentially acquired. [src: comprehensive_metal_ecology] The report argues that a constant per-Mb HGT rate makes resistance-gene abundance track current selective pressure, not long-term ecological specialisation, which predicts the observed null. [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

The cofactor signal (β = −0.033) aligns, in the report's view, with Fe–S cluster assembly being one of the most conserved, vertically inherited gene sets in prokaryotes (Lill 2009). [src: comprehensive_metal_ecology] See [[entities/iron-sulfur-cluster-biogenesis]].

### Genome-size control

Controlling for genome size reduces the metal-gene β by 46.7%, just below the pre-specified 50% threshold. The association survives correction (p = 0.006). [src: comprehensive_metal_ecology] The report reads this as small-genome specialists investing a disproportionately high fraction of their genomes in metal processing, beyond what genome size alone predicts. [src: comprehensive_metal_ecology] It adds that 46.7% attenuation is within the expected range for streamlining indicators, not an outlier needing special explanation. [src: comprehensive_metal_ecology] It describes the confounder analysis as consistent with the literature: genome size explains 46.7% of β, yet metal-gene density tracks specialisation beyond genome size. [src: comprehensive_metal_ecology]

### The near-zero Australian replication

The NGSA Australia-only replication (P3, n = 482, β = −0.002) is consistently near-zero. [src: comprehensive_metal_ecology] The report offers three probable explanations, none tested here. The first is that Australia's relative geological stability produces lower cross-biome variation in metal-gene investment. [src: comprehensive_metal_ecology] The second is that NGSA soil geochemistry covers a narrower chemical gradient. [src: comprehensive_metal_ecology] The third is that all P3 genera also appear in P1, which reduces independent information without adding new signal. [src: comprehensive_metal_ecology] The within-dataset AusMicrobiome genomic density analysis (P5, same genera, same genomic predictor) recovers a strong and larger signal. The report takes this to mean the near-zero P3 result reflects the soil-concentration predictor, not the genus panel. [src: comprehensive_metal_ecology] See [[concepts/robustness-and-replication-of-niche-breadth-associations]].

### Literature context

The report cites several studies that fit the streamlining reading:
- Rastogi et al. (2023): marine bacterioplankton generalists (B = 11.5) and specialists (B = 8.9) differ by ~29% in Levins' niche breadth. [src: comprehensive_metal_ecology] Specialist niches show deterministic selection of 54.1%, against 62.8% stochastic for generalists. [src: comprehensive_metal_ecology]
- Szukics et al. (2024): with a modified Levins' B in soil Thaumarchaeota, generalist-to-specialist transitions occur at a 6-fold higher rate than the reverse. [src: comprehensive_metal_ecology]
- Leu et al. (2022): free-living oligotrophic specialists average 3.0–4.5 Mb and particle-associated generalists 4.5–5.2 Mb, a 24–35% size difference. [src: comprehensive_metal_ecology] Generalists carry 2–5-fold more carbohydrate-active enzymes (CAZymes) and 8+ substrate-class transporters per genome. [src: comprehensive_metal_ecology]
- Lauro et al. (2009): comparable size reductions in SAR11 and Prochlorococcus specialists, with gene loss concentrated in regulation and secondary metabolism. [src: comprehensive_metal_ecology]

### Novelty

The report states that no published study systematically quantifies Fe–S or molybdopterin gene variation by ecological niche type. It calls the strong categorical signal in this finding the project's novel observation. [src: comprehensive_metal_ecology] Its systematic search found no paper that correlates per-megabase metal-gene KEGG ortholog (KO) density across prokaryotic genera with standardised Levins' B_std using phylogenetically controlled analysis. [src: comprehensive_metal_ecology] The closest prior work (Leu et al. 2022) examines metal-transporter presence/absence by ocean lifestyle, without per-Mb densities or phylogenetic generalized least squares (PGLS). [src: comprehensive_metal_ecology]

## Interpretation; Manuscript reviewer response analyses (2026-07)

This part of the report answers manuscript reviewers with four questions: how specific the metal-gene signal is, whether the cofactor comparison set is clean, how two carbohydrate results fit together, and whether latitude effects have a mechanism. All of these new analyses are labelled exploratory. [src: comprehensive_metal_ecology] The report presents them as sharpening its claim of a cross-genus, phylogenetically controlled link between genomic metal-gene investment and global ecological breadth. Earlier studies of metal tolerance explained variation among contaminated sites or among strains within species. [src: comprehensive_metal_ecology]

### Interpretation

The overall metal-gene versus niche-breadth β = −0.021 is not extreme relative to coreness-matched alternatives (NB20; emp_p = 0.298). The report places it within a pervasive streamlining landscape. [src: comprehensive_metal_ecology] Two features are called more distinctive. First, metal genes are 30–60% less compacted than the housekeeping baseline, which the report reads as consistent with selective retention. [src: comprehensive_metal_ecology] Second, resistance genes (β ≈ 0) fall in the true-negative category, while cofactor biosynthesis (β = −0.033) matches the housekeeping baseline. [src: comprehensive_metal_ecology]

The metal functional-category contrast (Δβ ≈ 0.036) is not reproduced at the same sub-functional resolution in AMR (antimicrobial resistance), TCS (two-component system) or ABC (ATP-binding cassette) transporter families (NB19). On this basis the report considers metal-cofactor dependence, not stress-response capacity, the mechanism most consistent with the patterns. [src: comprehensive_metal_ecology]

### Specificity controls: standalone null-category PGLS

The standalone PGLS (phylogenetic generalized least squares) of five non-metal KEGG categories against niche breadth finds no significant association. All five have p > 0.36 and |β| < 0.006, and they match the NB18 functional landscape results exactly. [src: comprehensive_metal_ecology] The report treats them as confirmed true-negative controls that support the specificity of the metal-gene signal. [src: comprehensive_metal_ecology]

- abc_transporters: 475 KOs (KEGG orthologs), 1,073 genera, β = −0.00546, SE (standard error) = 0.00628, raw p = 0.385, NB18 q (FDR-19) = 0.457. [src: comprehensive_metal_ecology]
- amr: 112 KOs, 1,073 genera, β = −0.00387, SE = 0.00546, raw p = 0.478, NB18 q (FDR-19) = 0.505. [src: comprehensive_metal_ecology]
- glycan_biosyn: 73 KOs, 1,050 genera, β = +0.00119, SE = 0.00402, raw p = 0.767, NB18 q (FDR-19) = 0.767. [src: comprehensive_metal_ecology]
- cell_motility: 153 KOs, 1,063 genera, β = +0.00397, SE = 0.00545, raw p = 0.466, NB18 q (FDR-19) = 0.505. [src: comprehensive_metal_ecology]
- two_component: 521 KOs, 1,073 genera, β = +0.00592, SE = 0.00651, raw p = 0.364, NB18 q (FDR-19) = 0.457. [src: comprehensive_metal_ecology]

### Cofactor and vitamin overlap audit

The audit shows that overlap between the cofactor comparison set and the metal-gene list is expected and does not change the result. It cross-referenced all 382 KEGG cofactors-and-vitamins KOs against the 730-KO curated metal-gene list (all 5 evidence tiers), BacMet2 and Pfam metal-binding clan coverage. [src: comprehensive_metal_ecology] It found 83 shared KOs. [src: comprehensive_metal_ecology] Twelve of these are in the primary 140 metal-gene KOs and were already excluded from the 370-KO non-metal cofactor comparison set. [src: comprehensive_metal_ecology]

The other 71 come from metal-list Tiers 3–5 or BacMet2. They fall in heme (hemA/B/C/D/E/G/H/J/L/N, hemQ), cobalamin/cobamide (cobA–Q, cbiA–T), molybdopterin (moaA/C) and biotin (bioA/B/D/F/I/U/W) biosynthesis, which are metal-dependent cofactor pathways by KEGG design. [src: comprehensive_metal_ecology] The report classes these 71 as mechanistically non-metal cofactors. They produce cofactors for other enzymes and do not process environmental metals directly. Their presence in the comparison set does not alter interpretation. [src: comprehensive_metal_ecology]

The full 382-KO set and the 12-KO-reduced 370-KO set both give β = −0.029, so the broader overlap has minimal quantitative impact. [src: comprehensive_metal_ecology] The report concludes that the non-metal cofactor comparison is valid and that the 83/382 overlap does not threaten the specificity interpretation. [src: comprehensive_metal_ecology]

### Reconciling carbohydrate results across projects

Two cross-project carbohydrate results point in opposite directions. In the functional landscape (NB18), carbohydrate metabolism KO density was negatively associated with niche breadth (β = −0.026, p = 1.3 × 10⁻⁹). [src: comprehensive_metal_ecology] In microbeatlas_metal_ecology NB07, GapMind carbon breadth was positively associated with it (β = +0.142, SE = 0.033, p = 1.9 × 10⁻⁵). [src: comprehensive_metal_ecology]

The report calls these geometrically consistent. Per-Mb KO density has genome length in the denominator, so streamlining raises density even as the absolute carbohydrate gene complement falls. [src: comprehensive_metal_ecology] GapMind pathway completeness is a qualitative repertoire metric that counts whether full pathways are present, and it grows with generalism. [src: comprehensive_metal_ecology] Specialists therefore show high carbohydrate KO density per Mb and low GapMind breadth, and generalists show the converse. [src: comprehensive_metal_ecology] This reconciliation is exploratory because it compares independently computed cross-study metrics. The report says it needs an integrated genome-size-partitioned analysis. [src: comprehensive_metal_ecology]

### Latitude mechanism tests

The analysis asked whether the latitude suppressor effect in Table 7 (β: 0.021 → 0.031 when latitude is added as a confounder) is explained by bedrock geochemistry (H4a) or climate stability (H4b). [src: comprehensive_metal_ecology] Genus covariates came from Spark-side aggregation of arkinlab_microbeatlas, which returned 10,040 genera, 1,224 of them matched to the PGLS input. [src: comprehensive_metal_ecology] GeoROC bedrock Cu/Ni/Zn/Co/Pb/Cr concentrations (ppm) were available for n=9,954 non-null genera. CMMI ore deposit proximity was pre-joined for n=1,161 genera. [src: comprehensive_metal_ecology]

Latitude was not an independent predictor of niche breadth in any of the nine models (p = 0.20–0.78) once metal genes were controlled. [src: comprehensive_metal_ecology] The models below list n, the metal-density β with p, then the added covariate β with p.

- Model A, metal + absolute latitude: n = 1,224; β_metal = −0.0207 (p = 6.6×10⁻⁸); latitude β = −0.0017 (p = 0.577). [src: comprehensive_metal_ecology]
- Model B, + GeoROC bedrock metals: n = 1,221; β_metal = −0.0193 (p = 4.6×10⁻⁷); GeoROC β = +0.0120 (p = 2.2×10⁻⁴). [src: comprehensive_metal_ecology]
- Model C, + ERA5 temperature range: n = 1,223; β_metal = −0.0206 (p = 6.5×10⁻⁸); temperature β = +0.0136 (p = 9.6×10⁻⁵). [src: comprehensive_metal_ecology]
- Model D, + CMMI proximity: n = 1,161; β_metal = −0.0213 (p = 5.9×10⁻⁸); CMMI β = −0.0030 (p = 0.375). [src: comprehensive_metal_ecology]
- Model E, + CSU PF1 bioavailable mobility: n = 1,108; β_metal = −0.0209 (p = 1.7×10⁻⁷); β = +0.0040 (p = 0.227). [src: comprehensive_metal_ecology]
- Model F, + Sci2025 soil metal hazard quotient: n = 1,088; β_metal = −0.0208 (p = 2.3×10⁻⁷); β = +0.0037 (p = 0.291). [src: comprehensive_metal_ecology]
- Model G, + SoilTemp range −10cm: n = 207; β_metal = −0.0194 (p = 0.074); β = +0.0238 (p = 0.0085). The n is small, and the metal term is no longer significant. [src: comprehensive_metal_ecology]
- Model H, + ecotapestry mafic score: n = 975; β_metal = −0.0233 (p = 2.2×10⁻⁸); β = +0.0088 (p = 0.013). [src: comprehensive_metal_ecology]
- Model I, + USGS (United States Geological Survey) REE deposit proximity: n = 1,224; β_metal = −0.0208 (p = 5.6×10⁻⁸); β = +0.0031 (p = 0.318). [src: comprehensive_metal_ecology]

The report treats H4a as supported by two independent bedrock proxies. The GeoROC total metal concentration index gives β = +0.012, p = 2.2×10⁻⁴ (Model B). The Ecotapestry mafic/felsic score gives β = +0.009, p = 0.013 (Model H, n = 975). [src: comprehensive_metal_ecology] β_metal attenuates by ≤13% in both models and stays highly significant. [src: comprehensive_metal_ecology]

Contemporary measures did not predict niche breadth. Science 2025 soil metal hazard quotients (Model F, HHET; n = 1,088, p = 0.291) and CSU PF1 bioavailable mobility fractions (Model E; n = 1,108, p = 0.227) were not significant. [src: comprehensive_metal_ecology] CMMI ore deposit proximity (Model D, p = 0.375) and USGS REE deposit proximity (Model I, p = 0.318) were not significant either. [src: comprehensive_metal_ecology] The report suggests that the significant bedrock result alongside null contemporary soil-metal results reflects deep evolutionary or long-term ecological filtering, not contemporary metal exposure. This is an interpretation, not a direct test. [src: comprehensive_metal_ecology]

## Manuscript reviewer response analyses (2026-07): Q4 per-metal decomposition …

This part of the report tests whether geochemical and climate covariates explain the negative association between metal-gene density and genus niche breadth. Across all nine latitude mechanism models, β_metal ranged from −0.019 to −0.023, and the report concludes the primary finding is robust to every geochemical and climate covariate tested. [src: comprehensive_metal_ecology] Per-metal bedrock models point to chromium as the main bedrock signal, with cobalt secondary. [src: comprehensive_metal_ecology]

### Climate and deposit proximity

The report treats climate-stability hypothesis H4b as supported by two independent temperature metrics: ERA5 temperature range and SoilTemp measured soil temperature range. [src: comprehensive_metal_ecology] In full-sample Model C, temperature leaves β_metal fully unchanged. Climate variability predicts niche breadth independently but does not explain the metal-gene association. [src: comprehensive_metal_ecology] SoilTemp Model G had only 94 0.5° bins and 207 matched genera, and β_metal lost significance there (p = 0.074). The report calls it underpowered and confirmatory of direction only. [src: comprehensive_metal_ecology]

The 7% attenuation in Model B is the largest reduction in β_metal. Slight amplification in the geographically restricted Model H (n = 975 genera) brackets the upper end. [src: comprehensive_metal_ecology] USGS (United States Geological Survey) rare-earth-element deposit proximity in Model I was not associated with niche breadth (p = 0.318). [src: comprehensive_metal_ecology]

### Per-metal bedrock models

The per-metal analysis ran GeoROC phylogenetic generalized least squares (PGLS) models. Each used genus-level medians of log(ppm+1) queried from Spark. Niche breadth was modelled on metal-gene density, absolute latitude and a bedrock-metal covariate, optionally with pH. [src: comprehensive_metal_ecology] The report says this analysis is complete. [src: comprehensive_metal_ecology]

Variance inflation factors (VIFs) for the six bedrock metals were Cu 1.16, Ni 1.87, Zn 1.14, Co 1.26, Pb 1.12 and Cr 1.83. [src: comprehensive_metal_ecology] The report therefore treats bedrock metals as near-independent at genus scale. It considers per-metal and joint models valid without regularisation. [src: comprehensive_metal_ecology]

Without pH control (J models), metal-gene density stayed negative in every model, and the report states it was stable (−0.019 to −0.022) across all J–M models. [src: comprehensive_metal_ecology] Only Co and Cr bedrock terms were significant after Benjamini-Hochberg (BH) correction.

| Model | n genera | β_metal | β_bedrock | p_raw | p_BH |
|---|---|---|---|---|---|
| J_Cu | 1,212 | −0.0208 | −0.0036 | 0.235 | 0.333 [src: comprehensive_metal_ecology] |
| J_Ni | 1,220 | −0.0206 | +0.0015 | 0.614 | 0.614 [src: comprehensive_metal_ecology] |
| J_Zn | 1,213 | −0.0210 | −0.0034 | 0.278 | 0.333 [src: comprehensive_metal_ecology] |
| J_Co | 1,214 | −0.0215 | +0.0091 | 2.8×10⁻³ | 8.4×10⁻³ [src: comprehensive_metal_ecology] |
| J_Pb | 1,220 | −0.0209 | +0.0042 | 0.181 | 0.333 [src: comprehensive_metal_ecology] |
| J_Cr | 1,220 | −0.0203 | +0.0187 | 1.1×10⁻⁹ | 6.7×10⁻⁹ [src: comprehensive_metal_ecology] |

The report concludes that Cu, Ni, Zn and Pb were not significant after FDR correction. It also concludes that common ore-forming metals do not drive the composite GeoROC signal. [src: comprehensive_metal_ecology]

### pH control

With pH added (K models), Cu, Ni, Zn and Pb bedrock terms stayed non-significant (p = 0.437, 0.557, 0.289 and 0.392). [src: comprehensive_metal_ecology] Co stayed significant at p = 0.020 (β = +0.0072), and Cr at p = 1.0×10⁻⁸ (β = +0.0176). [src: comprehensive_metal_ecology] pH was a positive predictor in every K model, for example β_pH = +0.0110, p = 7.9×10⁻⁴ in K_Cu and β_pH = +0.0095, p = 3.0×10⁻³ in K_Cr. [src: comprehensive_metal_ecology] The report initially reads this pH effect as a genuine speciation/ecology signal distinct from geological metal effects (β ≈ +0.011, p < 0.001). [src: comprehensive_metal_ecology] It explains the unchanged Cr signal by saying Cr speciation is redox-dominated rather than pH-dominated. [src: comprehensive_metal_ecology]

### Joint and PCA models

In the joint M model with all six metals (VIF < 2), n = 1,207 and β_metal = −0.022 (p = 6×10⁻⁹). [src: comprehensive_metal_ecology] Cr was dominant (β = +0.0301, p = 9.5×10⁻¹³). [src: comprehensive_metal_ecology] Ni reversed sign (β = −0.0164, p = 5.5×10⁻⁵), which the report calls a suppressor effect against Cr. [src: comprehensive_metal_ecology] Pb was weakly positive (β = +0.0072, p = 0.030). [src: comprehensive_metal_ecology] Co (β = +0.0046, p = 0.171), Cu (β = −0.0011, p = 0.736) and Zn (β = −0.0016, p = 0.630) were not significant. [src: comprehensive_metal_ecology] The report advises reading the Ni coefficient cautiously. It describes it as an exploratory partial-regression effect, consistent with Cr and Ni sharing mafic rock association. [src: comprehensive_metal_ecology]

In the PCA models, PC1 (principal component 1) had positive loadings on all metals and explained 47% of variance (β = +0.009, p = 0.0025). PC2 was a contrast axis explaining 22% (β = −0.007, p = 0.029). [src: comprehensive_metal_ecology]

### Interpretation

The report names Cr as the dominant driver of the composite GeoROC signal. It reads Cr enrichment as indicating mafic/ultramafic bedrock, consistent with the ecotapestry mafic-score model (Model H). [src: comprehensive_metal_ecology] It calls Co a secondary contributor. Co is attenuated but survives pH control, and it is also enriched in mafic rocks and komatiites. [src: comprehensive_metal_ecology] See [[entities/chromium]] and [[entities/cobalt]].

## Manuscript reviewer response analyses (2026-07); Limitations

This part of the report tests whether soil redox explains the link between bedrock metal content and genus niche breadth. It then lists the limitations of the whole study. The redox controls leave the chromium signal unchanged. The limitations show a small effect size and several replication or coverage gaps. [src: comprehensive_metal_ecology]

### Redox proxy controls (Q4)

The analysis used two globally comprehensive soil proxies from enriched_metadata_gee. High soil moisture implies waterlogging, anaerobic conditions and immobile Cr(III). High soil organic matter (SOM, 0 cm) implies microbial O₂ drawdown and reducing capacity. [src: comprehensive_metal_ecology] The report used proxies because direct Cr(VI) data do not exist globally. The CSU speciation table has all-null BCR fraction fields and WoSIS has only pH, organic carbon and texture. GEMAS is Europe-only (4,343 pts) and NGSA mobile chromium is Australia-only (1,315 pts). [src: comprehensive_metal_ecology] The analysis is marked complete. It writes four N-series rows to data/latitude_mechanism_results.csv and adds moisture and SOM covariates to data/genus_lat_env_covariates.csv. [src: comprehensive_metal_ecology]

Genus-level correlations with bedrock metal (n ≈ 1,213–1,218) are weak. Moisture is not significantly correlated with bedrock Cr (r = −0.050, p = 0.083). It is negatively correlated with bedrock Co (r = −0.140, p = 9.3×10⁻⁷). [src: comprehensive_metal_ecology] SOM is not significantly correlated with Cr (r = −0.015, p = 0.597) or Co (r = −0.047, p = 0.103). [src: comprehensive_metal_ecology] The report reads bedrock Cr as near-orthogonal to both proxies. It reads Co-rich bedrock as slightly drier and more oxidizing mafic terrain. [src: comprehensive_metal_ecology]

### Niche-breadth models with redox covariates

- N_Cr (+ moisture), n = 1,219 genera: bedrock Cr β = +0.0175 (p = 1.2×10⁻⁸); pH β = +0.0117 (p = 5.4×10⁻³); moisture β = +0.003 (p = 0.44, NS). [src: comprehensive_metal_ecology]
- N_Co (+ moisture), n = 1,213: bedrock Co β = +0.0072 (p = 0.021); pH β = +0.0120 (p = 5.2×10⁻³); moisture β = +0.003 (p = 0.50, NS). [src: comprehensive_metal_ecology]
- N_Cr_som, n = 1,218: bedrock Cr β = +0.0187 (p = 1.3×10⁻⁹); pH β = +0.003 (p = 0.39, NS); SOM β = −0.0155 (p = 6.8×10⁻⁵). [src: comprehensive_metal_ecology]
- N_Co_som, n = 1,213: bedrock Co β = +0.0075 (p = 0.016); pH β = +0.005 (p = 0.21, NS); SOM β = −0.0134 (p = 6.6×10⁻⁴). [src: comprehensive_metal_ecology]

The report concludes that the bedrock Cr signal is not mediated by soil redox. β_Cr is unchanged between N_Cr and K_Cr (0.0175 vs 0.0176), and moisture is NS. This rules out the proposed "Cr(VI) via reducing/waterlogged soils" pathway. [src: comprehensive_metal_ecology] The report proposes two possible mechanisms, which it does not test. One is chronic Cr(III)/Ni/Mg stress in serpentine soils. The other is that ultramafic terrain selects niche specialists through correlated factors such as Ca/Mg ratio, soil structure and slow weathering. [src: comprehensive_metal_ecology]

### SOM as an incidental finding

High-SOM soils have narrower niches independently of bedrock metal type (β = −0.016, p = 6.8×10⁻⁵ in the Cr model). The report calls this incidental and outside the original model set. [src: comprehensive_metal_ecology] Including SOM absorbs the pH association: pH goes from p ≈ 0.003 in K models to p = 0.39. [src: comprehensive_metal_ecology] The report reads the "broader niches at high pH" signal as largely mediated through or confounded with SOM. High-SOM boreal and peatland environments tend to be acidic. The report suggests SOM may affect metal speciation through DOM chelation more directly than pH does. [src: comprehensive_metal_ecology] For the same reason, the pH niche-breadth signal in Finding 13 (β = −0.760) may be partly SOM-mediated. SOM-metal chelation in acidic peatland soils may confound a direct pH → speciation → specialist-selection reading. [src: comprehensive_metal_ecology]

### Limitations: effect size and causality

The metal-gene functional landscape is correlational. The evidence supports metal-content enrichment above compaction, but causality is unresolved. [src: comprehensive_metal_ecology] Metal-gene density explains a small share of genus-level niche-breadth variance (r² = 0.046 in P1), and breadth is multidimensionally determined. [src: comprehensive_metal_ecology] Explicit genome-size correction attenuates the association by 46.7% but does not eliminate it. [src: comprehensive_metal_ecology] In NB23, genome size partly confounds the association (46.7% attenuation), but the signal survives (p = 0.006). [src: comprehensive_metal_ecology] Annotation depth acts as a suppressor variable, not a confounder. [src: comprehensive_metal_ecology]

### Limitations: replication and data coverage

- The Australia-only NGSA replication (P3) is near-zero, which lowers confidence that the soil-concentration predictor is universal. [src: comprehensive_metal_ecology]
- The BacDive NB09 culture-based geographic niche-breadth replication is pending execution. [src: comprehensive_metal_ecology]
- ENIGMA FRC data cover n = 3 wells and are uninformative at that size. [src: comprehensive_metal_ecology]
- Levins' B_std from 16S OTUs (operational taxonomic units) may carry noise from coarse OTU–genus matching and MicrobeAtlas annotations. [src: comprehensive_metal_ecology]
- The cofactor category's strongest categorical signal rests on 7 KOs (KEGG orthologs). It is statistically robust (ΔAIC = −35.4), but its narrow biological definition warrants caution. [src: comprehensive_metal_ecology]

### Limitations: MAG quality

Per-Mb metal-gene density may be affected by MAG (metagenome assembled genome) incompleteness that is not random across taxa. [src: comprehensive_metal_ecology] NB22 tested this. Adding completeness leaves the density β unchanged (p = 0.43, NS). [src: comprehensive_metal_ecology] Adding contamination gives p = 0.042 with <1.2% β change. [src: comprehensive_metal_ecology] The high-quality-restricted analysis (n = 511) gives β = −0.018, p = 0.005, and the report treats the concern as addressed. [src: comprehensive_metal_ecology]

### Limitations: resistance genes, coreness and specificity

Resistance-gene null confidence intervals (CI) do not exclude small effects. The report therefore reads the null as absence of a substantial phylogenetically conserved association. [src: comprehensive_metal_ecology] The NB20 coreness-matched permutation does not support uniqueness of the metal gene set among conserved gene categories. Its emp_p is 0.298, and the primary β = −0.021 lies within the null distribution. [src: comprehensive_metal_ecology] The report places the distinctiveness of the metal gene set in its internal functional split, not its overall magnitude, which is part of the streamlining landscape. [src: comprehensive_metal_ecology] In NB23, core fraction is zero at the 95% threshold for all metal categories, so coreness cannot explain functional specificity. [src: comprehensive_metal_ecology]

### Limitations: co-occurrence confound

The positive-partner-count signal in Findings 15–16 (β = 138–210 across strata) correlates with niche breadth (Spearman ρ = 0.33–0.37, p < 10⁻⁴⁰). [src: comprehensive_metal_ecology] Partial analyses controlling for B_std are needed before the signal can be called independent of the primary specialisation axis. [src: comprehensive_metal_ecology]

## Data: Generated Data

This part of the report lists the KBase Data Lakehouse collections it draws on and the data files it produces. The tables below are parallel lists. The analysis files hold the results reported elsewhere on the page. [src: comprehensive_metal_ecology]

### Lakehouse collections used

| Collection | Tables | Purpose |
|---|---|---|
| kbase_ke_pangenome | eggnog_mapper_annotations, gene_genecluster_junction, gene_cluster, genome, gtdb_taxonomy_r214v1 | KO (KEGG ortholog) density per genus from MAG (metagenome assembled genome) pangenomes [src: comprehensive_metal_ecology] |
| kescience_mgnify | OTU (operational taxonomic unit) × sample abundance matrix, via MicrobeAtlas | Levins' niche breadth calculation [src: comprehensive_metal_ecology] |
| arkinlab_microbeatlas | sample_metadata | pH, temperature and biome metadata for confounder checks [src: comprehensive_metal_ecology] |
| kescience_bacdive | isolation, strain, taxonomy | Geographic niche breadth, pending NB09 execution [src: comprehensive_metal_ecology] |
| enigma_genome_depot_enigma | browser_genome, browser_gene, browser_protein_kegg_orthologs, browser_kegg_ortholog, browser_sample | ENIGMA FRC MAG KO content [src: comprehensive_metal_ecology] |
| enigma_coral | ddt_brick0000007 | Oak Ridge FRC groundwater metal concentrations [src: comprehensive_metal_ecology] |
| arkinlab_envdbs | cmmi_ores | Exploratory ore deposit proximity analysis [src: comprehensive_metal_ecology] |

### Input and core data files

- `curated_mrg_ko_ids_v2.csv` has 730 rows. It is an evidence-tiered metal-gene KO list covering 5 tiers and 24 metals. [src: comprehensive_metal_ecology]
- `curated_mrg_ko_ids_v2_pfam.csv` has 730 rows of KOs annotated with Pfam/InterPro domains. [src: comprehensive_metal_ecology]
- `01_genus_ko_density_spark.csv` has 8,256 rows of per-genus primary KO density from Spark. [src: comprehensive_metal_ecology]
- `genus_trait_table.csv` has 2,851 rows of Levins' niche breadth per genus from MicrobeAtlas. [src: comprehensive_metal_ecology]
- `01_pgls_input_bacteria.csv` has 1,574 rows. It combines density, niche breadth and phylogeny as input to PGLS (phylogenetic generalized least squares). [src: comprehensive_metal_ecology]

### Primary and replication result files

- `01_primary_pgls_results.csv` has 2 rows: P1 (bacteria) and P2 (archaea). [src: comprehensive_metal_ecology]
- `02_ngsa_pgls_results.csv` has 1 row, the P3 NGSA Australia result. [src: comprehensive_metal_ecology]
- `02_joint_fdr.csv` has 3 rows of joint BH (Benjamini-Hochberg) FDR (false discovery rate) correction across P1/P2/P3. [src: comprehensive_metal_ecology]
- `emp_niche_pgls_comprehensive.csv` has 1 row, the EMP (Earth Microbiome Project) 16S niche-breadth result. [src: comprehensive_metal_ecology]
- `enigma_frc_replication.csv` has 14 rows of ENIGMA FRC Spearman correlations. [src: comprehensive_metal_ecology]
- `03_tier_pgls_results.csv` has 2 rows of tier-sweep results (T1.4, T1.5). [src: comprehensive_metal_ecology]
- `03_category_pgls_results.csv` has 5 rows of per-functional-category results. [src: comprehensive_metal_ecology]
- `03_metal_pgls_results.csv` has 9 rows of per-metal KO-set results. [src: comprehensive_metal_ecology]
- `04_confounder_results.csv` has 5 rows of confounder attenuation analysis. [src: comprehensive_metal_ecology]
- `05_sensitivity_results.csv` has 8 rows of sensitivity checks for λ, subset and biome. [src: comprehensive_metal_ecology]
- `negative_control_pgls_results.csv` holds permutation and named negative-control results. [src: comprehensive_metal_ecology]

### Later notebook outputs

- `functional_landscape_results.csv` has 19 rows of NB18 KEGG landscape PGLS results. [src: comprehensive_metal_ecology]
- `clade_stratified_pgls_results.csv` has 4 rows of NB16 phylum-level PGLS results. [src: comprehensive_metal_ecology]
- `internal_structure_results.csv` has 13 rows of NB19 subcategory PGLS results for AMR (antimicrobial resistance), TCS (two-component system) and ABC (ATP-binding cassette). It was completed 2026-07-06. [src: comprehensive_metal_ecology]
- `coreness_permutation_results.csv` has 1,000 rows for the NB20 coreness-matched permutation null, which gives emp_p = 0.298. [src: comprehensive_metal_ecology]
- `attenuation_profile_comparison.csv` has 100 rows for the NB20 genome-size attenuation profile. The observed 46.7% lies within CI (confidence interval) [43.9%, 318.2%]. [src: comprehensive_metal_ecology]
- `aus_beta_comparison.csv` has 5 rows for the NB21 P1 versus P5 β comparison and z-tests, completed 2026-07-06. [src: comprehensive_metal_ecology]
- `intersecting_genus_pgls.csv` has 1 row of NB21 intersection-genus PGLS results, completed 2026-07-06. [src: comprehensive_metal_ecology]
- `mag_quality_sensitivity.csv` has 4 rows of NB22 completeness/contamination covariate PGLS results, completed 2026-07-06/07. [src: comprehensive_metal_ecology]
- `category_descriptive_stats.csv` has 8 rows of NB23 per-category statistics. Core fraction is 0 at the 95% threshold. [src: comprehensive_metal_ecology]
- `category_conditional_models.csv` has 5 rows of NB23 conditional PGLS results. They identify annotation depth as a suppressor and report genome-size attenuation of 46.7%. [src: comprehensive_metal_ecology]
- `split_magnitude_permutation.csv` has 4 rows of NB25 results. The metal gene set has Δβ = 0.035259 and p < 0.001, with 0/1,000 permutations exceeding it. [src: comprehensive_metal_ecology]
- `cofactor_jackknife_results.csv` has 4 rows of NB26 cofactor KO jackknife results. All 4 KOs are stable, with β −0.016 to −0.029, all p < 0.001, and no sign changes. [src: comprehensive_metal_ecology]
- `inverse_pgls_results.csv` has 17 rows of NB27 single- and multi-predictor inverse PGLS models. n_biomes_z is dominant (β=0.215, p≈0), and all niche-range predictors are positive. [src: comprehensive_metal_ecology]
- `inverse_rda_variance_partitioning.csv` has 6 rows of NB28 variance partitioning. Metals have unique R²=0.064, pH+climate unique R²=0.041, shared R²=0.005, and all environment R²=0.110. [src: comprehensive_metal_ecology]

## Data: Generated Data (2)

This part of the report describes the data and results files it generated, with row counts and, for several, the main result each holds. [src: comprehensive_metal_ecology] Most results here are summary lines from the report's file descriptions, not full tables.

### Validation and null-result files

The spatial cross-validation file holds 5 rows from NB29 spatial block cross-validation (CV). It gives mean root mean square error (RMSE) 11.89, with a range of 6.20–19.37. [src: comprehensive_metal_ecology] Metals account for 45.9% of Shapley additive explanations (SHAP), and log_Ni_ppm is the top predictor. [src: comprehensive_metal_ecology]

The Q1 null-category phylogenetic generalized least squares (PGLS) file has 5 rows and stands as a confirmation of the NB18 values. [src: comprehensive_metal_ecology] All 5 categories are non-significant (p > 0.36, |β| < 0.006). [src: comprehensive_metal_ecology]

The Q2 cofactor/vitamin KEGG ortholog (KO) overlap audit has 382 rows. [src: comprehensive_metal_ecology] It finds 83 KOs shared with the 730-KO list. [src: comprehensive_metal_ecology] Of these, 12 are in the primary 140. [src: comprehensive_metal_ecology] A further 71 are additionally flagged, all in metal-cofactor pathways by design. [src: comprehensive_metal_ecology]

### Q4 latitude and environment files

The genus-level covariate file has 10,040 rows. [src: comprehensive_metal_ecology] It includes these covariates:
- GeoROC metals (9,954 non-null), CMMI proximity, ERA5 temperature range (9,985) and CSU PF1 mobility (9,217). [src: comprehensive_metal_ecology]
- Science 2025 HHET HQ for Cu/Ni/Co/Cr/Pb, SoilTemp range at −10 cm, an ecotapestry mafic/felsic score and USGS (United States Geological Survey) REE nearest-distance. [src: comprehensive_metal_ecology]
- Soil moisture (9,959 non-null) and soil organic matter (SOM) at 0 cm (9,944 non-null). [src: comprehensive_metal_ecology]

The mechanism results file has 28 rows covering Models A–I, J–M and the N series. [src: comprehensive_metal_ecology] β_metal is stable across all models. [src: comprehensive_metal_ecology]

- **H4a (geology):** The GeoROC composite gives β=+0.012, p=2.2×10⁻⁴. [src: comprehensive_metal_ecology] Cr drives it (Benjamini-Hochberg (BH) p=6.7×10⁻⁹), as does Co (BH p=0.0084). [src: comprehensive_metal_ecology] The mafic score gives β=+0.009, p=0.013. [src: comprehensive_metal_ecology] Sci2025 HQ is not significant. [src: comprehensive_metal_ecology]
- **H4b (temperature):** ERA5 temperature gives β=+0.014, p=9.6×10⁻⁵. [src: comprehensive_metal_ecology] pH is positive in all K models (p < 0.001). [src: comprehensive_metal_ecology]
- **N models:** Cr and Co are unattenuated by soil moisture. [src: comprehensive_metal_ecology] SOM is independently negative (β=−0.016, p=6.8×10⁻⁵). [src: comprehensive_metal_ecology]

The per-metal collinearity diagnostics file has 14 rows. It holds a Pearson r matrix, variance inflation factors (VIFs), PCA loadings and explained variance. [src: comprehensive_metal_ecology] All VIFs are below 2. [src: comprehensive_metal_ecology]

### Phylogenetic signal, horizontal transfer and niche files

- The genome-level Fritz & Purvis D file has 309 rows for curated metal KOs on the GTDB 18,961-tip tree. [src: comprehensive_metal_ecology]
- The genus-level Pagel's λ file has 276 rows for curated metal KOs. [src: comprehensive_metal_ecology]
- The horizontal gene transfer (HGT) synthesis table has 23 rows covering 13 double-signal and 10 control KOs. Its columns are D, λ, plasmid_fraction, mobile_fraction, mgnify_rho, env_p and hgt_score. [src: comprehensive_metal_ecology]
- The environmental niche-breadth PGLS coefficients file has 3 rows, for temperature, pH and a composite gradient. It gives β, standard error (SE), p and λ per response. [src: comprehensive_metal_ecology]
- A companion file holds the full per-response PGLS results for the niche-breadth analysis. [src: comprehensive_metal_ecology]
- The per-KO driver file has 198 rows, for 9 TIER1 KOs × 22 responses. It gives β, t, p and false discovery rate (FDR) q. [src: comprehensive_metal_ecology]

### Co-occurrence files

One file holds co-occurrence PGLS results for sig_pos_partners, sig_neg_partners and phi_degree by stratum. [src: comprehensive_metal_ecology] A second holds Spearman correlations between co-occurrence counts and B_std across strata. [src: comprehensive_metal_ecology]

## Supporting Evidence: Notebooks

This part of the report lists the notebooks behind its analyses, from gene-list profiling through confirmatory tests, robustness checks, replications and exploratory follow-ups. [src: comprehensive_metal_ecology] Some entries are marked exploratory, pending or limited. [src: comprehensive_metal_ecology]

### Core confirmatory analyses

Notebook 00 profiles the 730-KO (KEGG ortholog) gene list and makes gene_list_summary.csv and tier/metal heatmaps. [src: comprehensive_metal_ecology] Notebook 01 runs the primary PGLS (phylogenetic generalized least squares) tests: P1 in bacteria, P2 in archaea, and a soil-restricted sensitivity analysis. [src: comprehensive_metal_ecology] Notebook 02 runs the NGSA replication (P3) and a joint FDR (false discovery rate) correction across all three confirmatory tests. [src: comprehensive_metal_ecology] Notebook 03 covers tier expansion, functional-category analysis and metal-specific PGLS. [src: comprehensive_metal_ecology]

### Confounders and sensitivity

Notebook 04 checks genome size, GC content, isolation source, latitude and biome as confounders. [src: comprehensive_metal_ecology] Notebook 05 tests the λ assumption, minimum n, raw response, hemisphere and Australia. [src: comprehensive_metal_ecology] Notebook 06 scans KBase Data Lakehouse namespaces for further covariate candidates. [src: comprehensive_metal_ecology] Notebook 22 adds MAG (metagenome assembled genomes) completeness and contamination covariates and a high-quality sensitivity analysis. [src: comprehensive_metal_ecology]

### Exploratory and replication notebooks

Notebook 07 explores proximity to geological ore deposits, and the report marks it exploratory. [src: comprehensive_metal_ecology] Notebook 08 is an exploratory replication using PGLS of niche breadth from EMP (Earth Microbiome Project) 16S data. [src: comprehensive_metal_ecology] Notebook 09 runs PGLS of BacDive geographic niche breadth. [src: comprehensive_metal_ecology] The report says its schema is confirmed but its main analysis is pending. [src: comprehensive_metal_ecology] Notebook 10 validates 140 primary KOs against Pfam/InterPro domains. [src: comprehensive_metal_ecology] Notebook 11 attempts a site-level Spearman replication with ENIGMA FRC data. [src: comprehensive_metal_ecology] The report describes its data coverage as limited. [src: comprehensive_metal_ecology]

Notebook 12 is the P4 replication, using AusMicrobiome and NGSA soil metal concentrations. [src: comprehensive_metal_ecology] Notebook 15 is the P5 replication of genomic KO density in AusMicrobiome. [src: comprehensive_metal_ecology] Notebook 16 is P6, a PGLS stratified within Proteobacteria, Actinobacteria, Firmicutes and Bacteroidetes. [src: comprehensive_metal_ecology] Notebook 21 compares the P1 and P5 β values with a z-test and analyses intersecting genera and phylum composition. [src: comprehensive_metal_ecology]

### Controls and functional structure

Notebook 17 sets up named housekeeping negative controls and a streamlining baseline. [src: comprehensive_metal_ecology] Notebook 18 maps all 19 KEGG functional categories and identifies true negatives. [src: comprehensive_metal_ecology] Notebook 19 runs sub-functional PGLS in the AMR (antimicrobial resistance), TCS (two-component system) and ABC (ATP-binding cassette) comparison categories. [src: comprehensive_metal_ecology] Notebook 20 runs a coreness-matched permutation test and compares attenuation profiles. [src: comprehensive_metal_ecology] Notebook 23 gives per-category descriptive statistics and conditional PGLS on n_KOs, core_fraction and gene_length. [src: comprehensive_metal_ecology]

### Quantitative results from later notebooks

The split-magnitude permutation test (NB25) gave a resistance/cofactor Δβ of 0.035259, with p < 0.001 because 0 of 1,000 permutations exceeded it. [src: comprehensive_metal_ecology] The comparison families had Δβ < 0.033. [src: comprehensive_metal_ecology]

Notebook 26 tests the resistance-versus-cofactor interaction and jackknifes the cofactor KOs. [src: comprehensive_metal_ecology] All 4 cofactor KOs were stable, with β from −0.016 to −0.029, all p < 0.001 and no sign changes. [src: comprehensive_metal_ecology]

The inverse PGLS (NB27) found n_biomes dominant (β=0.215, p≈0). [src: comprehensive_metal_ecology] Temperature and metal range effects were positive. [src: comprehensive_metal_ecology] Mean-concentration effects were weak. [src: comprehensive_metal_ecology] The multiple R² was 0.063. [src: comprehensive_metal_ecology]

The inverse RDA (NB28) partitioned variance and found a larger unique share for metals (R²=0.064) than for pH plus climate (R²=0.041). [src: comprehensive_metal_ecology]

The XGBoost model predicting community weighted means from environment (NB29) had a mean CV (cross-validation) RMSE (root mean square error) of 11.89. [src: comprehensive_metal_ecology] Metals carried 45.9% of SHAP (Shapley additive explanations) importance. [src: comprehensive_metal_ecology] The top predictor was log_Ni_ppm. [src: comprehensive_metal_ecology] The report describes spatial generalisation as poor, which limits how far these predictions extend to new regions. [src: comprehensive_metal_ecology]

### Scripts

- `scripts/hgt_direct_evidence.py` gathers HGT (horizontal gene transfer) evidence from NCBI Entrez plasmid and mobile-element queries, a Fritz & Purvis D comparison and MGnify environmental enrichment. It produces a synthesis table and 3 figures. [src: comprehensive_metal_ecology]
- `scripts/partner_characterisation.py` characterises co-occurrence partners. It compares top-50 with control-50 focal genera, extracts partners by φ threshold, and applies MWU (Mann-Whitney U) and chi-square tests. It produces 3 figures. [src: comprehensive_metal_ecology]
- `scripts/run_cooccurrence_analysis.py` builds co-occurrence networks with the hypergeometric Veech test and phi coefficients. It then runs PGLS of positive partner count on KO density across 3 strata. [src: comprehensive_metal_ecology]
- `scripts/env_niche_breadth_analysis.py` runs niche-breadth PGLS with temperature, pH and composite gradients as responses. [src: comprehensive_metal_ecology]
- `scripts/per_ko_driver_analysis.py` screens 9 TIER1 KOs against 22 environmental responses and runs a metal-match MWU analysis. [src: comprehensive_metal_ecology]

## Future Directions

### Unfinished work and replication

The BacDive notebook NB09 has finished schema discovery. Its main country-count aggregation and phylogenetic generalized least squares (PGLS) have not run. [src: comprehensive_metal_ecology] Once run, BacDive culture-based cosmopolitanism would give a fully independent, non-16S-derived replication of niche breadth. [src: comprehensive_metal_ecology] [[entities/bacdive|BacDive]] is the source for this.

The report also proposes widening the evidence base in three ways:
- Access the full [[entities/enigma|ENIGMA]] geochemical database, beyond `ddt_brick0000007`. This would give groundwater chemistry for the remaining 18 wells that have metagenome assembled genome (MAG) data. [src: comprehensive_metal_ecology]
- Replace the 16S operational taxonomic unit (OTU)–genus bridge with genus-level niche breadth computed directly from MGnify metagenomic genus-level classifications. [src: comprehensive_metal_ecology]
- Run a northern-hemisphere soil amplicon-survey replication. The signal is stronger in northern hemisphere genera (β = −0.030) and in soil specialists (β = −0.033). A targeted replication would strengthen the explanation for the Australian null result. [src: comprehensive_metal_ecology]

### Mechanism and confounding

The report proposes a causal decomposition that uses the streamlining landscape as a baseline. Niche breadth would be regressed on a composite "compaction index" built from the true-negative category densities, and on metal-gene density residualised against that index. This would split the primary β into streamlining-driven and metal-content-specific parts. [src: comprehensive_metal_ecology] See [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]].

A second test asks whether cofactor-gene density, the strongest category, is the proximate mechanistic link. Niche breadth would be regressed on cofactor density, controlling for overall primary-set density. A partial R² would show whether cofactor genes drive the association or are co-linear with the broader metal-gene investment signal. [src: comprehensive_metal_ecology]

For pH, the report states that the niche signal (β = −0.760, p = 0.001) predicts that metal-gene-rich genera should cluster at lower pH values, where Cr(VI)/Cu²⁺ speciation is most reactive. This is a prediction, not an observed clustering. [src: comprehensive_metal_ecology] Overlaying genus pH optima on metal-speciation pH curves would test it mechanistically. [src: comprehensive_metal_ecology]

ENIGMA longitudinal MAG data could test whether genera with higher metal-gene density show lower occupancy turnover across time points. [src: comprehensive_metal_ecology]

### Direction of effect

An exploratory inverse PGLS (NB27) reversed the prediction direction. It found that niche-range breadth (biomes occupied, temperature/metal-concentration range) positively predicts per-Mb metal-gene density (n_biomes: β = 0.215, p ≈ 0). [src: comprehensive_metal_ecology] The report says this warrants confirmatory pre-registration before further inference, so it is not yet a settled result. [src: comprehensive_metal_ecology]

### Co-occurrence and horizontal transfer

The positive co-occurrence partner signal correlates with niche breadth (Spearman ρ = 0.33–0.37 across strata). [src: comprehensive_metal_ecology] A partial analysis regressing partner count on KEGG ortholog (KO) density, with B_std as a covariate, would show whether the signal is independent of niche breadth or mediated by it. [src: comprehensive_metal_ecology]

The Firmicutes bias among partner phyla suggests non-random assembly. [src: comprehensive_metal_ecology] Computing the mean phylogenetic distance between focal genera and their partners, against a random null from the same network, would test whether the guild is phylogenetically structured. [src: comprehensive_metal_ecology] See [[concepts/co-occurrence-network-structure-and-metal-tolerance-guilds]].

The Fritz & Purvis D proxy is only an indirect measure of gene-tree/species-tree discordance. [src: comprehensive_metal_ecology] For the top-5 double-signal KOs (nrsD, merE, aoxB, shp, golS), direct single-gene phylogenies against the GTDB species tree would confirm horizontal gene transfer (HGT) at placement-level resolution. The report proposes IQ-TREE and the approximately unbiased test, to be run when assembly data become available. [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

## Caveats and Open Work

- The effect is small (r² = 0.046). [src: comprehensive_metal_ecology] Housekeeping controls also associate negatively with niche breadth, so specificity to metals is not shown. [src: comprehensive_metal_ecology]
- Archaeal replication is non-significant, likely from low power. [src: comprehensive_metal_ecology] The Firmicutes within-phylum test is borderline and non-significant. [src: comprehensive_metal_ecology]
- P5 is not independent of P1. [src: comprehensive_metal_ecology]
- The per-KO driver analysis is exploratory. [src: comprehensive_metal_ecology] The cofactor jackknife shows that one KO, K01772, shifts β substantially. [src: comprehensive_metal_ecology]
- The plasmid test rests on only 3 double-signal resistance KOs. [src: comprehensive_metal_ecology] The report notes that BV-BRC sampling estimates for large-n genes add noise. [src: comprehensive_metal_ecology]

## Slots Into

- [[concepts/metal-gene-density-and-ecological-niche-breadth]]: the primary negative PGLS association across 1,574 genera. [src: comprehensive_metal_ecology]
- [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations]]: resistance and beta-lactam AMR are null while housekeeping and cofactor categories are negative. [src: comprehensive_metal_ecology]
- [[concepts/robustness-and-replication-of-niche-breadth-associations]]: the signal holds under biome, contamination and sample-count checks, but replication is partial. [src: comprehensive_metal_ecology]
- [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]]: D and λ candidates and plasmid fractions. [src: comprehensive_metal_ecology]
- [[concepts/co-occurrence-network-structure-and-metal-tolerance-guilds]]: soil partners of metal-gene-rich focal genera more often fall in the top ko/Mb quartile. [src: comprehensive_metal_ecology]
- [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]]: temperature range is not predicted, while Cr and Co bedrock enrichment is. [src: comprehensive_metal_ecology]
- [[concepts/validity-of-curated-metal-gene-annotation]]: 113 KOs without metal-coordination clans are described as mechanistically correct. [src: comprehensive_metal_ecology]
