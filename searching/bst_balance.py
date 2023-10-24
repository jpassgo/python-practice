class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(node):
    if node is None:
        return -1
    else:
        left_height = height(node.left)
        right_height = height(node.right)

    return 1 + max(left_height, right_height)


def is_balanced(node):
    if node is None:
        return -1
    else:
        left_height = is_balanced(node.left)
        right_height = is_balanced(node.right)
        if abs(left_height - right_height) > 1:
            return False

    return 1 + max(left_height, right_height)


root = TreeNode(
    10, TreeNode(7, TreeNode(6), TreeNode(8)), TreeNode(13, TreeNode(11), TreeNode(15))
)

print(height(root))
