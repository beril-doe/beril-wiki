---
type: "Dataset"
description: "Database of predicted protein structures for hundreds of millions of proteins, including the version-6 MSA depth snapshot used here."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/pitfalls.md"]
aliases: ["AFDB", "AlphaFold", "kescience_alphafold"]
---
# AlphaFold Protein Structure Database

The AlphaFold Protein Structure Database (AFDB, also called AlphaFold; the KBase Data Lakehouse collection is `kescience_alphafold`) holds predicted protein structures for hundreds of millions of proteins. [src: alphafold_msa_annotation] This page covers the KBase Data Lakehouse copy, which is a single version-6 snapshot. [src: alphafold_msa_annotation]

## Key facts

- The database and its 2025 update expanded coverage to predicted structures for hundreds of millions of proteins. [src: alphafold_msa_annotation]
- The Lakehouse inventory lists 241,070,489 AlphaFold predicted structures, and live-cluster validation counted the same number of entries. [src: berdl_data_atlas]
- The `alphafold_entries` table holds 241M predicted structures keyed by UniProt accession. [src: berdl_data_atlas]
- The `alphafold_msa_depths` table gives multiple sequence alignment (MSA) depth per UniProt accession. [src: alphafold_msa_annotation]
- All entries are model version v6, so the `model_version` column currently has no variation. [src: pitfalls]
- The report recommends `kescience_alphafold` (241M models) with `refdata_pdb` (253K experimental structures) as reference structures. Fitness joins through the FitnessBrowser SwissProt best-hit pivot (UC1, a use case). [src: berdl_data_atlas] See [[entities/protein-data-bank]] and [[concepts/structure-fitness-integration-of-mutant-fitness-data-with-predicted-protein-structures]].

## Coverage

SwissProt-best-hit coverage in AlphaFold was 99.5% (78,753 / 79,180) in live-cluster validation. [src: berdl_data_atlas] Of bacterial gene clusters, 38,051,842 (28.7%) bridge successfully to `kescience_alphafold.alphafold_msa_depths`. [src: alphafold_msa_annotation] The report states that prior analyses had not quantified the core–accessory coverage gradient at structural-novelty resolution with a database of 241M AlphaFold entries. [src: alphafold_msa_annotation] See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]] and [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes]].

Structure-based classification still exposes annotation gaps. The report cites Schaeffer et al. (2026), who found more than 100,000 domains with no Pfam mapping in AFDB Swiss-Prot entries. [src: alphafold_msa_annotation] It also cites Tunyasuvunakool et al. (2021): only 17% of human protein residues were covered by experimental structures before AlphaFold, and the report describes the bacterial situation as similar. [src: alphafold_msa_annotation] See [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates]].

## Caveats

- About 9% of entries have MSA depth < 30, described as low-confidence predictions. The pitfalls digest recommends filtering by `msa_depth` for structure-based analyses. [src: pitfalls]
- The snapshot is static, and newly deposited UniProt entries may change MSA depths as databases grow. [src: alphafold_msa_annotation]
- Coverage is UniProt-only, so proteins absent from UniProt have no AlphaFold entry. [src: pitfalls]
- Per-residue pLDDT confidence lives in the structure files, not in the metadata. [src: pitfalls] `alphafold_entries` carries no per-residue pLDDT or structural-feature data. The report proposes ingesting those features, or computing them from PDB files as a derived collection. [src: berdl_data_atlas]
- The UniRef100-to-UniProt join requires stripping the `UniRef100_` prefix. This is a per-row string operation, so large joins should consider a materialized mapping table. [src: pitfalls] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

## Sources

See [[summaries/alphafold_msa_annotation__REPORT]], [[summaries/berdl_data_atlas__REPORT]], [[summaries/pitfalls]] and [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]].

Claim C12 repeats C8 and C13 and is not cited separately.
