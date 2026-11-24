---
type: "Dataset"
description: "Complete-gene-deletion knockout collection of Acinetobacter baylyi ADP1 with essentiality calls and growth on carbon sources, as combined with TnSeq calls."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md"]
aliases: ["ADP1 single-gene deletion collection", "de Berardinis 2008 deletion collection", "de Berardinis knockout collection"]
---
# de Berardinis et al. 2008 ADP1 deletion mutant collection

The de Berardinis et al. (2008) collection is a complete collection of single-gene deletion mutants of *Acinetobacter baylyi* ADP1, also called the ADP1 single-gene deletion collection. [src: adp1_triple_essentiality] Two BERIL reports use it as experimental ground truth, one for growth on carbon sources and one for essentiality calls. [src: adp1_triple_essentiality] The data reach both reports through a user-provided SQLite file. [src: adp1_deletion_phenotypes, adp1_triple_essentiality] The evidence below describes how the collection was used, not a new test of the collection itself. See [[entities/acinetobacter-baylyi-adp1]] for the organism.

## Key facts

- The collection supplies deletion-mutant growth on 8 carbon sources: glucose, acetate, asparagine, butanediol, glucarate, lactate, pyruvate, and succinate. [src: adp1_triple_essentiality]
- One report uses it as essentiality ground truth in both of its studies. The original study used mutant growth rates on 8 carbon sources. The refined study used essentiality calls for rich (LB) and minimal media. [src: adp1_triple_essentiality]
- The refined study took the calls from the `essentiality_lb` and `essentiality_minimal` columns of `user_data/berdl_tables.db`. That file was first assembled in the `acinetobacter_adp1_explorer` project. [src: adp1_triple_essentiality]
- The same database has a genome_features table. It holds growth ratios, TnSeq (transposon sequencing) essentiality, and functional annotations for 5,852 ADP1 genes. [src: adp1_deletion_phenotypes] See adp1 sqlite database berdl tables db.

## Essentiality calls

The report treats knockout essentiality as a binary question: can the organism survive without this gene? It measures this by complete gene deletion and viable colony formation. [src: adp1_triple_essentiality]

- Rich media (LB): 2,953 genes, of which 346 are essential and 2,607 dispensable. [src: adp1_triple_essentiality]
- Minimal media: 3,092 genes, of which 499 are essential. [src: adp1_triple_essentiality]
- The minimal-media ground truth merges the two columns. It prioritizes `essentiality_minimal` and falls back to `essentiality_lb`, giving 3,092 genes with 499 essential. [src: adp1_triple_essentiality]

Details are in [[summaries/adp1_triple_essentiality__REPORT]].

## Growth on carbon sources

Growth ratios are mutant/wild-type ratios. Values below 1.0 indicate growth defects. Values above 1.0 indicate no defect, or a slight growth advantage from experimental normalization. [src: adp1_deletion_phenotypes] Mean growth ratio across conditions spans a 3.3-fold range, from 0.41 for urea to 1.36 for quinate. [src: adp1_deletion_phenotypes] The complete growth matrix has 2,034 genes with ratios on all 8 carbon sources. [src: adp1_deletion_phenotypes] See [[summaries/adp1_deletion_phenotypes__REPORT]] and condition specific gene importance across carbon sources.

## Coverage and limits

Of 2,593 TnSeq-dispensable genes, 272 (10.5%) lack deletion-collection growth data. The other 2,321 dispensable genes have data. [src: adp1_deletion_phenotypes] The report says the missing genes differ systematically from the present ones. [src: adp1_deletion_phenotypes] See [[concepts/coverage-gaps-in-deletion-collections-and-their-link-to-pangenome-conservation]].

The complete matrix excludes essential genes (499) and genes with incomplete data (316). This biases it toward dispensable genes whose deletion mutants were successfully made. [src: adp1_deletion_phenotypes]

Growth ratios are single-timepoint measurements with unknown technical noise. The condition-specificity analysis assumes that variation across conditions is biological, not measurement error. [src: adp1_deletion_phenotypes]

The report says its KBase Data Lakehouse-integrated analysis adds three insights not available from the original 2008 data. [src: adp1_deletion_phenotypes]
