# 
# 73. Set Matrix Zeroes
# 
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
# You must do it in place.
# 
# 
# https://leetcode.com/problems/set-matrix-zeroes/
# 
from typing import List


# 
# [[1, 2, 3, 0],[1, 2, 1, 3],[1, 2, 3, 4],[1, 1, 2, 3, 4 ],[1, 2, 3, 4]]
# 0, 3
# 
# 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        columns = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)

        for i in range(m):  
            for j in range(n):          
                if i in rows:                
                    matrix[i][j] = 0
                if j in columns:
                    matrix[i][j] = 0            
                

def print_values(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):        
        for j in range(n):
            print(matrix[i][j], end='')
        print('')
                

solution = Solution()
matrix = [[1, 2, 3, 0],[1, 2, 1, 3],[1, 2, 3, 4],[1, 1, 2, 3, 4 ],[1, 2, 3, 4]]

print_values(matrix)

solution.setZeroes(matrix)

print('********************')

print_values(matrix)
