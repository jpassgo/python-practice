from AVLTree import AVLTree
from Node import Node
from random import randint

tree = AVLTree()

node_list = []
i = 0
while i < 10:
    i += 1
    node_list.append(Node(randint(1, 100)))

for node in node_list:
    tree.insert(node)
    print(f"Data: {node.data}")
    # print(f"Height: {node.height}")
    

for node in node_list:
    print(f"Height: {tree.get_height(node)}")

