"""
Given an array arr[] of n sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list, then return the head of the merged linked list.

Examples:

Input: arr[] = [1 -> 2 -> 3, 4 -> 5, 5 -> 6, 7 -> 8]
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> 7 -> 8
Explanation:
The arr[] has 4 sorted linked list of size 3, 2, 2, 2.
1st list: 1 -> 2-> 3
2nd list: 4 -> 5
3rd list: 5 -> 6
4th list: 7 -> 8
The merged list will be:
 
Input: arr[] = [1 -> 3, 8, 4 -> 5 -> 6]
Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8
Explanation:
The arr[] has 3 sorted linked list of size 2, 3, 1.
1st list: 1 -> 3
2nd list: 8
3rd list: 4 -> 5 -> 6
The merged list will be:

Constraints
1 <= total no. of nodes <= 105
1 <= node->data <= 103
"""
import heapq
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
class Solution:
    def mergeKLists(self, arr):
        if not arr:
            return None
        
        min_heap = []
        
        # Push the first node of each linked list into the heap
        for index, node in enumerate(arr):
            if node:
                heapq.heappush(min_heap, (node.data, index, node))

        # Dummy node to start the merged linked list
        dummy = Node(0)
        curr = dummy

        while min_heap:
            # Extract the node with the smallest value
            value, index, node = heapq.heappop(min_heap)
            
            # Add this node to the merged linked list
            curr.next = node
            curr = curr.next
            
            # If the extracted node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.data, index, node.next))

        return dummy.next  # Return the merged linked list
