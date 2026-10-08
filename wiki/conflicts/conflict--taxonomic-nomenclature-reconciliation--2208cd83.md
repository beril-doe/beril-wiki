<!-- tension-hash: 2208cd8319a61705 -->
# BacDive-to-pangenome coverage: does strain matching reach 43.4% or 38.4%?

Two projects bridged BacDive (a curated database of bacterial strain phenotypes) to pangenome species (species-level gene collections pooled across genomes) defined by the GTDB (Genome Taxonomy Database), and they report different strain-to-pangenome coverage [src: bacdive_metal_validation, bacdive_phenotype_metal_tolerance]. This matters for the reconciliation concerns described in [[concepts/taxonomic-nomenclature-reconciliation]]. When two bridges over the same strain collection disagree, their coverage figures cannot be compared or reused without knowing each bridge's matching rules. The records available here do not settle what causes the gap [src: bacdive_phenotype_metal_tolerance].

## Evidence Sides

**Side A: higher coverage with exact matching plus GTDB suffix removal.** One bridge linked 42,227 strains (43.4%) using exact species-name matching, with GTDB suffix removal as a fallback [src: bacdive_metal_validation].

**Side B: lower coverage, counted as matched with a metal score.** Another bridge reports 37,368 strains (38.4%) matched to the pangenome with a metal score [src: bacdive_phenotype_metal_tolerance]. The available evidence does not state whether this bridge used the suffix-removal fallback, so the gap cannot be attributed to method from these records [src: bacdive_phenotype_metal_tolerance]. In addition, this report's own species-level percentage is internally inconsistent [src: bacdive_phenotype_metal_tolerance].

Neither figure is established here as the correct coverage. Each is a project-specific count under its own stated criterion.

## Possible Reconciliations

- **Hypothesis 1: method difference.** Side B may have used exact name matching without the GTDB suffix-removal fallback. Under this hypothesis, Side B's lower count would reflect suffix-bearing names it failed to match. The evidence neither confirms nor rules this out.
- **Hypothesis 2: reporting error.** Side B's species-level percentage is internally inconsistent [src: bacdive_phenotype_metal_tolerance], so its strain-level figure or its denominator might also be misreported. This would need checking against the underlying output files before either side is treated as a method benchmark.

## Resolving Work

- **Rerun Side B with the fallback toggled.** Data: Side B's BacDive bridge table. Method: rerun the name matching with and without the GTDB suffix-removal fallback. Question: does adding the fallback close the gap to Side A's count?
- **Join the two bridge tables strain by strain.** Data: both projects' full bridge tables. Method: join on the BacDive strain identifier and tabulate matched-in-A-only, matched-in-B-only and matched-in-both. Question: do the discordant strains share suffix-bearing GTDB names, or species with no metal score?
- **Recompute Side B's species-level percentage.** Data: Side B's species-level output. Method: recompute the percentage from the raw counts and the stated denominator. Question: which number in the internally inconsistent statement is wrong, and does the error carry into the strain-level coverage?
- **Test a name-independent matching route.** Data: BacDive genome accessions and GTDB genome accessions. Method: match by accession instead of by species name, and compare the result with both name-based bridges. Question: what fraction of strains either name-based bridge misses, and is one bridge systematically more permissive?
