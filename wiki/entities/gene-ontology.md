---
type: Dataset
description: Gene Ontology annotations and their provenance in BERDL and NMDC holdings
sources:
- id: amr_cofitness_networks
  resource: ../summaries/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
- id: nmdc_context_audit
  resource: ../summaries/nmdc_context_audit__REPORT.md
  title: nmdc context audit
title: Gene Ontology functional annotation resource
---
# Gene Ontology functional annotation resource

## What this entity is

The canonical name is Gene Ontology functional annotation resource, with the known alias GO (Gene Ontology). [^amr_cofitness_networks] The report does not specify a stable external identifier for this resource. [^amr_cofitness_networks]

The NMDC context audit **refines** the provenance description: the BERDL data atlas labels Gene Ontology and Rhea reference ontologies hosted under `kbase.nmdc_arkin` as “NMDC integrated,” although the audit identifies this labeling as provenance blur rather than proof that the resources are NMDC-native. [^nmdc_context_audit] This distinction is relevant when interpreting GO annotations used in downstream analyses and supports retaining explicit authority and provenance metadata alongside the resource. [^nmdc_context_audit]

## Key facts from AMR cofitness analysis

The analysis used GO annotations from [interproscan](interproscan.md) to assess functional enrichment in antimicrobial-resistance cofitness neighborhoods across 28 organisms. [^amr_cofitness_networks] InterProScan provided 68% gene coverage, reported as 3.6× better than the old SEED annotations. [^amr_cofitness_networks]

Among GO terms enriched in at least 3 organisms at FDR (false discovery rate) < 0.05, flagellum-dependent cell motility (GO:0071973) occurred in 5 organisms with mean odds ratio (OR) 4.7, flagellum assembly (GO:0044780) occurred in 5 organisms with mean OR 5.3, bacterial-type flagellum (GO:0009288) occurred in 4 organisms with mean OR 4.9, and flagellum-dependent swarming (GO:0071978) occurred in 4 organisms with mean OR 5.0. [^amr_cofitness_networks] Histidine biosynthesis (GO:0000105) occurred in 3 organisms with mean OR 5.3, and tryptophan biosynthesis (GO:0000162) occurred in 3 organisms with mean OR 5.3. [^amr_cofitness_networks]

The old SEED/KEGG annotation analysis found 0/280 significant enrichment tests at FDR < 0.05, whereas the GO analysis found 35/3,193 significant tests. [^amr_cofitness_networks] Mechanism-specific GO analyses produced 212 significant results among 9,244 tests. [^amr_cofitness_networks]

GO annotations strengthened the interpretation that AMR support-network structure is more organism-specific than mechanism-specific: within-mechanism Jaccard similarity increased from 0.069 with old KEGG annotations to 0.207 with InterProScan GO, while cross-mechanism similarity increased from 0.249 to 0.375. [^amr_cofitness_networks] The cross-mechanism-versus-within-mechanism comparison had p = 1.0 with old KEGG annotations and p = 4.3×10⁻¹³ with InterProScan GO. [^amr_cofitness_networks]

The report cautions that GO enrichment may reflect shared dispensability under laboratory conditions rather than direct co-regulation. [^amr_cofitness_networks] Broad GO categories such as transmembrane transport and membrane functions may obscure more specific signals because they appear in nearly all support networks and genomes. [^amr_cofitness_networks]

## Related pages

- [amr_cofitness_networks__REPORT](../summaries/amr_cofitness_networks__REPORT.md) — source report describing the GO-based AMR cofitness analysis. [^amr_cofitness_networks]
- [nmdc_context_audit__REPORT](../summaries/nmdc_context_audit__REPORT.md) — audit of provenance labeling and resource placement for NMDC-named BERDL holdings. [^nmdc_context_audit]
- [pangenome-integration](../concepts/pangenome-integration.md) — annotation of pangenome cluster representatives improved functional coverage and enrichment detection. [^amr_cofitness_networks]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — GO enrichment requires distinguishing condition-specific shared dispensability from direct co-regulation. [^amr_cofitness_networks]

[^amr_cofitness_networks]: [amr cofitness networks](../summaries/amr_cofitness_networks__REPORT.md)
[^nmdc_context_audit]: [nmdc context audit](../summaries/nmdc_context_audit__REPORT.md)
