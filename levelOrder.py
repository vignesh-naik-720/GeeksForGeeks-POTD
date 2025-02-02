"""
Given a root of a binary tree with n nodes, the task is to find its level order traversal. Level order traversal of a tree is breadth-first traversal for the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: [[1], [2, 3]]
Input: root[] = [10, 20, 30, 40, 50]

Output: [[10], [20, 30], [40, 50]]
Input: root[] = [1, 3, 2, N, N, N, 4, 6, 5]

Output: [[1], [3, 2], [4], [6, 5]]
Constraints:

1 ≤ number of nodes ≤ 10^5
0 ≤ node->data ≤ 10^9
"""
from collections import deque
def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(level_nodes)
        
        return result
