import unittest
from datastructures.disjoint_set import DisjointSet


class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        self.disjoint_set = DisjointSet(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_find(self):
        self.disjoint_set.forest = [-1, -1, -1, -1, -4, 4, 4, 6]

        self.assertEqual(self.disjoint_set.find('f'), self.disjoint_set.find('h'))
        self.assertNotEqual(self.disjoint_set.find('c'), self.disjoint_set.find('g'))

    def test_path_compression(self):
        disjoint_set = DisjointSet(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
        disjoint_set.forest = [-16, 0, 0, 2, 0, 4, 4, 6, 0, 8, 8, 10, 8, 12, 12, 14]

        disjoint_set.find('o')
        self.assertListEqual([-16, 0, 0, 2, 0, 4, 4, 6, 0, 8, 8, 10, 0, 12, 0, 14], disjoint_set.forest)

    def test_union(self):
        self.disjoint_set.forest = [-1, -1, -1, -1, -4, 4, 4, 6]
        self.disjoint_set.union('d', 'e')

        self.assertEqual(self.disjoint_set.find('d'), self.disjoint_set.find('e'))

    def test_union_by_size(self):
        self.disjoint_set.forest = [-1, -1, -1, -1, -4, 4, 4, 6]
        self.disjoint_set.union('d', 'g')

        self.assertListEqual([-1, -1, -1, 4, -5, 4, 4, 6], self.disjoint_set.forest)

        # attempt to merge two elements in the same set
        self.disjoint_set.union('f', 'g')
        self.assertListEqual([-1, -1, -1, 4, -5, 4, 4, 6], self.disjoint_set.forest)

        # merge two sets of equal size
        self.disjoint_set.union('a', 'c')
        self.assertTrue(self.disjoint_set.forest in [[-2, -1, 0, 4, -5, 4, 4, 6], [2, -1, -2, 4, -5, 4, 4, 6]])

    def test_count(self):
        self.disjoint_set.forest = [-1, -1, -1, -1, -4, 4, 4, 6]
        self.assertEqual(5, self.disjoint_set.count())


if __name__ == '__main__':
    unittest.main()
