---
type: "Summary"
description: "KBase Data Lakehouse atlas maps data depth, cross-tenant bridges, and validated synergy."
doc_type: "short"
full_text: "sources/berdl_data_atlas__REPORT.md"
---
# BERDL Data Atlas — Inventory, Topic Map, and Cross-Reference Synergies

## Overview

The BERDL Data Atlas inventories 1,740 deduplicated tables across 119 databases, 17 tenants, and 10 funding agencies or programs, covering 17 biological topics and billion-row biological datasets on one Spark cluster. It maps data volumes, agency and topic coverage, 536 schema-level cross-tenant bridges defined by 29 canonical join keys, and realized use across 66 BERIL projects. The atlas also identifies five high-leverage unused bridges and sample-validates UC1, a structural fitness atlas joining FitnessBrowser to AlphaFold through SwissProt best hits. [src: berdl_data_atlas]

## Key Findings

### Billion-row biological depth

The atlas audited 65 curated headline tables and found 1,011,650,903 KBase pangenome gene rows spanning 293,059 genomes, 27,690 GTDB species clades or pangenomes, and 132.5M gene clusters. Other large reference layers include 475,217,233 UniRef100 clusters, 188,848,220 UniRef90 clusters, 60,315,044 UniRef50 clusters, 241,070,489 AlphaFold predicted structures, 260,831,135 MicrobeAtlas OTU-count rows, 75,119,498 metatranscriptomic abundance rows, 27,410,721 FitnessBrowser measurements, 39,994,988 PubMed article records, and 215,130,942 UniProt proteins. [src: berdl_data_atlas]

The inventory also contains 97,334 BacDive strain phenotype profiles, 57,302 carbon-source phenotype measurements, 10,744 Web of Microbes growth observations across 37 organisms, 463,972 MicrobeAtlas 16S samples, 114,943 USGS produced-water samples, 16,640 NMDC biosamples, 5,438 NETL produced-water DNA samples, 4,346 ENIGMA SDT samples, 579 ENIGMA DDT measurement bricks, 2,371 Planet Microbe samples, 218,510 ENIGMA SDT ASVs, 83,287 AlphaEarth environment embeddings indexed to KBase genomes, 29,023,980 Kraken and 482,669 Gottcha taxonomic profile rows, 9,928,244 NOM mass-spectrometry assignments, 24,435,662 MetaVR records, 15,677,623 IMG/VR viral sequence records, 933,103 PhageFoundry strain-modelling gene records, 56,012 ModelSEED reactions, 45,708 ModelSEED compounds, 17,783 Rhea reactions, 48,196 GO terms, 8,813 EC terms, and 255,096 PaperBLAST curated gene assignments. [src: berdl_data_atlas]

### Agency and topic coverage

DOE accounts for approximately 78% of the KBase Data Lakehouse tables: DOE-BER contributes 63%, DOE BRaVE 14%, DOE/NSF 0.6%, and DOE-FE 0.4%; ARPA-H contributes 4% and NSF contributes 3.5%. DOE-BER is the only agency covering all 15 biological topics. Six topics are more than 75% single-owner, including mobile_phage at 96% PhageFoundry ownership and pangenome at 79% KBase ownership, while taxonomy spans 12 tenants and has the broadest cross-tenant surface. [src: berdl_data_atlas]

The field_observational topic represents 40% of tables, mobile_phage 14%, fitness_phenotype 11%, and genome 6.4%; all other primary topics represent less than 4% each. Sixteen tables, or 0.9%, remain unclassified and are personal scratch or one-off survey data. [src: berdl_data_atlas]

### Cross-tenant linkage surface

The atlas identifies 536 unordered cross-tenant bridges at tenant-by-topic-cell granularity from 29 canonical join keys covering genome, taxonomy, sample, annotation, pathway, biochemistry, protein, phage, literature, and KBase workspace relationships. The most widespread keys are sample_id across 10 tenants, genome_id across 9, ncbi_taxon_id across 9, feature_id across 9, and ec_number across 8. The highest-key bridges share up to 7 keys, including kbase.pathway with kescience.pathway, kescience.pathway with phagefoundry.mobile_phage, and refdata.structural with kescience.structural. [src: berdl_data_atlas]

Schema-level compatibility does not establish value-space overlap: genome_id can represent different identifiers in KBase, NCBI, and MAG pipelines. UC1 is the only bridge whose value-space validity was sample-executed in this study. [src: berdl_data_atlas]

### Realized cross-tenant use

Among 66 audited BERIL projects, 51, or 77%, span multiple tenants. KBase appears in 53/66 projects, or 80%, and KEScience appears in 35/66, or 53%; the realized kbase × kescience bridge accounts for 36 cross-tenant projects, mostly pangenome-by-fitness joins through genome_id and ncbi_taxon_id. ENIGMA contains 36% of tables but appears in 6 projects, while PhageFoundry contains 14% of tables but appears in 5 projects and PROTECT contains 4% but appears in 2 projects. [src: berdl_data_atlas]

KBase covers 10 topics with entropy 2.87 and is described as the most evenly cross-topic tenant; NMDC covers 11 topics with entropy 2.61; PROTECT covers 6 topics with entropy 2.37; KEScience covers 11 topics with entropy 1.83; and ENIGMA covers 5 topics with entropy 0.43. [src: berdl_data_atlas]

### Untapped bridges and proposed use cases

Five high-leverage bridges had zero realized use at audit time: UC1 kescience ↔ refdata with 12 shared keys for structural fitness signatures; UC2 enigma ↔ phagefoundry with 11 keys for subsurface prophages, metal resistance, and the Oak Ridge contamination gradient; UC3 kbase ↔ refdata with 11 keys for GTDB and KBase species-pangenome disagreement; UC4 nmdc ↔ protect with 10 keys for environmental distributions of clinically relevant pathogens and associated biogeochemistry; and UC5 nmdc ↔ refdata with 9 keys for ENVO ontology completeness in NMDC biosamples. [src: berdl_data_atlas]

### UC1 structural fitness atlas validation

The proposed UC1 join was corrected after SQL probing: FitnessBrowser does not expose protein_id and instead uses the composite orgId, locusId key. The validated path is genefitness joined on orgId and locusId to besthitswissprot, then joined from sprotAccession to uniprot_accession in alphafold_entries. [src: berdl_data_atlas]

The live-cluster validation found 27,410,721 FitnessBrowser gene-fitness measurements, 79,180 genes with a SwissProt best hit, 241,070,489 AlphaFold entries, 78,753 of 79,180 SwissProt best hits represented in AlphaFold, and 55,454 genes across 48 organisms with both fitness data and an AlphaFold model. The joined cohort contains 22,303 distinct AlphaFold models. [src: berdl_data_atlas]

Within the 55,454-gene cohort, 6,635 genes were essential, defined as min_fit ≤ −4; 8,271 were strong-defect, 10,950 moderate, 29,467 mild, and 131 had no defect. Genes were tested under an average of 121–187 conditions per gene. Example Escherichia coli rows linked thrA to AF-P00561-F1, thrB to AF-P00547-F1, thrC to AF-P00934-F1, and talB to AF-Q3Z606-F1. [src: berdl_data_atlas]

### Data-use guidance

For genome and pangenome work, the atlas recommends kbase_ke_pangenome, containing 293K genomes, 27.7K species, and 132.5M gene clusters, with genome_id and ncbi_taxon_id as cross-reference anchors. For laboratory phenotype, kescience_fitnessbrowser provides gene-level fitness across hundreds of conditions; curated phenotype is available through kescience_bacdive and kescience_webofmicrobes; environmental abundance and multi-omics are available through nmdc_arkin; field samples through enigma_coral; phage and mobile-element data through PhageFoundry catalogs; pathogen genomes through protect_genomedepot; structures through kescience_alphafold and refdata_pdb; reference proteins through refdata_uniref50_2026_01, refdata_uniref90_2026_01, refdata_uniref100_2026_01, and refdata_uniprot; and literature through kescience_paperblast and kescience_pubmed. [src: berdl_data_atlas]

The atlas’s universal heuristic is that analyses crossing topics such as genome, phenotype, and environment will usually cross tenants; the appropriate bridge is whichever of genome_id, ncbi_taxon_id, sample_id, or feature_id is exposed by both sides. [src: berdl_data_atlas]

## Caveats

- Join-key presence demonstrates schema-level compatibility, not valid value-space overlap. UC2–UC5 require live-cluster execution; UC1 is the only sample-validated use case. [src: berdl_data_atlas]
- Two tenant-to-agency mappings, evaluation and lambda, remain unverified by program documentation and account for 4 tables total. The mappings for phagefoundry and msyscolo were user-corrected to DOE BRaVE and DOE/NSF, respectively. [src: berdl_data_atlas]
- The realized-use audit mined project README files, so data-source mentions in research plans or notebook source may have been missed; the reported tenant breadth is therefore a lower bound. [src: berdl_data_atlas]
- Most NB05 depth counts are COUNT(*) row totals; only the canonical KBase genome count uses COUNT(DISTINCT genome_id). A pangenome gene row represents one genome-gene pair, so 1.01B gene rows correspond approximately to 293K genomes multiplied by approximately 3.4K genes per genome. [src: berdl_data_atlas]
- Across-tenant deduplication was not performed. Refdata and KBase may contain the same UniProt entries through different cluster indices, and ENIGMA and genome-depot tables share genome records with the ENIGMA SDT layer. [src: berdl_data_atlas]
- The validated UC1 cohort lacks per-residue pLDDT and structural-feature data in kescience_alphafold.alphafold_entries; these features must be ingested or computed from PDB files for downstream structure-function analysis. [src: berdl_data_atlas]
- NMDC metabolomics, proteomics, and lipidomics layers are largely untapped despite containing 3.1M, 346K, and 1.4M records, respectively, and are identified as cross-validation resources for UC4 and UC5. [src: berdl_data_atlas]

## Slots Into

- [[concepts/pangenome-integration]] — The atlas quantifies KBase pangenome depth, GTDB species-clade coverage, and the dominant realized kbase × kescience pangenome-to-fitness bridge. [src: berdl_data_atlas]
- [[concepts/condition-specific-fitness]] — UC1 validates a 55,454-gene cohort linking FitnessBrowser condition-specific measurements to AlphaFold models. [src: berdl_data_atlas]
- [[concepts/gene-essentiality]] — The UC1 cohort contains exact essential, strong-defect, moderate, mild, and no-defect fitness classes across 48 organisms. [src: berdl_data_atlas]
- [[concepts/multi-omics-integration]] — The atlas inventories NMDC metatranscriptomics, taxonomy profiles, mass spectrometry, ontology, and underused metabolomics, proteomics, and lipidomics layers as cross-tenant integration opportunities. [src: berdl_data_atlas]
- [[concepts/environmental-resistome]] — UC2 and UC4 identify untapped bridges connecting environmental or subsurface samples with phage, pathogen, resistance, and biogeochemical data. [src: berdl_data_atlas]
