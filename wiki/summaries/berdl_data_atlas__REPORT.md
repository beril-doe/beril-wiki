---
type: "Summary"
description: "Summary of the project BERDL Data Atlas — Inventory, Topic Map, and Cross-Reference Synergies."
doc_type: "short"
full_text: "sources/berdl_data_atlas__REPORT.md"
---
# BERDL Data Atlas — Inventory, Topic Map, and Cross-Reference Synergies

This page summarises the BERDL Data Atlas project, which inventoried the KBase Data Lakehouse, mapped its topics and funders, audited cross-tenant joins, and tested one proposed use case on the live cluster. The inventory reports 1,740 deduplicated tables across 119 databases. [src: berdl_data_atlas] UC1 (use case 1) was sample-validated on the live cluster. [src: berdl_data_atlas] The other use cases (UC3, UC4, UC5) appear in the report as proposals. [src: berdl_data_atlas]

## Key Findings

### Scale and depth

The Lakehouse holds 1,740 deduplicated tables across 119 databases, 17 tenants and 10 funding agencies / programs, spanning 17 biological topics. [src: berdl_data_atlas] It also offers reference layers for biochemistry, mass spec, growth phenotype, viral genomes and environmental embeddings, all queryable from one Spark cluster. [src: berdl_data_atlas] See [[entities/kbase-data-lakehouse]] and [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]].

- ~1.01 B KBase pangenome genes (293K genomes / 27.7K species pangenomes / 132.5M gene clusters). [src: berdl_data_atlas]
- 475M UniRef100 + 189M UniRef90 + 60M UniRef50 protein clusters. [src: berdl_data_atlas]
- 261M MicrobeAtlas OTU-count rows. [src: berdl_data_atlas]
- 75M metatranscriptomic abundance rows. [src: berdl_data_atlas]
- 27.4M FitnessBrowser measurements. [src: berdl_data_atlas]

The largest entity table is `kbase_ke_pangenome.gene`, with 1,011,650,903 rows (~3.4K genes × 293K genomes). [src: berdl_data_atlas]

### Funding agencies and topics

DOE accounts for ~78% of tables: DOE-BER 63%, DOE BRaVE 14%, DOE/NSF 0.6% and DOE-FE 0.4%. [src: berdl_data_atlas] ARPA-H (PROTECT) contributes 4%. [src: berdl_data_atlas] DOI (USGS, United States Geological Survey) and the academic / multi / user namespaces fill the rest. [src: berdl_data_atlas] DOE-BER is the only agency covering all 15 biological topics. [src: berdl_data_atlas] ARPA-H (PROTECT) spans 6 topics. [src: berdl_data_atlas] NSF (National Science Foundation, Planet Microbe), DOE-FE (NETL) and DOI (USGS) are narrow in topic but cover unique sample types. [src: berdl_data_atlas]

Six topics are >75 % single-owner, for example `mobile_phage` at 96 % PhageFoundry, `pangenome` at 79 % kbase and `reference_protein` at 78 % refdata. [src: berdl_data_atlas] Seven topics are cross-tenant, with a top tenant share ≤ 55 %. [src: berdl_data_atlas] See [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]].

### Cross-tenant linkage

The schema-level audit found 536 cross-tenant bridges, defined by 29 canonical join keys. [src: berdl_data_atlas] The keys cover genome, taxonomy, sample, annotation, pathway, biochemistry, protein, phage, literature and KBase workspace. [src: berdl_data_atlas] By tenant span, `sample_id` covers 10 tenants, `genome_id` 9, `ncbi_taxon_id` 9, `feature_id` 9 and `ec_number` 8. [src: berdl_data_atlas] The top bridges share up to 7 keys. Examples are `kbase.pathway ↔ kescience.pathway`, `kescience.pathway ↔ phagefoundry.mobile_phage`, and `refdata.structural ↔ kescience.structural` via `alphafold_pdb` + `pfam` + `protein_id`. [src: berdl_data_atlas] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

### Realized versus theoretical use

Realized cross-tenant use in the audit of BERIL projects is concentrated on the `kbase × kescience` axis. That axis accounts for 36 projects, mostly pangenome × fitness joins via `genome_id` and `ncbi_taxon_id`. [src: berdl_data_atlas] `kescience` appears in 35/66 audited projects (53%). [src: berdl_data_atlas] ENIGMA holds 36% of tables but appears in only 6 projects. [src: berdl_data_atlas] PROTECT holds 4% of tables and appears in 2 projects. [src: berdl_data_atlas]

Five high-leverage bridges had zero realized use at audit time:
- `kescience ↔ refdata` (12 keys, including AlphaFold identifiers). [src: berdl_data_atlas]
- `enigma ↔ phagefoundry` (11 keys). [src: berdl_data_atlas]
- `kbase ↔ refdata` (11 keys, including `gtdb_taxonomy`). [src: berdl_data_atlas]
- `nmdc ↔ protect` (10 keys). [src: berdl_data_atlas]
- `nmdc ↔ refdata` (9 keys). [src: berdl_data_atlas]

See [[concepts/realized-versus-theoretical-cross-collection-data-reuse]].

### Proposed use cases

Four proposed use cases are tied to these bridges. See [[concepts/untapped-cross-program-synergy-use-cases-for-environmental-and-clinical-microbiology]].
- UC1 uses `kescience ↔ refdata`, with 12 keys. It asks whether high-fitness-impact genes have structural signatures detectable in AlphaFold. [src: berdl_data_atlas]
- UC3 uses `kbase ↔ refdata`, with 11 keys. It asks where GTDB clades and KBase species pangenomes disagree and what that implies for gene flow. [src: berdl_data_atlas]
- UC4 uses `nmdc ↔ protect`, with 10 keys. It asks where clinically relevant pathogens live in the environment and what biogeochemistry tracks them. [src: berdl_data_atlas]
- UC5 uses `nmdc ↔ refdata`, with 9 keys. It asks what fraction of NMDC biosamples carry well-formed ENVO (Environment Ontology) terms and where coverage breaks. [src: berdl_data_atlas]

### UC1 structural fitness atlas validation

UC1 was sample-validated on the live cluster. [src: berdl_data_atlas] The original recipe pointed at `protein_id` as the bridge column. This was wrong, because FitnessBrowser uses a composite `(orgId, locusId)` primary key and does not expose `protein_id`. [src: berdl_data_atlas] SQL (structured query language) probing found the working path. It runs from `genefitness` through `(orgId, locusId)` to `besthitswissprot`, then through `sprotAccession = uniprot_accession` to `alphafold_entries`. [src: berdl_data_atlas] See [[concepts/structure-fitness-integration-of-mutant-fitness-data-with-predicted-protein-structures]].

The corrected join gives 55,454 FitnessBrowser genes across 48 organisms with both fitness data and an AlphaFold model. [src: berdl_data_atlas] These genes map to 22,303 distinct AF models. [src: berdl_data_atlas] The validation counted 27,410,721 gene-fitness measurements and 241,070,489 AlphaFold entries. [src: berdl_data_atlas] SwissProt-best-hit coverage of AlphaFold is 99.5% (78,753 / 79,180). [src: berdl_data_atlas]

Within the joined cohort, 6,635 genes are essential (min_fit ≤ −4), 8,271 are strong-defect, 10,950 are moderate and 131 have no defect. Genes were tested at an average of 121–187 conditions per gene. [src: berdl_data_atlas] The report calls the cohort strongly enriched for essentiality signal and ready for downstream structure-function analysis. [src: berdl_data_atlas]

### Intended audiences

The atlas serves KBase users, who want to know where to look and which join recipes to use per topic. It also serves PIs and funders, who want to know which agencies fund which biology and where investment unlocks new analyses. [src: berdl_data_atlas]

## Executive Summary

This part of the report gives the scale of the [[entities/kbase-data-lakehouse|KBase Data Lakehouse]] (1,740 deduplicated tables across 119 databases), its funding mix, its cross-tenant bridges, and a sample-validated use case. [src: berdl_data_atlas]

### Scale and contents

The inventory holds 1,740 deduplicated tables across 119 databases, 17 tenants and 10 funding agencies / programs, spanning 17 biological topics. [src: berdl_data_atlas] The main data layers are listed below. [src: berdl_data_atlas]

- About 1.01 B KBase pangenome genes, from 293K genomes, 27.7K species pangenomes and 132.5M gene clusters. [src: berdl_data_atlas]
- 475M UniRef100, 189M UniRef90 and 60M UniRef50 protein clusters. [src: berdl_data_atlas]
- 241M AlphaFold predicted structures. [src: berdl_data_atlas]
- 261M MicrobeAtlas OTU-count rows. [src: berdl_data_atlas]
- 75M metatranscriptomic abundance rows. [src: berdl_data_atlas]
- 27.4M FitnessBrowser measurements. [src: berdl_data_atlas]
- 40M PubMed records. [src: berdl_data_atlas]

The Lakehouse also has reference layers for biochemistry, mass spec, growth phenotype, viral genomes and environmental embeddings. All of these can be queried from one Spark cluster. [src: berdl_data_atlas]

### Funding coverage

DOE dominates the table count at about 78%. That share splits into DOE-BER 63%, DOE BRaVE 14%, DOE/NSF 0.6% and DOE-FE 0.4%. [src: berdl_data_atlas] ARPA-H (PROTECT) contributes 4% of tables. [src: berdl_data_atlas] NSF (Planet Microbe) contributes 3.5%. [src: berdl_data_atlas] DOI (United States Geological Survey, USGS) and the academic, multi and user namespaces fill the rest. [src: berdl_data_atlas] DOE-BER is the only agency covering all 15 biological topics. [src: berdl_data_atlas]

### Cross-tenant bridges and realized use

The schema defines many cross-tenant links, but realized use is uneven. The audit found 536 schema-level cross-tenant bridges, defined by 29 canonical join keys. [src: berdl_data_atlas] Of 66 audited BERIL projects, 77% (51) already span multiple tenants. [src: berdl_data_atlas] That use concentrates on the kbase × kescience axis, with 36 projects. [src: berdl_data_atlas]

Five bridges with many keys had zero realized use at audit time:

| Bridge | Keys | Note |
|---|---|---|
| kescience ↔ refdata | 12 | includes AlphaFold identifiers (IDs) [src: berdl_data_atlas] |
| enigma ↔ phagefoundry | 11 | [src: berdl_data_atlas] |
| kbase ↔ refdata | 11 | includes gtdb_taxonomy [src: berdl_data_atlas] |
| nmdc ↔ protect | 10 | [src: berdl_data_atlas] |
| nmdc ↔ refdata | 9 | [src: berdl_data_atlas] |

### Validated use case: structural fitness atlas

Use case 1 (UC1), the structural fitness atlas, was sample-validated on the live cluster. [src: berdl_data_atlas] The proposed join recipe needed correction. FitnessBrowser exposes (orgId, locusId), not protein_id. Its bridge to AlphaFold runs through besthitswissprot.sprotAccession. [src: berdl_data_atlas] The corrected join gives a working dataset of 55,454 FitnessBrowser genes across 48 organisms. Each gene has both fitness measurements and an AlphaFold model. [src: berdl_data_atlas] SwissProt-best-hit coverage of AlphaFold is 99.5%. [src: berdl_data_atlas]

### Intended audiences

The atlas targets two groups. KBase users want to know where to look for what, with join recipes per topic. PIs and funders want to see which agencies fund which biology, where coverage exists, and where investment would unlock new analyses. [src: berdl_data_atlas]

## Key Findings: Finding 6: UC1 (structural fitness atlas) sample-validates against the live …

### Data volume

Sixty-five curated headline tables queried on the live cluster show depth across genomes, genes, proteins, structures, phenotype/fitness, samples, community profiles, mass spec, viruses, biochemistry, ontology, environment, and literature. [src: berdl_data_atlas] The largest entity table is `kbase_ke_pangenome.gene` with 1,011,650,903 rows (~3.4K genes × 293K genomes). [src: berdl_data_atlas] See [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]].

### Topic map

Funding agencies differ sharply in topic breadth. DOE-BER spans 15 / 15 topics. [src: berdl_data_atlas] ARPA-H (PROTECT) spans 6 topics. [src: berdl_data_atlas] Defense / HHS is mono-topic: PhageFoundry, entirely in mobile_phage. [src: berdl_data_atlas] NSF (National Science Foundation; Planet Microbe), DOE-FE (NETL) and DOI (USGS, the United States Geological Survey) are narrow in topic but cover unique sample types. [src: berdl_data_atlas]

Six topics are >75 % single-owner. [src: berdl_data_atlas] PhageFoundry owns 96 % of mobile_phage, [src: berdl_data_atlas] kbase owns 79 % of pangenome, [src: berdl_data_atlas] and refdata owns 78 % of reference_protein. [src: berdl_data_atlas] Seven topics are cross-tenant with top tenant ≤ 55 % share. [src: berdl_data_atlas] Taxonomy spans 12 tenants, the broadest cross-tenant surface. [src: berdl_data_atlas] See [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]].

### Linkage audit

The audit scanned 29 canonical join keys covering genome, taxonomy, sample, annotation, pathway, biochemistry, protein, phage, literature, and KBase workspace. [src: berdl_data_atlas] The most widely shared keys, by number of tenants spanned, are:

| Key | Tenants |
|---|---|
| sample_id | 10 [src: berdl_data_atlas] |
| genome_id | 9 [src: berdl_data_atlas] |
| ncbi_taxon_id | 9 [src: berdl_data_atlas] |
| feature_id | 9 [src: berdl_data_atlas] |
| ec_number | 8 [src: berdl_data_atlas] |

At tenant × topic cell granularity, 536 unordered cross-tenant bridges exist. [src: berdl_data_atlas] Top bridges share up to 7 keys, for example kbase.pathway ↔ kescience.pathway and kescience.pathway ↔ phagefoundry.mobile_phage. [src: berdl_data_atlas] The refdata.structural ↔ kescience.structural bridge runs via alphafold_pdb, pfam, and protein_id. [src: berdl_data_atlas] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

### Realized use in BERIL projects

Actual use is concentrated in a few tenants. kbase appears in 53/66 audited projects (80%) and kescience in 35/66 (53%). [src: berdl_data_atlas] The kbase ↔ kescience realized bridge alone accounts for 36 cross-tenant projects, mostly pangenome × fitness joins via genome_id and ncbi_taxon_id. [src: berdl_data_atlas] Table share and project use diverge for other tenants. ENIGMA holds 36% of tables but appears in only 6 projects. [src: berdl_data_atlas] PhageFoundry holds 14% of tables and appears in 5 projects. [src: berdl_data_atlas] PROTECT holds 4% of tables and appears in 2 projects. [src: berdl_data_atlas] See [[concepts/realized-versus-theoretical-cross-collection-data-reuse]].

### Proposed use cases

The report proposes five cross-tenant use cases, each tied to a bridge and its shared-key count. [src: berdl_data_atlas]

- UC2: enigma ↔ phagefoundry, 11 shared keys. Do subsurface prophages mobilize metal-resistance along the Oak Ridge contamination gradient? [src: berdl_data_atlas]
- UC3: kbase ↔ refdata, 11 shared keys. Where do GTDB clades and KBase species pangenomes disagree, and what does that imply for gene flow? [src: berdl_data_atlas]
- UC4: nmdc ↔ protect, 10 shared keys. Where do clinically relevant pathogens live in the environment, and what biogeochemistry tracks them? [src: berdl_data_atlas]
- UC5: nmdc ↔ refdata, 9 shared keys. What fraction of NMDC biosamples carry well-formed ENVO (Environment Ontology) terms, and where does coverage break? [src: berdl_data_atlas]

See [[concepts/untapped-cross-program-synergy-use-cases-for-environmental-and-clinical-microbiology]].

### Correction to the UC1 bridge, and its validation

The original UC1 recipe named `protein_id` as the bridge column. That was wrong, because FitnessBrowser does not expose `protein_id`. It uses a composite `(orgId, locusId)` primary key. [src: berdl_data_atlas] SQL (structured query language) probing found the working path: genefitness joins to besthitswissprot through (orgId, locusId), then to alphafold_entries through sprotAccession = uniprot_accession. [src: berdl_data_atlas] The E. coli sample mappings below support the semantic validity of this corrected path. [src: berdl_data_atlas]

- 27,410,721 FitnessBrowser gene-fitness measurements. [src: berdl_data_atlas]
- 79,180 genes with a SwissProt best-hit. [src: berdl_data_atlas]
- 241,070,489 AlphaFold entries. [src: berdl_data_atlas]
- SwissProt-best-hit coverage in AlphaFold of 99.5% (78,753 / 79,180). [src: berdl_data_atlas]
- 55,454 genes with both fitness data and an AlphaFold model, covering 48 organisms and 22,303 distinct AF models. [src: berdl_data_atlas]

E. coli sample rows confirmed the semantic validity of the join: thrA → AF-P00561-F1, thrB → AF-P00547-F1, thrC → AF-P00934-F1, and talB → AF-Q3Z606-F1. [src: berdl_data_atlas]

The joined cohort splits into fitness classes: 6,635 essential genes (min_fit ≤ −4), [src: berdl_data_atlas] 8,271 strong-defect, [src: berdl_data_atlas] 10,950 moderate, [src: berdl_data_atlas] 29,467 mild, [src: berdl_data_atlas] and 131 no-defect genes. [src: berdl_data_atlas] See [[concepts/structure-fitness-integration-of-mutant-fitness-data-with-predicted-protein-structures]].

## Key Findings; Results

This part of the report gives the platform inventory counts and the profile of the joined FitnessBrowser–AlphaFold cohort. [src: berdl_data_atlas]

### Joined FitnessBrowser–AlphaFold cohort (UC1)

Genes in the joined cohort were tested at an average of 121–187 conditions per gene. The cohort's fitness classes are 6,635 essential (min_fit ≤ −4), 8,271 strong-defect, 10,950 moderate, 29,467 mild and 131 no defect. [src: berdl_data_atlas] The report calls the cohort strongly enriched for essentiality signal and ready for downstream structure-function analysis. [src: berdl_data_atlas] This is the report's own assessment. See [[concepts/structure-fitness-integration-of-mutant-fitness-data-with-predicted-protein-structures]]. The UC1 (use case) validation was probed interactively in an on-cluster Spark Connect session. Its recipe and numbers are in the report and in the fitnessbrowser_alphafold_join.md agent memory. [src: berdl_data_atlas]

### Genomes, pangenomes, clusters

The inventory lists 293,059 KBase ke_pangenome genomes [src: berdl_data_atlas], 27,690 GTDB species clades / pangenomes [src: berdl_data_atlas], 132.5M gene clusters [src: berdl_data_atlas] and 1,011,650,903 KBase pangenome genes. [src: berdl_data_atlas] The refdata collection holds 1,158,553 SPIRE MAGs (metagenome assembled genomes) [src: berdl_data_atlas] and 52,515 JGI GEM-MAGs. [src: berdl_data_atlas] Other genome sets are 3,110 ENIGMA depot genomes and 6,705 ENIGMA SDT genomes [src: berdl_data_atlas], 4,923 PROTECT MIND genomes [src: berdl_data_atlas], and ~1,950 PhageFoundry host genomes across 5 host species. [src: berdl_data_atlas]

### Proteins and structures

| Item | Count |
|---|---|
| UniProt proteins [src: berdl_data_atlas] | 215,130,942 |
| UniRef100 clusters (2026-01) [src: berdl_data_atlas] | 475,217,233 |
| UniRef90 clusters (2026-01) [src: berdl_data_atlas] | 188,848,220 |
| UniRef50 clusters (2026-01) [src: berdl_data_atlas] | 60,315,044 |
| AlphaFold predicted structures [src: berdl_data_atlas] | 241,070,489 |
| PDB experimental structures [src: berdl_data_atlas] | ~253K |

### Phenotype, fitness and growth

FitnessBrowser holds 27,410,721 per-gene fitness measurements across 7,552 experiments and 228,709 genes. [src: berdl_data_atlas] The inventory also lists 97,334 BacDive strain phenotype profiles [src: berdl_data_atlas] and 57,302 carbon-source phenotype measurements. [src: berdl_data_atlas] Web of Microbes has 10,744 growth observations across 37 organisms. [src: berdl_data_atlas]

### Field samples and environmental data

MicrobeAtlas has 463,972 16S samples, 98,919 OTUs (operational taxonomic units) and 260,831,135 OTU-count rows. [src: berdl_data_atlas] Other sample collections are:

- 114,943 USGS (United States Geological Survey) produced-water samples [src: berdl_data_atlas]
- 16,640 NMDC biosamples [src: berdl_data_atlas]
- 5,438 NETL produced-water DNA samples [src: berdl_data_atlas]
- 4,346 ENIGMA SDT samples [src: berdl_data_atlas] and 579 ENIGMA DDT measurement 'bricks' [src: berdl_data_atlas]
- 2,371 Planet Microbe samples [src: berdl_data_atlas]
- 218,510 ENIGMA SDT ASVs (amplicon sequence variants) [src: berdl_data_atlas]
- 83,287 AlphaEarth environment embeddings indexed to KBase genomes [src: berdl_data_atlas]

### Community multi-omics

NMDC GOLD has 75,119,498 metatranscriptomic abundance rows. [src: berdl_data_atlas] Taxonomic profiles total 29,023,980 kraken rows [src: berdl_data_atlas] and 482,669 gottcha rows. [src: berdl_data_atlas] The inventory lists 9,928,244 NOM mass spec assignments. [src: berdl_data_atlas]

### Phage, virus and mobile elements

The refdata collection holds 24,435,662 MetaVR [src: berdl_data_atlas] and 15,677,623 IMG/VR viral sequence records. [src: berdl_data_atlas] PhageFoundry adds 933,103 strain-modelling gene records. [src: berdl_data_atlas]

### Biochemistry, ontology, literature

The inventory lists 56,012 ModelSEED reactions [src: berdl_data_atlas], 45,708 compounds [src: berdl_data_atlas] and 17,783 Rhea reactions. [src: berdl_data_atlas] The NMDC integrated collection has 48,196 GO (Gene Ontology) terms [src: berdl_data_atlas] and 8,813 EC (Enzyme Commission) terms. [src: berdl_data_atlas] Literature resources are 255,096 PaperBLAST curated genes [src: berdl_data_atlas] and 39,994,988 PubMed article records. [src: berdl_data_atlas]

## Results; Interpretation

This part of the report gives the topic and tenant profile of the KBase Data Lakehouse. It then states the report's interpretation: the platform is broad and deep, cross-tenant bridges show synergy, and a few use cases are still untapped. It ends with the report's routing advice and its novelty claims. [src: berdl_data_atlas]

### Topic and tenant profile

Four topics account for most tables, and field_observational is the largest. [src: berdl_data_atlas] See [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]].

- field_observational is 40% of tables, dominated by ENIGMA SDT/DDT structure. [src: berdl_data_atlas]
- mobile_phage is 14% (PhageFoundry). [src: berdl_data_atlas]
- fitness_phenotype is 11%. [src: berdl_data_atlas]
- genome is 6.4%. [src: berdl_data_atlas]
- Every other topic is <4%. [src: berdl_data_atlas]
- The unclassified residual is 0.9% (16 rows), all personal scratch or one-off survey data. [src: berdl_data_atlas]

The report profiles five named tenants by the number of topics each spans and an entropy value. [src: berdl_data_atlas]

| Tenant | Topics | Entropy | Report's description |
|---|---|---|---|
| kbase | 10 | 2.87 | most evenly cross-topic; biological reference hub [src: berdl_data_atlas] |
| nmdc | 11 | 2.61 | broadest coverage [src: berdl_data_atlas] |
| protect | 6 | 2.37 | punches above its size [src: berdl_data_atlas] |
| kescience | 11 | 1.83 | knowledge-engine layer [src: berdl_data_atlas] |
| enigma | 5 | 0.43 | deep-but-narrow [src: berdl_data_atlas] |

The phagefoundry and usgs tenants are mono-topic. [src: berdl_data_atlas]

### Interpretation

The report calls the platform simultaneously broad and deep. Broad means 17 tenants spanning 10 funding programs and 17 biological topics. Deep means billion-row gene records and protein clusters, hundred-million-row community profile tables, and tens of millions of fitness measurements. [src: berdl_data_atlas] See [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]].

The report reads 536 schema-level cross-tenant bridges and 77% realized cross-tenant adoption as evidence that the architecture delivers cross-program synergy. [src: berdl_data_atlas] It attributes the dominance of the kbase × kescience axis in realized analyses to three features of the two tenants. Both are intra-DOE-BER, both are well documented, and together they cover the most cross-tenant topics (genome × phenotype). [src: berdl_data_atlas] This is the report's explanation, not a separately tested result. See [[concepts/realized-versus-theoretical-cross-collection-data-reuse]].

DOE-BER supplies 63% of tables, covers every topic and appears in 80% of BERIL projects. [src: berdl_data_atlas] The report names the concentration of DOE-BER biological references (KBase, KE Science, NMDC, ENIGMA, refdata) in one queryable space as the single largest contributor to BERIL throughput. [src: berdl_data_atlas]

DOE BRaVE (PhageFoundry) and ARPA-H (PROTECT) each appear in fewer than 8 projects despite spanning relevant topics. [src: berdl_data_atlas] The report treats ibd_phage_targeting and cf_formulation_design as existing bridge patterns. It says scaling them is a coordination problem, not a technical one. [src: berdl_data_atlas] It proposes NSF Planet Microbe, DOE-FE NETL and DOI USGS as external validation sets for DOE-BER-anchored analyses. These are small in table count but have unique sample provenance (open ocean, produced waters). [src: berdl_data_atlas]

### Untapped use cases

The report presents five untapped use cases (UC1–UC5) as the next class of analyses. They extend into refdata for structural and GTDB joins, nmdc_arkin for multi-omics and environmental context, PhageFoundry / PROTECT for cross-agency biology, and ENIGMA for subsurface ecology. [src: berdl_data_atlas] See [[concepts/untapped-cross-program-synergy-use-cases-for-environmental-and-clinical-microbiology]].

- It names UC1 as the biggest untapped opportunity. UC1 is the structure × phenotype bridge between kescience and refdata via AlphaFold, with 99.5% join coverage and sample validation. The report says it is ready to scope as a standalone project. [src: berdl_data_atlas] See [[concepts/structure-fitness-integration-of-mutant-fitness-data-with-predicted-protein-structures]].
- It calls investment in shared sample and ENVO (Environment Ontology) ontology, through UC5, the highest-leverage scoping bet. [src: berdl_data_atlas]

### Where to go for which data

The report's universal heuristic is that an analysis crossing topics (for example genome × phenotype × environment) almost certainly crosses tenants. [src: berdl_data_atlas] The canonical bridge is whichever of genome_id, ncbi_taxon_id, sample_id and feature_id both sides expose. data/cross_tenant_bridges.csv lists the exact key set per pair. [src: berdl_data_atlas] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

| Need | Recommended source | Join |
|---|---|---|
| Genome and pangenome | kbase_ke_pangenome (293K genomes / 27.7K species / 132.5M gene clusters) [src: berdl_data_atlas] | genome_id, ncbi_taxon_id [src: berdl_data_atlas] |
| Lab phenotype | kescience_fitnessbrowser (gene-level fitness, hundreds of conditions) [src: berdl_data_atlas] | ke_pangenome on genome_id [src: berdl_data_atlas] |
| Curated phenotype | kescience_bacdive (organismal traits), kescience_webofmicrobes (carbon utilization) [src: berdl_data_atlas] | ncbi_taxon_id [src: berdl_data_atlas] |
| Environmental abundance, multi-omics | nmdc_arkin (kraken / gottcha taxonomy profiles, NOM mass spec, ML embeddings) [src: berdl_data_atlas] | ncbi_taxon_id for taxa; sample_id for biogeochemistry [src: berdl_data_atlas] |
| Subsurface field samples | enigma_coral SDT/DDT/sample tables [src: berdl_data_atlas] | genomes via enigma_genome_depot_enigma on genome_id [src: berdl_data_atlas] |
| Phage and mobile genetic elements | phagefoundry_* per-host catalogs [src: berdl_data_atlas] | host genomes on ncbi_taxon_id [src: berdl_data_atlas] |
| Pathogens | protect_genomedepot (MIND classification) [src: berdl_data_atlas] | environmental abundance via ncbi_taxon_id [src: berdl_data_atlas] |
| Reference structures | kescience_alphafold (241M models), refdata_pdb (253K experimental) [src: berdl_data_atlas] | fitness via the FitnessBrowser SwissProt best-hit pivot (UC1) [src: berdl_data_atlas] |
| Reference proteins and families | refdata_uniref{50,90,100}, refdata_uniprot [src: berdl_data_atlas] | protein_id or pfam_id [src: berdl_data_atlas] |
| Literature | kescience_paperblast, kescience_pubmed [src: berdl_data_atlas] | pmid / doi [src: berdl_data_atlas] |

### Literature anchoring and novelty claims

The atlas references cite the data systems being catalogued, not biological hypotheses being tested. [src: berdl_data_atlas] The most-used realized bridge is kbase × kescience, used by 36 BERIL projects. It builds on the FitnessBrowser pangenome cross-reference of Price et al. (2018), published in *Nature*. [src: berdl_data_atlas] The report says this is now backed by the cross-organism pangenome of the KBase KE pipeline (Arkin et al. 2018). [src: berdl_data_atlas] It presents UC1's validated SwissProt-best-hit-to-AlphaFold path as the realization of the structure-function loop opened by Jumper et al. (2021). [src: berdl_data_atlas]

The report makes the following claims of being first. They are its own claims. [src: berdl_data_atlas]

- The first comprehensive machine-readable catalog, table_topic_map.csv, with tenant, agency, program and biological-topic provenance. [src: berdl_data_atlas]
- The first cross-tenant linkage atlas, with 29 canonical keys defining 536 schema-level bridges. [src: berdl_data_atlas]
- The first realized-versus-theoretical bridge overlay. It surfaces 51 cross-tenant BERIL projects and identifies unused high-leverage bridges. [src: berdl_data_atlas]
- The first per-entity-class depth inventory, using COUNT(*) / COUNT(DISTINCT) across 65 headline tables. [src: berdl_data_atlas]
- The first sample-validated synergy use case (UC1), with a corrected executable join recipe and live-cluster coverage statistics. [src: berdl_data_atlas]

## Interpretation; Data

This part of the report interprets what the atlas does and does not establish, and lists the headline tenants and the data files it ships. The atlas surveys every accessible tenant of the KBase Data Lakehouse. [src: berdl_data_atlas] Its limits are mostly about join validity, mapping and audit coverage.

### Limits of the interpretation

Join validity is shown only for the first use case. The bridge atlas shows that the schema admits a join, but it does not show that the value spaces overlap. [src: berdl_data_atlas] UC1 (use case 1) has been completed, while UC2–UC5 each need their own first sample execution before publication. [src: berdl_data_atlas] The genome_id key means a UPA in KBase, an accession in NCBI and a hash in MAG pipelines. [src: berdl_data_atlas] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

Two tenant-to-agency mappings remain unverified by program documentation: evaluation and lambda, which hold 4 tables in total. [src: berdl_data_atlas] User-confirmed corrections assign phagefoundry to DOE BRaVE and msyscolo to DOE/NSF. These replaced earlier "likely" Defense/HHS and NSF/USDA inferences. [src: berdl_data_atlas] See [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]].

The realized-use audit reads project READMEs. It may miss data-source mentions in research plans or notebooks, so per-project tenant breadth is a lower bound. [src: berdl_data_atlas] See [[concepts/realized-versus-theoretical-cross-collection-data-reuse]] and [[concepts/audit-blind-spots-in-inventories-of-data-and-its-use]].

Depth counts use COUNT(*) row totals for most tables. Only the canonical KBase genome count uses COUNT(DISTINCT genome_id). [src: berdl_data_atlas] A pangenome gene row is one (genome, gene) pair. The report therefore describes 1.01B genes as about 293K genomes × ~3.4K genes per genome. [src: berdl_data_atlas] See [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]].

The atlas does not deduplicate across tenants. [src: berdl_data_atlas] refdata and kbase may hold the same UniProt entries under different cluster indices. ENIGMA and the genome-depot tables share genome records with the ENIGMA SDT layer. [src: berdl_data_atlas]

### Headline tenants and tables

| Tenant | Tables | Contents |
|---|---|---|
| kbase_ke_pangenome | genome, gtdb_species_clade, gtdb_metadata, gene, gene_cluster, pangenome, alphaearth_embeddings_all_years | Computed pangenomes; canonical genome reference and cross-program join anchor [src: berdl_data_atlas] |
| kescience_fitnessbrowser | genefitness, besthitswissprot, gene, experiment | Per-gene fitness across hundreds of conditions; SwissProt best hits are the UC1 structural-bridge pivot [src: berdl_data_atlas] |
| kescience_alphafold | alphafold_entries | 241M predicted structures keyed by UniProt accession [src: berdl_data_atlas] |
| kescience_bacdive | strain | 97K curated strain phenotype profiles [src: berdl_data_atlas] |
| kescience_webofmicrobes | observation, organism | Curated growth observations [src: berdl_data_atlas] |
| kescience_paperblast | curatedgene | 255K curated gene-paper assignments [src: berdl_data_atlas] |
| kescience_pubmed | pubmed_article_wide | 40M PubMed records [src: berdl_data_atlas] |
| kescience_pdb | pdb_entries | PDB experimental structures (kescience copy) [src: berdl_data_atlas] |
| refdata_uniprot | protein, entity | 215M UniProt protein records [src: berdl_data_atlas] |
| refdata_uniref50_2026_01, refdata_uniref90_2026_01, refdata_uniref100_2026_01 | cluster | UniRef protein clusters at 3 redundancy levels, 2026-01 snapshot [src: berdl_data_atlas] |
| refdata_pdb | pdb_entries, pdb_uniprot_mapping | PDB experimental structures and UniProt mapping [src: berdl_data_atlas] |
| refdata_jgi_gem_mags, refdata_spire, refdata_jgi_virus | genome_metadata, imgvr_sequence_info, metavr_main | Reference MAGs (metagenome assembled genomes) and viral sequence catalogs [src: berdl_data_atlas] |
| nmdc_metadata | biosample_set | NMDC biosample registry [src: berdl_data_atlas] |
| nmdc_arkin | kraken_gold, gottcha_gold, metatranscriptomics_gold, nom_gold, embeddings_v1, trait_features, rhea_reactions, go_terms, ec_terms | Integrated multi-omics, ML embeddings, ontology and reactions [src: berdl_data_atlas] |
| enigma_coral | sdt_sample, sdt_genome, sdt_asv, ddt_ndarray | ENIGMA field samples, MAGs, ASVs (amplicon sequence variants) and multidimensional measurement datasets [src: berdl_data_atlas] |
| enigma_genome_depot_enigma | browser_genome, browser_gene, browser_protein | ENIGMA genome, gene and protein browser depot [src: berdl_data_atlas] |
| protect_genomedepot | browser_genome, browser_gene, browser_protein | PROTECT MIND pathogen genome depot [src: berdl_data_atlas] |
| phagefoundry_* (Acinetobacter, Klebsiella, P. aeruginosa, P. viridiflava, ecoliphagesgenomedepot, strain_modelling) | browser_genome, browser_gene, strainmodelling_genome, strainmodelling_gene | DOE BRaVE Phage Foundry host-specific genome browsers and strain models [src: berdl_data_atlas] |
| planetmicrobe_planetmicrobe | sample | NSF (National Science Foundation) Planet Microbe samples [src: berdl_data_atlas] |
| netl_pw_dna | dna_metadata | DOE-FE NETL produced-water DNA samples [src: berdl_data_atlas] |
| usgs_produced_waters | usgspwdb_c, usgspwdb_n | DOI / USGS (United States Geological Survey) produced-water sample data [src: berdl_data_atlas] |
| arkinlab_microbeatlas | otu_counts_long, otu_metadata, sample_metadata | MicrobeAtlas 16S OTU (operational taxonomic unit) profiles [src: berdl_data_atlas] |
| kbase_msd_biochemistry | reaction, molecule | ModelSEED biochemistry reference [src: berdl_data_atlas] |
| globalusers_carbon_source_phenotypes | phenotype_data_table | Carbon-source phenotype measurements, multi-tenant shared [src: berdl_data_atlas] |

Related entity pages include [[entities/kbase-ke-pangenome]], [[entities/fitness-browser]], [[entities/alphafold-protein-structure-database]], [[entities/bacdive]], [[entities/uniref]] and [[entities/microbeatlas]].

### Data files shipped with the report

| File | Rows | Contents |
|---|---|---|
| data/table_topic_map.csv | 1,740 | Every tenant, agency, program, database and table, with primary and secondary topic tags and column names [src: berdl_data_atlas] |
| data/tenant_to_agency.csv | 15 | Tenant to agency, program and primary funder, with user corrections for phagefoundry and msyscolo [src: berdl_data_atlas] |
| data/join_keys.json | 29 keys | Tenant, topic, database and table cells where each canonical key appears [src: berdl_data_atlas] |
| data/join_key_coverage.csv | 29 | Per-key table, tenant and topic coverage [src: berdl_data_atlas] |
| data/cross_tenant_bridges.csv | 536 | Cross-tenant tenant×topic bridges with shared-key counts and key inventories [src: berdl_data_atlas] |
| data/realized_use.csv | 66 | Per-project tenant and database usage, cross_tenant flag and topic focus [src: berdl_data_atlas] |
| data/theoretical_vs_realized.csv | 72 | Tenant-pair overlay of theoretical shared keys and realized project counts [src: berdl_data_atlas] |
| data/untapped_bridges.csv | 20 | Highest-leverage unrealized bridges, with ≥1 shared key and 0 realized projects [src: berdl_data_atlas] |
| data/tenant_reuse_frequency.csv | 9 | Per-tenant BERIL project count and percent [src: berdl_data_atlas] |
| data/data_volume.csv | 65 | Per-entity-class depth using COUNT(*) and COUNT(DISTINCT) per headline table [src: berdl_data_atlas] |

## Supporting Evidence; Future Directions; Authors

This part of the report lists the notebooks that support the atlas and sets out six future directions, then names the author. [src: berdl_data_atlas]

### Supporting notebooks

Six notebooks, numbered 00 to 05, carry the analysis. Together they cover the inventory, the topic map, the linkage atlas, the realized-use audit, the use cases and the data volume. [src: berdl_data_atlas]

- `00_inventory_audit.ipynb` walks the KBase Data Lakehouse Spark catalog. It tags tables by tenant, agency and biological topic, removes dotted-namespace duplicates and audits an unclassified residual of 0.9 %. [src: berdl_data_atlas]
- `01_topic_map.ipynb` gives an agency×topic heatmap and topic concentration. It also gives per-tenant synergy capacity, defined as distinct topics × entropy. [src: berdl_data_atlas]
- `02_linkage_atlas.ipynb` gives a 29-key cross-tenant bridge atlas and a tenant-topic linkage graph. It ranks bridges by shared-key count. [src: berdl_data_atlas]
- `03_realized_use_audit.ipynb` mines READMEs from 66 BERIL projects. It gives tenant-reuse frequency, a theoretical-versus-realized bridge overlay and an untapped-bridge ranking. [src: berdl_data_atlas]
- `04_synthesis_and_use_cases.ipynb` gives a composite atlas figure and audience summaries. It also gives five synergy use cases (UC1–UC5, where UC1 is a use case) derived from the top untapped bridges. [src: berdl_data_atlas]
- `05_data_volume.ipynb` inventories 65 headline tables with COUNT(*) and COUNT(DISTINCT). It gives a per-class rollup, per-table breakdown figures and a headline-numbers summary. [src: berdl_data_atlas]

### Future directions

**Validating the use cases.** The report calls for checking UC2–UC5 against the live cluster. Each needs about 15–30 min of SQL (structured query language) probing to confirm value-space overlap and find join-recipe corrections. [src: berdl_data_atlas] UC3 links kbase and refdata for GTDB harmonization. The report names it the next lowest-friction validation, because it is intra-DOE-BER and both tenants are well documented. [src: berdl_data_atlas] The report also proposes promoting UC1 into its own project, seeded with the validated 55,454-gene cohort. [src: berdl_data_atlas]

**Known gaps.**
- `kescience_alphafold.alphafold_entries` lacks per-residue pLDDT and structural-feature data. The report proposes ingesting these features or computing them from PDB files as a derived KBase Data Lakehouse collection. [src: berdl_data_atlas]
- The tenant-to-agency mappings for `evaluation` and `lambda` still need verification against program documentation. [src: berdl_data_atlas]
- User-confirmed corrections are already in `data/tenant_to_agency.csv`. They map `phagefoundry` to DOE BRaVE and `msyscolo` to DOE/NSF (National Science Foundation). [src: berdl_data_atlas]
- NMDC's metabolomics (3.1M), proteomics (346K) and lipidomics (1.4M) layers are, per agent memory, largely untapped despite being a primary cross-validation source. This rests on agent memory, not on a measurement in the report. [src: berdl_data_atlas] UC4 (`nmdc ↔ protect`) and UC5 (`nmdc ↔ refdata`) both rely on this layer. [src: berdl_data_atlas]

**Maintenance and outreach.** `build_inventory.py` and `data_volume.py` rebuild the canonical CSVs from the live cluster in about 95 s and about 60 s respectively. The report recommends re-running them at each major KBase Data Lakehouse ingest milestone. [src: berdl_data_atlas] It also proposes that the audience messages in NB04 §3 and the per-entity headline numbers in NB05 seed a one-page data-availability summary on the KBase / BERIL UI. [src: berdl_data_atlas]

### Authors

The report lists Adam Arkin (University of California, Berkeley, ORCID: 0000-0002-4999-2931). [src: berdl_data_atlas]

## Caveats and Open Work

- The `protein_id` bridge proposed for UC1 was incorrect and needed correction by SQL probing. [src: berdl_data_atlas]
- UC1 was validated on a sample on the live cluster. The structure-function analysis itself is downstream work. [src: berdl_data_atlas]
- The zero-use bridges refer to the audit time and the audited BERIL projects only. [src: berdl_data_atlas]
- UC3, UC4 and UC5 are proposals whose bridges had no realized use. [src: berdl_data_atlas]

## Slots Into

- [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]]: the row counts, such as 1,011,650,903 gene rows, give platform depth. [src: berdl_data_atlas]
- [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]]: DOE-BER spans all 15 topics, and 6 topics are >75 % single-owner. [src: berdl_data_atlas]
- [[concepts/join-key-validity-and-identifier-format-mismatches]]: the `protein_id` bridge was wrong for FitnessBrowser. [src: berdl_data_atlas]
- [[concepts/realized-versus-theoretical-cross-collection-data-reuse]]: 536 schema-level bridges, against use concentrated on `kbase × kescience`. [src: berdl_data_atlas]
- [[concepts/structure-fitness-integration-of-mutant-fitness-data-with-predicted-protein-structures]]: 55,454 genes across 48 organisms have both fitness data and an AlphaFold model. [src: berdl_data_atlas]
- [[concepts/untapped-cross-program-synergy-use-cases-for-environmental-and-clinical-microbiology]]: UC4 and UC5 rest on bridges with zero realized use. [src: berdl_data_atlas]
