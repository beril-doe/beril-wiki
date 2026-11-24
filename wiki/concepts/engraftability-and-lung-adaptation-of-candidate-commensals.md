---
type: "Concept"
description: "Use of patient prevalence, transcriptional activity and pangenome isolation sources to judge whether commensals persist in the airway; stops at the metabolic design."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/discoveries.md"]
---
# Engraftability and lung adaptation of candidate commensals

This page covers how the cystic fibrosis (CF) formulation design judged whether candidate commensals could persist in the airway. It used three lines of evidence: patient prevalence and transcriptional activity, pangenome isolation sources, and literature context. The evidence is indirect. Engraftability is inferred from patient data, and lung metadata are sparse. [src: cf_formulation_design] For the design context see [[concepts/multi-criterion-design-of-protective-microbiome-formulations]] and [[summaries/cf_formulation_design__REPORT]].

## Engraftability from patient metagenomes and metatranscriptomes

The report treats persistence in the patient airway as one of its formulation criteria, called engraftability. [src: cf_formulation_design] It used paired metagenomic (DNA abundance) and metatranscriptomic (RNA activity) data from 175 patient samples to find species that are both prevalent and metabolically active. [src: cf_formulation_design] 134 species were detected across the patient metagenomes. [src: cf_formulation_design] The score is prevalence × log(activity ratio). The activity ratio is metaRS CPM / metaG CPM, which captures transcriptional engagement per unit DNA. [src: cf_formulation_design]

Among inhibition-tested species, [[entities/neisseria-mucosa]] has the highest score (1.595), combining high prevalence with strong transcriptional activity. [src: cf_formulation_design] [[entities/rothia-dentocariosa]] (0.422) and [[entities/streptococcus-salivarius]] (0.172) are also above the median. [src: cf_formulation_design] Micrococcus luteus has zero engraftability because it was not detected in any patient metagenome. [src: cf_formulation_design] Patient metatranscriptomics also confirms commensal-specific PTS sugar transport expression in vivo. [src: discoveries]

Caveat: patient prevalence is a proxy, not a direct measure of colonization persistence after probiotic administration. [src: cf_formulation_design]

## Pangenome isolation sources

The report queried NCBI environmental metadata for all pangenome genomes in its five formulation species to assess lung association. [src: cf_formulation_design] See [[entities/ncbi-env-environmental-metadata]] and [[entities/kbase-ke-pangenome]]. It identified 21 lung/respiratory genomes. Rothia dentocariosa contributes 10 (38% of its species) and Neisseria mucosa contributes 5 (33%). [src: cf_formulation_design] Both are described as naturally lung-adapted, with 33–38% respiratory genomes in the pangenome. [src: cf_formulation_design] The report calls them disproportionately lung-associated, natural respiratory organisms rather than repurposed gut commensals. [src: cf_formulation_design] The cross-project digest reports the same 38% and 33% figures for the KBase Data Lakehouse pangenome. [src: discoveries]

| Species | Best inhibition | Engraftability | Pangenome genomes | Lung genomes |
|---|---|---|---|---|
| Neisseria mucosa | 88% | 1.595 | 15 (8 in PROTECT clade) | 5 (33%) [src: cf_formulation_design] |
| Streptococcus salivarius | 98% | 0.172 | 153 | 5 (4%) [src: cf_formulation_design] |
| Rothia dentocariosa | 79% | 0.422 | 29 | 10 (38%) [src: cf_formulation_design] |

The 8-genome Neisseria mucosa clade contains 1 respiratory genome. [src: cf_formulation_design] Lung-adapted S. salivarius genomes show L-malate enrichment (+0.39 score) and sorbitol depletion (−0.82). The report suggests this reflects metabolic adaptation to the airway carbon landscape. [src: cf_formulation_design]

Caveat: only 21 lung genomes across 5 species limit this comparison. [src: cf_formulation_design]

## Consequences for the formulation

Rothia dentocariosa and Neisseria mucosa anchor the FDA-safe formulation, because of their highest inhibition, highest engraftability and lung tropism. [src: discoveries] Their combined engraftability (0.820) is nearly 6× higher than the k=3 formulation's 0.140. [src: cf_formulation_design]

Micrococcus luteus has 0 lung genomes and is primarily skin/environmental. [src: cf_formulation_design] The report suggests it may face engraftment challenges despite its metabolic contribution. [src: cf_formulation_design] This creates a design tension: the species most important for metabolic coverage is the least likely to persist in the lung. [src: cf_formulation_design]

## Literature context

The report cites Rigauts et al. (2022) on Rothia mucilaginosa enrichment in healthy airways. [src: cf_formulation_design] S. salivarius BLIS K12 has established respiratory probiotic credentials. [src: cf_formulation_design] Weyand (2017) reviewed upper respiratory Neisseria colonization models and noted N. mucosa's prevalence in oral tissue. [src: cf_formulation_design] The report treats N. mucosa engraftment as an assumption, with this literature as ecological context. [src: cf_formulation_design]

## Open Directions

- Measure persistence directly, for example by sampling patients after a probiotic trial. This would test whether the prevalence-based score predicts colonization.
- Add respiratory isolation-source metadata for more genomes. This would test whether the 33–38% lung fractions hold beyond 21 lung genomes.
- Test whether the 8-genome Neisseria mucosa clade, with 1 respiratory genome, differs in airway fitness from the other genomes of the species.
- Look for engraftment-supporting strategies or substitutes for Micrococcus luteus. This would address the coverage-versus-persistence tension.
