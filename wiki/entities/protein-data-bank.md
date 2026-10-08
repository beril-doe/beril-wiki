---
type: "Dataset"
description: "The Protein Data Bank (PDB), the collection of experimental macromolecular structures available in the KBase Data Lakehouse and used by PaperBLAST, with its query pitfalls."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/paperblast_explorer__REPORT.md", "summaries/pitfalls.md"]
---
# Protein Data Bank

**Aliases:** PDB. The Protein Data Bank supplies the experimental structures in the KBase Data Lakehouse inventory. The atlas counts ~253K PDB experimental structures alongside 241,070,489 AlphaFold predicted structures, 215,130,942 UniProt proteins, and 475,217,233 UniRef100, 188,848,220 UniRef90 and 60,315,044 UniRef50 clusters, with the UniRef counts dated 2026-01 [src: berdl_data_atlas]. Predicted AlphaFold models therefore far outnumber experimental PDB entries in the platform's structural holdings [src: berdl_data_atlas].

## Tables in the KBase Data Lakehouse

Two PDB collections are catalogued [src: berdl_data_atlas]:
- `kescience_pdb`: table `pdb_entries`, described as a kescience copy of the PDB experimental structures [src: berdl_data_atlas].
- `refdata_pdb`: tables `pdb_entries` and `pdb_uniprot_mapping`, holding the PDB experimental structures plus a UniProt mapping [src: berdl_data_atlas].

## Use in PaperBLAST

The PaperBLAST collection contains 12.4 million rows across 14 tables. It links genes to papers by text mining PubMed Central full-text articles, and it adds curated annotations from 13 databases and structural data from the PDB [src: paperblast_explorer].

PaperBLAST holds site annotations for 132,179 PDB structures, with 2.1M site records across 4 types: binding (1.69M), functional (182K), modified (112K) and mutagenesis (104K) [src: paperblast_explorer]. The most frequent of its 48,991 unique ligands are zinc ions (65K sites), chlorophyll A (58K), calcium ions (53K) and heme (44K) [src: paperblast_explorer].

## Query pitfalls

The following documented caveats apply when querying the PDB tables [src: pitfalls]:
- `r_work` and `r_free` are NULL for non-X-ray methods (EM, NMR), and `resolution` is NULL for NMR. Apply filters by experimental method before averaging these fields [src: pitfalls].
- `pdb_uniprot_mapping.pdb_beg` and `pdb_end` are stored as STRING and can literally contain the string `"None"` for unmapped regions. Coerce or filter these values before casting them to numbers [src: pitfalls].
- `pdb_entries.organism` reports only the first polymer entity, so a multi-organism complex appears as a single-organism entry [src: pitfalls].
- `pdb_entries` has one row per entry, not one row per chain. Use `pdb_uniprot_mapping` for chain-level analysis [src: pitfalls].

## Prospective use

The AMR pangenome atlas names AlphaFold and PDB structures as resources for a future structural analysis. In that analysis, AMR proteins would be cross-referenced against these structures to identify novel resistance folds. The report lists this as a proposed next step, not a result, and no novel folds have been reported from it [src: amr_pangenome_atlas].

## Related pages

- [[entities/kescience-alphafold]]
- [[entities/kescience-paperblast]]
- [[entities/uniprot]]
- uniref
- [[concepts/structural-annotation-gap]]
- [[summaries/berdl_data_atlas__REPORT]]
- [[summaries/paperblast_explorer__REPORT]]
- [[summaries/pitfalls]]
- [[summaries/amr_pangenome_atlas__REPORT]]
