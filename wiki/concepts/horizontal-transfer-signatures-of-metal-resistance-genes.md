---
type: "Concept"
description: "Evidence for horizontal gene transfer of metal-related genes from phylogenetic randomness (Fritz and Purvis D versus Pagel's lambda), plasmid fractions across databases and environmental enrichment; stops at functional consequences for niche breadth."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/lab_field_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Horizontal transfer signatures of metal-resistance genes

This page covers evidence that some metal-related genes spread by horizontal gene transfer (HGT). It rests mainly on one report, comprehensive_metal_ecology, which combines phylogenetic randomness, plasmid fractions in two databases and environmental enrichment. Two further reports add context from phylogenetic signal in metal antimicrobial resistance (AMR) and from field work. The evidence is exploratory and modest. The plasmid tests are marginal and underpowered, and some candidates could not be tested. [src: comprehensive_metal_ecology] The new BV-BRC cross-category tests did not replicate the NCBI category-level signal. [src: comprehensive_metal_ecology] See [[summaries/comprehensive_metal_ecology__REPORT]], [[summaries/microbeatlas_metal_ecology__REPORT]] and [[concepts/phylogenetic-signal-of-gene-content-and-traits]].

## Literature Context

The candidate papers describe the general machinery by which metal-related genes can move between bacteria. They do not test the hub's specific statistics. Reviews describe plasmids and integrative conjugative elements as carriers of traits such as antibiotic and metal resistance. For such traits, the compounds involved may directly induce conjugative transfer [PMID 28438469](https://pubmed.ncbi.nlm.nih.gov/28438469/). Plasmids also carry metal resistance in plant-associated bacteria [PMID 30070649](https://pubmed.ncbi.nlm.nih.gov/30070649/). Acinetobacter plasmids are reported to spread heavy-metal detoxification systems alongside antibiotic resistance genes [PMID 32656745](https://pubmed.ncbi.nlm.nih.gov/32656745/). The Listeria plasmidome contains adaptive genes for resistance to heavy metals and metalloids [PMID 34638661](https://pubmed.ncbi.nlm.nih.gov/34638661/).

Several papers describe co-location of metal resistance with other resistance genes on mobile elements. Oxazolidinone resistance genes sit on mobile elements that often also carry metal and biocide resistance, so metals may co-select for them [PMID 34076490](https://pubmed.ncbi.nlm.nih.gov/34076490/). IncHI2 plasmids in swine Salmonella carried complex class 1 integrons containing antimicrobial and heavy metal genes [PMID 38695519](https://pubmed.ncbi.nlm.nih.gov/38695519/). Neomycin-resistance plasmids in Danish pig E. coli, apart from one multicopy ColRNAI plasmid, also carried genes for other antimicrobials or heavy metals, which the authors say highlights co-selection risk [PMID 37787538](https://pubmed.ncbi.nlm.nih.gov/37787538/). An environmental review likewise names heavy metals as a co-selection driver of resistome expansion through mobile elements [PMID 42308338](https://pubmed.ncbi.nlm.nih.gov/42308338/). In Cupriavidus metallidurans, laboratory culture isolated from the horizontal transfer network led to loss of genomic islands, and some strains lost key metal-resistance determinants without continuous selection [PMID 34910578](https://pubmed.ncbi.nlm.nih.gov/34910578/). That suggests metal-resistance gene content is selection-dependent and labile.

The corpus findings are consistent with this general picture and do not conflict with it. The hub's resistance KOs are enriched on plasmids. This holds in NCBI (median plasmid fraction 0.00043 vs 0.00016 for metal-dependent metabolism KOs, p = 0.023). It was not reproduced in BV-BRC (p = 0.118). Its double-signal plasmid test is marginal (p = 0.045 and p = 0.044) and underpowered, and the mer operon gene merD drives it. The mer result fits the literature's view of plasmids and integrons as vehicles for metal resistance. The null BV-BRC category comparison means the corpus cannot confirm the broader claim of plasmid enrichment across databases. The literature's idea that metal resistance tracks current selection, as in C. metallidurans, is compatible with the report's argument that resistance-gene abundance follows present selective pressure rather than ecological specialisation. That C. metallidurans evidence is a single-organism laboratory result.

The corpus extends this literature with a quantitative, genome-scale approach. It pairs Fritz and Purvis D with Pagel's λ to nominate 13 double-signal KOs, and it tests plasmid fractions and environmental enrichment. None of the candidate papers uses these measures, so the double-signal framework and its link to niche breadth are novel here and remain exploratory. D is an indirect proxy for gene-tree discordance, and the candidate papers do not validate it.

## Two-scale phylogenetic signal

The report uses two measures of phylogenetic signal. Fritz & Purvis D was computed at genome level on a GTDB 18,961-tip tree for 309 KEGG orthologs (KOs) with at least 20 genomes. D = 1 means random, HGT-like, and D = 0 means Brownian motion, vertical. [src: comprehensive_metal_ecology] Pagel's λ was computed at genus level by phylogenetic generalized least squares (PGLS) for 275 KOs. λ = 1 means strong phylogenetic signal and λ = 0 means none. [src: comprehensive_metal_ecology]

Across 275 KOs present in both datasets, D and λ were weakly and not significantly negatively correlated (Spearman ρ = −0.041, p = 0.49). The report reads this as the two metrics capturing partially independent signals. [src: comprehensive_metal_ecology] It states that the near-orthogonality validates that they capture independent evolutionary signals. [src: comprehensive_metal_ecology] The framework is exploratory, and it picks out 13 double-signal resistance/transport/sensing genes (D > 0.2, λ < 0.3) as the most likely HGT-mobile subset. [src: comprehensive_metal_ecology]

The report notes that D is only an indirect proxy for gene-tree/species-tree discordance. [src: comprehensive_metal_ecology] It proposes direct single-gene phylogenies for the top-5 double-signal KOs (nrsD, merE, aoxB, shp, golS) against the GTDB species tree, using IQ-TREE and the approximately unbiased test, once assembly data are available. [src: comprehensive_metal_ecology]

### Phylogenetic signal in metal AMR from MicrobeAtlas

A separate report interprets a phylogenetic-signal gradient as suggesting that ecological range is lineage-constrained while metal AMR is more labile, likely because mobile genetic elements (MGE) exchange AMR genes among distant taxa. [src: microbeatlas_metal_ecology] It considers intermediate metal AMR λ (0.26–0.44) consistent with Hemme et al. (2016), who found recombinational hotspots for metal resistance gene acquisition in contaminated groundwater. [src: microbeatlas_metal_ecology] It also considers core-fraction λ above total cluster-count λ consistent with Gillieatt & Coleman (2024), who reviewed mechanisms of AMR gene transfer by MGEs under metal co-selection. [src: microbeatlas_metal_ecology]

The ordering core fraction λ > type diversity λ > cluster count λ is read as consistent with mainly vertical inheritance of constitutive resistance, and with horizontal transfer and local metal exposure shaping accessory accumulation and type expansion. [src: microbeatlas_metal_ecology] That report uses Pagel's λ partitioning as a framework for separating vertically inherited repertoires from HGT-driven accessory acquisition. [src: microbeatlas_metal_ecology] It interprets a significant metal-type PGLS β, after phylogenetic control, as showing that HGT-driven metal type expansion covaries with niche breadth beyond phylogenetic relatedness. [src: microbeatlas_metal_ecology] It asserts that the HGT-labile diversity component is the one that covaries with ecological range. [src: microbeatlas_metal_ecology]

## The double-signal candidates

Thirteen KOs met the double-signal criterion of D > 0.2 and λ < 0.3. [src: comprehensive_metal_ecology] Each row gives KO, gene, category, genome-level D, genus-level λ and genome count n.

| KO | Gene | Category | D | λ | n | Claim |
|---|---|---|---|---|---|---|
| K07785 | nrsD | Resistance | 0.821 | 0.089 | 59 | [src: comprehensive_metal_ecology] |
| K19059 | merE | Resistance | 0.728 | 0.102 | 154 | [src: comprehensive_metal_ecology] |
| K19057 | merD | Resistance | 0.701 | 0.165 | 156 | [src: comprehensive_metal_ecology] |
| K19594 | gesB | Resistance | 0.597 | 0.156 | 89 | [src: comprehensive_metal_ecology] |
| K08356 | aoxB | Resistance | 0.562 | 0.000 | 259 | [src: comprehensive_metal_ecology] |
| K19595 | gesA | Resistance | 0.458 | 0.161 | 103 | [src: comprehensive_metal_ecology] |
| K25119 | shp | Resistance | 0.385 | 0.000 | 123 | [src: comprehensive_metal_ecology] |
| K03897 | iucD | Other | 0.354 | 0.237 | 362 | [src: comprehensive_metal_ecology] |
| K19592 | golS | Sensing | 0.265 | 0.135 | 144 | [src: comprehensive_metal_ecology] |
| K05908 | doxDA | Other | 0.254 | 0.000 | 241 | [src: comprehensive_metal_ecology] |
| K08170 | norB | Other | 0.239 | 0.033 | 315 | [src: comprehensive_metal_ecology] |
| K14974 | nicC | Transport | 0.224 | 0.000 | 382 | [src: comprehensive_metal_ecology] |
| K15585 | nikB | Transport | 0.202 | 0.000 | 448 | [src: comprehensive_metal_ecology] |

All 13 fall in resistance, transport or sensing categories, and none is a cofactor biosynthesis KO. The report reads this as consistent with constitutively required cofactor genes being inherited vertically. [src: comprehensive_metal_ecology] The 10 high-λ control KOs (cusA, cusC, cobN, cobT, zntR, oprJ, mexI, cnrR, cbiH60, fre; all λ > 0.7, D < 0.3) are dominated by metal homeostasis and cofactor-related genes. [src: comprehensive_metal_ecology]

The exploratory analysis compared the 13 double-signal KOs with these 10 controls on four independent evidence lines. [src: comprehensive_metal_ecology] Double-signal KOs had higher D than controls (median 0.385 vs −0.077; Mann-Whitney U (MWU) U = 123, p = 1.81×10⁻⁴). [src: comprehensive_metal_ecology] The report treats this D comparison as its strongest evidence. D was measured on the same GTDB tree as the primary PGLS, and the report equates it with gene-tree/species-tree discordance. [src: comprehensive_metal_ecology] See [[entities/gtdb]].

## Plasmid fractions

Plasmid enrichment of double-signal resistance KOs is marginal. The report says the test is underpowered and driven mainly by merD, in the Tn21-family mer operon. [src: comprehensive_metal_ecology] See [[entities/mercury-resistance-mer-genes]].

- NCBI Entrez: double-signal resistance KOs (n = 3) had a median plasmid fraction of 0.0042, against 0.0004 for background resistance KOs with n_total ≥ 50 (n = 51). MWU p = 0.045, U = 122. [src: comprehensive_metal_ecology]
- The three NCBI fractions were merD 4.3%, aoxB 0.4% and norB 0.1%. [src: comprehensive_metal_ecology]
- BV-BRC, an independent database of 84,446 plasmid accessions: p = 0.044 (n_double = 2, merD 7.2% and norB 0.3%; n_background = 48 after arsC KO deduplication). [src: comprehensive_metal_ecology] Medians were 0.0049 vs 0.0005. [src: comprehensive_metal_ecology]
- A confirmatory BV-BRC double-signal versus background resistance test gave U=84, p=0.047 (n=2 vs n=49), consistent with the original p=0.044. [src: comprehensive_metal_ecology]
- gesA and gesB (n = 1 in both databases) and nrsD (n = 16) could not be tested. [src: comprehensive_metal_ecology]
- High-plasmid background KOs (pcoB 6.8%, merA 4.5%, tetA 4.1%) fail the D or λ threshold. The report says this makes the test conservative. [src: comprehensive_metal_ecology]
- golS is effectively chromosomal in both databases (NCBI fraction 0.000017). The report suggests its HGT may have occurred chromosomally. [src: comprehensive_metal_ecology]
- NCBI mobile-element co-annotation was directionally consistent but not significant (DS n = 13 vs control n = 10; MWU p = 0.062). Both medians were 0.000. [src: comprehensive_metal_ecology]

### Plasmid fraction by functional category

NCBI plasmid fractions were higher for resistance KOs than for metal-dependent metabolism KOs (n = 54 vs 14; medians 0.00043 vs 0.00016; p = 0.023). They were also higher than for all non-resistance KOs (n = 54 vs 86; 0.00043 vs 0.00022; p = 0.020). [src: comprehensive_metal_ecology] BV-BRC did not reproduce this: resistance and non-resistance KOs did not differ significantly (n = 51 vs 82; 0.00057 vs 0.00052; p = 0.118; one-sided Mann-Whitney U=2347). [src: comprehensive_metal_ecology]

The other BV-BRC cross-category comparisons were also null: resistance over Metabolism (p=0.129), over Sensing (p=0.103) and over Transport (p=0.271). [src: comprehensive_metal_ecology] The report says the BV-BRC comparison does not replicate the NCBI p=0.020 signal. [src: comprehensive_metal_ecology] It offers two reasons. The BV-BRC Transport/Homeostasis group is inflated by functional resistance genes classified as transport (aph at 7.1%; czcA/czcB from the original 66-KO dataset), which collapses the Transport–Resistance median gap. [src: comprehensive_metal_ecology] Sampling estimates for large-n genes also add noise. [src: comprehensive_metal_ecology] These are the report's explanations, not tested results.

| Category | NCBI n | NCBI median | BV-BRC n (n≥50) | BV-BRC median | Claims |
|---|---|---|---|---|---|
| Resistance/Detoxification | 54 | 0.00043 | 51 | 0.00057 | [src: comprehensive_metal_ecology] |
| Transport/Homeostasis | 48 | 0.00021 | 46 | 0.00052 | [src: comprehensive_metal_ecology] |
| Sensing/Regulation | 21 | 0.00020 | 21 | 0.00055 | [src: comprehensive_metal_ecology] |
| Metal-dependent Metabolism | 14 | 0.00016 | 12 | 0.00033 | [src: comprehensive_metal_ecology] |
| Cofactor Biosynthesis | 2 | 0.00012 | 2 | 0.00035 | [src: comprehensive_metal_ecology] |

Only hemH and MOCS2B met n ≥ 50 in the NCBI cofactor group. cobC1 (n = 45) and ahbAB (n = 2) were excluded. [src: comprehensive_metal_ecology] In BV-BRC, only hemH (n=346,821) and cobT met n≥50; cobC1, MOCS2B, ahbAB and ahbD were excluded. [src: comprehensive_metal_ecology] The NCBI resistance-versus-cofactor comparison was underpowered and not significant (p = 0.082, n_cofactor = 2). [src: comprehensive_metal_ecology] The BV-BRC table has 154 rows, and large-n genes were estimated by 4-page sampling. [src: comprehensive_metal_ecology] Cofactor biosynthesis KOs have near-zero plasmid fractions in both NCBI and BV-BRC, with hemH ≤ 0.07%. [src: comprehensive_metal_ecology] The report reads cofactor KO plasmid fractions of ≤ 0.023% as consistent with strict chromosomal location; the claim does not name the database, and the BV-BRC cofactor median in the table above is 0.00035. [src: comprehensive_metal_ecology] It says the NCBI gradient (resistance > transport ≈ sensing > metabolism > cofactor) mirrors the λ ordering. [src: comprehensive_metal_ecology]

## Environmental enrichment

In MGnify, 5 of 8 double-signal KOs with data were enriched with environmental metals at false discovery rate (FDR) q < 0.1. [src: comprehensive_metal_ecology] See [[entities/kescience-mgnify]]. The q values were:

- nicC, 5.6×10⁻⁵ [src: comprehensive_metal_ecology]
- nikB, 2.8×10⁻⁵ [src: comprehensive_metal_ecology]
- gesA, 9.4×10⁻⁵ [src: comprehensive_metal_ecology]
- iucD, 1.1×10⁻⁴ [src: comprehensive_metal_ecology]
- norB, 7.1×10⁻² [src: comprehensive_metal_ecology]

The median absolute Spearman correlation between double-signal KO presence and bioavailable metals was |ρ| = 0.034. [src: comprehensive_metal_ecology] The KOs nrsD, merE, merD, shp and doxDA were absent from the MGnify dataset and could not be assessed. [src: comprehensive_metal_ecology]

## External context

Gios et al. (2025), as cited by the report, showed in Patescibacteria that per-Mb HGT rates are independent of genome size (1.1 HT genes/Mb regardless of genome scale). [src: comprehensive_metal_ecology] They also found that metal-linked ABC (ATP-binding cassette) cation transporters are preferentially acquired. [src: comprehensive_metal_ecology] The report reasons that a constant per-Mb rate makes resistance-gene abundance track current selective pressure rather than long-term ecological specialisation, which it says predicts the null niche-breadth signal. [src: comprehensive_metal_ecology] A field report cites Peng et al. (2022), who found that Oak Ridge *Rhodanobacter* strains acquired heavy metal resistance through HGT. [src: lab_field_ecology] See [[entities/rhodanobacter]].

## Link to niche breadth

The report presents this as a gene-level complement to its class-level null result for resistance genes and niche breadth (β ≈ 0, p = 0.66). [src: comprehensive_metal_ecology] Individual resistance genes with the highest D are the most likely to have been acquired horizontally, which decouples their abundance from ecological specialisation history. [src: comprehensive_metal_ecology] The report states that HGT-mobile resistance genes are decoupled from ecological specialisation at both the category level (niche breadth) and the individual KO level (phylogenetic randomness). [src: comprehensive_metal_ecology] See [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth]].

## Open Directions

- Test gesA, gesB and nrsD for plasmid association with a larger plasmid collection. At most one genome per database carried gesA or gesB, so the plasmid test could not run.
- Repeat the plasmid enrichment test on all 13 double-signal KOs with a permutation or gene-level model. Only 2–3 resistance KOs had n ≥ 50, so the test is underpowered and merD dominates it.
- Re-run the BV-BRC cross-category comparison after moving resistance-classified efflux genes (aph, czcA, czcB) out of Transport. This would test whether the report's inflation explanation accounts for the NCBI–BV-BRC discordance.
- Build true gene trees for merD, merE, nikB and nicC and compare them with the species tree. This would test whether D is a valid proxy for gene-tree/species-tree discordance.
- Check golS for chromosomal mobile elements such as integrons or genomic islands. This would test the report's suggestion that its HGT was chromosomal.
- Add nrsD, merE, merD, shp and doxDA to the MGnify enrichment dataset so all 13 KOs can be scored for environmental enrichment.
