"""
Given the head of a linked list that may contain a loop.  A loop means that the last node of the linked list is connected back to a node in the same list. The task is to remove the loop from the linked list (if it exists).

Custom Input format:

A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

The generated output will be true if there is no loop in list and other nodes in the list remain unchanged, otherwise, false.

Examples:

Input: head = 1 -> 3 -> 4, pos = 2
Output: true
Explanation: The linked list looks like
A loop is present in the list, and it is removed.
Input: head = 1 -> 8 -> 3 -> 4, pos = 0
Output: true
Explanation: 

The Linked list does not contains any loop. 
Input: head = 1 -> 2 -> 3 -> 4, pos = 1
Output: true
Explanation: The linked list looks like 

A loop is present in the list, and it is removed.
Constraints:
1 ≤ size of linked list ≤ 10^5
"""
#Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # Helper function to detect the loop
        def detectMeetingNode(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow  # Meeting point
            return None
        # Remove the loop if detected
        meeting_node = detectMeetingNode(head)
        if not meeting_node:
            return True  # No loop detected
        # Find the start of the loop
        slow = head
        if slow == meeting_node:
            # Loop starts at head
            while meeting_node.next != slow:
                meeting_node = meeting_node.next
        else:
            while slow.next != meeting_node.next:
                slow = slow.next
                meeting_node = meeting_node.next
        
        # Break the loop
        meeting_node.next = None
        return True
