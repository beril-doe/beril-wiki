---
type: "Summary"
description: "BacDive validation links environmental metal isolation to genomic tolerance scores."
doc_type: "short"
full_text: "sources/bacdive_metal_validation__REPORT.md"
---
# BacDive Isolation Environment × Metal Tolerance Prediction

## Overview

This project linked BacDive strains to GTDB pangenome metal tolerance scores and tested whether isolation environments provide independent ecological validation of genome-based predictions. Of 97,334 BacDive strains, 42,227 (43.4%) matched 6,426 GTDB species, including 25,089 strains with isolation metadata. The strongest result was that bacteria isolated from heavy-metal contamination sites had metal tolerance scores one standard deviation above the environmental baseline (Cohen's d = +1.00, Mann-Whitney p=0.006, n=10), although the small matched heavy-metal group makes the estimate imprecise. [src: bacdive_metal_validation]

## Key Findings

### Environmental metal tolerance signal

Heavy-metal contamination isolates had a median metal score of 0.240, mean of 0.236, median delta of +0.053, Cohen's d of **+1.00**, and p-value **0.006** (n=10), compared with an environmental baseline median of 0.187 and mean of 0.195. Cohen's d was calculated as (mean_group - mean_baseline) / pooled_SD, with pooled_SD = sqrt((SD_group² + SD_baseline²) / 2). [src: bacdive_metal_validation]

The reported contamination gradient was heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). Waste/sludge isolates had n=305, median 0.219, mean 0.218, median delta +0.032, d=+0.57, and p<0.0001; all-contamination isolates had n=176, median 0.215, mean 0.211, median delta +0.028, d=+0.43, and p<0.0001; industrial isolates had n=796, median 0.199, mean 0.202, median delta +0.012, d=+0.20, and p<0.0001; host-associated isolates had n=12,086, median 0.194, mean 0.201, median delta +0.007, d=+0.14, and p<0.0001. [src: bacdive_metal_validation]

The report interprets the heavy-metal result and the dose-dependent pattern as validation that the genome-based Metal Fitness Atlas score captures real ecological metal-adaptation signal. This interpretation is supported by direct environment-group comparisons, but the heavy-metal estimate is at the detection limit and should be treated as imprecise. [src: bacdive_metal_validation]

### Phylum-stratified analysis

Within Pseudomonadota, contamination isolates had metal scores delta=+0.040 above environmental isolates (p<0.001; n=85 contamination and n=5,655 environmental), and within Actinomycetota the delta was +0.035 (p<0.001; n=62 and n=772, respectively). The contamination signal was not significant within Bacillota (delta=-0.012, p=0.285; n=19 and n=492) or Bacteroidota (delta=-0.008, p=0.456; n=5 and n=156). [src: bacdive_metal_validation]

These results support a metal-adaptation signal beyond broad phylum composition within the two most-sampled phyla, while the null results for Bacillota and Bacteroidota are consistent with either biological differences or limited statistical power because contamination isolates were scarce. [src: bacdive_metal_validation]

### BacDive–pangenome bridge

Species-name matching linked 42,227 of 97,334 BacDive strains (43.4%) to metal tolerance scores across 6,426 unique GTDB species. Exact species-name agreement accounted for 33,535 strains (34.5%), and GTDB suffix removal provided 8,692 additional matches (8.9%), such as matching BacDive “Pseudomonas fluorescens” to GTDB “Pseudomonas fluorescens A”. A total of 55,107 strains (56.6%) were unmatched, and 25,089 matched strains had isolation-source metadata. [src: bacdive_metal_validation]

Only 24 matched strains had metal-utilization records covering iron, manganese, arsenate, chromate, cobalt, or zinc; 8 results were positive and 16 negative. Positive utilizers had lower metal scores in the exploratory comparison, but the result was inconclusive because Mann-Whitney p=0.14 and Cohen's d=-0.57 with only 24 records. [src: bacdive_metal_validation]

### Power and interpretation

For n=10 heavy-metal isolates versus approximately 5,000 environmental-baseline strains, the minimum detectable effect size at 80% power was approximately d=0.93; the observed d=1.00 barely exceeded this threshold. The research plan referenced n=31 BacDive heavy-metal isolates, but only 10 matched pangenome species with metal scores after the species-name bridge. [src: bacdive_metal_validation]

The report reconciles the environmental signal with the finding from the metal-specificity project that metal tolerance genes are 88% core by distinguishing within-species conservation from between-species variation in the total number of metal-tolerance genes. It proposes that species with larger core genomes encoding more metal-tolerance functions can score higher and be more likely to occur in contaminated environments; this is an interpretation rather than a direct causal test. [src: bacdive_metal_validation]

Compared with the lab_field_ecology result of a suggestive but non-significant correlation between laboratory metal tolerance and field abundance at Oak Ridge (rho=0.50, p=0.095, n=11 genera), the BacDive analysis provides stronger large-scale support for the same hypothesis, with d=+0.43 to +1.00 across contamination categories. The heavy-metal comparison itself still uses only n=10 isolates. [src: bacdive_metal_validation]

Host-associated bacteria scored slightly higher than expected rather than lower: d=+0.14 and p<0.0001. The report attributes this likely to genome-size confounding, because host-associated BacDive records are dominated by Pseudomonadota pathogens such as Pseudomonas, Klebsiella, and Acinetobacter with large genomes and more KEGG-annotated gene clusters; genome-size normalization reduces but does not eliminate this possible effect. The host-associated signal was smaller than the contamination signals of d=+0.43 to +1.00. [src: bacdive_metal_validation]

## Caveats

The heavy-metal group contains only n=10 matched isolates and was at the detection limit for d=1.00, so a larger dataset is needed to estimate the effect precisely. [src: bacdive_metal_validation]

BacDive represents culturable, described strains rather than the full diversity of environmental bacteria, and culture-collection bias may under-represent metal-tolerant extremophiles. [src: bacdive_metal_validation]

Species-level matching is lossy: 56.6% of BacDive strains did not match a GTDB species, primarily because GTDB uses different species boundaries from LPSN/DSMZ. Genome-accession matching through GCA→pangenome genome_id could improve coverage but requires a Spark query. [src: bacdive_metal_validation]

The metal tolerance score is genome-size-normalized as metal clusters divided by annotated clusters. This controls for genome size, which is important because Pseudomonadota tend to have larger genomes, but normalization does not eliminate the possibility that metal-tolerance functions correlate with total metabolic complexity. [src: bacdive_metal_validation]

The metal-utilization validation is underpowered because only 24 records matched strains with metal scores; the negative direction for positive utilizers should not be over-interpreted. [src: bacdive_metal_validation]

The absence of a significant signal in Bacillota and Bacteroidota cannot distinguish real biological differences from limited power because contamination-isolate sample sizes were small. [src: bacdive_metal_validation]

## Future Directions

- Match BacDive GCA accessions directly to pangenome genome_ids through `kbase_ke_pangenome.genome` to recover more of the 56.6% unmatched strains. [src: bacdive_metal_validation]
- Integrate ENIGMA CORAL community data from the Oak Ridge metal-contaminated site for complementary field validation. [src: bacdive_metal_validation]
- Test whether specific metal-tolerance gene families predict specific contamination environments for metals with sufficient BacDive representation, including iron and manganese. [src: bacdive_metal_validation]
- Expand BacDive metal-phenotype extraction beyond the current `metabolite_utilization` table to include possible MIC and growth-inhibition data. [src: bacdive_metal_validation]

## Slots Into

- [[concepts/environmental-resistome]] — The BacDive isolation-environment comparisons provide ecological validation of genome-based metal-tolerance predictions and identify contamination-associated tolerance signals. [src: bacdive_metal_validation]
- [[concepts/pangenome-integration]] — The BacDive–GTDB pangenome bridge quantifies species-level matching coverage, suffix-based matching, and the remaining 56.6% unmatched strains. [src: bacdive_metal_validation]
- [[concepts/multi-omics-integration]] — The project connects genome-derived metal-tolerance scores with curated isolation and utilization phenotypes, while documenting that the utilization comparison remains underpowered. [src: bacdive_metal_validation]
