---
type: "Dataset"
description: "CARD (Comprehensive Antibiotic Resistance Database) is an external antibiotic-resistance reference resource; the corpus names its Antibiotic Resistance Ontology (ARO) as a classification standard and its gene groups as a source of known horizontal gene transfer (HGT) controls."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md"]
---
# CARD (Comprehensive Antibiotic Resistance Database)

CARD is an external reference resource for antibiotic resistance. CARD includes the Antibiotic Resistance Ontology (ARO), a separate component of the database rather than another name for it. The corpus names ARO as a way to classify resistance genes systematically by ontology [src: amr_pangenome_atlas]. It also names CARD's `bla` group of β-lactamase families as a reference set for known horizontal gene transfer (HGT) [src: gene_function_ecological_agora].

Aliases: CARD; Comprehensive Antibiotic Resistance Database [src: amr_pangenome_atlas, gene_function_ecological_agora].

## Role in the corpus

**Not used for mechanism labels in the AMR pangenome atlas (caveat).** The atlas built on [[entities/amrfinderplus]] classified resistance mechanisms by keyword matching against AMRFinderPlus product descriptions, for example "beta-lactamase", "efflux" and "acetyltransferase". It did not use CARD ARO terms [src: amr_pangenome_atlas]. Its mechanism categories therefore come from keywords, not from an ontology [src: amr_pangenome_atlas].

**Proposed remedy for the unclassified fraction (caveat).** The atlas's 22.2% "Other/Unclassified" category includes genes whose product descriptions match no keyword set. Examples are ribosomal protection proteins with non-standard names and novel resistance mechanisms [src: amr_pangenome_atlas]. As future work, the report proposes mapping [[entities/bakta]] `bakta_db_xrefs` cross-references to CARD ARO terms. This would give a systematic, ontology-based classification and could shrink that fraction. The remedy is only a proposal and has not been tested [src: amr_pangenome_atlas].

**Source of known-HGT positive controls.** In the gene-function ecological agora project, the Phase 1B design for the consumer null added a set of known-HGT positive controls. AMR was the closest control then available, but a parent-phylum anchor masks intra-phylum HGT, and the new set addressed that gap [src: gene_function_ecological_agora]. The added controls were specific [[entities/beta-lactamases]] families with documented cross-phylum spread, taken from the CARD `bla` group. The design also added class-I [[entities/crispr-cas]] systems, defined by a [[entities/pfam]] family, based on the cross-tree-of-life HGT documented by Metcalf et al 2014 [src: gene_function_ecological_agora]. The evidence describes this as a planned design addition and reports no results from the control set [src: gene_function_ecological_agora].

Related: [[summaries/amr_pangenome_atlas__REPORT]] · [[summaries/gene_function_ecological_agora__REPORT]] [src: amr_pangenome_atlas, gene_function_ecological_agora]
