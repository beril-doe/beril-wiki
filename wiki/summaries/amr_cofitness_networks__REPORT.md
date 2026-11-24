---
type: "Summary"
description: "Summary of the project AMR Co-Fitness Support Networks."
doc_type: "short"
full_text: "sources/amr_cofitness_networks__REPORT.md"
---
# AMR Co-Fitness Support Networks

The report itself warns that the enrichment may reflect shared dispensability in laboratory conditions rather than co-regulation, so the functional enrichment is correlational and unresolved. [src: amr_cofitness_networks]

## Key Findings

### Scope of the analysis
The analysis uses the 28 organisms that have AMR genes, fitness matrices and independent component analysis (ICA) modules. [src: amr_cofitness_networks]

Of 801 AMR genes with fitness data, 769 (96%) have at least one extra-operon cofitness partner at |r| > 0.3. [src: amr_cofitness_networks]

There are 180,370 total cofitness partners and 179,375 extra-operon partners, with only 0.6% excluded as near-operon. [src: amr_cofitness_networks]

Mean support-network size is 233 genes at |r|>0.3. [src: amr_cofitness_networks] It is 110 genes at |r|>0.4. [src: amr_cofitness_networks] It is 71 genes at |r|>0.5. [src: amr_cofitness_networks]

### AMR genes in ICA fitness modules
Only 24% of AMR genes (192/801) are assigned to ICA fitness modules. [src: amr_cofitness_networks]

Their modules have a median of 46 genes versus 27 for non-AMR modules (Mann-Whitney U, MWU, p = 1.7×10⁻⁸). [src: amr_cofitness_networks] The report regards this as robust because ICA captures condition-specific co-regulation rather than shared mean fitness. [src: amr_cofitness_networks]

This indicates that AMR genes, when tightly co-regulated with other genes, sit in large, multi-function cellular programs, not small isolated modules. [src: amr_cofitness_networks] The report reads these larger, cross-organism conserved modules as broad cellular programs with genuine co-regulatory structure. [src: amr_cofitness_networks]

AMR genes occur in 136 unique module families. [src: amr_cofitness_networks] Of the AMR gene-module assignments, 99% (208/209) are in cross-organism conserved families, interpreted as ancient regulatory relationships. [src: amr_cofitness_networks]

Module size does not differ between efflux and enzymatic mechanisms (both 48, MWU p = 0.91). [src: amr_cofitness_networks]

Notebook 02 covers AMR genes in ICA modules, module size comparison and family membership. [src: amr_cofitness_networks]

### Functional enrichment with InterProScan GO
InterProScan GO results show flagellar and biosynthesis enrichment, which the old SEED annotations did not. [src: amr_cofitness_networks]

InterProScan Gene Ontology (GO) annotations give 68% gene coverage, 3.6× better than old SEED annotations. [src: amr_cofitness_networks]

Pfam has 88% coverage versus 68% for GO in the AMR support-network analysis. [src: amr_cofitness_networks]

With InterProScan GO, flagellar and amino acid biosynthesis terms are enriched across organisms (FDR = false discovery rate; OR = odds ratio):

- GO:0071973, flagellum-dependent cell motility: 5 organisms at FDR<0.05, mean OR 4.7. [src: amr_cofitness_networks]
- GO:0044780, flagellum assembly: 5 organisms, mean OR 5.3. [src: amr_cofitness_networks]
- GO:0009288, bacterial-type flagellum: 4 organisms, mean OR 4.9. [src: amr_cofitness_networks]
- GO:0071978, flagellum-dependent swarming: 4 organisms, mean OR 5.0. [src: amr_cofitness_networks]
- GO:0000105, histidine biosynthesis: 3 organisms, mean OR 5.3. [src: amr_cofitness_networks]
- GO:0000162, tryptophan biosynthesis: 3 organisms, mean OR 5.3. [src: amr_cofitness_networks]

Notebook 03b tests this hypothesis (H1) with InterProScan GO and reports flagellar/biosynthesis enrichment. [src: amr_cofitness_networks] Notebook 03 had reported a null result for H1/H3 with old SEED annotations. [src: amr_cofitness_networks]

Energy metabolism was not enriched (0/25 organisms, fold 0.91 in the permutation test), attributed to its usefulness in laboratory conditions. [src: amr_cofitness_networks]

The conserved core of support networks includes transmembrane transport (87–100% of organisms). [src: amr_cofitness_networks] It also includes signal transduction (87–100%). [src: amr_cofitness_networks] It includes transcription regulation (96–100%). [src: amr_cofitness_networks] It includes phosphorelay signaling (91–100%). [src: amr_cofitness_networks] Flagellar motility (53–61%) forms a second tier of conservation. [src: amr_cofitness_networks] Amino acid biosynthesis (30–73%) forms the same second tier. [src: amr_cofitness_networks]

### Mechanism specificity
Mechanism-specific enrichment is suggestive but does not survive correction. [src: amr_cofitness_networks]

Efflux AMR genes show the strongest amino acid biosynthesis enrichment, with histidine in 6 organisms and tryptophan in 5. [src: amr_cofitness_networks]

Metal resistance genes show stronger chemotaxis enrichment, in 4 organisms. [src: amr_cofitness_networks]

However, no GO term is significantly mechanism-specific after FDR correction. [src: amr_cofitness_networks] The only hint is histidine biosynthesis (efflux 68% vs metal 30%, p = 0.013 uncorrected, q = 0.18 after FDR). [src: amr_cofitness_networks]

The mechanism-specific GO analysis gives 212 significant tests of 9,244 at FDR<0.05, with efflux histidine biosynthesis in 6 organisms as the top signal. [src: amr_cofitness_networks]

### Organism wiring versus mechanism
Different AMR mechanisms in the same organism have mean GO Jaccard 0.375, sharing 38% of cofitness GO terms. [src: amr_cofitness_networks]

The same mechanism across organisms has mean GO Jaccard 0.207, sharing only 21%. [src: amr_cofitness_networks]

The difference between these comparisons is highly significant (MWU p = 4.3×10⁻¹³). [src: amr_cofitness_networks]

The organism's regulatory landscape therefore shapes the AMR support network far more than the type of resistance mechanism. [src: amr_cofitness_networks] The report regards this as robust to the dispensability confound, because whatever the reason AMR genes correlate with partners, each organism has its own characteristic set of dispensable or co-varying genes. [src: amr_cofitness_networks] It interprets this as a genuine structural property of genome organization, not an artifact of enrichment categories. [src: amr_cofitness_networks]

For example, a *Pseudomonas* efflux pump shares more cofitness partners with a beta-lactamase in the same *Pseudomonas* than with an efflux pump in *Shewanella*. [src: amr_cofitness_networks]

The report also regards this as consistent with compensation integrating AMR genes into whatever programs the organism already has. [src: amr_cofitness_networks] Eckartt et al. (2024, Nature) identified compensatory mutations targeting the same functional pathway as the resistance mutation. [src: amr_cofitness_networks]

Notebook 04b tests the cross-organism hypothesis (H4) with InterProScan GO and confirms organism-specificity. [src: amr_cofitness_networks] Notebook 04 had tested H4 with old KEGG annotations. [src: amr_cofitness_networks]

### Fitness cost
Support-network size does not correlate with AMR gene fitness cost (Spearman rho = −0.006, p = 0.87, N = 769). [src: amr_cofitness_networks] The report suggests the absence may reflect insufficient variance in fitness cost across genes. [src: amr_cofitness_networks]

This holds within mechanisms (efflux rho = −0.049, enzymatic rho = +0.038, metal rho = −0.031; all p > 0.4). [src: amr_cofitness_networks]

Neighborhood size does not explain the uniform cost of resistance (+0.086 from amr_fitness_cost). [src: amr_cofitness_networks]

The report cites amr_fitness_cost as finding that mechanism predicts conservation (metal 44% accessory versus efflux 13%) but not cost. [src: amr_cofitness_networks] It attributes cost to the organism's gene content and growth context, and conservation to the mechanism's acquisition history. [src: amr_cofitness_networks] Olivares Pacheco et al. (2017) showed that efflux pump costs in *P. aeruginosa* are metabolic (PMF drain) and compensated by metabolic rewiring. [src: amr_cofitness_networks]

### Annotation quality
Annotation quality changed what the analysis could detect. [src: amr_cofitness_networks]

Old SEED/KEGG coverage was 40–80% per organism and variable, versus 60% uniform for InterProScan GO. [src: amr_cofitness_networks]

Old SEED annotations detected no significant enrichment in AMR support networks (0/280). [src: amr_cofitness_networks] With InterProScan GO, 35/3,193 tests were significant. [src: amr_cofitness_networks] The report concludes that InterProScan GO turned a null result into a significant one, showing legacy annotations are insufficient for functional genomics. [src: amr_cofitness_networks]

With old annotations no GO term reached ≥3 organisms, versus 6 with InterProScan GO (flagella, amino acid biosynthesis). [src: amr_cofitness_networks]

Within-mechanism cross-organism Jaccard rose from 0.069 to 0.207 (3× higher). [src: amr_cofitness_networks] Cross-mechanism Jaccard rose from 0.249 to 0.375 (1.5× higher). [src: amr_cofitness_networks]

The old KEGG test of cross-mechanism exceeding within-mechanism overlap gave p = 1.0, versus 4.3×10⁻¹³ with InterProScan GO. [src: amr_cofitness_networks] Old KEGG found 2 mechanism-specific terms (lipoprotein, toluene tolerance) at FDR<0.05, versus 0 for InterProScan GO. [src: amr_cofitness_networks] A permutation enrichment with old SEED gave 23 significant of 250 tests, with membrane/cell wall on top (24%, fold 1.12). [src: amr_cofitness_networks]

Genome-wide cofitness analyses require high-coverage, uniformly computed annotations, and InterProScan on pangenome cluster representatives provides them. [src: amr_cofitness_networks]

### Co-regulation versus shared dispensability

The enrichment of flagellar motility, chemotaxis and amino acid biosynthesis admits two interpretations. [src: amr_cofitness_networks]

Interpretation A (co-regulation): shared transcription factors or signaling cascades co-control resistance, motility and biosynthesis, producing condition-specific cofitness. [src: amr_cofitness_networks] Sagawa et al. (2017) validated that cofitness recovers transcriptional regulatory relationships in 24 bacteria, and the report says its analysis identifies functional categories. [src: amr_cofitness_networks] Martinez & Rojo (2011) reviewed the link between metabolism and intrinsic resistance, noting that global metabolic regulators modulate antibiotic susceptibility. [src: amr_cofitness_networks] The report says this framework supports its findings only if Interpretation A is correct. [src: amr_cofitness_networks] It proposes that proton-motive-force (PMF) competition could explain efflux–flagellar cofitness, since both use PMF, but shared dispensability could produce the same signal. [src: amr_cofitness_networks]

Interpretation B (shared dispensability): AMR, flagellar and biosynthetic genes are metabolic burdens in standard laboratory conditions, giving modestly positive knockout fitness across most experiments. [src: amr_cofitness_networks] AMR genes, flagellar genes and biosynthesis genes are all metabolic burdens under these conditions. [src: amr_cofitness_networks]

Under B, the cofitness signal reflects shared membership in a laboratory-dispensable gene class, not a mechanistic connection. [src: amr_cofitness_networks] Cofitness needs condition-specific covariation, but dispensable genes could share responses to nutrient richness or starvation without being co-regulated. [src: amr_cofitness_networks] Pearson r subtracts each gene's mean fitness, so uniformly slightly positive fitness alone would give zero correlation. [src: amr_cofitness_networks]

The report argues the enriched categories favor B. FB experiments use shaken liquid culture, where flagella are useless. [src: amr_cofitness_networks] Nearly all use shaken culture, with no surface to swim on or gradient to follow. [src: amr_cofitness_networks] Most use rich or defined media with amino acid supplements, where biosynthesis is redundant. [src: amr_cofitness_networks] Motility, chemotaxis and biosynthesis are exactly the categories that would be dispensable in shaken flask culture. [src: amr_cofitness_networks]

The report names a general caveat for cofitness-based functional genomics: genes that are dispensable under experimental conditions may show artifactual co-regulation signals, a concern relevant beyond AMR to any cofitness study using lab-grown organisms. [src: amr_cofitness_networks] It also cautions that functional enrichment can reflect shared experimental context, citing Nichols et al. (2011, Cell), who showed condition-dependent fitness profiles reveal gene function in *E. coli*. [src: amr_cofitness_networks]

## Caveats and Open Work

- The enrichment may reflect shared dispensability rather than genuine co-regulation. [src: amr_cofitness_networks]
- The permutation test matched random genes by conservation class but not by mean fitness level. [src: amr_cofitness_networks] The report suggests flagellar enrichment might disappear entirely if random genes were matched to the slightly-positive fitness distribution of AMR genes. [src: amr_cofitness_networks]
- A fitness-matched permutation, drawing random genes with the same slightly-positive fitness distribution, is needed to tell the two apart. [src: amr_cofitness_networks]
- The report names this permutation, with mean fitness from −0.05 to +0.05, as the key unresolved test. [src: amr_cofitness_networks]
- The report calls the most important follow-up a permutation test drawing random non-AMR genes matched on mean fitness level, not just conservation class. If random genes with fitness between −0.05 and +0.05 also show flagellar/biosynthesis enrichment in their cofitness neighborhoods, the enrichment is a shared-dispensability artifact. [src: amr_cofitness_networks]
- If AMR genes uniquely enrich even among fitness-matched genes, the report says the co-regulation interpretation is supported. [src: amr_cofitness_networks]
- High cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation, even without the dispensability confound. [src: amr_cofitness_networks]
- Mechanism-specific results are weak after multiple-testing correction. [src: amr_cofitness_networks]
- Cofitness treats missing fitness values as zero in z-score space (np.nan_to_num), which approximates but does not equal pairwise-complete Pearson correlation. [src: amr_cofitness_networks] The report considers this unlikely to affect conclusions because FB matrices are relatively dense. [src: amr_cofitness_networks]
- Broad GO terms (transmembrane transport, membrane) appear in nearly all networks and genomes, potentially masking specific signals. [src: amr_cofitness_networks]
- At |r| > 0.3 the mean network size is 233 genes, including many weak associations; confirmation at |r| > 0.4 is needed. [src: amr_cofitness_networks]
- The 28 organisms are lab-adapted, phylogenetically biased (many Pseudomonas) and ecologically limited. [src: amr_cofitness_networks]
- The 5-ORF exclusion zone uses matrix row index as a proxy for genomic proximity, which may not reflect chromosomal gene order. [src: amr_cofitness_networks] The begin, end and strand columns are loaded and could support coordinate-based exclusion. [src: amr_cofitness_networks]
- The report proposes computing cofitness separately for antibiotic conditions and standard growth. Elevated AMR–flagella cofitness specifically under antibiotic stress would support a regulatory connection. [src: amr_cofitness_networks]
- The report proposes checking flagellar knockout mean fitness across FB experiments. Positive fitness would confirm shared dispensability as plausible, while near-zero or negative fitness would strengthen co-regulation. [src: amr_cofitness_networks]
- The report proposes Pfam domain-level enrichment, which may reveal more specific support-network functions than broad GO terms. [src: amr_cofitness_networks]
- The report proposes testing phage defense, secondary metabolite and other condition-specific gene classes for the same cofitness patterns. If they show them, the signal is general to laboratory-dispensable genes, not AMR-specific. [src: amr_cofitness_networks]

## Slots Into

- [[concepts/shared-dispensability-as-a-confound-in-cofitness-enrichment]]: the dispensability argument for flagellar, chemotaxis and biosynthesis enrichment, and the unrun fitness-matched permutation. [src: amr_cofitness_networks]
- [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]]: 0/280 versus 35/3,193 significant tests by annotation source. [src: amr_cofitness_networks]
- [[concepts/organism-specific-versus-mechanism-specific-wiring-of-amr-support-networks]]: Jaccard 0.375 within organisms versus 0.207 across organisms. [src: amr_cofitness_networks]
- [[concepts/amr-genes-in-ica-fitness-modules]]: 24% of AMR genes in modules, with larger median size. [src: amr_cofitness_networks]
- [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]]: the conserved core and second tier of functions. [src: amr_cofitness_networks]
- [[concepts/fitness-cost-of-antimicrobial-resistance-genes]]: no correlation between network size and fitness cost. [src: amr_cofitness_networks]
