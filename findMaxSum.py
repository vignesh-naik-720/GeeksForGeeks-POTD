"""
Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

Examples:

Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
Output: 42
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Input: root[] = [-17, 11, 4, 20, -2, 10]
Output: 31
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Constraints:
1 ≤ number of nodes ≤ 103
-104 ≤ node->data ≤ 104
"""
def findMaxSum(self, root): 
        self.max_sum = float('-inf')  # Variable to store the maximum path sum

        def helper(node):
            if not node:
                return 0
            
            # Recursively compute the maximum path sum for left and right subtrees
            left_sum = max(helper(node.left), 0)  # Ignore negative sums
            right_sum = max(helper(node.right), 0)
            
            # Compute the maximum path sum passing through the current node
            current_sum = node.data + left_sum + right_sum
            
            # Update the global maximum path sum if the current sum is greater
            self.max_sum = max(self.max_sum, current_sum)
            
            # Return the maximum sum of one of the paths including the current node
            return node.data + max(left_sum, right_sum)
        
        helper(root)
        return self.max_sum
