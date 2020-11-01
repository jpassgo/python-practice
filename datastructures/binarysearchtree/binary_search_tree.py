from Node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root is None:
            self.root = key
        else:
            self._insert(self.root, key)

    # the underscore denotes this method as a private method
    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child is None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data:
            if curr.left_child is None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        # left, root, right
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def pre_order(self):
        pass

    def _pre_order(self, curr):
        pass

    def post_order(self):
        pass

    def _post_order(self, curr):
        pass

    def find_value(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, curr, key):
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._find_value(curr.left_child, key)
            else:
                return self._find_value(curr.right_child, key)
        return "Value not found in tree"

    def delete_value(self, key):
        return self._delete_value(self.root, None, None, key)

    def _delete_value(self, curr, parent, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    print("problem scenario")
                elif curr.left_child is None and curr.right_child is None:
                    self.swap_parents_children_with_leaf(parent, is_left)
                elif curr.left_child is None:
                    self.swap_parents_children_with_right_child(
                        parent, curr, is_left)
                else:
                    self.swap_parents_children_with_left_child(
                        parent, curr, is_left)
            elif key < curr.data:
                self._delete_value(curr.left_child, curr, True, key)
            elif key > curr.data:
                self._delete_value(curr.right_child, curr, False, key)
        else:
            print(f"{key} not found in Tree")

    def swap_parents_children_with_leaf(self, parent, is_left):
        if is_left:
            parent.left_child = None
        else:
            parent.right_child = None

    def swap_parents_children_with_right_child(self, parent, curr, is_left):
        if parent:
            if is_left:
                parent.left_child = curr.right_child
            else:
                parent.right_child = curr.right_child
        else:
            self.root = curr.right_child

    def swap_parents_children_with_left_child(self, parent, curr, is_left):
        if parent:
            if is_left:
                parent.left_child = curr.left_child
            else:
                parent.right_child = curr.left_child
        else:
            self.root = curr.left_child


tree = BinarySearchTree()
tree.insert("A")
tree.insert("X")
tree.insert("F")
tree.insert("C")
tree.insert("B")

tree.in_order()
# print(tree.find_value("F"))
tree.delete_value("F")
tree.in_order()
