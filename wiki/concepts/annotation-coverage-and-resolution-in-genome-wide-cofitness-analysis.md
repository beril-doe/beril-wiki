---
type: "Concept"
description: "How the coverage and uniformity of functional annotations (legacy SEED/KEGG versus InterProScan GO or Pfam) determine whether cofitness enrichment is detectable."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md", "summaries/fitness_modules__REPORT.md", "summaries/pitfalls.md"]
---
# Annotation coverage and resolution in genome-wide cofitness analysis

Annotation coverage and uniformity decide whether cofitness enrichment can be detected. In the antimicrobial resistance (AMR) cofitness project, legacy annotations gave a null result and InterProScan GO (Gene Ontology) annotations gave significant enrichment. [src: amr_cofitness_networks] In the fitness_modules project, annotation granularity and the overlap threshold both mattered: the initial pipeline (KEGG + SEED + TIGRFam, min_annotated=3) annotated few modules, and adding PFam domains while lowering the threshold to 2 raised annotation sharply. [src: discoveries, fitness_modules] The evidence is direct comparison within two projects. The AMR conclusions come from one analysis design, and the report itself frames them as a methodological point. [src: amr_cofitness_networks]

## Legacy versus InterProScan annotations in AMR cofitness networks

The annotation-comparison table reports old SEED/KEGG coverage of 40–80% per organism, variable, versus InterProScan GO coverage of 60% uniform across all genes. [src: amr_cofitness_networks] The report's text and the central digest give InterProScan GO gene coverage as 68%, 3.6× better than old SEED annotations. [src: amr_cofitness_networks, discoveries] The claims do not explain why the table says 60% and the text says 68%, so both figures are stated as the report gives them. The report also gives Pfam 88% coverage versus 68% for GO. [src: amr_cofitness_networks] See [[entities/interproscan-go-annotations]], [[entities/seed-subsystems]] and [[entities/kegg]].

The null result with old SEED annotations was 0/280 significant enrichment tests, and the central digest repeats it. [src: amr_cofitness_networks, discoveries] InterProScan GO gave 35/3,193 significant tests at FDR<0.05 (false discovery rate). [src: amr_cofitness_networks] The notebooks follow this split: the SEED analysis was null for H1/H3, while the InterProScan GO analysis found flagellar and biosynthesis enrichment for H1. [src: amr_cofitness_networks]

Cross-organism comparisons show the same pattern:
- GO terms found in ≥3 organisms: 0 with old annotations versus 6 with InterProScan GO, involving flagella and amino acid biosynthesis. [src: amr_cofitness_networks]
- Within-mechanism cross-organism Jaccard: 0.069 with old annotations versus 0.207 with InterProScan GO (3× higher). [src: amr_cofitness_networks]
- Cross-mechanism Jaccard: 0.249 versus 0.375 (1.5× higher). [src: amr_cofitness_networks]
- Cross > within p-value: 1.0 with old KEGG versus 4.3×10⁻¹³ with InterProScan GO. [src: amr_cofitness_networks]

H4 was tested with both annotation sets: old KEGG annotations in one notebook, and InterProScan GO in another that confirmed organism-specificity. [src: amr_cofitness_networks] The report concludes that genome-wide cofitness analyses need high-coverage, uniformly computed annotations, and that InterProScan on pangenome cluster representatives provides them. [src: amr_cofitness_networks] It reads the shift from null to significant as showing that legacy annotations are insufficient for functional genomics. [src: amr_cofitness_networks] See also [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]].

## Granularity and the enrichment threshold in fitness modules

Annotation granularity matters as well as coverage. In fitness_modules, the initial pipeline (KEGG + SEED + TIGRFam, min_annotated=3) annotated only 8.2% of modules (92/1,116). [src: discoveries] The stated root cause was that KEGG KO (KEGG ortholog) groups average ~1.2 genes per term, so modules with 5-50 members almost never have 3+ genes sharing a KO. [src: discoveries, pitfalls] The fitness_modules report likewise calls KEGG KOs too gene-specific for module-level enrichment. [src: fitness_modules]

Adding PFam domains (814 terms with 2+ genes versus TIGRFam's 88) and lowering the overlap threshold to 2 raised annotation to 79.7% (890/1,116). [src: discoveries, pitfalls] These two changes were made together, so the data do not separate their effects. The fitness_modules report states this as 8% to 80% (92 to 890 modules), unlocking 7.6x more function predictions. [src: fitness_modules] Predictions rose from 878 to 6,691 (7.6×), covering all 32 organisms. [src: discoveries] Annotated families rose from 32 to 145 out of 156 (93%). [src: discoveries] Three organisms (Caulo, Methanococcus_S2, Korea) went from 0 enrichments to 24-29 enriched modules. [src: discoveries] See [[entities/pfam-domain-annotations]] and [[concepts/fitness-modules-essential-genes-and-condition-specific-gene-function]].

The digest says PFam is the dominant source because its domain-level labels match module granularity. [src: discoveries] It also says min_annotated, the minimum number of overlapping genes to test, must be calibrated to annotation granularity. [src: discoveries] For gene-specific KEGG KOs (~1 gene/term), min_annotated=3 eliminates nearly all tests. [src: discoveries] For domain-level PFam annotations, min_annotated=2 works well with FDR correction. [src: discoveries] The report argues that Fisher's exact test handles small counts correctly, so validity comes from FDR correction across all tests rather than from large overlaps. [src: discoveries]

## Tensions

- PFam gives the broadest coverage in fitness_modules, but its domain-level labels may overcount functional associations. [src: fitness_modules] In the AMR project, Pfam domain-level enrichment is proposed as a way to find more specific support-network functions than broad GO terms. [src: amr_cofitness_networks] Both are expectations or cautions, not tested results.
- Legacy annotations are not uniformly worse. Old KEGG annotations identified 2 mechanism-specific terms at FDR<0.05 (lipoprotein, toluene tolerance), whereas InterProScan GO identified 0. [src: amr_cofitness_networks]

## Open Directions

- Run Pfam domain-level enrichment on the AMR support networks, where Pfam coverage is 88% versus 68% for GO. This would test whether it finds more specific functions than GO. [src: amr_cofitness_networks]
- Rerun the AMR enrichment with old annotations under a threshold matched to their granularity. This would separate the effect of coverage from that of the overlap threshold.
- Rerun fitness_modules enrichment with PFam added but min_annotated=3, and with min_annotated=2 but without PFam. This would separate the two changes.
- Check Pfam-based fitness-module enrichments against an independent functional benchmark. This would measure the overcounting risk. [src: fitness_modules]
- Examine why old KEGG found lipoprotein and toluene-tolerance terms that InterProScan GO did not. [src: amr_cofitness_networks]
