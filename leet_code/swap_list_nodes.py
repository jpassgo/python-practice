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
        return




def populate_nodes(head_value = 1, size = 0):
    head = ListNode(head_value)
    populate_nodes_recursive(head, head_value+1, size)
    return head

def populate_nodes_recursive(previous, value, size):
    previous.next = ListNode(value)
    if value >= size:
        return
    else:
        populate_nodes_recursive(previous.next, value+1, size)


head = populate_nodes(size = 5)

