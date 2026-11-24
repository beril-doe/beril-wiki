---
type: "Method"
description: "Sequence-profile-based domain annotation (Pfam, Gene3D, SUPERFAMILY, PANTHER) used to count domain hits per gene cluster."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
aliases: ["IPR domain hits", "InterProScan", "interproscan_domains"]
---
# InterProScan domain annotation

InterProScan domain annotation, also called IPR domain hits or interproscan_domains, is the topic of this page. Domain annotation uses sequence profiles, not structural homology. [src: alphafold_msa_annotation] The profiles come from Pfam, Gene3D, SUPERFAMILY and PANTHER. [src: alphafold_msa_annotation] Two projects used it: one counted hits per gene cluster [src: alphafold_msa_annotation], and one used it to recover markers that bakta missed. [src: plant_microbiome_ecotypes]

## Key facts

- The alphafold_msa_annotation report used the `kbase_ke_pangenome` tables `gene_cluster`, `bakta_annotations` and `interproscan_domains` for cluster classification, annotation quality, a UniRef100 bridge and domain hits. [src: alphafold_msa_annotation] See [[entities/kbase-ke-pangenome]].
- A notebook, NB02_domain_annotation.ipynb, used Spark to count InterProScan domain hits per gene cluster. [src: alphafold_msa_annotation]
- The plant microbiome report used `interproscan_domains`, `interproscan_go` and `interproscan_pathways` for domain hits, Gene Ontology (GO) terms and MetaCyc pathways in its novel ortholog group (OG) annotation, Phase 2. [src: plant_microbiome_ecotypes]

## Coverage in bacterial gene clusters

In the bacterial dataset, 111,035,431 gene clusters (83.8% of all clusters) have at least one domain annotation. [src: alphafold_msa_annotation] For clusters with annotation, mean hits = 7.5 and mean distinct IPR families = 3.3. [src: alphafold_msa_annotation]

The report compares this with the AlphaFold bridge coverage of 29.3%. It reads the higher domain coverage as showing that sequence-profile annotation reaches further into sequence space than structural homology. [src: alphafold_msa_annotation] It also explains the link to multiple sequence alignment (MSA) depth: MSA depth reflects detectable evolutionary relatives in sequence databases. Those relatives are the proteins whose characterisation generated the profiles in Pfam, Gene3D, SUPERFAMILY and PANTHER. [src: alphafold_msa_annotation] See [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes]] and [[summaries/alphafold_msa_annotation__REPORT]].

## Use as a check on bakta Pfam annotation

In the plant microbiome project, an audit compared InterProScan with [[entities/bakta-pfam-domains]]. See [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

- 12 of the 22 marker Pfams were completely absent from `bakta_pfam_domains`, although they were abundant in `interproscan_domains`. [src: plant_microbiome_ecotypes]
- The 10 marker Pfams present in bakta returned only 10–35% of the InterProScan hit count. They are undercounted but not absent. [src: plant_microbiome_ecotypes]
- InterProScan found 280,193 marker domain hits across 24,595 species. [src: plant_microbiome_ecotypes]
- It recovered 2,804 additional species with cell wall degrading enzyme (CWDE) cellulase/pectinase domains PF00150 and PF00544 that the Phase 1 bakta-only search missed. [src: plant_microbiome_ecotypes]

The report states that its biological claims are unaffected. Its NB10 refined cohort pipeline already used the `signature_acc` field of `interproscan_domains` for type III, IV and VI secretion system (T3SS, T4SS, T6SS) and CWDE markers. The report therefore treats the 280,193-hit recovery as correct and the refined cohort assignments as unaffected. [src: plant_microbiome_ecotypes] Separately, the Pfam LIKE recovery in NB13 Cell 3 confirmed the InterProScan secretion-system Pfam numbers and did not expand them. [src: plant_microbiome_ecotypes] See [[summaries/plant_microbiome_ecotypes__REPORT]].
