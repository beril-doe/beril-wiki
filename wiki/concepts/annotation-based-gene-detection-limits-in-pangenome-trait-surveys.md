---
type: "Concept"
description: "How name-based annotation matching, lack of functional validation, rare-gene power and database version drift limit pangenome-scale presence/absence surveys of functional genes."
sources: ["summaries/discoveries.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/pitfalls.md"]
---
# Annotation-based gene detection limits in pangenome trait surveys

Annotation labels can change a pangenome presence/absence result completely, as the lanmodulin and Psl cases show. [src: discoveries, pitfalls] Several limits are stated by the reports as caveats rather than measured. See also [[concepts/annotation-source-disagreement-and-coverage]] and [[concepts/limits-of-keyword-and-marker-based-functional-annotation]].

## Literature Context

The candidate papers bear on this page only indirectly. None of them tests name-based annotation matching in pangenome trait surveys, and none addresses lanmodulin, xoxF, Psl, PGP genes or PHB genes. They do speak to three themes the hub raises: how well annotation-derived features represent function, how far gene content can be inferred when annotation is incomplete, and how homology-based annotation leaves gaps.

One paper compared encodings of the same genomes. It built machine learning models on 1,088 Acinetobacter baumannii isolates across 10 antimicrobial agents and validated them in an independent cohort of 508 isolates. KEGG orthology (KO) representations consistently outperformed traditional gene presence-absence encoding across all algorithms, and XGBoost reached 94.44% weighted accuracy [PMID 42095666](https://pubmed.ncbi.nlm.nih.gov/42095666/). The authors argue that presence-absence matrices inadequately capture functional capacity. This is a prediction-performance result in one pathogen, and the authors state that prospective validation is still needed. It is consistent with the hub's Psl example, where KO-based detection (K20997–K21005) gave about 95% prevalence versus under 1% by gene name alone. It also fits the lanthanide atlas's use of calibrated, KO-aware sources. It does not test annotation-source disagreement directly.

A second paper shows that gene content can be partly inferred without annotation. Classifiers using k-mers from 100 conserved genes predicted presence or absence of E. coli protein families found in 10%-90% of genomes, with a per-genome average macro F1 of 0.944 [PMID 37314210](https://pubmed.ncbi.nlm.nih.gov/37314210/). Poorly annotated proteins, including hypothetical proteins, were predicted with F1 = 0.902. A holdout set of 419 freshwater E. coli genomes gave F1 = 0.880 [PMID 37314210](https://pubmed.ncbi.nlm.nih.gov/37314210/). The work covers a single species and variable genes of intermediate frequency, so it does not address the rare genes the hub discusses, such as ipdC in 214 of 11,272 species. It does suggest that label-independent presence prediction is feasible. That could help with the hub's open question of whether eggNOG under-calls phaR (K18080), but this has not been tested.

A third paper concerns homology limits. Homology-based annotation is limited where well-characterized sequences are absent, and context-based methods can find missing enzymes. In Mycobacterium tuberculosis, homology-based ModEnzA gave 56 novel enzyme predictions and the hole-finding protocol predicted 74 putative local holes [PMID 33076816](https://pubmed.ncbi.nlm.nih.gov/33076816/). This is consistent with the atlas's caveat that novel rare-earth-element enzymes lacking KEGG/RefSeq homologs would go undetected.

Overall, the corpus's central findings are not directly covered by these papers. These include the 418 versus 5,092 xoxF gap, the complete eggNOG and bakta disagreement for lanmodulin, the lack of pseudogene screening, the quasi-complete separation in the ipdC model and the nifH count drift (1,913 estimated versus 2,756 actual). They are therefore novel relative to this evidence. The qualitative point that annotation choice changes functional inference is consistent with the literature. The corpus's quantitative source-disagreement results extend it.

## Name-based matching and source disagreement

Different annotation sources can give very different answers for the same gene. For [[entities/lanmodulin]], a calibration on 134K KBase Data Lakehouse pangenome genomes found that the two annotation sources disagree completely. [src: discoveries] The report advises using bakta product='Lanmodulin' exclusively and treating eggNOG Preferred_name='lanM' as zero-information. [src: discoveries]

For [[entities/xoxf-lanthanide-dependent-methanol-dehydrogenase]], 5,092 genomes carried any xoxF marker, but only 418 (8%) hit both eggNOG K00114 and bakta Lanthanide-dependent methanol dehydrogenase-family products. [src: discoveries] The eggNOG-only set of 3,272 genomes appears to include bakta "Putative dehydrogenase XoxF" entries that the regex missed, plus other generic dehydrogenases hitting K00114. [src: discoveries] The report therefore advises reporting eggNOG-K00114 as the primary set and either-source as the inclusive set, disclosing the gap, and naming the source for any xoxF count. [src: discoveries]

The lanthanide atlas reports the same problem for xoxJ, lanmodulin and PQQ (pyrroloquinoline quinone) biosynthesis. Its headline statistics use a calibrated source of truth per marker, and union-of-sources analyses are reported alongside. [src: lanthanide_methylotrophy_atlas]

The PGP survey took the opposite approach, matching exact bakta gene names such as nifH, acdS and pqqC. [src: pgp_pangenome_ecology] This misses genes annotated only by product description or with variant names, especially less-characterized PGP genes. [src: pgp_pangenome_ecology]

Psl shows the size of the effect. In GenomeDepot-based databases (protect_genomedepot, phagefoundry_paeruginosa_genome_browser), pslA-pslO are rarely annotated with canonical names, except in the PAO1 reference genome. [src: pitfalls] The pangenome bakta_annotations cover Psl better, but pslA, pslG and pslK stay sparse. [src: pitfalls] Using KEGG orthologs (KO) K20997–K21005 from eggnog_mapper_annotations gives about 95% prevalence versus under 1% by gene name alone. [src: pitfalls] See [[entities/protect-genome-depot]].

A related case is the polyhydroxybutyrate (PHB) survey. phaR (K18080) had 0 detected clusters and 0 species. [src: phb_granule_ecology] With 5 of 6 PHB KOs detected, the report suggests K18080 may be underrepresented in eggNOG annotations. [src: phb_granule_ecology] This is a suggestion, not a tested result.

## No functional validation

The lanthanide atlas assesses xoxF and PQQ at the gene-call level and does not screen for pseudogenes, truncated ORFs or assembly fragmentation. [src: lanthanide_methylotrophy_atlas] The PGP report likewise states that a cluster annotated as pqqC is not necessarily functional, and that truncations, frameshifts and pseudogenization are not filtered. [src: pgp_pangenome_ecology] The atlas is also bounded by eggNOG and bakta calls, so genuinely novel rare-earth-element enzymes lacking KEGG/RefSeq homologs would go undetected. [src: lanthanide_methylotrophy_atlas] See [[concepts/pathway-completeness-inference-from-ko-annotations-and-pleiotropic-enzymes]].

## Rare genes and statistical power

Rarity limits what models can test. Only 214 of 11,272 species (1.9%) carry ipdC, which limits power for the PGP H4 stratified analysis. [src: pgp_pangenome_ecology] A phylum-plus-soil logistic model (Model 3) failed from quasi-complete separation caused by ipdC's rarity across phyla (214 species, 1.9%). Conclusions therefore rest on Model 1 (trp only) and Model 2 (trp + is_soil). [src: pgp_pangenome_ecology] See [[concepts/aromatic-amino-acid-biosynthesis-and-auxin-pathway-gene-coupling]].

Labels add noise as well. The PGP analysis uses noisy ncbi_isolation_source labels, and NCBI is heavily biased toward clinical and host-associated isolates. [src: pgp_pangenome_ecology] The report considers the acdS and pqqC rhizosphere enrichment odds ratios (ORs) of 7.0 and 2.9 likely underestimates, because many soil isolates carry broader "environmental" labels. [src: pgp_pangenome_ecology] See [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere]] and [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## Database version drift

The PGP research plan estimated about 1,913 nifH clusters, but the actual count was 2,756 (43% higher). The report attributes this to incremental growth of the GTDB r214 pangenome since the plan was written. It states that the discrepancy does not affect any analysis. [src: pgp_pangenome_ecology] See bacterial nitrogen fixation nif genes.

## Open Directions

- Score xoxF with a curated hit list that includes "Putative dehydrogenase XoxF" products. Then check how many of the 3,272 eggNOG-only genomes are real xoxF, which would settle the 418 versus 5,092 gap.
- Rerun the PGP gene survey with product-text and KO-based detection alongside exact gene names. This would measure how many genes the name-only approach missed.
- Screen annotated pqqC and xoxF clusters for truncation and frameshifts. This would give a functional-validity rate for gene-call presence.
- Test whether eggNOG under-calls phaR (K18080) by searching phaR with a profile-based method in PHB-bearing genomes.
- Repeat ipdC models with penalized (Firth-type) logistic regression to recover a phylum-adjusted estimate despite separation.
