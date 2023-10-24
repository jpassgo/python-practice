#
#
# Find the max sum path in a given binary tree
#


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maxPathSum(tree):
    print(tree.value)

    max = tree.value + calculate_max(tree.left) + calculate_max(tree.right)

    return max


def calculate_max(tree, current_max=float("-inf")):
    stack = [tree]

    while stack:
        node = stack.pop()

        if node.left == None and node.right == None:
            current_max = max(current_max, node.value)

        if node.left != None:
            node.left.value = node.value + node.left.value
            stack.append(node.left)

        if node.right != None:
            node.right.value = node.value + node.right.value
            stack.append(node.right)

    return current_max
