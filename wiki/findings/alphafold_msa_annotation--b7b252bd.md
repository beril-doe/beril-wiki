---
type: "Finding"
description: "In the paradox-protein census of core gene clusters with MSA depth < 10 across 14,768 species clades, 415,603 distinct clusters had mean/median depth 4.57/4.0, of which 286,439 (68.9%) were hypothetical, 137 (0.033%) EC-annotated and 346 (0.083%) KEGG-mapped."
finding_id: "alphafold_msa_annotation--b7b252bd"
result: "observation"
source: "alphafold_msa_annotation"
quantities: [{"value": "415,603", "what": "distinct core clusters with msa_depth < 10", "unit": "clusters", "denominator": "", "scope": "14,768 species clades"}, {"value": "286,439 (68.9%)", "what": "hypothetical (no functional annotation) clusters", "unit": "clusters", "denominator": "415,603 distinct core clusters with msa_depth < 10", "scope": "paradox-protein census"}, {"value": "137 (0.033%)", "what": "EC-annotated clusters", "unit": "clusters", "denominator": "415,603 distinct core clusters with msa_depth < 10", "scope": "paradox-protein census"}, {"value": "346 (0.083%)", "what": "KEGG-mapped clusters", "unit": "clusters", "denominator": "415,603 distinct core clusters with msa_depth < 10", "scope": "paradox-protein census"}]
caveat: "Core means presence in a majority of genomes within a species clade, and purifying selection, importance and unprecedented fold are interpretations of conservation and low MSA depth, not direct measurements."
first_added: "2026-10-23"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# Low-depth core clusters are mostly hypothetical and rarely EC- or KEGG-annotated

In the paradox-protein census of core gene clusters with MSA depth < 10 across 14,768 species clades, 415,603 distinct clusters had mean/median depth 4.57/4.0, of which 286,439 (68.9%) were hypothetical, 137 (0.033%) EC-annotated and 346 (0.083%) KEGG-mapped. [src: alphafold_msa_annotation]

## Key figures

- **415,603 clusters**: distinct core clusters with msa_depth < 10 (scope 14,768 species clades) [src: alphafold_msa_annotation]
- **286,439 (68.9%) clusters**: hypothetical (no functional annotation) clusters (denominator 415,603 distinct core clusters with msa_depth < 10; scope paradox-protein census) [src: alphafold_msa_annotation]
- **137 (0.033%) clusters**: EC-annotated clusters (denominator 415,603 distinct core clusters with msa_depth < 10; scope paradox-protein census) [src: alphafold_msa_annotation]
- **346 (0.083%) clusters**: KEGG-mapped clusters (denominator 415,603 distinct core clusters with msa_depth < 10; scope paradox-protein census) [src: alphafold_msa_annotation]

## Evidence

> | Distinct core clusters with msa_depth < 10 | **415,603** | | Species clades represented | 14,768 | | Mean / median MSA depth | 4.57 / 4.0 | | Hypothetical (no functional annotation) | 286,439 (**68.9%**) | | EC-annotated | 137 (0.033%) | | KEGG-mapped | 346 (0.083%) | [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

Core means presence in a majority of genomes within a species clade, and purifying selection, importance and unprecedented fold are interpretations of conservation and low MSA depth, not direct measurements. [src: alphafold_msa_annotation]

> 1. **Conservation** (is_core = true): present in the majority of genomes within each of 14,768 species clades — implying strong purifying selection and likely important biological function. 2. **Structural novelty** (msa_depth < 10): fewer than 10 detectable homologs in the entire AlphaFold training set — meaning their fold is genuinely unprecedented in the available sequence databases. [src: alphafold_msa_annotation]

## Other caveats in this report

- The report flags a tension between core clusters' low overall hypothetical rate and the 68.9% hypothetical rate in their MSA-depth-< 10 subset. [src: alphafold_msa_annotation]
- UniProt-linked coverage favors better-studied organisms; the report hypothesizes, rather than measures, a larger annotation gap in the unlinked 70.7%. [src: alphafold_msa_annotation]
- Experimental structural characterization of paradox proteins is proposed, not reported as completed. [src: alphafold_msa_annotation]
- The report distinguishes an MSA-depth-associated gap from a pangenome-class-associated gap; horizontal transfer, rapid evolution, and narrow taxonomic distribution are offered as likely explanations rather than directly tested mechanisms. [src: alphafold_msa_annotation]
- MSA depth was assigned using each cluster's representative sequence; within-cluster sequence diversity was not assessed. [src: alphafold_msa_annotation]
