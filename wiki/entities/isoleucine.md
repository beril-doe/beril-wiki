---
type: "Compound"
description: "Isoleucine is an amino acid that appears in the corpus as a Pseudomonas aeruginosa PA14 growth substrate and as a biosynthetic pathway that showed no signal in NMDC community metabolic ecology."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
---
# Isoleucine

Isoleucine is an amino acid with two roles in this corpus. First, it is a substrate in a ranking of amino acids by how well *Pseudomonas aeruginosa* PA14 grows on them. Second, it is a biosynthetic pathway tested against metabolite availability in NMDC community data. In that analysis a compound-mapping correction for isoleucine also changed the [[entities/leucine]] result [src: cf_formulation_design, nmdc_community_metabolic_ecology].

## Growth substrate for *P. aeruginosa* PA14

The [[summaries/cf_formulation_design__REPORT]] project reports an amino acid preference hierarchy for [[entities/pseudomonas-aeruginosa]] PA14, ranked by optical density (OD): proline (OD 0.60), histidine (0.56), ornithine (0.46), glutamate (0.40), aspartate (0.36), isoleucine (0.36) and [[entities/arginine]] (0.35). This is a growth measurement from a single strain [src: cf_formulation_design].

## Community metabolic ecology (NMDC)

**Null result.** In [[summaries/nmdc_community_metabolic_ecology__REPORT]], isoleucine biosynthesis could be tested as the 13th pathway. It showed no BQH signal at this sample size (r = −0.057, n = 18, q = 0.823). In the same analysis, [[entities/tyrosine]] was an outlier that ran in the opposite, nonsignificant direction (r = +0.419, ns). The report suggests this may reflect alternative tyrosine sources, such as phenylalanine hydroxylation, that complicate the link between biosynthesis and availability [src: nmdc_community_metabolic_ecology].

**Effect on the leucine result.** A bug fix in isoleucine/leucine compound mapping strengthened the [[entities/leucine]] signal (r −0.326 → −0.390, q 0.045 → 0.022). Three isoleucine compounds had been wrongly assigned to leucine. Their completeness-vs-metabolite correlations were near zero, so the misassignment diluted the true leucine signal [src: nmdc_community_metabolic_ecology].

**Caveat on compound identification.** Metabolites were matched to pathways by string-matching compound names. Automated review found a substring collision, in which isoleucine compounds matched the "leucine" pattern. It was corrected with a first-match-wins rule, and the reported results come from the corrected run. Isoleucine is now included as a 13th testable pathway (r = −0.057, ns). KEGG compound IDs were sparse in the NMDC data (2% annotation rate), which limited KEGG-based matching. Cysteine, histidine and lysine remain untestable because no compounds for them were detected [src: nmdc_community_metabolic_ecology].
