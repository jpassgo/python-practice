# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
	balance = [True]

    height = calculateHeight(tree, 0, balance)
    print(height)
		
    return balance[0]

def calculateHeight(tree, height, balance):
    if tree == None:
        return height

    leftHeight = calculateHeight(tree.left, height+1, balance)
    rightHeight = calculateHeight(tree.right, height+1, balance)

    if abs(leftHeight - rightHeight) > 1:
        balance[0] = False

    return max(leftHeight, rightHeight)
        
    