from typing import List

from collections import deque


def bfs(graph: List[List[int]], s: int = 0):
    # Set for keeping track of visited nodes
    visited = set()

    queue = deque()

    visited.add(s)
    queue.appendleft(s)

    while queue:
        current_node = queue.pop()
        print(current_node)

        for node in graph[current_node]:
            if node not in visited:
                visited.add(node)
                queue.appendleft(node)


graph = [[1, 2], [0, 2, 4], [0, 1, 3], [2], [1]]
bfs(graph)
