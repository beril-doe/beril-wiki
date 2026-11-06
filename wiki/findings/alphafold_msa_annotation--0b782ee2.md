---
type: "Finding"
description: "EC and KEGG annotation were uncommon in the paradox-protein census, at 137 (0.033%) and 346 (0.083%) of clusters respectively."
finding_id: "alphafold_msa_annotation--0b782ee2"
result: "null result"
source: "alphafold_msa_annotation"
quantities: [{"value": "137 (0.033%)", "what": "EC-annotated paradox clusters", "unit": "clusters", "denominator": "", "scope": "paradox-protein census"}, {"value": "346 (0.083%)", "what": "KEGG-mapped paradox clusters", "unit": "clusters", "denominator": "", "scope": "paradox-protein census"}]
caveat: "The analysis excludes clusters without a non-UPI UniProt accession, and a larger annotation gap in the 71% without AlphaFold entries remains a hypothesis."
first_added: "2026-10-23"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# EC and KEGG annotation almost absent among low-depth core proteins

EC and KEGG annotation were uncommon in the paradox-protein census, at 137 (0.033%) and 346 (0.083%) of clusters respectively. [src: alphafold_msa_annotation]

## Key figures

- **137 (0.033%) clusters**: EC-annotated paradox clusters (scope paradox-protein census) [src: alphafold_msa_annotation]
- **346 (0.083%) clusters**: KEGG-mapped paradox clusters (scope paradox-protein census) [src: alphafold_msa_annotation]

## Evidence

> | EC-annotated | 137 (0.033%) | | KEGG-mapped | 346 (0.083%) | [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

The analysis excludes clusters without a non-UPI UniProt accession, and a larger annotation gap in the 71% without AlphaFold entries remains a hypothesis. [src: alphafold_msa_annotation]

> 1. **29.3% bridge coverage**: Only gene clusters with a non-UPI UniProt accession are included. The 71% without AlphaFold entries skews toward poorly characterised organisms and likely harbours a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation]

## Other caveats in this report

- The report flags a tension between core clusters' low overall hypothetical rate and the 68.9% hypothetical rate in their MSA-depth-< 10 subset. [src: alphafold_msa_annotation]
- UniProt-linked coverage favors better-studied organisms; the report hypothesizes, rather than measures, a larger annotation gap in the unlinked 70.7%. [src: alphafold_msa_annotation]
- Here, core status means presence in a majority of genomes within a species clade, not universality across all bacteria. Purifying selection, biological importance, and unprecedented fold are interpretations of conservation and low MSA depth, not direct measurements. [src: alphafold_msa_annotation]
- Experimental structural characterization of paradox proteins is proposed, not reported as completed. [src: alphafold_msa_annotation]
- The report distinguishes an MSA-depth-associated gap from a pangenome-class-associated gap; horizontal transfer, rapid evolution, and narrow taxonomic distribution are offered as likely explanations rather than directly tested mechanisms. [src: alphafold_msa_annotation]
