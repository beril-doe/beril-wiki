<!-- tension-hash: d89b8efaaad71d4f -->
# Tryptophan: 0/50 *P. fluorescens* Strains Used It as Carbon, Yet Binary Growth on It Is Predicted at AUC 0.933

Two projects in this corpus describe tryptophan in ways that are hard to hold together. One reports tryptophan as a metabolite that organisms *make* and are genetically equipped to process, but that no tested strain *used* as a carbon source. The other reports tryptophan as the single best-predicted binary growth substrate from gene content. Whether this is a contradiction or two compatible measurements of different things matters directly to [[concepts/cross-tenant-data-bridging]]: bridging schemas across tenants assumes a metabolite name means the same thing on both sides of the join, and here production, pathway completeness, fitness significance and growth may not be the same claim at all.

## Evidence Sides

**Production and pathway presence do not imply utilization.** Tryptophan increased in Web of Microbes (WoM, an exometabolomics resource recording metabolites organisms release into or draw from their environment) and had 231 significant Fitness Browser genes — Fitness Browser being the mutant-fitness data collection — plus a complete GapMind pathway, where GapMind predicts catabolic pathway completeness from genome content. Against that, 0/50 *P. fluorescens* strains used tryptophan as a carbon source. The conclusion drawn is that production therefore does not imply utilization; the utilization result is a null across the full denominator of 50 strains, not a weak positive. [src: fw300_metabolic_consistency]

**Binary growth on tryptophan is predictable from gene content.** Binary growth could be predicted for tryptophan with an AUC of 0.933 — AUC being the area under the receiver-operating-characteristic curve, a ranking statistic where higher values mean better separation of growth from no-growth cases — ahead of phenylalanine (0.932) and valine (0.927). The same models produced negative R² for continuous phenotypes, meaning the fitted models explained less variance than predicting the mean, so the predictability claim is specific to the binary grow/no-grow call. [src: genotype_to_phenotype_enigma]

## Possible Reconciliations

- *Hypothesis: different denominators.* The null is within one panel of 50 *P. fluorescens* strains scored on tryptophan as a carbon source [src: fw300_metabolic_consistency], while the AUC 0.933 is a binary grow/no-grow prediction [src: genotype_to_phenotype_enigma]; a classifier can separate growers from non-growers over a wider strain pool while one clade is uniformly negative.
- *Hypothesis: the classifier learns the negative class.* If tryptophan growth is rare, a high AUC may reflect confidently predicting non-growth from gene content, which would be consistent with a 0/50 null rather than opposed to it.
- *Hypothesis: capability versus use.* Pathway completeness and fitness significance may index tryptophan handling in roles other than sole-carbon catabolism, so both records are correct about different assays.

## Resolving Work

- Report the tryptophan class balance and positive-class count behind AUC 0.933, and recompute precision–recall; asks whether the AUC is carried by true growers or by correct negatives.
- Test the 50 *P. fluorescens* strains under nitrogen-source and mixed-substrate conditions, not carbon only; asks whether the 0/50 null is assay-specific.
- Check whether any strain in the tryptophan-predictable condition set overlaps the 50-strain panel; asks whether the two results ever describe the same organisms.
- Examine what the 231 significant Fitness Browser genes are significant *in* — condition, direction, and whether any correspond to the complete GapMind pathway.
- Re-fit the continuous-phenotype models with tryptophan held out; asks whether the negative R² is uniform or substrate-specific.
