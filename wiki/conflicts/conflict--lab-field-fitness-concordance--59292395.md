<!-- tension-hash: 59292395fb73ec10 -->
# Is the Oak Ridge lab tolerance–field abundance test based on 11 or 12 genera?

Two projects report the same Oak Ridge test of whether laboratory metal tolerance predicts field abundance but give different genus counts. [src: lab_field_ecology, bacdive_metal_validation] Both reports call the aggregate association suggestive but nonsignificant. [src: lab_field_ecology, bacdive_metal_validation] A third count appears inside one of the reports. [src: lab_field_ecology] The disagreement matters for [[concepts/lab-field-fitness-concordance]] because the denominator determines how much statistical power the test had. It also decides whether the per-genus and aggregate analyses can be treated as drawing on one genus set.

## Evidence Sides

**Side A: the originating report gives n = 12 genera for the aggregate test**

The lab_field_ecology report gives the aggregate association between laboratory tolerance and field abundance as a Spearman rho (a rank-based correlation coefficient) of 0.503, with p = 0.095 and n = 12 genera. Here p is the p-value, the probability of a result at least this extreme if no association existed. [src: lab_field_ecology] The same report found that five of 11 tested genera were significant individually. [src: lab_field_ecology] Within that report, 11 of the 14 detected Fitness Browser (the laboratory metal-tolerance data source) genera met the >=10-site prevalence threshold for the per-genus uranium correlations. The aggregate tolerance test, however, reports n=12 genera, and these two counts are not reconciled. [src: lab_field_ecology]

**Side B: the citing report gives n = 11 genera for the same result**

The bacdive_metal_validation report cites the same result as a suggestive but non-significant correlation, with rho=0.50, p=0.095 and n=11 genera. [src: bacdive_metal_validation]

**Shared ground**

Both reports agree that the aggregate association is suggestive but nonsignificant. The genus count differs between them, and the tension text does not reconcile it. [src: lab_field_ecology, bacdive_metal_validation]

## Possible Reconciliations

- *Hypothesis:* The citing report may have carried over the per-genus denominator, the 11 genera that met the prevalence threshold, and applied it to the aggregate test. That would produce a transcription mismatch rather than a substantive difference. Nothing in the evidence confirms this.
- *Hypothesis:* The aggregate tolerance test may have used a genus set selected by a different criterion from the >=10-site prevalence threshold. Under that explanation, both counts within lab_field_ecology would be correct for their own analyses. The selection rule for the aggregate test is not stated in the evidence.
- *Hypothesis:* One of the reports may contain a reporting error in n. Which one cannot be determined from the supplied text.

None of these is established, and this page does not prefer either count.

## Resolving Work

- **Aggregate genus list:** Recover the list of genera entering the lab_field_ecology aggregate Spearman test from its notebooks or intermediate tables. Then check whether that list has 11 or 12 members and which genus, if any, differs from the per-genus set.
- **Per-genus selection rule:** Re-apply the >=10-site prevalence threshold to the 14 detected Fitness Browser genera in the Oak Ridge abundance data. Confirm that the result is the 11-genus set, and check whether the aggregate test used a separate filter.
- **Citation provenance:** Trace where bacdive_metal_validation obtained n=11, whether from the lab_field_ecology report text, a table, or a recomputation. This would show whether the discrepancy is a citation error or an alternative analysis.
- **Recompute on both sets:** Recompute the Spearman correlation between tolerance score and field abundance ratio on both candidate genus sets. This tests whether the reported coefficient and p-value correspond to one specific set, which would identify the correct denominator.
