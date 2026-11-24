---
type: "Concept"
description: "How well exometabolomic, mutant-fitness, species-phenotype and pathway-prediction databases agree on the same metabolites, and how matching coverage, circularity and medium differences limit that comparison."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Cross-database concordance of metabolite evidence

This page asks how well exometabolomic (Web of Microbes, WoM), mutant-fitness (Fitness Browser, FB), species-phenotype (BacDive) and pathway-prediction (GapMind) databases agree on the same metabolites. The evidence comes from one organism, Pseudomonas FW300-N2E3 ([[entities/pseudomonas-fluorescens-fw300-n2e3]]), plus a linkage assessment from a second report. Where metabolites could be matched, agreement was high. Only a minority could be matched, and the report calls much of the agreement structural. [src: fw300_metabolic_consistency]

## Concordance where matching was possible

Of 58 metabolites produced or increased by FW300-N2E3 in WoM, 21 could be cross-referenced against at least one other database. [src: fw300_metabolic_consistency] Of these 21, 17 (81%) were fully concordant, 4 (19%) were partially concordant, and none were fully discordant; the mean concordance score was 0.94. [src: fw300_metabolic_consistency] Across all 41 individual metabolite-database comparisons, 37 were concordant (90.2%). [src: fw300_metabolic_consistency]

Three metabolites were concordant across all four databases. [src: fw300_metabolic_consistency]
- Malate was Increased in WoM, supported FB growth (92 genes), was utilized in BacDive (49/49, 100%) and had a complete GapMind pathway. [src: fw300_metabolic_consistency]
- Arginine was Increased, supported FB growth (270 genes), was utilized in BacDive (40/48, 83%) and had a complete GapMind pathway. [src: fw300_metabolic_consistency]
- Valine Emerged, supported FB growth (160 genes), was utilized in BacDive (1/1) and had a complete GapMind pathway. [src: fw300_metabolic_consistency]

The report treats these three as the gold standard of consistency. The organism produces and grows on each one, the species uses it, and its pathway is computationally complete. [src: fw300_metabolic_consistency]

The report claims this is the first systematic single-organism comparison spanning exometabolomics, mutant fitness, species phenotypes and pathway predictions. It also claims that no published study has compared WoM profiles with FB fitness data, although the same program generated both. [src: fw300_metabolic_consistency] It concludes that such integration is feasible and biologically meaningful. [src: fw300_metabolic_consistency] These are the report's own claims, not independently checked here. See [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments]] for the matching itself.

## Why the concordance is partly structural

The report calls the 94% concordance largely structural. FB (21/21 = 100%) and GapMind (13/13 = 100%) were invariably concordant with WoM production. [src: fw300_metabolic_consistency] BacDive was the only variable component, with 3/7 = 43% of matched metabolites utilized. [src: fw300_metabolic_consistency]

A binomial test found that this rate did not differ significantly from the overall *P. fluorescens* baseline (22/80 = 27.5%; p = 0.40). [src: fw300_metabolic_consistency] That is a null result on a small sample of 7 metabolites. For how reliable species-level BacDive calls are, see [[concepts/reliability-of-species-level-bacdive-consensus-phenotypes]].

## Matching coverage

Matching started from 58 WoM metabolites (27 Emerged, 31 Increased). [src: fw300_metabolic_consistency]
- 28/58 (48%) matched FB carbon/nitrogen source conditions. [src: fw300_metabolic_consistency]
- 8/58 (14%) matched BacDive *P. fluorescens* utilization data. [src: fw300_metabolic_consistency]
- 13/58 (22%) matched GapMind pathway predictions. [src: fw300_metabolic_consistency]

Manual curation produced the 28 WoM–FB and 8 WoM–BacDive matches. [src: fw300_metabolic_consistency]

Of 31 mapped FB conditions, 7 had no FW300-N2E3 experiments: 4-aminobutanoate, 5-oxo-proline, Betaine, Guanine, Nicotinamide, Sarcosine and trans-Aconitate. [src: fw300_metabolic_consistency] The downstream analysis therefore used only the 24 conditions with fitness data. [src: fw300_metabolic_consistency]

A second report, on WoM exploration, gives a different count for the same organism and database pair. Its curated matching for FW300-N2E3 (pseudo3_N2E3) identified 19 metabolites that WoM shows the organism producing and that FB tests as carbon or nitrogen sources. [src: webofmicrobes_explorer] Of these 19, 5 are de novo products (E) and 14 are amplified metabolites (I). [src: webofmicrobes_explorer] This 19 differs from the 28 WoM–FB matches in the consistency report. [src: fw300_metabolic_consistency] The claims do not say how the two counts relate, so they are stated separately here and not reconciled.

The remaining 37 metabolites (64%) were observed only in WoM. They were not tested in BacDive, not predicted by GapMind and not used as FB conditions for this organism. [src: fw300_metabolic_consistency] Only 21/58 (36%) could be tested, and only 3 had four-way coverage. The report says results are robust where data exist, but the untested 64% may hide further discordances. [src: fw300_metabolic_consistency]

The report attributes the low matching rates to nomenclature and scope differences. Many WoM metabolites, such as N-acetylated amino acids and nucleotide derivatives, have not been tested in FB, BacDive or GapMind. [src: fw300_metabolic_consistency] It also cautions that further matches may have been missed because of nomenclature. [src: fw300_metabolic_consistency] To address this, the report proposes using chemical identifiers (InChIKey, CHEBI) instead of name matching to expand the WoM–BacDive overlap beyond 8 metabolites. [src: fw300_metabolic_consistency]

### Approximate matches

Two FB matches are approximate base-to-nucleoside mappings, Cytosine→Cytidine and Uracil→Uridine, flagged `fb_match_quality=approximate`. [src: fw300_metabolic_consistency] Excluding them reduced testable metabolites from 21 to 19 and shifted mean concordance from 0.937 to 0.930. The report calls this negligible, because both were already fully concordant. [src: fw300_metabolic_consistency] Its sensitivity analysis found no effect on the concordance results. [src: fw300_metabolic_consistency]

## Linkage to metabolic resources

A separate report rates WoM–ModelSEED linkage as moderate. 26.8% of identified metabolites have definitive name-based links (high confidence). A further 41.6% match by formula only, which is ambiguous, with an ~8:1 expansion ratio. [src: webofmicrobes_explorer] See [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models]].

WoM–GapMind linkage was blocked in that report. GapMind pathway names are internal IDs (identifiers) and do not contain simple metabolite names, so name matching failed. [src: webofmicrobes_explorer] The report says a dedicated pathway-to-metabolite lookup table would enable the link. [src: webofmicrobes_explorer]

## Medium differences

WoM exometabolomics was measured on R2A rich medium. FB fitness was measured on minimal medium with single carbon or nitrogen sources. Metabolic profiles depend on condition, so some WoM metabolites may be produced only on rich media. [src: fw300_metabolic_consistency] This limits any one-to-one comparison of production and growth. See [[entities/r2a-medium]]. The report proposes comparing WoM profiles across growth media to find which metabolites are constitutively produced and which depend on the medium. [src: fw300_metabolic_consistency]

## Tensions

- High concordance (mean 0.94; 37 of 41 comparisons) [src: fw300_metabolic_consistency] sits against the report's statement that it is largely structural and that only 36% of metabolites were testable. [src: fw300_metabolic_consistency]
- The consistency report counts 28 WoM–FB matches for FW300-N2E3 [src: fw300_metabolic_consistency], while the WoM exploration report counts 19 metabolites produced in WoM and tested in FB as carbon or nitrogen sources. [src: webofmicrobes_explorer] The claims do not explain the difference.

## Open Directions

- Compare the 28 WoM–FB matches with the 19 curated matches for FW300-N2E3 item by item. This would show whether the counts differ by matching rule, condition type or data subset.
- Rebuild the WoM–BacDive crosswalk with InChIKey and CHEBI identifiers instead of names. This would test whether the overlap grows beyond 8 metabolites.
- Build a GapMind pathway-to-substrate/product lookup table. This would let WoM–GapMind concordance be tested for more than 13 metabolites.
- Compare WoM profiles across growth media. This would separate constitutively produced metabolites from medium-dependent ones, and so address the R2A versus minimal-medium gap.
- Run the same crosswalk on other organisms. This would show whether FB and GapMind concordance stays at 100%, or whether that was an artifact of FW300-N2E3.
