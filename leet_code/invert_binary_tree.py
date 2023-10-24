#
# 226. Invert Binary Tree
#
# Given the root of a binary tree, invert the tree, and return its root.
#
# https://leetcode.com/problems/invert-binary-tree/
#
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = root.left
        root.left = root.right
        root.right = temp

        if root.left is not None:
            self.invertTree(root.left)

        if root.right is not None:
            self.invertTree(root.right)

    def print_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.preorder_traversal(root, "root node = ")

    def preorder_traversal(self, node: Optional[TreeNode], text) -> Optional[TreeNode]:
        print(f"{text}{node.val}\n")
        if node.left is not None:
            self.preorder_traversal(node.left, "left node = ")
        if node.right is not None:
            self.preorder_traversal(node.right, "right node = ")


solution = Solution()
root = TreeNode(
    4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
)
solution.print_tree(root)
print("---------------")
solution.invertTree(root)
solution.print_tree(root)
