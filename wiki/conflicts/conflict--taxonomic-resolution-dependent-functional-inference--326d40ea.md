<!-- tension-hash: 326d40ead470e4cb -->
# Conflict: Within-Species Functional Differentiation vs. Null Functional Signal at Genus Resolution

Two projects in this corpus disagree about whether finer taxonomic resolution reveals functional structure that coarser aggregation hides — and, if it does, what that structure means. The ecotype project reports functional differentiation *within* species, while the contamination-gradient project reports a null or mode-sensitive result at genus resolution, so the two cannot be stacked into a single claim about contamination-associated community function. The disagreement matters because it decides whether the resolution argument on [[concepts/taxonomic-resolution-dependent-functional-inference]] is a demonstrated mechanism or an untested extrapolation: if genus aggregation is what erases signal, refining resolution should recover it; if the within-species structure is phylogenetic rather than ecological, refining resolution buys nothing for environment-linked inference.

## Evidence Sides

**Finer structure exists within species (ecotype side).** The within-species ecotype evidence — ecotypes being gene-content subpopulations nested inside a single named species — supports the premise that finer functional structure exists below the species label. [src: ecotype_functional_differentiation] But this side's own limitation is explicit and stays stated as a limitation: the ecotype analysis lacked within-species phylogenetic controls, i.e. no correction for shared ancestry among genomes inside a species, so it does not resolve whether the detected structure is ecological or phylogenetic. [src: ecotype_functional_differentiation] The claim is therefore directional (structure is present) but not causal (structure reflects environment).

**No signal survives at genus resolution (ENIGMA side).** In the ENIGMA community analysis, the contamination-gradient result is null or mode-sensitive at genus resolution — the association either fails to appear or depends on which mapping mode is used, rather than holding across modes. [src: enigma_contamination_functional_potential] A null stated at genus resolution is not evidence of absence at finer resolution, and it is also not converted into support for the ecotype reading; it stands as a null.

**Where they collide.** Taken together, the ecotype result limits direct extrapolation from gene-content ecotypes to contamination-associated community functions: one analysis detects functional differentiation within species, while the other is null or mode-sensitive at genus resolution. [src: enigma_contamination_functional_potential] [src: ecotype_functional_differentiation]

## Possible Reconciliations

- **Hypothesis — aggregation masking:** genus-level aggregation averages over ecotypes with opposing functional content, so the within-species differentiation is real and the genus-resolution null is a resolution artifact.
- **Hypothesis — phylogenetic confounding:** the within-species differentiation tracks shared ancestry rather than environment, in which case the genus-resolution null and the ecotype result are consistent and no contamination-linked function is implied. This is exactly the alternative the missing within-species phylogenetic controls leave open. [src: ecotype_functional_differentiation]
- **Hypothesis — scope mismatch:** the ecotype species and the ENIGMA community taxa may not overlap, so the two results would describe different organisms and never contradict each other in the first place.

## Resolving Work

- Re-run the ecotype functional-differentiation test with within-species phylogenetic controls on the same gene-content matrices: does differentiation survive correction for shared ancestry? [src: ecotype_functional_differentiation]
- Repeat the ENIGMA contamination test at sub-species (ecotype-level) resolution using the same mapping modes: does the null at genus resolution become non-null when resolution is refined? [src: enigma_contamination_functional_potential]
- Intersect the ecotype species set with the ENIGMA community taxa to establish whether the two analyses share organisms at all, before any cross-scale inference is attempted. [src: ecotype_functional_differentiation] [src: enigma_contamination_functional_potential]
- Test mode-sensitivity directly: report the contamination association across every mapping mode at each resolution, asking whether direction — not just significance — is stable. [src: enigma_contamination_functional_potential]
