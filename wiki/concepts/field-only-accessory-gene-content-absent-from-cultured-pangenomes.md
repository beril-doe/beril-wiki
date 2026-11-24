---
type: "Concept"
description: "Whether metagenome-assembled genomes carry accessory KEGG orthologs missing from the cultured-isolate pangenome of the same genus, including community-proxy versus per-MAG test designs and the interpretation of enriched modules."
sources: ["summaries/neon_mag_functional_discovery__REPORT.md"]
---
# Field-only accessory gene content absent from cultured pangenomes

This page covers whether NEON metagenome-assembled genomes (MAGs) carry accessory KEGG orthologs (KOs) that are missing from the cultured-isolate pangenome of the same genus. The evidence comes from one project, [[summaries/neon_mag_functional_discovery__REPORT]]. A community-proxy test returned a methodological null that motivated a per-MAG re-analysis. [src: neon_mag_functional_discovery] The per-MAG analysis supports the hypothesis on the available cohort, but it inherits a 53% cohort attrition from a habitat-biased gap in NMDC per-gene annotation tables. [src: neon_mag_functional_discovery] A sensitivity analysis shows the conclusion holds under reweighting and best-case imputation and fails only under an unrealistic worst case. [src: neon_mag_functional_discovery]

## Community-proxy design (H4): a methodological null

The original H4 test used a community-level KO union as a proxy for per-MAG accessory content. For each shared genus, it took the KOs present in at least 50% of NEON workflows where that genus has a MAG. It contrasted these with the cultured pangenome accessory content of the genus. [src: neon_mag_functional_discovery] The test analysed 24 shared genera. [src: neon_mag_functional_discovery] Pooled NEON-only KOs covered 9,547 / 9,584 (99.6%) of the entire universe. [src: neon_mag_functional_discovery] No KEGG modules were enriched at FDR (false discovery rate) < 0.05. [src: neon_mag_functional_discovery] The median Jaccard similarity between the NEON community and pangenome accessory content was 0.19. [src: neon_mag_functional_discovery] The community proxy is dominated by KOs from co-occurring taxa rather than the target genus, which confirms a caveat in the plan. [src: neon_mag_functional_discovery] The report documents this original underpowered run as a methodological dead end. [src: neon_mag_functional_discovery]

## Per-MAG design (H4b)

The per-MAG contrast used 73 usable MAGs across 19 genera. [src: neon_mag_functional_discovery] Median MAG KO set size was 1,113. [src: neon_mag_functional_discovery] Median field-only KO count per MAG was 343. [src: neon_mag_functional_discovery] Median Jaccard similarity between MAG KOs and the genus accessory pangenome was 0.42. [src: neon_mag_functional_discovery] All MAGs (100%) had at least 10 field-only KOs. [src: neon_mag_functional_discovery] The report concludes that cyanobacterial MAGs (Planktothrix, Dolichospermum) and uncultured peat-soil MAGs (Palsa-465, Palsa-295, Sulfotelmatobacter) carry hundreds of accessory KOs absent from any cultured representative of their genus. [src: neon_mag_functional_discovery]

| Genus | Habitat | MAGs | Median MAG KOs | Median field-only KOs | Median Jaccard |
|---|---|---|---|---|---|
| Planktothrix | water | 8 | 1,073 | 689 | 0.28 [src: neon_mag_functional_discovery] |
| Dolichospermum | water | 7 | 1,025 | 532 | 0.29 [src: neon_mag_functional_discovery] |
| Palsa-465 | soil | 3 | 1,222 | 502 | 0.45 [src: neon_mag_functional_discovery] |
| Puia | soil | 2 | 1,082 | 467 | 0.47 [src: neon_mag_functional_discovery] |
| Sulfotelmatobacter | soil | 5 | 1,253 | 434 | 0.45 [src: neon_mag_functional_discovery] |
| Rubrivivax | benthic/water | 10 | 1,769 | 397 | 0.48 [src: neon_mag_functional_discovery] |
| Palsa-295 | soil | 3 | 1,046 | 384 | 0.51 [src: neon_mag_functional_discovery] |
| [[entities/mycobacterium|Mycobacterium]] | soil | 1 | 1,088 | 71 | 0.54 [src: neon_mag_functional_discovery] |

## Enriched modules and how to read them

In pooled recurrent field-only KOs, 29 KEGG modules were enriched at FDR < 0.05. [src: neon_mag_functional_discovery] The report highlights photosystem, Calvin cycle and lycopene modules. [src: neon_mag_functional_discovery] It also highlights transport modules for oligopeptide, rhamnose and nickel. [src: neon_mag_functional_discovery] M00178 (Ribosome, bacteria) was enriched at 52 / 54 KOs and q = 9.5 × 10⁻²⁶. [src: neon_mag_functional_discovery]

Other enriched modules include:
- M00145, NAD(P)H:quinone oxidoreductase, 15 / 17, q = 1.5 × 10⁻⁵. [src: neon_mag_functional_discovery]
- M00163, Photosystem I, 11 / 11, q = 2.7 × 10⁻⁵. [src: neon_mag_functional_discovery]
- M00016, lysine biosynthesis, 11 / 12, q = 1.9 × 10⁻⁴. [src: neon_mag_functional_discovery]
- M00157, F-type ATPase, 8 / 8, q = 6.4 × 10⁻⁴. [src: neon_mag_functional_discovery]
- M00164, ATP synthase (legacy), 8 / 8, q = 6.4 × 10⁻⁴. [src: neon_mag_functional_discovery]
- M00026, histidine biosynthesis, 12 / 15, q = 6.4 × 10⁻⁴. [src: neon_mag_functional_discovery]
- M00161, Photosystem II, 15 / 23, q = 2.5 × 10⁻³. [src: neon_mag_functional_discovery]
- M00165, Calvin cycle, 11 / 15, q = 3.6 × 10⁻³. [src: neon_mag_functional_discovery]
- M00096, non-mevalonate C5 isoprenoid biosynthesis, 8 / 9, q = 3.4 × 10⁻³. [src: neon_mag_functional_discovery]
- M00097, lycopene biosynthesis, 8 / 9, q = 3.4 × 10⁻³. [src: neon_mag_functional_discovery]
- M00022, shikimate pathway, 10 / 13, q = 3.6 × 10⁻³. [src: neon_mag_functional_discovery]
- M00119, pantothenate biosynthesis, 6 / 6, q = 5.3 × 10⁻³. [src: neon_mag_functional_discovery]
- M00179, Ribosome, archaea (legacy), 30 / 65, q = 6.9 × 10⁻³. [src: neon_mag_functional_discovery]
- M00322, limonene degradation (legacy), 5 / 5, q = 1.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00323, urea cycle (legacy), 5 / 5, q = 1.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00004, pentose phosphate pathway, 7 / 10, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00017, methionine biosynthesis, 7 / 10, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00149, succinate dehydrogenase, 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00156, cytochrome c oxidase cbb3-type, 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00166, reductive pentose phosphate (legacy), 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00123, biotin biosynthesis, 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00202, oligopeptide transport (legacy), 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00220, rhamnose transport system (legacy), 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00246, nickel transport system (legacy), 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]

The photosystem-heavy list reflects the water-skewed cohort. It is not a unique feature of the field-only KO set across all NEON MAGs. [src: neon_mag_functional_discovery] The report attributes the photosystem and Calvin cycle dominance to heavy weighting of Planktothrix and Dolichospermum, whose cultured isolates represent a thin slice of true diversity. [src: neon_mag_functional_discovery]

The ribosome result needs care. Ribosomal proteins appear field-only in 52 of 54 cases, which the report identifies as an artifact of the KE pangenome is_core = false definition, not meaningful accessory novelty. [src: neon_mag_functional_discovery] The report locates the biologically meaningful signal in niche-specific modules rather than housekeeping ones. [src: neon_mag_functional_discovery] It treats oligopeptide, rhamnose and nickel transport, limonene degradation and the urea cycle as the most directly H4-supporting signals, plausibly niche-specific accessory functions under environmental selection that lab cultivation does not reproduce. [src: neon_mag_functional_discovery] This is an interpretation, not a direct test of selection.

## Robustness and cohort bias

The H4b cohort over-represents water habitats. Cyanobacteria have 100% per-gene KO coverage, and soil has 0–30%. [src: neon_mag_functional_discovery] The result therefore generalizes within a water-skewed sub-cohort. [src: neon_mag_functional_discovery] The 73-MAG cohort is a non-random 30% subset of a 246-MAG analysis target, with 173 MAGs missing. [src: neon_mag_functional_discovery] Five soil genera with strong a-priori monoterpene- and lactone-catabolism relevance returned 0 MAGs with per-gene KO data. They were Acidocella, BOG-234, Pseudolabrys, Pseudonocardia and Reyranella. [src: neon_mag_functional_discovery] See also [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]] and [[concepts/genome-type-and-sampling-bias-in-metagenome-assembled-genome-surveys]].

The report bounded the dependence on the missing MAGs with four estimators:

| Estimator | Median field-only KOs / MAG | Median Jaccard | Fraction of MAGs with ≥ 10 field-only KOs |
|---|---|---|---|
| Naive (observed only, n=73) | 371 [src: neon_mag_functional_discovery] | 0.43 [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Inverse-coverage-reweighted (effective n=218) | 319 [src: neon_mag_functional_discovery] | 0.43 [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Best-case imputation (missing MAGs = same-genus median) | 371 [src: neon_mag_functional_discovery] | not reported [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Worst-case (missing MAGs = 0 field-only) | 0 [src: neon_mag_functional_discovery] | not reported [src: neon_mag_functional_discovery] | 29.7% [src: neon_mag_functional_discovery] |

The bootstrap 95% CI on the reweighted median field-only KO count was 180–384, from 2,000 weighted resamples. It overlaps the naive estimate of 371. [src: neon_mag_functional_discovery] The report concludes that the central claim survives reweighting and best-case imputation with essentially no change. [src: neon_mag_functional_discovery] The only failing scenario is the worst case. It assigns zero field-only KOs to all 173 missing MAGs and drops the fraction with ≥10 to 29.7%, at the pre-registered 30% falsification threshold. [src: neon_mag_functional_discovery] The report calls this scenario biologically unrealistic. None of the five fully attrited soil genera is a known monoterpene-naïve or aldehyde-dehydrogenase-only lineage, and published Acidobacteriota genome content suggests substantial niche-specific accessory genes. [src: neon_mag_functional_discovery] It places the realistic range between the reweighted and best-case scenarios, both of which fully support H4b. [src: neon_mag_functional_discovery] The 15-MAG K14731 cohort is a lower bound. The full sub-Arctic peat soil cohort likely contains more novel lactone-hydrolase carriers hidden by annotation gaps. [src: neon_mag_functional_discovery]

## Candidates and proposed follow-up

The report lists 15 MAGs whose accessory content most exceeds the cultured pangenome. It proposes them as hypotheses for cultivation or synthetic-construct work. [src: neon_mag_functional_discovery] It also proposes a within-genus Mantel-like test of MAG-pair functional distance against GTDB-Tk ANI (average nucleotide identity) distance. The test would distinguish uniformly diverged accessory content from habitat-stratified gene gain or loss. [src: neon_mag_functional_discovery]

## Open Directions

- Run the Mantel-like test described above, to separate uniform divergence from habitat-stratified gain or loss within genera.
- Annotate per-gene KOs for soil MAGs, starting with the five fully attrited genera. This would close the habitat-biased annotation gap and test the worst-case scenario directly.
- Repeat the module enrichment on a habitat-balanced cohort, or per habitat, to see which enriched modules persist outside water MAGs.
- Rerun enrichment excluding ribosomal KOs, to check that the niche-specific transport modules (rhamnose, nickel, oligopeptide) remain enriched without the is_core artifact.
- Test the 15 top candidate MAGs against [[entities/kbase-ke-pangenome]] cultured accessory content with other pangenome definitions. Check whether the broad ribosome and housekeeping enrichments are artifacts of incomplete cultured-pangenome coverage. See [[concepts/module-level-enrichment-artifacts-from-broad-substrate-enzymes]].
