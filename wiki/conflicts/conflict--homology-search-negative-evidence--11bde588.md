<!-- tension-hash: 11bde5880711daef -->
# Why do bakta Pfam tables come up empty: query format, reduced profile set, or hypothetical-only search?

Three corpus sources explain empty or sparse Pfam results from bakta in different ways. Pfam is a database of protein-domain families, and bakta is a bacterial genome annotation pipeline that can report Pfam hits. The explanations are a query-format problem, a reduced profile set, and a search restricted to hypothetical proteins; one source also says the correct query format is still unestablished. The disagreement matters because a Pfam table with no hits is negative homology-search evidence. As [[concepts/homology-search-negative-evidence]] argues, such a result does not by itself demonstrate that a domain is absent. The 12/22 coverage gap [src: plant_microbiome_ecotypes] and the 0 hits across all 11 domains tested [src: pitfalls] are the concrete cases. No source tests another's mechanism, so the explanations stand unreconciled. [src: plant_microbiome_ecotypes, discoveries, pitfalls]

## Evidence Sides

**Side A: Query format, then a reduced "core" profile set (plant microbiome report)**
The plant microbiome report treats its original zero as a resolved query-format problem involving versioned IDs (Pfam accessions that carry a version suffix). [src: plant_microbiome_ecotypes] It attributes the separate 12/22 coverage gap to a likely reduced "core" Pfam profile set in bakta. [src: plant_microbiome_ecotypes] Because the report calls the profile-set explanation "likely", it is an inference rather than a demonstrated cause. [src: plant_microbiome_ecotypes]

**Side B: Pfam search run only on hypotheticals (discoveries digest)**
The discoveries digest attributes the under-reporting to bakta running its Pfam search only on hypotheticals, meaning proteins without another assigned function. [src: discoveries]

**Side C: Correct query format not yet established (pitfalls digest)**
The pitfalls digest's entry reports 0 hits across all 11 domains tested and still describes the correct query format as unestablished. [src: pitfalls] The plant microbiome report, by contrast, treats its versioned-ID format problem as resolved. [src: plant_microbiome_ecotypes]

## Possible Reconciliations

- *Hypothesis 1:* The mechanisms may stack. A versioned-ID format error could explain total zeros, while a hypothetical-only search or a reduced profile set could explain partial coverage gaps such as the 12/22 gap. No source has tested this. [src: plant_microbiome_ecotypes, discoveries, pitfalls]
- *Hypothesis 2:* The pitfalls entry may predate or not reflect the plant microbiome report's format fix, so Side C would describe an earlier state of knowledge rather than a live contradiction. The passages do not establish their relative timing, so this remains untested.
- *Hypothesis 3:* A reduced "core" profile set and a hypothetical-only search are not mutually exclusive; both could reduce coverage at once.

## Resolving Work

- Re-run the pitfalls test across the 11 domains, querying the bakta Pfam tables with both versioned and unversioned accessions, to show whether the 0-hit result is a format artifact and whether the plant microbiome fix generalizes.
- For the items behind the 12/22 coverage gap, compare bakta Pfam output against an independent full-Pfam search on the same proteins, for example HMMER `hmmscan` (which scans protein sequences against hidden Markov model profiles) with the complete Pfam library. Families found by the full library but absent from bakta's profile set would test the reduced-profile-set explanation.
- Split bakta Pfam hits by whether the protein is annotated as hypothetical. If no non-hypothetical protein ever carries a Pfam hit, that would support the discoveries digest's mechanism.
- Inspect the bakta version and database configuration used in each project to show whether a "core" profile subset was installed and whether the three sources describe different software setups.
