"""
Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. A path can start and end at any node within the tree but must always move downward (from parent to child).

Examples:

Input: k = 7   

Output: 3
Explanation: The following paths sum to k 
 
Input: k = 3

Output: 2
Explanation:
Path 1 : 1 -> 2 (Sum = 3)
Path 2 : 3 (Sum = 3)


Constraints:

1 ≤ number of nodes ≤ 10^4
-100 ≤ node value ≤ 100
-10^9 ≤ k ≤ 10^9
"""
def sumK(self,root,k):
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the current sum
            current_sum += node.data
            
            # Check if there exists a path with sum = k
            count = prefix_sums.get(current_sum - k, 0)
            
            # Update the prefix sum dictionary
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Recur for left and right subtrees
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Backtrack: Remove the current node's contribution
            prefix_sums[current_sum] -= 1
            if prefix_sums[current_sum] == 0:
                del prefix_sums[current_sum]
            
            return count
        
        # Dictionary to store prefix sum frequencies
        prefix_sums = {0: 1}
        
        return dfs(root, 0)
