# 
# 419. Battleships in a Board
# 
# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board. 
# Battleships can only be placed horizontally or vertically on board. 
# In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. 
# At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
# 
# https://leetcode.com/problems/battleships-in-a-board/
# 

from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # list of dicts of lists of dicts
        # where the key is the {row}x{column} (the starting coordinate) and the value is a list of coordinate pairs {row: column}
        global battle_ship_tracker
        battle_ship_tracker = {}
        # visited coordinates   
        global visited_coordinates
        visited_coordinates = []   

        for row in range(len(board)):   
            column = 0     
            while column < len(board[row]):
                coordinate = board[row][column]
                key = f'{row}x{column}'
                if coordinate == 'X':                    
                    battle_ship_tracker[key] = []
                    column = self.searchHorizontally(row, column)
                elif board[row+1][column] == 'X' and key not in visited_coordinates:
                    battle_ship_tracker[key] = []
                    self.searchVertically(row, column)

                

        return len(battle_ship_tracker)

                                    

    def searchHorizontally(self, row, column) -> int:                            
        battle_ship_tracker[f'{row}x{column}'].append({row: column})
        visited_coordinates.append(f'{row}x{column}')

        column += 1
        coordinate = self.coordinate(board, row, column)
        if coordinate == 'X':
            return self.searchHorizontally(row, column)
        else:
            return column

    def searchVertically(self, row, column) -> int:
        battle_ship_tracker[f'{row}x{column}'].append({row: column})

        row += 1
        coordinate = self.coordinate(board, row, column)
        if cooridinate == 'X':
            return self.searchVertically(row, column)
        else:
            return row

    def coordinate(self, board, row, column) -> int:
        return board[row][column] if column < len(board[row]) and row < len(board) else '.' 
        


board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

solution = Solution()

assert solution.countBattleships(board)