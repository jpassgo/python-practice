# 
#  https://leetcode.com/problems/swap-nodes-in-pairs/
# 
#  24. Swap Nodes in Pairs
# 
#  Given a linked list, swap every two adjacent nodes and return its head. 
#  You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# 

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next        


class Solution:

    def swap_list_nodes(self, head: ListNode):
        temp = head.next
        swap(head, head.next)
        return temp

    def swap(self, current, next):
        while current.next is not None:
            temp = current
            current = current.next
            current.next = temp
            swap(current.next, current.next.next)

        return 



# For testing the solution
def populate_nodes(head_value = 1, size = 0):
    head = ListNode(head_value)
    populate_nodes_recursively(head, head_value+1, size)
    return head

def populate_nodes_recursively(previous, value, size):
    current = ListNode(value)
    previous.next = current
    if value >= size:
        current.next = None
        return
    else:
        populate_nodes_recursively(previous.next, value+1, size)


head = populate_nodes(size = 5)


def recursively_print_nodes(node):
    print(f'Node Value: {node.val}')
    if node.next is None:
        return 
    else:
        recursively_print_nodes(node.next)


recursively_print_nodes(head)


Solution().swap_list_nodes(head = head)

recursively_print_nodes(head)