---
type: "Method"
description: "CheckM is a tool that estimates genome completeness and contamination; BERIL projects use it to filter genomes by quality, to rescale genome-content measures, and to check whether genome-size and pathway-count contrasts are quality artefacts."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md"]
---
# CheckM

CheckM estimates genome completeness and contamination. The two projects here use it in three ways. They filter genomes by quality before comparing cohorts. They rescale genome-content measures by completeness. They also compare mean completeness between cohorts to test whether differences in genome content are artefacts of MAG (metagenome-assembled genome) quality [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].

## Use in Bacillota B subsurface genome comparisons

The project compared deep-clay [[entities/bacillota-b]] anchor genomes (n=10) with soil-baseline Bacillota_B genomes (n=62). After CheckM rescaling, mean genome size in base pairs was 4,323,230 for the anchors and 3,233,715 for the baseline. The effect size was Cohen's d +1.37 (Cohen's d is a standardized effect size; see cohens d), with Mann–Whitney p 0.013. Mean CheckM-rescaled [[entities/eggnog]] OG (orthologous group) counts were 2,771 for the anchors and 2,233 for the baseline (d +1.32; p 0.009). In both measures the deep-clay anchors were larger [src: bacillota_b_subsurface_accessory].

Mean CheckM completeness was nearly the same in the two cohorts: 94.7% for the anchors and 94.3% for the baseline (d +0.08; p 0.93). The project treats this null result as a critical control and concludes that the size difference cannot be a MAG-quality artefact. On the evidence presented, the matched completeness weakens a quality artefact as an explanation for the genome-size difference [src: bacillota_b_subsurface_accessory].

The project's H2 analysis table has 6 rows. It applies Wilcoxon tests and Cohen's d to genome size, OG count, GC, and CheckM measures. These findings feed [[concepts/subsurface-bacillota-specialization]] [src: bacillota_b_subsurface_accessory].

## Use in clay-confined subsurface cohorts

The clay-confined subsurface project built its cohorts from [[entities/kbase-ke-pangenome]] NCBI environment metadata. It selected genomes whose isolation_source or env_* fields contained clay-related keywords, then joined them to the pangenome by biosample ID. The final cohorts were filtered at CheckM ≥80% completeness and ≤5% contamination [src: clay_confined_subsurface].

Quality filtering shrank the deep-anchor cohort from 9 genomes to 6. Before filtering, this cohort held 8 [[entities/mont-terri]] Opalinus borehole genomes (BRC-3 + BIC-A1) and 1 bentonite-formation genome. Because so few genomes remain after filtering, results for this cohort rest on a very small sample [src: clay_confined_subsurface].

The project's self-sufficiency test compared mean counts of complete GapMind amino-acid pathways between cohorts. After CheckM ≥80 filtering, the 6 deep anchors had a lower mean count than the 137 baseline genomes: 15.50 versus 17.14 (d=−0.84, p=0.009). The 30 shallow anchors had a higher mean count than the same 137 baseline genomes: 17.87 versus 17.14 (d=+0.43, p=0.029). These comparisons bear on [[concepts/biosynthetic-self-sufficiency-and-cultivation]] [src: clay_confined_subsurface].

The project gives two caveats for these pathway counts. First, the 18-pathway GapMind universe creates a ceiling effect: most cultured organisms, deep or shallow, reach 17–18/18 regardless of habitat, which leaves little room for a positive signal at the upper end. Second, the cultured cohort lacks the extreme self-sufficient lineages described in the literature, which are typically uncultivated and recovered as MAGs or single-cell genomes [src: clay_confined_subsurface].

The figure h1_self_sufficiency_violin.png shows how the counts of complete amino-acid pathways are distributed in each cohort, both before and after CheckM filtering [src: clay_confined_subsurface].

## Caveats

CheckM filtering and rescaling correct for differences in genome completeness. On their own, they do not show that the remaining contrasts in genome content are biological [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].

Only the Bacillota B project reports matched mean CheckM completeness between the cohorts it compares, and uses that match as evidence against a quality artefact. The clay-confined project reports quality filtering, not a comparison of completeness between cohorts [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].
