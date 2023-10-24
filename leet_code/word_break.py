#
# 139. Word Break
#
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
# space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
# https://leetcode.com/problems/word-break/
#
from typing import List


# The solution for this should be to use a trie
def wordBreak(s: str, wordDict: List[str]) -> bool:
    trie = {"root": {}}
    for word in wordDict:
        node = trie["root"]
        for character in word:
            if character in node.keys():
                break
            else:
                node[character] = {}
            node = node[character]

    node = trie["root"]
    i = 0
    s_len = len(s)
    while i < s_len:
        if s[i] in node.keys():
            node = node[s[i]]
            s = s.replace(s[i], "", 1)
            s_len = len(s)
        elif len(node.keys()) == 0:
            node = trie["root"]
        else:
            return False

    return True


print(wordBreak("leetcode", ["leet", "code"]))

print(wordBreak("applepenapple", ["apple", "pen"]))

print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
