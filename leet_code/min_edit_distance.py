# 
# 72. Edit Distance
# 
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
# 
# https://leetcode.com/problems/edit-distance/
# 

def minDistance(word1: str, word2: str) -> int:
    min_edit_count = 0
    word1_list = list(word1)
    word2_list = list(word2)
    word1_len = len(word1)
    i = 0
    while i < word1_len:
        if 



minDistance('hello', 'goodbye')