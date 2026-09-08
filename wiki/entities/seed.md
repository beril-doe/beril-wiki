---
type: Dataset
description: SEED is a functional annotation and pathway-membership resource.
sources:
- id: fitness_modules
  resource: ../summaries/fitness_modules__REPORT.md
  title: fitness modules
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
title: SEED
---
# SEED

## What this entity is

**Canonical name:** SEED. [^fitness_modules]

**Known aliases:** No additional aliases are specified in the source reports. [^fitness_modules][^metabolic_capability_dependency]

**Stable external identifier:** No stable external identifier is specified in the source reports. [^fitness_modules][^metabolic_capability_dependency]

SEED is a functional annotation resource used alongside KEGG, TIGRFam, and PFam to derive enrichment-based function predictions from fitness modules. [^fitness_modules] In the metabolic-capability study, SEED subsystem annotations served as a proxy for pathway membership when matching GapMind pathway predictions to gene-fitness data, which **refines** SEED’s role from functional interpretation to pathway-level integration. [^metabolic_capability_dependency]

## Key facts

The analysis used SEED-derived enrichment as one evidence source for interpreting independent component analysis (ICA) fitness modules across 32 organisms. [^fitness_modules]

The study generated 6,691 function predictions for hypothetical proteins, including predictions based on enrichment from SEED together with KEGG, TIGRFam, and PFam. [^fitness_modules]

The 6,691 predictions comprised 2,455 family-backed predictions, representing 37%, and 4,236 module-only predictions. [^fitness_modules]

These predictions were interpreted as evidence for biological-process involvement rather than proof of a specific gene-level molecular function or KEGG KO assignment. [^fitness_modules]

SEED therefore contributes functional-context evidence to the study's [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) analysis, while the held-out benchmark found that ortholog transfer was substantially stronger than module-based approaches for specific gene-level function prediction. [^fitness_modules]

The results connect SEED-supported module interpretation with cross-organism conservation across 1.15M bidirectional-best-hit pairs, 13,402 ortholog groups, and 156 module families spanning at least 2 organisms. [^fitness_modules]

For pathway-dependency analysis, SEED-proxy mapping enabled classification of complete pathways as active, intermediate, or latent, but the report cautions that related subsystem annotations can create false-positive pathway-membership assignments; direct GapMind per-step gene assignments would improve precision. This **qualifies** the earlier use of SEED as functional-context evidence rather than contradicting it. [^metabolic_capability_dependency]

Two GapMind pathways, deoxyribonate and myoinositol, lacked matching SEED subsystem role descriptions and were excluded from all analyses; full-name phenylalanine and tyrosine were recovered through `phe` and `tyr` abbreviation matching, while alanine was excluded because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [^metabolic_capability_dependency]

See the full source summaries: [fitness_modules__REPORT](../summaries/fitness_modules__REPORT.md) and [metabolic_capability_dependency__REPORT](../summaries/metabolic_capability_dependency__REPORT.md). [^fitness_modules][^metabolic_capability_dependency]

Related topics include [gene-essentiality](../concepts/gene-essentiality.md), [pangenome-integration](../concepts/pangenome-integration.md), and [cofitness-network-architecture](../concepts/cofitness-network-architecture.md). [^fitness_modules]

[^fitness_modules]: [fitness modules](../summaries/fitness_modules__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
