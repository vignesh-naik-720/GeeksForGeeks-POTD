"""
Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list.

Examples:

Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40
Explanation:

Input: head1 = 1 -> 1, head2 = 2 -> 4
Output: 1 -> 1 -> 2 -> 4
Explanation:

Constraints:
1 <= no. of nodes<= 10^3
0 <= node->data <= 10^5
"""
def sortedMerge(self,head1, head2):
        # If one of the lists is empty, return the other
        if not head1:
            return head2
        if not head2:
            return head1
        
        # Initialize pointers for the merged list
        if head1.data < head2.data:
            new_head = head1
            head1 = head1.next
        else:
            new_head = head2
            head2 = head2.next
        
        # Keep track of the tail of the merged list
        current = new_head
        
        # Traverse both lists and attach the smaller node to the merged list
        while head1 and head2:
            if head1.data < head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        
        # Attach the remaining nodes from either list
        if head1:
            current.next = head1
        if head2:
            current.next = head2
        
        return new_head
