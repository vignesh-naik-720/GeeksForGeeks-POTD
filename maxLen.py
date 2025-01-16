"""
Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

Examples:

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
Input: arr[] = [0]
Output: 0
Explnation: There is no subarray with an equal number of 0s and 1s.
Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 1
"""
def maxLen(self, arr):
        # Replace 0 with -1
        arr = [-1 if num == 0 else 1 for num in arr]
        
        # Initialize variables
        prefix_sum = 0
        max_length = 0
        hash_map = {}
        
        for i, num in enumerate(arr):
            prefix_sum += num
            
            # If prefix_sum is 0, the subarray from start to current index is balanced
            if prefix_sum == 0:
                max_length = max(max_length, i + 1)
            
            # If prefix_sum has been seen before, calculate subarray length
            if prefix_sum in hash_map:
                max_length = max(max_length, i - hash_map[prefix_sum])
            else:
                # Store the first occurrence of prefix_sum
                hash_map[prefix_sum] = i
        
        return max_length
