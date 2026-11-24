---
type: "Concept"
description: "Whether functional enrichment in cofitness neighborhoods reflects genuine co-regulation or shared laboratory dispensability of genes, and the permutation tests that would separate them; stops at AMR-specific mechanism comparisons."
sources: ["summaries/amr_cofitness_networks__REPORT.md"]
---
# Shared dispensability as a confound in cofitness enrichment

Functional enrichment in cofitness neighborhoods may reflect genes that are all dispensable in laboratory conditions, not genuine co-regulation. The evidence comes from one report, [[summaries/amr_cofitness_networks__REPORT]], on antimicrobial resistance (AMR) genes. It raises the confound and proposes tests, but it has not run them. [src: amr_cofitness_networks]

## The confound

AMR cofitness neighborhoods are enriched for flagellar motility and amino acid biosynthesis. The report cautions that shared dispensability under laboratory conditions may explain this, and it calls the point a key caveat for all cofitness-based functional inference. [src: amr_cofitness_networks] The report offers two readings of the enrichment in AMR support networks. [src: amr_cofitness_networks] (See also [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]] and [[entities/cofitness-analysis]].)

- **Interpretation A, co-regulation.** AMR genes sit in regulatory programs that co-control resistance, motility and biosynthesis. Shared transcription factors or signaling cascades would then produce condition-specific cofitness. [src: amr_cofitness_networks]
- **Interpretation B, shared dispensability.** AMR, flagellar and biosynthetic genes are all metabolic burdens under standard laboratory conditions. Their knockouts give modestly positive fitness across most experiments. [src: amr_cofitness_networks] The cofitness signal would then reflect membership in a "dispensable under lab conditions" class, not a mechanistic connection. [src: amr_cofitness_networks]

The report says nearly all [[entities/fitness-browser]] experiments use shaken liquid culture, where flagella are useless because there is no surface to swim on and no gradient to follow. [src: amr_cofitness_networks] It says most use rich or defined media with amino acid supplements, where biosynthesis is redundant. [src: amr_cofitness_networks] It describes AMR genes (no antibiotics present), flagellar genes (shaken liquid culture) and amino acid biosynthesis genes (supplemented media) as metabolic burdens under these conditions. [src: amr_cofitness_networks]

The report argues that the enriched categories are the ones that would be dispensable in shaken flask culture. [src: amr_cofitness_networks] Energy metabolism was not enriched: 0/25 organisms, fold 0.91 from the permutation test. The report attributes this to energy metabolism being useful in laboratory conditions. [src: amr_cofitness_networks]

## Why the existing permutation does not settle it

The AMR permutation test matched random genes by conservation class but not by mean fitness level. [src: amr_cofitness_networks] The report suggests the flagellar enrichment might disappear if random genes were drawn from the same slightly positive fitness distribution as AMR genes. [src: amr_cofitness_networks]

Pearson r subtracts each gene's mean fitness, so uniformly slightly positive genes alone would show zero correlation. [src: amr_cofitness_networks] Even so, dispensable genes may share condition-responsive patterns without being co-regulated. For example, both may be more dispensable in nutrient-rich conditions and less dispensable under starvation. [src: amr_cofitness_networks]

The report adds that even without this confound, high cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation. [src: amr_cofitness_networks] It also notes that a proposed [[entities/proton-motive-force]] competition model would explain efflux–flagellar cofitness, but shared dispensability could produce the same signal. [src: amr_cofitness_networks]

The report generalizes the concern. Genes that are dispensable under experimental conditions may show artifactual co-regulation in any cofitness study of laboratory-grown organisms. [src: amr_cofitness_networks]

## Tests the report proposes

The report names a fitness-matched permutation as the key unresolved test. [src: amr_cofitness_networks] It would draw random non-AMR genes matched on mean fitness level, with mean fitness between −0.05 and +0.05. [src: amr_cofitness_networks]

- If random slightly positive genes also show flagellar enrichment in their cofitness neighborhoods, shared dispensability is correct. [src: amr_cofitness_networks]
- If AMR genes uniquely enrich for flagella among fitness-matched genes, co-regulation is supported. [src: amr_cofitness_networks]

The report proposes three further checks.

- Compute cofitness separately for antibiotic conditions and standard growth. If AMR–flagella cofitness is specifically elevated under antibiotic stress, it would support a regulatory connection. [src: amr_cofitness_networks]
- Check whether flagellar knockouts show positive mean fitness across Fitness Browser experiments. If so, shared dispensability is plausible. If they are near zero or negative, co-regulation is strengthened. [src: amr_cofitness_networks]
- Test phage defense, secondary metabolite and other condition-specific gene classes for AMR-like cofitness. If they match, the signal is general to laboratory-dispensable genes and not AMR-specific. [src: amr_cofitness_networks]

## Open Directions

- Run the mean-fitness-matched permutation (−0.05 to +0.05) on the AMR support networks. This closes the gap left by matching on conservation class only.
- Split cofitness by antibiotic and standard-growth experiments. This tests whether AMR–flagella cofitness depends on the condition.
- Tabulate flagellar knockout mean fitness across Fitness Browser experiments. This checks the premise of the dispensability reading.
- Apply the same cofitness and permutation analysis to other condition-specific gene classes. This tests whether the signal is specific to AMR.
