
class TrieNode:

    def __init__(self):
        self.children = {}
        self.isCompleteWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root

        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                node.children[letter] = TrieNode()
                node = node.children[letter]

        if not node.isCompleteWord:
            node.isCompleteWord = True


    def is_word_present(self, word) -> bool:
        node = self.root

        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False

        return node.isCompleteWord


trie = Trie()

trie.add_word('hello')

assert trie.is_word_present('hello') == True
assert trie.is_word_present('hel') == False