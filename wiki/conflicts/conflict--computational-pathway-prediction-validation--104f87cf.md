<!-- tension-hash: 104f87cfb0f0b773 -->
# Matched growth for FW300-N2E3: independent validation of pathway predictions, or agreement guaranteed by construction?

This tension sits within [[concepts/computational-pathway-prediction-validation]]. The question is whether agreement between computational pathway-completeness predictions and observed growth for strain FW300-N2E3 counts as independent support for those predictions. The alternative is that the comparison was built so that agreement was almost certain. The answer determines how much weight a high concordance figure can carry. If agreement is structurally guaranteed, it says little about whether pathway predictions are reliable. Only the components that could have disagreed carry information.

## Evidence Sides

**Side A: matched growth supports pathway-completeness predictions.**
The FW300-N2E3 project reads its 13/13 agreement as support for pathway-completeness predictions [src: fw300_metabolic_consistency]. The comparison sets GapMind pathway predictions against Fitness Browser growth phenotypes. GapMind supplies the pathway-completeness predictions and the Fitness Browser supplies the observed growth [src: fw300_metabolic_consistency].

**Side B: the concordance is largely structural, and its informative part is null.**
The digest entry for the same project breaks down the 94% mean concordance across four databases into three parts [src: discoveries]:

- Fitness Browser 21/21 = 100%, labelled structural [src: discoveries].
- GapMind 13/13 = 100%, labelled structural [src: discoveries].
- BacDive 3/7 = 43%, labelled informative [src: discoveries]. BacDive is the source of the utilization data in this comparison [src: discoveries].

Across all comparisons, 37/41 were concordant (90.2%) [src: discoveries].

The digest also reports a binomial test, which asks whether an observed proportion differs from an expected baseline rate. It compared BacDive utilization of metabolites that WoM (Web of Microbes, the source of the metabolite-production observations) records as produced, at 43%, against the species baseline of 27.5%. It found no significant difference (p=0.40; the p-value is the probability of a difference at least this large if the two rates were equal) [src: discoveries].

The digest's reading is that the high concordance is largely inevitable for two reasons [src: discoveries]:

- The Fitness Browser always shows growth for metabolites used as sole carbon or nitrogen sources [src: discoveries].
- GapMind predicts complete pathways for common amino acids [src: discoveries].

## Possible Reconciliations

- **Hypothesis 1:** Both readings hold at different scopes. The matched-growth agreement works as a consistency check within a favourable metabolite set. The single informative component, BacDive, returned a null [src: discoveries, fw300_metabolic_consistency]. On this view, Side A describes internal consistency and Side B describes evidential strength.
- **Hypothesis 2:** The 13/13 GapMind agreement is real but uninformative, because it reflects how the metabolites were selected rather than how accurate the predictions are. Testing this would require metabolites for which GapMind could plausibly predict incomplete pathways.
- **Hypothesis 3:** The BacDive null reflects too few metabolites rather than no effect. A larger informative set could detect a difference this test could not; another non-significant result would still not show that the rates are equal.

## Resolving Work

- **Non-favourable metabolites:** Pair GapMind predictions with Fitness Browser growth calls for metabolites outside common amino acids and sole carbon or nitrogen sources, where incomplete pathways are plausible. Does GapMind agreement persist when disagreement is possible?
- **Negative controls:** Draw substrates from Fitness Browser conditions with no growth and score GapMind predictions on them. Does GapMind correctly predict incomplete pathways, which would establish discriminative power and not only agreement?
- **Larger BacDive panel:** Extend the BacDive utilization comparison to more WoM-produced metabolites and to more strains, then repeat the binomial test against the species baseline. Does the null hold once the sample is larger?
- **Separate reporting:** Re-report concordance with structural components (Fitness Browser, GapMind) kept apart from informative ones (BacDive). Does any informative database show concordance above its baseline?
