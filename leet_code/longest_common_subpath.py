# 
# 1923. Longest Common Subpath
# 
# There is a country of n cities numbered from 0 to n - 1. In this country, there is a road connecting every pair of cities.
# There are m friends numbered from 0 to m - 1 who are traveling through the country. 
# Each one of them will take a path consisting of some cities. Each path is represented by an integer array that
# contains the visited cities in order. 
# The path may contain a city more than once, but the same city will not be listed consecutively.
# Given an integer n and a 2D integer array paths where paths[i] is an integer array representing the path of the ith friend,
# return the length of the longest common subpath that is shared by every friend's path, 
# or 0 if there is no common subpath at all.
# A subpath of a path is a contiguous sequence of cities within that path.
# 
# https://leetcode.com/problems/longest-common-subpath/
# 
from typing import List

class Node:
    
    def __init__(self, value=None, children=[], count=0):
        self.value = value
        self.children = children
        self.count = count

    def get(self, value):
        for child in self.children:
            if child.value == value:
                return child

    def __repr__(self):
        return f'value={value}, count={count}, children={children}'

def longestCommonSubpath(n: int, paths: List[List[int]]) -> int:
    longest_path = 0
    root = Node()
    for path in paths:
        i = 0
        path_len = len(path)
        while i < path_len:
            longest_path = recursively_add_values(root, path, i)
            i += 1
    
    return longest_path

def recursively_add_values(node, paths: List[List[int]], i):
    if i < len(paths)-1:
        if paths[i] in node.children:
            return recursively_add_values(node.get(paths[i]), paths, i+1)
        else:
            node.children.append(Node(paths[i]))
            return recursively_add_values(node.get(paths[i]), paths, i+1)
    elif paths[i] in node.children:
        for current_node in node.children:
            if current_node.value == paths[i]:
                current_node.count += 1
                return current_node.count
    else:
        return 0


n = 5
paths = [[0,1,2,3,4],
                       [2,3,4],
                       [4,0,1,2,3]]

print(longestCommonSubpath(n, paths))