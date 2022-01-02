from Node import Node


class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balanceFactor = self.get_balance(root)

        # Left heavy sub tree
        if balanceFactor > 1:
            # left left
            if data < root.left.data:
                return self.right_rotation(root)
            # left right
            else:
                return self.left_right_rotation(root)
        if balanceFactor < -1:
            # right right
            if data > root.right.data:
                return self.left_rotation(root)
            # right left
            else:
                return self.right_left_rotation(root)

        return root

    def left_rotation(self, node):
        
        return node

    def right_rotation(self, node):
        node.left.right = node
        node = node.left
        return

    def left_right_rotation(self, node):
        pass

    def right_left_rotation(self, node):
        pass

    def rebalance(self, node):
        if 