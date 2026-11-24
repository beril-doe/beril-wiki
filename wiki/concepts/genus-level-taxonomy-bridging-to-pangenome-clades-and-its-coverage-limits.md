---
type: "Concept"
description: "How mapping community taxa labelled only to genus onto GTDB species clades creates unmapped and ambiguous taxa, and how strict, relaxed and species-proxy modes trade coverage against resolution."
sources: ["summaries/discoveries.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Genus-level taxonomy bridging to pangenome clades and its coverage limits

Mapping community taxa labelled only to genus onto GTDB species clades leaves some genera unmapped and others ambiguous. In the ENIGMA contamination analysis, 862 of 1,392 observed genera were unmapped [src: enigma_contamination_functional_potential], and the 530 mapped genera split into 150 unique-clade genera and 380 ambiguous multi-clade genera. [src: enigma_contamination_functional_potential] Other projects report their own genus-level coverage figures from different datasets. In the plant microbiome work, the NMDC bridge lost 62 genera (19.3%), and the effect of that loss on a complementarity test is unknown. [src: plant_microbiome_ecotypes] See also [[concepts/taxonomy-bridging-between-metagenomic-classifiers-and-reference-pangenomes]] and [[entities/genus-to-species-clade-taxonomy-bridge]].

## Literature Context

The two candidate papers speak to why genus-level labels limit taxonomic resolution and what higher-resolution profiling can offer. They do not test genus-to-GTDB clade bridging directly. In a comparison of mock bacterial communities, the Assembly-Binning-Method and rpoB metabarcoding showed comparable sensitivity and precision, while k-mer approaches produced a notably high number of false negatives [PMID 40615957](https://pubmed.ncbi.nlm.nih.gov/40615957/). In some cases the Assembly-Binning-Method improved resolution by identifying taxa at the species level rather than the genus level. It also correlated better with expected abundances than rpoB metabarcoding did [PMID 40615957](https://pubmed.ncbi.nlm.nih.gov/40615957/). This evidence comes from artificially generated mock communities, so it may not carry over to environmental samples.

The second paper is an integrated mouse gut metagenome catalog (iMGMC) with 660 metagenome-assembled genomes (MAGs). More than 92% of those MAGs lack species-level representatives in public repositories (<95% ANI match) [PMID 32130896](https://pubmed.ncbi.nlm.nih.gov/32130896/). Linking MAGs to 16S rRNA gene data allowed more accurate prediction of community functional profiles than 16S amplicons alone [PMID 32130896](https://pubmed.ncbi.nlm.nih.gov/32130896/). This result is specific to the mouse gut. It shows that species-level reference coverage can be thin in that habitat. It does not show how a species-level bridge would perform in the ENIGMA or other environmental datasets.

The corpus findings are consistent with this literature on the main point and extend it in a specific way. The ENIGMA taxonomy stops at genus, and 862 of 1,392 observed genera were unmapped. Of the 530 mapped genera, 380 were ambiguous multi-clade genera and 150 mapped to a unique clade. The shotgun and metagenome-based work supports the corpus proposal that species or strain resolution needs metagenomic data or a higher-resolution pipeline rather than genus labels [PMID 40615957](https://pubmed.ncbi.nlm.nih.gov/40615957/). The corpus also suggests that the species-proxy mode did not gain inference. It kept only 150 clades, with a mean mapped abundance fraction of 0.031. Its site_defense_score trend was positive but not significant (rho = 0.169, p = 0.081), and no high-coverage subset test was feasible. The report suggests that stricter resolution reduced analyzable signal without strengthening inference. This is the report's interpretation rather than an established conclusion. It neither contradicts nor is tested by the candidate papers.

The corpus's quantitative coverage figures are novel relative to these papers. They include the strict and relaxed mode clade counts of 530 and 7,380, and the 1,140 of 1,590 genus-feature pairs that differed when the two modes were built independently. Neither candidate paper reports comparable bridge-coverage statistics. The iMGMC result does suggest that a species-level bridge built on public references could miss many mouse gut genomes. The corpus's own claims about unmapped genera therefore still need direct testing, as in the Open Directions. See [[concepts/taxonomy-bridging-between-metagenomic-classifiers-and-reference-pangenomes]].

## Why the bridge stops at genus

The ENIGMA taxonomy table ddt_brick0000454 provides labels only through Genus, with no species or strain rows. [src: discoveries, enigma_contamination_functional_potential, pitfalls] A species-level bridge attempted on such data can fail or silently reuse genus-level mappings while appearing higher resolution. [src: pitfalls] The pangenome-to-ENIGMA bridge is therefore genus-level at best, and one report avoids isolate-specific transfer of pangenome reconstructions in favor of direct genome_depot annotation. [src: enigma_carbon_census_1] Genus-level mapping may also mask strain-level adaptation. [src: enigma_contamination_functional_potential]

## Coverage and ambiguity in ENIGMA

Of 1,392 observed genera, most were unmapped, and among the mapped genera more were ambiguous than unique. [src: enigma_contamination_functional_potential]
- Upstream outputs contained 1,392 observed genera, of which 530 were mapped and 862 unmapped. [src: enigma_contamination_functional_potential]
- NB02 built a genus-normalized bridge from 27,690 parsed GTDB species rows, mapping 530 genera and leaving 862 unmapped. [src: enigma_contamination_functional_potential]
- The bridge table had 8,242 rows from many-to-many genus-to-clade expansion. [src: enigma_contamination_functional_potential]
- 150 genera mapped to a unique clade, and 380 were ambiguous multi-clade genera. [src: enigma_contamination_functional_potential]
- The clade-count distribution has a long right tail, with a maximum of 433 clades per genus. [src: enigma_contamination_functional_potential]
- The most ambiguous genera were pseudomonas (433), streptomyces (378), prevotella (358), streptococcus (214) and mycobacterium (186). [src: enigma_contamination_functional_potential]

## Strict, relaxed and species-proxy modes

The three modes trade coverage against resolution. The strict mode had 530 clades and the relaxed mode 7,380. [src: enigma_contamination_functional_potential] The species-proxy mode keeps only genera that map to exactly one GTDB species clade, to approximate higher resolution when taxonomy stops at genus. [src: enigma_contamination_functional_potential] It had 150 clades. [src: enigma_contamination_functional_potential]

Mean mapped abundance fraction was 0.343 in strict/relaxed modes (range 0.031 to 0.854) and 0.031 in species-proxy mode (range 0.0002 to 0.543). [src: enigma_contamination_functional_potential, discoveries]

In the species-proxy mode, the site_defense_score trend was positive but not significant (rho = 0.169, Spearman p = 0.081). [src: enigma_contamination_functional_potential, discoveries] No high-coverage subset test was feasible at mapped_abundance_fraction >= 0.25. [src: enigma_contamination_functional_potential] The report suggests that stricter resolution currently reduces analyzable signal without strengthening inference. [src: enigma_contamination_functional_potential] It says true species-level gains likely need higher-resolution taxonomy or metagenomic mapping. [src: discoveries]

### Strict versus relaxed must be built independently

When strict and relaxed features were computed independently in NB02, 1,140 of 1,590 genus-feature pairs differed (~71.7%). [src: discoveries] Site stress scores differed for all 108 samples. [src: discoveries] Copying strict features into relaxed features gives identical downstream outputs and invalidates the sensitivity conclusions. [src: pitfalls] The report says this sensitivity should not be approximated by copied tables. [src: discoveries] It proposes precomputing clade-level annotation counts on the union of clades and aggregating them separately per mode. [src: pitfalls]

## Proposed remedies

The ENIGMA report proposes increasing taxonomic resolution through a species/strain-level bridge from metagenomic or higher-resolution ENIGMA taxonomy, and quantifying gains over genus and species-proxy modes. [src: enigma_contamination_functional_potential] It also proposes investigating how unmapped genera contribute to contamination gradients and where the bridge could be expanded. [src: enigma_contamination_functional_potential] For genus-only taxonomy, the pitfalls digest proposes either an explicit species-proxy mode with mapped-coverage loss reported, or a switch to other data sources. [src: pitfalls] It names metagenomes and an ASV (amplicon sequence variant) reclassification pipeline as sources that support species/strain resolution. [src: pitfalls]

## Coverage in other projects

Other projects also bridge at genus and report their own coverage.
- In NMDC community metabolic ecology, mean bridge coverage was 94.6%, and all 220 samples passed the 30% QC (quality control) threshold. [src: nmdc_community_metabolic_ecology] 92% of samples mapped at least 85% of community abundance to GTDB pangenome species. [src: nmdc_community_metabolic_ecology]
- For about 1,352 Centrifuge taxa matching several clades in a genus, one representative clade was chosen by alphabetical tiebreaking. [src: nmdc_community_metabolic_ecology] Genus-proxy-ambiguous taxa account for ~6.5% of mapped abundance, which bounds the sensitivity to that choice. [src: nmdc_community_metabolic_ecology]
- In PHB (polyhydroxybutyrate) granule ecology, a two-tier mapping (2,336 columns via gtdb_metadata taxid, 678 via taxonomy_dim) mapped 3,014/3,492 (86.3%) NMDC taxon columns. [src: phb_granule_ecology]
- In the dark-gene validation, 5 of 6 carrier genera mapped to 47 NMDC taxon columns across 6,365 metagenomic samples. [src: functional_dark_matter] Genus resolution may miss species-specific signals. [src: functional_dark_matter] The high significance rate (76/105) likely reflects common genera dominating both datasets. [src: functional_dark_matter]
- In plant microbiome ecotypes, the NMDC bridge matched 260 of 322 genera (80.7%) and lost 62 genera (19.3%). [src: plant_microbiome_ecotypes] Sensitivity analysis of the loss was deferred. [src: plant_microbiome_ecotypes]
- The plant microbiome report states that the impact of the unmatched genera on its complementarity hypothesis (H3) is unknown. If the unmatched genera include key complementary partners, the observed redundancy signal could be artifactual. [src: plant_microbiome_ecotypes] See [[concepts/functional-redundancy-versus-complementarity-among-co-occurring-genera]].
- In the MicrobeAtlas PRJNA1084851 analysis, 1,637 OTUs (operational taxonomic units), representing 16.8% of reads, could be joined to genus metal diversity data. [src: microbeatlas_metal_ecology] Citrobacter and Thermodesulfovibrio were not detected, possibly because they were below detection or their genus names mismatched SILVA nomenclature. [src: microbeatlas_metal_ecology]
- In genotype-to-phenotype work, species-level biogeography exists for only 20 pangenome-linked ENIGMA strains with verified GTDB matches. [src: genotype_to_phenotype_enigma] Matching through ncbi_strain_identifiers caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]

These figures come from different datasets and are not directly comparable.

## Open Directions

- Quantify how much the unmapped ENIGMA genera (862 of 1,392) contribute to contamination gradients, to size the gain from expanding the bridge.
- Build a species or strain-level bridge from metagenomes or an ASV reclassification pipeline, and measure gains over genus and species-proxy modes.
- Run the deferred sensitivity analysis of the 80.7% NMDC genus match in the plant microbiome work, including whether the 62 lost genera hold complementary partners that would change the H3 redundancy signal.
- Test whether the choice of representative clade for ambiguous genera such as pseudomonas shifts results beyond the ~6.5% bound.
