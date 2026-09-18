<!-- tension-hash: cf98e361c044acb7 -->
# Community-Scale Signal or Measured Activity: What NMDC-Scale Evidence Can Establish About Metabolism

Two projects in this corpus reach community scale by different routes and stop short at different places, and the corpus has not settled what a community-scale observable — a correlational association or a taxonomic occurrence count — can license about metabolic activity. One side offers negative associations between community pathway completeness (the fraction of a pathway's steps present) and ambient metabolite levels, which suggest a community-scale signal but do not establish individual flux — the reaction rates carried by a single organism — or causality, because all 33 Freshwater samples lacked paired metabolomics and abiotic covariates were unavailable [src: nmdc_community_metabolic_ecology]. The other side offers breadth — implicated genera appeared in 83/86 genera across 1,719 NMDC (National Microbiome Data Collaborative) metagenomes — but measured occurrence rather than degradation or activity [src: enigma_carbon_census_1]. The disagreement matters for [[concepts/metabolic-model-gapfilling]], where community-scale evidence is invoked as a constraint on what gapfilled models — models completed by adding the reactions needed to simulate growth — may be assumed to do.

## Evidence Sides

**Correlational association across samples.** The NMDC community metabolic ecology work reads negative completeness–metabolite associations as suggesting a community-scale signal, while stating that they do not establish individual flux or causality; the stated reasons are that all 33 Freshwater samples lacked paired metabolomics and that abiotic covariates were unavailable [src: nmdc_community_metabolic_ecology]. What the side holds stays an association across samples, not a measurement in an organism.

**Taxonomic occurrence breadth.** The Carbon Census similarly found broad occurrence at large denominators — implicated genera appeared in 83/86 genera across 1,719 NMDC metagenomes — but measured occurrence rather than degradation or activity [src: enigma_carbon_census_1]. The shortfall here is directional rather than statistical: a genus can be present without performing the implicated transformation.

## Possible Reconciliations

- *Hypothesis:* the two lines are complementary rather than competing — occurrence bounds which taxa could contribute, and completeness–metabolite associations bound which pathways plausibly turn over — so neither alone supports an activity claim and their conjunction supports only a narrower one.
- *Hypothesis:* both limitations reduce to one missing measurement layer, paired metabolite and activity data at the same samples, in which case the disagreement is about sampling design rather than about what inference from community data can carry.

## Resolving Work

- Paired metagenome–metabolome sampling in the Freshwater set, re-running the completeness–metabolite association with abiotic covariates included: does the negative direction survive covariate adjustment [src: nmdc_community_metabolic_ecology]?
- Metatranscriptomic or proteomic profiling of the genera counted as present: among the 83/86 genera across 1,719 NMDC metagenomes, what fraction expresses the implicated catabolic machinery [src: enigma_carbon_census_1]?
- Isotope-tracing or measured substrate-depletion assays on representative isolates from occurrence-positive genera: does occurrence predict degradation rate at all [src: enigma_carbon_census_1]?
- Joint modeling that regresses metabolite intensity on both community completeness and taxon occurrence in the same samples: do the two predictors carry independent information?
- Comparison of gapfilled model flux predictions against whichever community observable survives the above: which observable, if either, constrains gapfilling errors?
