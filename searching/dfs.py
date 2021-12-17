class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
     

root = TreeNode(10, TreeNode(7, TreeNode(6), TreeNode(8)), TreeNode(13, TreeNode(11), TreeNode(15)))

def pre_order_dfs(node, value):
    stack = []
    stack.append(node)

    while len(stack) != 0:
        current_node = stack.pop()

        if current_node.val == value:
            return True

        if current_node.left != None:
            stack.append(current_node.left)
        if current_node.right != None:
            stack.append(current_node.right)

    return False

def pre_order_bfs(node, value):
    queue = []
    queue.append(node)

    while len(queue) > 0:
        current_node = queue[0]
        del queue[0]
        
        if current_node.val == value: return True

        left = current_node.left
        right = current_node.right

        if left != None: queue.append(left)
        if right != None: queue.append(right)

    return False


print('pre_order_dfs')
print(pre_order_dfs(root, 10))
print(pre_order_dfs(root, 7))        
print(pre_order_dfs(root, 6))
print(pre_order_dfs(root, 8))
print(pre_order_dfs(root, 13))
print(pre_order_dfs(root, 11))        
print(pre_order_dfs(root, 15))

print(pre_order_dfs(root, 150))

print('pre_order_bfs')
print(pre_order_bfs(root, 10))
print(pre_order_bfs(root, 7))        
print(pre_order_bfs(root, 6))
print(pre_order_bfs(root, 8))
print(pre_order_bfs(root, 13))
print(pre_order_bfs(root, 11))        
print(pre_order_bfs(root, 15))

print(pre_order_bfs(root, 150))
