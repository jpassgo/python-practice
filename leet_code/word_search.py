# 
# 79. Word Search
# 
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or 
# vertically neighboring. The same letter cell may not be used more than once.
# 
# https://leetcode.com/problems/word-search/
# 

from typing import List

# class Solution:
def exist(board: List[List[str]], word: str) -> bool:
    coordinates = []
    char_index = 0
    word_len = len(word) - 1
    x_bounds = len(board) - 1
    y_bounds = len(board[0]) - 1
    x = 0
    y = 0
    while char_index < word_len:  
        while x <= x_bounds and y <= y_bounds:            
            if board[x][y] == word[char_index]:
                coordinates.append((x, y))
                break
            if board[x+1][y] == word[char_index]:
                coordinates.append((x+1, y))
                x+=1
                break
            elif board[x][y+1] == word[char_index]:
                coordinates.append((x, y+1))
                y+=1
                break

            if len(coordinates) == (word_len + 1):
                return True

            if y == y_bounds:
                x += 1
                y = 0
            else:
                y += 1

    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "SEE"


print(exist(board, word))