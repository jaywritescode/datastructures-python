class DisjointSet:
    def __init__(self, values):
        self.indices = {v: k for k, v in enumerate(values)}
        self.forest = [-1] * len(values)

    def find(self, value):
        """
        Returns the set that value is found in.

        Note that the actual return value is irrelevant. What matters is that find(a) == find(b) if and only if a ~ b.

        :param value: the value we're looking for
        :return: the label of the set that value is in
        """
        if value not in self.indices:
            raise KeyError
        return self._find(self.indices[value])

    def union(self, value1, value2):
        """
        Performs on a union the set(s) that the two given values are in.

        :param value1: a value
        :param value2: another value
        :return: None
        """
        return self._union_by_size(self.find(value1), self.find(value2))

    def count(self):
        """
        Counts the number of sets in the data structure.
        :return: the number of sets in the data structure
        """
        return len(list(filter(lambda x: x < 0, self.forest)))

    def _find(self, index):
        if self.forest[index] < 0:
            return index
        else:
            self.forest[index] = self._find(self.forest[index])
            return self.forest[index]

    def _union_by_size(self, root1, root2):
        if root1 == root2:
            return

        # make the tree with fewer nodes a child of the tree with more nodes
        if self.forest[root2] < self.forest[root1]:
            self.forest[root2] += self.forest[root1]
            self.forest[root1] = root2
        else:
            self.forest[root1] += self.forest[root2]
            self.forest[root2] = root1