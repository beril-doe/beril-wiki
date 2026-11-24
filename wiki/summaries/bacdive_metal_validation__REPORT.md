---
type: "Summary"
description: "Summary of the project BacDive Isolation Environment × Metal Tolerance Prediction."
doc_type: "short"
full_text: "sources/bacdive_metal_validation__REPORT.md"
---
# BacDive Isolation Environment × Metal Tolerance Prediction

This project asked whether bacteria isolated from metal-contaminated environments in [[entities/bacdive]] score higher on the genome-based metal tolerance score of the [[entities/metal-fitness-atlas]]. The answer is yes. Heavy metal isolates sit about one standard deviation above the environmental baseline, but that group has only 10 isolates, so the estimate is imprecise. [src: bacdive_metal_validation] The signal persists within two phyla and is absent in two others. [src: bacdive_metal_validation] The score is normalized for genome size, but the report notes the normalization is imperfect. [src: bacdive_metal_validation]

## Key Findings

### Isolation environment and metal tolerance score

Isolates from more heavily contaminated environments score higher, and the effect is dose-dependent: heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). [src: bacdive_metal_validation] The heavy metal group differs from baseline by Cohen's d = +1.00 (Mann-Whitney p=0.006, n=10). [src: bacdive_metal_validation] Cohen's d is (mean_group - mean_baseline) / pooled_SD, with pooled_SD = sqrt((SD_group² + SD_baseline²) / 2). [src: bacdive_metal_validation] The environmental baseline has median=0.187 and mean=0.195. [src: bacdive_metal_validation] The comparison table uses ~5,000 baseline isolates. [src: bacdive_metal_validation]

| Environment | n | Median | Mean | Median delta | Cohen's d | p |
|---|---|---|---|---|---|---|
| Heavy metal contamination | 10 | 0.240 | 0.236 | +0.053 | +1.00 | 0.006 [src: bacdive_metal_validation] |
| Waste/sludge | 305 | 0.219 | 0.218 | +0.032 | +0.57 | <0.0001 [src: bacdive_metal_validation] |
| All contamination | 176 | 0.215 | 0.211 | +0.028 | +0.43 | <0.0001 [src: bacdive_metal_validation] |
| Industrial | 796 | 0.199 | 0.202 | +0.012 | +0.20 | <0.0001 [src: bacdive_metal_validation] |
| Host-associated | 12,086 | 0.194 | 0.201 | +0.007 | +0.14 | <0.0001 [src: bacdive_metal_validation] |

The report concludes that bacteria from metal-contaminated environments carry more metal tolerance gene content than bacteria from uncontaminated environments. [src: bacdive_metal_validation] It reads the dose-response as support that environments with higher expected metal concentrations yield isolates with higher predicted tolerance. [src: bacdive_metal_validation] It also takes the heavy metal result as validating the Metal Fitness Atlas prediction method. [src: bacdive_metal_validation] That score comes from cross-species RB-TnSeq (random barcode transposon sequencing) fitness data, projected onto 27,702 pangenome species through KEGG functional annotations. [src: bacdive_metal_validation]

The metal score (metal_score_norm) controls for genome size, which matters because Pseudomonadota tend to have larger genomes. [src: bacdive_metal_validation] Without normalization, the environmental signal could partly reflect genome size rather than metal gene content. [src: bacdive_metal_validation]

### Phylum-stratified control

Phylum-stratified analysis tests whether contamination isolates simply come from phyla with inherently higher scores. [src: bacdive_metal_validation] Within [[entities/pseudomonadota]], the dominant phylum, contamination isolates still score higher than environmental isolates. [src: bacdive_metal_validation] The signal is real within Pseudomonadota and Actinomycetota and absent in Bacillota and Bacteroidota. [src: bacdive_metal_validation] The report reads this as a metal adaptation signal beyond phylogenetic structure, at least in the two most-sampled phyla. [src: bacdive_metal_validation] The phylum-stratified results file has 4 rows. [src: bacdive_metal_validation]

| Phylum | Contamination n | Environmental n | Delta | p |
|---|---|---|---|---|
| Pseudomonadota | 85 | 5,655 | +0.040 | <0.001 [src: bacdive_metal_validation] |
| Actinomycetota | 62 | 772 | +0.035 | <0.001 [src: bacdive_metal_validation] |
| Bacillota | 19 | 492 | -0.012 | 0.285 [src: bacdive_metal_validation] |
| Bacteroidota | 5 | 156 | -0.008 | 0.456 [src: bacdive_metal_validation] |

The report offers two explanations for the null phyla. The first is biology: Pseudomonadota and Actinomycetota include major soil bacteria exposed to metals, while Bacillota and Bacteroidota are primarily gut-associated. [src: bacdive_metal_validation] The second is statistical power: contamination isolates from those phyla are rare in BacDive, and the collection is biased toward Pseudomonadota. [src: bacdive_metal_validation] The report treats both as consistent with the data and not mutually exclusive. [src: bacdive_metal_validation]

### Host-associated bacteria (H1d)

H1d predicted lower metal scores for host-associated bacteria because of reduced metal exposure in host niches. [src: bacdive_metal_validation] The data showed the opposite: a slightly but significantly higher score (d=+0.14, p<0.0001). [src: bacdive_metal_validation] The report attributes this likely to genome-size confounding. Host-associated BacDive strains are dominated by large-genome Pseudomonadota pathogens such as Pseudomonas, Klebsiella and Acinetobacter, which have more KEGG-annotated gene clusters. [src: bacdive_metal_validation] Normalizing metal clusters by annotated clusters reduces but does not eliminate this effect, because metal tolerance functions correlate with total metabolic complexity. [src: bacdive_metal_validation] The report argues the result does not undermine H1a-H1c, because the contamination signal (d=+0.43-1.00) is much larger than the host-associated signal. [src: bacdive_metal_validation]

### Metal utilization tests

Only 24 BacDive metal utilization test records (iron, manganese, arsenate, chromate, cobalt, zinc) matched strains with scores. [src: bacdive_metal_validation] With 8 positive and 16 negative results, the comparison is underpowered (Mann-Whitney p=0.14, d=-0.57). [src: bacdive_metal_validation] Positive utilizers had lower scores. The report cautions against over-interpreting this nonsignificant direction. [src: bacdive_metal_validation] The report calls this validation inconclusive because 24 records are far too few for reliable statistics. [src: bacdive_metal_validation]

### Relation to other projects

The metal_specificity project found metal tolerance genes to be 88% core. [src: bacdive_metal_validation] The report reconciles this with the environmental signal. Core enrichment describes the within-species pattern, while between-species variation in total metal tolerance gene counts creates the environmental signal. [src: bacdive_metal_validation] It asserts that species with larger core genomes encoding more metal tolerance functions score higher and are more likely to occur in contaminated environments. [src: bacdive_metal_validation]

The lab_field_ecology project found a suggestive but nonsignificant correlation between lab metal tolerance and field abundance at Oak Ridge (rho=0.50, p=0.095, n=11 genera). [src: bacdive_metal_validation] The report calls the BacDive analysis stronger evidence for the same hypothesis at larger scale. [src: bacdive_metal_validation] It attributes the difference in significance to BacDive's larger sample size. [src: bacdive_metal_validation]

## Data and Methods

Species-name matching linked 42,227 BacDive strains (43.4% of 97,334) to scores across 6,426 unique GTDB species. [src: bacdive_metal_validation] Of these, 25,089 have isolation source metadata. [src: bacdive_metal_validation] Exact name agreement linked 33,535 strains (34.5%). [src: bacdive_metal_validation] GTDB suffix removal linked 8,692 more (8.9%), for example BacDive "Pseudomonas fluorescens" to GTDB "Pseudomonas fluorescens A". [src: bacdive_metal_validation] The bridge left 55,107 strains (56.6%) unmatched. [src: bacdive_metal_validation] The notebooks are 01_bacdive_pangenome_bridge.ipynb (builds the BacDive-to-pangenome species-to-metal-score bridge), 02_environment_metal_scores.ipynb (Mann-Whitney tests, power analysis, phylum-stratified analysis) and 03_metal_utilization.ipynb (exploratory metal-utilization phenotypes versus metal scores). [src: bacdive_metal_validation]

Output tables: the full bridge (data/bacdive_pangenome_bridge.csv) has 97,334 rows covering all BacDive strains with match status and metal scores. [src: bacdive_metal_validation] The matched-strain table has 42,227 rows with isolation and metal-score data. [src: bacdive_metal_validation] The environment comparison table has 5 rows. [src: bacdive_metal_validation] The metal-utilization table has 24 records. [src: bacdive_metal_validation]

## Caveats and Open Work

- The heavy metal group is small. With n=10 versus ~5,000 baseline isolates, the minimum detectable effect at 80% power is approximately d=0.93. [src: bacdive_metal_validation] The observed d=1.00 barely exceeds it. [src: bacdive_metal_validation] The group sits at the detection limit, so its effect size is imprecise. [src: bacdive_metal_validation] A larger heavy metal dataset is needed to estimate it precisely. [src: bacdive_metal_validation]
- RESEARCH_PLAN.md referenced n=31 heavy metal isolates, but only 10 matched pangenome species with scores after the bridge. [src: bacdive_metal_validation]
- Species-level matching is lossy. It failed for 56.6% of strains, primarily because GTDB uses different species boundaries than LPSN/DSMZ. [src: bacdive_metal_validation] Genome accession-based matching (GCA to pangenome genome_id) would improve coverage but requires a Spark query. [src: bacdive_metal_validation]
- BacDive holds culturable, described strains rather than full environmental diversity. Metal-tolerant extremophiles may be under-represented. [src: bacdive_metal_validation]
- The current metabolite_utilization table may miss metal tolerance tests available through the BacDive API (application programming interface), such as MIC data and growth inhibition. [src: bacdive_metal_validation]

Next analyses proposed by the report:
- GCA accession-based matching: query kbase_ke_pangenome.genome to match BacDive GCA accessions directly to pangenome genome_ids, potentially recovering more of the 56.6% unmatched strains. [src: bacdive_metal_validation]
- ENIGMA CORAL integration: cross-reference ENIGMA community data at the Oak Ridge metal-contaminated site for complementary field validation. [src: bacdive_metal_validation]
- Per-metal environment analysis: for metals with sufficient BacDive representation (iron, manganese), test whether specific metal tolerance gene families predict specific contamination environments. [src: bacdive_metal_validation]
- Expanding BacDive metal phenotypes beyond the current table. [src: bacdive_metal_validation]

## Slots Into

- [[concepts/isolation-environment-validation-of-genome-predicted-metal-tolerance]]: contamination isolates score above baseline in a dose-dependent pattern (d=+1.00 for heavy metal). [src: bacdive_metal_validation]
- [[concepts/validating-metal-tolerance-predictions-against-culture-collection-metadata]]: the metal utilization test was underpowered (24 records, p=0.14). [src: bacdive_metal_validation]
- [[concepts/coverage-and-bias-in-linking-strain-phenotype-databases-to-pangenomes]]: 43.4% of BacDive strains linked and 56.6% did not. [src: bacdive_metal_validation]
- [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]]: 88% core metal genes coexist with a between-species environmental signal. [src: bacdive_metal_validation]
- [[concepts/laboratory-fitness-as-a-predictor-of-field-abundance]]: BacDive supports the lab-to-field hypothesis where Oak Ridge was nonsignificant. [src: bacdive_metal_validation]
