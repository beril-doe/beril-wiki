<!-- tension-hash: 86566e6be31ea1c9 -->
# Environment–AMR association: ecological signal across taxa versus mostly null structure within them

Two lines of analysis in this corpus reach different verdicts on how deeply environment structures the bacterial resistome — the set of antimicrobial-resistance (AMR) genes a genome or population carries. Cross-taxon tests find an environment effect that survives attempts to explain it away as a species-label artifact, while tests run *inside* families and *inside* species return significance in only a small minority of cases, or cannot be powered at all. Because the ecological framing in [[concepts/environmental-resistome]] rests on the first result while the mechanistic interpretation (environment shaping resistance within a lineage) needs the second, the gap matters for how strongly any of those claims can be stated.

## Evidence Sides

**Side A — the association is an ecological signal, not a labeling artifact.** The environment–AMR association persisted after majority-vote thresholds (assigning each species a single environment label by the most common environment among its genomes) and after phylum- and family-level controls, supporting an ecological signal beyond a simple species-label artifact. [src: amr_environmental_resistome]

**Side B — within-taxon structure is weak or unresolved.** Only 20 of 141 testable families (14%) showed significant within-family effects after FDR correction — false discovery rate control, which caps the expected share of false positives among calls — and whole-genome ecotype analysis found environmental effects significant and positive in 12 species (7.0%), significant and negative in 4 species (2.3%), and absent in 156 species (90.7%). [src: amr_environmental_resistome, ecotype_analysis] The strain analysis found AMR ecotypes — distinct within-species AMR gene-content subtypes — in 19.5% of eligible species, but metadata were sparse and only 2 species passed strict testing criteria. [src: amr_strain_variation] This is a null-or-underpowered result, not a positive finding of no effect.

## Possible Reconciliations

- *Hypothesis: scale separation.* Environment may structure which lineages occupy which habitats without restructuring AMR content inside a lineage, so a cross-taxon signal and mostly absent within-species effects are both true at their own scale.
- *Hypothesis: power, not absence.* The 156 species (90.7%) with no detectable effect may reflect thin per-genome metadata and few genomes per species rather than genuinely unstructured resistomes. [src: amr_environmental_resistome, ecotype_analysis] Likewise, that only 2 species passed strict testing criteria may index metadata sparsity rather than absent within-species structure. [src: amr_strain_variation]
- *Hypothesis: testability filter.* Families and species that span enough environments to be testable may be an unrepresentative subset, so the 14% figure could understate or overstate the true within-family rate.

None of these is resolved by the present data, and averaging the cross-taxon and within-taxon rates would not be meaningful.

## Resolving Work

- Re-run the within-family tests on families restricted to those with balanced genome counts across multiple environments, asking whether the 14% significance rate rises once denominator imbalance is removed.
- Curate free-text isolation-source metadata into structured environment labels for the species that currently fail strict testing criteria, then re-test: does the count of testable species rise past 2?
- Power-analyse the ecotype tests directly — simulate known within-species environment effects at varying genome counts to establish the effect size detectable in the 156 non-significant species.
- Compare species whose environment effect was significant and positive (12) with those significant and negative (4) for shared gene content or habitat, asking whether negative effects are a distinct mechanism or noise.
- Test whether taxa excluded as untestable differ systematically in AMR burden from testable ones, quantifying the testability filter's bias.
