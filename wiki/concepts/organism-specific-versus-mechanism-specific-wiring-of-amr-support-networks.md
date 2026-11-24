---
type: "Concept"
description: "Whether AMR cofitness partners are shaped more by the host organism's regulatory wiring or by the resistance mechanism, including module membership and compensation hypotheses."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md"]
---
# Organism-specific versus mechanism-specific wiring of AMR support networks

The question is whether the partners that co-vary in fitness with antimicrobial resistance (AMR) genes depend more on the host organism or on the resistance mechanism. One report, amr_cofitness_networks, found that organism matters more: Gene Ontology (GO) overlap of cofitness partners is higher between different mechanisms in one organism than between the same mechanism in different organisms. [src: amr_cofitness_networks] The compensation interpretation is supported only if the report's co-regulation interpretation (Interpretation A) is correct. [src: amr_cofitness_networks] See also [[summaries/amr_cofitness_networks__REPORT]].

## Organism versus mechanism

Support networks are organism-specific. [src: discoveries] Different AMR mechanisms in the same organism have mean GO Jaccard 0.375, read as sharing 38% of cofitness GO terms. [src: amr_cofitness_networks] The same mechanism across organisms has mean GO Jaccard 0.207, read as sharing only 21%. [src: amr_cofitness_networks] The difference is significant (MWU, Mann-Whitney U, p = 4.3×10⁻¹³). [src: amr_cofitness_networks]

The report concludes that the organism's regulatory wiring shapes the network far more than the type of resistance mechanism. [src: amr_cofitness_networks] Its example is that an efflux pump in Pseudomonas shares more cofitness partners with a beta-lactamase in the same Pseudomonas than with an efflux pump in Shewanella. [src: amr_cofitness_networks]

The report says this result is robust to the dispensability confound. Whatever makes AMR genes correlate with their partners, each organism appears to have its own characteristic set of dispensable, co-varying genes. [src: amr_cofitness_networks] The report calls this a genuine structural property of genome organization, not an artifact of the enrichment categories. [src: amr_cofitness_networks]

Separately, module size does not differ between efflux and enzymatic mechanisms (efflux = enzymatic = 48, MWU p = 0.91). [src: amr_cofitness_networks]

## Link to cost and conservation

The report uses this to explain a puzzle from amr_fitness_cost. Mechanism predicts conservation (metal 44% accessory versus efflux 13%) but not cost. [src: amr_cofitness_networks] It attributes cost to the organism's gene content and growth context, and conservation to the mechanism's acquisition history. [src: amr_cofitness_networks] Related pages: [[concepts/fitness-cost-of-antimicrobial-resistance-genes]], [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]], [[entities/metal-resistance-genes]], [[entities/efflux-pumps]].

## Compensation hypotheses

The compensation reading is an interpretation. The report cites three supporting works.

- Martinez & Rojo (2011) reviewed the linkage between metabolism and intrinsic resistance. They noted that global metabolic regulators modulate antibiotic susceptibility. [src: amr_cofitness_networks] The report says this supports its findings only if Interpretation A is correct. [src: amr_cofitness_networks]
- Olivares Pacheco et al. (2017) showed that efflux pump costs in [[entities/pseudomonas-aeruginosa]] are metabolic (PMF drain) and compensated by metabolic rewiring. [src: amr_cofitness_networks] See [[entities/proton-motive-force]].
- Eckartt et al. (2024, Nature) identified compensatory mutations that target the same functional pathway as the resistance mutation. [src: amr_cofitness_networks]

The report regards organism-specific networks as consistent with compensation. On this view, compensation integrates AMR genes into whatever programs the organism already has. [src: amr_cofitness_networks]

## Open Directions

- Test whether the 0.375 versus 0.207 gap holds after matching organisms for the number of AMR genes and for genome size. This would show whether the gap reflects wiring or sampling.
- Compare cofitness partners of the same mechanism in closely related versus distant organisms. This would show whether organism specificity scales with phylogenetic distance.
- Check whether partners of efflux genes are enriched for energy metabolism in organisms with measured costs. This would test the PMF-drain compensation hypothesis directly.
- Relate overlap with [[concepts/amr-genes-in-ica-fitness-modules]] to see whether module membership follows the organism.
