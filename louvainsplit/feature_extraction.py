import torch
import numpy as np
import networkx as nx

def construct_feature_pyramid(graph, num_levels):
    feature_pyramid = []

    level_0_features = extract_basic_features(graph)
    level_0_tensor = torch.tensor(level_0_features, dtype=torch.float32).unsqueeze(0)
    feature_pyramid.append(level_0_tensor)

    for level in range(1, num_levels):
        abstract_features = extract_abstract_features(graph, level)
        feature_pyramid.append(abstract_features.clone().detach())

    return feature_pyramid

def extract_basic_features(graph):
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    avg_degree = sum(dict(graph.degree()).values()) / num_nodes
    clustering_coefficient = nx.average_clustering(graph)

    return [num_nodes, num_edges, avg_degree, clustering_coefficient]

def extract_abstract_features(graph, level):
    node_degrees = list(dict(graph.degree()).values())
    node_degrees = [deg for deg in node_degrees if deg >= 0]
    if not node_degrees:
        return torch.zeros((1, 11), dtype=torch.float32)

    quantiles = np.percentile(node_degrees, np.arange(0, 101, 10))
    features = [np.percentile(node_degrees, q) for q in quantiles]
    features_tensor = torch.tensor(features, dtype=torch.float32).unsqueeze(0)

    return features_tensor
