---
type: "Concept"
description: "How duplicate strains, uneven organism and metal coverage, missing pangenome links, lack of dose normalization, identifier mismatches and absent essential genes limit which organisms and genes enter cross-organism fitness conservation estimates."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/pitfalls.md"]
---
# Organism coverage and attrition in cross-organism fitness conservation analyses

Cross-organism fitness conservation estimates rest on fewer organisms and genes than the underlying screens cover. Reports document losses from duplicate strains, uneven metal coverage, missing pangenome links, identifier mismatches and essential genes that transposon screens cannot see. [src: metal_fitness_atlas, metal_specificity, counter_ion_effects] The evidence is direct counting within each report. For excluded organisms, two reports state that they consider systematic bias unlikely because the organisms are taxonomically diverse. [src: metal_fitness_atlas, metal_specificity] For essential genes, the reports say the exclusion makes core-enrichment estimates conservative. [src: metal_fitness_atlas, metal_specificity]

## Literature Context

The only candidate paper is a cross-species Tn-seq (transposon sequencing) study of cold shock adaptation in two mesophilic bacteria, Escherichia coli and Bacillus subtilis [PMID 41040150](https://pubmed.ncbi.nlm.nih.gov/41040150/). The authors monitored mutant fitness across the full course of the cold shock response and during sustained low-temperature growth. In B. subtilis they report a temporally structured program. Membrane fluidity and cell wall remodeling mattered most early, and post-transcriptional regulation mattered during late-stage recovery [PMID 41040150](https://pubmed.ncbi.nlm.nih.gov/41040150/). The cross-species comparison found both conserved and species-specific mechanisms. RNA metabolism and ribosome/translation regulators played broad roles, and RsmA and RsmH showed a conserved synergy in cold adaptation [PMID 41040150](https://pubmed.ncbi.nlm.nih.gov/41040150/). The evidence is an abstract only, covers two organisms, and concerns temperature rather than metals.

This paper is related to the corpus only in a general way. It also uses transposon-mutant fitness in more than one species to ask which determinants are conserved and which are lineage-specific. The corpus asks the same kind of question, but across 22 of 31 metal-tested organisms, with core-genome enrichment as the conservation measure. The abstract does not say how many organisms or genes were lost to filtering. It does not mention duplicate strains, missing pangenome links, identifier mismatches, dose normalization or essential genes. It therefore neither supports nor contradicts the corpus's attrition figures. These include the drop from 22 to 18 organisms after duplicate removal, the 7 of 31 organisms lost to locusId format mismatches, and the 40.7% gene attrition in the specificity analysis. They also include the single-organism coverage of several metals and the conservative bias from absent essential genes. The candidate paper does not address these findings.

The one point of contact is scale. The cold shock study compares only two species, so its conserved-versus-specific conclusions rest on a small organism set [PMID 41040150](https://pubmed.ncbi.nlm.nih.gov/41040150/). The corpus's own cautions about thin coverage are consistent with that limitation. Examples are cadmium (1 organism) and uranium (2 organisms), which show no significant core enrichment, a result the corpus attributes to limited coverage. The cold shock paper gives no evidence on whether broader sampling would change its conclusions. The corpus's open directions, which are fixing identifiers, controlling for phylogeny, normalizing dose and adding organisms, are not tested by this literature. A broader literature search would be needed to place them.

## Organism attrition

Each filtering step removes organisms, as the figures below show. [src: metal_fitness_atlas, metal_specificity]

- The atlas conservation analysis covers 22 of 31 metal-tested organisms (71%). [src: metal_fitness_atlas] A separate caveat states that 22 of 48 organisms have pangenome links and 26 lack Fitness Browser–pangenome mappings. [src: metal_fitness_atlas] The report gives both figures; they use different denominators.
- The 9 atlas organisms excluded for lacking links are Putida, Keio, SynE, Miya, Kang, BFirm, Cola, Ponti, and Dino. [src: metal_fitness_atlas] The report considers them taxonomically diverse, so it says exclusion is unlikely to introduce systematic bias. [src: metal_fitness_atlas]
- Removing 4 duplicate *P. fluorescens* FW300 strains, and keeping only pseudo3_N2E3, reduces the analysis from 22 to 18 organisms. [src: metal_fitness_atlas] Multiple *P. fluorescens* strains were flagged as inflating apparent conservation through phylogenetic non-independence. [src: metal_fitness_atlas] Core enrichment stayed robust after removal (OR=2.065, p=5.9e-141, versus OR=2.083, p=4.3e-162 with all organisms). The report concludes the result is not driven by Pseudomonas overrepresentation. [src: metal_fitness_atlas]
- Other analyses set their own cutoffs. The cross-resistance report extracted 119,561 genes for 28 organisms with ≥3 metals, from 30 extracted and 2 excluded. [src: metal_cross_resistance] The NaCl overlap analysis included 19 of 25 organisms with NaCl data. [src: counter_ion_effects]

## Identifier mismatches

Format mismatches silently removed organisms and many gene records. See [[concepts/join-key-validity-and-identifier-format-mismatches]].

- In the specificity analysis, 7 of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) could not be processed. Their metal-important gene locusIds did not match the fitness matrix index format. [src: metal_specificity]
- The 24 analyzed organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity] The report notes 40.7% gene attrition, and the excluded genes may differ in specificity. [src: metal_specificity]
- The excluded organisms include the model organisms Keio (*E. coli*), MR1 (*Shewanella*), and ANA3. [src: metal_specificity] The report states their absence is not expected to introduce systematic bias. [src: metal_specificity]
- Earlier, a similar type mismatch had dropped DvH (495 metal-important genes) and Btheta (276 genes) without warning. [src: pitfalls] The processing loop reported "no fitness matrix or no non-metal experiments" although the matrix existed. [src: pitfalls]
- That silent DvH exclusion made essential-metal specificity look like 0% for Mo, W, Se and Mn. After the fix, the values were Manganese (61%), Molybdenum (61%), Tungsten (57%) and Selenium (46%). [src: discoveries]
- The recommended fix is to convert both sides to strings before matching. The recommended detection is to compare output organism counts with expected input. [src: pitfalls] The report also proposes resolving the integer-versus-string mismatch for the seven excluded organisms to recover the remaining 40% of gene records. [src: metal_specificity]

## Uneven metal coverage

See [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]].

- Cobalt and nickel were tested in 27 organisms. Uranium, chromium, mercury, cadmium, selenium and manganese were tested in only 1–2, so rare-metal patterns reflect DvH and psRCH2 biology. [src: metal_fitness_atlas]
- In the counter-ion report, manganese, cadmium, selenium, mercury, iron, molybdenum and tungsten were tested in only 1 organism (DvH). Their overlap statistics lack cross-organism replication. [src: counter_ion_effects]
- Manganese and tungsten each have one organism (DvH). [src: metal_fitness_atlas] Chromium and uranium each have two (DvH, psRCH2). [src: metal_fitness_atlas]
- Cadmium (1 organism, delta=-0.010, p=0.92) and uranium (2 organisms, delta=+0.035, p=0.34) show no significant core enrichment. The report attributes this likely to limited organism coverage. [src: metal_fitness_atlas]
- Six USGS (United States Geological Survey) critical-minerals metals were tested in only 1–2 organisms. The report proposes 5+ organisms each. [src: metal_fitness_atlas]

## Dose and experiment-count effects

Unequal experiment numbers and concentrations make organisms hard to compare. [src: metal_fitness_atlas, metal_cross_resistance, counter_ion_effects]

- The atlas has no dose-response normalization. Concentrations vary across organisms (nickel 0.01-2.0 mM), and effects depend on concentration relative to each organism's tolerance. [src: metal_fitness_atlas] The cross-resistance report likewise says concentration differences could influence its estimates. [src: metal_cross_resistance] The atlas report proposes normalizing fitness effects by metal concentration relative to MIC. [src: metal_fitness_atlas]
- The atlas report also proposes phylogenetic independent contrasts to control phylogenetic non-independence across organisms. [src: metal_fitness_atlas]
- Organisms range from 3 to 112 metal experiments, affecting the reliability of per-organism matrices. [src: metal_cross_resistance]
- SynE is a shared-stress outlier at 88.6% (565/638 genes). It ran 12 NaCl (sodium chloride) dose-response experiments spanning 0.5–250 mM, against 1–6 for other organisms. [src: counter_ion_effects] The n_sick >= 1 threshold is much easier to meet with 12 experiments. [src: counter_ion_effects]

## Essential genes

Putatively essential genes (~14.3% of protein-coding genes) lack transposon insertions and are absent from NaCl and metal fitness data. They are 82% core, and their exclusion affects original and corrected conservation analyses equally. [src: counter_ion_effects] The atlas says this makes observed core enrichment a conservative estimate. [src: metal_fitness_atlas] The specificity report says the same: the true baseline core fraction is likely lower than 81%, so the reported deltas are conservative. [src: metal_specificity] It also states that the absence biases all conservation estimates toward core enrichment. [src: metal_specificity] See [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].

## Open Directions

- Fix the locusId format for the seven excluded organisms and rerun specificity, to test whether the 40.7% attrition changes the results.
- Rerun conservation estimates with a phylogenetic control, such as independent contrasts, in place of the single duplicate-strain removal.
- Normalize fitness by metal concentration relative to MIC, then test whether the rare-metal results (cadmium, uranium) survive.
- Test additional organisms for manganese, chromium, uranium and tungsten, to replace single-organism results with replicated ones.
- Rerun the NaCl overlap with a per-organism experiment-count correction, to test whether SynE's outlier status is a threshold artifact.
