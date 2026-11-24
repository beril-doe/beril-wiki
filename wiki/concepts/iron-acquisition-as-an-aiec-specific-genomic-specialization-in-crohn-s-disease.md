---
type: "Concept"
description: "Convergent pathway, gene-cluster and correlation evidence that iron acquisition and genotoxin loci mark adherent-invasive E. coli rather than all Crohn's pathobionts, with comparator caveats; stops at strain-resolved diagnostics."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
# Iron acquisition as an AIEC-specific genomic specialization in Crohn's disease

This page covers iron acquisition as an AIEC-specific genomic specialization in Crohn's disease (CD). The iron theme is narrowed to adherent-invasive Escherichia coli (AIEC), not to all CD pathobionts. [src: ibd_phage_targeting] NB08a also finds an iron-plus-genotoxin gene-cluster signature that is E. coli-only within the Tier-A core. [src: ibd_phage_targeting] The evidence comes from several analyses in the ibd_phage_targeting project. The NB07c narrowing is correlation-based. [src: ibd_phage_targeting] See also [[entities/escherichia-coli]] and [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

## Convergent lines of evidence

The report chains literature and database lookup, sample-level attribution, cohort-level enrichment, species–pathway covariation and genomic gene-cluster content. [src: discoveries] It counts these as five independent streams across three analytical granularities. [src: ibd_phage_targeting] A separate tally gives six lines: NB05, NB07a, NB07 v1.8, NB07c, NB08a and AIEC literature. [src: ibd_phage_targeting] The central discoveries digest likewise describes a four-way convergence of the pathway enrichment with E. coli Yersiniabactin/Enterobactin MIBiG matches, heme-biosynthesis attribution to E. coli, and AIEC iron-acquisition literature. [src: discoveries]

- **Pathway enrichment.** Iron/heme acquisition was the dominant CD-up theme in v1.8 (odds ratio, OR, = 8.1; false discovery rate, FDR, 7e-6; 15 of 52 CD-up pathways). This supported hypothesis H3a (b). [src: discoveries, ibd_phage_targeting]
- **Species attribution.** NB07a found a heme–E. coli pathway–pathobiont association of ρ=0.640. [src: ibd_phage_targeting]
- **Covariation.** NB07c found iron-pathway covariation concentrated on E. coli, with mean ρ=0.45 versus 0.13 for Anaerostipes caccae. [src: ibd_phage_targeting]
- **Genomic content.** NB08a found that E. coli alone among the actionable Tier-A core species carries iron-siderophore MIBiG matches: 54 BGCs (biosynthetic gene clusters) versus 0 in the other 5 actionable species. [src: ibd_phage_targeting] The enrichment is driven entirely by these 54 clusters. [src: ibd_phage_targeting] They comprise 19 Yersiniabactin, 16 Enterobactin and 19 siderophore-class clusters. [src: ibd_phage_targeting] E. coli also carries 25 genotoxin clusters, 8 Colibactin and 15 Microcin B17. [src: ibd_phage_targeting] Together these form an iron-plus-genotoxin signature unique to E. coli in the Tier-A core. [src: ibd_phage_targeting]
- **Theme enrichment.** NB08a gave iron_siderophore OR=44.4 (FDR 6e-56) and genotoxin_microcin OR=234 (FDR 3e-35). It rated H3c only partially supported. [src: ibd_phage_targeting] Both signatures were E. coli-only within the Tier-A core. [src: ibd_phage_targeting]

## Specific to AIEC, not all pathobionts

NB07c narrowed the v1.8 interpretation. The iron theme belongs to CD-associated E. coli, particularly its AIEC subset, and other Tier-A pathobionts have non-iron specializations. [src: ibd_phage_targeting] The report reads NB08a as genomic confirmation of this narrowing. It cites H. hathewayi purine and TMA (trimethylamine)/choline themes as the non-iron example. [src: ibd_phage_targeting] It also reads the result as showing iron acquisition to be a pathobiont-defining genomic capability, not just a pathway-level cohort signal. [src: ibd_phage_targeting] Its summary of the mechanism is E. coli AIEC subset, OR=8.1 for pathways and OR=44 for BGCs. [src: ibd_phage_targeting]

The report proposes, as interpretation, that CD-associated E. coli is an AIEC-specialized subset that invested in iron and adherent-invasion machinery at the cost of generalist metabolism. [src: ibd_phage_targeting] In NB07b, E. coli (20 passing pathways) showed within-carrier CD-down per-pathway abundance, opposite to its cohort-level CD-up direction. [src: ibd_phage_targeting] From this and the NB08a clusters, the report attributes the E. coli CD association to strain content in an AIEC subset. [src: ibd_phage_targeting]

## Comparator caveats and limits

- **Inflated odds ratio.** The OR of 44 is partly inflated because iron MIBiG matches are rare catalog-wide (51 / 9,774 = 0.5 %). It should not be read as a precise effect size. [src: ibd_phage_targeting] The report says the qualitative E. coli-only signature is robust across comparator choices. [src: ibd_phage_targeting]
- **Unmatched background.** The Tier-A background is the full catalog of 10,060 BGCs across all species, not a matched comparator. [src: ibd_phage_targeting] A matched-niche set was suggested as more conservative. [src: ibd_phage_targeting]
- **Negative control.** bacteriocin_RiPP sits at background rate (154 / 286 versus 5,217 / 9,774; OR 1.02, FDR 0.90). [src: ibd_phage_targeting]
- **Correlation basis.** The narrowing to E. coli rests on species-by-pathway Spearman ρ across CMD_IBD samples. [src: ibd_phage_targeting]
- **Menaquinol pathways.** In v1.8, 8 of 15 iron pathways were menaquinol biosynthesis, which is not strictly E. coli-specific. The strongest signature pathways, ENTBACSYN-PWY and HEMESYN2-PWY, are E. coli-canonical. [src: ibd_phage_targeting]
- **No interaction test.** The strict species-by-BGC interaction test for H3c was untested and dropped. [src: ibd_phage_targeting] NB08a Test 3 uses a CD-versus-healthy main-effect table, so it cannot separate interaction from species and BGC main effects. [src: ibd_phage_targeting] The interaction test needs raw-read-derived species-stratified BGC abundance, so the report treats the drop as a structural scope limit, not a deferred task. [src: ibd_phage_targeting]
- **Metabolomics.** Metabolomics is neutral for the iron/heme axis, because LC-MS (liquid chromatography-mass spectrometry) undersamples siderophores. [src: ibd_phage_targeting]

## Implications for intervention

The iron/AIEC axis informs whether to target a species broadly or only its AIEC subset. [src: discoveries] Applying the NB13 5-phage cocktail clinically would need per-patient genotyping for pks-island, Yersiniabactin and Enterobactin genes by PCR or an amplicon panel. [src: ibd_phage_targeting]

## Open Directions

- Genotype E. coli isolates or metagenome-assembled strains for pks, Yersiniabactin and Enterobactin loci, and test whether CD association tracks these loci. This would replace the correlational narrowing with a strain-resolved test.
- Recompute the iron-siderophore and genotoxin enrichment against a matched-niche comparator (gut Proteobacteria plus CD-associated Firmicutes). This would give a defensible effect size.
- Obtain species-stratified per-sample BGC abundance from raw reads to run the species-by-BGC interaction test for H3c.
- Test whether the 8 menaquinol pathways drive the iron-theme enrichment, by rerunning it without them.
- Measure siderophores with targeted metabolomics, since LC-MS undersampled them.
