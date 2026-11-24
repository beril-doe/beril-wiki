---
type: "Concept"
description: "How strain and species names are matched to GTDB pangenome genomes, including coverage, losses, false matches from short or ambiguous names, and repairs; stops at downstream biological interpretation."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/discoveries.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/pitfalls.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Linking isolate and strain records to reference genome databases

This page covers how strain and species names are matched to GTDB pangenome genomes. In the BacDive project, species-name matching linked 42,227 BacDive strains (43.4% of 97,334) to GTDB species. [src: bacdive_metal_validation] In ENIGMA work, a short strain name, MT20, matched an unrelated organism, and a strain-name collision pitfall was documented. [src: genotype_to_phenotype_enigma] The BacDive figures are counts reported in the BacDive project. The collision evidence comes from the ENIGMA and pitfalls reports. [src: bacdive_metal_validation, genotype_to_phenotype_enigma, pitfalls]

## Species-name matching for BacDive

A two-pass species-name bridge linked 42,227 BacDive strains (43.4% of 97,334) to metal tolerance scores across 6,426 unique GTDB species. [src: bacdive_metal_validation, discoveries] Of these strains, 25,089 have isolation source metadata. [src: bacdive_metal_validation]

Exact species-name agreement linked 33,535 strains (34.5%). [src: bacdive_metal_validation] Stripping the GTDB suffix as a fallback added 8,692 strains (8.9%). One example is BacDive "Pseudomonas fluorescens" matching GTDB "Pseudomonas fluorescens A". [src: bacdive_metal_validation]

The bridge enables cross-referencing BacDive phenotypic data with pangenome-derived predictions without Spark queries. [src: discoveries] The project wrote two outputs. One holds all 97,334 strains with match status and metal scores. [src: bacdive_metal_validation] The other holds the 42,227 matched strains. [src: bacdive_metal_validation]

## Losses

The bridge left 55,107 strains (56.6%) unmatched because no GTDB species was available. [src: bacdive_metal_validation] The reports attribute this mainly to GTDB using different species boundaries from LPSN/DSMZ. [src: bacdive_metal_validation, discoveries]

GTDB renames many species with suffixes such as `_A` and `_B`. It also adds genus-level splits such as `Pantoea A`. [src: pitfalls]

Matching loss shrinks small subsets sharply. The research plan referenced n=31 BacDive heavy metal isolates, but only 10 matched pangenome species with metal scores after the bridge. [src: bacdive_metal_validation]

Other databases lose coverage in other ways:
- Joining Fitness Browser organism records to GTDB metadata through NCBI taxonomy IDs returned zero matches in one project. [src: pitfalls] The report states that the `ncbi_taxid` column held the string tokens "t" and "f" instead of numeric IDs. [src: pitfalls]
- BacDive NCBI taxid links to Fitness Browser at species level, not strain level, so the mapping is many-to-one. [src: pitfalls]
- Web of Microbes (WoM) linkage to the pangenome is available at genus level, and all WoM genera have pangenome representation. [src: webofmicrobes_explorer] Species-level matching would need strain-to-genome mapping, which that project did not attempt. [src: webofmicrobes_explorer]

See [[concepts/join-key-validity-and-identifier-format-mismatches]] for more on key problems.

## False matches from short strain names

Short ENIGMA field-isolate names such as MT20, MT42, GW460-LB6 and FW507-14TSA are not globally unique. Matched against `ncbi_strain_identifiers`, they can hit unrelated NCBI organisms. [src: pitfalls]

Matching ENIGMA strains to the pangenome this way caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma] The clearest case is MT20. In ENIGMA it is groundwater *Rhodanobacter glycinis* (Xanthomonadales). In GTDB it is clinical *Streptococcus pneumoniae* (Lactobacillales). [src: pitfalls] The report describes the GTDB MT20 match as 8,434 genomes, 1,751 of them clinical. [src: pitfalls] These injected 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma, pitfalls]

The report presents this as a systematic hazard for any project linking field isolates to reference databases by short strain identifiers. [src: genotype_to_phenotype_enigma] See [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]] and [[entities/enigma]].

## Repairs

For ENIGMA, the fix used CORAL brick 522 (GTDB-Tk assignments) for authoritative taxonomy and cross-checked genus consistency. This cut verified linkages from 32 to 20 and eliminated all false matches. [src: genotype_to_phenotype_enigma] Species-level biogeography is therefore available for only 20 pangenome-linked strains with verified GTDB matches. [src: genotype_to_phenotype_enigma] The pitfalls report recommends rejecting linkages where the source-database genus and the GTDB genus disagree. [src: pitfalls] It also recommends assembly accession (GCF_*) matching where possible, because it is unambiguous. [src: pitfalls]

For BacDive, the recommendation is two-pass matching: exact species name, then the base name with the GTDB suffix stripped. For higher coverage, it suggests matching GCA genome accession to pangenome `genome_id`, which needs `GB_` prefix and version-suffix handling. [src: pitfalls] BacDive `sequence_info.accession` is `GCA_*`, but pangenome `genome_id` uses `GB_GCA_*` or `RS_GCF_*`. Prefixes must be matched or stripped before joining. [src: pitfalls] The BacDive report notes that accession matching would improve coverage but needs a Spark query. [src: bacdive_metal_validation] It proposes querying `kbase_ke_pangenome.genome` to match BacDive GCA accessions directly to pangenome genome_ids, potentially recovering more of the 56.6% unmatched strains. [src: bacdive_metal_validation]

## Open Directions

- Run the proposed query of `kbase_ke_pangenome.genome` to match BacDive GCA accessions to pangenome genome_ids. Measure how many of the 55,107 unmatched strains it recovers.
- Re-run the 10-of-31 metal-isolate subset after accession matching. This would show whether small validation subsets regain power.
- Apply the genus-consistency check to every name-based ENIGMA linkage. Compare the result with the 20 verified links.
- Attempt strain-to-genome mapping for WoM organisms to test species-level linkage beyond genus.
