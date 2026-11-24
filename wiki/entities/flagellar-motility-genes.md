---
type: "Gene_Or_Pathway"
description: "Flagellum assembly and motility GO categories enriched in AMR support networks."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md"]
aliases: ["flagellum"]
---
# Flagellar motility genes

Flagellar motility genes (also called the flagellum) are the subject of this page. Flagellum assembly and motility GO categories are enriched in AMR support networks, and the evidence comes from one cofitness analysis. [src: discoveries] See [[summaries/amr_cofitness_networks__REPORT]] and [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]].

## Key facts

The analysis covered 801 AMR genes across 28 organisms. It found AMR cofitness neighborhoods enriched for flagellar motility (GO:0071973, 5 organisms FDR<0.05) and flagellum assembly (GO:0044780, 5 organisms). [src: discoveries]

Flagellar motility (53–61%) forms a second tier of AMR support-network conservation. [src: amr_cofitness_networks]

- GO:0071973, flagellum-dependent cell motility: 5 organisms, mean OR 4.7. [src: amr_cofitness_networks]
- GO:0044780, flagellum assembly: 5 organisms, mean OR 5.3. [src: amr_cofitness_networks]
- GO:0009288, bacterial-type flagellum: 4 organisms, mean OR 4.9. [src: amr_cofitness_networks]
- GO:0071978, flagellum-dependent swarming: 4 organisms, mean OR 5.0. [src: amr_cofitness_networks]

## Interpretation and caveats

The report favors shared dispensability as the explanation. Nearly all Fitness Browser (FB) experiments use shaken liquid culture, where it considers flagella useless because there is no surface to swim on and no chemical gradient to follow. [src: amr_cofitness_networks] It argues that the enriched categories are those that would be dispensable in shaken flask culture, including motility. [src: amr_cofitness_networks] See [[concepts/shared-dispensability-as-a-confound-in-cofitness-enrichment]] and [[entities/fitness-browser]].

The report notes a caveat. If random genes had been drawn with the same slightly-positive fitness distribution as AMR genes, the flagellar enrichment might disappear entirely. [src: amr_cofitness_networks]

An alternative is proton motive force (PMF) competition. It would explain why efflux genes correlate with flagellar genes, since both use PMF, but shared dispensability could produce the same signal. [src: amr_cofitness_networks] See [[entities/proton-motive-force]].

The report proposes checking flagellar knockout mean fitness across FB experiments. Positive fitness would support the plausibility of shared dispensability, and near-zero or negative fitness would strengthen the co-regulation interpretation. [src: amr_cofitness_networks]

## Open Directions

Test flagellar knockout mean fitness across FB experiments, as the report proposes, to separate shared dispensability from co-regulation. Also repeat the enrichment with random genes matched to the AMR fitness distribution to see whether it persists.
