---
type: "Gene_Or_Pathway"
description: "Tryptophan biosynthesis pathway with AMR and FW300-N2E3 fitness evidence"
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/fw300_metabolic_consistency__REPORT.md"]
---
# Tryptophan biosynthesis

## What this entity is

**Canonical name:** Tryptophan biosynthesis. [src: amr_cofitness_networks]

**Known aliases:** No aliases were reported in the source document. [src: amr_cofitness_networks]

**Stable external identifier:** Gene Ontology term GO:0000162. [src: amr_cofitness_networks]

Tryptophan biosynthesis is a functional category identified through [[entities/interproscan]] Gene Ontology annotation in antimicrobial-resistance (AMR) cofitness neighborhoods. [src: amr_cofitness_networks]

## Evidence from AMR cofitness networks

Tryptophan biosynthesis was significantly enriched in AMR cofitness neighborhoods in 3 organisms among GO terms enriched in at least 3 organisms at FDR (false discovery rate) < 0.05, with a mean odds ratio of 5.3. [src: amr_cofitness_networks]

By AMR mechanism, tryptophan biosynthesis was enriched for efflux-resistance genes in 5 organisms. [src: amr_cofitness_networks]

The enrichment supports the broader observation that amino acid biosynthesis occurs in AMR support networks, but it does not establish direct transcriptional co-regulation; the signal may instead reflect shared dispensability under Fitness Browser laboratory conditions, including media containing amino acid supplements. [src: amr_cofitness_networks]

The report identifies a fitness-matched permutation using random non-AMR genes with the same mean-fitness distribution as the key analysis needed to distinguish genuine co-regulation from shared dispensability. [src: amr_cofitness_networks]

## Evidence from FW300-N2E3 metabolic integration

In [[entities/pseudomonas-fw300-n2e3]], GapMind predicted a complete tryptophan biosynthesis pathway, and Fitness Browser experiments showed growth on tryptophan; this **supports** the pathway's physiological relevance beyond the AMR-neighborhood enrichment. [src: fw300_metabolic_consistency]

FW300-N2E3 also increased tryptophan in its WoM exometabolome and had 231 genes with significant fitness effects on tryptophan. This **refines** the AMR interpretation: broad biosynthetic fitness signals can accompany both pathway requirement and extracellular metabolite release, while the report treats the production-plus-growth-but-no-species-level-catabolism pattern as a hypothesis of overflow, cross-feeding, or signaling rather than evidence that FW300-N2E3 cannot grow on tryptophan. [src: fw300_metabolic_consistency]

The 231-gene fitness landscape includes pleiotropic requirements, so it does not by itself establish that all significant genes are tryptophan-specific; separating housekeeping from substrate-specific effects remains necessary. [src: fw300_metabolic_consistency]

## Related pages

This entity is discussed in [[summaries/amr_cofitness_networks__REPORT]] and [[summaries/fw300_metabolic_consistency__REPORT]], and relates to [[concepts/condition-specific-fitness]], [[concepts/gene-essentiality]], [[concepts/metabolic-model-gapfilling]], [[concepts/multi-omics-integration]], [[concepts/pangenome-integration]], and [[entities/histidine-biosynthesis]]. [src: amr_cofitness_networks, fw300_metabolic_consistency]
