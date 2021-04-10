class BinaryIndexTree:
    """
    A binary index tree (BIT), a.k.a. Fenwick tree.

    BITs are used to solve the following problem efficiently:
        Given an array of integers of length n, find the sum of the values from indices 0 to i, where 0 <= i < n.

    Note that "sum" can be replaced by any associative binary operation, but that's not currently implemented.
    """
    def __init__(self, array):
        """
        Constructor.

        :param array: the initial array, Note that this array is zero-indexed.
        """
        self.length = len(array)
        self.tree = self._construct(array)

    def _construct(self, array):
        self.tree = [None]
        self.tree.extend([0] * len(array))

        for index, value in enumerate(array):
            self.update(index + 1, value)
        return self.tree

    def update(self, index, value):
        """
        Increments the value at the given index in the BIT. Note that the BIT is one-indexed.

        :param index: the index we're updating
        :param value: the amount we're incrementing by
        :return: None
        """
        if index <= 0:
            raise IndexError

        while index <= self.length:
            self.tree[index] += value
            index += BinaryIndexTree.least_significant_bit(index)

    def query(self, n):
        """
        Calculates the sum of the first n entries in the array.

        :param n: the number of entries to collect
        :return: the sum of the first n entries
        """
        value = 0
        while n > 0:
            value += self.tree[n]
            n -= BinaryIndexTree.least_significant_bit(n)
        return value

    @staticmethod
    def least_significant_bit(x):
        return x & (-x)