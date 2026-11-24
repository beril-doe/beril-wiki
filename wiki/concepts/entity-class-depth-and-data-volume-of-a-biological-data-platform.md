---
type: "Concept"
description: "Row counts per entity class (genomes, genes, protein clusters, structures, fitness, samples, community profiles, viruses, biochemistry, literature) and how those counts are defined; stops at what the data show biologically."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/pitfalls.md"]
---
# Entity-class depth and data volume of a biological data platform

This page sets out how many rows the KBase Data Lakehouse holds in each entity class and how those counts were defined. Most numbers come from one inventory report, which queried 65 headline tables on the live cluster. [src: berdl_data_atlas] Some figures are approximate (for example ~253K and ~1,950), and the pangenome table sizes in the genomes section come from a separate pitfalls note. The counts describe volume only. They do not show what the data mean biologically. See [[entities/kbase-data-lakehouse]] and [[summaries/berdl_data_atlas__REPORT]].

## Literature Context

The single candidate paper describes MethArDB, a specialized database of methanogenic archaea, together with its companion toolkit MethArCT [PMID 42742455](https://pubmed.ncbi.nlm.nih.gov/42742455/). The abstract reports 3919 genomes, 87 host-associated plasmids and 42 phages. Genomes carry standardized quality classes (complete, scaffold, draft), protein sequences and metadata on geography, habitats, metabolism and inheritable elements [PMID 42742455](https://pubmed.ncbi.nlm.nih.gov/42742455/). The authors say the field is limited by scarce strain resources, fragmented genomic data, inconsistent genome quality and large uncultured lineages. The abstract gives no evaluation results, so the benefits of the platform's cultivation predictions are not quantified here. Only the abstract was available, not the full text.

The hub page asks a different question. It is an inventory of row counts per entity class on the KBase Data Lakehouse, and it says explicitly that the counts show volume only, not biological meaning. It reports 293,059 KBase ke_pangenome genomes, 27,690 GTDB species clades and 1,011,650,903 pangenome gene rows. It also notes that a row total is not always a count of distinct biological objects. The two sources are therefore not directly comparable. One is a small, single-taxon curated database. The other is a cross-domain platform inventory.

The one point of contact is that both describe genome collections as counts of defined entities. MethArDB's 3919 genomes are about two orders of magnitude fewer than the hub's 293,059 pangenome genomes, but the hub does not cover methanogens specifically. The corpus does not examine genome quality classes, metadata standardization or cultivation prediction. The paper's quality tiers therefore neither support nor contradict the corpus. The corpus's findings are neither in tension with this paper nor an extension of it. The paper is only loosely related context: a taxon-focused resource of the kind that a depth inventory could be compared against. Linking such domain-specific genome sets to the platform's pangenome counts would be a possible future direction, but no such analysis is reported here.

## How the counts are defined

The report calls this the first per-entity-class depth inventory. It ran COUNT(*) or COUNT(DISTINCT) on 65 headline tables. [src: berdl_data_atlas] Most tables use COUNT(*), which gives row totals. Only the canonical KBase genome count uses COUNT(DISTINCT genome_id). [src: berdl_data_atlas] A row total is therefore not always a count of distinct biological objects. A pangenome gene row is one (genome, gene) pair, so 1.01B genes is about 293K genomes × ~3.4K genes per genome. [src: berdl_data_atlas]

The same caution applies to proteins. The kbase_genomes protein table is deduplicated, with 253M unique sequences for ~1B features, so many features share a protein_id. [src: pitfalls]

The report describes the platform as broad, with 17 tenants spanning 10 funding programs and 17 biological topics. It also describes it as deep, with billion-row gene records and protein clusters, hundred-million-row community profile tables and tens of millions of fitness measurements. [src: berdl_data_atlas]

## Genomes, genes and clusters

The largest entity table is kbase_ke_pangenome.gene, with 1,011,650,903 rows. [src: berdl_data_atlas] The report's summary form is ~1.01 B pangenome genes across 293K genomes, 27.7K species pangenomes and 132.5M gene clusters. [src: berdl_data_atlas] The detailed inventory lists 293,059 KBase ke_pangenome genomes, 27,690 GTDB species clades / pangenomes and 132.5M gene clusters. [src: berdl_data_atlas] See [[entities/kbase-ke-pangenome]].

A separate pitfalls note gives approximate sizes for other pangenome tables: gene and gene_genecluster_junction about 1B rows each, and genome_ani about 421M. [src: pitfalls] The same note lists these annotation tables:
- eggnog_mapper_annotations, about 93M rows. [src: pitfalls]
- interproscan_domains, about 833M rows. [src: pitfalls]
- bakta_db_xrefs, about 572M rows. [src: pitfalls]
- gapmind_pathways, about 305M rows. [src: pitfalls]

The note advises never full-scanning these tables and always pre-filtering by gtdb_species_clade_id (or genome_id) before joining. [src: pitfalls]

Other genome collections differ in size:
- See [[entities/reference-mag-and-viral-collections]].
- The inventory lists 3,110 ENIGMA depot genomes and 6,705 ENIGMA SDT genomes. [src: berdl_data_atlas] See [[entities/enigma]].
- It lists 4,923 PROTECT MIND genomes. [src: berdl_data_atlas] See [[entities/protect-genome-depot]].
- It lists about 1,950 PhageFoundry host genomes across 5 host species. [src: berdl_data_atlas]

## Proteins and structures

The inventory lists 215,130,942 UniProt proteins. It also lists 475,217,233 UniRef100, 188,848,220 UniRef90 and 60,315,044 UniRef50 clusters (2026-01). [src: berdl_data_atlas] The report rounds these to 475M, 189M and 60M protein clusters. [src: berdl_data_atlas] See [[entities/uniref]]. Structures number 241,070,489 AlphaFold predictions and about 253K experimental PDB structures. [src: berdl_data_atlas] See [[entities/alphafold-protein-structure-database]] and [[entities/protein-data-bank]].

## Phenotype and fitness

FitnessBrowser holds 27,410,721 per-gene fitness measurements across 7,552 experiments and 228,709 genes. [src: berdl_data_atlas] The pitfalls note gives genefitness as ~27M rows and cofit as ~13.6M rows, and advises filtering by orgId and ideally locusId before scanning. [src: pitfalls] See [[entities/fitness-browser]].
- 97,334 BacDive strain phenotype profiles. [src: berdl_data_atlas] See [[entities/bacdive]].
- 57,302 carbon-source phenotype measurements. [src: berdl_data_atlas]
- 10,744 Web of Microbes growth observations across 37 organisms. [src: berdl_data_atlas] See [[entities/web-of-microbes]].
- 933,103 PhageFoundry strain-modelling gene records. [src: berdl_data_atlas] See [[entities/phagefoundry]].

## Samples and community profiles

MicrobeAtlas holds 463,972 16S samples, 98,919 operational taxonomic units (OTUs) and 260,831,135 OTU-count rows. [src: berdl_data_atlas] See [[entities/microbeatlas]]. Other sample counts in the inventory:

| Collection | Count |
|---|---|
| United States Geological Survey (USGS) produced-water samples | 114,943 [src: berdl_data_atlas] |
| NMDC biosamples | 16,640 [src: berdl_data_atlas] |
| NETL produced-water deoxyribonucleic acid (DNA) samples | 5,438 [src: berdl_data_atlas] |
| ENIGMA SDT samples | 4,346 [src: berdl_data_atlas] |
| ENIGMA DDT measurement 'bricks' | 579 [src: berdl_data_atlas] |
| Planet Microbe samples | 2,371 [src: berdl_data_atlas] |
| ENIGMA SDT amplicon sequence variants (ASVs) | 218,510 [src: berdl_data_atlas] |
| AlphaEarth environment embeddings indexed to KBase genomes | 83,287 [src: berdl_data_atlas] |

See [[entities/planet-microbe]] and [[entities/alphaearth-environmental-embeddings]].

Community multi-omics adds 75,119,498 metatranscriptomic abundance rows from NMDC GOLD. [src: berdl_data_atlas] It also adds 29,023,980 kraken and 482,669 gottcha taxonomic profile rows. [src: berdl_data_atlas] The inventory lists 9,928,244 NOM mass spec assignments. [src: berdl_data_atlas] See [[entities/nmdc-integrated-collections]].

## Viruses

The refdata collection holds 24,435,662 MetaVR and 15,677,623 IMG/VR viral sequence records. [src: berdl_data_atlas]

## Biochemistry, ontology and literature

The inventory lists 56,012 ModelSEED reactions, 45,708 compounds and 17,783 Rhea reactions. [src: berdl_data_atlas] See [[entities/modelseed-biochemistry]]. The NMDC integrated collection holds 48,196 Gene Ontology (GO) terms and 8,813 Enzyme Commission (EC) terms. [src: berdl_data_atlas] Literature holds 255,096 PaperBLAST curated genes and 39,994,988 PubMed article records. [src: berdl_data_atlas] See [[entities/paperblast]] and [[entities/pubmed]]. The report adds that reference layers for biochemistry, mass spec, growth phenotype, viral genomes and environmental embeddings are all queryable from one Spark cluster. [src: berdl_data_atlas]

## Open Directions

- Re-count each headline table with COUNT(DISTINCT) on its natural key. This would show which row totals overstate distinct entities, a gap left by the COUNT(*) approach.
- Add a distinct-genome count for each sample and community table. This would show how much of the 293,059-genome pangenome the community data can be linked to.
- Repeat the inventory at a later date. This would show how fast each class grows, since the UniRef counts are tied to a 2026-01 snapshot.
- Check the report's data_volume rows against the pitfalls row counts for tables such as genome_ani, eggnog_mapper_annotations and genefitness. This would confirm that the two sources use the same counting rules.
