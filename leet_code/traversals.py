#
# Just a place for various traversal implementations
#
#


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = Node(10, Node(7, Node(6), Node(8)), Node(13, Node(11), Node(15)))


def depth_first_search(value, node):
    if node is None:
        return

    print(node.value)
    depth_first_search(value, node.left)
    depth_first_search(value, node.right)


print(depth_first_search(6, root))

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
dfs(visited, graph, "A")
