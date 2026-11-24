---
type: "Method"
description: "Reusable function that compares two genome-KO matrices with per-KO Fisher's exact tests to assess cultivation bias."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md", "summaries/oak_ridge_cultivation_gap__REPORT.md"]
aliases: ["cultivation bias diagnostic"]
---
# cultivation_bias_diagnostic

The cultivation_bias_diagnostic is a reusable function that compares two genome-KO matrices with per-KO Fisher's exact tests to assess cultivation bias.

The function is defined in the oak_ridge_cultivation_gap project. [src: oak_ridge_cultivation_gap]

## Key facts

- The `cultivation_bias_diagnostic()` function lives in notebook 07_bias_diagnostic_module.ipynb of the oak_ridge_cultivation_gap project. [src: oak_ridge_cultivation_gap]
- The report states that it can be applied to any two genome-KO matrices, so other KBase Data Lakehouse projects can assess cultivation bias in their cohorts. [src: oak_ridge_cultivation_gap]
- Notebook 04_cultivation_coverage.ipynb in the same project provides per-KO Fisher's exact testing, a volcano plot, and marker analysis. [src: oak_ridge_cultivation_gap] See [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]] for the test.

## Separate marker-based statistic in the clay reports

Two other reports describe a different statistic that also targets cultivation bias. It uses marker prevalences and a binomial test, not per-KO Fisher tests. For a cohort of cultured clay-isolated genomes, it computes the prevalence of sulfate reduction (SR) markers (dsrAB-aprAB-sat) and iron reduction (IR) markers (omcS / mtrC / mtrA). It compares them with Mitzscherling rock-attached frequencies (SRB ~0.2%, IRB ~7%). [src: discoveries] The clay report presents this as a concrete, p-valued statistic for cultivation bias. It says the approach generalizes to future cohorts drawn from the KBase Data Lakehouse or similar cultured-pangenome resources. [src: clay_confined_subsurface] The reference data are described in [[entities/mitzscherling-et-al-2023-rock-attached-community-profile]].

## Proposed use

The oak_ridge_cultivation_gap report proposes applying the function to other KBase Data Lakehouse sites that have both cultured and metagenome assembled genomes (MAG) collections. The aim is to test whether the porewater-bias signature is universal across subsurface environments. [src: oak_ridge_cultivation_gap] This is a proposal, not a result. See [[concepts/porewater-bias-as-a-general-signature-of-cultivation-based-subsurface-collections]] and [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]].
