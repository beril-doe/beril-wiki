---
type: "Dataset"
description: "Gene Ontology annotations and their provenance in BERDL and NMDC holdings"
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/nmdc_context_audit__REPORT.md"]
---
# Gene Ontology functional annotation resource

## What this entity is

The canonical name is Gene Ontology functional annotation resource, with the known alias GO (Gene Ontology). [src: amr_cofitness_networks] The report does not specify a stable external identifier for this resource. [src: amr_cofitness_networks]

The NMDC context audit **refines** the provenance description: the BERDL data atlas labels Gene Ontology and Rhea reference ontologies hosted under `kbase.nmdc_arkin` as “NMDC integrated,” although the audit identifies this labeling as provenance blur rather than proof that the resources are NMDC-native. [src: nmdc_context_audit] This distinction is relevant when interpreting GO annotations used in downstream analyses and supports retaining explicit authority and provenance metadata alongside the resource. [src: nmdc_context_audit]

## Key facts from AMR cofitness analysis

The analysis used GO annotations from [[entities/interproscan]] to assess functional enrichment in antimicrobial-resistance cofitness neighborhoods across 28 organisms. [src: amr_cofitness_networks] InterProScan provided 68% gene coverage, reported as 3.6× better than the old SEED annotations. [src: amr_cofitness_networks]

Among GO terms enriched in at least 3 organisms at FDR (false discovery rate) < 0.05, flagellum-dependent cell motility (GO:0071973) occurred in 5 organisms with mean odds ratio (OR) 4.7, flagellum assembly (GO:0044780) occurred in 5 organisms with mean OR 5.3, bacterial-type flagellum (GO:0009288) occurred in 4 organisms with mean OR 4.9, and flagellum-dependent swarming (GO:0071978) occurred in 4 organisms with mean OR 5.0. [src: amr_cofitness_networks] Histidine biosynthesis (GO:0000105) occurred in 3 organisms with mean OR 5.3, and tryptophan biosynthesis (GO:0000162) occurred in 3 organisms with mean OR 5.3. [src: amr_cofitness_networks]

The old SEED/KEGG annotation analysis found 0/280 significant enrichment tests at FDR < 0.05, whereas the GO analysis found 35/3,193 significant tests. [src: amr_cofitness_networks] Mechanism-specific GO analyses produced 212 significant results among 9,244 tests. [src: amr_cofitness_networks]

GO annotations strengthened the interpretation that AMR support-network structure is more organism-specific than mechanism-specific: within-mechanism Jaccard similarity increased from 0.069 with old KEGG annotations to 0.207 with InterProScan GO, while cross-mechanism similarity increased from 0.249 to 0.375. [src: amr_cofitness_networks] The cross-mechanism-versus-within-mechanism comparison had p = 1.0 with old KEGG annotations and p = 4.3×10⁻¹³ with InterProScan GO. [src: amr_cofitness_networks]

The report cautions that GO enrichment may reflect shared dispensability under laboratory conditions rather than direct co-regulation. [src: amr_cofitness_networks] Broad GO categories such as transmembrane transport and membrane functions may obscure more specific signals because they appear in nearly all support networks and genomes. [src: amr_cofitness_networks]

## Related pages

- [[summaries/amr_cofitness_networks__REPORT]] — source report describing the GO-based AMR cofitness analysis. [src: amr_cofitness_networks]
- [[summaries/nmdc_context_audit__REPORT]] — audit of provenance labeling and resource placement for NMDC-named BERDL holdings. [src: nmdc_context_audit]
- [[concepts/pangenome-integration]] — annotation of pangenome cluster representatives improved functional coverage and enrichment detection. [src: amr_cofitness_networks]
- [[concepts/condition-specific-fitness]] — GO enrichment requires distinguishing condition-specific shared dispensability from direct co-regulation. [src: amr_cofitness_networks]
