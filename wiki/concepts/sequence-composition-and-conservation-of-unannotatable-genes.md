---
type: "Concept"
description: "Comparison of length, GC, core/accessory status, essentiality and ortholog breadth between persistently unannotated and later-annotated genes, including confounds such as gene length."
sources: ["summaries/discoveries.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Sequence composition and conservation of unannotatable genes

Persistently unannotated ("truly dark") genes differ from later-annotated ("annotation-lag") genes in length, GC content, pangenome status and ortholog breadth. The report states that all its structural comparison effects exceed its pre-registered thresholds of Cohen's d ≥ 0.2 or OR (odds ratio) ≥ 1.5. [src: truly_dark_genes] Gene length is a stated confound. [src: truly_dark_genes]

## Literature Context

The candidate papers say little about the length, GC and ortholog-breadth comparison itself. They do give context on why unannotated genes are hard to study and why they may still matter. Several are in silico surveys of hypothetical proteins. One study characterised hypothetical proteins from 6 Clostridium difficile strains with bioinformatic tools [PMID 36035185](https://pubmed.ncbi.nlm.nih.gov/36035185/). Another predicted functions for 142 of the 366 uncharacterized proteins in Chlamydophila pneumoniae CWL029 [PMID 26649559](https://pubmed.ncbi.nlm.nih.gov/26649559/). These are computational predictions, not experimental tests. A network-based study of a Pseudomonas aeruginosa pan-proteome (635 strains) placed 4% of proteins in completely dark connected components. It then ranked them partly by taxonomic restriction and by conservation across strains [PMID 42605071](https://pubmed.ncbi.nlm.nih.gov/42605071/). That framing is close to the hub's pairing of narrow ortholog breadth with persistent darkness.

Two further papers bear on the confounds of length and mobile origin. In Shewanella oneidensis MR-1, proteomics detected 36 proteins under 101 amino acids, including 10 annotated as hypothetical [PMID 15669716](https://pubmed.ncbi.nlm.nih.gov/15669716/). Some conserved hypotheticals were seen at frequencies similar to essential small proteins, which suggests that short genes can be real and important, though this is a single-organism observation. In Streptococcus mutans, SprV is a conserved 90-amino-acid hypothetical protein essential for normal growth. Its deletion altered about 20% of gene expression, and inactivating the S. gordonii ortholog also caused poor growth and defective UV tolerance and competence development [PMID 28167518](https://pubmed.ncbi.nlm.nih.gov/28167518/). That is two streptococcal species, so it is still a narrow test. The authors also note that its function differs from that of structure- and sequence-based homologs. Both papers support the caution that short, unannotated genes are not necessarily dispensable, and that length-related measurement and annotation bias may hide function. This bears on the hub's higher essential fraction among truly dark genes, 18.0% versus 13.4%.

On mobile origin, the Klebsiella pneumoniae 342 microarray comparison found that E. coli K-12 open reading frames with little or no identity in strain 342 included hypothetical proteins and genes presumed to come from lateral transfer by phage, plasmids or transposons [PMID 11282649](https://pubmed.ncbi.nlm.nih.gov/11282649/). A nine-isolate Salmonella Typhimurium study, which its authors call exploratory, found over 90% core genome conservation. Variability was concentrated in genomic islands encoding hypothetical proteins [PMID 41471146](https://pubmed.ncbi.nlm.nih.gov/41471146/). Both are consistent with the report's reading that accessory, recently acquired, poorly conserved genes are enriched among the unannotated.

Overall, the corpus's findings are consistent with this literature in direction. Truly dark genes are less often core (43.1% versus 72.7%), have narrower ortholog breadth, and show larger GC deviation. The literature does not test them directly. The corpus's quantified effects (d = −0.432 for length, OR = 0.284 for core status, OR = 0.236 for ortholog presence) have no counterpart in these papers, so they are novel and extend the literature. The length-matched refit is only a proposed analysis in the hub's Open Directions, so no length-adjusted result exists. The candidate papers do not remove the length confound. See [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]].

## Length and GC content

Truly dark genes are shorter: median length is 121 aa versus 194 aa for annotation-lag genes (d = −0.432, p < 1e-100). [src: discoveries, truly_dark_genes] Mean GC content is lower, 0.542 versus 0.584 (d = −0.395, p = 2e-115). [src: truly_dark_genes] Deviation from the host genome mean is nonetheless larger for truly dark genes (mean |ΔGC| = 0.047 vs 0.038, d = 0.247, p = 1.3e-43). [src: discoveries, truly_dark_genes] Strong deviation (|z| > 2) affects 9.2% of truly dark genes versus 4.0% of annotation-lag genes. The report calls this consistent with recent horizontal gene transfer outpacing annotation databases. [src: truly_dark_genes] See [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]].

## Conservation, orthologs and essentiality

Truly dark genes are less often core: 43.1% versus 72.7% (OR = 0.284, p < 1e-100). [src: discoveries, truly_dark_genes] Orthologs exist for 29.3% of them versus 63.7% of annotation-lag genes (OR = 0.236, p < 1e-100). [src: discoveries, truly_dark_genes] Median ortholog breadth is 1 organism versus 4 (d = −1.072, p < 1e-100). [src: truly_dark_genes] Only 3 of 65 dark-gene ortholog groups with cross-organism concordance data contain truly dark genes. [src: truly_dark_genes] See [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]] and [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs]].

The essential fraction is higher for truly dark genes, 18.0% versus 13.4% (OR = 1.420, p < 1e-10). [src: truly_dark_genes]

## Interpretation and confounds

The report reads these differences together as evidence of recently acquired, rapidly evolving novel biology rather than annotation lag. The lines it cites are shorter sequences, accessory genome enrichment, higher GC deviation, mobile-element proximity and narrow taxonomic breadth. [src: truly_dark_genes] This is the report's interpretation.

Two caveats limit it. Short genes are harder to annotate and harder to measure fitness for, so the length difference (d = −0.432) may partly explain the other differences. [src: truly_dark_genes] Also, BBH (bidirectional best hit) orthologs cover only 32 of 48 FB (Fitness Browser) organisms. Truly dark genes from the other 16 lack concordance and ortholog-breadth data. [src: truly_dark_genes] See [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]] and [[concepts/fitness-measurement-of-novel-singleton-genes-and-assay-limits]].

## Open Directions

- Refit the ortholog, core and GC comparisons with gene length as a covariate, or within length-matched strata. This would show how much of each effect survives the length confound.
- Extend ortholog detection to the 16 uncovered Fitness Browser organisms. This would test whether the narrow-breadth result holds across all organisms.
- Compare GC deviation with direct mobile-element proximity per gene. This would test the horizontal-transfer explanation.
- Check whether the higher essential fraction persists after length matching, using [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]] to separate real essentiality from measurement limits.
