---
type: "Finding"
description: "Core gene clusters had a median MSA depth of 15,308, versus 5,299 for auxiliary+singleton and 5,527 for auxiliary non-singleton clusters, and a 10th-percentile depth of 334 versus 25\u201332 for accessory genes."
finding_id: "alphafold_msa_annotation--f4d7e00d"
result: "observation"
source: "alphafold_msa_annotation"
quantities: [{"value": "15,308", "what": "median MSA depth of core clusters", "unit": "depth", "denominator": "", "scope": "core clusters"}, {"value": "5,299", "what": "median MSA depth, auxiliary+singleton", "unit": "depth", "denominator": "", "scope": "auxiliary+singleton clusters"}, {"value": "5,527", "what": "median MSA depth, auxiliary non-singleton", "unit": "depth", "denominator": "", "scope": "auxiliary non-singleton clusters"}, {"value": "334", "what": "10th-percentile MSA depth for core genes", "unit": "depth", "denominator": "", "scope": "core vs 25\u201332 for accessory"}]
caveat: "MSA depth was looked up for each cluster's representative sequence only, so within-cluster sequence diversity is ignored and the representative may differ from the typical member."
first_added: "2026-10-23"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# Core clusters have much deeper MSAs than accessory clusters

Core gene clusters had a median MSA depth of 15,308, versus 5,299 for auxiliary+singleton and 5,527 for auxiliary non-singleton clusters, and a 10th-percentile depth of 334 versus 25–32 for accessory genes. [src: alphafold_msa_annotation]

## Key figures

- **15,308 depth**: median MSA depth of core clusters (scope core clusters) [src: alphafold_msa_annotation]
- **5,299 depth**: median MSA depth, auxiliary+singleton (scope auxiliary+singleton clusters) [src: alphafold_msa_annotation]
- **5,527 depth**: median MSA depth, auxiliary non-singleton (scope auxiliary non-singleton clusters) [src: alphafold_msa_annotation]
- **334 depth**: 10th-percentile MSA depth for core genes (scope core vs 25–32 for accessory) [src: alphafold_msa_annotation]

## Evidence

> Core gene clusters have a median MSA depth of **15,308** — 2.89× higher than the auxiliary+singleton median of 5,299 and 2.77× higher than the auxiliary non-singleton median of 5,527. The separation is most pronounced at the low end: the 10th-percentile MSA depth is 334 for core genes vs. 25–32 for accessory genes. [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

MSA depth was looked up for each cluster's representative sequence only, so within-cluster sequence diversity is ignored and the representative may differ from the typical member. [src: alphafold_msa_annotation]

> 2. **Representative sequence bias**: MSA depth is looked up for the gene cluster's representative sequence only. Within-cluster sequence diversity is ignored; the representative may have a higher or lower MSA depth than the typical cluster member. [src: alphafold_msa_annotation]

## Other caveats in this report

- The report flags a tension between core clusters' low overall hypothetical rate and the 68.9% hypothetical rate in their MSA-depth-< 10 subset. [src: alphafold_msa_annotation]
- UniProt-linked coverage favors better-studied organisms; the report hypothesizes, rather than measures, a larger annotation gap in the unlinked 70.7%. [src: alphafold_msa_annotation]
- Here, core status means presence in a majority of genomes within a species clade, not universality across all bacteria. Purifying selection, biological importance, and unprecedented fold are interpretations of conservation and low MSA depth, not direct measurements. [src: alphafold_msa_annotation]
- Experimental structural characterization of paradox proteins is proposed, not reported as completed. [src: alphafold_msa_annotation]
- The report distinguishes an MSA-depth-associated gap from a pangenome-class-associated gap; horizontal transfer, rapid evolution, and narrow taxonomic distribution are offered as likely explanations rather than directly tested mechanisms. [src: alphafold_msa_annotation]
