---
type: "Gene_Or_Pathway"
description: "AMR mechanism class including beta-lactamases, the most evenly distributed across environments."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md"]
aliases: ["beta-lactamases", "bla"]
---
# Enzymatic inactivation of antibiotics

Enzymatic inactivation is an antimicrobial resistance (AMR) mechanism class that includes beta-lactamases (gene family bla). Across three reports it is the most evenly spread mechanism among environments, but its conservation differs by gene group. [src: amr_environmental_resistome, amr_pangenome_atlas, amr_fitness_cost]

## Key facts

- The assembled resistome includes 26,220 enzymatic-inactivation gene clusters. [src: amr_environmental_resistome]
- The environmental resistome report describes it as the most uniformly distributed mechanism, present in all environments but dominant in none. [src: amr_environmental_resistome]
- bla is among the top bacterial AMR gene families, with 6,115 hits. [src: amr_pangenome_atlas]

## Distribution across environments

Species-level fractions run from 24.1% in human gut to 44.1% in host-associated species. [src: amr_environmental_resistome] The values are 28.2% clinical, 24.1% human gut, 44.1% host-associated, 34.3% soil, 41.2% aquatic and 33.6% other environmental. [src: amr_environmental_resistome] The difference between environments is statistically detectable but small (Kruskal-Wallis H=266.0, p=2.0×10⁻⁵⁵, η²=0.019). [src: amr_environmental_resistome] See [[concepts/environment-dependent-resistance-mechanism-composition]] and [[entities/kruskal-wallis-test-with-eta-squared-effect-size]].

## Conservation: core versus accessory

- In the AMR atlas census, enzymatic inactivation accounts for 15,755 hits (19.0%), of which 28.2% are core. [src: amr_pangenome_atlas]
- Beta-lactamases alone account for 12,824 hits (15.4%), of which 54.9% are core. The report calls them intrinsic resistance in the chromosomal backbone (enrichment p=7.7e-74 versus baseline). [src: amr_pangenome_atlas]
- Known mobile elements such as blaTEM, tet(C) and ant(2'')-Ia are 0% core. [src: amr_pangenome_atlas]
- In the fitness-cost report's conservation analysis, enzymatic inactivation genes are 16% accessory, so overwhelmingly core. [src: amr_fitness_cost]

See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

## Fitness behaviour

Beta-lactamases in the FB cross-reference are nearly neutral, with median fitness -0.001. [src: amr_pangenome_atlas] Narrow-spectrum enzymatic inactivation genes flip fitness only under their matching antibiotic. [src: amr_fitness_cost] Beta-lactam genes show a 50% flip rate among 105 pairs across 10 organisms. The report considers this consistent with many tests using non-carbenicillin beta-lactams. [src: amr_fitness_cost] The report proposes that many FB AMR genes are acquired determinants such as beta-lactamases, which would explain the modest transposon-based cost estimate. [src: amr_fitness_cost] See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]] and [[concepts/antibiotic-dependent-fitness-flip-of-resistance-genes]].

## Sources

[[summaries/amr_environmental_resistome__REPORT]], [[summaries/amr_fitness_cost__REPORT]], [[summaries/amr_pangenome_atlas__REPORT]].
