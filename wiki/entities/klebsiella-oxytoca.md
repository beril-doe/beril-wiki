---
type: "Organism"
description: "Klebsiella oxytoca studied for co-fitness, pangenome co-inheritance, and essential dark genes"
sources: ["summaries/cofitness_coinheritance__REPORT.md", "summaries/functional_dark_matter__REPORT.md"]
---
# Klebsiella oxytoca

## What this entity is

**Canonical name:** Klebsiella oxytoca. [src: cofitness_coinheritance]

**Known alias:** Koxy, the study label used for this organism. [src: cofitness_coinheritance]

**Stable external identifier:** No stable external identifier was provided in the source document. [src: cofitness_coinheritance]

## Key facts from cofitness and co-inheritance analysis

Klebsiella oxytoca was one of 11 species initially targeted for analysis, and it contributed data to the primary analysis. [src: cofitness_coinheritance]

Its dataset contained 399 genomes, 4,942 pangenome clusters, and 423,936 co-fitness pairs. [src: cofitness_coinheritance]

Among 162,160 co-fitness pairs evaluated for co-occurrence, the mean phi coefficient was 0.041 for co-fit pairs versus 0.038 for prevalence-matched random pairs, giving a delta phi of +0.003 with p=3.3e-2. [src: cofitness_coinheritance]

Across organisms, Klebsiella oxytoca showed a small positive pairwise co-occurrence effect, consistent with the broader result that pairwise co-fitness only weakly predicts pangenome co-occurrence. [src: cofitness_coinheritance]

Its ICA (independent component analysis) module results included 44 modules, of which 14 (32%) were significant; the mean within-module phi was 0.079 versus a null mean of 0.040. [src: cofitness_coinheritance]

The analysis mapped co-fitness pairs to pangenome cluster pairs using `fb_pangenome_link.tsv`, deduplicated the mappings, and evaluated binary genome-by-cluster presence vectors with phi coefficients. [src: cofitness_coinheritance]

Ten prevalence-matched random pairs were generated per co-fitness pair, with each cluster's prevalence matched independently within a tolerance of +/-5%. [src: cofitness_coinheritance]

The study used Klebsiella oxytoca to examine how laboratory co-fitness measured in the [[entities/kescience-fitnessbrowser]] relates to gene co-occurrence in bacterial pangenomes, contributing to [[concepts/cofitness-network-architecture]] and [[concepts/pangenome-integration]]. [src: cofitness_coinheritance]

## Essential dark-gene prioritization

The newer functional-dark-matter analysis **refines** this organism's role beyond co-fitness and pangenome co-inheritance by listing Klebsiella oxytoca BWI76_RS08540 among its highest-ranked essential dark-gene candidates. The candidate received a score of 0.865 and had OmpA/TIGR02802 domain predictions. [src: functional_dark_matter]

Because essential genes lack viable transposon mutants and therefore standard fitness magnitudes, the report recommends [[entities/crispri]] knockdown followed by growth measurements under standard and stress conditions as the experimental strategy for such candidates. [src: functional_dark_matter] This provides a testable extension of the existing co-fitness evidence rather than contradicting its finding that pairwise co-fitness only weakly predicts pangenome co-occurrence. [src: functional_dark_matter]

## Source

- [[summaries/cofitness_coinheritance__REPORT]] — co-fitness and co-inheritance analysis across bacterial pangenomes. [src: cofitness_coinheritance]
- [[summaries/functional_dark_matter__REPORT]] — experimentally prioritized dark genes and essential-gene follow-up strategies. [src: functional_dark_matter]
