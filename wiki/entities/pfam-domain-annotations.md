---
type: "Dataset"
description: "InterProScan-derived Pfam domain annotations of Fitness Browser gene clusters with higher coverage than GO."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md", "summaries/fitness_modules__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/nmdc_context_audit__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
aliases: ["IPS", "InterProScan domain table", "Pfam", "Pfam/InterPro", "interproscan_domains", "nmdc.ref_data"]
---
# Pfam domain annotations

This page covers InterProScan-derived Pfam domain annotations of Fitness Browser gene clusters, which have higher coverage than GO. The main source is the `interproscan_domains` table (also called IPS) in [[entities/kbase-ke-pangenome]]. Several projects find that it covers more genes than GO or the Bakta Pfam table. [src: amr_cofitness_networks, gene_function_ecological_agora, phage_defense_arsenal]

## Key facts

- The AMR (antimicrobial resistance) cofitness report uses the `interproscan_go`, `interproscan_domains` (Pfam) and `bakta_annotations` tables for GO (Gene Ontology) terms, Pfam domains and KEGG orthology of Fitness Browser (FB) gene clusters. [src: amr_cofitness_networks]
- Its generated file `data/fb_interproscan_pfam.csv` holds 228,672 rows of InterProScan Pfam domains for FB gene clusters. [src: amr_cofitness_networks]
- One audit describes `interproscan_domains` as 146 M Pfam hits across 132.5 M cluster representatives, with 83.8 % cluster coverage. [src: gene_function_ecological_agora] Another table lists it as 833M hits with 83.8% cluster coverage. [src: gene_function_ecological_agora] The two hit counts differ, and the reports do not reconcile them. The phage defense report also gives 833M rows. [src: phage_defense_arsenal]
- The `nmdc.ref_data` resource holds 27,481 Pfam terms. [src: nmdc_context_audit] The NMDC context audit classifies it as an external re-host from the Pfam consortium. [src: nmdc_context_audit] It names Pfam/InterPro as the true authority for it [src: nmdc_context_audit] and uses `nmdc_ref_data.pfam_terms` to prove Pfam provenance. [src: nmdc_context_audit]

## Coverage compared with other sources

In the AMR support-network analysis, Pfam has 88% coverage versus 68% for GO. [src: amr_cofitness_networks] The report proposes that domain-level enrichment may reveal more specific support-network functions than broad GO terms do. [src: amr_cofitness_networks] See [[entities/interproscan-go-annotations]] and [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]].

In the gene function ecological agora report, median bakta/IPS Pfam coverage ratio was 0.102, so IPS has ~10× higher coverage on average. [src: gene_function_ecological_agora] The phage defense report likewise finds `interproscan_domains` far broader than `bakta_pfam_domains`, which has 18.8M rows. [src: phage_defense_arsenal] See [[entities/bakta-pfam-domains]].

In fitness modules, PFam is the dominant annotation source and gives domain-level labels that match module granularity. [src: discoveries] PFam provided the broadest annotation coverage. [src: fitness_modules] Adding PFam domains and lowering the enrichment overlap threshold from 3 to 2 raised module annotation from 8% to 80% (92 to 890 modules), unlocking 7.6x more function predictions. [src: fitness_modules] The same report cautions that PFam annotations, despite the best coverage, are at the domain level and may overcount functional associations. [src: fitness_modules] See [[concepts/fitness-modules-essential-genes-and-condition-specific-gene-function]].

Pfam does little for the hardest genes. Only 4.0% of truly dark genes have Pfam domain hits, and only 4.6% have KEGG KOs (KEGG orthologs). The report reads this as resistance to standard functional annotation methods. [src: truly_dark_genes] Pfam gives 362 hits for 235 truly dark clusters (4.0%), with TPR repeats dominating non-DUF hits. [src: truly_dark_genes] Fifty-six clusters have DUF-only domains. [src: truly_dark_genes] See [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]].

## Use as a Lakehouse substrate

The gene function ecological agora report treats `interproscan_domains` as the authoritative Pfam source. [src: gene_function_ecological_agora] A mid-pilot audit found the table had been unused in the first version. [src: gene_function_ecological_agora] The audit found only 1 zero-coverage marker, PF13415, a minor HATPase variant. [src: gene_function_ecological_agora] The report chose it for all Phase 3 architectural work, which removed the planned HMMER recomputation fallback. [src: gene_function_ecological_agora] It recommends InterProScan as the default substrate for domain-accession queries, not eggNOG PFAMs, which store domain names rather than accessions. [src: gene_function_ecological_agora]

Two practical points from the phage defense report apply to queries. First, filtering `interproscan_domains` by `analysis = 'Pfam' AND signature_acc IN (<curated_pfam_list>)` and joining to `gene_cluster` on `gene_cluster_id` returns ~500K rows in under 90 s in one query. This was for a list of ~20 accessions, and no per-species batching was needed. [src: phage_defense_arsenal] Second, `interproscan_domains.signature_acc` uses version-free accessions such as PF01867. `bakta_pfam_domains.pfam_id` uses versioned ones such as PF01867.29. [src: phage_defense_arsenal] See [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]].
