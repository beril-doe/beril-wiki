---
type: "Summary"
description: "Summary of the project Harvard Forest Long-Term Warming — DNA vs RNA Functional Response."
doc_type: "short"
full_text: "sources/harvard_forest_warming__REPORT.md"
---
# Harvard Forest Long-Term Warming — DNA vs RNA Functional Response

This page summarises a report on the 25-year +5°C soil warming experiment at Harvard Forest Barre Woods. The report asks whether RNA composition shifts more than DNA under warming. It finds a real but modest community-level response that reproduces published results. It does not support the RNA-leads-DNA hypothesis (H1). The data are from one site (n=42 biosamples) and one sampling date. [src: harvard_forest_warming] The report's author is Chris Mungall of Lawrence Berkeley National Laboratory (ORCID 0000-0002-6601-2165). [src: harvard_forest_warming]

## Key Findings

### Community composition
The community shows a real but modest response to warming. [src: harvard_forest_warming] The report reproduces the Actinobacteria-up and Acidobacteria-down findings of DeAngelis et al. 2015. [src: harvard_forest_warming] The site's published compositional warming signal is recoverable from kraken2 read-based taxonomy at q<0.05 in 14+14 samples. [src: harvard_forest_warming] The report states that its organic-horizon signal at q=0.049 directly reproduces the 16S-amplicon and metagenome-based signature from the same Harvard Forest team. [src: harvard_forest_warming]

The phylum analysis is a per-phylum Welch t-test on kraken2 read-based relative abundance, with n=14 control + 14 heated direct samples and BH-FDR (Benjamini-Hochberg false discovery rate) across phyla × horizon. [src: harvard_forest_warming]

Mineral horizon shows no phylum-level changes after FDR. [src: harvard_forest_warming]

Organic-soil results are listed below as control relative abundance, heated relative abundance, log2 FC (fold change) and q (BH).
- Actinobacteria: 0.249, 0.315, +0.341, q 0.049. [src: harvard_forest_warming]
- Acidobacteria: 0.035, 0.024, −0.549, q 0.049. [src: harvard_forest_warming]
- Cyanobacteria: 0.0032, 0.0026, −0.305, q 0.072. [src: harvard_forest_warming]
- Proteobacteria: 0.654, 0.605, −0.111, q 0.088. [src: harvard_forest_warming]
- Verrucomicrobia: 0.0058, 0.0041, −0.513, q 0.088. [src: harvard_forest_warming]

PERMANOVA (permutational multivariate analysis of variance) on Bray-Curtis genus distances gives treatment R²=7.6% (p=0.069). [src: harvard_forest_warming] Horizon gives R²=30.6% (p=0.0002). [src: harvard_forest_warming] The treatment × horizon 4-cell model gives R²=41% (p=0.0002). [src: harvard_forest_warming]

### DNA versus RNA (H1)
H1 proposed that RNA composition shifts more than DNA under warming. The report finds it not supported once a horizon × incubation confound is removed. [src: harvard_forest_warming] The transcript pool is not more sensitive than the genome pool at this sample size and timepoint. [src: harvard_forest_warming] Both pools show ~10-13% treatment R² after the confound is removed. [src: harvard_forest_warming]

In the paired n=25 subset (samples with both DNA and RNA), PERMANOVA pseudo-F for treatment was 3.12 in DNA (R²=11.9%, p=0.020). [src: harvard_forest_warming] A Procrustes alignment test was also run on this subset. [src: harvard_forest_warming]

In the same subset, it was 0.76 in RNA (R²=3.2%, p=0.60). [src: harvard_forest_warming]

That result seemed to contradict H1 in the opposite direction. However, the paired subset confounds horizon with incubation, because every organic sample is incubated and every mineral sample is direct. [src: harvard_forest_warming]

The direct-only sensitivity analysis removes that confound. DNA × mineral has n=14, F=1.75, R²=12.7%, p=0.081. [src: harvard_forest_warming] RNA × mineral has n=11, F=1.15, R²=11.4%, p=0.254. [src: harvard_forest_warming] RNA × organic has n=14, F=1.33, R²=10.0%, p=0.190. [src: harvard_forest_warming]

The report concludes that DNA and RNA pools show comparable treatment R² (10-13%). [src: harvard_forest_warming] It says its H1 sensitivity check indicates the apparent DNA-versus-RNA imbalance is largely a horizon × incubation artifact. [src: harvard_forest_warming] To its knowledge, this is the first explicit paired-sample comparison of DNA-pool and RNA-pool warming-response variance at Harvard Forest. [src: harvard_forest_warming]

The report offers explanations, which are proposals and not measurements:
- Compositional turnover has caught up. The plots have been heated since ~1991, and DeAngelis et al. (2015) and Pold et al. (2016) document strong genome-content shifts at this site. [src: harvard_forest_warming]
- Single-timepoint RNA carries diurnal and microspatial noise. All samples were collected on 2017-05-24. [src: harvard_forest_warming]
- The DNA pool integrates over years, so it is a cleaner readout of the chronic +5°C signal. [src: harvard_forest_warming]
- The metatranscriptome assembly recovered 14,302 distinct KOs (KEGG orthologs) versus 12,863 in the metagenome. [src: harvard_forest_warming] The report proposes that this richer rare-organism repertoire raises per-KO variance and reduces power. [src: harvard_forest_warming]
- Chronic substrate depletion could globally down-regulate the transcriptome. That would leave no preferred axis of treatment-driven RNA variance. [src: harvard_forest_warming]

The comparable-R² verdict does not rule out an early transient where RNA leads DNA. The report argues that the two pools converge in magnitude on multi-decadal timescales. [src: harvard_forest_warming]

### Carbon-cycling genes
Fisher tests asked whether heated-up KOs (q<0.10 and log2 FC above 0) are enriched for a curated 62-KO carbon-cycling list covering CAZymes (carbohydrate-active enzymes), peptidases, TCA (tricarboxylic acid cycle), β-oxidation, aromatic catabolism, methane and C1. [src: harvard_forest_warming] The enrichment test, per-KO differential abundance by pool and horizon, and a direct-sample H1 sensitivity analysis were run in one notebook. [src: harvard_forest_warming] Results are given as C-cycling hits, other hits, OR (odds ratio) and one-sided p.
- DNA × organic: 5 / 57, 428 / 12,806, OR 2.78, p 0.042. This is a significant enrichment. [src: harvard_forest_warming]
- DNA × mineral: 0 / 57, 2 / 12,806, OR 0.0, p 1.0. [src: harvard_forest_warming]
- RNA × organic: 0 / 57, 0 / 14,245, OR NaN (not a number), p 1.0. [src: harvard_forest_warming]
- RNA × mineral: 0 / 57, 0 / 14,245, OR NaN, p 1.0. [src: harvard_forest_warming]

No individual RNA-pool KO survives FDR (q<0.10) at n=11+11 across 14K KOs. [src: harvard_forest_warming] The report identifies methanotrophy genes pmoA/pmoB and glyoxylate-cycle genes icl + ms, rather than canonical CAZymes, as its strongest mechanistic RNA signals. [src: harvard_forest_warming] The methanotrophy signals are directional and consistent across horizons, and both glyoxylate signals have p=0.037 in heated mineral soil. [src: harvard_forest_warming] The specific C-cycling RNA signals below have nominal p-values only and do not survive FDR. [src: harvard_forest_warming] Each is a heated-versus-control log2 FC with nominal p.
- K10944 pmoA, organic: +0.730, p=0.009. [src: harvard_forest_warming]
- K10945 pmoB, organic: +0.669, p=0.012. [src: harvard_forest_warming]
- K10944 pmoA, mineral: +0.743, p=0.029. [src: harvard_forest_warming]
- K10945 pmoB, mineral: +0.880, p=0.054. [src: harvard_forest_warming]
- K01637 aceA / icl, mineral: +0.460, p=0.037. [src: harvard_forest_warming]
- K01638 aceB / glcB, mineral: +0.268, p=0.037. [src: harvard_forest_warming]
- K01183 chiA, organic: +0.236, p=0.074. [src: harvard_forest_warming]
- K00382 lpdA, organic: −0.161, p=0.021. [src: harvard_forest_warming]

The report calls these signals biologically directional and consistent across horizons. It notes that the multiple-testing burden precludes individual FDR significance. [src: harvard_forest_warming]

The report describes the methanotrophy-up and glyoxylate-up RNA signature as previously unreported at this site, while noting published precedents elsewhere. [src: harvard_forest_warming] It calls the heated-mineral glyoxylate signature and Actinobacteria enrichment mechanistically self-consistent. [src: harvard_forest_warming]

### Horizon-specific responses
Most warming responses are horizon-specific, with ~39% of DNA KOs organic-only, mineral-only, or sign-flipping. [src: harvard_forest_warming] Correlation of KO responses between horizons is weak. For DNA, Pearson r is 0.075 (p=1.78e-17) and Spearman ρ is 0.216 (p=2e-134). [src: harvard_forest_warming] For RNA, Pearson r is 0.034 (p=6e-5) and Spearman ρ is 0.120 (p=4e-47). [src: harvard_forest_warming] The analysis compared per-KO log2 FC between organic and mineral horizons and classified horizon-specific responders. [src: harvard_forest_warming]

The curated C-cycling list is not differentially enriched in any horizon-specific class (OR<1, p>0.87 everywhere). [src: harvard_forest_warming] The report concludes that H3 holds genome-wide, but curated C-cycling categories are not the primary driver of the horizon × warming interaction. [src: harvard_forest_warming]

### Metabolites
Heated mineral samples have fewer detectable metabolites, 155 vs 167 ChEBI per sample (MW p=0.012). [src: harvard_forest_warming] The report calls this a ~7% drop. [src: harvard_forest_warming] It reads reduced richness as consistent with faster substrate turnover under warming. [src: harvard_forest_warming] The analysis used per-sample ChEBI counts and per-ChEBI Fisher's exact heated-versus-control tests. [src: harvard_forest_warming]

Control mineral samples have a mean ChEBI count of 167 ± 9. [src: harvard_forest_warming] Heated mineral samples have 155 ± 4, with MW p=0.012. [src: harvard_forest_warming] Control organic samples have 173 ± 6. [src: harvard_forest_warming] Heated organic samples have 160 ± 13, with MW p=0.209, in the same direction. [src: harvard_forest_warming]

No individual metabolite passes BH-FDR at this sample size, although several have nominal Fisher p<0.10. [src: harvard_forest_warming] Three ChEBI labels are reported:
- ChEBI:71028 is heated-only (11/11 vs 6/11), p=0.035. [src: harvard_forest_warming]
- ChEBI:30918 is control-only (0/11 vs 6/11), p=0.012. [src: harvard_forest_warming]
- ChEBI:27967 is heated-enriched, OR=12 (10/11 vs 5/11), p=0.063. [src: harvard_forest_warming]

ChEBI label resolution is left as follow-up because the project does not query external ontologies. [src: harvard_forest_warming]

### Context from published work
The report places its results against earlier studies. These comparisons are the report's interpretation, not new measurements.
- DeAngelis et al. (2015) found Actinobacteria, Alphaproteobacteria and Acidobacteria the strongest warming-responsive phyla across 5/8/20-year warmed plots, most pronounced in the organic horizon. [src: harvard_forest_warming] Pold et al. (2016) showed warming increases the fraction of carbohydrate-degrading genes affiliated with Actinobacteria. [src: harvard_forest_warming]
- The report calls its heated-mineral richness drop (155 vs 167 ChEBI, p=0.012) qualitatively consistent with substrate-depletion models. [src: harvard_forest_warming] Melillo et al. (2017) document a 4-phase oscillating soil-C loss trajectory under +5°C. [src: harvard_forest_warming] Domeignoz-Horta et al. (2022), on 28-year warmed plots, argue reduced substrate quantity and quality, not thermal acclimation, drives the apparent response. [src: harvard_forest_warming]
- Roy Chowdhury et al. (2021) is the closest methodological precedent, using Harvard Forest organic and mineral metatranscriptomes. [src: harvard_forest_warming] They found a larger treatment effect on KEGG transcripts than on CAZymes, with ~68% of differentially expressed CAZyme transcripts upregulated in heated soils. [src: harvard_forest_warming] The report calls its comparable DNA and RNA response (10-13% R²) in tension with that result, but notes differing timepoint, replication and pipeline. [src: harvard_forest_warming] Their upward CAZyme response is consistent with the report's chitinase up-result. [src: harvard_forest_warming]
- Choudoir et al. (2025) found heated-plot isolate genomes enriched in central carbohydrate and N metabolism with reduced codon usage bias. [src: harvard_forest_warming] The report reads this as pointing to sub-clade selection rather than only a compositional shift in its DNA-level Actinobacteria enrichment. [src: harvard_forest_warming]
- Zhang et al. (2024) report subtropical forest +4°C warming raising net CH₄ uptake 12-61% across soil depths and raising high-affinity USCα methanotrophs at 0-10 cm. [src: harvard_forest_warming] The report reads this as supporting the hypothesis that warming-induced moisture decrease increases CH₄ availability to methanotrophs. [src: harvard_forest_warming]
- Aliyu et al. (2016) describe coordinated icl/aceA + aceB/glcB upregulation as a published Actinobacteria signature of stress or C2-substrate utilization. [src: harvard_forest_warming]

## Data and Methods
All analyses use only the nmdc_metadata and nmdc_results tables, not nmdc_arkin. [src: harvard_forest_warming] The data come from NMDC study nmdc:sty-11-8ws97026 (n=42 biosamples), whose PI is Jeffrey Blanchard at U. Massachusetts Amherst. [src: harvard_forest_warming] The design is factorial: treatment (control vs heated) × horizon (organic vs mineral) × incubation (direct vs lab-incubated). [src: harvard_forest_warming] The DNA cohort is n=28 (mineral direct plus organic incubated). [src: harvard_forest_warming] The RNA cohort is n=39 (full mineral direct, organic direct and organic incubated). [src: harvard_forest_warming]

Study metadata, biosample design, workflow linkage and ChEBI metabolite IDs come from nmdc_metadata tables. [src: harvard_forest_warming] Read-based taxonomy, MAG taxonomy, KEGG KO annotations (DNA and RNA), Pfam domains and assembly QC come from nmdc_results tables. [src: harvard_forest_warming]

A synthesis notebook produces the report's multi-panel summary figure. [src: harvard_forest_warming]

## Caveats and Open Work
- The paired DNA/RNA subset confounds horizon with incubation, so the direct-only analysis is the cleaner test. [src: harvard_forest_warming]
- Omics coverage is unbalanced because the NMDC pipeline produced no metagenomes for organic-direct or some mineral-direct samples. This drives the H1 sensitivity caveat. [src: harvard_forest_warming] All organic-horizon DNA samples are lab-incubated, so incubation cannot be factored out cleanly there. [src: harvard_forest_warming]
- All samples come from a single date (2017-05-24), so RNA may carry non-warming noise. The design cannot detect seasonal effects, which Shinfuku et al. 2024 show are substantial at this site. [src: harvard_forest_warming]
- RNA-pool KO signals do not survive FDR. [src: harvard_forest_warming] Sample sizes (n=28 metagenome, n=39 metatranscriptome) limit per-KO FDR power across 12-14K KOs. [src: harvard_forest_warming]
- Metatranscriptome KO data from contig annotations measure transcript-pool composition, not TPM-quantified expression, and are biased by assembly quality. [src: harvard_forest_warming]
- Quantitative metabolomics, NOM and proteomics are excluded because nmdc_arkin tables are excluded. Equivalent layers exist in nmdc_arkin.{nom_gold, metabolomics_gold, proteomics_gold}. [src: harvard_forest_warming]
- abiotic_features are all zeros, from an NMDC parsing artifact, so no soil temperature, pH or nitrogen data exist in the KBase Data Lakehouse. The +5°C label is the only environmental contrast. [src: harvard_forest_warming]
- The report notes that its verdict does not exclude an early transient RNA lead. [src: harvard_forest_warming]

The report proposes these next analyses:
- Add nmdc_arkin quantitative NOM, metabolomics and proteomics layers to strengthen H2. It calls quantitative SOM chemistry the most direct complement to its gene-level findings. [src: harvard_forest_warming]
- Resolve ChEBI labels for the top differential metabolite hits with an ontology resolver, and run pathway enrichment against KEGG modules. [src: harvard_forest_warming]
- Run a cross-study meta-analysis with NMDC SPRUCE peatland (nmdc:sty-11-33fbta56) and Alaskan permafrost thaw (nmdc:sty-11-db67n062) to test whether the methanotrophy-up signature reproduces across sites. [src: harvard_forest_warming]
- Identify which MAGs in the 298-MAG cohort carry the upregulated pmoA/pmoB, and test whether they are USCα methanotrophs or distributed across phyla. [src: harvard_forest_warming]
- Test the hypothesis that warming activates a ruderal community subset characterized by Actinobacteria, glyoxylate-cycle-active organisms and methanotrophy, using Choudoir et al. 2025 pangenome data. [src: harvard_forest_warming]

## Slots Into
- [[concepts/warming-response-of-soil-microbial-community-composition]]: the organic-soil Actinobacteria increase and Acidobacteria decrease reproduce DeAngelis et al. 2015. [src: harvard_forest_warming]
- [[concepts/dna-versus-rna-pool-sensitivity-to-environmental-perturbation]]: DNA and RNA treatment R² are comparable (10-13%), and H1 is not supported. [src: harvard_forest_warming]
- [[concepts/functional-gene-responses-to-soil-warming]]: DNA × organic is enriched in C-cycling KOs, and RNA pmoA/pmoB signals are nominal only. [src: harvard_forest_warming]
- [[concepts/soil-metabolite-richness-under-warming-and-substrate-depletion]]: heated mineral samples have fewer detectable ChEBI metabolites. [src: harvard_forest_warming]
