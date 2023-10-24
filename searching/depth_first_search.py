class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(
    10, TreeNode(7, TreeNode(6), TreeNode(8)), TreeNode(13, TreeNode(11), TreeNode(15))
)


def depth_first_search(value, root):
    stack = []
    stack.append(root)
    while len(stack) != 0:
        current_node = stack.pop()
        print(current_node.val)
        if current_node.val == value:
            return True
        if current_node.right != None:
            stack.append(current_node.right)
        if current_node.left != None:
            stack.append(current_node.left)

    return False


def breadth_first_search(value, node):
    queue = []
    queue.append(node)
    while len(queue) != 0:
        current_node = queue.pop(0)
        print(current_node.val)
        if current_node.val == value:
            return True
        if current_node.left != None:
            queue.append(current_node.left)
        if current_node.right != None:
            queue.append(current_node.right)


def depth_first_search_recur(value, node):
    return True if recur(value, node) else False


def recur(value, node):
    if node == None:
        return

    print(node.val)
    if node.val == value:
        return True

    recur(value, node.left)
    recur(value, node.right)


# print(depth_first_search(6, root))
print(depth_first_search_recur(6, root))
print(depth_first_search_recur(29, root))
# print(depth_first_search(29, root))
# print(depth_first_search(13, root))


# print(breadth_first_search(6, root))
# print(breadth_first_search(29, root))
# print(breadth_first_search(13, root))
