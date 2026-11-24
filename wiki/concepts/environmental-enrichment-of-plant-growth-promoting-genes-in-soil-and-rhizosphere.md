---
type: "Concept"
description: "Whether PGP genes are over- or under-represented in soil/rhizosphere species versus other environments, including phylum-controlled and sensitivity analyses and label-quality caveats; stops at presence-based species-level enrichment."
sources: ["summaries/discoveries.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Environmental enrichment of plant-growth-promoting genes in soil and rhizosphere

Whether PGP genes are over- or under-represented in soil/rhizosphere species versus other environments, including phylum-controlled and sensitivity analyses and label-quality caveats; stops at presence-based species-level enrichment.

## Literature Context

The candidate papers are mostly genome-mining or rhizosphere studies of single strains or single fields. They give context for the corpus but do not test soil enrichment of PGP genes across species. Single-strain studies annotate auxin, siderophore, nitrogen fixation, pyrroloquinoline quinone and ACC deaminase genes in rhizosphere isolates: Rahnella perminowiae S11P1 and Variovorax sp. S12S4 from saffron [PMID 38500021](https://pubmed.ncbi.nlm.nih.gov/38500021/), and Pseudomonas aeruginosa NG61 from sunflower [PMID 35460384](https://pubmed.ncbi.nlm.nih.gov/35460384/). Chryseobacterium cucumeris PCH239 was also characterized, with its siderophore, phosphate and IAA activities validated experimentally [PMID 36884102](https://pubmed.ncbi.nlm.nih.gov/36884102/). Bacillus genomes from maize rhizosphere carry auxin, nitrogen fixation and siderophore elements [PMID 34529229](https://pubmed.ncbi.nlm.nih.gov/34529229/). These are descriptive, each covers one or a few genomes, and none has a non-rhizosphere comparison group. They show that PGP genes occur in rhizosphere isolates. They do not show that the genes are enriched there.

A few papers do compare environments. A maize metagenome study found nutrient-mobilization genes, including nifA, fixJ, norB and pstA, significantly more abundant (α = 0.05) in former-grassland rhizosphere soils than in a second field. This shows that land-use history shapes PGP gene composition [PMID 34573413](https://pubmed.ncbi.nlm.nih.gov/34573413/). Two further studies relate to rhizosphere-versus-bulk enrichment. A rhizosphere Pseudomonas study found root-upregulated genes more abundant in rhizosphere communities than in bulk soil and more prevalent in plant-associated Pseudomonas genomes [PMID 41345977](https://pubmed.ncbi.nlm.nih.gov/41345977/). A wheat drought study reported enrichment of drought-response genes and particular Streptomyces and Leifsonia taxa in the rhizosphere [PMID 40446806](https://pubmed.ncbi.nlm.nih.gov/40446806/). Reviews summarize PGPR genomics and genome mining [PMID 38028595](https://pubmed.ncbi.nlm.nih.gov/38028595/), [PMID 39738995](https://pubmed.ncbi.nlm.nih.gov/39738995/).

The corpus's findings are consistent with this literature in direction. The finding that acdS, pqqC and hcnC are enriched in soil/rhizosphere species fits the view that rhizosphere lineages carry PGP traits, and the plant-association markers match it as well. They extend it, because the comparison uses 1,039 soil/rhizosphere species against 10,233 other species, with phylum-controlled and rhizosphere-only sensitivity analyses (acdS OR 6.98 and 10.6). None of the candidates offers a comparison like that. The within-genus shuffle result is also new here. Only 3 of 15 plant-association markers survived it, and the other candidates do not control for phylogeny at all.

The nifH depletion in soil (OR 0.60) is not directly supported by the candidates. The maize study found nifA enriched in one rhizosphere field relative to another, but that is a different gene and a different contrast [PMID 34573413](https://pubmed.ncbi.nlm.nih.gov/34573413/). It is therefore best read as untested rather than contradicted. The ipdC result changed from non-significant in the raw test (OR 0.79) to depletion under phylum control (OR 0.56). No candidate addresses this, so it is novel and rests on one project. The explanations offered for nifH depletion remain interpretations, not tests.

Overall, the candidates give no soil-versus-other-environment tests of these genes. The corpus's species-level enrichment estimates are therefore not confirmed or challenged by this evidence.

## Soil enrichment of focal PGP genes

Three of five focal genes were enriched in soil/rhizosphere species. The comparison used 1,039 soil/rhizosphere species and 10,233 species from other environments, with Benjamini-Hochberg false discovery rate (BH-FDR) q < 0.05. [src: pgp_pangenome_ecology] A separate summary reports acdS and pqqC as strongly enriched across 27K GTDB species. [src: discoveries]

| Gene | Soil/rhizosphere | Other | OR | q |
|---|---|---|---|---|
| acdS | 15.8% | 2.6% | 7.02 | 5.1e-62 [src: pgp_pangenome_ecology] |
| pqqC | 43.8% | 21.2% | 2.90 | 2.8e-53 [src: pgp_pangenome_ecology] |
| hcnC | 11.3% | 6.4% | 1.85 | 6.1e-08 [src: pgp_pangenome_ecology] |
| nifH | 12.9% | 19.7% | 0.60 (depleted) | 5.5e-08 [src: pgp_pangenome_ecology] |
| ipdC | 1.5% | 1.9% | 0.79 | 0.47 (ns) [src: pgp_pangenome_ecology] |

The pqqC–acdS module is described as strongly rhizosphere-enriched, with acdS OR = 7.0. [src: pgp_pangenome_ecology] The hcnC result is read as suggesting that the hcnA–hcnC operon is part of the rhizosphere niche toolkit. [src: pgp_pangenome_ecology] See also [[entities/acc-deaminase-acds]], [[entities/hcnc]] and [[entities/pyrroloquinoline-quinone-biosynthesis]].

## Robustness of acdS enrichment

Two further analyses of acdS were run, each addressing one concern. With phylum-level fixed effects in logistic regression, the OR was 6.98 (p = 4.8e-61). [src: pgp_pangenome_ecology] Separately, a strict rhizosphere-only sensitivity analysis used genomes whose isolation source contained "rhizosphere" or "root nodule". It gave OR = 10.6 (q = 7.6e-38). [src: pgp_pangenome_ecology] It also cites the model of Glick (1998) and Ravanbakhsh et al. (2017), in which ACC deaminase is advantageous in ethylene-rich root environments. [src: pgp_pangenome_ecology]

A different project tested plant association rather than soil. A genus-cluster-robust generalized linear model (GLM) gave ACC deaminase an OR of 8.01, 95% CI [4.19, 15.32], q 2.1×10⁻⁹. [src: plant_microbiome_ecotypes] Within-genus label shuffling, the strictest species-level null, retained 3 of 15 plant-association markers: nitrogen fixation, ACC deaminase and T3SS (type III secretion system). [src: plant_microbiome_ecotypes] The report describes this permutation as complementing a genus-level cluster-robust GLM in which 8 of 14 markers were significant. [src: plant_microbiome_ecotypes] This result concerns plant association, not soil/rhizosphere enrichment, so it does not show that the soil signal is species-level. The labels differ, so the ORs are not directly comparable.

## nifH depletion and its exception

nifH forms a separate guild and is depleted in soil relative to aquatic environments. [src: discoveries] Diazotrophs are depleted in soil-classified genomes relative to aquatic and host-associated environments. [src: pgp_pangenome_ecology] The report offers two explanations. The database's nitrogen fixers are mostly aquatic/marine (cyanobacteria, Azotobacter) or host-associated (rhizobia). [src: pgp_pangenome_ecology] Nitrogen fixation is also energetically expensive and matters most in oligotrophic aquatic settings and specific symbioses. [src: pgp_pangenome_ecology] It cites Wardell et al. (2022), who describe nif mobility on symbiosis islands as relevant mainly in legume-associated Rhizobiales. [src: pgp_pangenome_ecology] These are interpretations, not tests.

The phylum-stratified analysis found an exception. Bacillota_A was nifH-enriched in soil (OR = ∞, q = 2.5e-4), attributed to soil-specific anaerobic diazotrophs such as clostridia. [src: pgp_pangenome_ecology] See bacterial nitrogen fixation nif genes.

The plant-association model points the other way for nitrogen fixation. It gave nitrogen fixation an OR of 2.71, 95% CI [1.54, 4.78], q 1.3×10⁻³. [src: plant_microbiome_ecotypes] This is a different contrast (plant-associated versus not), so it does not directly contradict soil depletion. See Tensions.

## ipdC: null on raw test, depleted with phylum control

ipdC showed no raw soil enrichment (OR = 0.79, ns). [src: pgp_pangenome_ecology] The phylum-controlled logistic model instead found soil depletion (OR = 0.56, p = 0.027). [src: pgp_pangenome_ecology]

## Plant-association markers under phylogenetic control

In the plant-association GLM, 8 of 14 markers had q < 0.05 with 95% Wald CIs excluding zero. [src: plant_microbiome_ecotypes] With |coef| > 0.2, 8/14 survived, and 13 of 14 agreed with the L1 verdict. [src: plant_microbiome_ecotypes] The significant markers and ORs were:

- ACC deaminase 8.01 [src: plant_microbiome_ecotypes]
- T3SS 2.71, 95% CI [1.94, 3.80], q 2.6×10⁻⁸ [src: plant_microbiome_ecotypes]
- nitrogen fixation 2.71 [src: plant_microbiome_ecotypes]
- phenazine 2.12, 95% CI [1.69, 2.64], q 5.9×10⁻¹⁰ [src: plant_microbiome_ecotypes]
- CWDE cellulase 1.87 (CWDE = cell wall degrading enzyme), 95% CI [1.46, 2.40], q 2.5×10⁻⁶ [src: plant_microbiome_ecotypes]
- phosphate solubilization 1.68, 95% CI [1.20, 2.35], q 4.8×10⁻³ [src: plant_microbiome_ecotypes]
- CWDE pectinase 1.59, 95% CI [1.25, 2.01], q 3.4×10⁻⁴ [src: plant_microbiome_ecotypes]
- effector 1.35, 95% CI [1.09, 1.67], q 1.2×10⁻² [src: plant_microbiome_ecotypes]

The combined verdict classified 3 markers as species-level robust [src: plant_microbiome_ecotypes], 5 as cassette-level (genus-acquired but not species-distinguishing) [src: plant_microbiome_ecotypes], and 6 as not robust under any test. [src: plant_microbiome_ecotypes] The five cassette-level markers are phenazine, CWDE cellulase, CWDE pectinase, phosphate solubilization and effector. [src: plant_microbiome_ecotypes] The six non-robust markers are DAPG biocontrol, T4SS, hydrogen cyanide, IAA biosynthesis, siderophore and acetoin/butanediol. [src: plant_microbiome_ecotypes]

Several of these were non-significant in the GLM:

- dapg_biocontrol, OR 0.98, q 0.96 [src: plant_microbiome_ecotypes]
- t4ss, OR 0.98, q 0.96 [src: plant_microbiome_ecotypes]
- hydrogen_cyanide, OR 0.96, q 0.96 [src: plant_microbiome_ecotypes]
- siderophore, OR 0.72, q 0.26 [src: plant_microbiome_ecotypes]
- acetoin_butanediol, OR 0.69, q 0.11 [src: plant_microbiome_ecotypes]

IAA biosynthesis was the sole discordant marker. L1 gave coef 0.61 (significant), but the cluster-robust model gave coef −0.09, p = 0.82, so it was labeled an L1 false positive. [src: plant_microbiome_ecotypes] Twelve markers failed the within-genus shuffle, so their signals are consistent with reshuffling labels within genus. [src: plant_microbiome_ecotypes] The three-tier framing is the report's own. [src: plant_microbiome_ecotypes] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

## Label-quality caveats

The soil/rhizosphere category is conservative. Only 1,637 species (5.9% of species with an environment label) are classified as soil/rhizosphere dominant, reflecting NCBI's clinical and host-associated sampling bias. [src: pgp_pangenome_ecology] The isolation-source labels are noisy. [src: pgp_pangenome_ecology] The report therefore considers the acdS and pqqC ORs (7.0 and 2.9) likely underestimates, because many soil isolates carry broader "environmental" labels. [src: pgp_pangenome_ecology] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]] and [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].

## Tensions

- nifH is depleted in soil (OR 0.60) [src: pgp_pangenome_ecology], but nitrogen fixation is enriched in plant-associated genomes (OR 2.71). [src: plant_microbiome_ecotypes]
- ipdC is non-significant in the raw test [src: pgp_pangenome_ecology] but depleted under phylum control. [src: pgp_pangenome_ecology] The conclusion depends on the phylogenetic adjustment.

## Open Directions

- Re-run the soil comparison with a within-genus shuffle null, as was done for plant association, to see which soil-enriched genes (acdS, pqqC, hcnC) are species-level rather than genus-level signals. This closes the gap that only the plant-association study had that test.
- Refine soil labels using environmental ontology or metagenome-source metadata, to test whether the predicted underestimate of acdS and pqqC ORs holds.
- Stratify nifH by phylum and lifestyle (free-living versus symbiotic) to test the proposed explanations for soil depletion.
- Check ipdC depletion with alternative phylogenetic controls to see whether the phylum-level result is stable.
