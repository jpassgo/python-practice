from typing import List

class Solution:
    
    def countBattleships(self, board: List[List]) -> int: 
        rows = len(board) - 1
        columns = len(board[0]) - 1

        number_of_ships = 0

        x = 0
        y = 0

        # iterate through board until we find an X, then do DFS to find the rest of the ship
        while x <= rows:
             while y <= columns:
                if board[x][y] == 'X':
                    number_of_ships += 1
                    # perform dfs
                    board = self.dfs(board, x, y, rows, columns)
                y += 1
             x += 1

        return number_of_ships


    def dfs(self, board, x, y, rows, columns) -> List[List]:
        if x < rows and y < columns:
            board[x][y] = '.'
            # do recursive checks
            if board[x+1][y] == 'X':
                self.dfs(board, x+1, y, rows, columns)
            elif board[x][y+1] == 'X':
                self.dfs(board, x, y+1, rows, columns)
            else:
                return board    
        else:
            return board


solution = Solution()
battleship_count = solution.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
print(battleship_count)
assert battleship_count == 2