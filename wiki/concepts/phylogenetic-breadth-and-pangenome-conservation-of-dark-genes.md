---
type: "Concept"
description: "How widely dark gene families are distributed across species and phyla, how coarse breadth classes fail to discriminate, and how full-pangenome orthologous-group counts and conservation tiers change prioritization."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Phylogenetic breadth and pangenome conservation of dark genes

In the functional dark matter analysis, over half of dark ortholog groups (OG) span multiple phyla and thousands of species. [src: functional_dark_matter] Coarse breadth classes hide this, and full-pangenome counts and conservation tiers change which families rank highest. [src: functional_dark_matter] The evidence comes mainly from one project (functional_dark_matter), echoed in the cross-project digest, with supporting context from two other reports. [src: discoveries]

## Literature Context

The candidate papers give only indirect context for how widely unannotated genes are distributed. A survey of 532 sequenced genomes (491 bacterial and 41 archaeal strains) extracted 180,879 mini-proteins of no more than 100 amino acids [PMID 19107199](https://pubmed.ncbi.nlm.nih.gov/19107199/). It reports two separate statistics. The majority are species-specific, averaging 58.79% among six representative phyla. Also, 70.03% across all strains are hypothetical proteins. The authors add that a fraction of highly conserved hypothetical proteins may play crucial roles. They do not say how many such proteins there are, and they do not link the hypothetical class to the species-specific class [PMID 19107199](https://pubmed.ncbi.nlm.nih.gov/19107199/). The study covers small proteins only.

A pan-genome study of 34 Lactobacillus paracasei strains found over 4200 ortholog groups in the pan-genome, of which about 1800 make up the conserved core. The variable genome (the variome) consists mainly of hypothetical proteins, phages, plasmids, transposon/conjugative elements and several known functions [PMID 23894338](https://pubmed.ncbi.nlm.nih.gov/23894338/). This is a single species, so it shows that unannotated content can sit in the variable fraction of one pan-genome. It does not show that the pattern holds across the literature. Two further papers show patchy or localized distributions. Bacterial annexin homologues occur in only seventeen bacterial species, with an anomalous phylogenetic distribution that the authors explain by massive gene loss or very divergent evolution. They state that current evidence does not settle the origin of these genes [PMID 24454864](https://pubmed.ncbi.nlm.nih.gov/24454864/). Acidobacterial metagenomic fosmid inserts (17 positive clones) from subdivision 6 shared a syntenic region containing conserved hypothetical proteins. The significance of that region is unknown [PMID 20729323](https://pubmed.ncbi.nlm.nih.gov/20729323/).

Against this background, the corpus findings are partly consistent with the literature and partly an extension of it. The truly_dark_genes comparison fits the picture of narrow distribution. Truly dark genes have a median ortholog breadth of 1 organism versus 4, and a core genome fraction of 43.1% versus 72.7%. This resembles the species-restricted and variable content in [PMID 19107199](https://pubmed.ncbi.nlm.nih.gov/19107199/) and [PMID 23894338](https://pubmed.ncbi.nlm.nih.gov/23894338/). That resemblance is qualitative, because those papers use different populations and methods.

The functional_dark_matter result is the main extension. Over half of dark ortholog groups span multiple phyla, and 55.9% fall in the kingdom tier. Species counts range from 1 to 27,482 across the full pangenome of 27,690 species. Top families such as COG0468, COG0443 and COG0491 are in kingdom-tier true knowledge gaps. These results go beyond the mini-protein survey, which only notes that some conserved hypothetical proteins may matter [PMID 19107199](https://pubmed.ncbi.nlm.nih.gov/19107199/). They quantify broadly conserved dark families at a scale the candidate papers do not reach. They also do not contradict the species-specific dark fraction. The two populations are different, and the candidate papers do not test the corpus's tier scheme, so its tier distribution and prioritization are novel relative to this evidence.

## Coarse breadth classes fail to discriminate

The eggNOG breadth classification used in NB05's s_pangenome score does not discriminate, because 99.9% of dark gene clusters map to universal root-level OGs and receive identical conservation scores. [src: functional_dark_matter] The count is 30,721 of 30,756 clusters, with root-level eggNOG OGs present across domains of life. [src: functional_dark_matter] The report adds that the sparse 48-organism Fitness Browser (FB) sampling (37/48 Proteobacteria) also fails to distinguish conservation patterns among dark genes. [src: functional_dark_matter] See [[entities/eggnog-orthologous-groups]].

An early refinement used a species count per root OG. Mapping 30,756 gene clusters to taxonomy showed that species count (1–33) gives finer resolution than the universal/clade-restricted split. [src: functional_dark_matter] Root OG species counts ranged from 1 to 33 (median=1, mean=2.2). [src: functional_dark_matter] The metric counts pangenome species sharing the same root OG. [src: functional_dark_matter]

A supplementary scoring replaced binary breadth with min(n_species / 20, 1.0) × 0.5. [src: functional_dark_matter] Its rankings correlate highly with the original (Spearman ρ = 0.982). [src: functional_dark_matter] The top lists still differ: top-50 overlap is 62% [src: functional_dark_matter] and top-100 overlap is 58%. [src: functional_dark_matter] So a continuous metric changes which candidates lead, even when overall rank correlation is high.

## Full-pangenome breadth

The report measured breadth across the full pangenome of 27,690 species, not only the 48 FB organisms. [src: functional_dark_matter] NB11b used the GTDB r214 pangenome. It exploded eggNOG_OGs annotations across 93.5M gene clusters and matched 11,774 dark gene root OGs. [src: functional_dark_matter] See [[entities/kbase-ke-pangenome]].

Species counts now range from 1 to 27,482 (median 135, mean 2,128), and phylum counts range from 1 to 142. [src: functional_dark_matter] This replaces the previous 1-to-33 range from the FB-only analysis. [src: functional_dark_matter] The cross-project digest reports the same range and median. [src: discoveries]

Coverage also grew. Of 57,011 dark genes, 39,532 (69.3%) had pangenome links via the conservation_vs_fitness project. [src: functional_dark_matter] OG_id propagation within 48-organism ortholog groups recovers 5,206 more dark genes (9.1%). [src: functional_dark_matter] Together with the full-pangenome query, coverage rose from 32,791 (57.5%) to 37,997 (66.6%) dark genes. [src: functional_dark_matter]

Earlier cluster-level breadth analysis found both clade-restricted families (single phylum) and widespread ones (3+ phyla). [src: functional_dark_matter] The report maps 30,756 clusters across 27,690 species. [src: functional_dark_matter]

## Conservation tiers

The 11,774 root OGs fall into 8 taxonomic tiers, based on the narrowest rank containing all member species. [src: functional_dark_matter] The shares are kingdom 55.9%, class 11.0%, family 10.5%, genus 6.9%, mobile 6.5%, phylum 4.8%, order 3.9% and species 0.5%. [src: functional_dark_matter] The digest also reports that 55.9% are kingdom-level, across multiple phyla. [src: discoveries] Mobile elements are detected through phylogenetic patchiness, meaning presence in distant phyla but few species per phylum. [src: functional_dark_matter] See [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]].

At gene level (57,011 dark genes, including 19,014 FB-only fallback assignments) the distribution differs. Kingdom is 51.4%, species 29.8%, genus 6.2%, class 4.0%, family 3.5%, mobile 1.9%, phylum 1.9% and order 1.3%. [src: functional_dark_matter] The OG-level and gene-level figures are different populations and should not be compared directly.

The report interprets this as a fundamental limit on understanding broadly conserved biology, not a minor annotation gap. [src: functional_dark_matter] It reads broad conservation as likely fundamental and clade-restricted genes as likely niche-specific. [src: functional_dark_matter] These readings are interpretations, not tested results.

The OGs also get hypothesis status tiers: strong testable hypothesis 6.0%, weak lead 52.5% and true knowledge gap 41.5%. [src: functional_dark_matter] Strong hypotheses rest on module predictions with EC (Enzyme Commission) numbers, high cross-organism concordance, high-confidence GapMind matches, or named domains with strong fitness. [src: functional_dark_matter] Weak leads rest on DUF-only domains, bare module predictions, medium/low GapMind, strong fitness without annotation, or named domains without fitness. [src: functional_dark_matter] True knowledge gaps have zero functional evidence of any kind. [src: functional_dark_matter]

## Effect on prioritization

The importance score is (tier-adjusted conservation + log₂-scaled species fraction) × an ignorance multiplier. [src: functional_dark_matter] Kingdom-level true knowledge gaps rank highest and species-specific strong hypotheses lowest. [src: functional_dark_matter] The report prioritizes widespread families because they are conserved yet unannotated. [src: functional_dark_matter]

Top-ranked OGs, from the Route B table:
- COG0468: 27,427 species, 142 phyla, kingdom tier, true knowledge gap, importance 23.9. [src: functional_dark_matter]
- COG0443: 27,279 species, 142 phyla, true knowledge gap, importance 23.9. [src: functional_dark_matter]
- COG0491: 27,393 species, 142 phyla, true knowledge gap, importance 23.9. [src: functional_dark_matter]
- COG0172: 27,431 species, weak lead. [src: functional_dark_matter]

The digest says COG0468, COG0443 and COG0491 are present in virtually all sequenced bacterial genomes yet have zero functional evidence. [src: discoveries] The report suggests Route A misses them because they may be essential under all conditions and so show no differential fitness signal. [src: functional_dark_matter] This is a suggestion, not a measured result.

Among the most widespread top-500 dark clusters (present in 15+ pangenome species), common domain families include TauE (sulfonate export, 7 clusters). [src: functional_dark_matter] DUF444 and Cu-oxidase_4 each occur in 5 clusters. [src: functional_dark_matter] EamA occurs in 4, including the #1 candidate. [src: functional_dark_matter] DUF484, DUF971 and DUF934 occur in 3+ clusters each. [src: functional_dark_matter]

## Related reports

In the alphafold_msa_annotation census, paradox proteins are core genes present in the majority of genomes in each of 14,768 species clades. [src: alphafold_msa_annotation] The report reads this as implying strong purifying selection and likely important function. [src: alphafold_msa_annotation] See [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes]].

In truly_dark_genes, truly dark genes are narrower than annotation-lag genes. They have orthologs in 29.3% of cases versus 63.7%. [src: truly_dark_genes] Median ortholog breadth is 1 organism versus 4 (d = −1.072, p < 1e-100). [src: truly_dark_genes] They are 4.2× less likely to have cross-organism orthologs (OR = 0.236, odds ratio). [src: truly_dark_genes] Their core genome fraction is 43.1% versus 72.7% (OR = 0.284, p < 1e-100). [src: truly_dark_genes] See [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]].

## Open Directions

- Map the bacterial paradox clusters onto the GTDB phylogeny to find phyla and families with the highest density of conserved-yet-novel proteins. This would add a phylogenetic view to the OG-level tiers above.
- Compute tier distributions separately for truly dark and annotation-lag genes. This would test whether the narrow breadth of truly dark genes persists under full-pangenome counts, not just FB ortholog breadth.
- Test whether top Route B knowledge gaps (COG0468, COG0443, COG0491) are essential, for example in essentiality data. This would check the suggestion that they lack differential fitness signal.
- Re-rank with the species-count metric at full-pangenome scale. This would show how much the top-50 and top-100 lists change when counts are not capped at 33.
