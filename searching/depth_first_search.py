

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
     

root = TreeNode(10, TreeNode(7, TreeNode(6), TreeNode(8)), TreeNode(13, TreeNode(11), TreeNode(15)))


def depth_first_search(value, root):
    stack = []
    stack.append(root)
    while len(stack) == 0:
        current_node = stack.pop()
        if current_node.left != None:
            stack.append(current_node.left)
        if current_node.right != None:
            stack.append(current_node.right)

def recursive_depth_first_search(value, current_node, stack) -> bool:
    
    
        


print(depth_first_search(6, root))
print(depth_first_search(29, root))
print(depth_first_search(13, root))