<!-- tension-hash: 1e5ceb5371ca3788 -->
# Does the lab–field concordance evidence validate Fitness Browser data, or only suggest it?

The sources disagree on how strongly laboratory fitness phenotypes match environmental gene distributions, and on whether "validation" is the right word for that match. The central digest calls the evidence a validation of Fitness Browser data as a proxy for in situ importance. [src: discoveries] The underlying project's own statistics support only suggestive, conditional concordance. [src: functional_dark_matter] The choice matters because work building on [[concepts/lab-field-fitness-concordance]] could otherwise treat lab fitness as a settled predictor of field relevance.

## Evidence Sides

**Side A: the evidence validates lab fitness as an ecological proxy**

- The discoveries digest cites the 29/47 concordance of dark genes (genes of unknown function), with Fisher's combined p=0.031, a single significance value pooled from many individual tests. It pairs this with the NMDC (National Microbiome Data Collaborative) confirmations and presents both as validating Fitness Browser data as a proxy for in situ importance. [src: discoveries]
- The functional_dark_matter report's conclusions describe the concordance as exceeding chance and as supporting the inference that lab fitness phenotypes reflect real ecological function. [src: functional_dark_matter]
- The BacDive report describes its heavy-metal result as validating the Metal Fitness Atlas. [src: bacdive_metal_validation]

**Side B: the statistics support only suggestive, conditional concordance**

- The same project report pairs the 29/47 with a one-sided binomial p = 0.072, a test of whether the concordance rate exceeds chance agreement. [src: functional_dark_matter]
- It attributes the high NMDC trait–condition correlations, including the 441 of 449 exploratory tests reaching FDR < 0.05 (FDR, false discovery rate: the expected share of false positives among results called significant), largely to compositional coupling. [src: functional_dark_matter]
- Its statistics therefore support only suggestive, conditional concordance. [src: functional_dark_matter]
- The BacDive report notes that its heavy-metal effect barely exceeds its detection threshold. [src: bacdive_metal_validation]

## Possible Reconciliations

- *Hypothesis:* The two sides use "validation" in different senses. The digest may mean directional consistency across lines of evidence, while the project report weighs how far each statistic rises above chance and how much confounding could explain it.
- *Hypothesis:* The pooled Fisher result and the binomial result answer different questions. One aggregates evidence across individual associations; the other asks whether the overall concordance rate exceeds chance. Both could be accurate within their own scope.
- *Hypothesis:* The validation language in the project conclusions and in the BacDive report reflects summary framing rather than a stronger statistical result than each report measured.

## Resolving Work

- **Composition-controlled NMDC correlations.** Rerun the NMDC trait–condition correlations using log-ratio transforms (expressing abundances relative to a reference so shared totals cancel) or abundance-matched null taxa (equally abundant taxa lacking the trait, to separate abundance from trait effects). Question: how many associations survive FDR < 0.05 once compositional coupling is controlled?
- **Powered dark-gene concordance.** Add carrier vs. non-carrier comparisons across more species, sized by a pre-registered power analysis (a calculation of the sample needed to detect a specified effect). Question: is the concordance rate distinguishable from chance with an adequate sample?
- **Held-out BacDive replication.** Test the heavy-metal effect on BacDive isolates not used in the original analysis. Question: does the effect remain above its detection threshold?
- **Shared validation standard.** Apply an agreed decision rule, such as requiring both the pooled test and the rate test to pass, to the existing functional_dark_matter statistics. Question: which summary statistic should license the word "validation" in this corpus?
