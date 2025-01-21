"""
Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.

Examples:

Input: head = 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8, k = 4
Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5

Explanation: The first 4 elements 1, 2, 2, 4 are reversed first and then the next 4 elements 5, 6, 7, 8. Hence, the resultant linked list is 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5.
Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3
Output: 3 -> 2 -> 1 -> 5 -> 4

Explanation: The first 3 elements 1, 2, 3 are reversed first and then left out elements 4, 5 are reversed. Hence, the resultant linked list is 3 -> 2 -> 1 -> 5 -> 4.
Constraints:
1 <= size of linked list <= 105
1 <= data of nodes <= 106
1 <= k <= size of linked list 
"""
def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head
    
        dummy = Node(0)
        dummy.next = head
        prev, curr, nex = dummy, dummy, dummy
        length = 0
    
        # Calculate the length of the linked list
        while curr.next:
            curr = curr.next
            length += 1
    
        # Reverse nodes in k groups
        while length >= k:
            curr = prev.next
            nex = curr.next
            for _ in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            length -= k
    
        # If remaining nodes are less than k, reverse them as well
        if length > 0:
            curr = prev.next
            nex = curr.next
            for _ in range(1, length):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
    
        return dummy.next
