---
type: "Gene_Or_Pathway"
description: "Hydrogen cyanide synthase subunit gene (hcnA–C operon) associated with biocontrol and rhizosphere niche."
sources: ["summaries/pgp_pangenome_ecology__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
aliases: ["hcnA", "hydrogen cyanide synthase"]
---
# hcnC

This page covers hcnC, a hydrogen cyanide synthase subunit gene of the hcnA–hcnC operon, linked to biocontrol and the rhizosphere niche. In the pgp_pangenome_ecology report it is enriched in soil and rhizosphere species. [src: pgp_pangenome_ecology] A separate plant-association analysis found the hydrogen cyanide marker not significant. [src: plant_microbiome_ecotypes]

## Key facts

- hcnC prevalence was 11.3% in soil/rhizosphere species versus 6.4% in other environments (Odds Ratio 1.85, q-value 6.1e-08). [src: pgp_pangenome_ecology]
- The report suggests the hcnA–hcnC operon is part of the rhizosphere niche toolkit. This is an interpretation, not a direct test. [src: pgp_pangenome_ecology]
- hcnA clusters were 78.5% core, 10.8% auxiliary, and 10.8% singleton (q vs baseline 9.2e-37). See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]]. [src: pgp_pangenome_ecology]

## Co-occurrence with other genes

hcnC co-occurs with pqqC (odds ratio, OR = 1.91). [src: pgp_pangenome_ecology] The report describes pqqC as co-occurring with hcnC and ipdC, forming a coherent "rhizosphere effectiveness" module. [src: pgp_pangenome_ecology] See [[entities/pyrroloquinoline-quinone-biosynthesis]] and [[concepts/co-occurrence-of-plant-growth-promoting-genes-and-trait-guilds]].

The nitrogen-fixation marker nifH was negatively associated with hcnC (OR = 0.23, q = 5.8e-29). [src: pgp_pangenome_ecology] See bacterial nitrogen fixation nif genes.

## A null result in a different analysis

In the plant-association cluster-robust generalized linear model (GLM), hydrogen_cyanide was not significant (coef −0.04, OR 0.96, 95% confidence interval [0.52, 1.76], Benjamini-Hochberg false discovery rate q 0.96). [src: plant_microbiome_ecotypes] This is a different marker and analysis from the soil/rhizosphere prevalence enrichment, and the claims do not state that one limits the other. See [[summaries/plant_microbiome_ecotypes__REPORT]] and [[summaries/pgp_pangenome_ecology__REPORT]].

The pangenome report states that a focused study of hcnA-C phylogeny and co-occurrence with biocontrol phenotypes would be valuable. [src: pgp_pangenome_ecology]

## Open Directions

- Run the proposed hcnA-C phylogeny and biocontrol-phenotype study to test the biocontrol link.
- Compare the soil enrichment with the plant-association null result on the same species set. This would test whether the two analyses really disagree. See [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere]].
