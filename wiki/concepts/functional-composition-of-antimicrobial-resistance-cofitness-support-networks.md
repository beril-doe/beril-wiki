---
type: "Concept"
description: "Which functional categories (flagella, amino acid biosynthesis, transport, signaling) populate the cofitness partners of AMR genes across organisms, and how network size relates to mechanism and fitness cost; stops at interpretation of causes."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md"]
---
# Functional composition of antimicrobial-resistance cofitness support networks

This page covers the functional composition of antimicrobial-resistance cofitness support networks. Enrichment of flagellar motility and amino acid biosynthesis in the networks of 801 AMR genes across 28 organisms is statistically supported. [src: discoveries, amr_cofitness_networks] No mechanism-specific enrichment survives correction, and network size does not track fitness cost. [src: amr_cofitness_networks] The evidence is one analysis, amr_cofitness_networks, repeated in the discoveries digest. See [[summaries/amr_cofitness_networks__REPORT]].

## Network size and coverage

Of 801 AMR genes with fitness data, 769 (96%) have at least one extra-operon cofitness partner at |r| > 0.3. [src: amr_cofitness_networks] Mean support-network size is 233 genes at |r|>0.3, 110 at |r|>0.4 and 71 at |r|>0.5. [src: amr_cofitness_networks] The report cautions that the |r| > 0.3 networks include many weak associations and need confirmation at |r| > 0.4. [src: amr_cofitness_networks]

## Enriched functions

Flagellar and amino acid biosynthesis GO terms are enriched in AMR support networks, as the list shows. [src: amr_cofitness_networks] Each count is the number of organisms significant at false discovery rate (FDR) < 0.05, with the mean odds ratio (OR).

- GO:0071973 flagellum-dependent cell motility: 5 organisms, mean OR 4.7. [src: amr_cofitness_networks]
- GO:0044780 flagellum assembly: 5 organisms, mean OR 5.3. [src: amr_cofitness_networks]
- GO:0009288 bacterial-type flagellum: 4 organisms, mean OR 4.9. [src: amr_cofitness_networks]
- GO:0071978 flagellum-dependent swarming: 4 organisms, mean OR 5.0. [src: amr_cofitness_networks]
- GO:0000105 histidine biosynthesis: 3 organisms, mean OR 5.3. [src: amr_cofitness_networks]
- GO:0000162 tryptophan biosynthesis: 3 organisms, mean OR 5.3. [src: amr_cofitness_networks]

The discoveries digest reports the same flagellar and biosynthesis enrichments. [src: discoveries] This enrichment is undetectable with old FB SEED annotations (0/280 significant). Only InterProScan GO (68% coverage) reveals it. [src: discoveries] See [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]] and [[entities/seed-subsystems]]. A permutation test on the old SEED annotations gave 23 significant tests of 250, with membrane/cell wall on top (24%, fold 1.12). [src: amr_cofitness_networks]

## Conserved core and tiers

Some functions appear in nearly every organism's network. The conserved core across mechanisms includes transmembrane transport (87–100% of organisms), signal transduction (87–100%), transcription regulation (96–100%) and phosphorelay signaling (91–100%). [src: amr_cofitness_networks] Flagellar motility (53–61%) forms a second tier of conservation. [src: amr_cofitness_networks] Amino acid biosynthesis (30–73%) forms the same tier. [src: amr_cofitness_networks] Broad terms such as transmembrane transport and membrane appear in nearly all networks and all genomes, so they may mask more specific signals. [src: amr_cofitness_networks] See [[entities/flagellar-motility-genes]] and [[entities/histidine-and-tryptophan-biosynthesis]].

## Mechanism

Efflux genes show the strongest amino acid biosynthesis enrichment, with histidine in 6 organisms and tryptophan in 5. [src: amr_cofitness_networks] Metal resistance genes show stronger chemotaxis enrichment, in 4 organisms. [src: amr_cofitness_networks] The mechanism-specific GO analysis gave 212 significant tests of 9,244 at FDR<0.05, with efflux histidine biosynthesis (6 organisms) on top. [src: amr_cofitness_networks] However, no GO term is significantly mechanism-specific after FDR correction. [src: amr_cofitness_networks] Histidine biosynthesis is the only hint: efflux 68% vs metal 30%, p = 0.013 uncorrected, q = 0.18 after FDR. [src: amr_cofitness_networks] See [[entities/efflux-pumps]] and [[entities/metal-resistance-genes]].

## Network size and fitness cost

Network size does not correlate with AMR gene fitness cost (Spearman rho = −0.006, p = 0.87, N = 769). [src: amr_cofitness_networks] This holds within each mechanism (efflux rho = −0.049, enzymatic rho = +0.038, metal rho = −0.031; all p > 0.4). [src: amr_cofitness_networks] The size of the co-regulatory neighborhood does not explain the uniform cost of resistance (+0.086 from amr_fitness_cost). [src: amr_cofitness_networks] The report notes that the missing correlation may reflect insufficient variance in fitness cost across genes. [src: amr_cofitness_networks] See [[entities/antimicrobial-resistance-gene-catalog-amr-fitness-cost]].

## Interpretation and limits

The report describes this as the first pan-bacterial mapping of AMR co-fitness neighborhoods across 28 organisms. [src: amr_cofitness_networks] It cautions that the flagellar and biosynthesis enrichment may reflect shared dispensability under lab conditions rather than mechanistic co-regulation. [src: amr_cofitness_networks] See [[concepts/shared-dispensability-as-a-confound-in-cofitness-enrichment]]. The 28 organisms are lab-adapted, biased toward Pseudomonas and limited in ecological diversity. [src: amr_cofitness_networks] As a hypothesis, the digest suggests that co-regulation with motility and biosynthesis means AMR costs reflect competition for the proton motive force. [src: discoveries] See [[entities/proton-motive-force]].

## Open Directions

- Repeat the enrichment at |r| > 0.4 and 0.5, where networks are smaller, to test whether the flagellar and biosynthesis signals survive removal of weak associations.
- Compare AMR partners with non-AMR genes matched for dispensability, to separate shared lab dispensability from co-regulation.
- Test histidine-biosynthesis specificity for efflux genes in more organisms, since the q = 0.18 result is not significant.
- Add organisms from varied ecologies, and non-Pseudomonas lineages, to check whether the pattern generalizes.
- Measure proton motive force directly in motility and biosynthesis mutants, to test the competition hypothesis.
