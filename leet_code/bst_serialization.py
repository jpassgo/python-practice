#
# 449. Serialize and Deserialize BST
#
# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
#  or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
# The encoded string should be as compact as possible.
#
# https://leetcode.com/problems/serialize-and-deserialize-bst/
#
import json
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized_dict = self.recursive_insert(root, {})
        return serialized_dict

    def recursive_insert(self, current: TreeNode, str_dict: dict):
        str_dict["val"] = current.val
        if current.left is not None:
            str_dict["left"] = self.recursive_insert(current.left, {})
        if current.right is not None:
            str_dict["right"] = self.recursive_insert(current.right, {})

        json_str = json.dumps(str_dict)
        return json_str

    def deserialize(self, data: str) -> Optional[TreeNode]:
        root = json.loads(data)
        return self.recursive_deserialize(root)

    def recursive_deserialize(self, root: dict):
        return TreeNode(
            root["val"],
            self.recursive_deserialize(root["left"]),
            self.recursive_deserialize(root["right"]),
        )


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


codec = Codec()
# valid_root = TreeNode(10)
# valid_root.left = left
# valid_root.right = right

# left = TreeNode(7)
# left_left = TreeNode(6)
# left_right = TreeNode(8)
# left.left = left_left
# left.right = left_right

# right = TreeNode(13)
# right_left = TreeNode(11)
# right_right = TreeNode(15)
# right.right_left = right_left
# right.right_right = right_right
root = TreeNode(
    10, TreeNode(7, TreeNode(6), TreeNode(8)), TreeNode(13, TreeNode(11), TreeNode(15))
)

serialized_tree = codec.serialize(root)
print(serialized_tree)
deserialized_tree = codec.deserialize(serialized_tree)
print(deserialized_tree)
