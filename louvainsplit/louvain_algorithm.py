import torch
import networkx as nx
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import community.community_louvain as community_louvain

def louvain_algorithm(feature_pyramid, num_clusters, similarity_measure='cosine'):
    if similarity_measure == 'cosine':
        feature_matrix = torch.cat(feature_pyramid, dim=1).detach().numpy()
        similarities = cosine_similarity(feature_matrix.T)
    else:
        raise ValueError("Invalid similarity_measure. Choose 'cosine'.")

    G = nx.from_numpy_array(similarities)
    partition = community_louvain.best_partition(G, resolution=1.0)
    partitions = [[] for _ in range(num_clusters)]

    for node, cluster_id in partition.items():
        partitions[cluster_id % num_clusters].append(node)

    return partitions
