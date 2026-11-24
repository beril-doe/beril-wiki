---
type: "Concept"
description: "Joining gene-level fitness measurements to AlphaFold models through SwissProt best hits to ask whether fitness-impact genes carry structural signatures; stops at the structural analyses themselves."
sources: ["summaries/berdl_data_atlas__REPORT.md"]
---
# Structure–fitness integration of mutant fitness data with predicted protein structures

This page covers the joining of gene-level fitness measurements to AlphaFold models through SwissProt best hits, to ask whether fitness-impact genes carry structural signatures. The join was validated on the live KBase Data Lakehouse cluster. [src: berdl_data_atlas] The structural analyses themselves have not yet been run. The evidence comes from one report, [[summaries/berdl_data_atlas__REPORT]].

## The proposed question and bridge

The use case (UC1) uses the kescience ↔ refdata bridge, with 12 shared keys, to ask whether high-fitness-impact genes have structural signatures detectable in AlphaFold. [src: berdl_data_atlas] The report ranks this structure–phenotype bridge as the biggest untapped opportunity. It cites 99.5% join coverage and sample validation, and it calls the use case ready to scope as a standalone project. [src: berdl_data_atlas] It also presents the validated SwissProt-best-hit-to-AlphaFold path as the Lakehouse realization of the structure-function loop opened by Jumper et al. (2021). [src: berdl_data_atlas] It describes UC1 as the first sample-validated synergy use case, with a corrected executable join recipe and live-cluster coverage statistics. [src: berdl_data_atlas] The report proposes promoting UC1 into its own project, with the validated 55,454-gene cohort as the seed dataset. [src: berdl_data_atlas] See also [[concepts/untapped-cross-program-synergy-use-cases-for-environmental-and-clinical-microbiology]], [[entities/fitness-browser]] and [[entities/alphafold-protein-structure-database]].

## Live-cluster validation

The counts below come from the live-cluster validation. They show that almost every SwissProt-hit gene has an AlphaFold entry. [src: berdl_data_atlas]

- FitnessBrowser gene-fitness measurements: 27,410,721. [src: berdl_data_atlas]
- Genes with a SwissProt best hit: 79,180. [src: berdl_data_atlas]
- AlphaFold entries: 241,070,489. [src: berdl_data_atlas]
- SwissProt-best-hit coverage in AlphaFold: 99.5% (78,753 / 79,180). [src: berdl_data_atlas]
- Genes with both fitness data and an AlphaFold model: 55,454, covering 48 organisms and 22,303 distinct AF models. [src: berdl_data_atlas]

E. coli sample rows confirmed that the join is semantically valid. They were thrA → AF-P00561-F1, thrB → AF-P00547-F1, thrC → AF-P00934-F1 and talB → AF-Q3Z606-F1. [src: berdl_data_atlas] The validation was probed interactively in an on-cluster Spark Connect session. [src: berdl_data_atlas] For related identifier problems, see [[concepts/join-key-validity-and-identifier-format-mismatches]].

## Composition of the joined cohort

The joined cohort spans the full range of fitness effects. Genes were tested at an average of 121–187 conditions per gene. [src: berdl_data_atlas] The report describes the cohort as strongly enriched for essentiality signal and ready for downstream structure-function analysis. [src: berdl_data_atlas]

| Fitness class | Genes |
|---|---|
| Essential (min_fit ≤ −4) | 6,635 [src: berdl_data_atlas] |
| Strong defect | 8,271 [src: berdl_data_atlas] |
| Moderate | 10,950 [src: berdl_data_atlas] |
| Mild | 29,467 [src: berdl_data_atlas] |
| No defect | 131 [src: berdl_data_atlas] |

## Limits

The AlphaFold entries table, kescience_alphafold.alphafold_entries, has no per-residue pLDDT or structural-feature data. The report proposes either ingesting those features or computing them from PDB files as a derived Lakehouse collection. [src: berdl_data_atlas]

## Open Directions

- Compute per-residue pLDDT and structural features for the 22,303 distinct AF models, then add them as a derived collection. This closes the gap in the entries table.
- Compare structural features of essential genes (6,635) with those of mild-defect genes (29,467) in the 55,454-gene cohort. This is the first direct test of the UC1 question.
- Check whether results hold within single organisms across the 48, to separate organism effects from structural effects.
- Examine the SwissProt-hit genes without an AlphaFold entry to see whether they share a property that biases the cohort.
