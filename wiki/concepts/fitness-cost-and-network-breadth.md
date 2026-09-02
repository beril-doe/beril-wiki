---
type: "Concept"
description: "Cofitness-network size is not a reliable predictor of AMR fitness cost."
sources: ["summaries/amr_cofitness_networks__REPORT.md"]
---
# Network Breadth Does Not Necessarily Predict Fitness Cost

The [[summaries/amr_cofitness_networks__REPORT]] reports that the breadth of an antimicrobial-resistance (AMR) gene’s cofitness support network did not predict its fitness cost across the analyzed organisms. [src: amr_cofitness_networks]

## Core Finding

Across 769 AMR genes with cofitness networks, support-network size was not correlated with AMR gene fitness cost: Spearman’s rho, a rank-based correlation coefficient, was −0.006 with p = 0.87. [src: amr_cofitness_networks] Within AMR mechanisms, the correlations were rho = −0.049 for efflux, rho = +0.038 for enzymatic resistance, and rho = −0.031 for metal resistance, with all p > 0.4. [src: amr_cofitness_networks]

The report also states that the uniform resistance cost was +0.086 and was not explained by co-regulatory-neighborhood size. [src: amr_cofitness_networks] This directly supports the conclusion that a broader measured support network does not necessarily impose a larger AMR fitness cost under the tested conditions. [src: amr_cofitness_networks]

## Interpretation

The null association should not be interpreted as evidence that network context is biologically irrelevant, because the analysis may have contained insufficient variance in fitness cost across genes to detect a relationship. [src: amr_cofitness_networks] The result therefore refines [[concepts/condition-specific-fitness]] by separating two properties that can be related in principle but were not related in this dataset: the number of genes sharing a fitness-profile pattern and the magnitude of the resistance-associated fitness phenotype. [src: amr_cofitness_networks]

Cofitness measures shared fitness phenotypes rather than direct transcriptional control, so a large network can reflect shared condition-dependent dispensability without implying a proportionally greater cost. [src: amr_cofitness_networks] In the report’s interpretation, AMR genes, flagellar genes, and biosynthetic genes may all appear connected because they are dispensable under some laboratory conditions, even when their network breadth does not determine their individual fitness cost. [src: amr_cofitness_networks]

This distinction connects the result to [[concepts/cofitness-versus-coregulation]] and [[concepts/cofitness-network-architecture]]: network breadth describes the extent of correlated fitness behavior, whereas fitness cost describes the phenotype associated with resistance. [src: amr_cofitness_networks]

## Evidence Boundaries

The analysis included 28 organisms with AMR genes, fitness matrices, and independent component analysis (ICA) fitness modules, and 769 of the 801 AMR genes with fitness data had at least one extra-operon cofitness partner at |r| > 0.3. [src: amr_cofitness_networks] At this threshold, the mean support network contained 233 genes, while the means at |r| > 0.4 and |r| > 0.5 were 110 and 71 genes, respectively. [src: amr_cofitness_networks]

These broad networks may include many weak associations, and the report identifies confirmation at |r| > 0.4 as necessary. [src: amr_cofitness_networks] Missing fitness values were treated as zero in z-score space through `np.nan_to_num`, which approximates but does not equal pairwise-complete Pearson correlation, although the report judged the dense Fitness Browser matrices unlikely to substantially alter the conclusions. [src: amr_cofitness_networks]

The absence of a network-size–cost relationship is therefore a direct null result within this dataset, not a general demonstration that network architecture can never influence fitness cost. [src: amr_cofitness_networks] The report further notes that the 28 organisms were lab-adapted, phylogenetically biased, included many Pseudomonas organisms, and had limited ecological diversity, restricting ecological generalization. [src: amr_cofitness_networks]

## Relation to Fitness-Matched Null Models

The proposed [[concepts/fitness-matched-null-models]] analysis is important because the enrichment signals in the same networks may arise from shared dispensability under laboratory conditions rather than direct co-regulation. [src: amr_cofitness_networks] The report specifically proposes drawing random non-AMR genes with the same mean-fitness distribution, including the −0.05 to +0.05 range, to test whether observed network structure exceeds what is expected from fitness level alone. [src: amr_cofitness_networks]

A fitness-matched null would not by itself establish a network-size effect on cost, but it would clarify whether network breadth contains information beyond the baseline dispensability of the genes being compared. [src: amr_cofitness_networks]

## Open Directions

- Recompute cofitness separately for antibiotic-treatment and standard-growth conditions, then test whether network breadth predicts fitness cost in either condition-specific matrix. [src: amr_cofitness_networks]
- Apply a fitness-matched permutation using random non-AMR genes with the same mean-fitness distribution, including the −0.05 to +0.05 range, and ask whether the observed network-size–cost correlation differs from the matched null. [src: amr_cofitness_networks]
- Repeat the network-size–cost analysis at |r| > 0.4 and |r| > 0.5, then test whether stricter support-network definitions produce a correlation that is absent at |r| > 0.3. [src: amr_cofitness_networks]
- Quantify the variance of AMR fitness costs and use a power analysis or hierarchical model to ask whether the null result could reflect insufficient variation across genes, mechanisms, or organisms. [src: amr_cofitness_networks]
- Compare cofitness network breadth with direct regulatory evidence and Pfam-domain enrichment to test whether broad networks reflect shared cofitness, co-regulation, or common functional architecture. [src: amr_cofitness_networks]
