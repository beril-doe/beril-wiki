<!-- tension-hash: 9cf52c50424ab132 -->
# Concordance Where Measured Versus Coverage of the Endpoint Models Need

Evidence that a metabolic model is right can be counted two ways: by how often the model's predictions agree with an external reference, or by whether the reference records the quantity the model actually predicts. The two counts pull in opposite directions in this corpus. One line of evidence reports a coverage gap — matched observations that exist but lack the action type a model-support argument requires — while another reports high agreement rates for a single organism that nonetheless differ sharply by which reference database is consulted. Because [[concepts/metabolic-model-gapfilling]] treats pathway capacity, condition-specific fitness, and annotation provenance as complementary constraints rather than interchangeable validation, the disagreement matters: it determines whether a high concordance score licenses a claim about flux, or only about the endpoint the reference happens to record.

## Evidence Sides

**The coverage side: matches exist, but not at the needed endpoint.** Nineteen production-to-Fitness-Browser matches lacked consumption actions in the 2018 snapshot. [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency] The Fitness Browser is a collection of mutant fitness phenotypes; a production action records that a metabolite appeared or rose, not that an organism consumed it. On this reading the matched set cannot speak to utilization or dependency at all, however many matches are counted, and the shortfall is structural rather than statistical — a null result for the consumption endpoint, not a weak one.

**The concordance side: agreement is high, and reference-dependent.** FW300-N2E3 showed GapMind 13/13 and Fitness Browser 21/21 concordance but BacDive only 3/7. [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency] GapMind is a computational pathway-completeness annotator; BacDive is a curated bacterial phenotype database. All three counts are reported for the same organism, so on this side agreement is complete against two references and 3/7 against the third; the evidence here does not say which reference a model should be scored against, or what drives the spread between them.

Both sides converge on one statement and diverge on its consequence: production, capability, utilization, dependency, and flux remain distinct endpoints. [src: webofmicrobes_explorer, discoveries, fw300_metabolic_consistency]

## Possible Reconciliations

- *Hypothesis:* the two results measure different endpoints, so a high concordance count and a missing-action count can both be correct simultaneously, with neither constraining the other.
- *Hypothesis:* per-reference agreement is governed by curation completeness, so the lower BacDive fraction reflects absent records rather than model error.
- *Hypothesis:* concordance measured on one organism does not generalize, and the coverage gap is the limiting factor at corpus scale.

## Resolving Work

- Re-run the production-to-Fitness-Browser matching against a snapshot that includes consumption actions; ask whether any of the nineteen matches gains a utilization endpoint.
- Repeat the GapMind/Fitness Browser/BacDive comparison across additional organisms; ask whether the per-reference spread seen for FW300-N2E3 is organism-specific or reference-specific.
- Audit the BacDive comparison record by record; ask whether the cases falling outside the 3/7 concordance are absent records or records that contradict the model.
- Build the pathway-to-metabolite lookup table the matching currently lacks; ask how many matches are recovered by name resolution alone.
- Score model predictions separately per endpoint — capability, utilization, dependency, flux — and ask whether agreement rates differ systematically by endpoint.
