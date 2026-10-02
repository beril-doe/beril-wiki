<!-- tension-hash: 10a3282f8dc9cee9 -->
# Environmental Structure in Gene Content: Strong Trait- and Pathway-Level Signals Against a Null Broad Comparison

Within [[concepts/ecotype-environment-gene-content]], two kinds of analysis point in opposite directions. Targeted analyses — of plant growth-promoting (PGP) genes and of community pathway-completeness profiles — report sharp, habitat-linked differences in functional gene content. A broad species-level test asking whether environmental species show stronger environment–gene-content coupling than human-associated species returns a null, with the small difference running the other way. This matters because the two results license opposite framings of the same corpus: either habitat is a first-order determinant of gene content, or "environmental" as a category carries no extra selective coupling. Neither can be discarded, and averaging them would destroy the information in both.

## Evidence Sides

**Targeted trait and community-pathway analyses detect habitat structure.** Soil strongly enriched *acdS*, *pqqC*, and *hcnC* — PGP marker genes for ACC deaminase, PQQ cofactor biosynthesis, and hydrogen cyanide synthesis — and depleted *nifH*, the nitrogenase marker for nitrogen fixation [src: pgp_pangenome_ecology; ecotype_env_reanalysis]. At the community level, NMDC found Soil and Freshwater pathway separation along PC1, the first axis of a principal component analysis of pathway completeness, with median PC1 +3.86 versus −6.28 [src: nmdc_community_metabolic_ecology; ecotype_env_reanalysis].

**The broad environmental comparison is null, and the direction is inverted.** The broad environmental comparison was null [src: pgp_pangenome_ecology; ecotype_env_reanalysis]. The ecotype reanalysis found Environmental median 0.051 versus Human-associated median 0.084 in partial correlation — the environment–gene-content association after controlling for shared covariates — so environmental species did not exceed human-associated species [src: nmdc_community_metabolic_ecology; ecotype_env_reanalysis]. This stays a null result, not weak support for either direction.

## Possible Reconciliations

- *Unit-of-analysis hypothesis*: the signals may be reconcilable if community samples and single species are not the same denominator — pathway completeness summed over a community can separate habitats while per-species gene-content coupling does not.
- *Dilution hypothesis*: a handful of strongly habitat-sorted genes such as *acdS*, *pqqC*, *hcnC*, and *nifH* may be swamped when coupling is summarised genome-wide, so both results could hold simultaneously.
- *Contrast-axis hypothesis*: Soil-versus-Freshwater and soil-versus-other contrasts may be sharper than the Environmental-versus-Human-associated split, if human-associated habitats are themselves highly selective.
- *Annotation-coverage hypothesis*: differential completeness of environmental versus host-associated genome annotation could depress measured coupling in the broad test without affecting targeted gene presence/absence.

## Resolving Work

- Recompute the broad partial-correlation test restricted to the PGP marker set (*acdS*, *pqqC*, *hcnC*, *nifH*) rather than genome-wide gene content: does restricting to habitat-sorted genes move the Environmental group above the Human-associated group?
- Re-run the ecotype comparison with Soil split out as its own group instead of pooled under "Environmental": is the null driven by heterogeneity inside the environmental category?
- Project the NMDC pathway-completeness matrix onto species-level genomes and test the same partial-correlation statistic: does the PC1 separation survive the change of analysis unit?
- Quantify annotation completeness per genome and include it as a covariate in the broad test: does adjusting for annotation depth alter the null?
- Test the reciprocal direction — human-associated marker genes across habitats — to check whether the inverted direction reflects a genuine host-habitat coupling.
