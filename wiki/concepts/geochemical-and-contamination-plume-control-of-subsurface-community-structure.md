---
type: "Concept"
description: "How uranium, co-varying geochemistry and a contamination plume model explain spatial and vertical community patterns in contaminated groundwater; correlational, one site."
sources: ["summaries/discoveries.md", "summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/lab_field_ecology__REPORT.md"]
---
# Geochemical and contamination-plume control of subsurface community structure

This page covers how uranium, co-varying geochemistry and a contamination plume model are used to explain spatial and vertical community patterns in contaminated groundwater. The evidence is correlational and comes from one site. The plume model is an interpretation of community data. Its geochemical predictions have not yet been tested, because the Subsurface Observatory (SSO) geochemistry is not loaded. [src: enigma_sso_asv_ecology]

## Literature Context

Two candidate papers address the question this page raises: whether groundwater community structure can be linked to contamination geochemistry, uranium in particular. At the Shiprock uranium mill tailings site, which is contaminated mainly by uranium, sulfate and nitrate, feedforward neural networks predicted phospholipid fatty acid (PLFA) classes from geochemistry much better than generalized linear models did [PMID 16435170](https://pubmed.ncbi.nlm.nih.gov/16435170/). Tritium, an indicator of riverine influence, and uranium were important predictors. Nitrate and inorganic carbon were least important. Less contaminated wells were associated with Gram-negative bacterial and eukaryotic PLFA indicators. More contaminated wells held communities dominated by terminally branched saturates and branched monounsaturates, which the authors read as indicating metal reducers, actinomycetes and Gram-positive bacteria [PMID 16435170](https://pubmed.ncbi.nlm.nih.gov/16435170/). The authors conclude that the community is coupled to geochemistry. This is a lipid-biomarker result from a single site. It is not a 16S survey.

A second study used 16S rRNA gene sequence data to predict 26 geochemical features across 93 wells. It could identify contaminants including uranium and nitrate at a nuclear waste site [PMID 25968645](https://pubmed.ncbi.nlm.nih.gov/25968645/). Its most informative taxa were strains known to interact with uranium and oil. The authors also found that communities at oil-contaminated sites retained a memory of prior contamination after the contaminants had degraded. They stress that geographic generalizability still needs evaluation [PMID 25968645](https://pubmed.ncbi.nlm.nih.gov/25968645/).

The corpus is consistent with this literature in its main premise. The Oak Ridge analysis found distinct community compositions in sites split at median uranium. It also found 5 Fitness Browser genera that correlated significantly with uranium after BH-FDR correction, and it called its uranium hypotheses only partially supported, since 5 of 11 tested genera passed. These results agree with the view that composition tracks contamination and can serve as a readout of geochemistry [PMID 25968645](https://pubmed.ncbi.nlm.nih.gov/25968645/). The Shiprock finding that more contaminated wells held different groups of taxa than less contaminated wells parallels the corpus pattern. There, Caulobacter and Sphingomonas fell at high uranium, while Herbaspirillum and Bacteroides rose [PMID 16435170](https://pubmed.ncbi.nlm.nih.gov/16435170/). That comparison is loose, because the two studies use different markers and different sites.

The SSO plume model goes beyond these papers in two ways. It uses 16S similarity to infer flow paths and a NE→SW plume at meter scale, and it makes specific predictions at named wells. The candidate papers do not test either idea. Its geochemical predictions are untested, so the plume model is still a hypothesis. The prior work does support the approach of testing it. Community data have predicted geochemistry elsewhere [PMID 25968645](https://pubmed.ncbi.nlm.nih.gov/25968645/), and loading the registered SSO geochemistry would allow the same kind of test. Neither paper challenges the corpus. The corpus's uranium-specific taxa and its meter-scale plume interpretation are not covered by the candidates.

## The plume model at the SSO

The SSO report proposes one explanatory model: a contamination plume enters from the northeast and flows southwest through the saturated zone. [src: enigma_sso_asv_ecology] The report places the SSO downhill and southwest of an Area 3 source at Oak Ridge Reservation. That source delivers high-nitrate, low-pH water containing uranium, chromium and nickel. [src: enigma_sso_asv_ecology] See [[entities/subsurface-observatory-well-grid]] and [[entities/oak-ridge-reservation]].

### Spatial patterns

Wells U3, M6 and L7 form a diagonal corridor with shared community composition along the NE→SW flow path. [src: discoveries] The report finds this corridor from Bray-Curtis dissimilarity alone. It says the corridor shows that 16S community similarity can map subsurface hydrology at meter scale, and that 16S data can delineate flow paths at sub-decameter resolution. [src: enigma_sso_asv_ecology, discoveries] The model attributes the shared composition to interception of the plume and shared geochemical exposure. [src: enigma_sso_asv_ecology] It places plume entry near upper-east U3 and flow toward lower-west L7. [src: enigma_sso_asv_ecology] It explains greater east-west than uphill-downhill turnover by a lateral plume edge, so communities track contamination rather than topography. [src: enigma_sso_asv_ecology] See [[concepts/meter-scale-spatial-structure-and-distance-decay-of-subsurface-communities]].

### Vertical structure

The report reads depth dominance over well identity as plume travel through the saturated zones SZ1/SZ2. In this reading deep samples are affected and shallow samples are background. [src: enigma_sso_asv_ecology] It interprets the vertical zonation (permutational multivariate analysis of variance, PERMANOVA, R² = 27.5%) as plume confinement to the saturated zone, not just a generic depth gradient. [src: enigma_sso_asv_ecology] See [[concepts/depth-and-hydrogeological-zonation-of-subsurface-microbial-communities]].

### Process hotspots

The model places M5 at a mixing zone where nitrate-rich plume water meets native organic carbon, which explains the denitrification hotspot. [src: enigma_sso_asv_ecology] It reads 7.7% [[entities/rhodanobacter]] at M5 as moderate plume influence, below the most contaminated Area 2 wells but above background. [src: enigma_sso_asv_ecology] It places M6 in the plume core downstream of M5. There denitrification has used up the nitrate and only fermentative metabolism persists. [src: enigma_sso_asv_ecology] It attributes groundwater enrichment of Rhodanobacter, Gallionella and Sideroxydans to transport of plume-adapted denitrifiers and iron oxidizers, while sediment-attached anaerobes stay in biofilms. [src: enigma_sso_asv_ecology] See [[concepts/attached-versus-planktonic-communities-in-groundwater-and-sediment]] and [[concepts/taxonomy-based-functional-inference-of-biogeochemical-processes-and-the-redox-ladder]].

The report says the stability of groundwater communities strengthens the model. It reads the stability as persistent environmental structure rather than transient fluctuation. [src: enigma_sso_asv_ecology] See [[concepts/temporal-stability-of-groundwater-communities]].

## Testable predictions

The report names the missing SSO geochemistry as the key validation dataset for the plume model. [src: discoveries] It makes these predictions:

- Nitrate, pH and metals should show a NE→SW gradient, highest at U3/M6 and lowest at M4/U1. [src: enigma_sso_asv_ecology]
- Metals in nearby EU/ED wells (100WS/27WS bricks, 90–120 m NE of the SSO) should confirm a plume approaching from the northeast, with concentrations decreasing toward the SSO. [src: enigma_sso_asv_ecology]
- In pump test groundwater (Brick 460-462, wells L8/M5/U2), Rhodanobacter should be highest at M5 and lower at L8 and U2. [src: enigma_sso_asv_ecology]
- The 18 SSO isolate genomes from M6-C2 should encode anaerobic metabolisms, including fermentation and sulfate reduction. [src: enigma_sso_asv_ecology]

The report proposes these steps. It would load the 221 registered geochemistry samples (metals, IC/TOC, isotopes, NH₃/NO₂) into CORAL to validate or refute the model. [src: enigma_sso_asv_ecology] It would extract pump test ASV data as a third snapshot (Mar 2024) from L8, M5 and U2. [src: enigma_sso_asv_ecology] It would repeat 16S profiling across seasons to see whether communities track plume fluctuations. [src: enigma_sso_asv_ecology]

## Uranium and community composition across Oak Ridge sites

A separate analysis relates genus abundance to uranium across Oak Ridge samples. It supports geochemical sorting, but only partly. Oak Ridge sites split at the median uranium concentration showed distinct community compositions. [src: lab_field_ecology] At contaminated sites, rare-biosphere taxa and subsurface specialists became more prominent. [src: lab_field_ecology] After Benjamini-Hochberg false discovery rate (BH-FDR) correction, 5 Fitness Browser (FB) genera correlated significantly with [[entities/uranium]]. [src: lab_field_ecology] The report calls its hypothesis H2 (genus abundance tracks uranium) partially supported, because 5 of 11 tested genera passed. [src: lab_field_ecology]

| Genus | Spearman rho | p | FDR q | Direction |
|---|---|---|---|---|
| Caulobacter | -0.411 | 1.0e-5 | 1.1e-4 | less abundant at high U [src: lab_field_ecology] |
| Sphingomonas | -0.382 | 4.5e-5 | 2.5e-4 | less abundant at high U [src: lab_field_ecology] |
| Pedobacter | -0.266 | 0.005 | 0.013 | less abundant at high U [src: lab_field_ecology] |
| Herbaspirillum | +0.336 | 3.8e-4 | 0.001 | more abundant at high U [src: lab_field_ecology] |
| Bacteroides | +0.264 | 0.006 | 0.013 | more abundant at high U [src: lab_field_ecology] |

Azospirillum was marginal after correction (rho=+0.20, p=0.042, q=0.077). [src: lab_field_ecology] The report treats Caulobacter and Sphingomonas as sensitive indicators of uranium contamination. It treats Herbaspirillum and Bacteroides as possible tolerant colonizers. [src: lab_field_ecology] It reads the shift as broader restructuring of rare taxa, redox conditions and carbon/energy sources, not simply more metal-tolerant organisms. It calls H3 (community shifts with uranium) partially supported. [src: lab_field_ecology] See [[concepts/laboratory-fitness-as-a-predictor-of-field-abundance]], [[concepts/field-validation-of-metal-diversity-genera-in-contaminated-groundwater]] and [[entities/sphingomonas]].

The report ties these results to the literature. It cites Carlson et al. (2019) as showing that low pH with elevated uranium and metals selectively inhibits non-Rhodanobacter taxa. It calls its Caulobacter and Sphingomonas depletion consistent with that. [src: lab_field_ecology] It states that Rhodanobacter dominates contaminated Oak Ridge wells. [src: lab_field_ecology] It cites Michael et al. (2024) as showing reproducible succession after carbon amendment, and reads its uranium correlations as supporting deterministic geochemical responses. [src: lab_field_ecology]

## Caveats

- No SSO geochemistry is loaded. The 221 sample tubes are registered in CORAL, so all environmental inferences come from community composition alone. [src: enigma_sso_asv_ecology]
- Only 5 of 9 SSO wells (L7, L9, M4, M6, U2) have groundwater ASV (amplicon sequence variant) data. M5 and U3 are missing. [src: enigma_sso_asv_ecology]
- The denitrification and iron-oxidation hotspot readings rest on sediment data. The report says groundwater validation would substantially strengthen the model. [src: enigma_sso_asv_ecology]
- In the uranium analysis, 108 overlapping samples may not capture the full Oak Ridge geochemical range. [src: lab_field_ecology]
- Multiple communities per sample (filter sizes, replicates) were aggregated. [src: lab_field_ecology]
- pH, dissolved oxygen and carbon sources were not controlled for. The report proposes CCA (canonical correlation analysis) or RDA to model composition on several geochemical variables while controlling for pH, redox and carbon sources. [src: lab_field_ecology]
- Geochemistry is a snapshot, while community composition reflects historical conditions and colonization history. The ENIGMA samples span multiple dates, and the report proposes testing whether community change over time tracks geochemical change. [src: lab_field_ecology]

## Open Directions

- Load the 221 registered SSO geochemistry samples into CORAL and test the predicted NE→SW gradient directly. This closes the gap that all environmental inference is currently from community composition.
- Obtain EU/ED well metals and pump-test ASV data from L8, M5 and U2. These test the northeast plume source and the M5 Rhodanobacter peak with groundwater rather than sediment.
- Annotate the 18 M6-C2 isolate genomes for fermentation and sulfate reduction, to test the M6 plume-core interpretation.
- Repeat 16S profiling across seasons, and test whether community change over time tracks geochemical change in the ENIGMA samples.
- Fit CCA or RDA models of Oak Ridge communities on several geochemical variables at once. This would separate uranium from its co-varying geochemistry.
