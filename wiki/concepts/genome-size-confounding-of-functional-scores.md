---
type: "Concept"
description: "How genome size and annotation breadth can bias normalized functional scores"
sources: ["summaries/bacdive_metal_validation__REPORT.md"]
---
# Genome Size and Annotation Breadth Can Confound Normalized Functional Scores

A normalized functional score can remain associated with genome size and annotation breadth even when the score divides functional clusters by the total number of annotated clusters. [src: bacdive_metal_validation]

## Core Mechanism

The BacDive–GTDB analysis defined its metal-tolerance score as metal clusters divided by annotated clusters, thereby controlling for genome size but not necessarily eliminating relationships between metal-tolerance functions and total metabolic complexity. [src: bacdive_metal_validation] The denominator is therefore not a neutral measure of genome scale: differences in annotation breadth can alter both the apparent functional numerator and the reference set used for normalization. [src: bacdive_metal_validation]

This creates a potential confounding path in which organisms with larger genomes or more broadly annotated gene clusters receive different normalized functional scores because genome size, annotation coverage, and functional complexity are correlated. [src: bacdive_metal_validation] The report specifically identifies this mechanism as a possible explanation for unexpectedly elevated scores among host-associated isolates, rather than treating the host-associated result as evidence of causal metal adaptation. [src: bacdive_metal_validation]

## BacDive Evidence

Host-associated isolates had a metal-tolerance effect size of d=+0.14 with p<0.0001, while the contamination categories ranged from d=+0.43 to d=+1.00. [src: bacdive_metal_validation] The smaller host-associated effect therefore does not establish the same ecological interpretation as the stronger contamination-associated signals. [src: bacdive_metal_validation]

The report attributes the host-associated elevation as likely reflecting genome-size confounding because host-associated BacDive records were dominated by Pseudomonadota pathogens such as [[entities/pseudomonas]], [[entities/klebsiella]], and [[entities/acinetobacter-baumannii]], which have larger genomes and more KEGG-annotated gene clusters. [src: bacdive_metal_validation] Genome-size normalization reduced but did not eliminate this possible effect. [src: bacdive_metal_validation]

The contamination signal was not uniform across taxonomic groups: within [[entities/pseudomonadota]], contamination isolates had a metal-score delta of +0.040 relative to environmental isolates, with p<0.001 for n=85 contamination and n=5,655 environmental isolates; within [[entities/actinobacteria]], the delta was +0.035 with p<0.001 for n=62 and n=772, respectively. [src: bacdive_metal_validation] These comparisons support the possibility that the environmental signal persists beyond broad phylum composition in the two most-sampled phyla, but they do not by themselves remove genome-size or annotation-breadth confounding. [src: bacdive_metal_validation]

Within [[entities/bacillota-b]], the contamination delta was -0.012 with p=0.285 for n=19 contamination and n=492 environmental isolates, whereas within [[entities/bacteroidota]] it was -0.008 with p=0.456 for n=5 and n=156, respectively. [src: bacdive_metal_validation] These null results cannot distinguish biological differences from limited statistical power because contamination-isolate sample sizes were small. [src: bacdive_metal_validation]

## Interpretation for the [[concepts/environmental-resistome]]

The BacDive analysis provides ecological validation for the [[entities/metal-fitness-atlas]] score because heavy-metal contamination isolates had a median score of 0.240 and a mean score of 0.236, compared with an environmental-baseline median of 0.187 and mean of 0.195. [src: bacdive_metal_validation] The heavy-metal comparison had Cohen's d=+1.00, Mann–Whitney p=0.006, and n=10. [src: bacdive_metal_validation]

The broader contamination gradient was heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). [src: bacdive_metal_validation] Waste/sludge isolates had n=305 and d=+0.57, all-contamination isolates had n=176 and d=+0.43, and industrial isolates had n=796 and d=+0.20; each comparison had p<0.0001. [src: bacdive_metal_validation] These results support an ecological metal-adaptation signal, but they do not show that the signal is independent of genome size, annotation breadth, or correlated metabolic complexity. [src: bacdive_metal_validation]

The report proposes that species with larger core genomes encoding more metal-tolerance functions could score higher and be more likely to occur in contaminated environments. [src: bacdive_metal_validation] This is a hypothesis rather than a direct causal test, so normalized scores should be interpreted as associations that may combine metal adaptation with genome-scale and annotation-scale differences. [src: bacdive_metal_validation]

## Boundary of the Evidence

The heavy-metal estimate is imprecise because only n=10 matched isolates were available, and the observed d=1.00 barely exceeded the approximately d=0.93 minimum detectable effect size reported for 80% power with n=10 heavy-metal isolates versus approximately 5,000 environmental-baseline strains. [src: bacdive_metal_validation] The small sample makes it especially important to test whether the large effect persists after explicit adjustment for genome size, annotated-cluster count, taxonomy, and sampling source. [src: bacdive_metal_validation]

BacDive represents culturable, described strains rather than the full diversity of environmental bacteria, so culture-collection bias may affect both the distribution of genome sizes and the apparent prevalence of metal-tolerance functions. [src: bacdive_metal_validation] In addition, 55,107 of 97,334 BacDive strains, or 56.6%, were unmatched to a GTDB species, while 42,227 strains, or 43.4%, matched 6,426 GTDB species. [src: bacdive_metal_validation] This incomplete [[concepts/pangenome-integration]] bridge can change which genome-size and annotation-breadth classes enter the analysis. [src: bacdive_metal_validation]

## Relation to Score Design

Genome-size normalization is useful because it prevents raw counts of metal-tolerance clusters from simply tracking genome length. [src: bacdive_metal_validation] It is insufficient when the denominator, annotation process, or total functional complexity differs systematically among ecological groups. [src: bacdive_metal_validation]

A robust interpretation should therefore distinguish three quantities: the absolute number of metal-tolerance clusters, the total number of annotated clusters used as the denominator, and the residual association with isolation environment after accounting for genome size and annotation breadth. [src: bacdive_metal_validation] This framing refines the use of the [[entities/metal-fitness-atlas]] score from a standalone ecological proxy toward a quantity requiring covariate-aware validation. [src: bacdive_metal_validation]

The source report links this issue to [[concepts/genome-size-confounding-of-functional-scores]] and to the broader question of whether genome-derived functional predictions generalize across ecological contexts. [src: bacdive_metal_validation]

## Open Directions

- Match BacDive GCA accessions directly to [[entities/kbase-ke-pangenome]] genome identifiers, recover more of the 56.6% unmatched strains, and test whether matching failure is associated with genome size or isolation environment. [src: bacdive_metal_validation]
- Refit the BacDive environment comparisons with genome size, annotated-cluster count, taxonomic group, and culture-source category as covariates, and ask whether the contamination effect remains after separating numerator and denominator effects. [src: bacdive_metal_validation]
- Compare absolute metal-tolerance cluster counts with the normalized score across the same matched strains, and test whether ecological rankings change when annotation breadth is held constant. [src: bacdive_metal_validation]
- Integrate [[entities/enigma-coral]] community data from the Oak Ridge metal-contaminated site and test whether field abundance associations agree with genome-size-adjusted metal-tolerance predictions. [src: bacdive_metal_validation]
- Expand BacDive metal-phenotype extraction beyond the current metabolite-utilization records to include MIC and growth-inhibition data, then test whether measured phenotypes track normalized scores independently of genome and annotation breadth. [src: bacdive_metal_validation]
