from Node import Node

class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            self._insert(self.root, node)

    def _insert(self, curr, node):
        if node.data < curr.data:
            node.height += 1 
            if curr.left == None:    
                curr.left = node
            else:
                self._insert(curr.left, node)
        elif node.data >= curr.data:
            node.height += 1
            if curr.right == None:
                curr.right = node
            else:
                self._insert(curr.right, node)
        
    def left_rotation(self):
        pass

    def right_rotation(self):
        pass




        
