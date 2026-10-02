<!-- tension-hash: e2e1ad79238d238c -->
# Tension: Clinical Sampling Skew Is Real, but Does It Explain the Weak Environment–Gene-Content Signal?

Two projects agree that the AlphaEarth genome subset — the collection of genomes carrying AlphaEarth satellite-imagery embeddings, numeric vectors summarizing the landscape around each sampling coordinate — is clinically skewed, meaning human-associated isolates are overrepresented relative to environmental ones. They disagree about what that skew buys as an explanation. One project tested the skew directly as a cause of the weak relationship between environment and gene content (the set of genes a genome carries) and did not find the expected effect; the other reports that environmental samples carry stronger geographic structure in the same embeddings, leaving spatial and genomic signals pointing in different directions. This matters because whether the skew explains the weak signal decides whether that weak environment–gene-content relationship should be read as an artifact of which genomes were sampled or as a result about biology. The tension arises in [[concepts/sampling-depth-and-downsampling-effects]].

## Evidence Sides

**Skew confirmed, but not exculpatory.** The principal tension is between confirmed clinical sampling bias and the absence of a stronger environmental correlation after group comparison. [src: ecotype_env_reanalysis] The AlphaEarth subset is clinically skewed, but the evidence does not support the claim that this skew alone explains the weak environment–gene-content relationship. [src: ecotype_env_reanalysis] This side rests on a group comparison that returned a null result, and the null stays null: it is an absence of the expected difference, not a demonstration that the skew is harmless.

**Skew confirmed, with stronger geographic structure in environmental samples.** The explorer independently confirms the skew but also shows that environmental samples have stronger geographic embedding structure, so spatial signal and gene-content signal remain discordant rather than reconciled. [src: env_embedding_explorer] What this side establishes is the discordance between the two signals; it does not itself test whether the skew causes the weak gene-content relationship.

## Possible Reconciliations

- **Hypothesis: different signals, different sensitivities.** Geographic embedding structure may respond to sample provenance while gene-content–environment coupling is governed by something else entirely, so both observations can hold without either side being wrong.
- **Hypothesis: the null is power-limited, not causal.** The group comparison may lack the resolution to detect a real but modest skew effect, in which case the reanalysis result constrains effect size rather than refuting the mechanism.
- **Hypothesis: embeddings mediate only spatial, not ecological, variation.** If AlphaEarth vectors encode landscape rather than the niche axes that shape gene content, improving the sampling balance would sharpen geography without sharpening the genomic correlation.

## Resolving Work

- Re-run the group comparison on environment-balanced resamples of the AlphaEarth subset, asking whether the null survives when composition is equalized rather than adjusted for.
- Power-analyze the same comparison to report the smallest skew effect it could have detected, converting the null into an explicit upper bound.
- Test geographic embedding structure and environment–gene-content coupling on the same genomes, asking whether species with strong spatial signal also show stronger genomic coupling.
- Substitute non-imagery environmental descriptors for AlphaEarth vectors and ask whether the gene-content correlation strengthens, separating embedding limitations from sampling composition.
