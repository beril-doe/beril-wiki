<!-- tension-hash: 751c5f9aeeea664a -->
# Does Metal Type Diversity Shape Niche Breadth and Gene Content, or Do Individual Metal Concentrations?

Projects in this corpus disagree about whether the *diversity of metal types* a taxon encounters is the environmental variable that differentiates gene content and niche breadth, or whether the apparent signal reflects sampling power and co-varying individual metal concentrations. This matters for [[concepts/ecotype-environment-gene-content]] because the two framings imply different models: if metal type diversity is the operative predictor, environment–gene-content models can carry a single compact composite variable, whereas if individual metal concentrations drive the shifts, each metal needs its own term and the composite is misleading.

## Evidence Sides

**Metal type diversity is associated with niche breadth.** The MicrobeAtlas analysis found metal type diversity associated with niche breadth [src: microbeatlas_metal_ecology]. The retest of the same association discussed below is a PGLS (phylogenetic generalized least squares, regression that corrects for shared ancestry among taxa) re-run under a stricter prevalence rule [src: microbeatlas_metal_ecology].

**The broad environmental comparison was null, and the strict prevalence test did not reach significance.** A separate reanalysis comparing environmental against human-associated species returned a null result for the environment–gene-content contrast [src: ecotype_env_reanalysis]. Within the metal analysis itself, the strict prevalence version — niche breadth recomputed under a stricter prevalence threshold for counting an OTU (operational taxonomic unit, a sequence-similarity cluster standing in for a species) as present in an environment — was non-significant at p = 0.092 [src: microbeatlas_metal_ecology; ecotype_env_reanalysis]. The null stays a null and the threshold stays a threshold: neither result is restated here as a measured effect.

**Individual metal concentrations, not metal type diversity, may be the real predictor.** The soil-metal study found strong metal–COG associations — COG being Clusters of Orthologous Groups, the functional gene-family categories used to profile community gene content [src: soil_metal_functional_genomics]. But chromium, copper, lead, and zinc co-vary, and partial-correlation analyses (which would hold the other metals fixed while testing one) remain pending, so this study does not resolve whether metal type diversity or individual metal concentrations drive functional shifts [src: soil_metal_functional_genomics].

## Possible Reconciliations

- *Hypothesis:* the strict prevalence threshold removes taxa from the analysis faster than it removes noise, so the p = 0.092 result reflects lost power rather than an absent effect [src: microbeatlas_metal_ecology; ecotype_env_reanalysis].
- *Hypothesis:* metal type diversity is a proxy that carries signal only because it correlates with the concentrations of the co-varying metals chromium, copper, lead, and zinc [src: soil_metal_functional_genomics].
- *Hypothesis:* the two scales measure different things — niche breadth across environments versus community gene content within soils — so the broad environmental null and the metal association are compatible rather than contradictory [src: ecotype_env_reanalysis, microbeatlas_metal_ecology].

## Resolving Work

- Run the pending partial-correlation analyses on the soil metal–COG associations, holding chromium, copper, lead, and zinc against one another: does any single metal retain an association once its co-varying partners are conditioned out? [src: soil_metal_functional_genomics]
- Re-run the niche-breadth PGLS across a sweep of prevalence thresholds rather than the strict one alone: does the effect decay smoothly with threshold (power loss) or drop abruptly (artifact)? [src: microbeatlas_metal_ecology]
- Substitute individual metal concentrations for metal type diversity as the PGLS predictor on the same taxa: which parameterization explains niche breadth better? [src: microbeatlas_metal_ecology, soil_metal_functional_genomics]
- Test the environmental-versus-human-associated contrast restricted to metal-exposed habitats: does the null persist when the environmental axis is metal exposure specifically? [src: ecotype_env_reanalysis]
- Check whether the taxa driving the metal–niche-breadth association are represented in the soil sample set at all, to establish whether the two datasets can in principle corroborate each other [src: microbeatlas_metal_ecology, soil_metal_functional_genomics]
