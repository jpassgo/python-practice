#
# Using a trie
#


class TrieNode:
    def __init__(self, is_word=False):
        self.children = {}
        self.is_word = is_word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        self.recursive_insert(0, word, self.root)

    def recursive_insert(self, index, word, node):
        if index == len(word) - 1:
            if len(node.children) > 0 and word[index] in node.children:
                if node.children[word[index]].is_word:
                    return
                else:
                    node.children[word[index]].is_word = True
                    return
            else:
                node.children[word[index]] = TrieNode(True)
                return

        if word[index] in node.children:
            return self.recursive_insert(index + 1, word, node.children[word[index]])

        else:
            node.children[word[index]] = TrieNode()
            return self.recursive_insert(index + 1, word, node.children[word[index]])

    def is_word_present(self, word):
        node = self.root
        for character in word:
            if character in node.children:
                node = node.children[character]

        return node.is_word


trie = Trie()
trie.insert("helllo")
print(trie.is_word_present("helllo"))
print(trie.is_word_present("hello"))
