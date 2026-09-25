<!-- tension-hash: c09534c6dbea31a9 -->
# Magnitude of the environment–gene-content correlation is disputed between downsampled and full-genome analyses, while both agree the environmental-group comparison is null

Two projects report medians for the partial correlation between environmental similarity and gene-content similarity — the correlation that remains after phylogenetic similarity is held constant — that differ sharply: 0.003 in the original ecotype analysis versus 0.081 in the reanalysis [src: ecotype_env_reanalysis]. The disagreement matters because the cautionary reading on [[concepts/ecotype-clustering-validity]] rests partly on environment explaining very little gene content once phylogeny is controlled; whether "very little" means near-zero or merely small changes how much residual environmental signal an ecotype account has to explain. Whether the two figures are even estimates of a common quantity is itself part of the dispute; what the projects do not dispute is the null comparison between environmental and human-associated species.

## Evidence Sides

**Downsampled original analysis (low magnitude).** The original ecotype analysis reported a median partial correlation of 0.003 across its analysis [src: ecotype_env_reanalysis]. It used diversity-maximizing downsampling with a maximum of 250 genomes [src: ecotype_env_reanalysis]. The reanalysis characterizes the gap between the two medians as a 27x difference [src: ecotype_env_reanalysis]. The original coarse classification yielded p=0.66, whereas the genome-level harmonized reanalysis yielded p=0.83; both support a null environmental-group comparison, but the methodological discrepancy leaves the magnitude of the correlations unresolved [src: ecotype_analysis, ecotype_env_reanalysis].

**Full-embedding reanalysis (higher magnitude).** The reanalysis reported 0.081 [src: ecotype_env_reanalysis]. It used all genomes with embeddings, including up to 3,505 genomes per species, rather than diversity-maximizing downsampling with a maximum of 250 genomes, and used different genome sets and distance distributions [src: ecotype_env_reanalysis]. The reanalysis itself holds that these absolute values are not comparable across methodologies, although the Environmental versus Human-associated comparison remains valid because it was performed within one consistent method [src: ecotype_env_reanalysis].

## Possible Reconciliations

- *Hypothesis (differing genome sets):* the two medians reflect the different genome sets and distance distributions the reanalysis used rather than a different underlying biology [src: ecotype_env_reanalysis].
- *Hypothesis (genome cap):* the gap tracks the genome cap itself — all genomes with embeddings, up to 3,505 genomes per species, against a maximum of 250 under diversity-maximizing downsampling [src: ecotype_env_reanalysis].
- *Hypothesis (incommensurability):* neither value estimates a shared parameter, as the reanalysis asserts when it states that these absolute values are not comparable across methodologies, and only within-method contrasts — such as the Environmental versus Human-associated comparison, which remains valid because it was performed within one consistent method — carry meaning [src: ecotype_env_reanalysis].

## Resolving Work

- Re-run the reanalysis pipeline on the original's downsampled genome sets (max 250 per species) with all other steps unchanged: does the median return toward 0.003, isolating downsampling as the sole cause?
- Compute the partial correlation as a function of genome cap (250 to 3,505 per species) on a fixed species set: is the difference a monotone power effect or a discontinuity at the downsampling rule?
- Compare the within-species genetic and environmental distance distributions under both genome sets: do the changed distance distributions alone account for the 27x gap?
- Re-test the environmental versus human-associated comparison under the original's coarse classification and the harmonized genome-level classification on identical genome sets: does the null (p=0.66, p=0.83) hold when classification and sampling vary independently?
