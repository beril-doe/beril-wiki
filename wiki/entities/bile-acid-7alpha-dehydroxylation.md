---
type: "Gene_Or_Pathway"
description: "Gut-microbial bai-operon bile-acid transformation whose active taxa, metabolite signature, and ecological cost shape IBD phage-cocktail design."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
Bile-acid 7α-dehydroxylation is a gut-microbial bile-acid transformation encoded by the *bai* operon; the report cites Devlin & Fischbach (2015), "A biosynthetic pathway for a prominent class of microbiota-derived bile acids" (*Nat Chem Biol* 11(9):685–690, PMID: 26412091), as the mechanism in [[entities/clostridium-scindens]]-like bacteria and as the anchor for its NB09c bile-acid network finding [src: ibd_phage_targeting].

Aliases in the corpus: "7α-dehydroxylation", "BA 7α-dehydroxylation", "*bai*-operon activity". The project attributes the activity to core *bai*-operon genes that are, in its own wording, "presumably present in essentially all *F. plautii* strains" — a presumption asserted in the report rather than a measurement made in it, so the core-rather-than-strain-variable status of the pathway is not established here [src: ibd_phage_targeting].

## Active and inactive taxa

The central digest classifies [[entities/flavonifractor-plautii]], [[entities/eggerthella-lenta]] and [[entities/enterocloster-bolteae]] as taxa that actively 7α-dehydroxylate, while [[entities/mediterraneibacter-gnavus]] and [[entities/escherichia-coli]] do not, and warns that depleting active 7α-dehydroxylators shifts the bile-acid pool toward inflammatory primary tauro-conjugated forms — a "bile-acid coupling cost" of targeting a pathobiont [src: discoveries].

The underlying project reports the discriminating pattern directly: *M. gnavus* and *E. coli* show the opposite association structure — positive with primary tauro-conjugated bile acids, negative with secondary bile acids — and were therefore not assigned to the 7α-dehydroxylation network [src: ibd_phage_targeting]. This **supports** the active/inactive split above with a within-project, measurement-level null for the two inactive taxa [src: discoveries, ibd_phage_targeting].

## Cross-corroborated evidence chain

The bile-acid claim is one of two independent six-line cross-corroboration narratives built from a single dataset, each demonstrating the same biological claim across analytical granularities. The bile-acid line runs: within-carrier pathway differential abundance (DA — testing whether a feature differs in abundance between groups) → subject-level metabolite DA → paired sample-level direct substrate-product signature → strain-level informative null → mechanism literature [src: discoveries].

A methodological caveat **qualifies** where that chain's weight sits: bile-acid pool sizes vary across cohorts because of dietary and antibiotic confounding, but the mechanistic substrate-product signature for active 7α-dehydroxylation is preserved at the within-paired-sample level. The NB09c narrative is therefore anchored on paired sample-level evidence plus the literature mechanism, not on cohort-aggregate DA replication; the report treats cohort-aggregate cross-cohort DA and within-cohort paired-sample correlation as different evidence streams, one of which can be weaker without invalidating the other [src: ibd_phage_targeting].

At the metabolite level, only 3 of 21 bile-acid-theme metabolites were CD-up (CD — Crohn's disease): free taurine, tauro-α-muricholate and tauro-β-muricholate. Free taurine, the conjugating amino acid rather than a bile acid, is CD-up at cliff=+0.47, and tauro-α/β-muricholate — a primary tauro-conjugated bile acid — is CD-up at +0.40. The report reads this as consistent with reduced microbial bile-acid 7α-dehydroxylation in Crohn's disease, where primary tauro-conjugated bile acids accumulate when *F. plautii* / *C. scindens* / Eggerthellaceae dehydroxylation activity is impaired, and as corroborating *F. plautii*'s mechanistic role [src: ibd_phage_targeting]. See [[concepts/metabolite-class-signatures-of-gut-inflammation]].

The external anchor is [[entities/franzosa]] et al. (2019), "Gut microbiome structure and metabolic activity in inflammatory bowel disease" (*Nat Microbiol* 4(2):293–305, PMID: 30531976), an [[entities/hmp2]] metabolomics plus microbiome integration described as the canonical bile-acid 7α-dehydroxylation deficit together with polyamine and lipid signatures in inflammatory bowel disease [src: ibd_phage_targeting].

## Species abundance versus strain content

The digest records zero strain-adaptation gene signal in the Kumbhari cohort and reads the association as species-abundance-mediated rather than strain-content-mediated — phage targeting would then produce predictable activity depletion with no within-species strain-content escape route [src: discoveries]. The project scopes that null to one species: it reports zero strain-adaptation genes at FDR<0.10 (FDR — false discovery rate, the multiple-testing-adjusted significance threshold) for *F. plautii*, out of 3,245 genes total tested in *F. plautii*, while the same Kumbhari analysis did recover niche-adaptation gene signals in other species, with top gene symbols consistent across 9-10 species each [src: ibd_phage_targeting].

The project's own interpretation rests on the presumptive genomic premise noted above: *F. plautii* CD-association is said to operate through species-level abundance rather than strain-level genomic adaptation because the 7α-dehydroxylation activity is encoded by core *bai*-operon genes presumably present in essentially all *F. plautii* strains, so the CD signal reflects how much *F. plautii* (any strain) is present rather than which strain dominates [src: ibd_phage_targeting]. Because the pan-strain presence of *bai* is assumed rather than measured, the "no strain-content escape route" reading suggests the hypothesis that phage depletion removes the activity with it, rather than an established finding [src: discoveries, ibd_phage_targeting].

## Design consequence for phage cocktails

Bile-acid 7α-dehydroxylation centred on *F. plautii* / *E. lenta* / *E. bolteae* and iron acquisition centred on *E. coli* AIEC (adherent-invasive *E. coli*) are proposed as two cross-corroborated six-line mechanism narratives sitting within one unified axis as orthogonal molecular sub-mechanisms [src: ibd_phage_targeting]. The iron side is developed in iron acquisition and pathobiont expansion; the bile-acid side supplies the cost term in [[concepts/ecological-cost-of-microbiome-target-depletion]].

*F. plautii*'s bile-acid coupling cost is called the dominant E1 design constraint: it is present in 78 % of patients including all 9 E1 patients, and carries the highest BA-coupling cost (NB09c §13) together with a Pillar-4 phage gap (NB12) — a double penalty that argues for deprioritizing it from the cocktail [src: ibd_phage_targeting]. Patient ecotypes such as E1 are treated as strata in [[concepts/gut-microbiome-ecotypes-as-patient-strata]].

The NB09c cost annotation is graded rather than binary: *F. plautii* targeting carries the highest cost, *E. bolteae* targeting a moderate cost as a secondary 7α-dehydroxylation contributor, *E. lenta* targeting a moderate cost with a pattern the report calls partial 7α-dehydroxylation, and [[entities/hungatella-hathewayi]] / *M. gnavus* / *E. coli* targeting a low BA-coupling cost because those species are not in the 7α-dehydroxylation network in this dataset [src: ibd_phage_targeting].

At the design-output level, Pillar 5 reports concrete cocktails for 14 of 23 patients (61 %); a pure phage cocktail is not feasible for E1, where a 3-strategy hybrid is required; the *F. plautii* bile-acid cost is the dominant E1 design constraint; and *E. coli* is present in only 35 % of the cohort [src: ibd_phage_targeting].

A translation caveat limits all of the above: the BA-coupling cost is currently ecotype-level (NB09c §13), not per-patient, so clinical translation requires per-patient bile-acid measurements [src: ibd_phage_targeting].

## Open Directions

- Measure *bai*-operon gene presence across sequenced *F. plautii* strains to test, rather than presume, the pan-strain premise that makes the activity species-abundance-mediated [src: ibd_phage_targeting].
- Pair per-patient bile-acid metabolomics with ecotype assignment to convert the ecotype-level BA-coupling cost into a per-patient cost usable in cocktail selection [src: ibd_phage_targeting].
- Re-test the substrate-product signature in a cohort with recorded diet and antibiotic exposure, to separate cohort-aggregate bile-acid pool variation from the within-paired-sample mechanistic signal the narrative rests on [src: ibd_phage_targeting].
- Repeat the Kumbhari strain-adaptation scan for *E. lenta* and *E. bolteae*, whose depletion costs NB09c rates as moderate against *F. plautii*'s highest, to see whether their 7α-dehydroxylation contribution is also species-abundance-mediated or instead strain-variable [src: discoveries, ibd_phage_targeting].
