<!-- tension-hash: 1878bf802935e572 -->
# Conserved, Essential, or Just Well-Sampled? Competing Accounts of the Conservation–Essentiality Link

Across this corpus one headline result recurs: genes whose loss blocks growth under the assayed condition — *essential* genes — are enriched in the *core* genome, meaning gene clusters present in nearly all genomes of a species pangenome rather than the accessory clusters present in only some. The disagreements gathered under the Tensions heading of [[concepts/gene-essentiality]] are not about whether that gradient exists but about how large it is, what it is made of, and whether the many proxies that stand in for essentiality — conservation, annotation quality, pathway completeness, constraint-based models, co-fitness modules, metabolite production records — are measuring the same thing at all. This page covers every disagreement in the input tension text: the two incompatible headline core fractions; whether the gradient survives pangenome sampling; core enrichment that is not specific to essentiality; lineage-restricted genes that are less core yet more essential; a module analysis structurally blind to essential genes; pathway-level conservation that inverts the gene-level story; metal-fitness enrichment that fails to replicate in a single organism; a respiratory model–measurement mismatch; data types that cannot license essentiality inference at all together with the conditionality of "essential"; discordant model- and module-based knockout prediction accuracy; and a discrepancy in how much metal-gene signal is shared stress response. It matters because several downstream claims in this wiki — that conservation predicts essentiality, that pathway completeness predicts dependency, that models predict knockout phenotypes — inherit whichever side turns out to be right. None of these estimates may be averaged.

## Evidence Sides

### Two headline core fractions for essential genes

**Side A — the lower fraction, larger gene set.** The two conservation–essentiality integrations report different essential-gene core fractions: 82% (and 82.2% under strongest-effect grouping) across approximately 194,000 genes from 43 bacteria. [src: fitness_effects_conservation] [src: conservation_vs_fitness]

**Side B — the higher fraction, different filters.** The other integration reports 86.1% among 148,826 genes from 33 organisms. [src: fitness_effects_conservation] [src: conservation_vs_fitness]

**What the input says about the gap.** This methodological tension involves datasets, organism filters, pangenome mappings, and denominators; the estimates must not be averaged. [src: fitness_effects_conservation] [src: conservation_vs_fitness]

### Real gradient versus pangenome-sampling artifact

**Side A — a directly measured contrast.** Essential genes were 86.1% core versus 81.2% for non-essential genes. [src: conservation_vs_fitness]

**Side B — an unstable denominator.** Clades with only 2 genomes can have trivially high core fractions and pangenome coverage varies. The main *Escherichia coli* clade was absent because it contained too many genomes; Keio, an *E. coli* BW25113 strain, mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness]

### Core enrichment that is not specific to essentiality

**Side A — essentiality tracks core status and better annotation.** ADP1 analyses associate essentiality with core status and richer annotation. [src: acinetobacter_adp1_explorer] [src: alphafold_msa_annotation] [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] [src: fitness_effects_conservation]

**Side B — core clusters are shallow and mostly uncharacterized.** 415,603 core clusters had multiple-sequence-alignment (MSA) depth <10 — too few homologs for confident alignment-based inference — and 68.9% were hypothetical, i.e. carried no assigned function. [src: acinetobacter_adp1_explorer] [src: alphafold_msa_annotation] [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] [src: fitness_effects_conservation]

**Side C — core status is common among genes with no phenotype at all.** Core enrichment coexists with 66% core status among always-neutral genes (no fitness effect in any assayed condition), 24.4% positive-fitness core genes versus 19.9% accessory genes, and function-specific reversals. [src: acinetobacter_adp1_explorer] [src: alphafold_msa_annotation] [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] [src: fitness_effects_conservation]

### Lineage-restricted genes that are more essential

**Side A — the aggregate gradient.** See the two headline core fractions and the essential-versus-non-essential contrast above. [src: fitness_effects_conservation] [src: conservation_vs_fitness]

**Side B — an inversion in the dark proteome.** Persistent hypothetical genes were less core and had narrower ortholog breadth than annotation-lag genes, but had a higher essential fraction, 18.0% versus 13.4%. The source states this does not overturn the aggregate conservation–essentiality gradient; it shows that essentiality can persist in lineage-restricted genes and that short-gene measurement and annotation biases must be separated from biological novelty. [src: truly_dark_genes]

### Modules are core-enriched but contain no essential genes

**Side A — module genes are more conserved.** Module genes were 86.0% core versus 81.5% for all genes. [src: module_conservation]

**Side B — zero essential genes appeared in modules**, because essential genes are invisible to insertion-based independent component analysis (ICA, a decomposition that extracts co-varying gene groups from fitness data): a gene that cannot tolerate an insertion contributes no fitness signal to decompose. The source labels this a measurement tension rather than a biological contradiction. [src: module_conservation]

### Pathway-level conservation against the gene-level gradient

**Side A — latent pathways look more conserved, with a null test.** Latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, with p=0.94. [src: metabolic_capability_dependency] [src: pathway_capability_dependency]

**Side B — the newer analysis reverses the direction on a small matched sample.** Active Dependencies had mean core completeness 0.986 versus 0.975 for Latent Capabilities in only 7 matched model organisms, while that project's larger analysis links pathway variability — not pathway dependency — to openness. [src: metabolic_capability_dependency] [src: pathway_capability_dependency]

### Metal-fitness core enrichment versus a single-organism null

**Side A — strong enrichment in the pooled atlas.** Broad metal-important genes were 87.4% core versus 76.9% baseline. [src: metal_fitness_atlas] [src: field_vs_lab_fitness] [src: metal_specificity]

**Side B — no enrichment in DvH.** *Desulfovibrio vulgaris* Hildenborough (DvH) heavy-metal genes were 71.2% core and not significantly enriched after correction. [src: metal_fitness_atlas] [src: field_vs_lab_fitness] [src: metal_specificity]

**Side C — specificity lowers enrichment, co-stress raises it.** Metal-specific genes were 84.8% core pooled, less enriched than general sick genes at 90.2%, while metal+stress genes were 94.3% core. These results should not be averaged because definitions, thresholds, organism sets, and stress histories differ. [src: metal_fitness_atlas] [src: field_vs_lab_fitness] [src: metal_specificity]

### Respiratory requirement versus model prediction

**Side A — the measured requirement runs against the energetic expectation.** Complex I (the proton-pumping NADH dehydrogenase) was required on quinate despite theoretical quinate production of 0.57 NADH per carbon, while it was dispensable on glucose at 1.50 NADH per carbon. [src: respiratory_chain_wiring] [src: discoveries]

**Side B — the model and the comparative test disagree.** FBA (flux balance analysis, constraint-based prediction of metabolic fluxes) predicted zero NDH-2 flux — NDH-2 being the non-pumping type II NADH dehydrogenase — because it optimizes ATP yield, and the cross-species NDH-2 comparison found no significant compensatory pattern (p=0.52). [src: respiratory_chain_wiring] [src: discoveries]

### What the data can license: production matches, universality, completeness

**Side A — production records cannot support essentiality claims.** Web of Microbes production matches cannot establish uptake, pathway completeness, or gene essentiality: the snapshot has no organism consumption actions, and 107 formula-only matches expanded to 900 candidate molecules. [src: webofmicrobes_explorer] [src: discoveries] [src: essential_metabolome] [src: metabolic_capability_dependency]

**Side B — "essential" is mostly conditional, not universal.** Only 859 of 17,222 ortholog families were universally essential, while 4,799 were variably essential and 11,564 never essential. [src: webofmicrobes_explorer] [src: discoveries] [src: essential_metabolome] [src: metabolic_capability_dependency]

**Side C — completeness does not imply the real repertoire.** 17 of 18 amino-acid pathways were complete in all 7 mapped organisms, yet DvH lacked predicted serine biosynthesis. [src: webofmicrobes_explorer] [src: discoveries] [src: essential_metabolome] [src: metabolic_capability_dependency]

### How well models and modules predict knockouts

**Side A — moderate concordance in one organism.** ADP1 showed moderate FBA–knockout concordance. [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules]

**Side B — poor baseline accuracy and missing mappings.** Annotation-gap analysis found 42.5% baseline FBA accuracy across 574 organism–carbon-source combinations; FBA lacked mappings for 30/51 aromatic-network genes and predicted 0% Complex I essentiality despite 1.76× higher aromatic flux. [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules]

**Side C — different prediction targets, not a contradiction.** Module-ICA had <1% strict knockout (KO) precision despite strong cofitness, versus 95.8% for ortholog transfer; the input states these are different prediction targets rather than a biological contradiction. [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules]

### How much metal-gene signal is shared stress response

**Side A — large overlap, enrichment survives its removal.** The counter-ion analysis found 39.8% overlap between metal-important and NaCl-stress genes, while removing shared-stress genes preserved core enrichment for 12 of 14 metals and the original 87.4% core, OR=2.08 conclusion (OR = odds ratio, the enrichment factor). [src: counter_ion_effects] [src: metal_specificity]

**Side B — a much smaller overlap under stricter criteria.** A separate analysis found 14.7% of metal-important genes sick under osmotic stress; the 2.7× discrepancy reflects stricter thresholds and different organism sets. [src: counter_ion_effects] [src: metal_specificity]

## Possible Reconciliations

All of the following are **hypotheses**, not findings.

- **The two headline fractions may not measure one quantity.** Hypothesis: 82% / 82.2% and 86.1% are estimates of different constructs, since datasets, organism filters, pangenome mappings and denominators differ; if so, both sides are internally correct and the corpus has no single headline number. [src: fitness_effects_conservation] [src: conservation_vs_fitness]
- **The higher fraction may be inflated by small clades.** Hypothesis: because clades with only 2 genomes can have trivially high core fractions, the 86.1% versus 81.2% contrast may be carried by clades too small to define an accessory genome. [src: conservation_vs_fitness]
- **Coverage, not biology, may shape the gradient.** Hypothesis: with the main *Escherichia coli* clade absent for containing too many genomes and Keio mapping at only 26.1% coverage, the best-studied organism contributes least, so the gradient is estimated mainly where coverage happens to be high. [src: conservation_vs_fitness]
- **Core status may be a proxy for "well studied".** Hypothesis: if 415,603 core clusters have MSA depth <10 and 68.9% are hypothetical, the association of essentiality with core status and richer annotation could be partly an annotation-effort confounder; 66% core among always-neutral genes, 24.4% versus 19.9% positive-fitness core/accessory genes and function-specific reversals are consistent with core status being common rather than essentiality-specific. [src: acinetobacter_adp1_explorer] [src: alphafold_msa_annotation] [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] [src: fitness_effects_conservation]
- **A two-population model may absorb the dark-gene inversion.** Hypothesis: a small lineage-restricted essential class (18.0% essential among persistent hypothetical genes versus 13.4%) can coexist with the broad conserved essential class without contradiction — exactly as the source argues — provided short-gene measurement and annotation biases are separated from biological novelty. [src: truly_dark_genes]
- **The module result is already labeled a measurement difference.** Hypothesis: both the 86.0% versus 81.5% core contrast and the absence of essential genes from modules follow from insertion-based ICA's blind spot, leaving no biological claim about essential genes' module membership available either way. [src: module_conservation]
- **The pathway reversal may be metric and sample scope.** Hypothesis: mean conservation (0.869 versus 0.829, p=0.94) and mean core completeness (0.986 versus 0.975 in only 7 matched model organisms) are different metrics on different organism sets; with p=0.94 asserting no difference, the reversal may be noise, and the larger analysis's link from pathway variability to openness may be the surviving signal. [src: metabolic_capability_dependency] [src: pathway_capability_dependency]
- **Metal enrichment may differ by definition and power, not biology.** Hypothesis: 87.4% versus 76.9% pooled and 71.2% in DvH, not significant after correction, differ in definitions, thresholds, organism sets and stress histories. A narrower hypothesis covers only the specificity contrast: restricting to metal-specific genes may strip out genes sick across many stresses, lowering enrichment from 90.2% to 84.8%. This is not a monotone rule about narrow definitions — metal+stress genes carry an extra criterion yet are the most enriched stratum at 94.3% core. [src: metal_fitness_atlas] [src: field_vs_lab_fitness] [src: metal_specificity]
- **The respiratory mismatch may be an objective-function artifact.** Hypothesis: zero predicted NDH-2 flux follows from optimizing ATP yield rather than from biology, so the measured Complex I requirement on quinate at 0.57 NADH per carbon and dispensability on glucose at 1.50 NADH per carbon may reflect regulation or constraints the objective ignores; the p=0.52 cross-species result is consistent with there being no general compensatory rule to find. [src: respiratory_chain_wiring] [src: discoveries]
- **The licensing block may be a distinction of evidence type, not a conflict of fact.** Hypothesis: 107 formula-only matches expanding to 900 candidate molecules with no consumption actions, 859 of 17,222 universally essential families alongside 4,799 variably and 11,564 never essential, and 17 of 18 complete amino-acid pathways in all 7 mapped organisms with DvH lacking predicted serine biosynthesis can all hold simultaneously. [src: webofmicrobes_explorer] [src: discoveries] [src: essential_metabolome] [src: metabolic_capability_dependency]
- **Prediction accuracies may differ by target and by model quality.** Hypothesis: moderate ADP1 FBA–knockout concordance is compatible with 42.5% baseline accuracy across 574 organism–carbon-source combinations if ADP1's model has better mappings than average — noting 30/51 unmapped aromatic-network genes and 0% predicted Complex I essentiality despite 1.76× higher aromatic flux; and <1% strict KO precision versus 95.8% ortholog transfer compares co-fitness grouping against homology transfer, which the input says are different targets. [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules]
- **The overlap gap is attributed to thresholds.** Hypothesis: the 2.7× gap between 39.8% and 14.7% is fully explained by stricter thresholds and different organism sets, in which case the surviving claim is the threshold-robust one — core enrichment preserved for 12 of 14 metals and the original 87.4% core, OR=2.08 conclusion. [src: counter_ion_effects] [src: metal_specificity]

## Resolving Work

**Headline core fractions and pangenome sampling**
- Recompute both fractions on the intersection of the two gene sets — the organisms and genes shared between the approximately 194,000-gene, 43-bacteria set and the 148,826-gene, 33-organism set — holding the essentiality caller fixed; question: does the 82% versus 86.1% gap survive a common denominator? [src: fitness_effects_conservation] [src: conservation_vs_fitness]
- Stratify the essential-core fraction by genomes per clade and re-report the gradient with 2-genome clades excluded; question: how much of the 86.1% versus 81.2% contrast is carried by clades too small to define an accessory genome? [src: conservation_vs_fitness]
- Rebuild the *E. coli* pangenome with genome subsampling so the main clade can be included, then re-map Keio (BW25113); question: does the gradient hold when coverage rises above 26.1%? [src: conservation_vs_fitness]
- Publish both estimates side by side with their filters, mappings and denominators as page-level metadata rather than one reconciled number, per the explicit instruction not to average. [src: fitness_effects_conservation] [src: conservation_vs_fitness]

**Specificity of the core signal and lineage-restricted essentials**
- Recompute essential-versus-neutral core fractions separately for annotated and hypothetical clusters, using the 68.9%-hypothetical and MSA-depth-<10 partition of the 415,603 core clusters; question: does essentiality still predict core status inside the poorly characterized stratum? [src: acinetobacter_adp1_explorer] [src: alphafold_msa_annotation] [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] [src: fitness_effects_conservation]
- Use the 66% core fraction of always-neutral genes as the explicit null for any future core-enrichment claim; question: what enrichment magnitude is distinguishable from background core prevalence? [src: acinetobacter_adp1_explorer] [src: alphafold_msa_annotation] [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] [src: fitness_effects_conservation]
- Test whether the 24.4% versus 19.9% positive-fitness core/accessory contrast and the function-specific reversals share a functional signature, e.g. by COG (Clusters of Orthologous Groups) category; question: which functional classes drive the reversals? [src: acinetobacter_adp1_explorer] [src: alphafold_msa_annotation] [src: conservation_fitness_synthesis] [src: core_gene_tradeoffs] [src: fitness_effects_conservation]
- Length-match and insertion-density-match persistent hypothetical genes against annotation-lag genes before re-testing the 18.0% versus 13.4% essential-fraction difference; question: is the excess essentiality biological or a short-gene measurement artifact? [src: truly_dark_genes]

**Module blind spot**
- Re-derive modules from a non-insertion readout on the same organisms and test whether essential genes then join core-enriched modules; question: is the zero-essential-gene result assay-specific? [src: module_conservation]
- Recompute the 86.0% versus 81.5% module core enrichment with essential genes removed from the background as well as the foreground; question: does enrichment persist against a non-essential-only baseline? [src: module_conservation]
- Quantify the insertion-tolerance floor per organism and flag modules whose members sit near it; question: how many module memberships are unresolvable in principle by insertion-based ICA? [src: module_conservation]

**Pathway level versus gene level**
- Recompute the latent-versus-active comparison on the full organism set rather than the 7 matched model organisms, reporting both mean conservation and mean core completeness; question: does the 0.986 versus 0.975 direction survive sample size, given p=0.94 in the larger comparison? [src: metabolic_capability_dependency] [src: pathway_capability_dependency]
- Enter pathway variability and pathway dependency as competing predictors of pangenome openness in one model; question: which retains signal when both are included? [src: metabolic_capability_dependency] [src: pathway_capability_dependency]
- Audit the 17-of-18 complete amino-acid pathway calls in the 7 mapped organisms against measured phenotypes, starting from DvH's missing predicted serine biosynthesis; question: what is the false-completeness rate of pathway annotation here? [src: webofmicrobes_explorer] [src: discoveries] [src: essential_metabolome] [src: metabolic_capability_dependency]

**Metal-fitness enrichment and stress overlap**
- Apply one metal-importance threshold and one core definition across the pooled atlas and the DvH dataset, then re-test 87.4% versus 76.9% and 71.2%; question: does the DvH null persist under harmonized criteria and correction? [src: metal_fitness_atlas] [src: field_vs_lab_fitness] [src: metal_specificity]
- Decompose the pooled set into general sick (90.2%), metal-specific (84.8%) and metal+stress (94.3%) strata per organism; question: is the ordering consistent across organisms or driven by a few? [src: metal_fitness_atlas] [src: field_vs_lab_fitness] [src: metal_specificity]
- Recompute metal/osmotic overlap on a common organism set across a threshold sweep spanning both studies; question: at which threshold does 39.8% become 14.7%? [src: counter_ion_effects] [src: metal_specificity]
- Re-run the shared-stress removal using the stricter osmotic-sickness definition; question: does core enrichment still hold for 12 of 14 metals, and does the 87.4% core, OR=2.08 conclusion survive? [src: counter_ion_effects] [src: metal_specificity]

**Model–measurement mismatches**
- Re-run FBA on quinate and glucose with the ATP-yield objective relaxed and compare against measurement; question: does any feasible objective reproduce Complex I requirement at 0.57 NADH per carbon and dispensability at 1.50 NADH per carbon? [src: respiratory_chain_wiring] [src: discoveries]
- Repeat the cross-species NDH-2 compensation test with organisms stratified by respiratory-chain composition; question: is p=0.52 a genuine absence of compensation or a pooling effect? [src: respiratory_chain_wiring] [src: discoveries]
- Close the 30/51 missing aromatic-network gene mappings and re-measure accuracy on the 574 organism–carbon-source combinations; question: how much of the 42.5% baseline is mapping loss versus model structure, and does 0% predicted Complex I essentiality change given 1.76× higher aromatic flux? [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules]
- Score the ADP1 model and the 574-combination panel on one shared metric, and evaluate module-ICA against ortholog transfer on an identical knockout set with an identical precision definition; question: do "moderate concordance" versus 42.5%, and <1% versus 95.8%, narrow once target and yardstick are held fixed? [src: adp1_triple_essentiality] [src: annotation_gap_discovery] [src: discoveries] [src: fitness_modules]

**Evidence licensing**
- Link consumption-side data to the metabolite snapshot before any uptake claim; question: how many of the 900 candidate molecules behind 107 formula-only matches survive disambiguation once consumption actions exist? [src: webofmicrobes_explorer] [src: discoveries] [src: essential_metabolome] [src: metabolic_capability_dependency]
- Report the 859 universally essential, 4,799 variably essential and 11,564 never essential split of the 17,222 ortholog families alongside every corpus claim phrased as "essential genes are…"; question: which conclusions hold for the variably essential majority? [src: webofmicrobes_explorer] [src: discoveries] [src: essential_metabolome] [src: metabolic_capability_dependency]
