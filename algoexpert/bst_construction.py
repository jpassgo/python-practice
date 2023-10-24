# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.insert_recursively(value, self.left)
            else:
                self.left = value
        else:
            if self.right is not None:
                self.insert_recursively(value, self.right)
            else:
                self.right = value

        return self

    def insert_recursively(self, value, currentNode):
        if currentNode < self.value:
            if currentNode.left is not None:
                self.insert_recursively(value, currentNode.left)
            else:
                currentNode.left = value
        else:
            if currentNode.right is not None:
                self.insert_recursively(value, currentNode.right)
            else:
                currentNode.right = value

        return currentNode

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left is not None:
            return self.contains_recursively(value, self.left)
        elif self.right is not None:
            return self.contains_recursively(value, self.right)

        return False

    def contains_recursively(self, value, currentNode):
        if value == currentNode.value:
            return True
        elif value < currentNode.value and currentNode.left is not None:
            return self.contains_recursively(value, currentNode.left)
        elif currentNode.right is not None:
            return self.contains_recursively(value, currentNode.right)

        return False

    def remove(self, value):
        return self
