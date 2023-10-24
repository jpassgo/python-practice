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


def countBattleships(board: List[List[str]]) -> int:
    battleship_counter = 0
    temp_board = board

    row_count = len(board) - 1
    column_count = len(board[0]) - 1
    x, y = 0, 0
    while x <= row_count:
        while y <= column_count:
            if temp_board[x][y] == "X":
                temp_board = shipFound(temp_board, x, y, row_count, column_count)
                battleship_counter += 1
            y += 1
        x += 1

    return battleship_counter


def shipFound(temp_board, x, y, row_count, column_count) -> bool:
    temp_board[x][y] = "."
    if (
        x == row_count
        or y == column_count
        or temp_board[x + 1][y] == "."
        or temp_board[x][y + 1] == "."
    ):
        return temp_board
    elif temp_board[x + 1][y] == "X":
        return shipFound(temp_board, x + 1, y, row_count, column_count)
    elif temp_board[x][y + 1] == "X":
        return shipFound(temp_board, x + 1, y, row_count, column_count)


board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]

print(countBattleships(board))

board = [["."]]
print(countBattleships(board))
