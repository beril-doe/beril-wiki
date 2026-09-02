---
type: "Dataset"
description: "COG-based functional categories for comparing microbial gene content and ecology"
sources: ["summaries/cog_analysis__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/ecotype_functional_differentiation__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
---
# COG Functional Categories

## What this entity is

**Canonical name:** COG functional categories  
**Known aliases:** Clusters of Orthologous Groups; COG categories; COG functional classification  
**Stable external identifier:** Not reported in the source. [src: cog_analysis]

COG functional categories classify genes by broad orthologous-group functions, including mobile elements, defense mechanisms, translation, nucleotide metabolism, coenzyme metabolism, amino acid metabolism, and energy production. [src: cog_analysis]

The [[summaries/cog_analysis__REPORT]] analysis used COG functional categories to examine 357,623 genes from 32 species spanning 9 phyla. [src: cog_analysis] The [[summaries/ecotype_functional_differentiation__REPORT]] analysis extends this use to within-species gene-content ecotypes, comparing COG profiles for 1,820 genomes across 12 species. [src: ecotype_functional_differentiation] The [[summaries/core_gene_tradeoffs__REPORT]] analysis refines the interpretation of conserved functional categories by showing that conservation does not uniformly imply low laboratory burden: the direction and magnitude of burden vary by function and condition. [src: core_gene_tradeoffs]

The [[summaries/enigma_contamination_functional_potential__REPORT]] analysis further used eggNOG-derived COG-fraction proxies to summarize inferred functional potential across 108 ENIGMA samples. [src: enigma_contamination_functional_potential] This **refines** the adaptive interpretation: broad COG summaries did not show a robust genus-level monotonic association between contamination and community defense potential, even though coverage-aware exploratory models detected defense associations sensitive to mapping mode, coverage, covariates, and multiple-testing correction. [src: enigma_contamination_functional_potential]

The [[summaries/soil_metal_functional_genomics__REPORT]] analysis adds an environmental-chemistry application: across 51,748 soil samples and nine metals, it identified 2,355 significant COG–metal associations at FDR < 0.05, with transporters and biosynthesis genes prominent among the top hits. [src: soil_metal_functional_genomics] This **supports** using COG profiles to detect environment-associated functional shifts, but **refines** the interpretation of broad defense and adaptive categories because the associations are observational and may reflect co-contamination rather than metal-specific functions. [src: soil_metal_functional_genomics]

## Key facts from cog_analysis

- Novel or singleton genes were enriched in COG L, mobile elements, by **+10.88%**, with **100% consistency** across species; this was the strongest reported signal. [src: cog_analysis]
- Novel or singleton genes were enriched in COG V, defense mechanisms, by **+2.83%**, with **100% consistency**. [src: cog_analysis]
- Novel or singleton genes were enriched in COG S, unknown function, by **+1.64%**, with **69% consistency**. [src: cog_analysis]
- Core genes were depleted relative to novel or singleton genes in COG J, translation, by **-4.65%**, with **97% consistency**; this was the strongest reported depletion. [src: cog_analysis]
- Core genes were also depleted in COG F, nucleotide metabolism, by **-2.09%** with **100% consistency**; COG H, coenzyme metabolism, by **-2.06%** with **97% consistency**; COG E, amino acid metabolism, by **-1.81%** with **81% consistency**; and COG C, energy production, by **-1.75%** with **88% consistency**. [src: cog_analysis]
- The analysis interpreted core genes as forming a conserved metabolic and housekeeping engine, while novel genes were associated with mobile elements, defense, unknown functions, ecological adaptation, and niche-specific functions. [src: cog_analysis]
- The report interpreted horizontal gene transfer (HGT), the movement of genetic material between lineages, as the primary innovation mechanism and treated the **+10.88%** enrichment of COG L as evidence that mobile elements may account for much genomic novelty. [src: cog_analysis]
- All **8** predictions from the initial *N. gonorrhoeae* analysis were reported as confirmed across the 32-species comparison. [src: cog_analysis]

The ecotype analysis **supports and broadens** the adaptive interpretation: across 257 chi-square or Fisher’s exact tests, 170 tests (**66.1%**) showed COG differentiation between ecotypes after BH-FDR (Benjamini–Hochberg false-discovery-rate) correction at q < 0.05, and all 12 analyzed species had at least one differentiated category. [src: ecotype_functional_differentiation] Categories E (amino acid metabolism), S (unknown function), and V (defense) differentiated in **11/12** species, while G (carbohydrate metabolism) differentiated in **10/12** species. [src: ecotype_functional_differentiation] The strong recurrence of S, V, and E differences **supports** the earlier association of novel or variable genes with unknown, defense, and ecological functions, but the result concerns within-species ecotypes rather than the core-versus-novel comparison. [src: ecotype_functional_differentiation]

Adaptive categories V, P, G, E, Q, M, and K had a significance rate of **79.8% (67/84)** versus **68.8% (33/48)** for housekeeping categories J, F, H, and C; their mean effect size was **0.0136** versus **0.0064**, and a one-sided Mann–Whitney U test gave **p = 2.53 x 10^-6**. [src: ecotype_functional_differentiation] This **refines** the prior housekeeping-engine interpretation: housekeeping functions also differentiate, but adaptive categories show larger proportional shifts between ecotypes. [src: ecotype_functional_differentiation]

The ecotype analysis further found that S had the largest mean effect size, **0.0392**, and L the second largest, **0.0337**; S was significant in **11/12** species and L in **9/12**. [src: ecotype_functional_differentiation] This **supports** the existing emphasis on unknown functions and mobile elements as major sources of pangenome variation, while the small effects and lack of phylogenetic controls mean that ecological adaptation remains a hypothesis rather than an isolated causal conclusion. [src: ecotype_functional_differentiation]

The soil-metal study **refines** the interpretation of category-level shifts by showing that metal-associated patterns are environment-dependent: biome-stratified PGLS (phylogenetic generalized least squares, a regression method accounting for phylogenetic relationships) found distinct metal–COG relationships in soil, marine, and wastewater environments rather than a universal resistance programme. [src: soil_metal_functional_genomics] Its copper-specific analysis found positive associations with cell division and nucleotide transport categories BQ, FQ, and FK and negative associations with energy-production categories DI and CE, suggesting—but not establishing—energetic trade-offs under copper stress. [src: soil_metal_functional_genomics]

The core-gene trade-off analysis **refines** the housekeeping-engine interpretation: core genes were more burdensome than non-core genes in Protein Metabolism, Motility, and RNA Metabolism by **+6.2 percentage points**, **+7.8 percentage points**, and **+12.9 percentage points**, respectively, whereas non-core Cell Wall genes were more burdensome by **14.1 percentage points** (a difference of **-14.1 percentage points**). [src: core_gene_tradeoffs]

The same analysis identified **25,271** true trade-off genes, or **17.8%** of genes examined; these genes were **1.29** times more likely to be core than non-core, with an odds ratio of **1.29** and **p=1.2e-44**. This **supports** treating conserved functions as conditionally active rather than uniformly inert, while the result remains based on laboratory fitness and conservation rather than direct measurement of selection in nature. [src: core_gene_tradeoffs]

## Composite categories

Composite COG assignments containing multiple functional letters were treated as biologically meaningful rather than annotation artifacts. [src: cog_analysis]

The LV composite, representing mobile and defense functions, showed **+0.34% enrichment** with **76% consistency** and was interpreted as evidence for multifunctional modules such as mobile defense islands. [src: cog_analysis]

Composite categories were counted once per gene rather than split across their component letters, and the report recommends retaining them in downstream analyses. [src: cog_analysis]

## Annotation context and limitations

COG annotations covered approximately **70%** of genes, so unassigned genes may skew the observed distributions. [src: cog_analysis] In the ecotype analysis, approximately **38%** of gene clusters had COG annotations, leaving **62%** unannotated; this **qualifies** the broader ecotype result because unannotated ecotype-specific genes may be missed. [src: ecotype_functional_differentiation]

The ENIGMA analysis **supports this qualification**: COG-fraction proxies are coarse summaries rather than curated metal-resistance pathways, and its contamination analysis did not establish broad stress or defense shifts at genus resolution. [src: enigma_contamination_functional_potential] Its exploratory defense signal was significant in a relaxed coverage-adjusted model (beta = **0.000751**, 95% bootstrap CI **[0.000224, 0.001779]**, p = **0.000398**, FDR q = **0.0462**) but not robust across the strict mapping mode after global FDR; within-fraction tests were non-significant. [src: enigma_contamination_functional_potential] Thus, the earlier COG-based adaptive patterns **cannot be assumed** to represent curated contamination-resistance functions, and pathway-level analyses remain needed. [src: enigma_contamination_functional_potential]

The soil-metal analysis provides a further limitation: its conditional db-RDA (distance-based redundancy analysis) model reported R² = **0.799** and p = **0.005** with 999 permutations after conditioning on batch and project effects, but an unconditional metal-only R² was not reported. [src: soil_metal_functional_genomics] The 2,355 discoveries among 3,915 implied tests may also have an inflated true FDR because co-varying metals make tests non-independent, and systematic effect-size, spatial-autocorrelation, partial-correlation, and proximity-sensitivity validation remains pending. [src: soil_metal_functional_genomics] These caveats **contradict** any interpretation of the soil associations as already demonstrating metal-specific resistance functions; the report specifically proposes partial correlation and further spatial validation. [src: soil_metal_functional_genomics]

The analysis used **32 species**, and a larger sample could reveal phylum-specific patterns that were not visible in the comparison. [src: cog_analysis] The ecotype study analyzed 12 species from a stratified 15-species sample drawn from 456 eligible species, so its functional differentiation result should not be generalized to all species without further testing. [src: ecotype_functional_differentiation]

The analysis used [[entities/eggnog]] v6 annotations, which may differ from original COG assignments. [src: cog_analysis] The ecotype study also used PCA followed by KMeans clustering and lacked within-species phylogenetic controls, so category differences may partly reflect clustering assumptions or phylogenetic structure rather than ecology. [src: ecotype_functional_differentiation] The ENIGMA analysis likewise faced incomplete and ambiguous pangenome mapping: 862 of 1,392 observed genera were unmapped, while 380 mapped genera were multi-clade genera. [src: enigma_contamination_functional_potential]

The trade-off findings are also limited by laboratory-condition coverage: “burden” defined as fit > 1 may reflect condition-specific trade-offs rather than true dispensability, and the Fitness Browser conditions are biased toward experimentally convenient environments. [src: core_gene_tradeoffs]

## Related pages

- [[concepts/pangenome-integration]] — COG distributions provide a functional interpretation of conserved and novel bacterial pangenome genes; the ecotype analysis adds within-species functional differentiation, while the ENIGMA analysis tests the limits of broad COG proxies across pangenome mappings. [src: cog_analysis] [src: ecotype_functional_differentiation] [src: enigma_contamination_functional_potential]
- [[concepts/ecotype-environment-gene-content]] — COG profiles show that gene-content ecotypes are functionally differentiated, while environmental and phylogenetic causes remain unresolved; the ENIGMA analysis further indicates that broad functional shifts may require finer taxonomic resolution. [src: ecotype_functional_differentiation] [src: enigma_contamination_functional_potential]
- [[concepts/environmental-resistome]] — The ENIGMA results **refine** interpretation of COG V and other broad defense proxies by distinguishing exploratory contamination-linked signals from robust evidence for an environmental resistome; the soil-metal analysis adds observational metal-associated transporter and biosynthesis shifts but leaves metal specificity unresolved. [src: enigma_contamination_functional_potential] [src: soil_metal_functional_genomics]
- [[concepts/metal-cross-resistance]] — Co-varying chromium, copper, lead, and zinc create a direct test of whether apparent metal associations are metal-specific or reflect multi-metal stress. [src: soil_metal_functional_genomics]
- [[concepts/gene-essentiality]] — The trade-off analysis **supports** distinguishing conservation from laboratory essentiality or burden. [src: core_gene_tradeoffs]
- [[concepts/condition-specific-fitness]] — Function-specific burden and trade-off status vary with environmental condition. [src: core_gene_tradeoffs]
- [[entities/eggnog]] — The annotation source used for the reported COG assignments and ENIGMA-derived functional proxies. [src: cog_analysis] [src: enigma_contamination_functional_potential]
