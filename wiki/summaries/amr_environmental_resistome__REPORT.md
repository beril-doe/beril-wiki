---
type: "Summary"
description: "Pangenome-scale analysis links environmental niche to AMR diversity and mechanism."
doc_type: "short"
full_text: "sources/amr_environmental_resistome__REPORT.md"
---
# Environmental Resistome at Pangenome Scale

## Overview

This report analyzes antimicrobial-resistance (AMR) gene clusters across 14,723 bacterial species and 293K genomes using the KBase KE pangenome collection. It finds that ecological niche is associated with AMR diversity, core/accessory composition, and resistance-mechanism composition, with clinical and human-gut species carrying more predominantly acquired AMR than soil and aquatic species. The associations persist under phylum- and family-level phylogenetic controls, although the study is observational and subject to sampling, classification, and annotation limitations. [src: amr_environmental_resistome]

## Key Findings

### 1. Clinical species carry more AMR gene clusters

Clinical-source species had a median of 5 AMR gene clusters, compared with 2 for soil, aquatic, and host-associated species, a 2.5× difference (Kruskal–Wallis H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056). Human-gut species also had a median of 5. Of 15 pairwise environment comparisons, 13 were significant after false-discovery-rate (FDR) correction; the largest effect was clinical versus aquatic (rank-biserial r = −0.49). The association held at 50%, 60%, 75%, and 90% majority-vote environment-classification thresholds, with η² = 0.044–0.056. The analysis extends the approximately 6,000-genome ecology-resistome result of Gibson et al. (2015) to 14,723 species across 293K genomes. [src: amr_environmental_resistome]

### 2. Clinical and gut resistomes are predominantly accessory

Clinical species had 68% accessory AMR, compared with 43% in soil species (Kruskal–Wallis H = 506.0, p = 4×10⁻¹⁰⁷, η² = 0.036). Mean core and accessory AMR fractions were: soil 57.1% and 42.9%; aquatic 54.4% and 45.6%; host-associated 49.7% and 50.3%; other environmental 40.4% and 59.6%; clinical 32.4% and 67.6%; and human gut 19.7% and 80.3%, respectively. The report interprets core AMR as predominantly chromosomally encoded and intrinsic, and accessory AMR as predominantly mobile and acquired, consistent with the cited river-metagenome result from Jiang et al. (2024). [src: amr_environmental_resistome]

### 3. Resistance-mechanism composition depends on environment

All four tested mechanisms showed significant environment-dependent composition after Benjamini–Hochberg FDR correction. Metal resistance represented 45.0% of AMR in aquatic species and 44.0% in soil species, but 6.1% in human-gut species (η² = 0.107). Target modification represented 43.6% in human-gut species and 27.5% in clinical species, but 6.2% in aquatic species (η² = 0.100). The complete mechanism fractions were: efflux, clinical 6.1%, human gut 7.0%, host-associated 3.7%, soil 2.0%, aquatic 1.1%, and other environmental 2.7% (η² = 0.055); enzymatic inactivation, 28.2%, 24.1%, 44.1%, 34.3%, 41.2%, and 33.6% (η² = 0.019); metal resistance, 19.7%, 6.1%, 12.7%, 44.0%, 45.0%, and 24.9% (η² = 0.107); and target modification, 27.5%, 43.6%, 22.8%, 10.1%, 6.2%, and 25.1% (η² = 0.100), in the same environment order. [src: amr_environmental_resistome]

The report interprets soil and aquatic enrichment for metal resistance as consistent with natural heavy-metal exposure, and clinical and gut enrichment for target modification and, to a lesser extent, efflux as consistent with antibiotic selection pressure. It connects this pattern to the reported mechanism-conservation result that metal resistance was 44% accessory whereas efflux was 13% core, proposing that efflux genes serve host-associated organisms across conditions while metal-resistance genes vary with metal exposure. This ecological explanation is an interpretation rather than a causal test. [src: amr_environmental_resistome]

Of the AMR clusters, 15,550 (18.7%) could not be assigned to a mechanism from gene name or product annotation and were excluded from mechanism fractions. Tetracycline-resistance genes were divided between efflux (tet(A-E,K,L)) and target modification (tet(M,O,Q,W) ribosomal-protection proteins). [src: amr_environmental_resistome]

### 4. Clinical representation predicts AMR within species

Among 823 species with genomes in at least 2 environments and at least 5 genomes each, the fraction of genomes from clinical sources predicted total AMR cluster count (Spearman rho = 0.465, p = 2.2×10⁻⁴⁵). Clinical-dominated species had a mean of 72.9 AMR clusters versus 16.4 in environmental-dominated species, a 4.4× difference (Mann–Whitney U test p = 2×10⁻¹⁸), and had a higher grouped accessory fraction (93.6% versus 81.7%, p = 0.004). The continuous correlation between clinical fraction and accessory percentage was borderline (rho = 0.065, p = 0.064). This is a species-level proxy, not a true per-genome within-species comparison. [src: amr_environmental_resistome]

Deeply sampled case studies were: *Klebsiella pneumoniae*, 13,637 genomes, 1,115 AMR clusters, 7 core and 1,108 accessory (99%), clinical-dominant at 80%; *Staphylococcus aureus*, 13,274 genomes, 642 clusters, 9 core and 633 accessory (99%), clinical-dominant at 85%; *Salmonella enterica*, 10,097 genomes, 836 clusters, 11 core and 825 accessory (99%), host-associated-dominant at 31%; *Streptococcus pneumoniae*, 7,944 genomes, 59 clusters, 1 core and 58 accessory (98%), clinical-dominant at 99.6%; and *Mycobacterium tuberculosis*, 6,673 genomes, 44 clusters, 4 core and 40 accessory (91%), clinical-dominant at 98%. *K. pneumoniae* had only 7 core clusters among 1,115, illustrating extensive accessory AMR variation in a clinically dominated species. [src: amr_environmental_resistome]

### 5. Environment effects persist after phylogenetic control

At the phylum level, 5 of 6 major phyla—Pseudomonadota, Bacillota_A, Actinomycetota, Bacteroidota, and Bacillota—showed significant within-phylum environment effects on AMR; Chloroflexota was non-significant. Bacteroidota had the largest within-phylum effect (η² = 0.130). At the family level, 20 of 141 testable families (14%) showed significant within-family environment effects after FDR correction; the strongest listed results were Enterobacteriaceae (q = 3×10⁻²¹), Bacteroidaceae (q = 1.3×10⁻¹⁷), Lachnospiraceae (q = 2.5×10⁻¹²), and Pseudomonadaceae (q = 3.9×10⁻¹²). These results support an ecological association that is not solely a proxy for phylogeny, while most families lacked enough environmental breadth for testing. [src: amr_environmental_resistome]

### 6. Continuous environmental embeddings support the discrete analysis

Among 2,659 species with both AMR data and AlphaEarth environmental embeddings, 52 of 64 embedding dimensions significantly correlated with AMR diversity at FDR < 0.05; the top dimension was A34 (rho = +0.24). A Mantel test found that environmental distance, measured as cosine distance between embeddings, predicted AMR-profile distance, measured as Bray–Curtis distance between mechanism fractions (r = 0.098, p = 0.001). Stratified correlations were strongest for clinical species (r = 0.177), moderate for soil (r = 0.129), and weakest for aquatic species (r = 0.061). The report treats this as supplementary confirmation with limited interpretability because embedding dimensions are opaque and coverage was 28% of genomes. [src: amr_environmental_resistome]

## Data Assembly and Statistical Results

The assembled data contained 82,908 AMR gene clusters across 14,723 species out of 27,700 total species; 280,337 genomes had NCBI environment metadata, of which 93.5% were classified per genome. Species-level majority-vote environment classifications covered 95% of species (13,981 species). A total of 884 species qualified for the initial within-species criterion of at least 5 genomes in at least 2 environments, while the reported within-species analysis included 823 species. Mechanism classification assigned 26,220 clusters to enzymatic inactivation, 22,223 to metal resistance, 11,067 to target modification, and 5,224 to efflux. [src: amr_environmental_resistome]

The reported Kruskal–Wallis tests were: AMR count by environment, H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056; core AMR percentage by environment, H = 506.0, p = 4×10⁻¹⁰⁷, η² = 0.036; metal resistance, H = 1498.4, p ~ 0, η² = 0.107; target modification, H = 1394.9, p = 1.7×10⁻²⁹⁹, η² = 0.100; efflux, H = 768.0, p = 9.8×10⁻¹⁶⁴, η² = 0.055; and enzymatic inactivation, H = 266.0, p = 2.0×10⁻⁵⁵, η² = 0.019. [src: amr_environmental_resistome]

## Caveats and Unperformed Analyses

Environment and phylogeny remain deeply entangled despite family-level controls; some families are nearly entirely clinical, and only 14% of tested families showed significant within-family effects. NCBI sampling strongly overrepresents clinical isolates, while soil and aquatic species are undersampled, potentially inflating the clinical-versus-environmental contrast. Majority-vote species classifications collapse within-species variation, although sensitivity analyses at 60–90% thresholds partly mitigate this issue. [src: amr_environmental_resistome]

AMRFinderPlus-focused annotation may underestimate novel environmental resistance and bias results toward clinical enrichment, where resistance genes are better characterized. The 95% prevalence threshold for core AMR is dependent on species genome count, so core/accessory labels are imprecise for sparsely sampled species. The association is correlational: clinical exposure could increase AMR, AMR could contribute to clinical isolation, or both could reflect virulence-resistance co-selection. [src: amr_environmental_resistome]

Effect sizes were modest despite very small p-values: environment explained 2–13% of variance in AMR composition (η² = 0.02–0.13), while phylogeny likely explains more. The 18.7% of clusters (15,550) lacking mechanism assignments may bias mechanism comparisons if unclassified clusters are distributed non-randomly across environments. [src: amr_environmental_resistome]

Planned but unperformed analyses included PCoA ordination, PERMANOVA, environment-specific gene identification, metagenome-assembled genome/isolate assessment, and an archaea-specific analysis. The originally planned per-genome Fisher’s exact test was replaced by the species-level within-species proxy because billion-row joins were computationally costly. [src: amr_environmental_resistome]

## Slots Into

- [[concepts/pangenome-integration]] — adds a 14,723-species, 293K-genome demonstration that pangenome-scale core/accessory AMR composition varies with ecological environment.
- [[concepts/multi-omics-integration]] — provides environmental embeddings and mechanism-level AMR profiles as an ecological integration layer, while showing that continuous embedding dimensions have limited interpretability.
- [[concepts/condition-specific-fitness]] — supplies environment-associated AMR mechanism and conservation patterns that can motivate tests of whether resistance costs and persistence differ across ecological niches.
- [[concepts/environmental-resistome]] — provides the central synthesis of environment-structured AMR diversity, mechanism composition, and within-species clinical enrichment.
