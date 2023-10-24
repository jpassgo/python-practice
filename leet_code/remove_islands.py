def removeIslands(matrix):
    # 	key: (x, y), value: bool
    islandsToNotModify = {}

    x = 0
    y = 1
    while y < len(matrix[0]) - 1:
        # 		check if value is 1
        if matrix[x][y] == 1:
            # 		step into the interior and check if that value is 1
            if matrix[x + 1][y] == 1:
                # 		depth first search find all connected 1s and add them to our islandsToNotModify
                islandsToNotModify = depthFirstSearch(
                    islandsToNotModify, x + 1, y, matrix
                )
        y += 1

    x = 1
    y = 0
    while x < len(matrix) - 1:
        # 		check if value is 1
        if matrix[x][y] == 1:
            # 		step into the interior and check if that value is 1
            if matrix[x][y + 1] == 1:
                # 		depth first search find all connected 1s and add them to our islandsToNotModify
                islandsToNotModify = depthFirstSearch(
                    islandsToNotModify, x, y + 1, matrix
                )
        x += 1

    x = len(matrix) - 1
    y = 1
    while y < len(matrix[0]) - 1:
        # 		check if value is 1
        if matrix[x][y] == 1:
            # 		step into the interior and check if that value is 1
            if matrix[x - 1][y] == 1:
                # 		depth first search find all connected 1s and add them to our islandsToNotModify
                islandsToNotModify = depthFirstSearch(
                    islandsToNotModify, x - 1, y, matrix
                )
        y += 1

    x = 1
    y = len(matrix[0]) - 1
    while x < len(matrix) - 1:
        # 		check if value is 1
        if matrix[x][y] == 1:
            # 		step into the interior and check if that value is 1
            if matrix[x][y - 1] == 1:
                # 		depth first search find all connected 1s and add them to our islandsToNotModify
                islandsToNotModify = depthFirstSearch(
                    islandsToNotModify, x, y - 1, matrix
                )
        x += 1

    for x in range(1, len(matrix) - 1):
        for y in range(1, len(matrix[x]) - 1):
            if matrix[x][y] == 1 and (x, y) not in islandsToNotModify.keys():
                matrix[x][y] == 0

    return matrix


def depthFirstSearch(islandsToNotModify, x, y, matrix):
    islandsToNotModify[(x, y)] = True
    if (
        x > 1
        and matrix[x - 1][y] == 1
        and not islandExistsInMap(islandsToNotModify, x - 1, y)
    ):
        return depthFirstSearch(islandsToNotModify, x - 1, y, matrix)
    elif (
        x < len(matrix) - 1
        and matrix[x + 1][y] == 1
        and not islandExistsInMap(islandsToNotModify, x + 1, y)
    ):
        return depthFirstSearch(islandsToNotModify, x + 1, y, matrix)
    elif (
        y > 1
        and matrix[x][y - 1] == 1
        and not islandExistsInMap(islandsToNotModify, x, y - 1)
    ):
        return depthFirstSearch(islandsToNotModify, x, y - 1, matrix)
    elif (
        y < len(matrix[x]) - 1
        and matrix[x][y + 1] == 1
        and not islandExistsInMap(islandsToNotModify, x, y + 1)
    ):
        return depthFirstSearch(islandsToNotModify, x, y + 1, matrix)
    else:
        return islandsToNotModify


def islandExistsInMap(islandsToNotModify, x, y):
    return (x, y) in islandsToNotModify.keys()
