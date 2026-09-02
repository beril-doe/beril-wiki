---
type: "Organism"
description: "Bacillota_B lineages compared across deep-clay and soil habitats"
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md"]
---
# Bacillota_B lineages compared across deep-clay and soil habitats

## What this entity is

**Canonical name:** Bacillota_B lineages. [src: bacillota_b_subsurface_accessory]

**Known aliases:** Bacillota B; Bacillota_B. [src: bacillota_b_subsurface_accessory]

**Stable external identifier:** No stable external identifier is specified in the source reports. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

This entity represents Bacillota_B lineages compared between deep-clay subsurface habitats and soil or sediment baseline habitats in the [[summaries/bacillota_b_subsurface_accessory__REPORT]] and [[summaries/clay_confined_subsurface__REPORT]]. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

## Evidence from deep-clay comparisons

The BERDL Bacillota_B pangenome contained 334 genomes, substantially fewer than the v1.1 planning estimate of 6,700 genomes. [src: bacillota_b_subsurface_accessory]

The earlier deep-clay anchor cohort contained 10 genomes from [[entities/mont-terri]] Opalinus borehole and rock-porewater samples plus 2 Russian [[entities/beyelii-yar]] borehole genomes, while its soil-baseline cohort contained 62 phylum-matched soil or sediment genomes. [src: bacillota_b_subsurface_accessory]

In the newer clay-confined analysis, the deep cohort comprised 9 genomes before quality filtering, including 8 Mont Terri Opalinus borehole genomes and 1 bentonite-formation genome; the phylum-stratified soil baseline comprised 150 genomes before filtering and 137 afterward. [src: clay_confined_subsurface]

Across 14,109 Firmicutes-level eggNOG orthologous groups, a Fisher’s exact test with Benjamini–Hochberg false-discovery-rate correction, a fold-difference threshold of ≥3, and a minimum of ≥3 positive anchor genomes identified 547 significantly enriched groups at q<0.05. [src: bacillota_b_subsurface_accessory]

The enriched set included 42 anaerobic-respiration groups, 24 sporulation-revival groups, 12 mineral-attachment or exopolysaccharide groups, 4 anaerobic-regulator groups, and 3 osmoadaptation groups; 462 groups were categorized as other or unannotated by the keyword scan. [src: bacillota_b_subsurface_accessory]

Manual inspection suggested that the true anaerobic-respiration-related total was closer to 80–100 of the 547 enriched groups because the other or unannotated category included electron-transfer functions. [src: bacillota_b_subsurface_accessory]

Deep-clay anchor genomes had a mean genome size of 4,110,038 bp versus 3,046,124 bp for soil-baseline genomes, with Cohen’s d=+1.39 and Mann–Whitney p=0.025. [src: bacillota_b_subsurface_accessory]

CheckM-rescaled mean genome sizes were 4,323,230 bp for anchors and 3,233,715 bp for baselines, with Cohen’s d=+1.37 and p=0.013. [src: bacillota_b_subsurface_accessory]

Mean eggNOG orthologous-group counts were 2,630 in anchors versus 2,106 in baselines, with Cohen’s d=+1.30 and p=0.022; CheckM-rescaled counts were 2,771 versus 2,233, with Cohen’s d=+1.32 and p=0.009. [src: bacillota_b_subsurface_accessory]

Mean GC content was 48.84% in anchors versus 47.76% in baselines, with Cohen’s d=+0.21 and p=0.44. [src: bacillota_b_subsurface_accessory]

Mean CheckM completeness was 94.7% for anchors and 94.3% for baselines, with Cohen’s d=+0.08 and p=0.93, indicating that the larger anchor genomes and higher orthologous-group counts were not explained by a genome-quality difference in this comparison. [src: bacillota_b_subsurface_accessory]

These results **support** a self-sufficiency model for cultivable deep-clay Bacillota_B and **contrast** with streamlining reported for Patescibacteria, although the source cautions that these groups differ ecologically and phylogenetically. [src: bacillota_b_subsurface_accessory]

The newer study **qualifies** that interpretation: its GapMind 18-pathway amino-acid completeness metric was not elevated in the deep cohort, which had mean 16.22/18 versus 16.66/18 for the baseline unfiltered (Mann–Whitney p=0.153; Cohen’s d=−0.17) and 15.50/18 versus 17.14/18 after quality filtering (p=0.009; d=−0.84). [src: clay_confined_subsurface]

Within Bacillota_B, deep genomes had mean completeness 16.50 versus 16.79 for baseline genomes, with p=0.073 and d=−0.13; this **refines** rather than wholly rejects the earlier genome-expansion result because the 18-pathway metric may saturate near 18 and does not test every form of genomic self-sufficiency. [src: clay_confined_subsurface]

## Anaerobic toolkit and corrected multi-heme cytochrome comparison

The earlier corrected multi-heme cytochrome detector combined PFAM PF02085, PFAM PF22678, and a CXXCH heme-binding motif count of ≥4 in gene-cluster protein sequences; a genome was positive if any signal was present. [src: bacillota_b_subsurface_accessory]

Under that corrected detector, 5/9 deep-cohort genomes were positive, or 55.6%, compared with 1/9, or 11.1%, under the original marker set; shallow-cohort results were 12/30, or 40.0%, corrected versus 15/30, or 50.0%, originally; and soil-baseline results were 61/149, or 40.9%, corrected versus 30/149, or 20.1%, originally. [src: bacillota_b_subsurface_accessory]

Corrected pairwise Fisher tests found no significant cohort differences: deep versus shallow had odds ratio 1.88 and p=0.46; deep versus baseline had odds ratio 1.80 and p=0.49; and shallow versus baseline had odds ratio 0.96 and p=1.0. [src: bacillota_b_subsurface_accessory]

This correction **contradicts** the original shallow-enrichment narrative and indicates that corrected multi-heme cytochrome content was similar across the clay cohorts and soil baseline. [src: bacillota_b_subsurface_accessory]

The sulfite-reduction-side finding remained supported: 5/9 deep-cohort genomes were positive versus a Mitzscherling rock-attached null rate of 0.2%, with binomial p=4×10⁻¹². [src: bacillota_b_subsurface_accessory]

The clay-confined analysis **supports and sharpens** the anaerobic interpretation: the combined Wood–Ljungdahl, group 1 [NiFe]-hydrogenase, and dissimilatory sulfate-reduction toolkit had mean scores of 1.889 for deep genomes, 0.033 for shallow genomes, and 0.393 for the soil baseline, while all three modules occurred in 0.556, 0.000, and 0.021 of those cohorts, respectively. [src: clay_confined_subsurface]

Within Bacillota_B, Wood–Ljungdahl was present in 5/5 deep genomes versus 15/19 baseline genomes (p=0.54; p_BH=0.54, with 1.0 reported in the within-phylum table), and group 1 [NiFe]-hydrogenase in 5/5 versus 14/19 (p=0.54; p_BH=0.54, with 1.0 reported); sulfate reduction occurred in 5/5 versus 4/19, with odds ratio ∞, p=0.003, and p_BH=0.044. [src: clay_confined_subsurface]

Thus, the newer data **refine** the earlier functional-specialization model: Wood–Ljungdahl and [NiFe]-hydrogenase enrichment primarily tracks Bacillota_B phylogeny, whereas sulfate reduction remains enriched after the within-phylum control. [src: clay_confined_subsurface]

## Functional and taxonomic context

The deep-clay cohort was enriched for functions associated with anaerobic respiration, sporulation and germination, mineral attachment or exopolysaccharide production, anaerobic regulation, osmoadaptation, biofilm and capsule formation, two-component systems, and potassium uptake. [src: bacillota_b_subsurface_accessory]

The cohort spanned Syntrophomonadales, Desulfitobacteriales, Moorellales, Thermacetogeniales, Ammonifexales, Carboxydocellales, Desulfotomaculales, Heliobacteriales, and Thermincolales in the phylum-matched soil or sediment comparison. [src: bacillota_b_subsurface_accessory]

The anchor genomes were distributed among 3 BRH-c8a genomes, 2 BRH-c4a genomes, 2 Desulfosporosinus genomes, Desulforudis, Ch130, and 1 other genome, so some enriched orthologous groups may be lineage markers rather than recurrent subsurface-specialization features. [src: bacillota_b_subsurface_accessory]

The newer cohort included Desulfosporosinus, BRH-c8a, BRH-c4a, Lutibacter, BRH-c54, Roseovarius, and Stenotrophomonas lineages, with 8 Opalinus genomes traced to BRC-3 or BIC-A1 borehole isolation sources. [src: clay_confined_subsurface]

The source therefore **qualifies** the subsurface-specialization interpretation: the anchor cohort was borehole- and porewater-dominated, contained 10 genomes versus 62 baselines in the earlier comparison, and could not test whether rock-attached Bacillota_B differ in gene content. [src: bacillota_b_subsurface_accessory]

The newer study further **refines** the habitat interpretation by finding that the cultured deep cohort matches the Bagnoud Mont Terri porewater paradigm rather than demonstrating representation of the rock-attached community; rock-attached Geobacter and Geothrix lineages and CPR/DPANN episymbionts are essentially absent from the cultured cohort. [src: clay_confined_subsurface]

## Related pages

- [[concepts/subsurface-bacillota-specialization]] — synthesis of deep-clay Bacillota_B functional specialization and genome expansion. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
- [[concepts/pangenome-integration]] — within-lineage orthologous-group enrichment, cohort construction, and pangenome limitations. [src: bacillota_b_subsurface_accessory]
- [[concepts/multi-heme-cytochrome-detection]] — corrected marker logic and the loss of the original iron-reduction contrast. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
- [[concepts/metabolic-model-gapfilling]] — GapMind pathway completeness and the limits of the self-sufficiency metric. [src: clay_confined_subsurface]
- [[summaries/bacillota_b_subsurface_accessory__REPORT]] — source-project summary. [src: bacillota_b_subsurface_accessory]
- [[summaries/clay_confined_subsurface__REPORT]] — source-project summary. [src: clay_confined_subsurface]
