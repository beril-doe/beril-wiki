---
type: "Concept"
description: "Pathway, metabolite and paired-sample evidence that some Crohn's-associated pathobionts carry out bile-acid 7α-dehydroxylation, and what depleting them is predicted to cost; stops at generic metabolomics methods."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
# Bile-acid 7α-dehydroxylation deficit and the ecological cost of targeting bile-acid-transforming species

Some Crohn's disease (CD)-associated pathobionts, notably Flavonifractor plautii, Eggerthella lenta and Enterocloster bolteae, appear to carry out bile-acid 7α-dehydroxylation in paired HMP2 samples. The ibd_phage_targeting report therefore predicts that depleting them by phage would carry an ecological cost. The evidence is correlational and ecotype-level, and it rests mostly on within-cohort paired samples plus literature mechanism. The report supports the cost as a precaution, not as a clinically validated result. [src: discoveries, ibd_phage_targeting]

## Pathway and metabolite evidence

The report calls F. plautii, E. lenta and E. bolteae active 7α-dehydroxylating species in the CD pathobiont module. [src: ibd_phage_targeting] It describes a six-line convergence narrative: NB07b F420-pathway, NB09a tauro-muricholate, NB09c paired correlation, NB05 actionable status, Franzosa 2019, and Devlin/Fischbach mechanism literature. [src: ibd_phage_targeting]

- NB07b finds F420-bile-acid metabolism among the within-carrier CD-up biosynthesis pathways of F. plautii (see [[entities/flavonifractor-plautii]]). [src: ibd_phage_targeting]
- In HMP2, only 3 of 21 bile-acid-theme metabolites are CD-up (OR 0.56, FDR 1.0), so the theme as a whole is not supported. [src: ibd_phage_targeting] The three are free taurine, tauro-α-muricholate and tauro-β-muricholate. [src: ibd_phage_targeting]
- NB09a reads the tauro-muricholate and taurine elevation at subject level as substrate-pool elevation. [src: ibd_phage_targeting] The report takes it as consistent with reduced microbial 7α-dehydroxylation in CD. It also says it corroborates F. plautii's mechanistic role. [src: ibd_phage_targeting]

## Paired-sample substrate–product signature

NB09c used 468 paired CSM* HMP2 samples, 8 species and 583 metabolites, with Spearman ρ. F. plautii, E. lenta and E. bolteae show the predicted signature: negative with primary tauro-bile acids and positive with secondary bile acids. [src: ibd_phage_targeting] The report calls this direct sample-level confirmation of the network in HMP2. [src: ibd_phage_targeting]

| Species | Correlations (ρ) |
|---|---|
| F. plautii | cholate −0.26; lithocholate +0.15 [src: ibd_phage_targeting] |
| E. bolteae | deoxycholate +0.17; lithocholate +0.18 [src: ibd_phage_targeting] |
| E. lenta | ketodeoxycholate −0.14; cholate −0.13 [src: ibd_phage_targeting] |

Mediterraneibacter gnavus and Escherichia coli show the opposite pattern. Their correlations are positive with primary tauro-bile acids and negative with secondary ones, so the report places them outside the network. [src: ibd_phage_targeting] Separately, the report describes C. scindens as a protective 7α-dehydroxylating species. [src: discoveries] See also [[entities/clostridium-scindens]], [[entities/eggerthella-lenta]] and [[entities/mediterraneibacter-gnavus]].

## Predicted cost of depletion

The report predicts that phage targeting of F. plautii, E. lenta and E. bolteae would shift the bile-acid pool toward inflammatory primary tauro-conjugated forms. [src: ibd_phage_targeting, discoveries] For the NB05 actionable Tier-A targets, it replaces "metabolic-coupling cost" with bile-acid coupling cost as the primary per-target ecological-cost annotation. [src: ibd_phage_targeting]

- F. plautii: highest cost. [src: ibd_phage_targeting] It is Tier-2 phage priority, and the report suggests considering UDCA or a bile-acid-binding agent. [src: ibd_phage_targeting]
- E. bolteae: moderate cost, as a secondary 7α-dehydroxylation contributor. [src: ibd_phage_targeting]
- E. lenta: moderate cost, a partial pattern consistent with Eggerthellaceae bile-acid metabolism. [src: ibd_phage_targeting]
- H. hathewayi, M. gnavus and E. coli: low cost, because they are outside the network in this dataset. [src: ibd_phage_targeting, discoveries]

The report recommends avoiding F. plautii and using UDCA or cholestyramine co-therapy to maintain the secondary bile-acid pool. [src: ibd_phage_targeting]

The strain-level analyses returned nulls for F. plautii: zero FDR<0.10 strain-adaptation genes among 3,245 tested in Kumbhari, and 0 FDR-passing genes in NB10a. [src: ibd_phage_targeting] The report reads this as species-abundance-mediated CD association. [src: ibd_phage_targeting] From that it infers that phage depletion would reduce 7α-dehydroxylation proportionally, with no escape route via within-species gene-content selection. [src: ibd_phage_targeting] This is an inference, and it rests on the hypothesis that the activity is encoded by core bai-operon genes present in essentially all strains. [src: ibd_phage_targeting]

The general rule is not to treat "depletes target species" as the sole optimization criterion for microbiome interventions. Incidental loss of beneficial activity such as 7α-dehydroxylation or butyrogenesis changes the net inflammatory balance. [src: discoveries]

## Caveats and evidence streams

Cohort-aggregate cross-cohort bile-acid differential abundance is weaker. Sign-concordance is 57% for primary and 40% for secondary bile acids. [src: ibd_phage_targeting] The report ranks the paired HMP2 signature as the more robust stream, because aggregate metabolite differential abundance is dominated by batch effects. [src: ibd_phage_targeting] It also says bile-acid pool sizes are more susceptible to dietary and antibiotic confounding than within-cohort species × metabolite correlation. [src: ibd_phage_targeting] The two are different evidence streams, and one can be weaker without invalidating the other. [src: ibd_phage_targeting] The signature is a species × metabolite correlation, not a CD-vs-Control aggregate differential abundance. [src: ibd_phage_targeting] For the batch problem, see [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

The UC Davis cohort has no per-patient bile-acid measurements. The F. plautii annotation is therefore ecotype-level, from paired HMP2 samples. [src: ibd_phage_targeting] Clinical translation needs per-patient bile-acid panels for monitoring and dosing. [src: ibd_phage_targeting]

## Open Directions

- Measure per-patient bile-acid panels in a CD cohort that also has taxon abundances. This would test the ecotype-level cost prediction at patient level.
- Check bai-operon presence and expression across F. plautii strains. This would test the core-gene hypothesis behind the "no strain escape" inference.
- Repeat the paired substrate–product correlations in a second paired cohort with diet and antibiotic covariates. This would address confounding and the single-cohort limit.
- Model a phage-depletion scenario with and without UDCA or cholestyramine on the tauro-conjugated:secondary bile-acid ratio.
- Relate the network to [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]] to ask whether commensal 7α-dehydroxylators could compensate.
