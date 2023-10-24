class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        self.head = reverse_recurse(self.head)

    def reverse_recurse(self, node):
        if node.next == None:
            return node
        else:
            node.next.next = Node
            node.next = None
