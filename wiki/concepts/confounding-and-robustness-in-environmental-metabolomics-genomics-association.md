---
type: "Concept"
description: "How study structure, ecosystem stratification, missing abiotic covariates, compound-mapping errors and sample size limit inference when pairing community pathway completeness with metabolomics."
sources: ["summaries/discoveries.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
---
# Confounding and robustness in environmental metabolomics–genomics association

This page covers confounding and robustness in environmental metabolomics–genomics association. The NMDC leucine signal survived the checks that were possible: soil-only stratification and study-level blocking, in a dataset that is 95% single-study. [src: discoveries] Abiotic gradients could not be tested because the covariates were missing. [src: nmdc_community_metabolic_ecology] The arginine signal was weaker under stratification. [src: nmdc_community_metabolic_ecology] See [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]] and [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Literature Context

The only candidate paper is a human clinical multiomics study, not an environmental one, so it bears on the hub only loosely. It studied metabolic dysfunction-associated fatty liver disease (MAFLD) in 56 heterogeneous patients. It combined oral and gut metagenomics with plasma metabolomics and inflammatory proteomics [PMID 35128832](https://pubmed.ncbi.nlm.nih.gov/35128832/). The abstract says the aim was to decipher hepatic steatosis pathogenesis by excluding critical confounding factors, namely genetic variants and diabetes. The authors integrated the data in a biological network, identified key features and used them to predict steatosis. They then report validating the findings in a follow-up cohort of 22 subjects with varying degrees of steatosis [PMID 35128832](https://pubmed.ncbi.nlm.nih.gov/35128832/). The abstract does not say whether that cohort was independent of the first. It also gives no effect sizes or robustness statistics, so it cannot be used to benchmark any specific result here.

The shared methodological point is that pairing microbiome or genomic data with metabolomics needs explicit handling of confounders and some form of validation, and the study's design reflects this. The hub's findings are consistent with that general stance. The NMDC leucine signal was checked by soil-only stratification and study-level blocking, and the arginine signal was re-tested after excluding the minor second study. The paper's confounders are host genetics and diabetes, which are clinical variables. The hub's confounders are study structure, ecosystem type, missing abiotic covariates (pH, temperature, total organic carbon) and compound-name collisions. The paper does not address any of these, so the hub's treatment of them is novel relative to this candidate. The candidate neither supports nor contradicts the hub's specific results, including the leucine signal and the weaker arginine signal under stratification.

The two studies also differ in scale and in how they handled confounding. The clinical study restricted its cohort by design and used a validation cohort of 22 subjects. The NMDC analysis could not restrict or adjust for abiotic gradients because those covariates were all missing. Its leucine result rests on a dataset that is 95% single-study. The hub's open directions are replication on further NMDC studies, abiotic partial correlation or mixed models, freshwater metabolomics, PC1-residualized tests and a substring-collision audit. These come from the corpus's own limitations, and this paper does not support them. The literature evidence available here is therefore too thin to place the hub's claims, and the hub's findings stand largely on the corpus's own checks. See [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]] for the biological context.

## Study structure

The H1 dataset is effectively single-study, so cross-study protocol heterogeneity is mostly absent as a confounder, but this also limits generality. [src: nmdc_community_metabolic_ecology] In the 131-sample H1 dataset, 95% of samples (125/131) come from nmdc:sty-11-r2h77870. [src: discoveries, nmdc_community_metabolic_ecology] The remaining 6 come from a second study, nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology] The 175 metabolomics samples as a whole derive from multiple studies. [src: nmdc_community_metabolic_ecology]

- All leucine samples (n = 62) came from one study with consistent analytical methods, so the report treats cross-study liquid chromatography-mass spectrometry (LC-MS) heterogeneity as effectively absent for leucine. [src: nmdc_community_metabolic_ecology]
- The leucine signal is internally consistent within one analytical protocol. [src: discoveries] The report calls LC-MS heterogeneity effectively absent as a confounder, contrary to naive expectation for NMDC metabolomics. [src: discoveries]
- Excluding the 6-sample second study gives arginine r = −0.264, p = 0.019 (n = 78). The report reads this as showing the arginine signal is not driven by the minor study. [src: nmdc_community_metabolic_ecology] The second study does not materially affect H1 results. [src: nmdc_community_metabolic_ecology]
- Limit: replication across more NMDC studies with paired taxonomy and metabolomics would test whether the leucine and arginine signals generalise. [src: nmdc_community_metabolic_ecology]
- The report recommends counting study-level sample representation before treating aggregate NMDC metabolomics as cross-study data. [src: discoveries] It suggests modelling study-level random effects when coverage is broader. [src: nmdc_community_metabolic_ecology]

## Ecosystem stratification

Soil-only restriction left the leucine result and the sign test unchanged, but arginine lost FDR significance. [src: nmdc_community_metabolic_ecology] H1 was re-run on the 125 Soil samples, excluding 6 Unknown-ecosystem samples. [src: nmdc_community_metabolic_ecology] Leucine stayed false-discovery-rate (FDR) significant (r = −0.390, q = 0.022, n = 62), identical to the full cohort because all leucine samples were Soil. [src: nmdc_community_metabolic_ecology, discoveries] Arginine lost FDR significance (r = −0.264, q = 0.117, n = 78) but stayed directionally consistent. [src: nmdc_community_metabolic_ecology] The binomial sign test was unchanged (11/13 negative, p = 0.011). [src: nmdc_community_metabolic_ecology]

Ecosystem effects are strong. 17/18 amino acid pathways differ across ecosystem types (q < 0.05, Kruskal-Wallis), and the report names carbon substrate availability, not biosynthesis capacity, as the primary driver. [src: discoveries] It warns that carbon substrate range is the dominant ecological axis and can confound amino acid pathway analyses. It recommends PC1-residualized or ecosystem-stratified Black Queen tests. [src: discoveries] See [[concepts/ecosystem-differentiation-of-community-metabolic-potential]].

All 33 Freshwater samples lacked paired metabolomics. They were excluded from H1 but kept for the H2 principal component analysis (PCA), using pathway completeness alone. [src: nmdc_community_metabolic_ecology] H1 is therefore effectively soil-only, and freshwater Black Queen dynamics are untested. [src: nmdc_community_metabolic_ecology]

## Missing abiotic covariates

Abiotic features (pH, temperature, total organic carbon) were all NaN (not a number) in the 174-sample analysis matrix. This prevented partial correlations controlling environmental gradients, which could confound both H1 and H2. [src: nmdc_community_metabolic_ecology] The report proposes partial correlation or mixed-effects models once abiotic data are populated for the overlap samples. This could strengthen the signal or identify confounders. [src: nmdc_community_metabolic_ecology] Related gaps are discussed in annotation and environmental metadata table gaps in the data lakehouse.

## Compound-mapping errors

A substring collision let isoleucine compounds match the "leucine" pattern. Automated review found it, and it was corrected with first-match-wins, so reported results reflect the corrected run. [src: nmdc_community_metabolic_ecology] Three misassigned isoleucine compounds had near-zero completeness-versus-metabolite correlation and diluted the leucine signal. [src: nmdc_community_metabolic_ecology] The fix strengthened it from r −0.326 to −0.390 and q 0.045 to 0.022. [src: nmdc_community_metabolic_ecology] See [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models]].

Proxies are also imperfect. Chorismate is rarely detected. Shikimic acid and 3-dehydroshikimic acid stand in for it but reflect precursor availability, not chorismate pool size. [src: discoveries]

## Sample size and coverage

Some pathways cannot be tested. Glutamine (n = 4) and proline (n = 9) were skipped for insufficient metabolomics coverage. [src: nmdc_community_metabolic_ecology] Three amino acid pathways (cys, his, lys) remain untestable in the 175-sample overlap cohort because compounds were not detected. [src: discoveries]

## Open Directions

- Replicate H1 on additional NMDC studies with paired taxonomy and metabolomics, using study-level random effects, to close the single-study gap.
- Populate abiotic variables for the overlap samples and rerun H1 and H2 with partial correlation or mixed models, to test environmental confounding.
- Add paired metabolomics for Freshwater samples to test whether Black Queen signals extend beyond soil.
- Rerun amino acid tests with PC1-residualized carbon substrate range to separate carbon availability from biosynthesis capacity.
- Audit all compound-name matching for substring collisions, as with isoleucine and leucine.
