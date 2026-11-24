---
type: "Concept"
description: "How metal-gene density relates to genus niche breadth along geochemical, climatic, pH and organic-matter axes, and how well environment predicts community metal-gene content."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md"]
---
# Environmental drivers of genus niche breadth and metal-gene density

This page covers how metal-gene density relates to genus niche breadth along latitude, bedrock geochemistry, climate, pH and organic-matter-related axes, and how well environment predicts community metal-gene content. All results come from one report, [[summaries/comprehensive_metal_ecology__REPORT]], and most are labelled exploratory. Metal-gene density predicts narrower pH and composite niches but not temperature range. Environment predicts community metal-gene content poorly. [src: comprehensive_metal_ecology] The metal-gene niche-breadth coefficient survived every geochemical and climate covariate tested. Bedrock chemistry, especially chromium, predicted niche breadth, but contemporary soil metal measures did not. [src: comprehensive_metal_ecology] Later models show the bedrock chromium signal is not mediated by soil moisture. Soil organic matter independently predicts narrower niches and absorbs the pH association. [src: comprehensive_metal_ecology]

## Literature Context

The candidate papers are site-scale studies of contaminated or amended soils and sediments. They do not address genus niche breadth. They show that measured metals, pH and other local variables are often associated with community and metal-resistance-gene (MRG) composition, but the drivers differ by site.

In a decommissioned uranium-containing polymetallic mine in southwest China, redundancy analysis (RDA) identified arsenic, lithium and moisture as key drivers of community assembly, and lithium specifically as a driver of MRGs in soil [PMID 41016211](https://pubmed.ncbi.nlm.nih.gov/41016211/). In industrial soils of East Kazakhstan, long-read metagenomics found that heavy metals, particularly Zn, shaped community structure and ARG and MRG composition, and RDA identified Zn and soil pH as the principal drivers [PMID 42182018](https://pubmed.ncbi.nlm.nih.gov/42182018/). In Brazilian Cerrado soils receiving composted manure, pH and phosphorus shaped the resistome at uncontaminated sites, while Cu was the dominant driver at the one naturally metal-rich site [PMID 40934669](https://pubmed.ncbi.nlm.nih.gov/40934669/). In a Pb-Zn mine restoration, available lead and cadmium influenced archaea diversity and functional genes, pH affected phosphorus dynamics through bacterial diversity, and vegetation directly influenced metal dynamics [PMID 40054196](https://pubmed.ncbi.nlm.nih.gov/40054196/). In farmland around gold tailings, the microbial community was the most influential driver of soil ARGs, and heavy metals had direct and partially indirect effects [PMID 34030239](https://pubmed.ncbi.nlm.nih.gov/34030239/). A microcosm experiment after 16 years of biosolids application indicated heavy metals as the primary selective pressure, potentially driving simultaneous enrichment of metal and antibiotic resistance genes [PMID 40834540](https://pubmed.ncbi.nlm.nih.gov/40834540/). Along a heavy-metal contamination gradient in sediments, functional composition was more tightly linked to environmental drivers than taxonomic composition, and many resistance genes derived from Geobacter [PMID 27301322](https://pubmed.ncbi.nlm.nih.gov/27301322/). In river sediments, effective sulfur drove metal bioavailability [PMID 39608434](https://pubmed.ncbi.nlm.nih.gov/39608434/).

The corpus's per-KO and community-level results are broadly consistent with this picture, in that metals and pH relate to metal-gene content. The report's NB28 partitioning found a metal-unique fraction (R²=0.064) larger than the pH+climate fraction (R²=0.041). These values are unadjusted and descriptive. This fits the contaminated-site finding that metals matter, but it comes from a global survey of mostly uncontaminated samples, so it does not directly replicate those studies. The report's pH signal, which became non-significant (p = 0.39) once soil organic matter was added, parallels the site studies in which pH matters in some settings and metals in others [PMID 40934669](https://pubmed.ncbi.nlm.nih.gov/40934669/) [PMID 42182018](https://pubmed.ncbi.nlm.nih.gov/42182018/). The candidates did not test organic matter as a mediator of pH, so that result is not confirmed or contradicted by them.

The corpus's main claims are novel relative to these candidates. These claims are that metal-gene density predicts narrower genus pH and composite niches but not temperature range, that the coefficient survives geochemical and climate covariates, that bedrock chromium predicts niche breadth while contemporary soil metal measures do not, and that environment poorly predicts community metal-gene content in held-out regions. None of the candidate papers measured genus-level niche breadth, bedrock geochemistry or spatially blocked prediction. They extend the context only at the level of environmental drivers of MRGs. The report's exploratory, genus-level results should be read as hypotheses beside this site-scale evidence.

## Latitude as a suppressor of the niche-breadth association

Adding mean latitude as a covariate amplified the metal-gene coefficient from 0.021 to 0.031 (−51.8% attenuation, p <10⁻⁴). [src: comprehensive_metal_ecology] The report calls this the opposite of confounding and reads it as collinearity between latitude and metal-gene density that partially suppresses the unadjusted coefficient. [src: comprehensive_metal_ecology] It interprets metal-gene-rich genera as disproportionately found at lower latitudes, where genera are also more specialised. [src: comprehensive_metal_ecology] It hypothesises that higher geochemical heterogeneity and stable climate let narrow-niche specialists persist without metabolic versatility. [src: comprehensive_metal_ecology] On this reading, latitude control removes a between-latitude composition effect and reveals a stronger within-latitude association. [src: comprehensive_metal_ecology] The report calls this consistent with metal-homeostasis specialists tracking geochemically diverse low-latitude environments. It also says geographic composition partially masks the genomic-investment/niche-breadth relationship. [src: comprehensive_metal_ecology]

### Mechanism tests

Nine PGLS models (phylogenetic generalized least squares) tested whether bedrock geochemistry (H4a) or climate stability (H4b) explains the suppressor effect. [src: comprehensive_metal_ecology] The inputs were genus covariates from arkinlab_microbeatlas (10,040 genera returned, 1,224 matched to the PGLS input) and GeoROC bedrock metal concentrations. CMMI ore-deposit proximity was available for n=1,161 genera. [src: comprehensive_metal_ecology] In the models listed in the table below, β_metal stayed negative; its p-value was below 0.001 in every model except the small SoilTemp model G (p = 0.074). Latitude itself was never significant (p = 0.20–0.78). [src: comprehensive_metal_ecology] The report's summary of the Q4 mechanism results also states that β_metal was stable across all models. [src: comprehensive_metal_ecology]

| Model | n | β_metal (p) | Added covariate |
|---|---|---|---|
| A: metal + abs. latitude | 1,224 | −0.0207 (6.6×10⁻⁸) | none; β_lat = −0.0017, p = 0.577 [src: comprehensive_metal_ecology] |
| B: + GeoROC bedrock metals | 1,221 | −0.0193 (4.6×10⁻⁷) | β = +0.0120, p = 2.2×10⁻⁴ [src: comprehensive_metal_ecology] |
| C: + ERA5 temperature range | 1,223 | −0.0206 (6.5×10⁻⁸) | β = +0.0136, p = 9.6×10⁻⁵ [src: comprehensive_metal_ecology] |
| D: + CMMI proximity | 1,161 | −0.0213 (5.9×10⁻⁸) | β = −0.0030, p = 0.375 [src: comprehensive_metal_ecology] |
| E: + CSU PF1 bioavailable mobility | 1,108 | −0.0209 (1.7×10⁻⁷) | β = +0.0040, p = 0.227 [src: comprehensive_metal_ecology] |
| F: + Science 2025 soil metal hazard quotient | 1,088 | −0.0208 (2.3×10⁻⁷) | β = +0.0037, p = 0.291 [src: comprehensive_metal_ecology] |
| G: + SoilTemp range at −10cm | 207 | −0.0194 (0.074) | β = +0.0238, p = 0.0085 [src: comprehensive_metal_ecology] |
| H: + ecotapestry mafic score | 975 | −0.0233 (2.2×10⁻⁸) | β = +0.0088, p = 0.013 [src: comprehensive_metal_ecology] |
| I: + USGS (United States Geological Survey) REE deposit proximity | 1,224 | −0.0208 (5.6×10⁻⁸) | β = +0.0031, p = 0.318 [src: comprehensive_metal_ecology] |

Bedrock metals, temperature range, soil temperature range and mafic score were significant positive predictors of niche breadth. Ore-deposit proximity, REE deposit proximity, bioavailable mobility and soil hazard quotients were not. [src: comprehensive_metal_ecology] In the report's mechanism summary, the H4a composite bedrock association (β=+0.012, p=2.2×10⁻⁴) was driven by Cr (BH p=6.7×10⁻⁹) and Co (BH p=0.0084), mafic score gave β=+0.009 (p=0.013), and ERA5 temperature gave β=+0.014 (p=9.6×10⁻⁵). [src: comprehensive_metal_ecology]

Across all nine models β_metal ranged from −0.019 to −0.023. [src: comprehensive_metal_ecology] The 7% attenuation in Model B was the largest reduction, and the slight amplification in geographically restricted Model H (n = 975 genera) brackets the upper end. [src: comprehensive_metal_ecology] In full-sample Model C, temperature left β_metal fully unchanged. Climate variability predicted niche breadth independently but did not explain the metal-gene association. [src: comprehensive_metal_ecology] The report concludes the primary finding is robust to all covariates tested. [src: comprehensive_metal_ecology]

### Hypothesis verdicts

The report considers H4a (bedrock geochemistry) supported by two independent proxies, GeoROC metal concentration and the ecotapestry mafic/felsic score. β_metal attenuated by ≤13% in both bedrock models and stayed highly significant. [src: comprehensive_metal_ecology] It considers H4b (climate stability) supported by two independent temperature metrics, ERA5 temperature range and SoilTemp measured soil temperature range. [src: comprehensive_metal_ecology] Model G is underpowered: it has only 94 0.5° bins and 207 matched genera, and β_metal loses significance, so it confirms direction only. [src: comprehensive_metal_ecology]

The report contrasts significant bedrock associations with null contemporary soil metal (Model F, Model E). It suggests the bedrock association reflects deep evolutionary or long-term ecological filtering rather than contemporary metal exposure. This is an interpretation, not a tested result. [src: comprehensive_metal_ecology]

## Niche axes: pH, temperature and composite gradient

This analysis was exploratory. [src: comprehensive_metal_ecology] pH niche width is max(soil pH) − min(soil pH) across a genus's MicrobeAtlas 16S sampling sites. [src: comprehensive_metal_ecology] Temperature range is the analogous span of mean annual temperature. The composite gradient is the first principal component of standardised pH, temperature and precipitation site coordinates. [src: comprehensive_metal_ecology] Predictors were z-scored KO (KEGG ortholog) density. [src: comprehensive_metal_ecology]

Metal-gene density predicted a narrower soil pH niche (n = 1,195, β = −0.760, SE = 0.233, p = 0.001, λ = 0.11). [src: comprehensive_metal_ecology] It predicted a narrower composite gradient, described as the strongest signal (n = 1,172, β = −0.064, SE = 0.017, p <0.001). [src: comprehensive_metal_ecology] It did not predict temperature range (n = 1,195, β = +0.079, SE = 0.886, p = 0.929). [src: comprehensive_metal_ecology]

The report attributes the pH result to pH-dependent metal speciation, which would constrain metal specialists to pH conditions where their genes give effective homeostasis. [src: comprehensive_metal_ecology] The pH signal predicts that metal-gene-rich genera cluster at lower pH, where Cr(VI)/Cu²⁺ speciation is most reactive. [src: comprehensive_metal_ecology] The report proposes overlaying genus pH optima onto metal-speciation pH curves to test this mechanistically. [src: comprehensive_metal_ecology] It also cautions that the pH signal may be partially mediated by soil organic matter: high-SOM acidic soils such as boreal peatlands are metal-speciation niches where SOM-metal chelation may confound a direct pH → speciation → specialist-selection interpretation. [src: comprehensive_metal_ecology] It says the temperature null contrasts with its primary thermal-stability framework. [src: comprehensive_metal_ecology] It also states that temperature tolerance depends mainly on membrane composition and chaperones, not metal processing. [src: comprehensive_metal_ecology] Pagel's λ for pH niche (0.11–0.20) is much lower than for Levins' B_std (0.757). The report reads this as environmental-axis niches being shaped mostly by ecology rather than phylogeny. [src: comprehensive_metal_ecology] See [[concepts/phylogenetic-signal-of-gene-content-and-traits]].

### Bedrock and soil chemistry

Cr and Co bedrock enrichment, both associated with mafic geology, positively predicts niche breadth after controlling for metal genes. [src: comprehensive_metal_ecology] The report suggests pH and mafic-geology signals may reflect a shared soil-chemistry axis that structures niche breadth independently. [src: comprehensive_metal_ecology] It describes serpentine/ultramafic soils as Mg/Ca-rich, Ca-dominated and often alkaline. [src: comprehensive_metal_ecology] See [[entities/chromium]] and [[entities/cobalt]].

Cross-referencing KO density with ore-deposit proximity (CMMI database, n = 18–19 regions) gave weak, non-significant, exploratory correlations. Cu r = 0.34 (p = 0.17), Zn r = 0.34 (p = 0.17) and Pb r = 0.01 (p = 0.99). [src: comprehensive_metal_ecology]

## Per-metal GeoROC bedrock models

The per-metal GeoROC PGLS models use genus-level medians of log(ppm+1) queried from Spark. They model niche breadth with metal-gene density, absolute latitude and a bedrock-metal covariate, optionally with pH. [src: comprehensive_metal_ecology] Collinearity was low: VIFs (variance inflation factors) were Cu 1.16, Ni 1.87, Zn 1.14, Co 1.26, Pb 1.12 and Cr 1.83. The report therefore treats bedrock metals as near-independent at genus scale and the per-metal and joint models as valid without regularisation. [src: comprehensive_metal_ecology]

Only Cr and Co bedrock terms were significant after Benjamini-Hochberg (BH) correction in the J models (no pH control). Metal-gene density stayed near −0.020 in every model. [src: comprehensive_metal_ecology]

| Metal | n | β_metal (p), model J | β_bedrock, J (p raw / BH) | β_bedrock, K with pH (p) | β_pH, K (p) |
|---|---|---|---|---|---|
| Cu | 1,212 | −0.0208 (6.6×10⁻⁸) | −0.0036 (0.235 / 0.333) [src: comprehensive_metal_ecology] | −0.0024 (0.437, NS) | +0.0110 (7.9×10⁻⁴) [src: comprehensive_metal_ecology] |
| Ni | 1,220 | −0.0206 (8.2×10⁻⁸) | +0.0015 (0.614 / 0.614) [src: comprehensive_metal_ecology] | +0.0017 (0.557, NS) | +0.0117 (2.7×10⁻⁴) [src: comprehensive_metal_ecology] |
| Zn | 1,213 | −0.0210 (4.5×10⁻⁸) | −0.0034 (0.278 / 0.333) [src: comprehensive_metal_ecology] | −0.0033 (0.289, NS) | +0.0114 (4.3×10⁻⁴) [src: comprehensive_metal_ecology] |
| Co | 1,214 | −0.0215 (1.9×10⁻⁸) | +0.0091 (2.8×10⁻³ / 8.4×10⁻³) [src: comprehensive_metal_ecology] | +0.0072 (0.020) | +0.0100 (2.3×10⁻³) [src: comprehensive_metal_ecology] |
| Pb | 1,220 | −0.0209 (5.4×10⁻⁸) | +0.0042 (0.181 / 0.333) [src: comprehensive_metal_ecology] | +0.0027 (0.392, NS) | +0.0113 (5.3×10⁻⁴) [src: comprehensive_metal_ecology] |
| Cr | 1,220 | −0.0203 (7.8×10⁻⁸) | +0.0187 (1.1×10⁻⁹ / 6.7×10⁻⁹) [src: comprehensive_metal_ecology] | +0.0176 (1.0×10⁻⁸) | +0.0095 (3.0×10⁻³) [src: comprehensive_metal_ecology] |

The report calls Cr the dominant driver of the composite GeoROC signal, unchanged after pH control. It reads Cr enrichment as mafic/ultramafic bedrock, consistent with the ecotapestry mafic-score model. [src: comprehensive_metal_ecology] It says Cr speciation is redox-dominated rather than pH-dominated, which explains why pH control does not attenuate the Cr signal. [src: comprehensive_metal_ecology] Co is a secondary contributor that is attenuated but survives pH control, and Co is also enriched in mafic rocks and komatiites. [src: comprehensive_metal_ecology] Cu, Ni, Zn and Pb were not significant after FDR (false discovery rate) correction, so the report concludes common ore-forming metals do not drive the composite signal. [src: comprehensive_metal_ecology]

pH was a positive predictor in every K model (β ≈ +0.011, p < 0.001). The report first reads this as a genuine speciation/ecology signal distinct from the geological metal effect. [src: comprehensive_metal_ecology] Its mechanism summary likewise records pH as positive in all K models (p < 0.001). [src: comprehensive_metal_ecology] The SOM models below revise this reading.

### Joint and composite models

In the joint M model with all six bedrock metals (VIF < 2), n = 1,207 and β_metal = −0.022 (p = 6×10⁻⁹). [src: comprehensive_metal_ecology] Cr was dominant (β = +0.0301, p = 9.5×10⁻¹³). [src: comprehensive_metal_ecology] Ni reversed sign to −0.0164 (p = 5.5×10⁻⁵), a suppressor effect relative to Cr. [src: comprehensive_metal_ecology] Pb was positive (β = +0.0072, p = 0.030). [src: comprehensive_metal_ecology] Co (β = +0.0046, p = 0.171), Cu (β = −0.0011, p = 0.736) and Zn (β = −0.0016, p = 0.630) were not significant. [src: comprehensive_metal_ecology] The report advises cautious interpretation of the Ni reversal. It views it as a partial-regression effect consistent with Cr and Ni sharing mafic rock association, and as exploratory. [src: comprehensive_metal_ecology]

In PCA (principal component analysis) models, PC1 (positive loadings on all metals, 47% var) had β = +0.009, p = 0.0025. PC2 (contrast axis, 22% var) had β = −0.007, p = 0.029. [src: comprehensive_metal_ecology]

### Redox and organic-matter proxies

The report tested globally comprehensive soil proxies from enriched_metadata_gee as speciation controls for the Cr and Co signals. Soil moisture links high values to waterlogging, anaerobic conditions and immobile Cr(III). [src: comprehensive_metal_ecology] Soil organic matter at 0 cm links high values to microbial oxygen drawdown and reducing capacity. [src: comprehensive_metal_ecology] Direct Cr(VI) data are unavailable globally: the CSU BCR fraction fields are all-null, WoSIS holds only pH/OC/texture, GEMAS is Europe-only (4,343 pts) and NGSA mobile chromium is Australia-only (1,315 pts). [src: comprehensive_metal_ecology] In genus-level correlations (n ≈ 1,213–1,218), soil moisture was not significantly correlated with bedrock Cr (r = −0.050, p = 0.083) but was negatively correlated with bedrock Co (r = −0.140, p = 9.3×10⁻⁷). [src: comprehensive_metal_ecology] SOM (0 cm) was not significantly correlated with bedrock Cr (r = −0.015, p = 0.597) or bedrock Co (r = −0.047, p = 0.103). [src: comprehensive_metal_ecology] The report reads bedrock Cr as near-orthogonal to both redox proxies, and Co-rich bedrock as modestly drier and more oxidizing, consistent with mafic terrain. [src: comprehensive_metal_ecology]

#### Moisture does not mediate the chromium signal

Adding soil moisture to the niche-breadth models left the bedrock signals in place. In the N_Cr model (n = 1,219 genera), bedrock Cr had β = +0.0175 (p = 1.2×10⁻⁸), pH β = +0.0117 (p = 5.4×10⁻³) and moisture β = +0.003 (p = 0.44, NS). [src: comprehensive_metal_ecology] In the N_Co model (n = 1,213), bedrock Co had β = +0.0072 (p = 0.021), pH β = +0.0120 (p = 5.2×10⁻³) and moisture β = +0.003 (p = 0.50, NS). [src: comprehensive_metal_ecology] The report concludes the Cr niche-width signal is not mediated by soil redox, and that the moisture test rules out a Cr(VI)-via-reducing/waterlogged-soils pathway. [src: comprehensive_metal_ecology] It proposes that chronic Cr(III)/Ni/Mg stress in serpentine soils, or several correlated ultramafic-terrain factors (Ca/Mg ratio, soil structure, slow weathering), could explain the signal. These are proposed mechanisms, not tested ones. [src: comprehensive_metal_ecology]

#### Soil organic matter narrows niches and absorbs pH

With SOM added, SOM was independently negative. In the N_Cr_som model (n = 1,218), bedrock Cr had β = +0.0187 (p = 1.3×10⁻⁹), pH β = +0.003 (p = 0.39, NS) and SOM β = −0.0155 (p = 6.8×10⁻⁵). [src: comprehensive_metal_ecology] In the N_Co_som model (n = 1,213), bedrock Co had β = +0.0075 (p = 0.016), pH β = +0.005 (p = 0.21, NS) and SOM β = −0.0134 (p = 6.6×10⁻⁴). [src: comprehensive_metal_ecology] The report states SOM β = −0.016 (p = 6.8×10⁻⁵) in the Cr model. [src: comprehensive_metal_ecology] Including SOM absorbed the pH association, which moved from p ≈ 0.003 in K models to p = 0.39. [src: comprehensive_metal_ecology] The report calls the SOM effect an incidental finding outside the original model set. [src: comprehensive_metal_ecology] It interprets the "broader niches at high pH" signal as largely mediated through or confounded with SOM, since high-SOM boreal and peatland environments tend to be acidic. It proposes that SOM may act through DOM chelation of metals more directly than pH does. [src: comprehensive_metal_ecology] This **refines** the first reading of pH as a distinct speciation signal. [src: comprehensive_metal_ecology]

## Per-KO environmental drivers

An exploratory PGLS tested 9 TIER1 KOs detectable in the [[entities/kbase-data-lakehouse]] pangenome against 22 environmental niche-breadth responses. The responses were metal concentrations from GeoROC, NGSA-ICP and NGSA-MMI. [src: comprehensive_metal_ecology] Of 198 models, 32 were significant at p < 0.05 (16.2%) and 28 at FDR q < 0.1. [src: comprehensive_metal_ecology]

| KO | Gene | Significant responses |
|---|---|---|
| K03446 | emrB | 11; strongest Ni (GeoROC) β = 8.45, t = 5.01, p = 6.0×10⁻⁷ [src: comprehensive_metal_ecology] |
| K17686 | copA | 8 [src: comprehensive_metal_ecology] |
| K07787 | cusA | 6; strongest Hg (NGSA-MMI) t = 3.14, p = 0.002 [src: comprehensive_metal_ecology] |
| K07785 | nrsD | 3; strongest Cr (NGSA-MMI) t = 4.36, p = 1.4×10⁻⁵ [src: comprehensive_metal_ecology] |
| K07665 | cusR | 2 [src: comprehensive_metal_ecology] |
| K03325 | ACR3 | 1 [src: comprehensive_metal_ecology] |
| K15726 | czcA | 1 [src: comprehensive_metal_ecology] |
| K19594 | gesB | 0 [src: comprehensive_metal_ecology] |
| K19595 | gesA | 0 [src: comprehensive_metal_ecology] |

KO–metal pairs matching the annotated target metal had higher t-statistics than mismatched pairs (mean t = 0.263 vs −0.253; Mann-Whitney U p = 0.035). The report calls this a modest metal-specific signal. [src: comprehensive_metal_ecology] The report identifies emrB as a Cu/Tl transporter encoding a broad-substrate multi-drug efflux pump. [src: comprehensive_metal_ecology] It suggests emrB's diverse associations reflect broad RND/MFS efflux selectivity rather than primary metal resistance, and that its prevalence may track metal-stress environments non-specifically. [src: comprehensive_metal_ecology] See [[entities/efflux-pumps]]. Six TIER1 KOs are absent from the pangenome database: cusB, merR, czcC, czcB, czcD and cueR. They include core Cu efflux and Hg sensing components, which limits interpretation of per-KO specificity. [src: comprehensive_metal_ecology]

## Predicting community metal-gene content from environment

Environment predicts community-weighted mean (CWM) metal-gene density poorly across space. NB29 used XGBoost with spatial 5-fold block cross-validation. The response was RA-weighted mean_n_metal_clusters (mean=12.7, SD=8.2). Predictors were pH, temperature, precipitation, elevation, NDVI, clay, lat/lon and log Cu/Zn/Pb/Ni. [src: comprehensive_metal_ecology] Mean CV RMSE was 11.89 (Block 0 = 19.37 to Block 3 = 6.20), comparable to the within-sample SD. [src: comprehensive_metal_ecology] Cu+Zn+Pb+Ni contributed 45.9% of mean |SHAP| (Shapley additive explanations), and log_Ni_ppm was the top predictor (mean |SHAP|=2.23). [src: comprehensive_metal_ecology] The report reads this as consistent with NB28: metals structure community composition, but spatial heterogeneity makes environment-to-CWM transfer generalise poorly. [src: comprehensive_metal_ecology] The hypothesis was only partially supported, because metals contribute beyond pH+climate but predictive power is low (RMSE ≈ SD). [src: comprehensive_metal_ecology] See [[entities/xgboost-with-phylogenetic-blocked-cross-validation]] for a related method.

NB28 partitioned CLR-transformed (centered log-ratio) abundances of the top-200 genera in 5,000 subsampled MicrobeAtlas samples. The axes were metals (Cu, Zn, Pb, Ni) and pH+climate. [src: comprehensive_metal_ecology] All variables together explained R²=0.110. [src: comprehensive_metal_ecology] Unique metals explained R²=0.064, unique pH+climate R²=0.041, and shared variance R²=0.005. [src: comprehensive_metal_ecology] The report says the metal-unique fraction is 58% larger, reversing the conventional expectation that pH dominates. [src: comprehensive_metal_ecology] These R² values are unadjusted, come from a linear model without permutation testing, and are interpreted descriptively. [src: comprehensive_metal_ecology]

## Tensions

- The metal-density/pH-niche link (β = −0.760) sits beside the NB29 result that environment, including metals, predicts CWM metal-gene density poorly in held-out regions. [src: comprehensive_metal_ecology] The first is a genus-level phylogenetic model and the second a community-level spatial-block prediction. The two are different tests.
- The temperature null (p = 0.929) contrasts with the report's primary thermal-stability framework. [src: comprehensive_metal_ecology] Separately, ERA5 and SoilTemp temperature range did predict niche breadth in the latitude mechanism models. [src: comprehensive_metal_ecology]
- The pH term is first read as a speciation/ecology signal distinct from geology. [src: comprehensive_metal_ecology] The report also suggests pH and mafic-geology signals may share one soil-chemistry axis. [src: comprehensive_metal_ecology] A third reading says the pH signal is largely mediated by or confounded with SOM, since pH became non-significant (p = 0.39) once SOM was included. [src: comprehensive_metal_ecology]
- The report predicts that metal-gene-rich genera cluster at lower pH, where Cr(VI)/Cu²⁺ speciation is most reactive. [src: comprehensive_metal_ecology] It also says SOM-metal chelation in high-SOM acidic soils may confound that pH-to-speciation interpretation. [src: comprehensive_metal_ecology]

## Open Directions

- Test the latitude suppressor with bedrock and temperature covariates together in one PGLS model, to see whether they jointly absorb the latitude effect. This addresses the fact that models B and C were fitted separately.
- Re-run NB28 variance partitioning with permutation testing and adjusted R², to see whether the metal-unique fraction (0.064) really exceeds pH+climate (0.041).
- Add the six missing TIER1 KOs (for example cusB, merR, cueR) from another annotation source to the per-KO driver analysis, to test metal specificity for Cu and Hg.
- Test the speciation hypothesis for pH niche by overlaying genus pH optima on metal-speciation pH curves, and by fitting metal-density × pH-specific bedrock interactions, including serpentine soils. Run it with SOM in the model, to separate speciation from SOM chelation.
- Expand the ore-deposit cross-reference beyond 18–19 regions, to see whether the weak correlations hold with more power.
- Repeat the SoilTemp model with more matched genera, to see whether β_metal regains significance.
- Test the Cr and Co signals against a direct redox measure in a region with Cr(VI) or mobile-fraction data, such as Europe (GEMAS) or Australia (NGSA).
- Test the serpentine/ultramafic mechanisms for the Cr signal (Ca/Mg ratio, soil structure, weathering rate) as covariates, since soil moisture did not mediate it.
