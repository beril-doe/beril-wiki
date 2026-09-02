---
type: "Concept"
description: "Schema-level keys require value-space validation before biological interpretation."
sources: ["summaries/berdl_data_atlas__REPORT.md"]
---
# Schema Compatibility Does Not Establish Valid Biological Joins

A shared column name or declared join key establishes schema-level compatibility, not that the two datasets contain identifiers with the same meaning, format, provenance, or overlapping values. The [[summaries/berdl_data_atlas__REPORT]] therefore supports treating a proposed biological join as a validation problem rather than assuming that a syntactically executable SQL join is biologically valid. [src: berdl_data_atlas]

## Schema Surface Versus Biological Validity

The BERDL Data Atlas identified 536 unordered cross-tenant bridges at tenant-by-topic-cell granularity, using 29 canonical join keys across genome, taxonomy, sample, annotation, pathway, biochemistry, protein, phage, literature, and KBase workspace relationships. [src: berdl_data_atlas] The most widespread keys were sample_id across 10 tenants, genome_id across 9, ncbi_taxon_id across 9, feature_id across 9, and ec_number across 8. [src: berdl_data_atlas]

These counts describe where schemas expose potentially compatible fields, not where values have been shown to match or represent the same biological object. [src: berdl_data_atlas] In particular, genome_id can represent different identifiers in KBase, NCBI, and MAG pipelines, so a join on genome_id requires value-space checks before its results can support biological conclusions. [src: berdl_data_atlas]

## Evidence From the Validated UC1 Join

The atlas **refines** the interpretation of cross-tenant bridge inventories by showing how a proposed join had to be corrected through SQL probing. FitnessBrowser did not expose protein_id; its usable key was the composite orgId, locusId key. [src: berdl_data_atlas] The validated path joined genefitness to besthitswissprot on orgId and locusId, and then joined sprotAccession to uniprot_accession in alphafold_entries. [src: berdl_data_atlas]

UC1 was the only bridge whose value-space validity was sample-executed in the study. [src: berdl_data_atlas] The live-cluster validation found 27,410,721 FitnessBrowser gene-fitness measurements, 79,180 genes with a SwissProt best hit, 241,070,489 AlphaFold entries, and 78,753 of 79,180 SwissProt best hits represented in AlphaFold. [src: berdl_data_atlas] The resulting cohort contained 55,454 genes across 48 organisms with both fitness data and an AlphaFold model, and the joined cohort contained 22,303 distinct AlphaFold models. [src: berdl_data_atlas]

This result **supports** a staged validation workflow: inspect schemas, probe actual key values, quantify match coverage, and then inspect the biological meaning of the matched records. [src: berdl_data_atlas] The UC1 correction demonstrates that a plausible field suggested by a schema inventory may be absent, while a composite or differently named key provides the valid route. [src: berdl_data_atlas]

## Untested Bridges and Risk of Overinterpretation

Four proposed bridges remained unvalidated at the audit time, and the atlas states that UC2–UC5 require live-cluster execution. [src: berdl_data_atlas] UC2 proposed an enigma ↔ phagefoundry bridge with 11 keys for subsurface prophages, metal resistance, and the Oak Ridge contamination gradient; UC3 proposed a kbase ↔ refdata bridge with 11 keys for GTDB and KBase species-pangenome disagreement; UC4 proposed an nmdc ↔ protect bridge with 10 keys for environmental distributions of clinically relevant pathogens and associated biogeochemistry; and UC5 proposed an nmdc ↔ refdata bridge with 9 keys for ENVO ontology completeness in NMDC biosamples. [src: berdl_data_atlas]

The atlas recorded zero realized use for these five high-leverage bridges, including UC1 before its validation. [src: berdl_data_atlas] Thus, the existence of 536 candidate bridges should not be interpreted as evidence that 536 biological integrations are ready for analysis. [src: berdl_data_atlas]

## Validation Requirements

A defensible join should document the semantic definition of each key, identifier namespaces, transformation rules, overlap and match rates, duplicate behavior, and representative biological records. This requirement follows from the atlas caveat that join-key presence demonstrates schema-level compatibility but not valid value-space overlap. [src: berdl_data_atlas]

Cross-tenant deduplication is also relevant to interpretation: the atlas did not perform it, and it notes that Refdata and KBase may contain the same UniProt entries through different cluster indices, while ENIGMA and genome-depot tables share genome records with the ENIGMA SDT layer. [src: berdl_data_atlas] Counts from a joined dataset should therefore distinguish matched records, distinct biological entities, and duplicated representations. [src: berdl_data_atlas]

This concept connects to [[concepts/cross-tenant-data-bridging]], [[concepts/provenance-aware-resource-discovery]], [[concepts/pangenome-integration]], [[concepts/multi-omics-integration]], and [[concepts/metadata-resolution-and-within-species-heterogeneity]]. [src: berdl_data_atlas]

## Open Directions

- Execute UC2 on the enigma and phagefoundry live-cluster tables, using the 11 candidate keys plus identifier and duplicate audits, to determine whether subsurface prophage, metal-resistance, and Oak Ridge contamination-gradient records share a valid biological value space. [src: berdl_data_atlas]
- Execute UC3 across kbase and refdata with genome and species-pangenome identifiers, using overlap, namespace, and representative-record checks, to test the proposed GTDB–KBase species-pangenome disagreement analysis. [src: berdl_data_atlas]
- Execute UC4 across nmdc and protect with sample, genome, and taxonomic validation, then cross-check environmental distributions against biogeochemical records, to determine whether clinically relevant pathogen observations can be joined without identifier conflation. [src: berdl_data_atlas]
- Execute UC5 across nmdc and refdata with ENVO ontology identifiers, measuring annotation coverage and semantic validity, to test whether NMDC biosample metadata support the proposed ontology-completeness analysis. [src: berdl_data_atlas]
- Extend the validated UC1 cohort with per-residue pLDDT and structural-feature data from PDB files, because kescience_alphafold.alphafold_entries lacks those fields, to test structure–fitness relationships after the identifier join has been validated. [src: berdl_data_atlas]
