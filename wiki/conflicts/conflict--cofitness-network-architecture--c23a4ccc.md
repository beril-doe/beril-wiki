<!-- tension-hash: c23a4ccc83036ff3 -->
# Does NDH-2 compensation explain Complex I dependence on aromatics beyond ADP1?

This tension asks whether a respiratory-wiring explanation from *Acinetobacter baylyi* ADP1 holds in other species. Complex I is NADH:ubiquinone oxidoreductase and NDH-2 a type II NADH dehydrogenase; NADH is the reduced electron carrier both enzymes oxidize. In ADP1, Complex I subunits produced quinate-specific defects, and the aromatic-catabolism analysis proposes NDH-2 compensation to explain lower Complex I dependence on some substrates. [src: aromatic_catabolism_network] The corrected cross-species comparison found no supporting compensation pattern. [src: respiratory_chain_wiring] The outcome decides whether ortholog-transferred phenotypes (fitness effects carried between corresponding genes in different species) can extend a single-organism model. Annotation error can also manufacture apparent support. [src: discoveries] See [[concepts/cofitness-network-architecture]], [[concepts/condition-specific-fitness]] and [[concepts/cross-species-fitness-transferability]].

## Evidence Sides

**Side 1: ADP1 phenotypes point to a Complex I bottleneck and an NDH-2 compensation hypothesis**

Flux balance analysis (FBA) is a linear-programming model of metabolic flux. In ADP1 it predicted 0% Complex I essentiality, yet 10/13 subunits produced quinate-specific defects, and 30/51 network genes lacked FBA reaction mappings. [src: aromatic_catabolism_network]

Aromatic analysis and respiratory-chain studies associate quinate with greater Complex I dependence despite lower total NADH yield. That interpretation relies on theoretical stoichiometry and inferred capacity limits. FBA predicts zero flux through NDH-2 and ACIAD3522 on standard media. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]

NDH-2 compensation remains a substrate- and architecture-based hypothesis. [src: aromatic_catabolism_network]

**Side 2: The corrected cross-species test does not support compensation**

After NDH-2 false positives were corrected by filtering text-matched candidates to organisms with ≤2 hits per genome, the compensation test reverses: organisms with validated NDH-2 show larger Complex I aromatic deficits (mean -0.297) than those without (-0.156, p=0.52; p is the probability of a difference at least this extreme if no true difference existed, under the test's assumptions). [src: discoveries]

The initial analysis found 10/14 organisms with NDH-2, which appeared to support compensation. That result was driven by misannotated Complex I subunits leaking through the text filter in 5 organisms. [src: discoveries]

On the project's own corrected counts:
- Organisms were filtered to those with 1-2 NDH-2 hits, excluding those with >2 hits. [src: respiratory_chain_wiring]
- 5 of 14 organisms have validated NDH-2. [src: respiratory_chain_wiring]
- The difference in deficits is not significant (p = 0.52). [src: respiratory_chain_wiring]
- NDH-2 presence does not predict whether Complex I is dispensable on aromatics. [src: respiratory_chain_wiring]

The same report's limitation list states that the comparison has only 4 organisms without NDH-2. The 5-of-14 and 4-without counts are not reconciled in the source. [src: respiratory_chain_wiring]

The comparison may be underpowered (too few organisms to reliably detect a real effect) and is insufficient for statistical significance; it weakens the hypothesis's generalization across species. [src: respiratory_chain_wiring]

## Possible Reconciliations

- **Hypothesis:** The ADP1 respiratory wiring pattern is species-specific rather than a general rule, so the ADP1 phenotype stands while its cross-species extension fails. [src: respiratory_chain_wiring]
- **Hypothesis:** The cross-species null reflects low power and residual annotation error rather than an absence of compensation; the comparison is underpowered and vulnerable to annotation errors. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]

None of these is established, and the two results should not be reconciled as a universal rule. [src: respiratory_chain_wiring]

## Resolving Work

- Re-identify NDH-2 with domain-based homology searches instead of text matching across all Fitness Browser organisms with aromatic fitness data. Then re-run the deficit comparison to test whether the reversal survives annotation-independent gene calls.
- Reconcile the 5-of-14 and 4-without cohort counts by listing per-organism inclusion decisions. This would establish the true denominator before any power analysis.
- Run a power analysis on the corrected cohort. It should estimate how many additional organisms lacking NDH-2 are needed to detect a compensation effect of plausible size.
- Construct NDH-2 and Complex I double mutants in ADP1 and measure growth on quinate versus non-aromatic carbon sources. This tests compensation directly within the organism where the hypothesis originated.
- Add Complex I subunit-loss constraints to the ADP1 FBA model and compare the predictions with the measured quinate defects. This tests whether a threshold representation closes the model-versus-phenotype gap.
