---
type: "Concept"
description: "Under-tested metals (critical minerals, rare earths) and organisms in barcode transposon fitness data and the experiments that would close those gaps."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md"]
---
# Metal coverage gaps and proposed validation experiments

This page collects the metals and organisms that are thinly tested in barcode transposon fitness data, and the experiments the source reports propose to fill those gaps. The evidence is descriptive coverage counts plus proposals from the [[summaries/metal_fitness_atlas__REPORT]], with supporting notes from two other reports. The experiments are proposals, not results. Cross-species statistics for several metals rest on one or two organisms. [src: metal_fitness_atlas, counter_ion_effects]

## Metals tested in few organisms
The metal_fitness_atlas report states that six metals on the United States Geological Survey (USGS) critical minerals list are tested in only 1-2 organisms. It proposes 5+ organisms each, to enable the cross-species conservation analysis. [src: metal_fitness_atlas] The counter_ion_effects report separately notes that manganese, cadmium, selenium, mercury, iron, molybdenum and tungsten were tested in only 1 organism (DvH). Their overlap statistics therefore have no cross-organism replication. [src: counter_ion_effects] See also [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].

## Organisms with little or no metal data
Pseudomonas putida KT2440 has Fitness Browser (FB) fitness matrices but zero metal experiments. The report says it is the only FB organism with no metal data. [src: metal_fitness_atlas] It is a workhorse for bioremediation and metabolic engineering. [src: metal_fitness_atlas] Two atlas organisms have 54 novel metal candidate genes each but have been tested only against iron. [src: metal_fitness_atlas] These are Methanococcus maripaludis S2 and JJ. [src: metal_fitness_atlas] The Fitness Browser contains no rare earth element experiments. [src: metal_fitness_atlas] More broadly, the atlas scores 27,702 species but cannot validate predictions for organisms without random barcode transposon sequencing (RB-TnSeq) libraries. [src: metal_fitness_atlas] No transposon sequencing (TnSeq) data exists for any Acidithiobacillus species. [src: metal_fitness_atlas]

## Proposed experiments by metal
Manganese has 1 organism (DvH), which shows 100% core enrichment (delta=+0.198). [src: metal_fitness_atlas] The report proposes manganese tests in MR-1, Keio, Cup4G11, Putida and Caulo. [src: metal_fitness_atlas] Mn is a USGS critical mineral, and MR-1 can reduce Mn(IV), so it would test metal reducers. [src: metal_fitness_atlas]

Chromium has 2 organisms (DvH, psRCH2). [src: metal_fitness_atlas] The proposed organisms are MR-1, Cup4G11, Keio and pseudo3_N2E3. [src: metal_fitness_atlas] Cr is a DOE priority contaminant. [src: metal_fitness_atlas] The Oak Ridge FW300 Pseudomonas strains were isolated from Cr-contaminated groundwater but have never been tested against chromate. [src: metal_fitness_atlas]

Uranium has 2 organisms (DvH, psRCH2). [src: metal_fitness_atlas] The proposed organisms are MR-1, ANA3, PV4 and Cup4G11. [src: metal_fitness_atlas] U is the central ENIGMA contaminant, and MR-1 can reduce U(VI). [src: metal_fitness_atlas] The conservation delta is +0.035 (p=0.34), which is not significant. More organisms would show whether uranium fitness genes are neutral or the effect was underpowered. [src: metal_fitness_atlas]

Tungsten has 1 organism (DvH), with strong core enrichment (delta=+0.145). [src: metal_fitness_atlas] W is a USGS critical mineral and an essential cofactor for some enzymes. [src: metal_fitness_atlas] The report proposes Methanococcus_S2, Methanococcus_JJ and Keio, to test whether tungsten dependence is unique to sulfate reducers. [src: metal_fitness_atlas]

See [[entities/manganese]], [[entities/chromium]], [[entities/uranium]], [[entities/tungsten]] and [[entities/pseudomonas-fluorescens-fw300-n2e3]].

## Rare earth elements
The metal_fitness_atlas report proposes lanthanum chloride RB-TnSeq at 0.1-1 mM in Putida, Cup4G11, Keio and Marino. This would identify the first genome-wide gene set for rare earth element (REE) tolerance. [src: metal_fitness_atlas] Cerium chloride at 0.1-1 mM on the same panel would show whether REE tolerance uses a shared or element-specific gene set. [src: metal_fitness_atlas] The lanthanide_methylotrophy_atlas report independently proposes targeted RB-TnSeq with La/Ce chloride in the FB panel, following the same Priority 2 proposal. [src: lanthanide_methylotrophy_atlas] It expects the first transposon-validated REE-tolerance gene set in xoxF-carrying Pseudomonas putida, Cupriavidus, Sphingomonas and similar soil organisms. [src: lanthanide_methylotrophy_atlas] See [[entities/rare-earth-elements]] and [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Methanococcus maripaludis
M. maripaludis S2 is a methanogenic archaeon. It needs Ni for hydrogenase and W/Mo for formylmethanofuran dehydrogenase. [src: metal_fitness_atlas] The report proposes Ni, Co, Cu, Zn, W and Mo tests, noting that archaea are underrepresented in metal tolerance studies. [src: metal_fitness_atlas] Strain JJ would get the same panel, and the cross-strain comparison would reveal strain-specific metal adaptation. [src: metal_fitness_atlas] See [[entities/methanococcus-maripaludis]].

## Pseudomonas putida
The report proposes a full panel (Co, Ni, Cu, Zn, Al, Cr, U) on Putida. This would link the atlas to the P. putida engineering literature. Putida has the 5th-highest metal gene repertoire score among FB organisms (0.707), and testing would validate or refute that prediction. [src: metal_fitness_atlas] See pseudomonas putida.

## Bioleaching and metal-reducing species
The report proposes building RB-TnSeq libraries for key bioleaching species. This would bridge the gap between the atlas and industrial applications. [src: metal_fitness_atlas] Proposed organisms:
- Acidithiobacillus ferrooxidans under Fe, Cu, Co, Ni and Zn would give the first genome-wide functional map of bioleaching gene requirements. [src: metal_fitness_atlas]
- Geobacter sulfurreducens under Fe(III), Mn(IV) and U(VI) reduction would identify genes for extracellular electron transfer and metal transformation. [src: metal_fitness_atlas]
- Leptospirillum ferrooxidans under Fe(II) oxidation and acid conditions would reveal why this genus specializes in bioleaching environments. [src: metal_fitness_atlas]

## Projected gain
The report projects that the experiments would expand the atlas from 14 to 16+ metals by adding REEs. [src: metal_fitness_atlas] They would expand it from 24 to 27+ organisms with fitness data. [src: metal_fitness_atlas] Critical-metal coverage would grow from 1-2 organisms to 5+. [src: metal_fitness_atlas] Cross-species statistical power for manganese, chromium, uranium and tungsten would rise from suggestive to definitive. [src: metal_fitness_atlas] This is the report's projection and has not been tested.

## Open Directions
- Run manganese RB-TnSeq in Shewanella MR-1 and at least one non-reducer. This would test whether DvH's 100% core enrichment is universal and whether metal reducers differ.
- Test uranium in MR-1, ANA3, PV4 and Cup4G11. This would settle whether the non-significant delta (+0.035) reflects neutrality or low power.
- Screen chromate in the Oak Ridge FW300 Pseudomonas strains. This would test strains isolated from Cr-contaminated groundwater.
- Run La and Ce panels in Putida, Cup4G11, Keio and Marino. This would produce the first REE-tolerance gene sets and show whether they are shared.
- Run tungsten and nickel panels in both M. maripaludis strains. This would test whether W dependence is specific to sulfate reducers and show strain differences.
- Rerun the overlap statistics after new organisms are added. This would replace the single-organism (DvH) results with cross-organism replication.
