class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_iterative(root: TreeNode, value) -> bool:
    stack = [root]

    while stack:
        node = stack.pop()

        if node.val == value:
            return True

        if node.left:
            stack.push(node.left)

        if node.right:
            stack.push(node.right)

    return False


def bfs_iterative(root: TreeNode, value) -> bool:
    return False
