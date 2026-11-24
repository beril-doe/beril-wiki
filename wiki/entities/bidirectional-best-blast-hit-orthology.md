---
type: "Method"
description: "Ortholog inference by reciprocal best BLAST hits, with connected components used to form ortholog groups."
sources: ["summaries/costly_dispensable_genes__REPORT.md", "summaries/discoveries.md", "summaries/essential_genome__REPORT.md"]
aliases: ["BBH"]
---
# bidirectional best BLAST hit orthology

This page covers ortholog inference by bidirectional best BLAST hits (BBH), with connected components used to form ortholog groups (OGs). The evidence comes from three reports. In the essential_genome report, 2,838,750 BBH pairs yield 17,222 ortholog groups spanning all 48 organisms. [src: essential_genome] The results are sensitive to which organisms are included, and the method has known blind spots. [src: discoveries, essential_genome]

## Key facts

- The essential_genome report takes BBH pairs from the [[entities/fitness-browser]] `besthit` table. [src: essential_genome]
- The report provides data/all_bbh_pairs.csv with 2.84M BBH pairs across 48 organisms. [src: essential_genome]
- The costly_dispensable_genes analysis also assigns ortholog groups with BBH across 48 organisms. [src: costly_dispensable_genes]

## Sensitivity to organism set

The ortholog graph depends on which organisms are included. The fitness_modules comparison used BBH pairs from 5 organisms (10K pairs, 1,861 OGs) and from all 32 organisms (1.15M pairs, 13,402 OGs). [src: discoveries] The report says this produced radically different results. [src: discoveries] It advises extracting orthologs for all organisms in the analysis, not a pilot subset, because the graph is not additive: adding organisms creates new transitive connections. [src: discoveries] See [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]] for the related cofitness work.

## Caveats

- BBH is conservative. It misses paralogs, gene fusions and distant homologs, so some reported orphan essentials may have undetected diverged orthologs. [src: essential_genome]
- Connected components can over-merge. Transitive connections can join unrelated genes into one group, particularly for multi-domain proteins. [src: essential_genome]
- Orphan calls depend on the organism set. Genes with orthologs outside the 48 organisms would be misclassified as orphans. [src: costly_dispensable_genes]

These limits bear on [[concepts/universal-versus-variable-gene-essentiality-across-bacteria]] and [[concepts/limits-of-transposon-based-essentiality-calls]].
