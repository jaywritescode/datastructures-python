class Trie:
    def __init__(self):
        self.root = Trie.Node()

    def add(self, word, **kwargs):
        """
        Adds a word to the tree, with an optional data payload.

        Calling this method with a word that is already in the trie will update its data payload.

        :param word: the word
        :param kwargs: data to be stored alongside the node
        :return: None
        """
        current_node = self.root
        for char in word:
            current_node = current_node.get_child(char)

        current_node.payload = kwargs or dict()

    def get(self, word, default=None):
        """
        Gets the data payload associated with a word in the trie.

        :param word: the word
        :param default: the value to return if the word is not in the tree, defaults to None
        :return: the data payload associated with the word, or default
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return default
            current_node = current_node.children[char]

        return current_node.payload if current_node.is_word_terminus() else default

    def search(self, prefix=''):
        """
        Searches for all words in the trie that begin with the given prefix.

        :param prefix: the prefix
        :return: the words matching the prefix and their data payloads
        """
        results = dict()

        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return results
            current_node = current_node.children[char]

        stack = [(prefix, current_node)]
        while stack:
            _prefix, _node = stack.pop()

            # _node.is_word_terminus() == True ==> _node.payload is not None
            if _node.is_word_terminus():
                results[_prefix] = _node.payload

            for char in _node.children.keys():
                stack.append((_prefix + char, _node.children[char]))

        return results

    def __contains__(self, item):
        return self.get(item) is not None

    class Node:
        def __init__(self):
            self.children = dict()
            self.payload = None

        def get_child(self, char):
            if char not in self.children:
                self.children[char] = Trie.Node()
            return self.children[char]

        def is_word_terminus(self):
            return self.payload is not None


if __name__ == '__main__':
    t = Trie()
    t.add('their', weight=25)
    t.add('their', weight=30)
    t.add('there')

    print('the' in t)
    print('their' in t)
    print('there' in t)

