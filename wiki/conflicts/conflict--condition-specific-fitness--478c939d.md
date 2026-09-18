<!-- tension-hash: 478c939d18d6af71 -->
# Universal Essentiality and Non-Reproducible Cross-Cohort Structure: One Denominator Problem or Two Levels of Biology?

Two projects in this corpus report a near-invariant signal and a non-reproducible one, and the disagreement is whether they describe the same phenomenon. The essential-genome work reports that essentiality looks nearly universal once the denominator is restricted to organisms in which a family occurs, and frames this as refining rather than contradicting condition-specific interpretation [src: essential_genome]. The IBD work reports a very strong within-pilot association alongside cross-cohort cluster agreement at or near chance, and notes that the two measure different quantities [src: ibd_phage_targeting]. Whether the shared lesson is that denominators and units of transfer manufacture apparent conditionality, or that gene-level and community-level patterns differ in kind, decides how strongly [[concepts/condition-specific-fitness]] should generalize from single-context measurements.

## Evidence Sides

**Side A — restricting the denominator to occurrence makes essentiality look near-universal, and is offered as a refinement rather than a contradiction.** Only 15 essential families were essential in all 48 organisms, whereas 859 ortholog families — families of genes descended from a common ancestor across genomes — were universally essential within every organism in which they occurred [src: essential_genome]. The direction is that apparent conditionality shrinks when the denominator changes from all 48 organisms to only the organisms carrying the family; the source states this refines rather than contradicts condition-specific interpretation, because genomic context, paralogs, alternative pathways, and compensation affect essentiality [src: essential_genome].

**Side B — a within-pilot association and cross-cohort reproducibility are reported as distinct measurements.** The IBD within-pilot taxonomy–metabolite CCA axis (canonical correlation analysis: the linear combinations of two data blocks that correlate most strongly) had r=0.964, whereas pooled metabolomics had cross-cohort LOSO ARI=0.000 — leave-one-study-out adjusted Rand index, a cluster-agreement statistic expected to be 0 under chance — and the ecotype framework had mean LOSO ARI=0.113 [src: ibd_phage_targeting]. These measure within-pilot association versus cross-cohort reproducibility, not one quantity tracked across a transfer [src: ibd_phage_targeting]. The pooled-metabolomics value is a null result and stays null; the ecotype mean of 0.113 is non-zero [src: ibd_phage_targeting].

## Possible Reconciliations

- **Hypothesis: the two results measure different quantities.** Side A reports within-organism consistency of essentiality calls, Side B reports across-cohort reproducibility of cluster structure; under this hypothesis a high r=0.964 within-pilot association and an ARI=0.000 across cohorts are compatible with no contradiction [src: ibd_phage_targeting].
- **Hypothesis: denominator choice drives both.** If restricting to occurrence-carrying organisms raises apparent universality from 15 to 859 families [src: essential_genome], the analogous restriction in the IBD setting — testing only cohorts that populate the same ecotypes — might raise reproducibility above the 0.113 mean.
- **Hypothesis: the level of organization differs.** Gene-level essentiality may be buffered by paralogs and alternative pathways [src: essential_genome] in ways that community-level composition is not, making cross-context transfer genuinely harder at the community level.

## Resolving Work

- Recompute the IBD ecotype clustering under an occurrence-restricted denominator (cohorts populating the same ecotypes) with the same LOSO ARI protocol: does the mean rise above 0.113?
- Apply a leave-one-organism-out protocol to the 48-organism essentiality matrix, reporting an agreement statistic rather than a count: is universal essentiality reproducible under transfer, not just consistent within occurrence?
- Attach a permutation null to the within-pilot CCA r=0.964 axis: how much of it exceeds a label-randomized baseline?
- Test the paralog/alternative-pathway explanation directly by scoring the 859 universally essential families for paralog presence and asking whether paralog-free families transfer better across organisms.
