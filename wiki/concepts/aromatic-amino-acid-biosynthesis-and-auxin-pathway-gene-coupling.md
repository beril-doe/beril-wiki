---
type: "Concept"
description: "Whether completeness of tryptophan (and tyrosine) biosynthesis predicts carriage of the auxin-synthesis gene ipdC, including soil-versus-non-soil stratification and confounding by general metabolic capacity."
sources: ["summaries/discoveries.md", "summaries/pgp_pangenome_ecology__REPORT.md"]
---
# Aromatic amino acid biosynthesis and auxin pathway gene coupling

Complete tryptophan biosynthesis predicted carriage of the auxin-synthesis gene ipdC across 11,272 species, but tyrosine, the negative control, predicted it at a similar effect size. [src: pgp_pangenome_ecology] The report suggests general metabolic capacity as a possible confound, but it did not test this. [src: pgp_pangenome_ecology] The association was positive in non-soil species and reversed in soil species. [src: discoveries] The soil reversal rests on few ipdC-positive species and is hypothesis-generating. [src: pgp_pangenome_ecology] Evidence comes from one pangenome survey ([[summaries/pgp_pangenome_ecology__REPORT]]) and its digest ([[summaries/discoveries]]).

## Literature Context

The candidate papers establish that ipdC encodes indole-3-pyruvate decarboxylase, the key step of the tryptophan-dependent indole-3-pyruvate (IPyA) route to indole-3-acetic acid (IAA). In Azospirillum, ipdC is crucial to overall IAA biosynthesis, although a tryptophan-independent pathway also exists [PMID 10978548](https://pubmed.ncbi.nlm.nih.gov/10978548/). In *Bacillus thuringiensis* RZ2MS9, knocking out ipdC with CRISPR-Cas9 cut IAA synthesis in the presence of tryptophan by 57% and reduced maize growth promotion. This is a single-strain result [PMID 36242861](https://pubmed.ncbi.nlm.nih.gov/36242861/). Tryptophan-dependent IAA synthesis is also not confined to ipdC. A genomic analysis of about 7282 prokaryotic genomes found that 82.2% were potentially capable of synthesizing IAA from tryptophan or intermediates. Many genomes carried several pathways at once, and rhizobacteria mainly used the indole-3-acetamide and tryptamine routes [PMID 30974826](https://pubmed.ncbi.nlm.nih.gov/30974826/). *Variovorax* makes IAA from indole-3-acetonitrile rather than tryptophan [PMID 29884755](https://pubmed.ncbi.nlm.nih.gov/29884755/). These pathway-level findings mean that ipdC carriage is only one route to IAA.

The regulatory literature links ipdC to aromatic amino acids. In *Enterobacter cloacae* UW5, TyrR directly induces ipdC. Expression rises in response to tryptophan, phenylalanine and tyrosine [PMID 18757531](https://pubmed.ncbi.nlm.nih.gov/18757531/). Later work showed that TyrR binds the akr-ipdC intergenic region. ipdC induction was strongest with phenylalanine and weaker with tryptophan and tyrosine [PMID 25811953](https://pubmed.ncbi.nlm.nih.gov/25811953/). That work was done in *E. cloacae* UW5 only. Rhizosphere tryptophan supply also matters. In a cucumber system, *Bacillus amyloliquefaciens* SQR9 colonization increased root tryptophan secretion three- to fourfold, and that tryptophan was sufficient to raise bacterial IAA production [PMID 26808445](https://pubmed.ncbi.nlm.nih.gov/26808445/). In *Azospirillum brasilense*, an ipdC mutant had a reduced growth rate and altered physiology, and the authors suggest IAA protects against indole-derivative stress [PMID 40130845](https://pubmed.ncbi.nlm.nih.gov/40130845/).

The corpus's overall trp–ipdC association (OR = 2.81) is consistent with the tryptophan-dependence of the IPyA pathway [PMID 36242861](https://pubmed.ncbi.nlm.nih.gov/36242861/). Its tyrosine result (OR = 3.62), which failed as a negative control, is also consistent with TyrR regulation by all three aromatic amino acids [PMID 18757531](https://pubmed.ncbi.nlm.nih.gov/18757531/). It does not extend the TyrR finding itself. TyrR was not measured and regulation was not tested across species. TyrR is documented directly only in *E. cloacae* UW5 [PMID 25811953](https://pubmed.ncbi.nlm.nih.gov/25811953/). The survey result is a species-level association that fits that mechanism. The hub also names general metabolic capacity as an untested confound, so the TyrR reading stays a hypothesis.

The soil reversal (OR = 0.30, p = 0.02, few ipdC-positive species) is hypothesis-generating. The root-exudate explanation is plausible given that colonizing bacteria can raise root tryptophan secretion [PMID 26808445](https://pubmed.ncbi.nlm.nih.gov/26808445/). That evidence comes from one cucumber–Bacillus system and does not test the survey pattern. The candidate papers contain no survey-scale soil-stratified test of this coupling, so the reversal is novel relative to them. The 214 ipdC-positive species also reflect annotation-based detection, and ipdC-independent routes [PMID 30974826](https://pubmed.ncbi.nlm.nih.gov/30974826/) could blur the signal.

## Overall association

Complete tryptophan biosynthesis (GapMind score ≥ 0.9) predicted ipdC presence. [[entities/gapmind]] supplies the pathway scores. Species with a complete trp pathway carried ipdC at 2.5%, against 0.9% in trp-incomplete species (Fisher OR = 2.81, p = 6.3e-10). [src: pgp_pangenome_ecology] The tryptophan-only logistic model (Model 1) gave OR = 2.81, 95% CI 1.97–4.01, p = 1.4e-08, n = 11,272. [src: pgp_pangenome_ecology] Adding a soil covariate (Model 2) kept the association (OR_trp = 2.87, p = 7.0e-09). [src: pgp_pangenome_ecology]

A phylum-plus-soil model (Model 3) failed. ipdC is rare (214 species, 1.9%), which caused quasi-complete separation. Conclusions therefore rest on Models 1 and 2. [src: pgp_pangenome_ecology]

## Tyrosine control and a regulatory explanation

The tyrosine pathway was meant as a negative control. It also predicted ipdC, at similar effect size (OR = 3.62, p = 2.3e-11). [src: pgp_pangenome_ecology] The report counts this as a failed negative control (OR = 3.62, against trp OR = 2.81). [src: pgp_pangenome_ecology] See [[entities/tyrosine-biosynthesis]].

The report reads this failure as mechanistically interpretable, not just a statistical nuisance. In *Enterobacter cloacae* and related species, ipdC is regulated by TyrR, a transcription factor activated by tryptophan, phenylalanine and tyrosine (Ryu & Patten 2008, PMID 18757531). [src: pgp_pangenome_ecology] It adds that species lacking the pathways are unlikely to make IAA even if ipdC is present. [src: pgp_pangenome_ecology] This is a proposed explanation, not a direct test.

## Soil versus non-soil stratification

Stratifying by habitat gave opposite signs. [src: discoveries] In non-soil species (n = 10,233) the positive association persisted (OR = 3.56, p = 7.7e-13). [src: pgp_pangenome_ecology] Within soil/rhizosphere species (n = 1,039) it reversed (OR = 0.30, p = 0.02), so trp-complete soil species were less likely to carry ipdC. [src: pgp_pangenome_ecology] The report summarises this as positive coupling only in non-soil species (OR = 3.56) and reversal in soil species (OR = 0.30). [src: pgp_pangenome_ecology]

The report concludes that autonomous trp biosynthesis capacity does not predict ipdC prevalence within soil species. [src: pgp_pangenome_ecology] It hypothesises that soil plant-growth-promoting bacteria obtain tryptophan from root exudates. That would relax selection for autonomous synthesis while ipdC is kept to make IAA from plant-supplied substrate. [src: pgp_pangenome_ecology] Related reasoning appears in [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]].

## Caveats and confounding

- Only 214 of 11,272 species (1.9%) carry ipdC, which limits power for the stratified analysis. [src: pgp_pangenome_ecology]
- The soil reversal (OR = 0.30, p = 0.02) should be treated as hypothesis-generating, not conclusive. [src: pgp_pangenome_ecology]
- GapMind trp and tyr completeness scores are both proxies for overall metabolic pathway completeness. Isolating a specific biochemical coupling needs control for genome size or total pathway count. [src: pgp_pangenome_ecology]
- The report proposes regressing ipdC presence on trp completeness while controlling for genome-wide pathway completeness (number of complete pathways or genome size). [src: pgp_pangenome_ecology]
- A better test would control for overall genome completeness (size, COG coverage; COG = clusters of orthologous groups) to separate the aromatic-pathway effect from general metabolic capacity. [src: pgp_pangenome_ecology]

See also [[concepts/annotation-based-gene-detection-limits-in-pangenome-trait-surveys]].

## Tensions

- The positive overall trp–ipdC association (OR = 2.81) [src: pgp_pangenome_ecology] sits against the reversal in soil species (OR = 0.30) [src: pgp_pangenome_ecology], while non-soil species showed a positive association (OR = 3.56). [src: pgp_pangenome_ecology]
- Tryptophan was expected to be specific, but tyrosine gave a similar effect (OR = 3.62). [src: pgp_pangenome_ecology] The report offers TyrR regulation [src: pgp_pangenome_ecology] and a general-metabolic-capacity confound [src: pgp_pangenome_ecology] as readings. It does not separate them.

## Open Directions

- Regress ipdC presence on trp completeness with genome size or total complete-pathway count as covariates, to test whether the aromatic-specific signal survives general metabolic capacity.
- Add phenylalanine biosynthesis and combined aromatic pathways as predictors, to see whether TyrR-linked coupling is shared across all three amino acids.
- Repeat the soil stratification with a finer habitat definition and exact or penalised logistic regression, to address ipdC rarity and the quasi-complete separation that sank Model 3.
- Check whether trp-incomplete soil species that carry ipdC also carry tryptophan uptake genes or TyrR, to test the root-exudate hypothesis directly.
