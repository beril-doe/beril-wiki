# Subsurface and Soil Community Ecology

This hub covers what structures microbial communities in groundwater, sediments, clay formations and layered soils. The corpus addresses five candidate drivers:

- physical position (depth zone or soil horizon);
- contaminant load;
- prior environmental history;
- long-term warming;
- lineage-level genome specialization.

The evidence comes from Oak Ridge groundwater and sediment surveys, a long-term soil-warming site, cultured deep-clay genomes, a global soil-sample analysis and a two-round carbon enrichment experiment [src: lab_field_ecology, enigma_sso_asv_ecology, harvard_forest_warming, clay_confined_subsurface, soil_frontier_genomics, lignin_community_enrichment]. Most claims rest on one site or one project. This page states that limit claim by claim, so readers can tell what is measured from what is hypothesis.

## Literature Context

The candidate literature broadly holds that environmental gradients act as deterministic filters on microbial communities. In the East China Sea, spatial gradients acted as a deterministic filter on microbiome organization. Depth was among the factors shaping microbial distribution and co-occurrence, and seawater communities were more robust than sediment communities ([PMID 37783325](https://pubmed.ncbi.nlm.nih.gov/37783325/)). In Arctic Cryosols, 83 samples from four soil horizons showed that the abundance of bacteria and diazotrophs (nitrogen-fixing microorganisms) decreased from topsoil to permafrost. The exception was cryoOM, topsoil organic matter that cryoturbation had translocated into deeper horizons. CryoOM did not follow this decline and was enriched in oligotrophic (slow-growing) taxa ([PMID 33452882](https://pubmed.ncbi.nlm.nih.gov/33452882/)). Reviews describe soil and crop community assembly as a balance of deterministic and stochastic processes whose weight depends on environmental conditions ([PMID 36184075](https://pubmed.ncbi.nlm.nih.gov/36184075/)). A global synthesis of arbuscular mycorrhizal fungal communities found patterns more consistent with habitat filtering and stochastic processes than with resource competition ([PMID 35582944](https://pubmed.ncbi.nlm.nih.gov/35582944/)).

The corpus's zonation results are **consistent** with this literature. At the SSO site, hydrogeological zone explained 27.5% of sediment variance, while well identity was not significant. At Harvard Forest, soil horizon explained R²=30.6% (p=0.0002), and the warming term was not significant (R²=7.6%, p=0.069). However, every organic DNA sample there was lab-incubated and every mineral DNA sample was direct, so horizon cannot be cleanly separated from incubation. With that caveat, both results fit the view that vertical compartments are primary filters, as discussed in [[concepts/subsurface-hydrogeological-zonation]] and [[concepts/soil-horizon-response-heterogeneity]]. The corpus **extends** that view to a contaminated aquifer and a long-term warming manipulation. Two further limits apply. The SSO inferences rest on composition alone, and the Arctic study is a survey from one island, not a treatment comparison.

History-dependent assembly is also anticipated by the literature. A review of priority effects argues that the order and timing of arrival can shape community composition across soil, freshwater, plant and gut systems, and that historical contingency remains poorly understood relative to deterministic drivers ([PMID 34453137](https://pubmed.ncbi.nlm.nih.gov/34453137/)). The lignin enrichment result, where Round-1 history explained 58.9% of Round-2 bacterial variance against 32.7% for the current carbon source, gives a quantitative instance of this contingency, described in [[concepts/ecological-memory]]. However, the corpus did not test the priority-effect mechanism, and the fungal history term was not detected (p=0.090). The literature therefore offers a plausible explanation rather than a confirmed one.

On genome architecture, the corpus sits partly **in tension** with groundwater literature. Filtered groundwater yielded diverse candidate-phyla bacteria with consistently small cells (0.009±0.002 μm³). These cells had inferred missing biosynthetic capacities, which the authors associated with cell and genome size minimization ([PMID 25721682](https://pubmed.ncbi.nlm.nih.gov/25721682/)). The cultured deep-clay Bacillota_B genomes in [[concepts/subsurface-bacillota-specialization]] were instead larger, consistent with self-sufficiency. The two observations concern different lineages and different isolation biases (cultivation versus size filtration), so they need not conflict. Still, they caution against reading "subsurface" as implying a single genomic strategy.

In seagrass roots, genera more abundant in stressed plants were dominated by putative sulphur-cycling bacteria, including putative sulphate reducers ([PMID 31841144](https://pubmed.ncbi.nlm.nih.gov/31841144/)). That taxonomic association, inferred from 16S composition rather than measured activity, is consistent with sulfate reduction marking a redox niche. It comes from a different habitat, however, and does not bear directly on the deep-clay cohort.

## What the Corpus Shows

**Physical position outranks treatment as a structuring axis.**

At the SSO subsurface site, the project analyzed 16S amplicon sequence variants (ASVs, exact-sequence taxon proxies). It tested sediment communities with PERMANOVA (permutational multivariate analysis of variance, which partitions community-dissimilarity variance among factors):

- Hydrogeological zone explained 27.5% of variance (F = 4.05, p = 0.0001) [src: enigma_sso_asv_ecology].
- Well identity explained 19.2% and was not significant (F = 0.80, p = 0.979) [src: enigma_sso_asv_ecology].
- Firmicutes were enriched with depth (Spearman ρ = +0.76) and Chloroflexi toward shallow depths (ρ = −0.73) [src: enigma_sso_asv_ecology].

At [[entities/harvard-forest]], the soil-warming site shows the same pattern [src: harvard_forest_warming]:

- Soil horizon explained R²=30.6% (p=0.0002) [src: harvard_forest_warming].
- Warming treatment explained R²=7.6% (p=0.069) [src: harvard_forest_warming].
- Warming fold changes per KO (KEGG Orthology functional gene group) correlated only weakly between horizons, for example DNA Pearson r=0.075 [src: harvard_forest_warming].

These two independent projects **support** the reading in [[concepts/subsurface-hydrogeological-zonation]] and [[concepts/soil-horizon-response-heterogeneity]]: vertical compartments are primary axes of structure, not covariates to average over. That stratified compartments must be analysed separately rather than pooled remains a hypothesis; the Harvard Forest project did not test pooling directly [src: harvard_forest_warming].

Habitat also partitions communities within a single well. Groundwater and sediment from the same well had median Bray–Curtis dissimilarity (a 0–1 compositional distance) = 0.424 [src: enigma_sso_asv_ecology].

**Contaminants appear to select taxa, but the axis is entangled with others.**

[[concepts/contaminant-selection-of-subsurface-communities]] rests on one project. Oak Ridge groundwater sites split at the median [[entities/uranium]] concentration showed distinct compositions, with rare-biosphere taxa and subsurface specialists more prominent at contaminated sites [src: lab_field_ecology]. The report gave no test statistic or confound control [src: lab_field_ecology]. It explains *Rhodanobacter* dominance through published acid-plus-metal inhibition of other taxa, which is an extrapolation, not a measurement here [src: lab_field_ecology].

The SSO study adds supporting context. *Rhodanobacter* was enriched in groundwater (sediment 1.23%, groundwater 3.62%) [src: enigma_sso_asv_ecology]. The report also attributes depth zonation to a contamination plume confined to the saturated zone [src: enigma_sso_asv_ecology].

**History can outweigh current conditions.**

In a two-round lignin enrichment, bacterial 16S communities were tested by PERMANOVA [src: lignin_community_enrichment]:

- Round-1 carbon history explained 58.9% of Round-2 variance (F=14.31, R²=0.589, p=0.002) [src: lignin_community_enrichment].
- The current Round-2 carbon source explained 32.7% (F=4.85, R²=0.327, p=0.018) [src: lignin_community_enrichment].
- Communities with different histories did not converge under identical conditions [src: lignin_community_enrichment].

This is [[concepts/ecological-memory]]: legacy composition persists after the environment changes [src: lignin_community_enrichment]. The result holds for bacteria only. The fungal ITS2 (internal transcribed spacer, a fungal barcode) history term was not detected (p=0.090) [src: lignin_community_enrichment]. The report links non-convergence to priority effects, in which earlier-established taxa shape later assembly, as a hypothesis; it did not measure that mechanism [src: lignin_community_enrichment].

**Warming leaves a narrow but real compositional signal.**

In the organic horizon at Harvard Forest, two phylum shifts passed false discovery rate (FDR, the expected share of false positives among significant calls) correction, both narrowly [src: harvard_forest_warming]:

- Actinobacteria rose from 0.249 to 0.315 (log2 FC, the log2 fold change from control to heated, +0.341; q, the FDR-adjusted p-value, =0.049) [src: harvard_forest_warming].
- Acidobacteria fell from 0.035 to 0.024 (log2 FC −0.549, q=0.049) [src: harvard_forest_warming].

The functional layers in [[concepts/long-term-soil-warming-microbial-response]] are weaker [src: harvard_forest_warming]:

- Carbon-cycling KO enrichment appeared only in the DNA × organic pool, where incubation is confounded with warming: OR (odds ratio)=2.78, p=0.042, resting on five KOs; the other pools showed no enrichment [src: harvard_forest_warming].
- Methanotrophy and glyoxylate-shunt transcript signals are nominal only and do not survive FDR [src: harvard_forest_warming].
- Heated mineral soil showed lower detectable metabolite richness, counted as detected ChEBI (Chemical Entities of Biological Interest) entities: 155 vs 167, p=0.012 [src: harvard_forest_warming].

The report's "warming-activated ruderal subset" is explicitly a hypothesis [src: harvard_forest_warming].

**Selected cultivable deep-clay Bacillota_B genomes are larger, not streamlined.**

[[concepts/subsurface-bacillota-specialization]] compares 10 deep-clay with 62 soil-baseline Bacillota_B genomes. It found 547 significantly enriched orthologous groups (OGs, clusters of related proteins) at q<0.05 [src: bacillota_b_subsurface_accessory]. Deep-clay genomes were larger, which is consistent with a self-sufficiency model [src: bacillota_b_subsurface_accessory].

Dissimilatory sulfate reduction (SR, the [[entities/dissimilatory-sulfate-reduction]] pathway) was the most robust marker [src: clay_confined_subsurface]:

- Deep cohort versus soil baseline: 5/9 versus 5/140, OR = 33.8, p_BH (p-value adjusted by Benjamini–Hochberg false-discovery-rate correction) = 2.5×10⁻⁴ [src: clay_confined_subsurface].
- Within Bacillota_B: 5/5 versus 4/19, p_BH = 0.044 [src: clay_confined_subsurface].

By contrast, enrichments of Wood–Ljungdahl (the reductive acetyl-CoA pathway for CO₂ fixation) and group 1 [NiFe]-hydrogenase markers did not survive within-phylum control [src: clay_confined_subsurface]. This genomic evidence **refines** the SSO redox interpretation. It supports anaerobic potential in deeper lineages but does not demonstrate activity in any zone [src: bacillota_b_subsurface_accessory].

## Tensions and Caveats

**Inference versus measurement.**

The SSO report says all findings converge on a NE→SW contamination-plume model. It proposes that the U3–M6–L7 corridor of similar communities maps subsurface hydrology [src: enigma_sso_asv_ecology]. The same report concedes that every environmental inference comes from community composition alone and awaits geochemical confirmation [src: enigma_sso_asv_ecology]. Procrustes correspondence, which tests how well the community ordination (a low-dimensional map of compositional distances) can be rotated onto the physical well grid, was marginal (m² = 0.379, p = 0.080) [src: enigma_sso_asv_ecology].

**Compartment bias.**

The cultured deep-clay cohort matches a porewater-associated signal rather than demonstrating representation of the rock-attached community; compartment annotations were inferred from isolation-source keywords, so some entries could represent either [src: clay_confined_subsurface]. At [[entities/mont-terri]], sulfate reducers dominate porewater, while [[entities/geobacter]]/geothrix iron reducers dominate rock surfaces [src: discoveries]. A sulfate-reduction signal therefore should not be read as whole-site zonation [src: discoveries, clay_confined_subsurface].

**Local versus global clay effects.**

Across 5,441 soil samples, measured stressors did not predict functional gene counts out of sample. Low-clay cross-validation R² = −0.268 versus high-clay R² = −0.292; the 95% CI of the difference (−0.423, 0.161) includes zero [src: soil_frontier_genomics]. This does not contradict the lineage-level Bacillota_B result. It does limit generalizing that result to a globally predictable clay effect [src: soil_frontier_genomics].

**Confounds that cannot be separated with current data.**

- Uranium selection cannot be separated from low pH, co-occurring metals or hydrogeological zone [src: lab_field_ecology].
- At Harvard Forest, every organic DNA sample was lab-incubated and every mineral DNA sample was direct, so horizon and incubation are mixed [src: harvard_forest_warming].
- The curated carbon-cycling KO list was **not** enriched among horizon-specific KOs (OR<1, p>0.87). Horizon heterogeneity may therefore lie mostly outside the categories that motivate warming studies [src: harvard_forest_warming].

**Small and clustered cohorts.**

The 10 Bacillota_B anchors are phylogenetically clumped, so some enriched OGs may be lineage markers rather than subsurface signatures [src: bacillota_b_subsurface_accessory]. The report also states that 3 *Desulfosporosinus* genomes contributed to the sporulation signal, but its own anchor list gives 2. That discrepancy is unresolved [src: bacillota_b_subsurface_accessory].

**Bacteria versus fungi.**

Fungal ITS replicates were highly inconsistent. Within-group Bray–Curtis reached 0.99–1.00 for several Round-2 groups, versus 0.09 for 16S, so fungal memory is not established [src: lignin_community_enrichment].

## Where to Go Deeper

- [[concepts/subsurface-hydrogeological-zonation]] — the fullest spatial analysis: depth zones, habitat partitioning, the inferred flow corridor and redox ladder.
- [[concepts/soil-horizon-response-heterogeneity]] — the soil analogue of zonation, with the incubation confound laid out.
- [[concepts/contaminant-selection-of-subsurface-communities]] — proposals to replace the uranium median split with continuous-gradient ordination.
- [[concepts/subsurface-bacillota-specialization]] — genome-level evidence for anaerobic persistence and its phylogenetic controls.
- [[concepts/long-term-soil-warming-microbial-response]] — how composition, gene content, transcripts and metabolites differ in evidential strength.
- [[concepts/ecological-memory]] — the quantitative case for history-dependent assembly and its bacterial-only scope.

Key entities: [[entities/permanova]], [[entities/16s-amplicon-sequencing]], [[entities/dissimilatory-sulfate-reduction]], [[entities/geobacter]], [[entities/eggnog]], [[entities/rhodanobacter]], [[entities/harvard-forest]], [[entities/mont-terri]], [[entities/uranium]].

Reports: [[summaries/enigma_sso_asv_ecology__REPORT]], [[summaries/lab_field_ecology__REPORT]], [[summaries/harvard_forest_warming__REPORT]], [[summaries/lignin_community_enrichment__REPORT]], [[summaries/bacillota_b_subsurface_accessory__REPORT]], [[summaries/clay_confined_subsurface__REPORT]], [[summaries/soil_frontier_genomics__REPORT]].
