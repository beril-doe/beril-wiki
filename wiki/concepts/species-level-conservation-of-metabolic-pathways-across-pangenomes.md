---
type: "Concept"
description: "Whether GapMind pathway predictions on isolates generalize across genomes of a species, with clade-definition caveats; stops at pathogen genomes."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Species-level conservation of metabolic pathways across pangenomes

This page asks whether GapMind pathway predictions made on isolates carry over to other genomes of the same species. In the cf_formulation_design report they largely do for four of five core commensal species, and that report calls the conservation hypothesis (H5) strongly supported. [src: cf_formulation_design] The evidence is pangenome-based and predicted, not measured in each genome. Two other reports add limits: accessory genes contribute to pathway completeness [src: pathway_capability_dependency], and clade definitions change the numbers. [src: cf_formulation_design] The page stops at the pathogen genomes.

## Literature Context

Two candidate papers bear on whether metabolic and genomic traits generalize across genomes of a species. Neither tests GapMind predictions, and neither covers the commensal species in the hub. The other two candidates, on EF-P modification in Bacillus subtilis [PMID 29615499](https://pubmed.ncbi.nlm.nih.gov/29615499/) and a diatom endosymbiont bicarbonate transporter [PMID 40905388](https://pubmed.ncbi.nlm.nih.gov/40905388/), do not address pangenome conservation and are not used here.

The comparative analysis of four sequenced Paenibacillus polymyxa genomes reported a significantly conserved core genome. Complex metabolic pathways and regulatory networks were highly conserved, and genes for plant-host interaction and ecological fitness were well conserved despite variation in the accessory genome [PMID 25280501](https://pubmed.ncbi.nlm.nih.gov/25280501/). That study had only four genomes and was a genomic comparison with no growth or fitness measurements. The mutans streptococci study sequenced 6 clinical S. mutans isolates plus one S. sobrinus and one S. ratti isolate. It found significant differences in 42 pathways in genome-scale metabolic networks, and it inferred an "open" pan-genome from 67 S. mutans genomes. It also found that oxidative stress resistance genes were well conserved while pathogenicity-related genes varied strongly [PMID 23805886](https://pubmed.ncbi.nlm.nih.gov/23805886/). Pathway differences in that paper were mostly described across species within the group, not within one species.

The hub's finding that the PROTECT isolate carbon-utilization profiles largely generalize in four of five core commensal species is consistent with the Paenibacillus result of a conserved metabolic core, but it rests on far more genomes. Examples are 295 for Micrococcus luteus and 153 for Streptococcus salivarius. The hub's caveat that Gemella sanguinis (7 genomes) showed only 7/18 amino acid pathways conserved fits the mutans picture, in which an open pangenome and pathway differences mean strain choice can matter. That is a loose parallel, not a direct test, because the mutans paper did not measure conservation as the hub does.

The hub's reports of about 14% of species-level completeness coming from accessory genes in the top 5 accessory-dependent pathways, and of clade-definition effects for Neisseria mucosa, have no counterpart in these papers. Both papers report accessory or strain-specific variation, but neither quantifies how much of any pathway's completeness depends on it. The accessory-gene and clade-definition results are therefore novel relative to this evidence. The literature offers no tension with the hub's claim, and it supplies no direct support for GapMind-based generalization to other strains.

## Conservation in five core commensal species

The report examined [[entities/gapmind]] pathway conservation across 499 pangenome genomes in its 5 core commensal species. It asked whether PROTECT isolate carbon-utilization profiles generalize between strains. [src: cf_formulation_design] Micrococcus luteus, Streptococcus salivarius and Neisseria mucosa had 100% of amino acid (AA) pathways conserved. [src: cf_formulation_design] Rothia dentocariosa had 14/18 (78%). [src: cf_formulation_design] Gemella sanguinis, with the smallest pangenome, had the lowest at 7/18 (39%). [src: cf_formulation_design] Counts are pathways conserved at >95%.

| Species | Genomes | AA pathways | Carbon pathways |
|---|---|---|---|
| Micrococcus luteus | 295 | 18/18 (100%) [src: cf_formulation_design] | 39/39 (100%) [src: cf_formulation_design] |
| [[entities/streptococcus-salivarius]] | 153 | 18/18 (100%) [src: cf_formulation_design] | 32/35 (91%) [src: cf_formulation_design] |
| [[entities/rothia-dentocariosa]] | 29 | 14/18 (78%) [src: cf_formulation_design] | 39/41 (95%) [src: cf_formulation_design] |
| [[entities/neisseria-mucosa]] | 15 | 16/16 (100%) [src: cf_formulation_design] | 27/27 (100%) [src: cf_formulation_design] |
| Gemella sanguinis | 7 | 7/18 (39%) [src: cf_formulation_design] | 37/39 (95%) [src: cf_formulation_design] |

The report concludes that the measured capabilities are species-level traits conserved across hundreds of genomes. [src: cf_formulation_design] It says any well-characterized strain of M. luteus, S. salivarius, R. dentocariosa or N. mucosa should give equivalent metabolic competition. [src: cf_formulation_design] It contrasts this >95% conservation with the strain-level divergence described for Bifidobacterium. [src: cf_formulation_design] It presents the result as support for species-level formulation design. [src: cf_formulation_design]

The claim is weaker for the smaller pangenomes. G. sanguinis showed the most pathway variability in a small pangenome of 7 genomes, so strain choice matters most there. [src: cf_formulation_design] The summary profile table also lists AA conservation as 16/18 for N. mucosa and 14/18 for R. dentocariosa. [src: cf_formulation_design] It lists 7/18 for G. sanguinis and 18/18 for S. salivarius and M. luteus. [src: cf_formulation_design] The N. mucosa figure is 16/18 there but 16/16 in the conservation table. [src: cf_formulation_design] The report gives both numbers without reconciling them.

## Clade definition for Neisseria mucosa

A sensitivity check on the 8-genome clade gave 18/18 AA pathways at >95%, versus 16/18 for the 15-genome clade. [src: cf_formulation_design] It gave 37/62 carbon pathways versus 27/62. [src: cf_formulation_design] The 8-genome clade has 1 respiratory genome. [src: cf_formulation_design] The report concludes the primary analysis understates conservation for this anchor species. [src: cf_formulation_design] The profile table lists 8 genomes in the PROTECT clade and 18/18 AA conservation there. [src: cf_formulation_design]

## Conservation across pathway classes and accessory genes

Mean pathway conservation in metabolic_capability_dependency was 0.907 for intermediate pathways (n = 508) [src: metabolic_capability_dependency], 0.869 for latent capabilities (n = 248) [src: metabolic_capability_dependency] and 0.829 for active dependencies (n = 755). [src: metabolic_capability_dependency] The median was 1.000 in each group. [src: metabolic_capability_dependency] Pathway-level conservation rates did not distinguish latent from active pathways. [src: metabolic_capability_dependency] There, conservation_rate captures whether a pathway is complete in each genome of the species clade. [src: metabolic_capability_dependency]

For the top 5 accessory-dependent pathways (leucine, valine, arginine, lysine, threonine), about 14% of species-level completeness comes from accessory genes. [src: pathway_capability_dependency] Amino acid biosynthesis pathways show the largest core-versus-all gaps, so their completeness depends on genes not universally present in a species. [src: pathway_capability_dependency] These results come from a different report and are not tied to the five species above. See also [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]].

## Caveats

The fitness experiments cover only 48 organisms. Many organisms in the same species clade were not fitness-tested, which may inflate apparent conservation of pathways that are complete but untested. [src: metabolic_capability_dependency]

## Open Directions

- Rerun the conservation table for every species with clade assignments anchored to the PROTECT reference genomes, as done for N. mucosa. This would show how far clade definition shifts the figures.
- Add genomes for G. sanguinis, whose 7-genome pangenome is too small to judge conservation. Test whether 7/18 AA conservation holds.
- Compare core-only and all-gene completeness for each of the five species. This would show whether the accessory contribution seen in other reports weakens the strain-equivalence claim.
- Test conserved predictions against growth or fitness data in more than 48 organisms. This would check the untested-clade inflation.
