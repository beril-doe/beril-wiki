<!-- tension-hash: 85017f9718ca1c0f -->
# Is the BacDive metal-validation effect large-scale and well-powered, or a ten-isolate result near its detection limit?

Two projects describe the statistical power of the same prior result, the BacDive heavy-metal validation, in incompatible ways. Statistical power is the probability of detecting a true effect of a given size. One project presents the validation as a pangenome-scale analysis, a pangenome being the pooled gene content of all genomes in a species. It uses that power to explain a later null result, which is a failure to detect an effect rather than evidence that the effect is absent. The other project places the effect on a small isolate group, only just above its own minimum detectable effect. This matters for [[concepts/lab-field-fitness-concordance]]. The validation is evidence that genome-based metal tolerance predictions track where organisms are isolated. How much confidence that evidence deserves depends on which description of its power is correct. [src: metal_cross_resistance, bacdive_metal_validation]

## Evidence Sides

**Side A: pangenome-scale and adequately powered**

The metal_cross_resistance report describes the prior bacdive_metal_validation result as pangenome-scale, with 42K strains and Cohen's d = +1.0. Cohen's d is a standardized effect size: the difference between group means in units of standard deviation. [src: metal_cross_resistance]

The report treats that result as having the statistical power its own 20-species test lacked, and uses this framing to explain its own test's null outcome. [src: metal_cross_resistance]

**Side B: ten isolates, barely above the detection threshold**

The bacdive_metal_validation report places its heavy-metal effect (d=+1.00) on n=10 isolates. [src: bacdive_metal_validation]

That effect sits barely above a minimum detectable effect of approximately d=0.93 at 80% power. The minimum detectable effect is the smallest effect size the design could reliably detect at that power. [src: bacdive_metal_validation]

On this reading, the heavy-metal comparison had only marginal power. [src: bacdive_metal_validation]

The two descriptions of the same result's power are not reconciled in the corpus. [src: metal_cross_resistance, bacdive_metal_validation]

## Possible Reconciliations

- **Hypothesis 1: different denominators.** The "42K strains" figure may describe the full pangenome or reference set the analysis drew on. The n=10 figure may describe the heavy-metal isolate group actually tested. If so, the two sides count different things, and the power claim depends on which count governs the heavy-metal contrast. This is untested here.
- **Hypothesis 2: comparison-specific power.** Side A's characterization may refer to the project's overall design rather than the specific heavy-metal effect Side B evaluates. If so, both descriptions could be partly accurate at different levels. This is untested here.
- **Hypothesis 3: secondhand compression.** Side A may summarize the prior project secondhand and merge its scale and its effect size into one claim. Only the original report's per-comparison accounting could confirm this. This is untested here.

## Resolving Work

- **Recount the inputs:** Use the bacdive_metal_validation analysis tables. Recount the strains, species and isolates entering the heavy-metal comparison versus the baseline, to establish which denominator the "42K strains" figure refers to.
- **Recompute the power:** Run a power analysis on the actual heavy-metal group and baseline sizes. Ask whether the minimum detectable effect at 80% power is near the reported d or well below it.
- **Resample the effect:** Bootstrap the heavy-metal isolate set, meaning repeatedly resample it with replacement. Report a confidence interval on Cohen's d, the range of effect sizes consistent with the data. Ask whether the interval stays clearly above zero.
- **Enlarge the contamination set:** Use expanded BacDive isolation metadata for metal-contaminated sites. Test whether a larger heavy-metal group reproduces the effect and narrows its estimate.
- **Rerun the null test:** Apply the same mapping approach to the metal_cross_resistance gene signatures at pangenome scale. Ask whether its null result reflects low power or a true absence of the effect.
