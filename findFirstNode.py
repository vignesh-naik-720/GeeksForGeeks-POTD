"""
Given a head of the singly linked list. If a loop is present in the list then return the first node of the loop else return NULL.

Custom Input format:
A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

Examples:

Input:
 
Output: 3
Explanation: We can see that there exists a loop in the given linked list and the first node of the loop is 3.
Input:
 
Output: -1
Explanation: No loop exists in the above linked list.So the output is -1.
Constraints:
1 <= no. of nodes <= 106
1 <= node->data <= 106 
"""
def findFirstNode(self, head):
        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Step 1: Detect if there is a loop using Floyd's Cycle Detection Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Loop detected
            if slow == fast:
                break
        else:
            # No loop found
            return None

        # Step 2: Find the first node of the loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Return the node itself
        return slow
