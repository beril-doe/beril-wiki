---
type: "Concept"
description: "How few organisms with genome-wide fitness data carry a given defense gene or architecture, and what that means for testing its phenotype; stops at the Fitness Browser and PhageFoundry collections."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
---
# Fitness-data coverage gaps for defense genes

Genome-wide fitness data cover very few carriers of the SNIPE defense gene: the Fitness Browser has one organism with the full two-domain architecture. [src: snipe_defense_system] PhageFoundry has SNIPE annotations in Klebsiella but no fitness tables. [src: discoveries, snipe_defense_system] The evidence is direct database queries, but it rests on a single archaeal gene. See [[entities/snipe]], [[entities/fitness-browser]] and [[entities/phagefoundry]].

## Fitness Browser coverage of SNIPE

The Fitness Browser holds one SNIPE protein, so the phenotype of this defense architecture can be tested in only one organism. The query covered 48 organisms, 228K genes and 27M fitness scores. [src: snipe_defense_system]

The carrier is [[entities/methanococcus-maripaludis]] JJ, locus MMJJ_RS01635. It has PF13250 (DUF4041), PF13455 (Mug113/GIY-YIG nuclease) and PF10544 (DUF2525). [src: discoveries, snipe_defense_system] The protein has 129 fitness experiments and is described as the first SNIPE homologue with genome-wide knockout phenotypes. [src: discoveries, snipe_defense_system] The report calls it the first organism with both a confirmed SNIPE protein and genome-wide fitness data. [src: snipe_defense_system]

Only M. maripaludis has the full PF13250 + PF13455 architecture. [src: snipe_defense_system] The nuclease domain PF13455 alone ([[entities/mug113-nuclease-domain-pf13455]]) appears in 7 genes across 6 organisms: Azospirillum brasilense, Bacteroides thetaiotaomicron, Cupriavidus, Desulfovibrio vulgaris, Paraburkholderia kururiensis and M. maripaludis. [src: snipe_defense_system]

### What the one gene shows

The M. maripaludis SNIPE gene shows mild fitness defects under specific conditions, with a minimum fitness of -1.16 on formate/acetate. [src: snipe_defense_system] It is dispensable under most conditions. [src: snipe_defense_system]

M. maripaludis is an archaeon, and the report notes that its phage biology context differs significantly from the Enterobacterales phage lambda system. [src: snipe_defense_system]

## Klebsiella and PhageFoundry

PhageFoundry's Klebsiella genome browser has 1 DUF4041 annotation, representing 3 proteins at 558 aa, the same length as Escherichia coli SNIPE. It also has 4,619 PTS_EIIC (PF02378/ManY family) annotations. [src: discoveries] Klebsiella is the only PhageFoundry species with both SNIPE and the ManX-family PTS domain PF00358. [src: discoveries]

These annotations cannot be linked to fitness. PhageFoundry provides genome annotations only, in GenomeDepot format, with no fitness or TnSeq (transposon sequencing) tables. [src: snipe_defense_system] No Klebsiella strain in the Fitness Browser carries ManXYZ by gene name. [src: snipe_defense_system] So there is no Klebsiella-specific SNIPE or ManYZ fitness data here. [src: snipe_defense_system] Generating it would need new mutant libraries in natural carriers such as Klebsiella pneumoniae NCTC9140 or HS11286. [src: snipe_defense_system] The report developed a plan, PLAN_fitness_data_curation.md, to curate external K. pneumoniae Tn-Seq datasets. [src: snipe_defense_system]

## Caveats

The KBase Data Lakehouse Fitness Browser API (application programming interface) was experiencing a 503 outage during the analysis. [src: snipe_defense_system]

## Open Directions

- Curate the external K. pneumoniae Tn-Seq datasets from the report's plan, and test whether any covers a natural SNIPE carrier. This would close the Klebsiella gap.
- Rerun the PF13250 and PF13455 queries against the Fitness Browser tables in the KBase Data Lakehouse now that the API outage may be over. This would confirm that M. maripaludis is the only full-architecture carrier.
- Check whether the six PF13455-only organisms show nuclease-domain phenotypes. This would add comparators to the single archaeal gene.
- Build mutant libraries in K. pneumoniae NCTC9140 or HS11286 to test SNIPE and ManYZ phenotypes under phage challenge. See [[concepts/adsorption-receptors-versus-defense-systems-as-determinants-of-phage-host-range]].
