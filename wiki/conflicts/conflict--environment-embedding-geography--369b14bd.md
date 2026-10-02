<!-- tension-hash: 369b14bd5977bce9 -->
# Tension: which environment label — structured ontology or harmonized keywords — should anchor environment–genome analyses

Environment metadata for genomes in the [[concepts/environment-embedding-geography]] analyses can be drawn from two incompatible sources, and the corpus does not settle which one should anchor downstream inference. One route uses the structured `env_broad_scale` ENVO field (ENVO = Environment Ontology, a controlled vocabulary of environmental terms), which is cleaner but covers only 42% [src: env_embedding_explorer]. The other route harmonizes free-text `isolation_source` strings by keyword matching, which covers 71% of genomes with a label but leaves 17% Other and 12.5% Unknown [src: env_embedding_explorer]. The choice matters because every claim about environment–gene-content association inherits whichever denominator and label noise the chosen field carries, and a third axis — sample coordinates — adds its own unresolved ambiguity.

## Evidence Sides

**Structured ontology field: cleaner labels, smaller denominator.** The `env_broad_scale` field is cleaner but covers only 42% [src: env_embedding_explorer]. The disagreement here is about which error dominates: restricting analysis to the genomes this field covers buys label precision at the cost of the genomes it does not cover, and the 42% is a coverage figure, not an accuracy figure.

**Keyword-harmonized free text: broader denominator, residual unlabeled mass.** Keyword harmonization of `isolation_source` covers 71% of genomes with a label but leaves 17% Other and 12.5% Unknown [src: env_embedding_explorer]. The residual is not a rounding error to be ignored: "Other" and "Unknown" are distinct failure modes — a label that exists but escapes the keyword map, versus no label at all — and both remain as stated, uncollapsed.

**Coordinates as a parallel, unresolved axis.** Coordinates add a parallel tension because distance-decay — the tendency for samples farther apart to be more dissimilar — may reflect environmental context, epidemiological structure, institutional clustering, or approximate coordinates [src: env_embedding_explorer; ecotype_env_reanalysis]. These four explanations are listed as alternatives, not as ranked candidates; no side of this tension claims to have separated them.

## Possible Reconciliations

- *Hypothesis:* the two fields are complementary rather than competing, and `env_broad_scale` can serve as a fallback where `isolation_source` is ambiguous, raising effective coverage without averaging the two denominators together.
- *Hypothesis:* the 17% Other mass is structurally non-random — site-specific and clinical labels — so the keyword route's apparent breadth is coverage-biased in a way the ontology route is not.
- *Hypothesis:* the coordinate ambiguity is separable from the label ambiguity, and distance-decay attributed to environmental context is partly institutional clustering; this would make the field choice secondary to coordinate provenance.

## Resolving Work

- Score the same genome set under both label sources and report agreement, disagreement, and the size of the set labelable by only one — does the field choice change any environment–gene-content conclusion, or only its denominator?
- Partition the 17% Other and 12.5% Unknown by what kind of string they contain, and test whether the unlabeled mass is randomly distributed across taxa — is 71% coverage effectively 71%?
- Restrict analyses to the 42% with `env_broad_scale` and re-run the environment association, comparing effect direction and magnitude against the keyword-labeled run — does label cleanliness change sign or only precision?
- Use isolation_source homogeneity at each coordinate to separate field sites from institutional addresses, then re-test distance-decay — which of the four candidate explanations survives?
