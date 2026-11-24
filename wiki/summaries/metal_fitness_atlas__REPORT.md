---
type: "Summary"
description: "Summary of the project Pan-Bacterial Metal Fitness Atlas."
doc_type: "short"
full_text: "sources/metal_fitness_atlas__REPORT.md"
---
# Pan-Bacterial Metal Fitness Atlas

The Pan-Bacterial Metal Fitness Atlas asked whether genes needed to survive metal stress are mostly core or accessory in the pangenome. Its main answer is that they are enriched in the core genome, opposite to the initial hypothesis. The evidence is statistically strong in the pooled analysis across 22 organisms and 14 metals, though not every organism or metal shows it. [src: metal_fitness_atlas] The report calls it the first cross-species genome-wide metal-tolerance fitness atlas, with 383,349 gene × metal fitness records across 24 organisms and 14 metals. [src: metal_fitness_atlas] Rare-metal results rest on only 1-2 organisms. [src: metal_fitness_atlas] The report also proposes new experiments to fill coverage gaps, including rare earth elements and several critical metals. [src: metal_fitness_atlas]

## Key Findings

### Core enrichment of metal-fitness genes

This contradicts hypothesis H1a, which predicted accessory enrichment for toxic-metal genes from a prior DvH finding of 71.2% core among condition-specific heavy-metal genes. [src: metal_fitness_atlas] The report attributes the result to vulnerable core processes (cell envelope, DNA repair, central metabolism) rather than specialized metal resistance mechanisms. [src: metal_fitness_atlas] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].

- 21 of 22 organisms show metal-important genes as more core than baseline, and 14 are significant at p<0.05. [src: metal_fitness_atlas]
- The one exception is *P. fluorescens* FW300-N2E3, with a negligible negative delta (-0.003, p=0.70). [src: metal_fitness_atlas]
- 12 of 14 metals are individually significant at p<0.05. [src: metal_fitness_atlas]
- Cadmium (1 organism, delta=-0.010, p=0.92) is not significant, likely because of limited organism coverage. [src: metal_fitness_atlas]
- Uranium (2 organisms, delta=+0.035, p=0.34) is not significant, likely because of limited organism coverage. [src: metal_fitness_atlas] The report says more organisms would show whether uranium fitness genes are truly neutral or the effect was underpowered. [src: metal_fitness_atlas]
- Essential-metal tolerance genes (Fe, Mo, W, Se, Mn) have a mean core-fraction delta of +0.148, nearly double the toxic-metal delta of +0.081 (Mann-Whitney U=39, p=0.015, one-sided). [src: metal_fitness_atlas]
- The strongest enrichments are Mn (+0.198, all 30 important genes core), Zn (+0.151), Mo (+0.148), W (+0.145) and Fe (+0.116). [src: metal_fitness_atlas]

Per-metal conservation results from the atlas table (important genes, core fraction, delta, OR, p-value):

| Metal | Type | Genes | Core fraction | Delta | OR | p |
|---|---|---|---|---|---|---|
| Manganese | essential | 30 | 1.000 | +0.198 | inf | 2.0e-03 [src: metal_fitness_atlas] |
| Zinc | toxic | 1,517 | 0.890 | +0.151 | 2.94 | 2.0e-49 [src: metal_fitness_atlas] |
| Molybdenum | essential | 302 | 0.950 | +0.148 | 5.32 | 1.3e-14 [src: metal_fitness_atlas] |
| Tungsten | essential | 303 | 0.947 | +0.145 | 4.98 | 5.3e-14 [src: metal_fitness_atlas] |
| Mercury | toxic | 106 | 0.934 | +0.132 | 3.62 | 1.6e-04 [src: metal_fitness_atlas] |
| Selenium | essential | 134 | 0.933 | +0.131 | 3.59 | 2.9e-05 [src: metal_fitness_atlas] |
| Iron | essential | 651 | 0.919 | +0.116 | 3.07 | 8.5e-18 [src: metal_fitness_atlas] |
| Aluminum | toxic | 1,381 | 0.898 | +0.107 | 2.37 | 1.2e-26 [src: metal_fitness_atlas] |
| Copper | toxic | 2,139 | 0.867 | +0.090 | 1.91 | 3.8e-27 [src: metal_fitness_atlas] |
| Nickel | toxic | 1,760 | 0.877 | +0.088 | 1.93 | 3.0e-22 [src: metal_fitness_atlas] |
| Cobalt | toxic | 1,859 | 0.859 | +0.072 | 1.67 | 8.1e-16 [src: metal_fitness_atlas] |
| Chromium | toxic | 262 | 0.710 | +0.060 | 1.33 | 4.0e-02 [src: metal_fitness_atlas] |
| Uranium | toxic | 178 | 0.685 | +0.035 | 1.18 | 3.4e-01 [src: metal_fitness_atlas] |
| Cadmium | toxic | 92 | 0.522 | -0.010 | 0.96 | 9.2e-01 [src: metal_fitness_atlas] |

Removing 4 duplicate *P. fluorescens* FW300 strains (keeping pseudo3_N2E3) reduces the analysis from 22 to 18 organisms. [src: metal_fitness_atlas] Enrichment stays robust (OR=2.065, p=5.9e-141), and the report concludes it is not driven by Pseudomonas overrepresentation. [src: metal_fitness_atlas] The report nonetheless lists phylogenetic non-independence from multiple *P. fluorescens* strains as a caveat that can inflate apparent conservation. [src: metal_fitness_atlas]

### Interpretation: a two-tier model

The report reads core enrichment, not accessory enrichment, as showing that metal tolerance is about core genome robustness rather than accessory gene acquisition. [src: metal_fitness_atlas] It says the genes that matter are cell envelope integrity, DNA repair, protein quality control and central metabolism, not specialized resistance genes. [src: metal_fitness_atlas] It describes its two-tier model as only partially supported and needing reframing. [src: metal_fitness_atlas] Tier 1 (core) is general stress response, the majority of metal fitness genes, conserved for essential functions beyond metal tolerance. [src: metal_fitness_atlas] Tier 2 (accessory) is a smaller fraction giving specific resistance by efflux, sequestration or enzymatic detoxification, visible only after controlling for general stress response. [src: metal_fitness_atlas]

The report explains the earlier DvH 71.2% core result (field_vs_lab_fitness project) by that analysis isolating genes important only for metals. The atlas captures all genes with any metal fitness defect, dominated by core stress-response functions. [src: metal_fitness_atlas]

### Relation to the literature

The report says the core enrichment aligns with Borchert et al. (2019), who showed modular fitness landscapes with universally stress-sensitive core functions. [src: metal_fitness_atlas] It says the finding contradicts the assumption that metal resistance is primarily accessory (Li et al. 2017; Peng et al. 2022), but notes those studies focused on annotated resistance genes such as efflux pumps and czc operons, which are indeed accessory. [src: metal_fitness_atlas] It describes the 1,182 conserved families as extending Price et al. (2018) and as the first cross-species metal fitness atlas. [src: metal_fitness_atlas] The failure of the repertoire score to predict metal fitness is said to echo Rosconi et al. (2022): essentiality is context-dependent and not predictable from gene presence alone. [src: metal_fitness_atlas]

### Coverage and magnitude of metal fitness data

The Fitness Browser (FB) holds 559 metal-related experiments, 8.2% of 6,804 total, covering 16 metals. [src: metal_fitness_atlas] Coverage is uneven. Six metals have at least 3 organisms: cobalt (27 organisms), nickel (26), copper (23), aluminum (22), zinc (17) and iron (3). [src: metal_fitness_atlas] Aluminum, cobalt and nickel are the three United States Geological Survey (USGS) critical minerals with broad FB coverage. [src: metal_fitness_atlas] DvH is the most metal-profiled organism, with 149 experiments across 13 metals. [src: metal_fitness_atlas] The atlas has metal data for 31 organisms, 24 of them with fitness matrices. [src: metal_fitness_atlas]

Significant defects (fit < -1, |t| > 4) occur in 3.3% of gene × metal records (12,838 / 383,349). [src: metal_fitness_atlas] The strict category holds 5,667 metal-important genes (1.5%). [src: metal_fitness_atlas] Iron and essential-metal limitation give the highest important-gene fractions (12.3% for Fe, 11.2% for Mo/W). [src: metal_fitness_atlas] Toxic metals cluster around 2.7-4.4%. [src: metal_fitness_atlas] DvH has 1,366 metal-important genes, 49.8% of its genome across 13 metals. [src: metal_fitness_atlas] The cyanobacterium *Synechococcus elongatus* (SynE) is notably metal-sensitive, with 33.6% of genes important across just 2 metals. [src: metal_fitness_atlas]

### Conserved gene families and novel candidates

Of 2,891 ortholog groups with metal phenotypes, 1,182 are conserved across ≥2 organisms. [src: metal_fitness_atlas] 601 are conserved across ≥3 organisms. [src: metal_fitness_atlas] The most broadly conserved family, OG00128, spans 17 organisms and 9 metals. [src: metal_fitness_atlas] Families with metal phenotypes in more organisms tend to have higher pangenome conservation (% core), consistent with fundamental cellular processes. [src: metal_fitness_atlas]

The atlas identifies 149 novel metal-biology candidates. These have conserved metal fitness phenotypes across ≥2 organisms but lack full functional annotation. [src: metal_fitness_atlas] They break down into 89 truly unknown families, 43 with DUF/UPF domains and 17 with partial functional hints such as "transporter" or "hydrolase". [src: metal_fitness_atlas] These are function predictions based solely on cross-species fitness data. [src: metal_fitness_atlas]

### Metal-responsive modules

Independent component analysis (ICA) modules were scored with module activity z-scored across all experiments per organism. This gave 600 metal-responsive module records at |z| > 2.0 among 19,453 module × metal-experiment records (3.1%) across 31 organisms. [src: metal_fitness_atlas] DvH leads with 47 responsive modules across 12 metals, while psRCH2 has 11 across 6 metals. [src: metal_fitness_atlas] The 183 responsive modules with conservation data have a mean core fraction of 0.826, consistent with core enrichment of metal-fitness genes. [src: metal_fitness_atlas] Their median is 0.929, so most are predominantly core. [src: metal_fitness_atlas] An initial attempt using raw activity scores (max 0.96) gave 0 responsive modules because of the scale mismatch with z-scores. Per-experiment profiles with z-normalization resolved this. [src: metal_fitness_atlas]

### Pangenome-scale prediction

A signature of 1,286 KEGG ortholog (KO) terms from conserved metal gene families was used to score all 27,702 pangenome species. [src: metal_fitness_atlas] Without normalization, species with large open pangenomes (*K. pneumoniae*, *P. aeruginosa*) dominate, reflecting genome size rather than metal biology. [src: metal_fitness_atlas] After normalizing by metal clusters / total KEGG-annotated clusters, specialist bioleaching organisms emerge. *Leptospirillum* ranks at the 91st percentile, *Acidithiobacillus* at the 77th, *Marinobacter* at the 75th and *Sulfobacillus* at the 71st. [src: metal_fitness_atlas] The report calls Leptospirillum the highest-scoring bioleaching genus after normalization, and calls *Acidithiobacillus ferrooxidans* the #1 bioleaching organism. [src: metal_fitness_atlas] *Geobacter sulfurreducens*, described as a model metal-reducing bacterium, sits at the 53rd percentile. [src: metal_fitness_atlas] As a group, however, bioleaching genera are not significantly enriched over background (Mann-Whitney p=0.17). This indicates that metal-tolerance genes are broadly distributed rather than concentrated in specialists. [src: metal_fitness_atlas]

## Proposed Experiments to Close Coverage Gaps

The report states that six metals on the USGS critical minerals list are tested in only 1-2 organisms and proposes coverage of 5+ organisms each, which would enable the cross-species conservation analysis. [src: metal_fitness_atlas] See [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]]. All of these are proposals, not results.

- **Manganese:** one organism (DvH) is covered, and it shows 100% core enrichment (delta=+0.198). [src: metal_fitness_atlas] The report proposes RB-TnSeq (random barcode transposon sequencing) in MR-1, Keio, Cup4G11, Putida and Caulo. [src: metal_fitness_atlas] Manganese is a USGS critical mineral, and *Shewanella* MR-1 can reduce Mn(IV), which would test whether metal reducers differ in conservation. [src: metal_fitness_atlas]
- **Chromium:** two organisms (DvH, psRCH2) are covered. [src: metal_fitness_atlas] The report proposes RB-TnSeq in MR-1, Cup4G11, Keio and pseudo3_N2E3. [src: metal_fitness_atlas] Chromium is a DOE priority contaminant. [src: metal_fitness_atlas] The Oak Ridge FW300 *Pseudomonas* strains were isolated from chromium-contaminated groundwater but have never been tested against chromate. [src: metal_fitness_atlas]
- **Uranium:** two organisms (DvH, psRCH2) are covered. [src: metal_fitness_atlas] The nonsignificant delta=+0.035 (p=0.34) leaves neutrality versus underpowering unresolved. [src: metal_fitness_atlas] The report proposes experiments in MR-1, ANA3, PV4 and Cup4G11. [src: metal_fitness_atlas] Uranium is the central ENIGMA contaminant, and MR-1 can reduce U(VI). [src: metal_fitness_atlas]
- **Tungsten:** one organism (DvH) is covered, with strong core enrichment (delta=+0.145). [src: metal_fitness_atlas] Tungsten is a USGS critical mineral and an essential cofactor for some enzymes. [src: metal_fitness_atlas] The report proposes testing Methanococcus_S2, Methanococcus_JJ and Keio to see whether tungsten dependence is unique to sulfate reducers. [src: metal_fitness_atlas]
- **Rare earth elements:** the Fitness Browser contains no rare earth element experiments. [src: metal_fitness_atlas] The report describes them as the most strategically important critical minerals, with bioleaching and biorecovery a rapidly growing field. [src: metal_fitness_atlas] It proposes lanthanum chloride at 0.1-1 mM in Putida, Cup4G11, Keio and Marino to identify the first genome-wide rare earth tolerance gene set. [src: metal_fitness_atlas] *Pseudomonas putida* and *Gluconobacter* are studied for rare earth biosorption. [src: metal_fitness_atlas] It also proposes cerium chloride at 0.1-1 mM on the same panel to separate shared from element-specific tolerance genes. [src: metal_fitness_atlas] Cerium is the most abundant rare earth element. [src: metal_fitness_atlas]
- **Organisms with many candidates but little testing:** two organisms each have 54 novel metal candidate genes but were tested only against iron, and the report proposes a standard metal panel to validate or refute the predictions. [src: metal_fitness_atlas] *Methanococcus maripaludis* S2 has 54 novel ortholog groups and iron-only testing. [src: metal_fitness_atlas] The report proposes Ni, Co, Cu, Zn, W and Mo tests, noting archaea are underrepresented in metal tolerance studies. [src: metal_fitness_atlas] It is a methanogen with Ni requirements for hydrogenase and W/Mo requirements for formylmethanofuran dehydrogenase. [src: metal_fitness_atlas] Strain JJ also has 54 novel ortholog groups and iron-only testing. [src: metal_fitness_atlas] The report proposes the same panel for JJ to reveal strain-specific metal adaptation. [src: metal_fitness_atlas]
- ***Pseudomonas putida* KT2440:** it has Fitness Browser fitness matrices but zero metal experiments and is the only FB organism with no metal data. [src: metal_fitness_atlas] It is a workhorse for bioremediation and metabolic engineering. [src: metal_fitness_atlas] The report proposes testing Co, Ni, Cu, Zn, Al, Cr and U to link the atlas to the engineering literature. [src: metal_fitness_atlas] Putida has the 5th-highest metal gene repertoire score among FB organisms (0.707), so testing would validate or refute that prediction. [src: metal_fitness_atlas]
- **Bioleaching and metal-reducing species:** the atlas cannot validate predictions for organisms without RB-TnSeq libraries. [src: metal_fitness_atlas] The report proposes libraries for key bioleaching species to bridge the gap to industrial applications. [src: metal_fitness_atlas] No TnSeq data exists for any *Acidithiobacillus* species. [src: metal_fitness_atlas] RB-TnSeq in *A. ferrooxidans* under Fe, Cu, Co, Ni and Zn would give the first genome-wide functional map of bioleaching gene requirements. [src: metal_fitness_atlas] In *G. sulfurreducens*, Fe(III), Mn(IV) and U(VI) reduction conditions would identify genes for extracellular electron transfer and metal transformation. [src: metal_fitness_atlas] In *L. ferrooxidans*, Fe(II) oxidation and acid conditions would reveal why the genus specializes in bioleaching environments. [src: metal_fitness_atlas]

If performed, the report projects the experiments would expand the atlas from 14 to 16+ metals (adding rare earth elements), [src: metal_fitness_atlas] from 24 to 27+ organisms with fitness data, [src: metal_fitness_atlas] and from 1-2 organisms for critical metals to 5+. [src: metal_fitness_atlas] Cross-species statistical power for manganese, chromium, uranium and tungsten would rise from suggestive to definitive. [src: metal_fitness_atlas] The 149 novel gene candidates could be validated directly in organisms where they are predicted to be important. [src: metal_fitness_atlas]

## Data and Methods

The conservation analysis covers 22 of 31 metal-tested organisms (71%). [src: metal_fitness_atlas] The 9 excluded organisms (Putida, Keio, SynE, Miya, Kang, BFirm, Cola, Ponti, Dino) lack FB-pangenome links. [src: metal_fitness_atlas] The report considers systematic bias unlikely because they are taxonomically diverse. [src: metal_fitness_atlas] Another report statement gives 22 of 48 organisms with pangenome links, leaving 26 without Fitness Browser–pangenome mappings. [src: metal_fitness_atlas]

Data came from the KBase Data Lakehouse. From kescience_fitnessbrowser the report used genefitness, expcondition, experiment and ortholog tables. [src: metal_fitness_atlas] From kbase_ke_pangenome it used gene_cluster and eggnog_mapper_annotations. [src: metal_fitness_atlas]

## Caveats and Open Work

- Cadmium and uranium show no significant core enrichment, which the report attributes likely to limited organism coverage. [src: metal_fitness_atlas]
- The 9 organisms without FB-pangenome links are excluded from the conservation analysis. [src: metal_fitness_atlas]
- There is no dose-response normalization. Concentrations vary across organisms (nickel 0.01-2.0 mM), and fitness effects depend on concentration relative to each organism's tolerance threshold. [src: metal_fitness_atlas]
- The metal-important definition (fit < -1 OR n_sick ≥ 1, ~3.3% of genes) is broad, and most such genes are general stress genes rather than metal-specific. [src: metal_fitness_atlas]
- Putatively essential genes (~14.3% of protein-coding genes, ~82% core) lack insertions and are excluded, so the observed core enrichment is a conservative estimate. [src: metal_fitness_atlas]
- Repertoire prediction failed validation: gene presence/absence does not predict metal tolerance, and a regulatory or expression-based model is needed. [src: metal_fitness_atlas]
- Predictions for unknown genes rest only on cross-species fitness data. [src: metal_fitness_atlas]
- Unnormalized pangenome scores reflect genome size rather than metal biology. [src: metal_fitness_atlas]
- The atlas scores 27,702 species but cannot validate predictions for organisms without RB-TnSeq libraries. [src: metal_fitness_atlas]
- No rare earth element experiments exist in the Fitness Browser, and Putida has no metal experiments. [src: metal_fitness_atlas]

Next analyses the report proposes:

- Repeat the conservation analysis using only genes important for metals but not other stresses, to separate the core stress response from metal-resistance gene evolution. [src: metal_fitness_atlas]
- Use PaperBLAST, InterPro and AlphaFold structural prediction on the 89 truly unknown and 43 DUF-domain families among the 149 novel candidates. [src: metal_fitness_atlas]
- Normalize fitness effects by metal concentration relative to MIC for fair cross-species comparison. [src: metal_fitness_atlas]
- Apply phylogenetic independent contrasts to control phylogenetic non-independence. [src: metal_fitness_atlas]
- Replace count-based pangenome metal scores with per-species hypergeometric enrichment tests controlling total functional annotation content. [src: metal_fitness_atlas]

Declined data-file and notebook inventory claims are omitted as file inventory.
