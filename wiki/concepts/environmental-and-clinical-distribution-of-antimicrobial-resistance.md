---
type: "Concept"
description: "How AMR gene load, accessory fraction and conservation vary with isolation environment, clinical fraction of genomes and environmental embeddings; stops at mechanisms of transfer."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/discoveries.md"]
---
# Environmental and clinical distribution of antimicrobial resistance

How AMR (antimicrobial resistance) gene load, accessory fraction and conservation vary with isolation environment, clinical fraction of genomes and environmental embeddings; stops at mechanisms of transfer. Clinical species carry the most AMR clusters per species. [src: amr_pangenome_atlas] Clinical genome fraction predicts AMR within multi-environment species. [src: discoveries] The central digest describes amr_environmental_resistome as the largest genomic AMR-environment analysis to date. [src: discoveries]

## Literature Context

The candidate papers broadly support the idea that resistance is shaped by isolation environment and antibiotic exposure, though most are reviews or single-species studies and not pan-bacterial surveys. Reviews describe the environment as the largest source of resistance genes, and they note that the extent of its contribution to resistance evolution is still under investigation [PMID 37258869](https://pubmed.ncbi.nlm.nih.gov/37258869/). They also describe resistance as a natural feature of diverse ecosystems. Not all resistance genes are likely to disseminate geographically or phylogenetically, but the ones that do pose a serious threat [PMID 28392565](https://pubmed.ncbi.nlm.nih.gov/28392565/). A commentary on a soil study reports little evidence of horizontal gene transfer (HGT) in soil. It suggests this may reflect weak selective pressure there [PMID 25213620](https://pubmed.ncbi.nlm.nih.gov/25213620/).

Single-species genomic studies mostly agree that clinical isolates carry more resistance. In 125 *Pseudomonas aeruginosa* isolates, antimicrobial resistance was seen only in clinical isolates and not in environmental ones. The authors attribute this to antibiotic exposure-driven selection. Genomic diversity did not track isolation source, so the species' breadth of niches appeared to rest on a broadly conserved genome and not on niche-specific accessory genes [PMID 41641989](https://pubmed.ncbi.nlm.nih.gov/41641989/), [PMID 41040319](https://pubmed.ncbi.nlm.nih.gov/41040319/). In *Acinetobacter johnsonii*, clinical isolates accumulated more genes for β-lactamase and defence mechanisms and carried resistance islands, while environmental isolates were enriched in genes for substance degradation [PMID 34600047](https://pubmed.ncbi.nlm.nih.gov/34600047/). A Ghanaian *Klebsiella* One Health study found that ESBL, carbapenemase and virulence genes were predominantly present only in hospital samples. Several other AMR gene classes were relatively frequent in non-clinical sources [PMID 37858320](https://pubmed.ncbi.nlm.nih.gov/37858320/). In Norwegian *K. pneumoniae* species complex isolates, human isolates carried higher overall plasmid burdens and most AMR-encoding plasmids. Plasmid clusters were also shared across human, animal and marine sources [PMID 41712274](https://pubmed.ncbi.nlm.nih.gov/41712274/).

The corpus findings are consistent with this picture. The 10.6 AMR clusters per clinical species in amr_pangenome_atlas, the 2.5× clinical excess in amr_environmental_resistome and the high accessory share of *K. pneumoniae* resistance all point the same way as the single-species studies. The *Klebsiella* plasmid work fits the report's interpretation that the near-entirely accessory *K. pneumoniae* resistome reflects HGT in clinical settings [PMID 41712274](https://pubmed.ncbi.nlm.nih.gov/41712274/). That interpretation is not tested by the report itself. The *P. aeruginosa* result partly contrasts with a species-level view. It reports no source-linked accessory signature, while the corpus finds less-core AMR in diverse environments. This is a different measure, so it is not a direct conflict. The *P. aeruginosa* study is also small, at 125 isolates.

The corpus extends this literature mainly in scale and in its continuous predictors. It links clinical genome fraction (rho = 0.465 across 823 species) and AlphaEarth embeddings to AMR across thousands of species. None of the candidate papers tests these predictors, so that part is novel relative to this evidence. The Ghanaian finding that some AMR classes occur outside hospitals is a reminder that the corpus's species-level environment labels cover only 53.2% of AMR-carrying species. Sampling bias toward pathogens also remains unaddressed. Metagenomic reviews on resistome methods and source tracking are relevant to the proposed community-level follow-up [PMID 28673041](https://pubmed.ncbi.nlm.nih.gov/28673041/), [PMID 33086465](https://pubmed.ncbi.nlm.nih.gov/33086465/).

## AMR load by isolation environment

Species from clinical settings carry the most AMR clusters per species, and the differences across environments are statistically significant. In amr_pangenome_atlas, Human/Clinical species carry 10.6 AMR clusters per species (n=2,248). Soil/Terrestrial species carry 4.6 (n=2,469), Aquatic 3.9 (n=1,827) and Animal 3.0 (n=959). [src: amr_pangenome_atlas] The Kruskal-Wallis test gives H=440, p=7.0e-93. [src: amr_pangenome_atlas] That report describes clinical species as carrying 2.7x more AMR. [src: amr_pangenome_atlas]

amr_environmental_resistome reports that clinical and human gut species carry 2.5× more AMR clusters than soil or aquatic species. It says the excess is almost entirely in the accessory (acquired) gene pool. [src: amr_environmental_resistome] The amr_strain_variation report also finds that host-associated species carry more AMR genes per genome than terrestrial or aquatic species. This holds under two environment classifiers, a rule-based keyword scheme approximating BacDive categories and NCBI keyword annotation (Kruskal-Wallis, p < 0.05). The two classifiers agree in direction, and human-clinical isolates show the highest burden. [src: amr_strain_variation]

## Accessory fraction and conservation

Clinical AMR is less conserved than environmental AMR. amr_pangenome_atlas reports a core fraction of 30.8% for clinical AMR, against 58.1% for soil and 63.1% for plant. It interprets this as clinical selection for acquired or mobile resistance, while environmental AMR is mostly intrinsic. [src: amr_pangenome_atlas] Species sampled from more diverse environments also have less-core AMR genes (rho=-0.173, p=1.8e-19). [src: amr_pangenome_atlas] The central digest summarises amr_environmental_resistome as 68% accessory AMR in clinical species versus 43% in soil species. [src: discoveries] See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

## Clinical fraction within species

amr_environmental_resistome used a species-level proxy. It tests whether species with mostly clinical-source genomes carry more AMR than species with mostly environmental-source genomes. [src: amr_environmental_resistome] The report notes this is not a true per-genome within-species comparison, which would need billion-row joins. [src: amr_environmental_resistome]

Among 823 species with genomes in ≥2 environments (≥5 genomes each), clinical genome fraction predicts total AMR cluster count (Spearman rho = 0.465, p = 2.2×10⁻⁴⁵). The report calls this its strongest evidence that AMR accumulation tracks antibiotic exposure at the strain level. [src: amr_environmental_resistome] The central digest repeats this result for 823 multi-environment species (rho=0.465, p=2.2e-45). [src: discoveries] The digest also says the analysis extends Gibson et al. (2015, 6K genomes) by 50×. [src: discoveries] Elsewhere in the same report, 884 species are said to qualify for within-species analysis. [src: amr_environmental_resistome] That figure differs from the 823 in the analysis table, and the report does not reconcile them in these claims. [src: amr_environmental_resistome]

Clinical-dominated species have 4.4× more AMR clusters than environment-dominated species (mean 72.9 vs 16.4, MWU p = 2×10⁻¹⁸). [src: amr_environmental_resistome] MWU is the Mann-Whitney U test. They also have a higher accessory AMR fraction in the grouped comparison (93.6% vs 81.7%, MWU p = 0.004). [src: amr_environmental_resistome] The continuous correlation of clinical fraction with percent accessory AMR is only borderline (rho = 0.065, p = 0.064). [src: amr_environmental_resistome] The report concludes that AMR accumulation varies within species depending on where strains are found. [src: amr_environmental_resistome]

### Species case studies

The report's five case-study species differ widely in AMR cluster count, and nearly all of their clusters are accessory. [src: amr_environmental_resistome] Each item gives genomes, AMR clusters, core clusters, accessory clusters and dominant environment.

- *K. pneumoniae*: 13,637 genomes, 1,115 AMR clusters, 7 core, 1,108 accessory (99%), Clinical (80%). [src: amr_environmental_resistome]
- *S. aureus*: 13,274 genomes, 642 AMR clusters, 9 core, 633 accessory (99%), Clinical (85%). [src: amr_environmental_resistome]
- *S. enterica*: 10,097 genomes, 836 AMR clusters, 11 core, 825 accessory (99%), Host-associated (31%). [src: amr_environmental_resistome]
- *S. pneumoniae*: 7,944 genomes, 59 AMR clusters, 1 core, 58 accessory (98%), Clinical (99.6%). [src: amr_environmental_resistome]
- *M. tuberculosis*: 6,673 genomes, 44 AMR clusters, 4 core, 40 accessory (91%), Clinical (98%). [src: amr_environmental_resistome]

The report interprets the nearly all-accessory *K. pneumoniae* resistome as massive within-species variation driven by horizontal gene transfer (HGT) in clinical settings. This is an interpretation, not a test. [src: amr_environmental_resistome] See [[entities/klebsiella-pneumoniae]].

## Environmental embeddings

Continuous environmental embeddings point the same way. Among 2,659 species with AMR data and AlphaEarth embeddings, 52 of 64 embedding dimensions correlate with AMR diversity (FDR < 0.05, false discovery rate). The top dimension is A34 (rho = +0.24). [src: amr_environmental_resistome] A Mantel test finds that embedding cosine distance predicts Bray-Curtis distance of AMR mechanism fractions (r = 0.098, p = 0.001). [src: amr_environmental_resistome] The coupling is strongest in clinical species (r = 0.177), moderate in soil (r = 0.129) and weakest in aquatic (r = 0.061). [src: amr_environmental_resistome]

amr_pangenome_atlas analysed 2,684 species with ≥3 genomes and embeddings. It found that environmental diversity predicts AMR count (Spearman rho=0.466, p=1.6e-144). [src: amr_pangenome_atlas] The report suggests the hypothesis that niche breadth enables resistance accumulation through more horizontal-transfer opportunities. It says this aligns with the environmental reservoir hypothesis. [src: amr_pangenome_atlas] See [[entities/alphaearth-environmental-embeddings]].

## Tensions and caveats

- The embedding analysis confirms the discrete results but adds little interpretability, because the dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome] amr_pangenome_atlas likewise notes that embeddings exist for only 28% of genomes, biased toward genomes with geographic metadata. [src: amr_pangenome_atlas]
- Of 14,723 AMR-carrying species, only 7,838 (53.2%) have a classified environment, and the Kruskal-Wallis test uses only these. [src: amr_pangenome_atlas] The Other/Unknown bin holds 46.8% of species, reflecting sparse, inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- Genome databases over-represent clinical pathogens, which inflates AMR counts for human-associated species. [src: amr_pangenome_atlas]
- The report says its clinical–environmental comparison extends Hua et al.'s US isolate findings to 7,838 species. [src: amr_pangenome_atlas]
- The reports claim novelty for linking AlphaEarth diversity to AMR accumulation and for showing clinical AMR is more acquired and less core. [src: amr_pangenome_atlas]

## Open Directions

- Use nmdc_arkin metagenome taxonomic profiles to infer community AMR load from species AMR profiles. This would test whether species-level findings hold in real environmental communities.
- Map AMR gene prevalence in NMDC/MGnify communities. This would show whether the accessory AMR genes seen in isolates are also prevalent in community DNA.
- Redo the clinical-exposure test per genome with Fisher's exact test within species. This would replace the species-level proxy.
- Repeat the environment comparisons with sampling-bias correction, for example down-weighting over-sampled pathogens. This would show how much of the clinical excess is a database artefact.
