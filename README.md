# LouvainSplit

LouvainSplit is a Python package for efficient graph partitioning using the LouvainSplit algorithm, based on the paper by Mehrdad Javadi.

## Abstract

Graph partitioning is essential for uncovering cohesive communities within complex networks. This paper introduces LouvainSplit, an innovative algorithm designed to enhance graph partitioning efficiency and accuracy. LouvainSplit leverages advanced techniques in feature representation, community detection, and evaluation, providing a robust framework for addressing challenges inherent in graph partitioning tasks across diverse domains. At its core, LouvainSplit utilizes a feature pyramid representation approach to extract both basic and summary features from input graphs at multiple granularity levels. This methodology ensures a subtle evaluation of graph data by capturing fundamental graph information alongside intricate structural patterns, thus offering a comprehensive representation of underlying community structures. A key innovation of our approach is the integration of the Louvain algorithm, renowned for its efficacy in community detection. By leveraging pairwise cosine similarities computed from node feature vectors, the Louvain algorithm optimizes modularity iteratively, effectively partitioning graphs into cohesive communities. This iterative process facilitates the identification of significant network structures within complex networks, providing valuable insights into their organizational dynamics. To comprehensively evaluate LouvainSplit's performance, we integrated diverse graph partitioning algorithms, including PyMetis, Genetic Algorithm (GA), DBSCAN, KMeans, OPTICS, and spectral clustering to evaluate the effectiveness of LouvainSplit and using popular evaluation metrics across diverse benchmarks spanning various domains and graphs. The results demonstrate LouvainSplit's superiority in terms of recall score, modularity, and scalability compared to existing methods. Moreover, LouvainSplit maintains competitive average runtime values, ensuring efficient processing even with large-scale datasets.

DOI: [10.21203/rs.3.rs-4301602/v1](https://doi.org/10.21203/rs.3.rs-4301602/v1)

## Installation

You can install the package via pip:

```sh
pip install louvainsplit
