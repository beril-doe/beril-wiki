---
type: "Gene_Or_Pathway"
description: "Bacterial flagellar motility and assembly functions enriched in AMR networks"
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md"]
---
# Bacterial flagellar motility and assembly

## What this is

**Canonical name:** Bacterial flagellar motility and assembly. [src: amr_cofitness_networks]

**Known aliases:** flagellum-dependent cell motility; flagellum assembly; bacterial-type flagellum; flagellum-dependent swarming; flagellar motility. [src: amr_cofitness_networks]

**Stable external identifiers:** GO:0071973 (flagellum-dependent cell motility), GO:0044780 (flagellum assembly), GO:0009288 (bacterial-type flagellum), and GO:0071978 (flagellum-dependent swarming). [src: amr_cofitness_networks]

## Evidence from AMR cofitness networks

Flagellum-dependent cell motility was significantly enriched in AMR cofitness neighborhoods in 5 organisms, with a mean odds ratio of 4.7. [src: amr_cofitness_networks]

Flagellum assembly was significantly enriched in 5 organisms, with a mean odds ratio of 5.3. [src: amr_cofitness_networks]

Bacterial-type flagellum was significantly enriched in 4 organisms, with a mean odds ratio of 4.9. [src: amr_cofitness_networks]

Flagellum-dependent swarming was significantly enriched in 4 organisms, with a mean odds ratio of 5.0. [src: amr_cofitness_networks]

Across AMR mechanisms, flagellar motility occurred in 53–61% of organisms. [src: amr_cofitness_networks]

The enrichment supports the [[concepts/condition-specific-fitness]] interpretation that cofitness neighborhoods can reflect condition-specific shared dispensability rather than direct co-regulation. [src: amr_cofitness_networks]

The core-gene trade-off analysis **supports** this condition-specific interpretation: Motility genes showed a +7.8 percentage-point higher burden for core than non-core genes, indicating that conserved motility functions can be costly in laboratory conditions while remaining conditionally valuable. [src: core_gene_tradeoffs]

## Interpretation and limitations

The report does not establish that AMR genes directly regulate flagellar motility or assembly, because cofitness measures shared fitness phenotypes rather than direct transcriptional control. [src: amr_cofitness_networks]

Flagella and chemotaxis may be unnecessary in the shaken-liquid-culture conditions commonly used by the Fitness Browser, making shared laboratory dispensability a possible explanation for the enrichment. [src: amr_cofitness_networks]

The core-gene analysis **refines** this explanation by interpreting flagellar machinery as energetically expensive and potentially costly in laboratory conditions, yet conserved because motility can be essential for chemotaxis in natural environments; this remains an inference from laboratory fitness and conservation rather than direct measurement of natural selection. [src: core_gene_tradeoffs]

A key unresolved test is a fitness-matched permutation using random non-AMR genes with the same mean-fitness distribution, including the proposed −0.05 to +0.05 range. [src: amr_cofitness_networks]

The report also proposes directly assessing mean fitness for flagellar knockouts and testing cofitness separately under antibiotic and standard-growth conditions. [src: amr_cofitness_networks]

## Related pages

- [[summaries/amr_cofitness_networks__REPORT]] — source report on AMR cofitness support networks and flagellar enrichment.
- [[summaries/core_gene_tradeoffs__REPORT]] — source report on conservation-associated, condition-dependent fitness burden.
- [[concepts/condition-specific-fitness]] — frames shared dispensability as an alternative explanation for the enrichment.
- [[concepts/gene-essentiality]] — provides context for interpreting flagellar fitness phenotypes under laboratory conditions.
- [[entities/chemotaxis]] — related motility and signaling function included in the report's interpretation of enrichment.
