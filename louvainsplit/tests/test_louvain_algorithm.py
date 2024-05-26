import unittest
import networkx as nx
from louvainsplit import construct_feature_pyramid, louvain_algorithm

class TestLouvainAlgorithm(unittest.TestCase):

    def test_louvain_algorithm(self):
        G = nx.karate_club_graph()
        feature_pyramid = construct_feature_pyramid(G, num_levels=3)
        partitions = louvain_algorithm(feature_pyramid, num_clusters=3)
        self.assertEqual(len(partitions), 3)
        self.assertTrue(all(isinstance(part, list) for part in partitions))

if __name__ == '__main__':
    unittest.main()
