"""
Given the head of a linked list, the task is to reverse this list and return the reversed head.

Examples:

Input: head: 1 -> 2 -> 3 -> 4 -> NULL
Output: head: 4 -> 3 -> 2 -> 1 -> NULL
Explanation:

Input: head: 2 -> 7 -> 10 -> 9 -> 8 -> NULL
Output: head: 8 -> 9 -> 10 -> 7 -> 2 -> NULL
Explanation:

Input: head: 2 -> NULL
Output: 2 -> NULL
Explanation:

Constraints:
1 <= number of nodes, data of nodes <= 105
"""
#function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
def reverseList(self, head):
        # Initialize previous and current pointers
        prev = None
        curr = head
        
        while curr:
            # Temporarily store the next node
            next_node = curr.next
            # Reverse the current node's pointer
            curr.next = prev
            # Move the pointers one step forward
            prev = curr
            curr = next_node
        
        # The new head is the previous node
        return prev
