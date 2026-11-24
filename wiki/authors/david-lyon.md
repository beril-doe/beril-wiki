# David Lyon

ORCID: [0000-0002-1927-3565](https://orcid.org/0000-0002-1927-3565)

## Contributions

### Subsurface Bacillota_B accessory content and genome size

The [[summaries/bacillota_b_subsurface_accessory__REPORT]] project counted 547 enriched orthologous groups (OGs) in deep-clay Bacillota_B genomes. Its H1 prediction was at least 10. [src: bacillota_b_subsurface_accessory] The test was a per-OG Fisher's exact test on 14,109 Firmicutes-level eggNOG OGs, with Benjamini-Hochberg false discovery rate correction (q<0.05), fold-difference ≥3 and ≥3 positive anchor genomes. [src: bacillota_b_subsurface_accessory] In the same run 27 OGs were anchor-depleted. [src: bacillota_b_subsurface_accessory] Keyword scanning assigned 42 OGs to anaerobic respiration, 24 to sporulation revival, 12 to mineral attachment / EPS, 4 to anaerobic regulators and 3 to osmoadaptation. The other 462 were "other / unannotated". [src: bacillota_b_subsurface_accessory] The report says the scanner missed anaerobic-niche signal in that bucket. It estimates the H1-relevant total after manual reclassification at 80–100 of 547. [src: bacillota_b_subsurface_accessory] COG1977 (molybdopterin cofactor process) was in 10/10 anchor genomes versus 11/62 baseline genomes. OG 1UIFM (DsrE/DsrF/DsrH-like) was in 7/10 anchor versus 0/62 baseline genomes. [src: bacillota_b_subsurface_accessory]

The same project rejected H2 (genome-size streamlining), and the result went the opposite way. Anchor genomes (n=10) averaged 4,110,038 bp versus 3,046,124 bp for baseline (n=62), with Cohen's d +1.39 and Mann–Whitney p=0.025. [src: bacillota_b_subsurface_accessory] The mean size difference was 35%, and anchor genomes carried ~25% more eggNOG OGs. [src: bacillota_b_subsurface_accessory] GC content (p=0.44) and CheckM completeness (94.7% versus 94.3%, p=0.93) did not differ significantly. The report therefore concludes that the size gap is not a MAG-quality artefact. [src: bacillota_b_subsurface_accessory]

### Correction of the iron-reduction marker error

The bacillota_b_subsurface_accessory project found that K07811, K17324 and K17323, used as iron-reduction markers in the clay project, are a TMAO reductase and two glycerol ABC transport genes. None is an iron-reduction gene. [src: bacillota_b_subsurface_accessory] Its corrected detector scores a genome positive on PF02085, PF22678 or a CXXCH motif count ≥4. [src: bacillota_b_subsurface_accessory] Corrected iron-reduction rates were 55.6% (5/9) in deep clay, 40.0% (12/30) in shallow clay and 40.9% (61/149) in soil baseline. No pairwise Fisher comparison was significant; deep versus shallow gave OR=1.88, p=0.46. [src: bacillota_b_subsurface_accessory] The sulfate-reduction side stood, at 5/9 deep genomes against a rock-attached null of 0.2% (binomial p=4×10⁻¹²). [src: bacillota_b_subsurface_accessory]

### Clay-confined cultured genomes

The [[summaries/clay_confined_subsurface__REPORT]] project built a deep clay cohort of 9 genomes, 8 from Mont Terri Opalinus boreholes and 1 from bentonite. [src: clay_confined_subsurface] Sulfate-reduction markers were present in 5/9 (56%) deep genomes. Against the Mitzscherling null the binomial p was 4.0×10⁻¹². Against soil baseline, SR_complete gave OR=33.8 (p_BH=2.5×10⁻⁴). [src: clay_confined_subsurface] Its original iron-reduction analysis was withdrawn after the marker error, including the 3.7-fold shallow-clay enrichment (p=0.0025). [src: clay_confined_subsurface] After correction, no cohort comparison was significant (all Fisher p ≥ 0.46). [src: clay_confined_subsurface]

The deep cohort's mean anaerobic toolkit score was 1.89, versus 0.39 in soil baseline and 0.03 in shallow clay. [src: clay_confined_subsurface] Within Bacillota_B, Wood–Ljungdahl (5/5 vs 15/19, p=0.54) and [NiFe]-hydrogenase (5/5 vs 14/19, p=0.54) did not differ. Only sulfate reduction stayed enriched (5/5 vs 4/19, p_BH=0.04). [src: clay_confined_subsurface] Biosynthetic self-sufficiency was not supported. Deep versus baseline amino-acid pathway completeness was 16.22 versus 16.66 (d=−0.17, p=0.153). [src: clay_confined_subsurface]

### Lanthanide methylotrophy

The [[summaries/lanthanide_methylotrophy_atlas__REPORT]] project annotated xoxF in 3,690 of 293,059 GTDB-r214 genomes and mxaF in 195. The global ratio was 18.92 : 1 (Clopper-Pearson 95% CI [13.07, 27.69]). [src: lanthanide_methylotrophy_atlas] The xoxF dominance held under three phylogenetic corrections. The mixed model gave a ratio of ~143 : 1 (95% credible interval [122, 169]). [src: lanthanide_methylotrophy_atlas] xoxF was enriched in soil and sediment genomes (OR 1.92, p_BH 6.1 × 10⁻³⁹). REE-impacted samples showed a 3.5-fold descriptive elevation that did not clear the FDR threshold (n=37, p_BH = 0.082). [src: lanthanide_methylotrophy_atlas] Bakta-validated lanmodulin occurred in 62 genomes from 10 species. Its xoxF co-occurrence was 49 / 62 = 79.0%, just under the 80% threshold (p = 0.65). [src: lanthanide_methylotrophy_atlas] Only 4/37 REE acid-mine-drainage MAGs carried any xoxF. [src: lanthanide_methylotrophy_atlas]

## Projects (3)

- [[summaries/bacillota_b_subsurface_accessory__REPORT|bacillota_b_subsurface_accessory]]
- [[summaries/clay_confined_subsurface__REPORT|clay_confined_subsurface]]
- [[summaries/lanthanide_methylotrophy_atlas__REPORT|lanthanide_methylotrophy_atlas]]
