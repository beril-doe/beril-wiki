<!-- tension-hash: 175dc8a641dff50d -->
# Tension: are environment–resistome percentages a property of ecology, or of the entity sets and denominators used to count them?

Two counting problems sit unresolved inside [[concepts/environmental-resistome]]. First, soil associations between metal concentrations and COG categories (Clusters of Orthologous Groups — broad functional classes assigned to genes) cannot yet be attributed to any one metal, because chromium, copper, lead, and zinc co-vary in many industrial soils. [src: soil_metal_functional_genomics] Second, two central analyses of the same phenomenon report different magnitudes for the share of AMR (antimicrobial resistance) attributed to efflux — active export of compounds out of the cell by membrane pumps: 21% versus 7.0% in human-gut species. Those values are stated to require harmonized entity sets, filters, annotations, and denominators, so no ecological reading of the environment–mechanism pattern can yet be given a settled magnitude. [src: discoveries, amr_environmental_resistome, amr_fitness_cost]

## Evidence Sides

**Metal-specific interpretation of soil COG associations is not yet separable.** Chromium, copper, lead, and zinc co-vary in many industrial soils, so a COG category associated with one of them may be responding to any or all of the others; the soil analysis treats metal-specific attribution as unresolved rather than settled in either direction. [src: soil_metal_functional_genomics]

**The discoveries digest's efflux contrast.** The digest reports efflux — active export of compounds from the cell by membrane pumps — at 21% of AMR in human-gut species and 1% in aquatic species. [src: discoveries, amr_environmental_resistome, amr_fitness_cost]

**The environmental-resistome analysis's efflux contrast.** The same comparison is reported as 7.0% and 1.1%. The direction (human gut above aquatic) agrees; the magnitudes do not. [src: discoveries, amr_environmental_resistome, amr_fitness_cost]

Listed alongside these, and assigned to neither side, are related core/accessory values of 13% versus 44% — core genes being those present in essentially all genomes of a species, accessory genes those present in only some. Both the 21% versus 7.0% pair and the 13% versus 44% core/accessory values are stated to require harmonized entity sets, filters, annotations, and denominators. [src: discoveries, amr_environmental_resistome, amr_fitness_cost]

## Possible Reconciliations

- *Hypothesis:* the two efflux figures share a numerator but not a denominator — one may normalize over a different set of species, genomes, or gene clusters — so both could be arithmetically correct over their own entity sets.
- *Hypothesis:* differing annotation catalogs or filter thresholds admit different genes into the efflux class, inflating one share relative to the other without either being an error.
- *Hypothesis:* for the soil case, co-varying chromium, copper, lead, and zinc mean the per-metal COG associations are partially redundant measurements of a shared industrial-contamination gradient, not independent metal-specific programmes.

No averaging of 21% and 7.0% is admissible, and neither side is preferred here; the 13%-versus-44% pair likewise remains as stated until harmonized.

## Resolving Work

- Re-derive both efflux shares from a single fixed species list and gene-cluster set, reporting numerator and denominator explicitly: do the figures converge, or is the gap intrinsic to the entity sets?
- Recompute the mechanism shares under a common annotation catalog and a single filter threshold: how much of the 21%-versus-7.0% gap is annotation scope?
- Restate the 13% and 44% core/accessory values under the harmonized definitions: do they change when entity sets and denominators are fixed?
- For soil, apply partial/conditioned analyses that hold chromium, copper, lead, and zinc mutually constant: does any COG association remain attributable to a single metal?
- Take the efflux gene membership lists each pipeline produces over the shared species set and compare them by set difference: which genes enter one pipeline's efflux class but not the other's?
