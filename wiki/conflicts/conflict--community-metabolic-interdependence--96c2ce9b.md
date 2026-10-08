<!-- tension-hash: 96c2ce9b6f191d1f -->
# Single-Study Dominance of the Metabolomics Data: Limit on Generality, or Neutral to the Within-Study Result?

The metabolomics evidence behind [[concepts/community-metabolic-interdependence]] is heavily concentrated in one study. 125 of 131 samples (95%) come from `nmdc:sty-11-r2h77870`, and the remaining 6 samples come from a second study [src: discoveries]. The open question is what this concentration does to the amino-acid correlations used to test community-level Black Queen predictions. One reading stresses that the concentration limits how far the correlations generalize across environments and studies [src: discoveries]. The other reading stresses that the leucine and arginine results are not artefacts of mixing studies [src: nmdc_community_metabolic_ecology].

## Evidence Sides

**Side A: concentration limits generalization**
- 125 of 131 samples (95%) come from `nmdc:sty-11-r2h77870`, and the remaining 6 samples come from a second study [src: discoveries].
- This concentration limits how broadly the observed correlations can be generalized across environments and studies [src: discoveries].

**Side B: the results hold within the dominant study**
- All 62 leucine samples came from `nmdc:sty-11-r2h77870` [src: nmdc_community_metabolic_ecology].
- The arginine result was not driven by the minor study [src: nmdc_community_metabolic_ecology].
- The concept page records that this analysis **supports** the Side A limitation rather than overturning it [src: nmdc_community_metabolic_ecology].

The two sides agree on the sample composition, and the NMDC analysis supports the generalization limit rather than disputing it. They differ in emphasis: Side A stresses how far the correlations can reach, while Side B stresses that the leucine and arginine results are not produced by the minor study.

## Possible Reconciliations

- **Hypothesis 1 (different questions):** Side A concerns external validity (do the correlations hold elsewhere?). Side B concerns internal validity (is the result an artefact of combining studies?). If so, both can be true at once. The leucine and arginine signals would then be credible within one study's sampling frame, but untested beyond it.
- **Hypothesis 2 (study-specific signal):** The correlations may reflect conditions particular to `nmdc:sty-11-r2h77870`, such as its environment or its analytical protocol. Under this hypothesis they would weaken or vanish in other studies, and Side A's caution would prove decisive.
- **Hypothesis 3 (general signal, narrowly sampled):** The correlations may reflect a general pattern whose samples have so far come mostly from one study, with only 6 samples from a second study [src: discoveries]. Under this hypothesis the effects would reappear in independent studies, and Side B's robustness would carry over.

## Resolving Work

- **Leucine and arginine in other studies:** Assemble paired metabolomics and metagenome samples from National Microbiome Data Collaborative (NMDC) studies other than `nmdc:sty-11-r2h77870`. Re-run the per-pathway correlations of community biosynthetic completeness against metabolite concentration. Question: do the leucine and arginine signals replicate outside the dominant study?
- **Study as a random effect:** Fit mixed-effects models with study as a random effect across a multi-study sample. A random effect lets each study have its own baseline. Question: do the pathway effects persist once between-study variance is modelled?
- **Leave-one-study-out tests:** Across any expanded multi-study set, drop one study at a time and re-estimate each pathway. Question: does any single study drive the direction or significance of a pathway?
- **Environment-stratified replication:** Stratify new samples by ecosystem type. Question: do the correlations generalize across environments, or are they confined to the habitat type the dominant study sampled?
