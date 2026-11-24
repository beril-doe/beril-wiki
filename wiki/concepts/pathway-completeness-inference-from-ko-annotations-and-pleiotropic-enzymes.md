---
type: "Concept"
description: "How reliably a biosynthetic pathway can be called from eggNOG/KEGG KO annotations, including pleiotropic precursor enzymes, missing regulators and failed domain-class assignment."
sources: ["summaries/phb_granule_ecology__REPORT.md"]
---
# Pathway completeness inference from KO annotations and pleiotropic enzymes

This page covers how reliably a biosynthetic pathway can be called from eggNOG/KEGG KO annotations. KO means KEGG ortholog. In the polyhydroxybutyrate (PHB) case study, five of the six KOs were detected, and the regulator phaR never was. [src: phb_granule_ecology] The precursor enzymes inflate partial-pathway counts, and the synthase class assignment failed. [src: phb_granule_ecology] All evidence comes from one report, [[summaries/phb_granule_ecology__REPORT]], which used [[entities/eggnog-orthologous-groups]] annotations. See also [[concepts/annotation-based-gene-detection-limits-in-pangenome-trait-surveys]] and [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

## Literature Context

The candidate evidence for this page is thin: a single genomics paper, and only its abstract was available. That paper sequenced-genome study of 11 type strains in the family Planctomycetaceae. It annotated the genomes against the Clusters of Orthologous Groups database. It then predicted and reconstructed core and pan metabolic pathways using the KEGG (Kyoto Encyclopedia of Genes and Genomes) orthology system [PMID 24489782](https://pubmed.ncbi.nlm.nih.gov/24489782/). The study also built a phylogeny from 832 common protein families and examined genomic islands, structural variations and plasmid integration [PMID 24489782](https://pubmed.ncbi.nlm.nih.gov/24489782/). The abstract shows that calling metabolic pathways from KO assignments is an established way to describe the capabilities of a group of genomes. It gives no figures on how accurate those calls are, and it does not mention pleiotropic enzymes, missing regulators or failed domain-class assignment.

The corpus's polyhydroxybutyrate (PHB) case study uses the same general approach. It assigns KOs to pangenome gene clusters and infers pathway presence from them. This is consistent with the practice in [PMID 24489782](https://pubmed.ncbi.nlm.nih.gov/24489782/). The study there covered only 11 genomes, whereas the corpus's query covered 19,496 species. The corpus's central findings are not addressed by the candidate paper, so they are novel relative to this evidence base rather than confirmed or contradicted by it. These findings are:

- The regulator phaR (K18080) had 0 detected clusters.
- The precursors-only class (phaA/phaB without phaC) probably overestimates partial PHB capability, because those enzymes act in general metabolism.
- All 11,792 phaC clusters were assigned to "other_pfam" because eggNOG reports domain names rather than Pfam accession IDs.

These are reported by one project, and the candidate paper neither supports nor weakens them.

The literature retrieved here therefore gives only background support for the method. The hub's caution about pathway inference rests on the corpus's own observations. Testing it against other work would need papers that benchmark KO-based pathway completeness, or that examine annotation of shared enzymes such as beta-ketothiolases. See also [[concepts/annotation-based-gene-detection-limits-in-pangenome-trait-surveys]] and [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

## What the annotations detected

Querying the KBase Data Lakehouse pangenome eggNOG annotations for six PHB pathway KOs identified 118,513 gene clusters across 19,496 species. [src: phb_granule_ecology] Five of the six KOs were detected, as the table shows. [src: phb_granule_ecology]

| Gene | KO | Role | Clusters | Species |
|---|---|---|---|---|
| phaA | K00626 | beta-ketothiolase (pleiotropic) | 86,318 | 17,969 [src: phb_granule_ecology] |
| phaB | K00023 | acetoacetyl-CoA reductase (pleiotropic) | 9,617 | 6,977 [src: phb_granule_ecology] |
| phaC | K03821 | PHA synthase, committed step | 11,792 | 6,067 [src: phb_granule_ecology] |
| phaP | K14205 | phasin granule protein | 6,130 | 4,571 [src: phb_granule_ecology] |
| phaZ | K05973 | PHB depolymerase | 4,656 | 3,151 [src: phb_granule_ecology] |

PHA is polyhydroxyalkanoate. The regulator phaR (K18080) had 0 detected clusters and 0 species. [src: phb_granule_ecology] It was absent from all 27K species. The report suggests this reflects poor annotation coverage or misassignment of the gene. [src: phb_granule_ecology] The 5/6 detection rate suggests K18080 may be underrepresented in eggNOG annotations. [src: phb_granule_ecology]

## Pleiotropic precursors distort completeness calls

Species were classed by completeness. The counts were:

- complete (phaC plus phaA/phaB): 6,005 species [src: phb_granule_ecology]
- synthase-only: 62 species [src: phb_granule_ecology]
- precursors-only: 12,869 species [src: phb_granule_ecology]
- accessory-only: 555 species [src: phb_granule_ecology]
- absent: 8,199 species [src: phb_granule_ecology]

The precursors-only class is the largest partial class. The report attributes this to phaA and phaB acting in general fatty acid and thiolase metabolism beyond PHB synthesis. [src: phb_granule_ecology] The report states that phaA and phaB participate in general metabolism beyond PHB. [src: phb_granule_ecology] It says the precursors-only category, 46.5% of species, likely overestimates partial PHB capability. [src: phb_granule_ecology]

## Failed domain-class assignment

The PHA synthase class analysis assigned all 11,792 phaC clusters to "other_pfam". eggNOG supplies domain names (Abhydrolase_1, PhaC_N) rather than the Pfam accession IDs (PF00561, PF07167) that the classification code expected. [src: phb_granule_ecology] The report calls this a remaining limitation. [src: phb_granule_ecology] It proposes mapping PF00561 to Abhydrolase_1 for Class I/II and PF07167 to PhaC_N for Class III/IV. This would enable proper classification of the 11,792 phaC clusters. [src: phb_granule_ecology]

## Open Directions

- Re-run the class assignment after mapping Pfam accessions to eggNOG domain names. This would show whether Class I–IV can be recovered for the 11,792 phaC clusters.
- Search for phaR by sequence homology or domain in a sample of complete-pathway genomes. This would separate true absence from annotation failure for K18080.
- Test whether requiring phaC and excluding phaA/phaB-only calls changes downstream ecological associations. This would measure the effect of the precursors-only inflation.
- Examine the 62 synthase-only species for missing precursor annotations. This would show whether they are real exceptions or gaps.
