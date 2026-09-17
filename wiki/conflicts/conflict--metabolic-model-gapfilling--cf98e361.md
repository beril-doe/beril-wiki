<!-- tension-hash: cf98e361c044acb7 -->
# Community-Scale Signal or Measured Activity: What NMDC-Scale Evidence Can Establish About Metabolism

Two projects in this corpus reach community scale by different routes and stop short at different places, and the corpus has not settled which kind of community-scale observable — a correlational association or a taxonomic occurrence count — can license a claim about metabolic activity. One side reports negative associations between community pathway completeness (the fraction of a pathway's steps present) and ambient metabolite levels, but cannot attach them to individual flux (the reaction rate carried by a single organism), because all 33 Freshwater samples lacked paired metabolomics and abiotic covariates were unavailable [src: nmdc_community_metabolic_ecology]. The other side reports breadth — implicated genera appeared in 83/86 genera across 1,719 NMDC (National Microbiome Data Collaborative) metagenomes — but measured occurrence rather than degradation or activity [src: enigma_carbon_census_1]. The disagreement matters for [[concepts/metabolic-model-gapfilling]], where community-scale evidence is invoked as a constraint on what gapfilled models — models completed by adding the reactions needed to enable simulated growth — may be assumed to do.

## Evidence Sides

**Negative completeness–metabolite association (NMDC community metabolic ecology).** The negative completeness–metabolite associations are read as a community-scale signal, but the report states they do not establish individual flux or causality; the stated reasons are that all 33 Freshwater samples lacked paired metabolomics and that abiotic covariates were unavailable [src: nmdc_community_metabolic_ecology]. The claim is therefore suggestive, not established: an association across samples, not a measurement in an organism.

**Broad taxonomic occurrence (Carbon Census).** The Carbon Census establishes presence at large denominators — implicated genera appeared in 83/86 genera across 1,719 NMDC metagenomes — but the report states that what was measured is occurrence rather than degradation or activity [src: enigma_carbon_census_1]. The shortfall here is directional rather than statistical: a genus can be present without performing the implicated transformation.

## Possible Reconciliations

- *Hypothesis:* the two lines are complementary rather than competing — occurrence bounds which taxa could contribute, and completeness–metabolite associations bound which pathways plausibly turn over — so neither alone supports an activity claim and their conjunction supports only a narrower one.
- *Hypothesis:* both shortfalls reduce to one missing measurement layer, paired metabolite and activity data at the same samples, in which case the disagreement is about sampling design rather than about inference from community data.
- *Hypothesis:* the shortfalls are different in kind — an unmeasured-covariate gap, since abiotic covariates were unavailable [src: nmdc_community_metabolic_ecology], versus an unmeasured-function gap, since occurrence rather than degradation or activity was measured [src: enigma_carbon_census_1] — so no single added measurement would close both.

## Resolving Work

- Paired metagenome–metabolome sampling in the Freshwater set, re-running the completeness–metabolite association with abiotic covariates included: does the negative direction survive covariate adjustment [src: nmdc_community_metabolic_ecology]?
- Metatranscriptomic or proteomic profiling of the genera counted as present: among the 83/86 genera across 1,719 NMDC metagenomes, what fraction expresses the implicated catabolic machinery [src: enigma_carbon_census_1]?
- Isotope-tracing or measured substrate-depletion assays on representative isolates from occurrence-positive genera: does occurrence predict degradation rate at all [src: enigma_carbon_census_1]?
- Joint modeling that regresses metabolite intensity on both community completeness and taxon occurrence in the same samples: do the two predictors carry independent information?
- Comparison of gapfilled model flux predictions against whichever community observable survives the above: which observable, if either, constrains gapfilling errors?
