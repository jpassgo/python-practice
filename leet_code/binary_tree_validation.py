# 
# 98. Validate Binary Search Tree
# 
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# 
# A valid BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# https://leetcode.com/problems/validate-binary-search-tree/
# 

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        return self.preorder(root)

    def preorder(self, node: TreeNode):
        if node.left is None or node.right is None:
            return    
        if node.val < node.left.val:
            return False
        if node.val > node.right.val:
            return False
        self.preorder(node.left)
        self.preorder(node.right)
        return True


# Implement inorder, preorder, or postorder traversal. 
# Each time you check if the left node is less than the current (root) 
# and if the right node is greater than the root

valid_root = TreeNode(10, TreeNode(7, TreeNode(6), TreeNode(8)), TreeNode(13, TreeNode(11), TreeNode(15)))

invalid_root = TreeNode(10, TreeNode(15, TreeNode(6), TreeNode(8)), TreeNode(13, TreeNode(11), TreeNode(15)))

solution = Solution()
print(solution.isValidBST(valid_root))
print(solution.isValidBST(invalid_root))