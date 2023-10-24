class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes


class Node:
    def __init__(self, name="", children=[], visited=False):
        self.name = name
        self.children = children
        self.visited = visited

    def __repr__(self):
        return f"Name={self.name}, Children={self.children}"


# Find a path S and E
def find_path(s, e):
    if e in s.children:
        return True
    elif len(s.children) > 0:
        return dfs([s], e)


def dfs(stack, e):
    current_node = None
    if len(stack) > 0:
        current_node = stack.pop()
        current_node.visited = True

    if e in current_node.children:
        return True
    elif len(current_node.children) > 0:
        for child in current_node.children:
            if child.visited == False:
                stack.append(child)

        dfs(stack, e)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")

a = Node("a", [b, c])
c.children = [d, g]
d.children = [e, g]
e.children = [f, g]
print(find_path(a, e))
print(find_path(b, e))
