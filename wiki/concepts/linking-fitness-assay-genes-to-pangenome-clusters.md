---
type: "Concept"
description: "Coverage, mapping quality and exclusions when linking genes from a fitness library collection to pangenome species clusters by protein search, and how clade size limits core/auxiliary discrimination."
sources: ["summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md", "summaries/discoveries.md", "summaries/essential_genome__REPORT.md", "summaries/fitness_effects_conservation__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pitfalls.md", "summaries/prophage_amr_comobilization__REPORT.md"]
---
# Linking fitness-assay genes to pangenome clusters

This page covers how genes from the [[entities/fitness-browser]] (FB) library collection are linked to pangenome species clusters by protein search, and what limits the link. The main link table has 177,863 gene-to-cluster links, and 44 of 48 FB organisms mapped to a species clade. [src: conservation_vs_fitness] The weak points are organism attrition, a strict identity threshold, locus-tag mismatches and small clades. Most of this evidence is direct counting in one pipeline. The reports' explanations for what the threshold misses are stated as concerns, not measured.

## The link table and its coverage

The bridge file is `conservation_vs_fitness/fb_pangenome_link.tsv`. Several later reports reuse it. [src: amr_fitness_cost, cofitness_coinheritance, core_gene_tradeoffs, essential_genome, fitness_effects_conservation] The pairwise cofitness method maps cofit pairs to cluster pairs through this table. [src: cofitness_coinheritance] The mapping gave 177,863 links at 100.0% median protein identity and 94.2% median gene coverage. [src: conservation_vs_fitness] The linked genes were 145,821 core (82.0%) and 32,042 auxiliary (18.0%). The auxiliary genes include 7,574 singletons. [src: conservation_vs_fitness] A separate report used the table to find 178 AMR (antimicrobial resistance) genes across 37 FB organisms, with 29,386 fitness measurements. [src: amr_pangenome_atlas]

## Organism attrition and exclusions

Organisms drop out at each stage. See [[concepts/organism-coverage-and-attrition-in-cross-organism-fitness-conservation-analyses]] for the wider picture.

- Four organisms did not map: Cola, Kang, Magneto and SB2B. Their species had too few GTDB genomes to build a pangenome. [src: conservation_vs_fitness]
- Of the mapped organisms, 34 have at least 90% coverage. Phase 2 used 33, because Dyella79 was excluded for a locus-tag mismatch. [src: conservation_vs_fitness] Phase 2 therefore excluded 10 organisms with under 90% DIAMOND coverage, which reduces taxonomic breadth. [src: conservation_vs_fitness]
- *Escherichia coli* was excluded because its main clade was absent from the pangenome (too many genomes). Keio (E. coli BW25113) mapped to the small `s__Escherichia_coli_E` clade at only 26.1% coverage. [src: conservation_vs_fitness] See [[entities/escherichia-coli]].
- The metal atlas had links for only 22 of 48 organisms, so 26 lack mappings. [src: metal_fitness_atlas] Conservation analysis there covers 22 of 31 metal-tested organisms (71%). [src: metal_fitness_atlas] The 9 excluded organisms are Putida, Keio, SynE, Miya, Kang, BFirm, Cola, Ponti and Dino. [src: metal_fitness_atlas] That report judges bias unlikely because they are taxonomically diverse. [src: metal_fitness_atlas]
- One report could not test its fitness-cost hypothesis H3. It states that the 48 RB-TnSeq (random barcode transposon sequencing) organisms overlap poorly with the GTDB pangenome species it analyzed. [src: prophage_amr_comobilization]

## Mapping quality: identity thresholds

The reports raise the same worry about the identity cutoff. The 100% identity threshold avoids paralog confusion. It may undercount fitness effects of close variants, such as alleles differing by one synonymous substitution. [src: amr_pangenome_atlas] It may also miss closely related alleles and so undercount AMR fitness effects. [src: amr_pangenome_atlas] Other reports cite a 90% [[entities/diamond]] threshold. They caution that it may miss rapidly evolving genes [src: core_gene_tradeoffs] or recently acquired genes with low similarity. [src: costly_dispensable_genes] These are stated as possible losses, not measured ones. The reports give the thresholds as 100% and 90% without reconciling them. See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]].

## Locus-tag mismatches

The FB aaseqs download uses RefSeq-style locus tags for some organisms, for example ABZR86_RS*. The FB gene table uses original tags such as N515DRAFT_*. [src: discoveries, pitfalls] Joining DIAMOND hits back to the gene table can then silently give zero matches. [src: pitfalls] Dyella79 had 0% overlap, while other organisms had over 94%. [src: pitfalls] This caused a complete join failure (0% merge rate) for Dyella79. [src: conservation_vs_fitness, discoveries] It affected 1 of 34 organisms. The lesson is to verify locus-tag consistency in any pipeline that joins aaseqs-derived data to the gene table. [src: discoveries] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

## Clade size limits core/auxiliary discrimination

Small clades make "core" a weak label. A clade with 2 genomes has trivially high core fractions, because a gene in both genomes counts as 100% core. [src: conservation_vs_fitness] Most FB species have few GTDB genomes (median 9, range 2–399), which makes the ≥95% core threshold imprecise. [src: amr_fitness_cost] A gene present in all 9 genomes is labeled core but could be accessory at larger sampling depth. [src: amr_fitness_cost] The core-versus-accessory null result should be read cautiously for species with fewer than 20 genomes. [src: amr_fitness_cost]

## Open Directions

- Re-run the link at several identity thresholds, for example 90%, 95% and 100%. Compare the number of links and AMR genes recovered. This would measure what the strict cutoff misses. [src: amr_pangenome_atlas, core_gene_tradeoffs, costly_dispensable_genes]
- Repeat the core/auxiliary comparison on species with at least 20 genomes only. Check whether the null result holds. [src: amr_fitness_cost]
- Add a locus-tag overlap check for every organism before joining. List any other organisms with partial mismatches. [src: discoveries, pitfalls]
- Rebuild the pangenome clade for E. coli so that Keio maps with high coverage. [src: conservation_vs_fitness]
- Test whether the 10 organisms below 90% coverage differ in taxonomy from the 33 retained. [src: conservation_vs_fitness]
