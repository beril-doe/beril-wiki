---
type: "Concept"
description: "Why SHAP-style feature attributions over correlated genomic features (KEGG orthologs, genome-scale traits) indicate that a correlated block matters rather than that a specific gene matters, and how fitness-data concordance tests probe their mechanistic grounding."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# Feature Attribution Is Not Gene-Level Evidence When Genomic Features Are Correlated

Models that predict phenotypes from gene content are often read through [[entities/shap]] (SHapley Additive exPlanations, a method that assigns each input feature a share of a model prediction). When the inputs are KEGG Orthology groups (KOs, ortholog families from [[entities/kegg]]) and genome-scale traits, many features are inherited together. Attribution then describes a correlated block of features, not a specific gene. The evidence here comes from a single project, [[summaries/genotype_to_phenotype_enigma__REPORT]], so it is a single-project methodological result rather than a corpus-wide finding [src: genotype_to_phenotype_enigma].

## Credit Splitting Across Correlated Gene Blocks

The project showed that naive SHAP on 4,305 KOs splits credit across correlated gene blocks. Grouping features correlated at |r|>0.8 revealed a 63-feature genome-scale axis that dominates when training sets are small [src: genotype_to_phenotype_enigma].

The grouping used connected components at |r|>0.8. The largest block had 63 features: genome size, gene count, operons, rRNA/tRNA and co-inherited KOs. The report calls this block the "genome scale axis" [src: genotype_to_phenotype_enigma].

The interpretive caveat follows directly from this structure. The report states that individual SHAP values within a group should be read as "this group matters" rather than "this specific KO matters" [src: genotype_to_phenotype_enigma].

## Testing Attributions Against Gene-Fitness Data

The project kept 7 [[entities/kescience-fitnessbrowser]] anchor strains as a biological validation set, not as training data. The validation plan was to train on the full corpus, extract the top SHAP features, expand them to correlation-grouped gene blocks (connected components at |r|>0.8), map those blocks to Fitness Browser loci via `fb_pangenome_link.tsv`, and test whether the loci show significant fitness effects (|t|>4) in matched Fitness Browser experiments. Enrichment over the genome-wide random baseline was the measure of whether the model's features are mechanistically grounded [src: genotype_to_phenotype_enigma].

The outcome was weak concordance. The report describes the SHAP features as mechanistically coherent (condition-specific catabolic genes), but their Fitness Browser concordance was only 1.19×. The report reads this as showing that gene presence across genera and gene essentiality within a strain are different biological questions, answered by different data. This **refines** the caution above: a feature can be a good cross-genus predictor without being a gene whose disruption changes fitness in a given strain. This rests on one project's comparison and should be treated as a strong hypothesis, not a general law [src: genotype_to_phenotype_enigma].

## Tensions

The report is internally inconsistent about the validation status. Its future-directions section says the current 1.19× enrichment uses correlation-expanded blocks, and that whether KEGG-module expansion recovers more mechanistic signal remains untested [src: genotype_to_phenotype_enigma]. Its H3 hypothesis-outcomes section says that full Fitness Browser concordance validation with correlation-group expansion remains to be done [src: genotype_to_phenotype_enigma]. It is therefore unclear whether the 1.19× figure reflects the complete correlation-expanded test or a partial version. Both statements are recorded here unresolved.

## Open Directions

- Run the full Fitness Browser concordance test with correlation-group expansion on all 7 anchor strains, at the |t|>4 threshold against the genome-wide random baseline. This would settle whether the reported 1.19× enrichment reflects the completed correlation-expanded test [src: genotype_to_phenotype_enigma].
- Expand top-SHAP KOs to all KOs in the same KEGG module and recompute Fitness Browser concordance. This would test whether pathway-level expansion recovers additional mechanistic signal, and would distinguish "wrong feature, right pathway" from "wrong pathway" [src: genotype_to_phenotype_enigma].
- Compare SHAP rankings with and without the 63-feature genome-scale block across training-set sizes. This would test how far the dominance of that block in small training sets displaces condition-specific catabolic features [src: genotype_to_phenotype_enigma].
