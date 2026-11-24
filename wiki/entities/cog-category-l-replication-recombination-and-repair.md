---
type: "Other"
description: "COG functional category containing transposases, integrases, IS elements and DNA repair genes, with the highest multi-copy rate among tested categories."
sources: ["summaries/discoveries.md", "summaries/ecotype_functional_differentiation__REPORT.md", "summaries/gene_copy_number_variation__REPORT.md"]
aliases: ["COG L"]
---
# COG category L (replication, recombination and repair)

COG category L (clusters of orthologous groups category for replication, recombination and repair) is the functional category that holds transposases, integrases, IS elements and DNA repair genes. In the cited reports it has the highest multi-copy rate of the categories tested, and it is the strongest enrichment signal among novel/singleton genes. The evidence is correlational. The proposed split between mobile-element and true repair genes has not been run in these reports. [src: ecotype_functional_differentiation, gene_copy_number_variation, discoveries]

## Key facts

- Category L includes transposases, integrases and mobile genetic element machinery. [src: ecotype_functional_differentiation]
- One report labels L "Replication/repair" and notes that it includes transposases and integrases. [src: ecotype_functional_differentiation]
- The gene copy-number report says L contains transposases, integrases and IS elements, which are known to expand in bacterial pangenomes. [src: gene_copy_number_variation]

## Enrichment in novel genes

In bacterial pangenomes analyzed by cog_analysis, novel/singleton genes show L (mobile elements) enrichment of +10.88% with 100% consistency across species. The discoveries digest calls this the strongest signal. [src: discoveries]

The ecotype report calls the effect of L large. It sees this as consistent with Gao et al. (2025), who found source-specific enrichment of COG L in *Cronobacter sakazakii* pangenomes. [src: ecotype_functional_differentiation]

## Multi-copy rate

Across the tested bacterial species, L has a species-level median multi-copy rate of 1.12%. The other medians are V (defense) 0.11%, M (cell wall) 0.11% and K (transcription) 0.12%. For comparison, F (nucleotide metabolism) is 0.062% and H (coenzyme metabolism) is 0.041%. [src: gene_copy_number_variation]

The report states that adaptive COGs, especially L at 1.12%, showed 20–30× the housekeeping multi-copy rate. [src: gene_copy_number_variation] It reads the L dominance and adaptive-accessory enrichment as consistent with the same transposable-element expansion mechanism operating across the bacterial tree of life. This is an interpretation, not a direct test. [src: gene_copy_number_variation]

## Caveats and proposed tests

L mixes mobile elements with true repair genes, so the signal may be driven by transposases. The report proposes splitting L clusters into IS-element loci and true DNA repair loci (recA, mutL, uvr*). It would use bakta_amr or genomad_mobile_elements cross-references, if available in the current KBase Data Lakehouse migration state. [src: gene_copy_number_variation]

The split matters for interpretation. If the effect concentrates in IS elements, the story becomes "transposition-mediated CNV" rather than "adaptive paralogy". This affects the dosage-balance interpretation. [src: gene_copy_number_variation]

The report also proposes restricting to checkm_completeness ≥ 95 and checkm_contamination ≤ 2 and rerunning NB03. This would test whether fragmented assemblies inflate the L effect. [src: gene_copy_number_variation]

## Related pages

See [[entities/insertion-sequence-elements]], [[entities/clusters-of-orthologous-groups-functional-categories]], [[concepts/mechanisms-and-confounders-of-copy-number-variation-in-pangenomes]] and [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]].
