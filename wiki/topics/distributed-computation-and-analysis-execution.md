---
type: "Topic"
description: "This topic covers how analyses actually run against the KBase Data Lakehouse: Spark (the distributed query engine behind the Lakehouse), the pandas frames and notebooks where results are examined, and the sessions, credentials and access paths between them."
sources: []
---
# Distributed Computation and Analysis Execution

This topic covers how analyses actually run against the KBase Data Lakehouse: Spark (the distributed query engine behind the Lakehouse), the pandas frames and notebooks where results are examined, and the sessions, credentials and access paths between them.

No overview of this topic has passed review. Its concept pages follow.

## Literature Context

The candidate papers are bioinformatics applications and tooling built on Apache Spark and Hadoop. None of them concerns lakehouse catalogs, notebook sessions or Spark-to-pandas handoffs directly. Together they show that distributed frameworks are widely adopted for large biological data, and that the frameworks need careful engineering to work well.

Several papers present Spark as a scalable engine for large data. One describes an in-memory, RDD-based (resilient distributed dataset) model for big data anonymization. Its abstract says Spark is 100 times faster than Hadoop, a claim it makes without a comparison we can check here [PMID 37115783](https://pubmed.ncbi.nlm.nih.gov/37115783/). Others apply Spark to single-cell transcriptomics with the scSPARKL framework [PMID 40731055](https://pubmed.ncbi.nlm.nih.gov/40731055/), to fMRI analytics on Hadoop and Spark [PMID 31240237](https://pubmed.ncbi.nlm.nih.gov/31240237/), and to molecular interaction networks with the DIAMIN library [PMID 36368948](https://pubmed.ncbi.nlm.nih.gov/36368948/). PyBDA runs Spark behind a command-line tool and schedules jobs with Snakemake. The authors demonstrate it on image-based RNA interference data from 150 million single cells [PMID 31718539](https://pubmed.ncbi.nlm.nih.gov/31718539/). CloudDOE addresses the operational side, packaging Hadoop cloud deployment behind a graphical interface for people without cluster expertise [PMID 24897343](https://pubmed.ncbi.nlm.nih.gov/24897343/).

Two papers bear more directly on scale limits. The FastKmer study finds that Hadoop or Spark is productive for large sequence collections only when the framework's architectural details are considered in the algorithm design. It also reports that data skew has to be balanced across nodes to use the cluster fully [PMID 30999863](https://pubmed.ncbi.nlm.nih.gov/30999863/). The BIndex paper makes a related point for genomic range joins. Quadratic complexity limits existing algorithms, and its bin-based indexing with balanced partitioning gives up to 4.65x speedup in Spark add-in modules over the previously best tool [PMID 37022216](https://pubmed.ncbi.nlm.nih.gov/37022216/). Both are results from the authors' own benchmarks.

The corpus's own findings are the driver result-size caps, join and explode blow-ups, session timeouts, unpartitioned billion-row scans and type surprises when moving data between Spark and pandas. These are consistent with the literature's general message that Spark performance depends on partitioning, skew and join design. The join and explode blow-ups and the unpartitioned scans fit most closely with the FastKmer and BIndex findings. The corpus's findings extend that literature in two ways. They are about operating Spark through notebooks and Spark Connect sessions, and they cover credentials and metadata-versus-data access in a catalog. The candidate papers do not address either of these, so those parts of the corpus are novel relative to this evidence. No candidate paper contradicts the corpus. The papers are algorithm and tool reports, so they cannot confirm session or access behaviour in the KBase Data Lakehouse.

## What the Corpus Shows

- [[concepts/metadata-introspection-versus-data-read-access-in-spark-based-catalogs|Metadata introspection versus data-read access in Spark-based catalogs]]: Covers how Iceberg metadata queries, namespace aliases and permission surfaces behave when auditing lakehouse databases; stops at this access pattern.
- [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses|Spark query scale limits and notebook-session constraints in Lakehouse analyses]]: Covers driver result-size caps, join and explode blow-ups, kernel and Spark Connect session timeouts, unpartitioned billion-row scans and string/decimal/numpy type surprises when moving data between Spark and pandas, with workarounds; stops at schema-specific gotchas and at catalog metadata access.

## Tensions and Caveats

Each concept page above states the tensions and caveats of its own evidence.

## Where to Go Deeper

- [[summaries/cofitness_coinheritance__REPORT]]
- [[summaries/discoveries]]
- [[summaries/ecotype_functional_differentiation__REPORT]]
- [[summaries/euk_in_prok_correlates__REPORT]]
- [[summaries/functional_dark_matter__REPORT]]
- [[summaries/gc_ecotype_ecology__REPORT]]
- [[summaries/gene_function_ecological_agora__REPORT]]
- [[summaries/nmdc_context_audit__REPORT]]
- [[summaries/pitfalls]]
