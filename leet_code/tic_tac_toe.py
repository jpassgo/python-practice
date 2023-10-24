# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
#
# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".
#
# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
#
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
#
from typing import List


def tictactoe(moves: List[List[int]]) -> str:
    player_a_moves = {
        "0row": 0,
        "1row": 0,
        "2row": 0,
        "0col": 0,
        "1col": 0,
        "2col": 0,
        "diag": 0,
    }
    player_b_moves = {
        "0row": 0,
        "1row": 0,
        "2row": 0,
        "0col": 0,
        "1col": 0,
        "2col": 0,
        "diag": 0,
    }

    for i in range(len(moves)):
        # for every even number i, if we encounter a coord startin with 0 then increment 0row and so on for player_a_moves
        if i % 2 == 0:
            player_a_moves[f"{moves[i][0]}col"] += 1
            player_a_moves[f"{moves[i][1]}row"] += 1
            if moves[i][0] == moves[i][1]:
                player_a_moves["diag"] += 1
            if (
                player_a_moves[f"{moves[i][0]}row"] == 3
                or player_a_moves[f"{moves[i][1]}col"] == 3
                or player_a_moves["diag"] == 3
            ):
                return "A"
        else:
            player_b_moves[f"{moves[i][0]}col"] += 1
            player_b_moves[f"{moves[i][1]}row"] += 1

            if moves[i][0] == moves[i][1]:
                player_b_moves["diag"] += 1

            if (
                player_b_moves[f"{moves[i][1]}row"] == 3
                or player_b_moves[f"{moves[i][0]}col"] == 3
                or player_b_moves["diag"] == 3
            ):
                return "B"

    return "Draw"


# print(tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))

# print(tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))

print(tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
