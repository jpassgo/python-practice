from typing import List


class Node:
    children: List[Edge]


class Edge:
    target: Node
    cost: int
