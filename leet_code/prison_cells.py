# 
# 957. Prison Cells After N Days
# 
# There are 8 prison cells in a row and each cell is either occupied or vacant.
# Each day, whether the cell is occupied or vacant changes according to the following rules:
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note: that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.
# You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell 
# is vacant, and you are given an integer n. Return the state of the prison after n days (i.e., n such changes described above).
# 
# https://leetcode.com/problems/prison-cells-after-n-days/
# 
from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:        
        for i in range(n):            
            temp_cells = [0] * 8
            for i in range(0, 7):
                left_index = i - 1
                right_index = i + 1
                left_value = 0
                right_value = 0
                if left_index < 0:
                    temp_cells[0] = 0
                elif right_index > 7:
                    temp_cells[7] = 0
                else:
                    left_value = cells[left_index]
                    right_value = cells[right_index]

                    if (left_value == 0 and right_value == 0) or (left_value == 1 and right_value == 1):
                        temp_cells[i] = 1
                    else:
                        temp_cells[i] = 0
                                                                                        
            cells = temp_cells

        return cells


                    

            
cells = [0,1,0,1,1,0,0,1]

solution = Solution()
assert solution.prisonAfterNDays(cells, 7) == [0, 0, 1, 1, 0, 0, 0, 0]

try:
    assert solution.prisonAfterNDays(cells, 7) == [0, 0, 1, 1, 0, 0, 0, 1]
except AssertionError:
    print(f'AssertionError when comparing against incorrect value')

