---
type: "Dataset"
description: "Experimentally determined protein structures held in refdata_pdb and a kescience copy."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/pitfalls.md"]
aliases: ["PDB", "refdata_pdb"]
---
# Protein Data Bank

The Protein Data Bank (PDB; refdata_pdb) holds experimentally determined protein structures. The KBase Data Lakehouse carries it twice: as `refdata_pdb` and as a kescience copy, `kescience_pdb`. The inventory lists ~253K PDB experimental structures. [src: berdl_data_atlas] The evidence comes from the data inventory in [[summaries/berdl_data_atlas__REPORT]] and the cautions in [[summaries/pitfalls]].

## Key facts

- The `refdata_pdb` collection has the tables `pdb_entries` and `pdb_uniprot_mapping`. They supply experimental structures and UniProt mappings. [src: berdl_data_atlas]
- The `kescience_pdb` collection has a `pdb_entries` table. It supplies the kescience copy of the experimental structures. [src: berdl_data_atlas]
- For reference structures, the report recommends `kescience_alphafold` (241M models) together with `refdata_pdb` (253K experimental). Fitness data join through the FitnessBrowser SwissProt best-hit pivot in UC1 (use case). [src: berdl_data_atlas] See [[entities/alphafold-protein-structure-database]] for the model side.

## Pitfalls in kescience_pdb

Several quirks need handling before analysis.

- `pdb_entries` has one row per entry, not per chain. Use `pdb_uniprot_mapping` for chain-level data. [src: pitfalls]
- `r_work` and `r_free` are NULL for non-X-ray methods (EM and NMR). `resolution` is NULL for NMR. Apply method-specific filters before averaging. [src: pitfalls]
- `pdb_uniprot_mapping.pdb_beg` and `pdb_end` are STRING columns. They can hold the literal string "None" for unmapped regions, so coerce or filter them before casting. [src: pitfalls]
- `pdb_entries.organism` reflects only the first polymer entity, so multi-organism complexes look single-organism. [src: pitfalls]
- SIFTS coverage is limited to SwissProt/TrEMBL. Some PDB chains have no UniProt mapping at all. [src: pitfalls]

See also [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]].
