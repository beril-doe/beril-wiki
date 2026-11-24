---
type: "Concept"
description: "Whether genome-derived metal tolerance scores are higher for isolates from metal-contaminated or industrial environments than for baseline environmental isolates, including dose-response, phylum-stratified controls and the host-associated anomaly; stops at the construction of the score itself."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/discoveries.md", "summaries/metal_cross_resistance__REPORT.md"]
---
# Isolation-environment validation of genome-predicted metal tolerance

Genome-derived metal tolerance scores are higher for [[entities/bacdive]] isolates from metal-contaminated and industrial environments than for baseline environmental isolates. The effect grows with expected metal exposure and holds within two of four phyla tested. The strongest group (heavy metal, n=10) is small, and a separate Fitness Browser (FB)-scale test found no correlation. This page covers validation only, not construction of the score. [src: bacdive_metal_validation, metal_cross_resistance]

## Contamination versus baseline

Heavy metal contamination isolates score a full standard deviation above the environmental baseline (Cohen's d = +1.00, Mann-Whitney p=0.006, n=10). [src: bacdive_metal_validation, discoveries] See [[entities/cohen-s-d-effect-size]] and [[entities/mann-whitney-u-test]]. The environmental baseline has median=0.187 and mean=0.195. [src: bacdive_metal_validation] The report reads this as validation of the [[entities/metal-fitness-atlas]] prediction method and concludes that isolates from metal-contaminated environments carry more metal tolerance gene content. [src: bacdive_metal_validation, discoveries]

Each comparison uses about 5,000 baseline isolates. Columns: n, median score, mean score, median delta, Cohen's d, p. [src: bacdive_metal_validation]

- Heavy metal contamination: 10, 0.240, 0.236, +0.053, +1.00, 0.006. [src: bacdive_metal_validation]
- Waste/sludge: 305, 0.219, 0.218, +0.032, +0.57, <0.0001. [src: bacdive_metal_validation]
- All contamination: 176, 0.215, 0.211, +0.028, +0.43, <0.0001. [src: bacdive_metal_validation]
- Industrial: 796, 0.199, 0.202, +0.012, +0.20, <0.0001. [src: bacdive_metal_validation]
- Host-associated: 12,086, 0.194, 0.201, +0.007, +0.14, <0.0001. [src: bacdive_metal_validation]

## Dose-response

The effect is dose-dependent across isolation categories: heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). [src: bacdive_metal_validation, discoveries] The report takes this as support that environments with higher expected metal concentrations produce isolates with higher predicted tolerance. [src: bacdive_metal_validation]

## Phylum-stratified controls

Phylum stratification tests whether contamination isolates simply come from phyla with inherently higher scores. [src: bacdive_metal_validation] The signal persists within [[entities/pseudomonadota]] (the dominant phylum) and [[entities/actinomycetota]] but is absent in Bacillota and Bacteroidota. [src: bacdive_metal_validation, discoveries] Values are contamination n, environmental n, delta, p:

- Pseudomonadota: 85, 5,655, +0.040, <0.001. [src: bacdive_metal_validation]
- Actinomycetota: 62, 772, +0.035, <0.001. [src: bacdive_metal_validation]
- Bacillota: 19, 492, -0.012, 0.285. [src: bacdive_metal_validation]
- Bacteroidota: 5, 156, -0.008, 0.456. [src: bacdive_metal_validation]

The report concludes the score captures metal adaptation signal beyond phylogenetic structure, at least in the two most-sampled phyla. [src: bacdive_metal_validation] It offers two explanations for the null phyla. Pseudomonadota and Actinomycetota include major soil bacteria that meet metals, whereas Bacillota and Bacteroidota are primarily gut-associated. [src: bacdive_metal_validation] Alternatively, contamination isolates from those phyla are rare in BacDive, which is biased toward Pseudomonadota, so power is low. [src: bacdive_metal_validation] The two explanations are consistent with the data and not mutually exclusive. [src: bacdive_metal_validation]

Genome size could confound the signal. The metal_score_norm controls for genome size, which matters because Pseudomonadota tend to have larger genomes. [src: bacdive_metal_validation]

The report also reconciles this with the finding that metal tolerance genes are 88% core. Core enrichment describes the within-species pattern. Between-species variation in total metal tolerance gene counts creates the environmental signal. [src: bacdive_metal_validation] It asserts that species with larger core genomes encoding more metal tolerance functions score higher and are more likely to occur in contaminated environments. [src: bacdive_metal_validation] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].

## Host-associated anomaly

Hypothesis H1d predicted lower scores for host-associated bacteria because of reduced metal exposure. [src: bacdive_metal_validation] The data show the opposite: host-associated bacteria score slightly but significantly higher (d=+0.14, p<0.0001). [src: bacdive_metal_validation, discoveries] The report attributes this likely to genome-size confounding. Large-genome Pseudomonadota pathogens (*Pseudomonas*, *Klebsiella*, *Acinetobacter*) dominate these strains and have more KEGG-annotated gene clusters, which inflates the normalized score. [src: bacdive_metal_validation, discoveries] Normalizing by annotated clusters reduces but does not eliminate the effect, because metal tolerance functions correlate with total metabolic complexity. [src: bacdive_metal_validation] The report argues this does not undermine H1a-H1c, since the contamination signal (d=+0.43-1.00) is much larger than the host-associated signal (d=+0.14). [src: bacdive_metal_validation]

## Power and sample-size limits

With n=10 heavy metal isolates against ~5,000 baseline isolates, the minimum detectable effect at 80% power is approximately d=0.93. [src: bacdive_metal_validation] The observed d=1.00 barely exceeds this, so power was just enough. [src: bacdive_metal_validation] The effect-size estimate is imprecise, and a larger heavy metal dataset is needed. [src: bacdive_metal_validation] The research plan referenced n=31 heavy metal isolates, but only 10 matched pangenome species with scores after the species-name bridge. [src: bacdive_metal_validation] See [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases]]. BacDive holds culturable, described strains, so metal-tolerant extremophiles may be under-represented. [src: bacdive_metal_validation]

## Tensions

- At the FB species scale, multi-metal tolerance scores did not correlate with BacDive isolation from metal environments (Spearman rho ~ -0.02, p > 0.8). [src: metal_cross_resistance] The BacDive analysis above found higher scores for heavy-metal isolates than for the environmental baseline. [src: bacdive_metal_validation] The FB test had an effective sample size of 20 independent species, which the report calls far too small for a meaningful test. [src: metal_cross_resistance] It also lacks the power of the Metal Fitness Atlas validation at pangenome scale (42K strains). [src: metal_cross_resistance] BacDive matching by genus+species substring is imprecise for genus-only identifications such as Acidovorax sp. [src: metal_cross_resistance]

## Open Directions

- Collect more heavy-metal-contaminated isolates with genomes, beyond the 10 matched, to estimate the effect size precisely.
- Improve species-name matching to recover more of the 31 planned heavy metal isolates.
- Add contamination isolates from Bacillota and Bacteroidota, from sources other than BacDive, to separate real biology from low power.
- Model genome size explicitly, for example with annotated-cluster count as a covariate, to test the host-associated anomaly.
- Repeat the FB-scale test with more species to see whether the null persists.
