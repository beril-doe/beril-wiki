---
type: "Finding"
description: "Across the reported core-cluster MSA-depth bins, mean domain hits rose from 0.59 at depth < 10 to 10.83 at depth \u2265 10,000, and mean distinct IPR values rose from 0.059 to 4.601."
finding_id: "alphafold_msa_annotation--3386d12a"
result: "observation"
source: "alphafold_msa_annotation"
quantities: [{"value": "0.59", "what": "mean domain hits per core cluster", "unit": "hits", "denominator": "415,733 core clusters", "scope": "MSA depth < 10"}, {"value": "10.83", "what": "mean domain hits per core cluster", "unit": "hits", "denominator": "15,993,075 core clusters", "scope": "MSA depth \u2265 10,000"}, {"value": "0.059", "what": "mean distinct IPR per core cluster", "unit": "distinct IPR", "denominator": "415,733 core clusters", "scope": "MSA depth < 10"}, {"value": "4.601", "what": "mean distinct IPR per core cluster", "unit": "distinct IPR", "denominator": "15,993,075 core clusters", "scope": "MSA depth \u2265 10,000"}]
caveat: "The 293K genomes are not phylogenetically balanced (Pseudomonas and E. coli are over-represented), so core gene counts and MSA depth distributions are influenced by this sampling."
first_added: "2026-10-23"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# Domain annotation richness rises steadily with MSA depth in core clusters

Across the reported core-cluster MSA-depth bins, mean domain hits rose from 0.59 at depth < 10 to 10.83 at depth ≥ 10,000, and mean distinct IPR values rose from 0.059 to 4.601. [src: alphafold_msa_annotation]

## Key figures

- **0.59 hits**: mean domain hits per core cluster (denominator 415,733 core clusters; scope MSA depth < 10) [src: alphafold_msa_annotation]
- **10.83 hits**: mean domain hits per core cluster (denominator 15,993,075 core clusters; scope MSA depth ≥ 10,000) [src: alphafold_msa_annotation]
- **0.059 distinct IPR**: mean distinct IPR per core cluster (denominator 415,733 core clusters; scope MSA depth < 10) [src: alphafold_msa_annotation]
- **4.601 distinct IPR**: mean distinct IPR per core cluster (denominator 15,993,075 core clusters; scope MSA depth ≥ 10,000) [src: alphafold_msa_annotation]

## Evidence

> | MSA depth bin | Core clusters | Mean domain hits | Mean distinct IPR | |---|---|---|---| | < 10 | 415,733 | 0.59 | 0.059 | | 10–99 | 1,143,785 | 0.96 | 0.242 | | 100–999 | 2,301,137 | 1.95 | 0.852 | | 1,000–4,999 | 3,126,558 | 3.72 | 1.843 | | 5,000–9,999 | 2,591,011 | 5.62 | 2.664 | | ≥ 10,000 | 15,993,075 | 10.83 | 4.601 | [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

The 293K genomes are not phylogenetically balanced (Pseudomonas and E. coli are over-represented), so core gene counts and MSA depth distributions are influenced by this sampling. [src: alphafold_msa_annotation]

> 3. **Taxonomic imbalance**: The 293K genomes are not phylogenetically balanced (common taxa like *Pseudomonas* and *E. coli* are over-represented). Core gene counts and MSA depth distributions are influenced by this sampling. [src: alphafold_msa_annotation]

## Other caveats in this report

- The report flags a tension between core clusters' low overall hypothetical rate and the 68.9% hypothetical rate in their MSA-depth-< 10 subset. [src: alphafold_msa_annotation]
- UniProt-linked coverage favors better-studied organisms; the report hypothesizes, rather than measures, a larger annotation gap in the unlinked 70.7%. [src: alphafold_msa_annotation]
- Here, core status means presence in a majority of genomes within a species clade, not universality across all bacteria. Purifying selection, biological importance, and unprecedented fold are interpretations of conservation and low MSA depth, not direct measurements. [src: alphafold_msa_annotation]
- Experimental structural characterization of paradox proteins is proposed, not reported as completed. [src: alphafold_msa_annotation]
- The report distinguishes an MSA-depth-associated gap from a pangenome-class-associated gap; horizontal transfer, rapid evolution, and narrow taxonomic distribution are offered as likely explanations rather than directly tested mechanisms. [src: alphafold_msa_annotation]
