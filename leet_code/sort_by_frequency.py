# 
# 451. Sort Characters By Frequency
# 
# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.
# 
# https://leetcode.com/problems/sort-characters-by-frequency/
# 

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_map = {}

        for