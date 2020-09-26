from Node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    # the underscore denotes this method as a private method
    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        pass

    def _in_order(self, curr):
        pass

    def pre_order(self):
        pass

    def _pre_order(self, curr):
        pass
    
    def post_order(self):
        pass

    def _post_order(self, curr):
        pass


tree = BinarySearchTree()
tree.insert("A")

print(tree.root.data)