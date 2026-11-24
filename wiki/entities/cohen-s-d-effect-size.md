---
type: "Method"
description: "A standardized mean difference with pooled SD, used to compare isolation environment groups to baseline."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md"]
aliases: ["Cohen's d"]
---
# Cohen's d effect size

Cohen's d is a standardized mean difference. In this wiki it measures how far a group's mean sits from a baseline mean, in units of pooled standard deviation. The bacdive_metal_validation report uses it to compare BacDive isolation-environment groups with the environmental baseline, and the clay_confined_subsurface report also used it as an effect size. [src: bacdive_metal_validation, clay_confined_subsurface]

## Key facts

- The bacdive_metal_validation report computes d as (mean_group - mean_baseline) / pooled_SD, where pooled_SD = sqrt((SD_group² + SD_baseline²) / 2). [src: bacdive_metal_validation]
- The clay_confined_subsurface report tested self-sufficiency with a two-sided Mann–Whitney U test and used Cohen's d for effect size. See [[entities/mann-whitney-u-test]]. [src: clay_confined_subsurface]

## Use in BacDive isolation-environment validation

Heavy metal isolates score a full standard deviation above the environmental baseline (d = +1.00, Mann-Whitney p=0.006, n=10). [src: bacdive_metal_validation]

| Environment | n | Median score | Mean | Median delta | d | p |
|---|---|---|---|---|---|---|
| Heavy metal contamination | 10 | 0.240 | 0.236 | +0.053 | +1.00 | 0.006 [src: bacdive_metal_validation] |
| Waste/sludge | 305 | 0.219 | 0.218 | +0.032 | +0.57 | <0.0001 [src: bacdive_metal_validation] |
| All contamination | 176 | 0.215 | 0.211 | +0.028 | +0.43 | <0.0001 [src: bacdive_metal_validation] |
| Industrial | 796 | 0.199 | 0.202 | +0.012 | +0.20 | <0.0001 [src: bacdive_metal_validation] |
| Host-associated | 12,086 | 0.194 | 0.201 | +0.007 | +0.14 | <0.0001 [src: bacdive_metal_validation] |

See [[concepts/isolation-environment-validation-of-genome-predicted-metal-tolerance]], [[concepts/validating-metal-tolerance-predictions-against-culture-collection-metadata]], [[entities/bacdive]] and [[summaries/bacdive_metal_validation__REPORT]].

## Power caveat

The heavy metal group is small, so the d=1.00 result sits close to what the test could detect. With n=10 heavy metal isolates against ~5,000 environmental baseline isolates, the minimum detectable effect size at 80% power was approximately d=0.93. [src: bacdive_metal_validation] The observed d=1.00 barely exceeds this threshold, so the test had just enough power to detect the effect. [src: bacdive_metal_validation]

## Use in clay subsurface work

The clay_confined_subsurface report used d alongside the Mann–Whitney test for its self-sufficiency comparison. [src: clay_confined_subsurface] See [[concepts/biosynthetic-self-sufficiency-as-a-deep-subsurface-adaptation]] and [[summaries/clay_confined_subsurface__REPORT]].
