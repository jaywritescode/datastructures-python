import unittest
from datastructures.trie import Trie


class TestTrie(unittest.TestCase):

    def test_insert__zero_length_prefix__no_data(self):
        trie = Trie()

        word = 'their'
        trie.add(word)

        self.assertIn(word, trie)

    def test_insert__zero_length_prefix__with_data(self):
        trie = Trie()

        word = 'their'
        payload = {'weight': 30}
        trie.add(word, **payload)

        self.assertIn(word, trie)
        self.assertDictEqual(trie.get(word), payload)

    def test_insert__non_zero_length_prefix__no_data(self):
        trie = Trie()
        trie.add('their')

        word = 'there'

        trie.add(word)
        self.assertIn(word, trie)

    def test_insert__non_zero_length_prefix__with_data(self):
        trie = Trie()
        trie.add('their')

        word = 'there'
        payload = {'weight': 30}

        trie.add(word, **payload)
        self.assertIn(word, trie)
        self.assertDictEqual(trie.get(word), payload)

    def test_insert__word_is_prefix_in_trie__no_data(self):
        trie = Trie()
        trie.add('their')

        word = 'the'
        trie.add(word)

        self.assertIn(word, trie)

    def test_insert__word_is_prefix_in_trie__with_data(self):
        trie = Trie()
        trie.add('their')

        word = 'the'
        payload = {'weight': 30}

        trie.add(word, **payload)
        self.assertIn(word, trie)
        self.assertDictEqual(trie.get(word), payload)

    def test_insert__word_is_already_in_trie__update_data(self):
        trie = Trie()
        trie.add('their', weight=25)

        word = 'their'
        payload = {'weight': 30}

        trie.add(word, **payload)
        self.assertDictEqual(trie.get(word), payload)

    def test_get__word_is_in_trie__no_data(self):
        trie = Trie()
        word = 'their'

        trie.add(word)
        self.assertDictEqual(trie.get(word), {})

    def test_get__word_is_in_trie__with_data(self):
        trie = Trie()
        word = 'their'
        payload = {'weight': 25}

        trie.add(word, **payload)
        self.assertDictEqual(trie.get(word), payload)

    def test_get__word_not_in_trie(self):
        trie = Trie()
        word = 'their'

        self.assertIsNone(trie.get(word))

    def test_search(self):
        words = ['the', 'their', 'there', 'a', 'any', 'answer', 'by', 'bye']

        trie = Trie()
        for word in words:
            trie.add(word)

        self.assertSetEqual({x for x in trie.search('the')}, {'the', 'their', 'there'})

    def test_contains(self):
        words = ['the', 'their', 'there', 'a', 'any', 'answer', 'by', 'bye']

        trie = Trie()
        for word in words:
            trie.add(word)

        self.assertIn('answer', trie)
        self.assertIn('any', trie)
        self.assertNotIn('anybody', trie)


if __name__ == '__main__':
    unittest.main()
