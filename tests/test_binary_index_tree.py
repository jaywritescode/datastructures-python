import unittest
from datastructures.binary_index_tree import BinaryIndexTree


class TestBinaryIndexTree(unittest.TestCase):
    def test_query(self):
        array = [1, 0, 2, 1, 1, 3, 0, 4, 2, 5, 2, 2, 3, 1, 0, 2]
        bit = BinaryIndexTree(array)

        self.assertEqual(bit.query(13), sum(array[:13]))

    def test_update(self):
        array = [1, 0, 2, 1, 1, 3, 0, 4, 2, 5, 2, 2, 3, 1, 0, 2]
        bit = BinaryIndexTree(array)

        bit.update(5, 1)
        self.assertEqual(bit.query(13), sum(array[:13]) + 1)
