---
type: "Summary"
description: "Harvard Forest warming effects on DNA, RNA, carbon cycling, and metabolites"
doc_type: "short"
full_text: "sources/harvard_forest_warming__REPORT.md"
---
# Harvard Forest Long-Term Warming — DNA vs RNA Functional Response

## Overview

A 25-year +5°C soil-warming experiment at Harvard Forest Barre Woods (NMDC `nmdc:sty-11-8ws97026`; 42 biosamples) produced a real but modest community-level response that reproduced the published Actinobacteria-up/Acidobacteria-down signal and a structured functional-gene response of approximately 12% R² in DNA and 10–11% in RNA. Once the horizon × incubation confound was removed, DNA and RNA responses were comparable, so the proposed hypothesis that RNA shifts more than DNA was not supported. All analyses used `nmdc_metadata` and `nmdc_results` tables and did not use `nmdc_arkin`. [src: harvard_forest_warming]

## Key findings

- In 14 control and 14 heated direct samples, kraken2 read-based relative abundance showed Actinobacteria increasing from 0.249 to 0.315 in organic soil (log2 FC +0.341, q=0.049) and Acidobacteria decreasing from 0.035 to 0.024 (log2 FC −0.549, q=0.049). Cyanobacteria changed from 0.0032 to 0.0026 (log2 FC −0.305, q=0.072), Proteobacteria from 0.654 to 0.605 (log2 FC −0.111, q=0.088), and Verrucomicrobia from 0.0058 to 0.0041 (log2 FC −0.513, q=0.088); mineral soil showed no phylum-level changes after FDR correction. [src: harvard_forest_warming]

- PERMANOVA on Bray–Curtis genus distances attributed 7.6% of variance to treatment (p=0.069), 30.6% to horizon (p=0.0002), and 41% to the treatment × horizon four-cell factor (p=0.0002). [src: harvard_forest_warming]

- In the paired n=25 subset, treatment pseudo-F was 3.12 in DNA (R²=11.9%, p=0.020) and 0.76 in RNA (R²=3.2%, p=0.60), but this subset confounded horizon with incubation because every organic sample was incubated and every mineral sample was direct. In direct-sample sensitivity analyses, DNA × mineral had n=14, F=1.75, R²=12.7%, p=0.081; RNA × mineral had n=11, F=1.15, R²=11.4%, p=0.254; and RNA × organic had n=14, F=1.33, R²=10.0%, p=0.190. These results do not support the premise that the transcript pool is more sensitive to long-term warming. [src: harvard_forest_warming]

- A curated 62-KO carbon-cycling list was enriched among heated-up DNA KOs in organic soil: 5 of 57 carbon-cycling hits versus 428 of 12,806 other hits, Fisher odds ratio 2.78 and one-sided p=0.042. DNA × mineral had 0 of 57 carbon-cycling hits and 2 of 12,806 other hits (odds ratio 0.0, p=1.0); RNA × organic had 0 of 57 and 0 of 14,245 (NaN, p=1.0); and RNA × mineral had 0 of 57 and 0 of 14,245 (NaN, p=1.0). [src: harvard_forest_warming]

- RNA signals for particulate methane monooxygenase were directionally positive across both horizons: pmoA (K10944) had log2 FC +0.730 in organic soil (p=0.009) and +0.743 in mineral soil (p=0.029), while pmoB (K10945) had +0.669 in organic soil (p=0.012) and +0.880 in mineral soil (p=0.054). These individual signals were nominal and did not survive FDR across 14K KOs. [src: harvard_forest_warming]

- The glyoxylate-cycle genes isocitrate lyase aceA/icl (K01637) and malate synthase aceB/glcB (K01638) increased in heated mineral RNA, with log2 FC +0.460 and +0.268, respectively, and p=0.037 for each. Chitinase chiA (K01183) increased in heated organic RNA (log2 FC +0.236, p=0.074), whereas lpdA (K00382), associated with TCA/pyruvate dehydrogenase metabolism, decreased (log2 FC −0.161, p=0.021). [src: harvard_forest_warming]

- Warming responses were mostly horizon-specific. Organic-versus-mineral KO log2 FC correlations were Pearson r=0.075 (p=1.78e-17) and Spearman ρ=0.216 (p=2e-134) for DNA, and Pearson r=0.034 (p=6e-5) and Spearman ρ=0.120 (p=4e-47) for RNA. Approximately 39% of DNA KOs were organic-only, mineral-only, or sign-flipping; however, the curated carbon-cycling list was not differentially enriched in horizon-specific classes (odds ratio <1, p>0.87 everywhere). [src: harvard_forest_warming]

- Heated mineral samples had fewer detectable metabolites, with 155 ± 4 ChEBI identifications per sample versus 167 ± 9 in control mineral samples (Mann–Whitney p=0.012). Organic samples showed the same direction but not significance: 160 ± 13 in heated soil versus 173 ± 6 in control soil (p=0.209). No individual metabolite passed BH-FDR; nominal signals included ChEBI:71028, present in 11/11 heated versus 6/11 control samples (p=0.035), ChEBI:30918, present in 0/11 heated versus 6/11 control samples (p=0.012), and ChEBI:27967, present in 10/11 heated versus 5/11 control samples (odds ratio 12, p=0.063). [src: harvard_forest_warming]

- The sample design contained 42 biosamples across treatment, organic versus mineral horizon, and direct versus laboratory-incubated conditions. The DNA cohort contained n=28 samples and the RNA cohort n=39; organic-horizon DNA samples were all laboratory-incubated, while direct organic DNA was not produced by the NMDC pipeline. The metatranscriptome recovered 14,302 distinct KOs versus 12,863 in the metagenome. [src: harvard_forest_warming]

## Caveats

- The study used a single sampling date, 2017-05-24, so it cannot detect seasonal effects. [src: harvard_forest_warming]

- Omics-rich layers had limited sample sizes (n=28 metagenomes and n=39 metatranscriptomes), reducing per-KO FDR power across 12–14K KOs. [src: harvard_forest_warming]

- Metatranscriptome KO counts came from contig annotations and represent transcript-pool composition rather than TPM-quantified expression; contig-level annotation counts approximately represent relative transcript abundance but are biased by assembly quality. [src: harvard_forest_warming]

- The paired DNA/RNA comparison is affected by the horizon × incubation confound, and organic-horizon DNA lacks direct samples, preventing incubation from being factored cleanly out of that DNA analysis. [src: harvard_forest_warming]

- The single-timepoint RNA pool may include diurnal and microspatial variation from moisture pulses, root-exudate availability, and temperature conditions that are unrelated to chronic warming. The report therefore treats comparable long-term DNA and RNA response magnitude as compatible with, but not excluding, an earlier transient in which RNA could lead DNA. [src: harvard_forest_warming]

- `abiotic_features` was all zeros for these samples because of an NMDC parsing artifact, so the analysis lacked in-lakehouse soil temperature, pH, and nitrogen measurements; the +5°C treatment label was the only environmental contrast. [src: harvard_forest_warming]

- The project excluded `nmdc_arkin`, so it had no quantitative NOM, metabolomics, or proteomics layers. The ChEBI labels for the differential metabolite hits were not resolved through external ontologies. [src: harvard_forest_warming]

- The pmoA/pmoB and glyoxylate-cycle findings are directional gene-level signals, and the individual RNA signals did not survive FDR across 14K KOs. The report interprets the heated-mineral metabolite-richness decrease as consistent with faster substrate turnover, but it is not quantitative metabolomics evidence. [src: harvard_forest_warming]

## Slots Into

- [[concepts/multi-omics-integration]] — compares DNA and RNA functional-pool responses while integrating taxonomy, KO composition, and metabolite richness; [src: harvard_forest_warming]
- [[concepts/ecotype-environment-gene-content]] — links long-term warming, horizon-specific community composition, and functional-gene content, including Actinobacteria enrichment and carbon-cycling responses; [src: harvard_forest_warming]
- [[concepts/environment-embedding-geography]] — provides a Harvard Forest soil-warming case in which organic versus mineral horizon structures the observed environmental response; [src: harvard_forest_warming]
- [[concepts/pangenome-integration]] — supplies genome-content and functional-gene evidence that can be compared with Harvard Forest pangenome-level adaptation findings; [src: harvard_forest_warming]
