from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ship_count = 0
        i, j = 0, 0
        rows = len(board)-1
        cols = len(board[0])-1
        visited = []
        while i <= rows:
            j = 0
            while j <= cols:                
                if f'{i}{j}' not in visited and board[i][j] == 'X':
                       
                    if i == 2 and j == 0:
                        print(f'{i}{j}')  
                    ship_count += 1
                    
                    visited = self.dfs(board, i, j, rows, cols, visited)                    
                
                j += 1                
            i+=1                        
            
        return ship_count
    
    
    
    def dfs(self, board, i, j, rows, cols, visited):
        visited.append(f'{i}{j}')
        
        if i < rows and board[i+1][j] == 'X':
            return self.dfs(board, i+1, j, rows, cols, visited)
        elif j < cols and board[i][j+1] == 'X':
            return self.dfs(board, i, j+1, rows, cols, visited)
        return visited


solution = Solution()
battleship_count = solution.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
print(battleship_count)
assert battleship_count == 2