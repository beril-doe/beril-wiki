---
type: "Concept"
description: "Membership of AMR genes in independent-component-analysis (ICA) fitness modules, module size and cross-organism conservation of module families; stops at network-level enrichment."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md"]
---
# AMR genes in ICA fitness modules

This page covers which antimicrobial resistance (AMR) genes fall into independent component analysis (ICA) fitness modules, how large those modules are, and how widely their module families are conserved across organisms. The evidence comes from one project, amr_cofitness_networks, which analysed Fitness Browser data and compared module sizes with a statistical test. The central discoveries digest repeats the module-size result. [src: amr_cofitness_networks, discoveries] See [[summaries/amr_cofitness_networks__REPORT]] for the full report and [[entities/independent-component-analysis-fitness-modules]] for the method.

## Membership and module size

Only a minority of AMR genes are in modules, but the modules that contain them are larger than non-AMR modules. Only 24% of AMR genes (192/801) are assigned to ICA fitness modules. [src: amr_cofitness_networks] The modules they inhabit have a median of 46 genes, against 27 for non-AMR modules (Mann-Whitney U (MWU) p = 1.7×10⁻⁸). [src: amr_cofitness_networks, discoveries]

The report reads this as AMR genes sitting in large, multi-function cellular programs when they are tightly co-regulated with other genes, not in small isolated modules. [src: amr_cofitness_networks] It regards the size result as robust. Its reason is that ICA captures condition-specific co-regulation, not just shared mean fitness. [src: amr_cofitness_networks]

Module size did not differ between the efflux and enzymatic AMR mechanisms. Both had a median of 48 (MWU p = 0.91). [src: amr_cofitness_networks] See [[entities/efflux-pumps]] for the efflux class.

## Cross-organism conservation

Nearly all AMR module assignments fall in conserved module families. AMR genes occur in 136 unique module families. [src: amr_cofitness_networks] By assignment, 99% (208/209) of AMR gene-module assignments lie in cross-organism conserved module families, which the report interprets as ancient regulatory relationships. [src: amr_cofitness_networks] The report also states that 99% are in cross-organism conserved families. [src: amr_cofitness_networks] The report concludes that AMR genes that do land in modules are embedded in broad cellular programs with genuine co-regulatory structure. [src: amr_cofitness_networks]

## Supporting literature

The report cites Sagawa et al. (2017) as having validated that cofitness recovers transcriptional regulatory relationships in 24 bacteria. [src: amr_cofitness_networks] See [[entities/cofitness-analysis]].

## Open Directions

- Test why only 24% of AMR genes (192/801) enter modules. Compare module-assigned and unassigned AMR genes by mechanism, organism and gene fitness variance.
- Check whether the larger module size holds against a size-matched null. Draw random gene sets from non-AMR modules and compare them with AMR modules.
- Ask what the 136 module families do. Annotate their non-AMR members to name the "broad cellular programs" the report infers.
- Examine the 1 of 209 assignments outside conserved families. Test whether it is organism-specific resistance wiring, and compare with [[concepts/organism-specific-versus-mechanism-specific-wiring-of-amr-support-networks]].
