# 
# 234. Palindrome Linked List
# 
# Given the head of a singly linked list, return true if it is a palindrome.
# 
# https://leetcode.com/problems/palindrome-linked-list/
# 

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:  
        palindrome_counter_map = self.populate_palindrome_map(head, {})

        odd_counter = 0
        is_list_odd_len = len(palindrome_counter_map) % 2 != 0
        for key, value in palindrome_counter_map:
            is_value_even = value % 2 == 0

            if is_value_even is not True and is_list_odd_len:
                if odd_counter < 1:
                    odd_counter += 1
                else:
                    return False

    def populate_palindrome_map(self, current, map):
        if current.next:
            map[current.val] = map.get(current.val) + 1
            populate_palindrome_map(current.next, map)
        else:
            return map


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


head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, ))))

solution = Solution()
print(solution.isPalindrome(head))