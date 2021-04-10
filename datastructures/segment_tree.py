class SegmentTree:
    def __init__(self, arr, operation):
        self.length = len(arr)
        self.operation = operation
        self.tree = self._construct(arr, 1, 0, self.length - 1)

    def _construct(self, array, vertex, left_boundary, right_boundary, tree=None):
        tree = tree or [None] * (4 * self.length)
        if left_boundary == right_boundary:
            tree[vertex] = array[left_boundary]
        else:
            midpoint = (left_boundary + right_boundary) // 2

            self._construct(array, vertex * 2, left_boundary, midpoint, tree)
            self._construct(array, vertex * 2 + 1, midpoint + 1, right_boundary, tree)

            tree[vertex] = self.operation(tree[vertex * 2], tree[vertex * 2 + 1])

        return tree

    def query(self, left_boundary, right_boundary):
        """
        Reduces a slice of the tree by repeatedly applying the tree's operation.

        :param left_boundary: the left boundary of the array slice, inclusive
        :param right_boundary: the right boundary of the array slice, inclusive
        :return: the result of applying the tree's operation to consecutive elements in the given array slice
        """
        if left_boundary < 0 or right_boundary >= self.length:
            raise IndexError
        return self._query(1, 0, self.length - 1, left_boundary, right_boundary)

    def _query(self, vertex, vertex_left_boundary, vertex_right_boundary, query_left_boundary, query_right_boundary):
        if vertex_left_boundary == query_left_boundary and vertex_right_boundary == query_right_boundary:
            return self.tree[vertex]

        midpoint = (vertex_left_boundary + vertex_right_boundary) // 2
        if query_right_boundary <= midpoint:
            return self._query(vertex * 2, vertex_left_boundary, midpoint, query_left_boundary, query_right_boundary)
        elif query_left_boundary > midpoint:
            return self._query(vertex * 2 + 1, midpoint + 1, vertex_right_boundary, query_left_boundary, query_right_boundary)
        else:
            left = self._query(vertex * 2, vertex_left_boundary, midpoint, query_left_boundary, midpoint)
            right = self._query(vertex * 2 + 1, midpoint + 1, vertex_right_boundary, midpoint + 1, query_right_boundary)
            return self.operation(left, right)

    def update(self, index, value):
        """
        Updates the segment tree by setting array[index] to value, where array is the underlying array.

        :param index: the index to update
        :param value: the new value
        :return: self
        """
        if index < 0 or index >= self.length:
            raise IndexError
        self._update(1, 0, self.length - 1, index, value)
        return self

    def _update(self, vertex, vertex_left_boundary, vertex_right_boundary, index, new_value):
        if vertex_left_boundary == index and vertex_right_boundary == index:
            self.tree[vertex] = new_value
            return

        midpoint = (vertex_left_boundary + vertex_right_boundary) // 2
        if index <= midpoint:
            self._update(vertex * 2, vertex_left_boundary, midpoint, index, new_value)
        else:
            self._update(vertex * 2 + 1, midpoint + 1, vertex_right_boundary, index, new_value)

        self.tree[vertex] = self.operation(self.tree[vertex * 2], self.tree[vertex * 2 + 1])


if __name__ == '__main__':
    s = SegmentTree([1, 3, -2, 8, -7], lambda x, y: x + y)
    print(s.query(2, 4))
    s.update(2, 3)
    print(s.query(0, 4))