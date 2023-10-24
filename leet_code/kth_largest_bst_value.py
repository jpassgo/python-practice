#
# Find the Kth largest value in BST
#
#


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    sorted_list = depth_first_sorting(tree, k)
    return sorted_list[len(sorted_list) - k].value


def depth_first_sorting(node, k, list=[]):
    if node is None:
        return
    else:
        depth_first_sorting(node.left, list)
        list.append(node)
        depth_first_sorting(node.right, list)

    return list
