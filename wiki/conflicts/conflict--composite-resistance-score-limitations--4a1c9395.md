<!-- tension-hash: 4a1c939511a5523d -->
# Tension: Two BacDive-to-GTDB Bridges, Two Species-Level Coverage Totals

Two projects in this corpus built the same kind of bridge — linking strain records in BacDive (a curated database of bacterial strain metadata and phenotypes) to species in GTDB (the Genome Taxonomy Database, a standardized genome-based bacterial taxonomy) so that genome-derived metal tolerance scores could be joined to strain-level observations. They report different totals for how many strains and how many species that bridge covers. This matters because both totals are used as denominators: coverage figures quoted from one analysis are easily read as applying to the other, and any statement about what fraction of bacterial diversity the metal-tolerance scores reach depends on which bridge produced it. The disagreement arises on [[concepts/composite-resistance-score-limitations]], where both analyses are cited as evidence about what a composite score can and cannot support.

## Evidence Sides

**Side A — the phenotype analysis: 37,368 strains across 5,647 species.** The phenotype analysis reports 37,368 matched strains across 5,647 GTDB species as the basis for its species-level phenotype-to-score comparisons. [src: bacdive_phenotype_metal_tolerance] This is the smaller of the two bridges on both axes — fewer strains and fewer species.

**Side B — the isolation-environment analysis: 42,227 strains across 6,426 species.** The isolation-environment analysis reports 42,227 matched strains across 6,426 GTDB species. [src: bacdive_metal_validation] This is the larger bridge on both axes, and it is the figure that would be quoted if one wanted the most generous statement of taxonomic reach.

Neither side reports the other's number, and neither declares the other's bridge incorrect. The disagreement is in the totals themselves, not in a claim that one pipeline is invalid.

## Possible Reconciliations

- **Hypothesis: downstream filtering, not matching, explains the gap.** If the phenotype analysis required strains to carry usable phenotype records before counting them as matched, its totals would be a subset of a broader match, and the two numbers would describe different stages of one pipeline rather than two conflicting pipelines.
- **Hypothesis: the name-matching rules differ.** If the two analyses applied different species-name reconciliation steps between BacDive taxonomy and GTDB, they would admit different strain sets and therefore different species counts.
- **Hypothesis: the bridges were built against different snapshots.** If the BacDive extract or the GTDB species set differed in version between the two projects, both totals could be internally correct and simply non-comparable.

These are hypotheses; none is established by the evidence in the tension text.

## Resolving Work

- Re-run both bridges from a single pinned BacDive extract and a single pinned GTDB release, then compare strain and species counts; question: does the gap survive version control?
- Diff the two matched-strain tables strain by strain and classify each discrepant record by the stage at which it was dropped; question: is one set a strict subset of the other?
- Publish each project's matching rule and post-match filters as executable code and apply each rule to the other's input; question: which rule reproduces which total?
- Recompute the coverage denominators under both pipelines side by side and report both, rather than a single reconciled figure; question: how much does any downstream coverage claim move between bridges?
