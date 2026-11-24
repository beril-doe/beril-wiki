---
type: "Finding"
description: "The NB20 coreness-matched permutation using 1,000 KO sets matched on KO count and pan-genome prevalence decile distribution yielded emp_p = 0.298, with 29.8% of null sets producing \u03b2 \u2264 \u22120.021."
finding_id: "comprehensive_metal_ecology--a8dada51"
result: "null result"
source: "comprehensive_metal_ecology"
quantities: [{"value": "emp_p = 0.298", "what": "empirical p of coreness-matched permutation", "unit": "", "denominator": "", "scope": ""}, {"value": "29.8%", "what": "null KO sets with \u03b2 \u2264 \u22120.021", "unit": "", "denominator": "", "scope": ""}]
caveat: "The report distinguishes the mechanistically motivated housekeeping comparison from the coreness permutation's test of whether overall \u03b2 is extreme, stating that emp_p = 0.298 does not negate the housekeeping gap."
first_added: "2026-11-24"
source_hash: "3a3c00f14f9f661079f1855285d588dac32dfd6a5fef36e2729641e52137bbec"
---
# Metal-gene signal is not unusual among coreness-matched conserved gene sets

The NB20 coreness-matched permutation using 1,000 KO sets matched on KO count and pan-genome prevalence decile distribution yielded emp_p = 0.298, with 29.8% of null sets producing β ≤ −0.021. [src: comprehensive_metal_ecology]

## Key figures

- **emp_p = 0.298**: empirical p of coreness-matched permutation [src: comprehensive_metal_ecology]
- **29.8%**: null KO sets with β ≤ −0.021 [src: comprehensive_metal_ecology]

## Evidence

> Coreness-matched permutation (NB20; 1,000 sets matched on KO count and pan-genome prevalence decile distribution) yielded **emp_p = 0.298**: 29.8% of null KO sets produced β ≤ −0.021. [src: comprehensive_metal_ecology]

From the report [[summaries/comprehensive_metal_ecology__REPORT]].

## Caveat

The report distinguishes the mechanistically motivated housekeeping comparison from the coreness permutation's test of whether overall β is extreme, stating that emp_p = 0.298 does not negate the housekeeping gap. [src: comprehensive_metal_ecology]

> This comparison to the housekeeping baseline is mechanistically motivated; the coreness permutation addresses a different question (whether the overall β is extreme within the null) and its negative result (emp_p = 0.298) does not negate the housekeeping gap. [src: comprehensive_metal_ecology]

## Other caveats in this report

- The report suggests that low power combined with a small effect size likely explains the non-significant archaeal replication. [src: comprehensive_metal_ecology]
- The report argues that the appropriate null model for the metal-gene signal is the constitutive housekeeping β (≈ −0.029 to −0.035), rather than zero. [src: comprehensive_metal_ecology]
- Three of the seven metal cofactor KOs were absent from the MGnify MAG dataset and contributed zero density, so the exploratory jackknife used only the four detectably represented KOs. [src: comprehensive_metal_ecology]
- The report classifies the named housekeeping controls as streamlining indicators rather than true-negative controls, requiring a valid negative control's per-Mb density not to scale with specialisation. [src: comprehensive_metal_ecology]
- The primary metal-gene coefficient is not distinguishable in overall magnitude from randomly selected conserved gene sets with equal coreness structure. [src: comprehensive_metal_ecology]
