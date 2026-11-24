---
type: "Gene_Or_Pathway"
description: "Defense systems used as a positive HGT control, with a recent-to-ancient gain ratio of 24.5×."
sources: ["summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md"]
aliases: ["CRISPR", "class-I CRISPR-Cas"]
---
# CRISPR-Cas

CRISPR-Cas (also called CRISPR or class-I CRISPR-Cas) is a family of prokaryotic defense systems. The corpus uses it as a positive control for horizontal gene transfer (HGT): in the GTDB KO atlas its gains are strongly skewed toward recent, genus-level events, with a recent-to-ancient gain ratio of 24.5×. [src: discoveries, gene_function_ecological_agora] A separate project shows that how CRISPR-Cas is detected changes its apparent prevalence by about 40 percentage points. [src: phage_defense_arsenal]

## Key facts

- The recent-to-ancient ratio is recent% divided by ancient%. For CRISPR-Cas it is 24.5×, the highest class in the atlas. The other classes are TCS HK (two-component system histidine kinase) at 10.3×, β-lactamase at 9.0×, ribosomal at 6.2-6.3×, RNAP core (RNA polymerase) at 6.4× and tRNA-synth at 2.3×. [src: gene_function_ecological_agora]
- The control panel holds 6 CRISPR-Cas KOs (KEGG orthologs) out of 748 control-panel KOs. [src: gene_function_ecological_agora]
- CRISPR-Cas is very rare in Mycobacterium and Streptomyces gene-content data. [src: phage_defense_arsenal]

## Gain-age profile as an HGT control

CRISPR-Cas has 20,898 gains in the GTDB KO atlas. Of these, 58.7% are recent (genus-level), 27.6% older-recent, 7.0% mid, 4.3% older and 2.4% ancient (phylum or above). [src: gene_function_ecological_agora] The ratio is 58.7 / 2.4 = 24.5. The report calls this highly recent-skewed and consistent with documented HGT activity. [src: gene_function_ecological_agora]

CRISPR-Cas also lies in the high-recent-gain, low-leaf-consistency (LC) quadrant. This is the "HGT-active patchy" quadrant. CRISPR-Cas has LC 0.29, antimicrobial resistance (AMR) has 0.11 and TCS HK has 0.13. [src: gene_function_ecological_agora]

The report reads the recent skew as consistent with dispersal mainly through mobile-element-borne transfers. It cites Metcalf et al. 2014, who documented cross-tree-of-life HGT of class-I CRISPR-Cas systems. This is an interpretation, not a direct measurement. [src: gene_function_ecological_agora]

### Control-class calibration

The CRISPR-Cas positive control separated clearly from a tRNA-synthetase negative control. The test used 6 CRISPR-Cas KOs against 20 strict tRNA-synth KOs. Cohen's d was +3.558, the 95% CI (confidence interval) was [+2.93, +21.53], and the one-sided MW p was 4×10⁻⁶. This passed the M18 criterion. [src: gene_function_ecological_agora] Against 3 strict RNAP-core KOs, d was +1.905, the CI was [+1.47, +11.88] and p was 0.012, which also passed. [src: gene_function_ecological_agora] Against 83 strict ribosomal KOs, d was −0.919 and p was 0.71, which failed M18. [src: gene_function_ecological_agora] For the wider framework, see [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]].

## Prevalence and detection method

Detection method strongly affects CRISPR-Cas prevalence. Across all 27,626 pangenome species with at least one defense hit, CRISPR-Cas prevalence was 96.1%. This was the highest of the defense systems reported. [src: phage_defense_arsenal] The report states that this figure is inflated by permissive eggNOG description-based matching. The specific Cas1 Pfam (PF01867) is present in only 55% of species. [src: phage_defense_arsenal] Description-based detection therefore over-counts by about 40 percentage points on the same pangenome. [src: phage_defense_arsenal] The report warns that any comparison of CRISPR prevalence across studies must state its detection method. [src: phage_defense_arsenal] See [[concepts/domain-based-marker-detection-and-annotation-method-bias]] and [[concepts/pan-bacterial-prevalence-phylum-distribution-and-mobility-of-anti-phage-defense-systems]].

## Core versus accessory placement

Bacterial CRISPR-Cas gene clusters are 27.4% core and 47.2% singleton. The report classes this as mild accessory. Only DISARM sits nearer baseline (40.6% core, 42.3% singleton). CRISPR-Cas is more core than BREX (20.7% core, 55.8% singleton), CBASS, R-M Types I and II, Gabija and Retron, which all have lower core percentages. [src: phage_defense_arsenal] See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

## Sources

See [[summaries/gene_function_ecological_agora__REPORT]], [[summaries/phage_defense_arsenal__REPORT]] and [[summaries/discoveries]].
