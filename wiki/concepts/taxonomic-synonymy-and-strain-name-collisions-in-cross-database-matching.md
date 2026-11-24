---
type: "Concept"
description: "Covers how renamed taxa, differing name formats and non-unique strain names split or falsely merge organisms when matching across cohorts and reference databases; stops at statistical confounding."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/cf_formulation_design__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
---
# Taxonomic synonymy and strain-name collisions in cross-database matching

Matching organisms across cohorts and reference databases fails in two opposite ways. Renamed taxa and differing name formats split one organism into several rows. [src: ibd_phage_targeting, pitfalls] Non-unique short strain names merge unrelated organisms. [src: pitfalls] This page stops short of statistical confounding.

## Splitting: renamed taxa and name formats

### GTDB suffixes and database mismatch
GTDB renames species with suffixes such as _A and _B, adds genus splits, and redefines species boundaries differently from LPSN/DSMZ, the taxonomy [[entities/bacdive]] uses. [src: pitfalls]

Exact species-name matching captures only 34.5% of BacDive strains. [src: pitfalls] A GTDB suffix-removal fallback linked 8,692 additional strains (8.9%), for example BacDive "Pseudomonas fluorescens" to GTDB "Pseudomonas fluorescens A". [src: bacdive_metal_validation] Stripping suffixes adds another 8.9% for 43.4% total. [src: pitfalls] The remaining 56.6% are reported as different species concepts or genera not yet in GTDB r214. [src: pitfalls] The pitfalls digest recommends two-pass matching: exact species name, then base name with GTDB suffix stripped. For higher coverage it suggests matching GCA genome accession to pangenome genome_id, with GB_ prefix and version-suffix handling. [src: pitfalls]

Coverage loss shrinks the useful sample. BacDive has 31 strains tagged cat3=#Heavy metal contamination, but only 10 match pangenome species with metal tolerance scores. [src: pitfalls] The report advises computing post-matching sample sizes and power before interpreting results. [src: pitfalls] Another report notes that its species names follow GTDB and may differ from NCBI names. [src: cf_formulation_design] See also [[entities/gtdb]].

### Renames and formats across microbiome cohorts
The ibd_phage_targeting NB00 found three divergent taxon-name formats in fact_taxon_abundance: CMD_IBD short names, CMD_HEALTHY full MetaPhlAn3 lineage and KUEHL_WGS Kaiju. A naive pivot gave log₂FC ≈ 28 artifacts. [src: ibd_phage_targeting] See [[entities/crohnsphage-data-mart]].

The mart shows the format divergence directly: the short name Faecalibacterium prausnitzii versus a full lineage string ending in s__Faecalibacterium_prausnitzii. [src: pitfalls] Pivoting on taxon_name_original or any string key can silently split a species when cohorts use different MetaPhlAn3 database vintages or curatedMetagenomicData processing stages. [src: pitfalls]

Genus renames under GTDB r214+ drive part of this. In the CrohnsPhage mart, CMD_IBD uses modern names and CMD_HEALTHY uses legacy names. [src: pitfalls] Bacteroides vulgatus (CMD_HEALTHY) and Phocaeicola vulgatus (CMD_IBD) share one NCBI taxid but are treated as separate species. [src: pitfalls] A naive pivot then gives log₂FC ≈ 28 (≈ 2.68 × 10⁸ fold) for every renamed species, because one cohort's mean abundance collapses to pseudocount. [src: pitfalls] B. dorei, coprocola, plebeius, salanitronis, sartorii, massiliensis and coprophilus are also now Phocaeicola. [src: pitfalls] Other reclassification splits are:
- Eubacterium rectale to Agathobacter rectalis. [src: pitfalls]
- E. eligens to Lachnospira eligens. [src: pitfalls]
- E. hallii to Anaerobutyricum hallii. [src: pitfalls]
- Ruminococcus gnavus to Mediterraneibacter gnavus. [src: pitfalls]
- Clostridium bolteae, clostridioforme, symbiosum, innocuum, asparagiforme, hathewayi, citroniae and aldenense to Enterocloster, Hungatella or Erysipelatoclostridium. [src: pitfalls]
- Lactobacillus mucosae and ruminis to Limosilactobacillus and Ligilactobacillus. [src: pitfalls]

The problem applies to fact_taxon_abundance and other MetaPhlAn3-derived tables spanning cohorts processed at different times. It also applies when merging MetaPhlAn outputs with GTDB-r214+ analyses. [src: pitfalls]

### Fixes and their limits
The report's format normalization takes the species component out of full lineage strings and strips brackets from short names, which gives one canonical Genus species string. [src: pitfalls]

NB00 in ibd_phage_targeting ships a 23-entry SYNONYM_MAP covering the major renames, enough for a targeted species battery. [src: pitfalls] Full-taxonomy cross-cohort aggregation needs an NCBI-taxid-backed synonymy layer with GTDB-version-aware rename tables, an NB01 dependency in that project. [src: pitfalls]

The project's synonymy layer maps 2,417 aliases to 1,848 canonical species. [src: ibd_phage_targeting] The file data/species_synonymy.tsv grounds this in ref_taxonomy_crosswalk NCBI taxid matching, supplemented with GTDB r214+ genus renames. [src: ibd_phage_targeting] The report calls it the project-wide reconciliation backbone that made CMD pooling and Kaiju → MetaPhlAn3 projection tractable. [src: ibd_phage_targeting]

Taxid joins alone are not enough in the committed CrohnsPhage crosswalk. It leaves legacy Bacteroides_X rows orphaned because their ncbi_taxid is NaN (not a number). [src: pitfalls] It also lists B. vulgatus and P. vulgatus as separate rows with different canonical_name values. [src: pitfalls]

## Merging: non-unique strain names
Short ENIGMA field-isolate names such as MT20, MT42, GW460-LB6 and FW507-14TSA are not globally unique. Through ncbi_strain_identifiers they can match unrelated NCBI organisms. [src: pitfalls] The report documents this as a systematic integration hazard for any project linking field isolates to reference databases by short identifiers. [src: genotype_to_phenotype_enigma] [[entities/enigma]] MT20 is Rhodanobacter glycinis, a groundwater Xanthomonadales. GTDB's MT20 is clinical Streptococcus pneumoniae, a Lactobacillales. [src: pitfalls] [[entities/rhodanobacter]] is the genus involved. The erroneous match represented 8,434 genomes, 1,751 of them clinical. [src: pitfalls] The collision injected 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma, pitfalls]

Matching via ncbi_strain_identifiers caused 12 of 32 genus-level mismatches in the ENIGMA pangenome linkage. [src: genotype_to_phenotype_enigma, pitfalls] The fix used CORAL brick 522 GTDB-Tk assignments and a genus-consistency check. It cut verified linkages from 32 to 20 and eliminated all false matches. [src: genotype_to_phenotype_enigma] The pitfalls digest generalizes this: reject linkages where the source-database genus and the GTDB genus disagree. [src: pitfalls] It also prefers assembly accession (GCF_*) matching, which is unambiguous. [src: pitfalls] The pitfall is documented in docs/pitfalls.md and affects any project linking ENIGMA strains to the pangenome by name. [src: genotype_to_phenotype_enigma]

Related pages: [[concepts/join-key-validity-and-identifier-format-mismatches]], [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases]], [[concepts/coverage-and-bias-in-linking-strain-phenotype-databases-to-pangenomes]].

## Open Directions
- Compare suffix-stripping with GCA-accession matching on the same BacDive strains. This would show how much of the unmatched strains is a naming artifact and how much is a real absence from GTDB.
- Add the legacy Bacteroides_X rows to ref_taxonomy_crosswalk by name. Then test whether a synonymy layer removes all log₂FC ≈ 28 artifacts across the full taxonomy.
- Audit the other ENIGMA short names for collisions. Use the genus-consistency check against CORAL brick 522 to see how many of the 12 lost linkages can be recovered by accession.
- Test whether a GTDB-version-aware rename table gives the same species set for CMD_IBD and CMD_HEALTHY under successive GTDB releases.
