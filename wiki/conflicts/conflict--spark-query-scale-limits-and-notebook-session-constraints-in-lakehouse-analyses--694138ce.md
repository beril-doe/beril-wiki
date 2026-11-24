<!-- tension-hash: 694138cea824e289 -->
# Tension: Spark Broadcast Settings and Hints Across Lakehouse Analyses

Projects analysing data in the KBase Data Lakehouse give different reports on how Spark (a distributed query engine) behaves when joins use broadcasting, where a small table is copied to every worker. One tension concerns the setting autoBroadcastJoinThreshold = -1, which turns off automatic broadcasting. The other concerns explicit BROADCAST hints, which force broadcasting. This matters because notebook sessions are limited, and a recommended setting that hangs a notebook costs analysts time. The wider topic is in [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

## Evidence Sides

**Side A: disabling auto-broadcast helps (setting), or harms (setting)**

- The discoveries digest advises autoBroadcastJoinThreshold = -1 to avoid UniProt broadcast failures. [src: discoveries]
- The agora report found the same setting harmful, with a notebook hanging 17+ min. [src: gene_function_ecological_agora]
- The quotes do not say which join NB10 (a notebook) ran in the discoveries case, so neither result is shown to be a general rule.

**Side B: explicit BROADCAST hints and per-organism runtime**

- In Smeli profiling, explicit BROADCAST hints cut presence-matrix extraction to ~274s from ~300s per organism, only an 8% improvement. [src: pitfalls]
- Another project reported ~210s per organism with broadcast hints. [src: cofitness_coinheritance]
- The ~210s figure is an absolute runtime with no stated baseline or speedup. The two reports use different projects and setups, so the figures are not compared directly.

## Possible Reconciliations

- **Hypothesis 1: join-specific effects.** The -1 setting may help when a very large table such as UniProt would otherwise be broadcast, and hurt when a small table benefits from broadcasting. The quotes do not identify the joins, so this is untested.
- **Hypothesis 2: setup-specific runtimes.** The difference between ~274s and ~210s per organism may come from differences in project, data or query design rather than from the hints. No baseline is given for the ~210s project, so this is untested.

## Resolving Work

- **Data:** the NB10 UniProt join from the discoveries case and the agora notebook that hung. **Method:** recover the query plans and table sizes of each join. **Question:** did the two runs involve the same join, and which tables were broadcast?
- **Data:** one fixed join, such as UniProt, run in a clean session. **Method:** run it with autoBroadcastJoinThreshold = -1 and with the default, and record failures and hang time. **Question:** does the setting cause the 17+ min hang, or prevent the broadcast failures?
- **Data:** the Smeli presence-matrix extraction. **Method:** repeat it with and without BROADCAST hints in the same setup. **Question:** is the 8% improvement reproducible?
- **Data:** the cofitness_coinheritance extraction. **Method:** measure it without hints in the same setup as the ~210s run. **Question:** what is the baseline, so that a speedup can be stated for that project?
- **Data:** the same organism processed by both projects' code. **Method:** a controlled same-cluster measurement. **Question:** only after that can the ~274s and ~210s runtimes be compared.
