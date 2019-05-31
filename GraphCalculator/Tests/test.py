import unittest
import numpy as np
import GraphCalculator.GraphCalculator as tmp
import networkx as nx


class TestStringMethods(unittest.TestCase):

    def test_dfs1(self):
        sample = tmp.SampleApp()
        page = tmp.PageOne(sample, sample)
        matrix = np.matrix([[1, 0], [0, 1]])
        G = nx.from_numpy_matrix(matrix)
        matrix = nx.to_numpy_matrix(nx.dfs_tree(G))

        page.use_method(matrix)
        matrix2 = nx.to_numpy_matrix(page.result)
        g1 = []
        g2 = []

        matrix = np.array(matrix)
        g1.append(matrix.shape[0])
        g1.append(matrix.shape[1])
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                g1.append(matrix[i][j])

        matrix2 = np.array(matrix2)
        g2.append(matrix2.shape[0])
        g2.append(matrix2.shape[1])
        for i in range(0, matrix2.shape[0]):
            for j in range(0, matrix2.shape[1]):
                g2.append(matrix2[i][j])

        self.assertEqual(g1, g2)

    def test_dfs2(self):
        sample = tmp.SampleApp()
        page = tmp.PageOne(sample, sample)
        matrix = np.matrix([[0, 0], [0, 0]])
        G = nx.from_numpy_matrix(matrix)
        matrix = nx.to_numpy_matrix(nx.dfs_tree(G))

        page.use_method(matrix)
        matrix2 = nx.to_numpy_matrix(page.result)
        g1 = []
        g2 = []

        matrix = np.array(matrix)
        g1.append(matrix.shape[0])
        g1.append(matrix.shape[1])
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                g1.append(matrix[i][j])

        matrix2 = np.array(matrix2)
        g2.append(matrix2.shape[0])
        g2.append(matrix2.shape[1])
        for i in range(0, matrix2.shape[0]):
            for j in range(0, matrix2.shape[1]):
                g2.append(matrix2[i][j])

        self.assertEqual(g1, g2)

    def test_dfs3(self):
        sample = tmp.SampleApp()
        page = tmp.PageOne(sample, sample)
        matrix = np.matrix([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]])
        G = nx.from_numpy_matrix(matrix)
        matrix = nx.to_numpy_matrix(nx.dfs_tree(G))

        page.use_method(matrix)
        matrix2 = nx.to_numpy_matrix(page.result)
        g1 = []
        g2 = []

        matrix = np.array(matrix)
        g1.append(matrix.shape[0])
        g1.append(matrix.shape[1])
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                g1.append(matrix[i][j])

        matrix2 = np.array(matrix2)
        g2.append(matrix2.shape[0])
        g2.append(matrix2.shape[1])
        for i in range(0, matrix2.shape[0]):
            for j in range(0, matrix2.shape[1]):
                g2.append(matrix2[i][j])

        self.assertEqual(g1, g2)

    def test_bfs1(self):
        sample = tmp.SampleApp()
        page = tmp.PageTwo(sample, sample)
        matrix = np.matrix([[0, 0], [0, 0]])
        G = nx.from_numpy_matrix(matrix)
        matrix = nx.to_numpy_matrix(nx.bfs_tree(G, 0))

        page.use_method(matrix)
        matrix2 = nx.to_numpy_matrix(page.result)
        g1 = []
        g2 = []

        matrix = np.array(matrix)
        g1.append(matrix.shape[0])
        g1.append(matrix.shape[1])
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                g1.append(matrix[i][j])

        matrix2 = np.array(matrix2)
        g2.append(matrix2.shape[0])
        g2.append(matrix2.shape[1])
        for i in range(0, matrix2.shape[0]):
            for j in range(0, matrix2.shape[1]):
                g2.append(matrix2[i][j])

        self.assertEqual(g1, g2)

    def test_bfs2(self):
        sample = tmp.SampleApp()
        page = tmp.PageTwo(sample, sample)
        matrix = np.matrix([[1, 0], [0, 1]])
        G = nx.from_numpy_matrix(matrix)
        matrix = nx.to_numpy_matrix(nx.bfs_tree(G, 0))

        page.use_method(matrix)
        matrix2 = nx.to_numpy_matrix(page.result)
        g1 = []
        g2 = []

        matrix = np.array(matrix)
        g1.append(matrix.shape[0])
        g1.append(matrix.shape[1])
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                g1.append(matrix[i][j])

        matrix2 = np.array(matrix2)
        g2.append(matrix2.shape[0])
        g2.append(matrix2.shape[1])
        for i in range(0, matrix2.shape[0]):
            for j in range(0, matrix2.shape[1]):
                g2.append(matrix2[i][j])

        self.assertEqual(g1, g2)

    def test_bfs3(self):
        sample = tmp.SampleApp()
        page = tmp.PageTwo(sample, sample)
        matrix = np.matrix([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]])
        G = nx.from_numpy_matrix(matrix)
        matrix = nx.to_numpy_matrix(nx.bfs_tree(G, 0))

        page.use_method(matrix)
        matrix2 = nx.to_numpy_matrix(page.result)
        g1 = []
        g2 = []

        matrix = np.array(matrix)
        g1.append(matrix.shape[0])
        g1.append(matrix.shape[1])
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                g1.append(matrix[i][j])

        matrix2 = np.array(matrix2)
        g2.append(matrix2.shape[0])
        g2.append(matrix2.shape[1])
        for i in range(0, matrix2.shape[0]):
            for j in range(0, matrix2.shape[1]):
                g2.append(matrix2[i][j])

        self.assertEqual(g1, g2)


if __name__ == '__main__':
    unittest.main()
