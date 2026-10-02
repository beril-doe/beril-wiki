<!-- tension-hash: 47e6a7b460cf1b72 -->
# Does co-occurrence mark a guild of shared selection or a guild of metabolic complementarity?

Two projects in this corpus use gene and taxon co-occurrence to argue about ecological guilds — recurring sets of organisms or traits that occupy the same ecological role — and reach findings that point in opposite directions about what co-occurrence implies. One project reads the pairing of *pqqC* and *acdS* (two plant-growth-promoting, or PGP, marker genes) as an ecological guild on the strength of pairwise association and environmental enrichment [src: pgp_pangenome_ecology]. The other, testing whether co-occurring plant-associated genera carry complementary functional repertoires, found co-occurring genus pairs slightly *less* complementary than random pairs (Cohen's *d* ≈ −0.4 — a standardized mean difference, negative here meaning below the random baseline; permutation *p* < 0.001, i.e. the null of random pairing is rejected by shuffling labels) [src: plant_microbiome_ecotypes]. The stakes are definitional: if "guild" is to be inferred from co-occurrence at all, the corpus needs to say which mechanism the inference licenses. This tension arises on [[concepts/gene-cooccurrence-ecological-guilds]].

## Evidence Sides

**Co-occurrence marks shared environmental selection.** The PGP pangenome analysis supports a *pqqC*–*acdS* ecological-guild interpretation through strong pairwise association between the two genes and through enrichment of that pairing in particular environments [src: pgp_pangenome_ecology]. The claim is at the gene-pair level across genomes; it does not assert that the two genes are physically linked, nor that their carriers divide labour.

**Co-occurrence does not track complementary provisioning.** The plant-microbiome complementarity analysis found that co-occurring genus pairs are slightly less complementary than random pairs (Cohen's *d* ≈ −0.4, permutation *p* < 0.001) [src: plant_microbiome_ecotypes]. The effect is small and negative, not null: co-occurring partners look modestly more functionally redundant than chance, which is the opposite of what a division-of-labour guild predicts.

## Possible Reconciliations

- **Hypothesis: the two results measure different objects.** Gene-pair co-occurrence within genomes may index shared habitat filtering, while genus-pair complementarity across communities indexes between-organism provisioning; neither need constrain the other [src: pgp_pangenome_ecology, plant_microbiome_ecotypes].
- **Hypothesis: shared selection produces redundancy as a by-product.** If a habitat selects one trait set, co-occurring taxa converge on it, which would generate both the *pqqC*–*acdS* pairing and a slightly negative complementarity score [src: pgp_pangenome_ecology, plant_microbiome_ecotypes].
- **Hypothesis: the guild label is being applied at the wrong level.** Complementarity may exist at the pathway or activity level, which neither analysis has yet tested [src: pgp_pangenome_ecology, plant_microbiome_ecotypes].

These findings are not mutually exclusive, and the tension should not be resolved without pathway- and activity-level tests [src: pgp_pangenome_ecology, plant_microbiome_ecotypes].

## Resolving Work

- Take the genomes carrying *pqqC*–*acdS* and score complementarity at the pathway level rather than the marker level: does the negative complementarity direction persist when partial pathways can be summed across partners?
- Re-run the complementarity permutation on gene pairs rather than genus pairs, using the same shuffling scheme, to test whether the two analyses disagree or merely differ in unit of analysis.
- Stratify the complementarity test by environment: is the small negative effect uniform, or absent in the habitats where *pqqC*–*acdS* is enriched?
- Add activity-level evidence (expression or fitness assays) for *pqqC* and *acdS* co-carriers: are both functions simultaneously deployed, or is one silent in situ?
- Test whether co-occurrence at the gene level implies physical linkage in these genomes, since the shared-selection reading does not require it and the complementarity reading does not predict it.
