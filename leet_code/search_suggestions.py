# 1268. Search Suggestions System
# 
# You are given an array of strings products and a string searchWord.
# 
# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
# 
# Return a list of lists of the suggested products after each character of searchWord is typed.
# 
# https://leetcode.com/problems/search-suggestions-system/
# 
from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

# Implement using a trie
def suggestions(strings: List[str], search_word) -> List[List[str]]:
    root = fill_trie(TrieNode())

    for i in range(len(search_word[:3])):
        current_prefix = search_word[:i]
        node = get_node(root, current_prefix)


def get_suggestions(node, visited):
    if node in visited:
        return

    for child in node.children:
        

def get_node(root, prefix):
    node = root
    for c in prefix:
        if c in node.children:
            node = node.children[c]
        else:
            return None
    return node

def fill_trie(root: TrieNode, strings: List[str]):
    
    for s in strings:
        node = root         
        for c in s:
            if c in node.children:
                node = node.children[c]
            else:
                child = TrieNode()
                node.children[c] = child
                node = child

        node.isWord = True

    return root

