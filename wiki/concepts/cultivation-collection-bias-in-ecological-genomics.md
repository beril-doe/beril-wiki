---
type: "Concept"
description: "Culture-collection bias limits how genomes validate environmental adaptation"
sources: ["summaries/bacdive_metal_validation__REPORT.md"]
---
# Cultivation and collection bias constrain ecological genomic inference

Ecological genomic inference is constrained when available genomes come disproportionately from culturable, described strains rather than the full diversity of environmental bacteria. [src: bacdive_metal_validation] The BacDive metal-validation project directly illustrates this limitation by linking curated isolation environments to genome-derived metal-tolerance scores through a species-level [[concepts/pangenome-integration]] bridge. [src: bacdive_metal_validation] The underlying analysis is documented in [[summaries/bacdive_metal_validation__REPORT]]. [src: bacdive_metal_validation]

## Evidence from BacDive–pangenome matching

Of 97,334 BacDive strains, 42,227 strains (43.4%) matched 6,426 GTDB species, while 55,107 strains (56.6%) remained unmatched. [src: bacdive_metal_validation] Exact species-name agreement produced 33,535 matches (34.5%), and removing GTDB suffixes produced 8,692 additional matches (8.9%). [src: bacdive_metal_validation] Only 25,089 matched strains had isolation-source metadata, so both genome-score linkage and ecological metadata availability reduced the usable sample. [src: bacdive_metal_validation]

This matching loss limits which cultivated strains can contribute to ecological validation and can make the retained sample unrepresentative of environmental diversity. [src: bacdive_metal_validation] The report specifically notes that BacDive represents culturable, described strains and may under-represent metal-tolerant extremophiles because of culture-collection bias. [src: bacdive_metal_validation] The unresolved 56.6% could partly reflect different species boundaries between GTDB and LPSN/DSMZ rather than absence of relevant genomes, making accession-level matching an important remedy. [src: bacdive_metal_validation]

## Collection bias affects environmental validation

Among matched strains, heavy-metal contamination isolates had a median metal score of 0.240 and a mean of 0.236, compared with an environmental-baseline median of 0.187 and mean of 0.195. [src: bacdive_metal_validation] Their median delta was +0.053, Cohen's d was +1.00, and the Mann–Whitney p-value was 0.006 for n=10 isolates. [src: bacdive_metal_validation] Cohen's d was calculated as (mean_group - mean_baseline) / pooled_SD, with pooled_SD = sqrt((SD_group² + SD_baseline²) / 2). [src: bacdive_metal_validation]

The broader contamination gradient was heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). [src: bacdive_metal_validation] Waste/sludge isolates had n=305 and d=+0.57, all-contamination isolates had n=176 and d=+0.43, and industrial isolates had n=796 and d=+0.20; each comparison had p<0.0001. [src: bacdive_metal_validation] Host-associated isolates had n=12,086, d=+0.14, and p<0.0001, indicating that collection category can also track biological or genomic composition unrelated to environmental contamination. [src: bacdive_metal_validation]

These results support [[concepts/environmental-resistome]] by showing that curated isolation environments can validate genome-based metal-tolerance predictions, but the strength of that validation depends on which environments and organisms enter the culture collection. [src: bacdive_metal_validation] The heavy-metal result is especially uncertain because n=10 matched isolates produced an observed d=1.00, only slightly above the approximately d=0.93 minimum detectable effect size for 80% power against an environmental baseline of approximately 5,000 strains. [src: bacdive_metal_validation]

## Taxonomic composition and residual bias

Within Pseudomonadota, contamination isolates had metal scores delta=+0.040 above environmental isolates with p<0.001, using n=85 contamination and n=5,655 environmental isolates. [src: bacdive_metal_validation] Within Actinomycetota, the corresponding delta was +0.035 with p<0.001, using n=62 contamination and n=772 environmental isolates. [src: bacdive_metal_validation] These results support a contamination-associated signal beyond broad phylum composition in the two most-sampled phyla. [src: bacdive_metal_validation]

The signal was not significant within Bacillota, where delta=-0.012, p=0.285, n=19 contamination and n=492 environmental isolates, or Bacteroidota, where delta=-0.008, p=0.456, n=5 contamination and n=156 environmental isolates. [src: bacdive_metal_validation] These null results cannot distinguish biological differences from limited statistical power because contamination-isolate sample sizes were small. [src: bacdive_metal_validation]

Host-associated strains had a positive but small deviation, with d=+0.14 and p<0.0001. [src: bacdive_metal_validation] The report attributes this pattern potentially to genome-size and taxonomic confounding because host-associated records were dominated by Pseudomonas, Klebsiella, and Acinetobacter, which have large genomes and more KEGG-annotated gene clusters. [src: bacdive_metal_validation] Genome-size normalization reduced but did not eliminate this possible confounding, so normalization alone does not establish that isolation environment caused the score difference. [src: bacdive_metal_validation]

## Phenotype records are an additional bottleneck

Only 24 matched strains had metal-utilization records covering iron, manganese, arsenate, chromate, cobalt, or zinc. [src: bacdive_metal_validation] Eight of those results were positive and 16 were negative. [src: bacdive_metal_validation] Positive utilizers had lower metal scores in the exploratory comparison, but the result was inconclusive because Mann–Whitney p=0.14 and Cohen's d=-0.57 with only 24 records. [src: bacdive_metal_validation]

This underpowered phenotype comparison shows that linking genomes to collection metadata does not guarantee an independent phenotype validation. [src: bacdive_metal_validation] The limitation refines [[concepts/multi-omics-integration]]: genome-derived scores and curated phenotype records can be connected, but sparse and selectively recorded phenotypes may prevent reliable assessment of agreement. [src: bacdive_metal_validation]

## Interpretation and tensions

The contamination gradient supports the hypothesis that genome-based Metal Fitness Atlas scores capture real ecological metal-adaptation signal, but the heavy-metal estimate is imprecise because only n=10 isolates matched species with scores. [src: bacdive_metal_validation] This evidence is stronger at the larger contamination-category sample sizes than for the heavy-metal category itself, where the effect barely exceeded the power threshold. [src: bacdive_metal_validation]

The result also needs to be distinguished from the finding that metal-tolerance genes were 88% core in the metal-specificity project: within-species conservation can coexist with between-species differences in the total number of metal-tolerance genes. [src: bacdive_metal_validation] The proposed explanation that species with larger core genomes encoding more metal-tolerance functions are more likely to occur in contaminated environments is an interpretation rather than a direct causal test. [src: bacdive_metal_validation]

Compared with the Oak Ridge field-abundance analysis, which found a suggestive but non-significant correlation between laboratory metal tolerance and field abundance of rho=0.50, p=0.095, n=11 genera, the BacDive analysis provides larger-scale support for the same hypothesis through contamination-category effect sizes of d=+0.43 to +1.00. [src: bacdive_metal_validation] The comparison does not remove collection bias because the BacDive heavy-metal result still uses only n=10 isolates. [src: bacdive_metal_validation]

## Open Directions

- Match BacDive GCA accessions directly to pangenome genome_ids through `kbase_ke_pangenome.genome`, then test whether recovered strains change the contamination effect estimates and the 56.6% unmatched fraction. [src: bacdive_metal_validation]
- Integrate ENIGMA CORAL community data from the Oak Ridge metal-contaminated site and compare community-level metal-tolerance profiles with BacDive isolation-source predictions to test whether the culture-collection signal generalizes to field communities. [src: bacdive_metal_validation]
- Stratify matched BacDive strains by metal-tolerance gene families and contamination environment, using metals with sufficient representation including iron and manganese, to test whether specific functions predict specific environments. [src: bacdive_metal_validation]
- Expand BacDive phenotype extraction beyond the `metabolite_utilization` table to include MIC and growth-inhibition data, then test whether independently measured tolerance agrees with genome-derived scores. [src: bacdive_metal_validation]
- Reanalyze contamination effects within taxonomic strata and after genome-size normalization, using the small Bacillota and Bacteroidota groups to determine whether their null results reflect biology or limited power. [src: bacdive_metal_validation]
