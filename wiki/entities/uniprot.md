---
type: "Dataset"
description: "Protein sequence dataset used for cross-dataset identification and annotation."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/berdl_data_atlas__REPORT.md"]
---
# UniProt

## What this entity is

**Canonical name:** UniProt. [src: alphafold_msa_annotation]

**Known aliases:** UniProt accession; the report also refers to UniRef100 and UniParc identifiers as related identifier types, not as aliases of UniProt. [src: alphafold_msa_annotation]

**Stable external identifier:** No stable external identifier was specified in this report. [src: alphafold_msa_annotation]

UniProt is the protein-sequence identifier source used to bridge [[entities/kbase-ke-pangenome]] gene clusters to AlphaFold MSA-depth records in [[entities/kescience-alphafold]]. [src: alphafold_msa_annotation] The annotation-gap study **refines** this role by using UniProt’s reviewed bacterial sequences as homology exemplars for candidate gene assignment. [src: annotation_gap_discovery] The BERDL Data Atlas inventories 215,130,942 UniProt proteins and recommends refdata UniProt alongside UniRef50, UniRef90, and UniRef100 as reference-protein resources. [src: berdl_data_atlas] This **supports** UniProt’s role as a large reference layer while **refining** the earlier accession-bridge view; across-tenant deduplication was not performed, so Refdata and KBase may contain the same UniProt entries through different cluster indices. [src: berdl_data_atlas]

## Evidence from alphafold_msa_annotation

The analysis joined `kbase_ke_pangenome`, Bakta annotations, [[entities/interproscan]] domain annotations, and [[entities/kescience-alphafold]] records. [src: alphafold_msa_annotation]

Of 132,531,501 total gene clusters, 38,804,903 (29.3%) had a real UniProt accession. [src: alphafold_msa_annotation]

A total of 38,051,842 gene cluster–UniProt pairs (28.7% of all gene clusters) bridged successfully to AlphaFold MSA depths. [src: alphafold_msa_annotation]

The remaining 70.7% lacked UniRef100 IDs or had UniParc-only identifiers without an AlphaFold entry. [src: alphafold_msa_annotation]

The analysed subset was biased toward better-studied organisms, so the report states that the annotation gap among the remaining 70.7% is likely larger, although that inference was not directly measured. [src: alphafold_msa_annotation]

Across the 38,051,842 gene cluster–UniProt pairs, MSA depth and domain-hit count had Spearman ρ = 0.7563. [src: alphafold_msa_annotation]

Mean domain hits increased from 0.59 for MSA depth < 10 to 10.83 for MSA depth ≥ 10,000, while mean distinct InterPro families increased from 0.059 to 4.601. [src: alphafold_msa_annotation]

Across all 132,531,501 gene clusters, 111,035,431 (83.8%) had at least one InterProScan domain annotation, exceeding the 29.3% AlphaFold bridge coverage. [src: alphafold_msa_annotation]

The report used a non-UPI UniProt accession as a requirement for AlphaFold MSA-depth lookup, which contributed to the limited bridge coverage. [src: alphafold_msa_annotation]

The UniProt-to-AlphaFold bridge was based on a static version-6 BERDL AlphaFold snapshot, and later UniProt deposits may change MSA depths. [src: alphafold_msa_annotation]

## Evidence from annotation_gap_discovery

The annotation-gap study **supports** UniProt’s role as a sequence-evidence resource: it retrieved 328 reviewed bacterial Swiss-Prot exemplar sequences through the UniProt REST API, covering 75/84 unique ECs, for DIAMOND homology searches. [src: annotation_gap_discovery] Those searches identified 154 hits and contributed to the final 96 resolved reaction-organism pairs, although the full pipeline—not UniProt homology alone—provided the evidence triangulation. [src: annotation_gap_discovery]

## Related pages

- [[summaries/alphafold_msa_annotation__REPORT]] — source summary describing UniProt accession bridging, AlphaFold MSA depth, and annotation coverage. [src: alphafold_msa_annotation]
- [[summaries/annotation_gap_discovery__REPORT]] — source summary describing UniProt/Swiss-Prot exemplar retrieval and homology-supported annotation-gap resolution. [src: annotation_gap_discovery]
- [[summaries/berdl_data_atlas__REPORT]] — atlas summary describing UniProt inventory scale, reference-data guidance, and cross-tenant deduplication caveats. [src: berdl_data_atlas]
- [[entities/kbase-ke-pangenome]] — gene-cluster dataset joined to UniProt identifiers. [src: alphafold_msa_annotation]
- [[entities/kescience-alphafold]] — AlphaFold dataset receiving the UniProt-linked MSA-depth lookups. [src: alphafold_msa_annotation]
- [[entities/interproscan]] — domain-annotation dataset compared with UniProt-linked MSA depth. [src: alphafold_msa_annotation]
- [[entities/swiss-prot]] — reviewed protein-sequence source used for annotation-gap homology exemplars. [src: annotation_gap_discovery]
- [[entities/diamond]] — protein-sequence homology method used with UniProt/Swiss-Prot exemplars. [src: annotation_gap_discovery]
- [[concepts/pangenome-integration]] — cross-project concept covering pangenome structure and annotation coverage.
