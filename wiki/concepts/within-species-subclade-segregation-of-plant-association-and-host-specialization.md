---
type: "Concept"
description: "Whether plant-associated genomes cluster in core-phylogeny subclades within species and segregate by plant host, including the genome-ID linkage failure and limited tree coverage."
sources: ["summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Within-species subclade segregation of plant association and host specialization

This page asks whether plant-associated genomes cluster in core-phylogeny subclades within species, and whether those subclades segregate by plant host. In the plant_microbiome_ecotypes report, the answer is a weak yes: 5 of 17 testable species pass Bonferroni-corrected Fisher's exact test, concentrated in Xanthomonas and Pseudomonas, and two Xanthomonas species also segregate by host. [src: plant_microbiome_ecotypes] The evidence is limited by tree coverage, because only 18 of 65 candidate species have tree data. [src: plant_microbiome_ecotypes] An earlier null result was an identifier artifact, not biology. [src: plant_microbiome_ecotypes] See also [[summaries/plant_microbiome_ecotypes__REPORT]].

## Literature Context

The candidate papers give indirect context for the hub's question: whether host specialization tracks core phylogeny or is carried by accessory material. A comparative genomics study of 151 plant-associated bacteria found no common genetic basis for beneficial effects. Each of five beneficial groups shared specific gene sets, and the study reported putative host-specificity genes, mostly transcription factors, enzymes, transporters and chemotaxis regulators [PMID 30047115](https://pubmed.ncbi.nlm.nih.gov/30047115/). In *Fusarium oxysporum*, host-specific pathogenicity is determined by supernumerary chromosomes. These can transfer horizontally between lineages, which explains why the pathogenicity is polyphyletic while the core genome stays conserved [PMID 29153400](https://pubmed.ncbi.nlm.nih.gov/29153400/). In lagriamide-producing *Burkholderia* symbionts of Lagriinae beetles, the authors found no host-symbiont co-diversification and no monophyly of the symbionts. They inferred a single ancestral acquisition of the gene cluster followed by at least four independent symbiont acquisitions [PMID 39441990](https://pubmed.ncbi.nlm.nih.gov/39441990/). A clade of plant-associated relatives in that study kept large genomes and secondarily lost the cluster. Population genomics of *Macrophomina* (463 isolates) found that strawberry-pathogenic isolates fell in a single lineage. It also found associations between soybean isolation and specific population clusters, so specialization can occur within one species that has both specialist and generalist populations [PMID 40555251](https://pubmed.ncbi.nlm.nih.gov/40555251/). An *Alternaria linariae* genome from a single strain reported 221 candidate effector genes and some unique effectors. The authors suggest these may help the fungus colonize tomato, but this is a hypothesis for further investigation, not an established link to host specificity [PMID 40624476](https://pubmed.ncbi.nlm.nih.gov/40624476/).

The corpus finding is that 5 of 17 testable species show plant-association subclade clustering. Two Xanthomonas species also segregate by host: *X. campestris* with Brassica and *X. vasicola* with *Zea mays*. This is consistent with the picture above. Host-related traits can be structured within a species, as in *Macrophomina*, but accessory or horizontally mobile elements are a plausible driver, as in *Fusarium* and the *Burkholderia* symbionts. The corpus's weak, genus-concentrated support, and its interpretation that accessory cassettes stratify onto core subclades in Xanthomonas, fit this mixed pattern. None of these papers tests the same subclade-by-host question in bacterial pangenomes. The broader corpus result is therefore best described as extending the literature, not confirming it directly. The 151-genome study used cross-species comparisons, not within-species subclade tests. The fungal and symbiont examples are different kingdoms or lifestyles, so they are analogies only.

The corpus's genome-ID linkage failure and its tree-coverage limit (18 of 65 species) have no counterpart in these papers, so they are novel, methodological points. The corpus's call for accessory-gene profiling is consistent with the horizontal-transfer emphasis in the *Fusarium* review [PMID 29153400](https://pubmed.ncbi.nlm.nih.gov/29153400/).

## Subclade segregation of plant association

Of 17 testable species (≥3 plant and ≥3 non-plant genomes), 5 (29%) pass Bonferroni-corrected Fisher's exact test at α = 0.05/17 = 0.0029. [src: plant_microbiome_ecotypes] Twelve testable species show no such clustering. [src: plant_microbiome_ecotypes] The report's final verdict is weak support, with *X. vasicola*, *P. avellanae* and *X. campestris* strongest. [src: plant_microbiome_ecotypes] Of these, 3 are also Cochran-valid. [src: plant_microbiome_ecotypes]

| Species | N | Plant genomes | Best subclade % plant | Fisher p | Cochran-valid chi² |
|---|---|---|---|---|---|
| Xanthomonas vasicola | 101 | 30 | 71% | 1.6×10⁻⁴ | yes [src: plant_microbiome_ecotypes] |
| Mesorhizobium sp002294985 | 84 | 78 | 97% | 1.1×10⁻⁴ | no, small cells (Fisher only) [src: plant_microbiome_ecotypes] |
| Agrobacterium pusense | 80 | 13 | 100% | 4.5×10⁻⁴ | no, small cells (Fisher only) [src: plant_microbiome_ecotypes] |
| Pseudomonas_E avellanae | 319 | 68 | 31% | 7.3×10⁻⁴ | yes [src: plant_microbiome_ecotypes] |

Xanthomonas campestris is the fifth species, with p = 1.0×10⁻³. [src: plant_microbiome_ecotypes] Three of the five also satisfy Cochran's rule for chi² and are the most robust results. The other two pass only Fisher's exact test, which is exact and not subject to the small-cell constraint. [src: plant_microbiome_ecotypes]

The pattern is concentrated in Xanthomonas and Pseudomonas, genera known for pathovar-level host specialization, plus Mesorhizobium and Agrobacterium. [src: plant_microbiome_ecotypes] Among 30 dossier genera, 4 contain a significant species. [src: plant_microbiome_ecotypes] The borderline chi² p = 0.031 for *P. amygdali* in the earlier 5-species subset does not survive Bonferroni in the larger scan and stays invalid under Cochran's rule. [src: plant_microbiome_ecotypes] The earlier draft flagged *P. amygdali* by chi² alone, but that result fails Cochran's rule and Fisher's 2×2 collapse. [src: plant_microbiome_ecotypes]

## Host specialization within subclades

Host assignment covered 1,307 species across 19 testable hosts (≥10 species each). [src: plant_microbiome_ecotypes] Rice (*Oryza sativa*) was the most common host with 286 species, followed by *Arabidopsis thaliana* (184), wheat (122) and maize (98). [src: plant_microbiome_ecotypes]

Of 9 species with enough host annotation (≥5 host-annotated genomes, ≥2 hosts, ≥2 subclades), 2 pass both within-species and across-species Bonferroni. [src: plant_microbiome_ecotypes] *X. campestris* segregates to Brassica hosts: 46/47 genomes in subclade 2 are on Brassica, p = 2.7×10⁻¹² raw and 3.3×10⁻¹¹ after within-species Bonferroni. [src: plant_microbiome_ecotypes] *X. vasicola* segregates to *Zea mays*: 47/52 genomes in subclade 0, p = 1.4×10⁻¹¹ raw and 1.7×10⁻¹⁰ after Bonferroni. [src: plant_microbiome_ecotypes] The report reads both as canonical pathovar-host specializations confirmed at the genomic level. [src: plant_microbiome_ecotypes] *Ralstonia solanacearum* passes BH-FDR (Benjamini-Hochberg false discovery rate) but not across-species Bonferroni, with p = 5.9×10⁻³ within and q-BH 1.8×10⁻². [src: plant_microbiome_ecotypes]

Xanthomonas is the only dossier genus with species showing both subclade segregation and host segregation. [src: plant_microbiome_ecotypes]

## The genome-ID linkage failure

The first analysis (NB12) reported no significant segregation, with 0/5 species significant, but this was caused by a genome identifier (ID) format mismatch. [src: plant_microbiome_ecotypes] The tree table stores bare NCBI accessions, while genome_environment.csv uses GTDB-prefixed IDs, so is_plant_associated was entirely NaN (not a number) after the merge. [src: plant_microbiome_ecotypes] In Phase 2 all 5 species therefore had 0 testable subclade × plant-association enrichments, because the plant-associated subset dropped to zero. [src: plant_microbiome_ecotypes] Prepending GB_ to GCA_ accessions and RS_ to GCF_ accessions gave 1306/1306 matches, up from 0, and recovered 599 plant-associated genomes. [src: plant_microbiome_ecotypes] The general failure mode is covered in [[concepts/join-key-validity-and-identifier-format-mismatches]].

After the fix, the original 5-species set shows 1/5 significant under all metrics. [src: plant_microbiome_ecotypes] The Phase 2b 65-species scan closed the genome-ID linkage and ran the 18 available species. [src: plant_microbiome_ecotypes] The full scan raises the count to 5/17 by including the broader candidate pool. [src: plant_microbiome_ecotypes] The report also concludes that the original 5 species, chosen by genome count, were too few for honest conclusions. [src: plant_microbiome_ecotypes]

## Limited tree coverage

Only 18 of 65 plant-associated species with ≥20 genomes (28%) have data in kbase_ke_pangenome.phylogenetic_tree_distance_pairs. [src: plant_microbiome_ecotypes] Put the other way, 47 of 65 candidate species lack tree coverage in the KBase Data Lakehouse. [src: plant_microbiome_ecotypes] See [[entities/kbase-ke-pangenome]]. The 47 missing species include *Bradyrhizobium japonicum*, *B. diazoefficiens*, *Mesorhizobium ciceri*, *Sinorhizobium medicae*, *Burkholderia glumae*, *Methylobacterium extorquens*, *Streptomyces scabiei*, *Xylella taiwanensis* and *Clavibacter michiganensis*. [src: plant_microbiome_ecotypes] The report calls this a database limitation, not a methodology issue, and says it bounds power regardless of method. [src: plant_microbiome_ecotypes] The true effect across all 65 species cannot be estimated until the GTDB tree is more completely populated. [src: plant_microbiome_ecotypes]

The subclade method is core-phylogeny-based. Accessory-gene presence/absence profiling as an alternative subclade definition remains outstanding. [src: plant_microbiome_ecotypes] So do gene-content versus species-tree comparisons, and both need larger gene-cluster-by-genome data pulls than this project executed. [src: plant_microbiome_ecotypes]

## Interpretation

The report reads the results as showing that within-species plant adaptation is predominantly accessory-driven. In specific genera, notably Xanthomonas, accessory cassettes have stratified onto core subclades, so pathovar designations have a real phylogenetic basis there. [src: plant_microbiome_ecotypes] This agrees with Melnyk et al. (2019), who found that *Pseudomonas* plant-lifestyle transitions are driven by convergent gain or loss of accessory genomic islands rather than core-genome phylogeny. [src: plant_microbiome_ecotypes] Satterwhite & Bergelson (2025) found local host adaptation in 3/5 *P. syringae* pathovars but only 1/5 locally dominant. [src: plant_microbiome_ecotypes] The report proposes, as an interpretation, horizontal acquisition of accessory gene clusters in any phylogenetic background. It adds that strain-level prediction needs accessory genome profiling, not core-genome phylotyping. [src: plant_microbiome_ecotypes] See [[entities/pseudomonas]].

## Tensions

- The report states a null H7 result, with no subclade-level segregation, and ties it to Melnyk et al.. [src: plant_microbiome_ecotypes] It also finds 5/17 species significant. [src: plant_microbiome_ecotypes] The null was traced to the ID mismatch [src: plant_microbiome_ecotypes], and after the fix 1/5 of the original species stays significant. [src: plant_microbiome_ecotypes]
- Downstream H7 support remained weak, at 1/5 species, after validity checks. [src: plant_microbiome_ecotypes] The extended scan gives 5/17. [src: plant_microbiome_ecotypes]

## Open Directions

- Populate or rebuild GTDB tree distances for the 47 missing species, such as *Bradyrhizobium japonicum* and *Xylella taiwanensis*, and rerun the subclade scan to estimate the effect across all 65 species.
- Run accessory-gene-content tests inside the significant subclades of Xanthomonas, Mesorhizobium and Agrobacterium to check whether accessory cassettes track subclades.
- Pull gene-cluster-by-genome data to build gene-content trees and compare them with species trees, to find HGT-driven incongruences.
- Add host annotation for the species that were too sparsely annotated for the host test, and test whether *Ralstonia solanacearum* gains Bonferroni support.
- Add automatic ID-format validation to subclade joins so that all-NaN merges fail loudly.
