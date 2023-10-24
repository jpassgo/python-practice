# 938. Range Sum of BST
#
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes
# with a value in the inclusive range [low, high].
#
# https://leetcode.com/problems/range-sum-of-bst/
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    return recursivelySumNodes(root, low, high)


def recursivelySumNodes(node, low, high, sum=0):
    val = node.val
    if val >= low and val <= high:
        sum += val

    if node.left:
        sum = recursivelySumNodes(node.left, low, high, sum)

    if node.right:
        sum = recursivelySumNodes(node.right, low, high, sum)

    return sum
