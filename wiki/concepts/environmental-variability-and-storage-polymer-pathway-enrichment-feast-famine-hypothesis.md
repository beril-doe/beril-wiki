---
type: "Concept"
description: "Whether carbon-storage pathways such as PHB synthesis are enriched in temporally variable environments and depleted in stable or host-associated ones; stops at genomic association, not fitness measurement."
sources: ["summaries/phb_granule_ecology__REPORT.md"]
---
# Environmental variability and storage-polymer pathway enrichment (feast/famine hypothesis)

The feast/famine hypothesis (Dawes & Senior 1973) proposes that PHB (polyhydroxybutyrate) is most advantageous under temporal carbon fluctuation. [src: phb_granule_ecology] The phb_granule_ecology report tested this across 27,690 species with classified primary environments and says its data strongly support the hypothesis. [src: phb_granule_ecology] The evidence is genomic association only: it shows PHB gene presence by environment, not fitness. The report also says the hypothesis is not necessarily the sole driver. [src: phb_granule_ecology] See also [[summaries/phb_granule_ecology__REPORT]].

## Environmental gradient

PHB prevalence falls from high-variability to low-variability environments, and presence is associated with variability category (chi2 = 1,656.36, p ~ 0, dof = 2). [src: phb_granule_ecology] Plant and soil environments sit at 44% and 43.6%, against 7.4% for clinical and 3.3% for animal environments, a >10-fold difference. [src: phb_granule_ecology] Wastewater is 34.5% and marine 18.7%. [src: phb_granule_ecology]

The species-level table gives phaC prevalence by primary environment, with the expected variability the report assigned:

| Environment | Species | phaC prevalence | Expected variability |
|---|---|---|---|
| Plant-associated | 625 | 44.0% | High [src: phb_granule_ecology] |
| Soil | 1,484 | 43.6% | High [src: phb_granule_ecology] |
| Wastewater/engineered | 1,124 | 34.5% | High [src: phb_granule_ecology] |
| Freshwater | 3,263 | 25.5% | Moderate [src: phb_granule_ecology] |
| Sediment | 1,020 | 20.1% | Moderate [src: phb_granule_ecology] |
| Marine | 3,010 | 18.7% | Low [src: phb_granule_ecology] |
| Human associated | 1,237 | 11.1% | Low [src: phb_granule_ecology] |
| Human clinical | 2,472 | 7.4% | Low [src: phb_granule_ecology] |
| Animal associated | 3,711 | 3.3% | Low [src: phb_granule_ecology] |

At family level, enriched families skew toward freshwater (5/41) and wastewater (3/41), and depleted families toward marine (18/62) and host-associated (12/62) environments. [src: phb_granule_ecology] This family-level reading is limited by the dominant "other_unknown" category (30/41 enriched, 26/62 depleted). [src: phb_granule_ecology]

## Robustness to genome size

PHB enrichment in high-variability environments persists in all four genome-size quartiles, at 1.4–4.6x fold enrichment with all p < 1e-11. [src: phb_granule_ecology] The report reads this as environmental selection independent of genome size, and not a mere consequence of metabolic versatility. [src: phb_granule_ecology] This limits a genome-size confound, but see [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]]. The report says phylogenetically controlled analyses, such as phylogenetic logistic regression, would strengthen the findings by accounting for shared ancestry. [src: phb_granule_ecology]

## Interpretation and external context

The report interprets the pattern as genomic evidence that environmental variability has been a major selective driver of PHB pathway maintenance and acquisition. It extends experimental work in single species, such as *Cupriavidus necator* competition experiments, to a tree-of-life scale. [src: phb_granule_ecology] It cites Viljakainen & Hug (2021), who mapped PHA (polyhydroxyalkanoate) depolymerase genes across 3,078 metagenomes. They found the highest frequency in wastewater and the lowest in marine environments. [src: phb_granule_ecology] The report says its synthesis-gene analysis shows the same gradient from the production side. [src: phb_granule_ecology] It also cites Mason-Jones et al. (2023), who found that intracellular carbon storage including PHB in soil is 0.19-0.46x extractable microbial biomass. [src: phb_granule_ecology]

## Tensions

- Alternative selective pressures: PHB serves functions beyond carbon storage, including stress resistance, redox balance and cryoprotection. [src: phb_granule_ecology] The report cites Obruca et al. (2018, 2020) and Muller-Santos et al. (2021) for multi-stress resistance (UV, osmotic, oxidative, temperature, freezing). [src: phb_granule_ecology] Environmental correlation therefore need not reflect feast/famine alone. [src: phb_granule_ecology]
- Metadata sparsity: 34.9% of species have "other_unknown" as primary environment. The report says this may make the enrichment results underestimate the true signal. [src: phb_granule_ecology] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## Open Directions

- Run phylogenetic logistic regression of PHB presence on variability category, to test whether the association survives shared ancestry. This closes the gap named in the report's caveat.
- Re-annotate the "other_unknown" species using [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]], then repeat the chi-squared test to see whether the gradient sharpens.
- Replace the assigned high/moderate/low variability labels with measured temporal carbon-fluctuation data, for example from metagenome or soil time series. This tests variability directly.
- Compare PHB synthesis and depolymerase gene co-occurrence within the same genomes. This tests whether storage and mobilisation track together.
- Separate stress-resistance from feast/famine explanations by comparing PHB prevalence in stressful but nutrient-stable habitats against fluctuating but mild ones.
