class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
     

root = TreeNode(10, TreeNode(7, TreeNode(6), TreeNode(8)), TreeNode(13, TreeNode(11), TreeNode(15)))


def inorder(node, value, found=False):
    if not node:
        return
    
    if node.left:
        inorder(node.left, value, found)

    if node.right:
        inorder(node.right, value, found)

    if node.val == value:
        found = True
    
    return found

def inorder_iterative(node: TreeNode, value) -> bool:
    stack = [node]

    while stack:   
        node = stack.pop()

        if node.left:
            stack.append(node.left)

        if node.val == value:
            return True

        if node.right:
            stack.append(node.right)

    
    return False

print(inorder(root, 13))
print(inorder_iterative(root, 13))