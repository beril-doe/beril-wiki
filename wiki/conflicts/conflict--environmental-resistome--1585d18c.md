<!-- tension-hash: 1585d18c67fe9e3f -->
# Does genomic compartment mark resistance origin, or only mode of maintenance?

Two projects in this corpus describe the same core/accessory split in bacterial antimicrobial-resistance (AMR) genes — genes present in essentially every genome of a species (core) versus genes present in only some (accessory) — but draw different amounts of inference from it, a tension recorded on [[concepts/environmental-resistome]]. One reads the split as a signature of intrinsic versus acquired resistance, an origin claim; the other compares fitness across the two compartments and reports no difference between them. The disagreement matters because the properties at stake — resistance origin, mobility and cost — would each be read off the same partition. If the compartment split licenses only a claim about how a gene is maintained, every downstream claim built on it inherits the weaker warrant.

## Evidence Sides

**Compartment tracks resistance origin.** The atlas links core status to intrinsic examples and accessory status to acquired examples [src: amr_pangenome_atlas]. Under this reading, a gene's position in the pangenome is diagnostic: chromosomal backbone genes are ancestral to the species, while accessory genes arrived later, plausibly by horizontal acquisition.

**Compartment does not track fitness, and so does not by itself establish origin.** The fitness analysis found identical mean fitness values of −0.024 for core/intrinsic and accessory/acquired groups, with Cohen's *d* = 0.002 (Cohen's *d* is a standardized effect size, where values near zero indicate no separation between group means) and p = 0.33 [src: amr_fitness_cost]. This is a null result at conventional significance thresholds, not a small effect in either direction, and it is reported as a null. The conclusion drawn across both projects is that genomic compartment supports a mode-of-maintenance hypothesis but does not by itself establish resistance origin, mobility, or cost [src: amr_pangenome_atlas, amr_fitness_cost].

## Possible Reconciliations

- *Hypothesis:* the two sides describe different properties of the same partition — compartment records how a gene is maintained in a lineage, while origin, mobility and cost are separate properties that must each be measured directly. Under this hypothesis the atlas's labels are shorthand rather than inference, and no measurement contradicts another.
- *Hypothesis:* acquired genes that have been retained long enough to be observed in assembled genomes have already undergone compensatory adaptation, so any origin-linked fitness difference has been erased by the time either project can see it. This would make the null a survivorship effect rather than evidence against the origin reading.
- *Hypothesis:* the fitness assay and the compartment assignment are measured on non-overlapping gene sets or conditions, so the null speaks to a subset that does not carry the origin signal.

## Resolving Work

- Test mobility directly rather than by proxy: for the same gene clusters the atlas assigns to core and accessory compartments, score physical association with mobile genetic elements (plasmid replicons, integrons, insertion sequences) and ask whether accessory status predicts mobility independently of the intrinsic/acquired label.
- Reconstruct gene phylogenies against species phylogenies for matched core and accessory AMR clusters, and ask what fraction of accessory genes show topological evidence of horizontal transfer — the property the origin reading assumes.
- Re-run the core-versus-accessory fitness comparison restricted to clusters with independent mobility evidence, and ask whether a fitness difference appears in the subset where origin is established rather than inferred.
- Stratify the fitness null by species and by resistance mechanism to ask whether identical means conceal opposing per-lineage effects that cancel in the pooled comparison.
- Compare compartment assignments derived from different species-sampling depths, and ask how much of the core/accessory boundary is an artifact of how many genomes each species contributes.
