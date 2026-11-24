---
type: "Concept"
description: "How near-universal prevalence of most fitness-assayed genes removes presence/absence variance and attenuates phi-based co-occurrence tests, including zero-variance NaN cases and co-fitness strength trends."
sources: ["summaries/cofitness_coinheritance__REPORT.md"]
---
# Core-gene prevalence ceiling on co-occurrence signal

Most genes assayed in the Fitness Browser (FB) sit in core gene clusters with >95% prevalence. That leaves little presence/absence variance, so phi-based co-occurrence tests lose power. [src: cofitness_coinheritance] The evidence comes from one report, cofitness_coinheritance. The ceiling is partly the report's own interpretation rather than a directly tested mechanism. [src: cofitness_coinheritance] See [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]] for the broader question and [[summaries/cofitness_coinheritance__REPORT]] for the report.

## Literature Context

Phylogenetic profiling, the detection of genes that co-occur across genomes, is an established way to infer functional association. PhyloCorrelate applied several co-occurrence metrics, including ones that account for phylogenetic history, to 28 315 genes across 27 372 bacterial genomes. It reported 29 762 high confidence associations and functional predictions for 834 DUFs and proteins of unknown function [PMID 33416870](https://pubmed.ncbi.nlm.nih.gov/33416870/). An earlier map of gene-gene co-occurrence across about 600 bacterial species found that co-occurring "correlogs" were enriched for physically interacting proteins and co-expressed transcripts [PMID 22219725](https://pubmed.ncbi.nlm.nih.gov/22219725/). FunCoup 4 also uses phylogenetic profiles as one evidence type for functional association networks [PMID 29165593](https://pubmed.ncbi.nlm.nih.gov/29165593/).

Work in a single phylum is closer to the hub's setting. A study of 77 cyanobacterial genomes used co-occurrence of clusters of likely ortholog genes and found modules with a high degree of functional coherence. The authors attribute this to the similar-yet-diverse nature of cyanobacteria [PMID 29522508](https://pubmed.ncbi.nlm.nih.gov/29522508/). Another study of prokaryotic genomes found that genes coding for transcription factors showed lower co-occurrence than other genes in most prokaryotes. The authors read this as rapid evolution of transcriptional regulation [PMID 25515977](https://pubmed.ncbi.nlm.nih.gov/25515977/). The other candidates (antibiotic-resistance surveys, a diatom genome, and Klebsiella and Cronobacter genomics) do not bear on the prevalence ceiling. One Cronobacter pan-genome study described an open genome dominated by accessory genes, but its co-occurrence analysis addressed resistance genes and plasmids, not fitness-assayed genes [PMID 42287752](https://pubmed.ncbi.nlm.nih.gov/42287752/).

The hub's findings are consistent with this literature in using presence/absence profiles to test functional association. They extend it by identifying a specific limit. In the Fitness Browser analysis, most genes sit in core clusters with >95% prevalence, so phi approaches 0 for cofit and random pairs alike. For Korea, 95.2% of cofit pairs had NaN phi because both genes were present in all 72 genomes. The reported delta of -0.042 is therefore attributed to noise and not to biology. None of the candidate abstracts reports this prevalence ceiling or zero-variance handling, so on this point the hub is novel relative to the retrieved papers. This is a gap in the retrieved abstracts, not evidence that the issue is unrecognized.

The cyanobacterial result is compatible with the hub's recommendation to focus on species with substantial auxiliary gene content, since that study describes a diverse group of genomes. Its abstract does not measure prevalence or variance, so this is a loose parallel and not support for the ceiling mechanism. The hub itself marks the ceiling as the report's own interpretation, and notes that the weak negative trend between co-fitness strength and phi (Spearman rho=-0.109 across 1.04M pairs) was not directly tested. Nothing in the candidate papers confirms or contradicts it. The proposed auxiliary-only re-analysis would test it directly. See [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]].

## The ceiling and how it acts

Phi approaches 0 for both cofit pairs and random pairs, because there is almost no variance to correlate. [src: cofitness_coinheritance] The report says the analysis is most informative for species with substantial auxiliary gene content. [src: cofitness_coinheritance] To address the ceiling, the report proposes re-analysis restricted to pairs whose clusters are both auxiliary (<95% prevalence), to maximize presence/absence variance. [src: cofitness_coinheritance]

## Korea: zero-variance NaN cases

For Korea, 7,994 cofit pairs had mean phi 0.447 versus 0.489 for random pairs, delta -0.042, with two-sided p-value <1e-6. [src: cofitness_coinheritance] The negative delta arises because 95.2% of Korea cofit pairs have NaN (not a number) phi. Both genes in those pairs have 100% prevalence across 72 genomes, which gives zero-variance vectors. [src: cofitness_coinheritance] Only ~8,000 of 166,601 Korea pairs are computable. The report attributes the negative delta to statistical noise in this small effective sample, not to a biological signal. [src: cofitness_coinheritance]

The same pattern appears at module level. Korea is described as the best pairwise organism, yet it shows 0% significant modules. All its modules are >90% core with prevalence near 1.0. [src: cofitness_coinheritance] See [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]] for module-level results.

## Co-fitness strength trend

Stronger co-fitness scores weakly predicted lower phi across 1.04M pairs (Spearman rho=-0.109, p<1e-300). [src: cofitness_coinheritance] The report suggests this likely reflects a prevalence ceiling. The strongest co-fitness pairs are core genes with near-universal prevalence, which leaves little variance for co-occurrence detection. [src: cofitness_coinheritance] This is an explanation the report proposes, not a result it tested. [src: cofitness_coinheritance]

## Related limits

- The near-clonal species Ddia6719 and pseudo3_N2E3 have high baseline phi, so their absolute phi values are less interpretable. [src: cofitness_coinheritance]
- Ralstonia UW163 and GMI1000 have zero co-fitness data in the [[entities/fitness-browser]] despite being in its organism table, so they were excluded from the primary analysis. [src: cofitness_coinheritance]
- They are the most phylogenetically diverse, with the lowest average nucleotide identity (ANI), so they would likely have been the most informative species. [src: cofitness_coinheritance]

## Open Directions

- Run the auxiliary-only re-analysis described above, to test whether the cofit-versus-random phi difference reappears once the ceiling is removed.
- Stratify the co-fitness-strength versus phi correlation by pair prevalence, to test whether the rho of -0.109 is driven by core-gene pairs.
- Add co-fitness data for the two Ralstonia organisms, or other high-diversity species, to test the signal where auxiliary content is large.
- Report the number of computable (non-NaN) pairs next to every delta, so that results like Korea's are not read as biology.
