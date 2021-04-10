import unittest
from datastructures.segment_tree import SegmentTree


class TestSegmentTree(unittest.TestCase):
    def test_query(self):
        array = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]

        segmentTree = SegmentTree(array, lambda x, y: x + y)
        self.assertEqual(segmentTree.query(2, 8), sum(array[2:9]))

    def test_update(self):
        array = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]

        segmentTree = SegmentTree(array, lambda x, y: x + y)
        segmentTree.update(1, array[1] + 3)
        segmentTree.update(3, array[3] - 1)
        segmentTree.update(6, array[6] + 2)
        self.assertEqual(segmentTree.query(0, 9), sum(array) + 4)


if __name__ == '__main__':
    unittest.main()
