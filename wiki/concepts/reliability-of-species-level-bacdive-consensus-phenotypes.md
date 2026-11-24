---
type: "Concept"
description: "How sample size, per-strain deduplication and strain variation affect using BacDive species-level utilization calls to judge a single strain; stops at other phenotype databases."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/pitfalls.md"]
---
# Reliability of species-level BacDive consensus phenotypes

Species-level BacDive utilization calls can mislead when applied to one strain. The evidence here comes from one comparison (FW300-N2E3 against the [[entities/pseudomonas-fluorescens]] record in [[entities/bacdive]]) and from the pitfalls digest. It shows that sample size, record type and strain variation each change how far a consensus call can be trusted. Only tryptophan has enough data for a confident call. [src: fw300_metabolic_consistency]

## Sample size decides confidence

The FW300-N2E3 report scored each BacDive comparison as high, moderate or low confidence by sample size. It found that many BacDive discordances are data-limited. [src: fw300_metabolic_consistency] Naive use of consensus values without sample-size context can produce false discordance calls. [src: fw300_metabolic_consistency] Coverage per compound ranges from 1 to 51 strains under per-strain consensus. [src: fw300_metabolic_consistency]

- Tryptophan: 0 of 50 P. fluorescens strains use it as a carbon source (high confidence, n=50, pct_positive=0.0). This is the only case that reaches high confidence for a genuine production-versus-utilization discordance. [src: fw300_metabolic_consistency] See [[entities/tryptophan]] and [[concepts/metabolite-production-versus-utilization-discordance]].
- Lysine: counts 0+/3-, moderate confidence (n=3). The negatives are consistent, but the sample is small. [src: fw300_metabolic_consistency]
- Glycine: counts 0+/1-, low confidence (n=1). One measurement is unreliable and cannot support conclusions. [src: fw300_metabolic_consistency]

At the aggregate level, a binomial test found no significant difference between BacDive utilization of metabolites FW300-N2E3 produces (3/7 = 43%) and the P. fluorescens baseline (22/80 = 27.5%; p = 0.40). [src: fw300_metabolic_consistency]

## Deduplication and record types

BacDive holds duplicate records per strain. The report applies a per-strain majority vote before computing species-level rates. [src: fw300_metabolic_consistency] Without it, raw record counts can exceed strain counts. [src: fw300_metabolic_consistency]

The utilization field also mixes meanings. It has four values: + (utilizes), - (does not), produced, and +/- (variable or ambiguous). [src: pitfalls] Treating it as binary inflates counts. For P. fluorescens, indole has 60 produced entries and only 1 actual utilization test. [src: pitfalls] Computing pct_positive without excluding produced and +/- entries gives incorrect rates. [src: pitfalls] The recommended calculation divides + by (+ plus -) and tracks the four categories separately. [src: pitfalls]

Other limits on the database: physiology fields are sparse (Gram stain ~15K/97K, oxygen ~23K/97K), so IS NOT NULL filters are usually needed. [src: pitfalls] The metabolite panel is biased toward trehalose, arginine and glucose, so frequency-based ranking misleads. [src: pitfalls]

## Strain variation and taxonomic breadth

BacDive aggregates P. fluorescens strains that, under GTDB reclassification, span a broad clade (Pseudomonas_E fluorescens_E). [src: fw300_metabolic_consistency] Trehalose is strain-variable (1/6 positive), which suggests that trehalose metabolism varies across isolates. [src: fw300_metabolic_consistency] See [[entities/trehalose]]. The species consensus may therefore not reflect FW300-N2E3's own capabilities, even after deduplication. [src: fw300_metabolic_consistency]

Related: [[concepts/cross-database-concordance-of-metabolite-evidence]], [[summaries/fw300_metabolic_consistency__REPORT]], [[summaries/pitfalls]].

## Open Directions

- Place each BacDive compound call in a confidence tier (n and pct_positive) across other organisms, to see how many reported discordances survive a minimum-n filter.
- Split P. fluorescens records by GTDB sub-clade and recompute trehalose and other rates, to test whether strain variation tracks phylogeny.
- Test FW300-N2E3 directly on trehalose and lysine, the cases with small or variable BacDive support.
- Recompute the 3/7 versus 22/80 comparison with more produced metabolites, since the current test has few compounds.
