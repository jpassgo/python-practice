# using an adjacency list to represent the graph


def dfs(graph, node=0):
    visited = set()

    recursive_bfs(graph, visited, node)


def recursive_dfs(graph, visited, node):
    print(node)

    visited.add(node)

    for v in graph[node]:
        if v not in visited:
            recursive_dfs(graph, visited, v)


dfs([[1, 2], [0, 2, 4], [0, 1, 3], [2], [1]])
