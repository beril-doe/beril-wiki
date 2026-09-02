---
type: "Dataset"
description: "Protein-family domain database used for gene annotation and functional interpretation"
sources: ["summaries/fitness_modules__REPORT.md", "summaries/nmdc_context_audit__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/snipe_defense_system__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Pfam

## What this entity is

**Canonical name:** Pfam (PFam protein-family database). [src: fitness_modules]

**Known aliases:** Pfam; PFam domains. [src: fitness_modules]

**Stable external identifier:** Not reported in the source documents. [src: fitness_modules, nmdc_context_audit]

Pfam is a domain-level annotation resource used to associate genes with protein-family domains and biological-process modules. [src: fitness_modules]

The NMDC context audit identifies Pfam/InterPro as the authority for `nmdc.ref_data`, a Pfam re-host containing 27,481 terms in the `nmdc` tenant. This **refines** the existing description by distinguishing Pfam’s annotation role from its separately maintained BERDL reference-data copy. [src: nmdc_context_audit]

## Annotation and module interpretation

Pfam provided the broadest annotation coverage among the annotation sources evaluated for independent component analysis (ICA), a statistical decomposition method, of bacterial RB-TnSeq fitness data. [src: fitness_modules]

Adding Pfam domains and lowering the enrichment-overlap threshold from 3 to 2 increased the module annotation rate from 8% to 80%, expanded annotated modules from 92 to 890, and unlocked 7.6x more function predictions. [src: fitness_modules]

Pfam-based annotation supported module-level interpretation across 1,116 stable modules identified from 32 organisms, but the source does not attribute a separate number of those modules specifically to Pfam. [src: fitness_modules]

Pfam annotations were used alongside KEGG, SEED, and TIGRFam enrichment to generate 6,691 function predictions for hypothetical proteins across 32 organisms. [src: fitness_modules]

Pfam-based annotations provided broader coverage than KEGG KOs for module-level enrichment, because KEGG KOs were too gene-specific for that purpose. [src: fitness_modules]

The source cautions that Pfam operates at the domain level and may overcount functional associations. [src: fitness_modules]

The truly-dark-gene census **refines** this coverage claim by showing that Pfam rarely supplies domain-level evidence for genes that remain hypothetical after modern reannotation: only 4.0% of 5,870 unique truly dark gene clusters had Pfam hits, comprising 362 hits for 235 clusters. TPR repeats dominated non-DUF hits, while 56 clusters had DUF-only domains. [src: truly_dark_genes]

This result **supports** treating Pfam as a high-value source for partial functional clues without equating a domain hit with a complete gene-function assignment. Among truly dark genes, 4.6% had KEGG KOs, 43.5% had partial eggNOG-mapper signal, and 55.4% of COG assignments were in category S, meaning function unknown. [src: truly_dark_genes]

## SNIPE domain architecture and phage-defense detection

The SNIPE-defense analysis **refines** Pfam’s role as a domain-level resource by correcting the domain signatures used for a specific phage-defense family: PF13250 is the correct Pfam assignment for DUF4041, while PF13455 (Mug113) is the SNIPE nuclease family and is distinct from canonical GIY-YIG PF01541. [src: snipe_defense_system]

In the surveyed BERDL annotations, zero gene clusters contained both DUF4041/PF13250 and canonical GIY-YIG PF01541. Of 4,572 DUF4041-containing gene clusters, 54 carried the description “Meiotically up-regulated gene 113,” consistent with full-length SNIPE proteins containing the Mug113 nuclease annotation. This **contradicts** using PF01541 as the SNIPE nuclease marker and supports searching PF13250, DUF4041, or T5orf172 together with PF13455. [src: snipe_defense_system]

DUF4041/PF13250 occurred in 4,572 gene clusters across 1,696 species and 33 bacterial and archaeal phyla; 13.3% of these clusters were core, 30.7% accessory, and 56.1% singleton, making the accessory-plus-singleton fraction 86.7%. These results **support** interpreting SNIPE-associated Pfam domains as markers of a predominantly mobile defense-family distribution rather than stable core inheritance. [src: snipe_defense_system]

The SNIPE study **supports** Pfam’s use for broad defense-system screening through a curated signature list of approximately 20 Pfam accessions queried against the 833-million-row `interproscan_domains` table. [src: phage_defense_arsenal]

The phage-defense analysis **refines** the provenance description: InterProScan uses version-free accessions such as PF01867, whereas `bakta_pfam_domains` uses versioned accessions such as PF01867.29; cross-database joins therefore require stripping Bakta versions. [src: phage_defense_arsenal]

InterProScan filtering for `analysis = 'Pfam'` and the curated signature list returned ~500K rows in under 90 seconds, while the 18.8-million-row `bakta_pfam_domains` table contained 0 Cas1 PF01867 hits compared with ~25K in InterProScan. This **supports** provenance-aware resource selection rather than treating Pfam-backed tables as interchangeable. [src: phage_defense_arsenal]

The defense study also **refines** interpretation of Pfam-based detection: EggNOG description matching gave 96% CRISPR-Cas prevalence, whereas the specific Cas1 Pfam marker PF01867 gave approximately 55% on the same pangenomes. The 96% value is therefore treated as an upper bound, with detection-method labels required for CRISPR comparisons. [src: phage_defense_arsenal]

These results **support** the existing caution that domain-level annotation can overcount functional associations. The broad DrmB SNF2 helicase Pfam anchor PF00176 made DISARM accessory-enrichment results unreliable because PF00176 is also widespread in non-DISARM housekeeping helicases. [src: phage_defense_arsenal]

The SNIPE report further cautions that eggNOG Pfam annotations may miss divergent homologues and that DUF4041 may occur in non-SNIPE proteins; only 54/4,572 DUF4041 clusters showed Mug113 co-annotation. [src: snipe_defense_system]

## Provenance and related interpretation

The audit’s identification of `nmdc.ref_data` as an external Pfam re-host **supports** maintaining provenance labels when interpreting this resource, especially because the `nmdc` name does not by itself establish NMDC ownership. [src: nmdc_context_audit]

Pfam therefore supports process-level interpretation of [[concepts/cofitness-network-architecture]] and complements sequence-based gene-level approaches such as ortholog transfer, which achieved 95.8% strict precision, 91.2% coverage, and 0.934 F1 in the held-out benchmark. [src: fitness_modules]

The truly-dark-gene analysis **supports** this complementary role: 96.2% of the 6,427 truly dark genes had at least one clue, but only 4.0% had Pfam hits; Tier 3 genes with partial Pfam, COG, or eggNOG function and Tier 4 genes with phenotype-only evidence together comprised 2,314 genes prioritized for narrowing experimental hypotheses. [src: truly_dark_genes]

## Related pages

- [[summaries/fitness_modules__REPORT]] — source summary for the fitness-module analysis. [src: fitness_modules]
- [[summaries/nmdc_context_audit__REPORT]] — audit of provenance, scale, currency, and naming for NMDC-labeled BERDL resources. [src: nmdc_context_audit]
- [[summaries/phage_defense_arsenal__REPORT]] — pan-bacterial defense-system detection and Pfam-based marker analysis. [src: phage_defense_arsenal]
- [[summaries/snipe_defense_system__REPORT]] — SNIPE domain architecture, prevalence, mobility, and phage-defense analysis. [src: snipe_defense_system]
- [[summaries/truly_dark_genes__REPORT]] — residual unknown genes after Bakta reannotation and functional-database integration. [src: truly_dark_genes]
- [[concepts/cofitness-network-architecture]] — cofitness modules and their network structure. [src: fitness_modules]
- [[concepts/gene-essentiality]] — distinction between process-level module context and gene-level function prediction. [src: fitness_modules]
- [[concepts/pangenome-integration]] — cross-organism alignment and conserved module families. [src: fitness_modules]
- [[concepts/provenance-aware-resource-discovery]] — provenance-aware interpretation of re-hosted reference resources. [src: nmdc_context_audit]
- [[entities/kegg]] — gene-level annotation source compared with Pfam. [src: fitness_modules]
- [[entities/seed]] — annotation source used with Pfam for function predictions. [src: fitness_modules]
- [[entities/tigrfam]] — annotation source used with Pfam for function predictions. [src: fitness_modules]
- [[entities/pf13250-duf4041]] — corrected Pfam family assignment for the SNIPE-associated DUF4041 domain. [src: snipe_defense_system]
- [[entities/pf13455-mug113]] — Pfam family assignment for the SNIPE nuclease domain. [src: snipe_defense_system]
