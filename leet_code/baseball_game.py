#
# 682. Baseball Game
#
# You are keeping score for a baseball game with strange rules. The game consists of several rounds,
# where the scores of past rounds may affect future rounds' scores.
# At the beginning of the game, you start with an empty record.
# You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is
# one of the following:
# An integer x - Record a new score of x.
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
# Return the sum of all the scores on the record.
#
# https://leetcode.com/problems/baseball-game/
#


def score_baseball_game(ops) -> int:
    sum_of_scores = 0
    scores = []
    i = 0
    ops_len = len(ops)

    while i < ops_len:
        op = ops[i]

        scores_len = len(scores) - 1
        if op == "+":
            score = int(scores[scores_len]) + int(scores[scores_len - 1])
            scores.append(score)
            sum_of_scores += score
        elif op == "D":
            score = int(scores[scores_len]) * 2
            scores.append(score)
            sum_of_scores += score
        elif op == "C":
            score = int(scores[scores_len])
            scores.pop()
            sum_of_scores -= score
        else:
            score = int(op)
            scores.append(score)
            sum_of_scores += score
        i += 1

    return sum_of_scores


ops = ["5", "2", "C", "D", "+"]
ops2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(score_baseball_game(ops))
print(score_baseball_game(ops2))
