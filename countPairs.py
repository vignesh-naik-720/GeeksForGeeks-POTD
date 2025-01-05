"""
Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.

Examples:

Input: arr[] = [7, 2, 5, 3], target = 8
Output: 2
Explanation: There are 2 pairs with sum less than 8: (2, 5) and (2, 3). 
Input: arr[] = [5, 2, 3, 2, 4, 1], target = 5
Output: 4
Explanation: There are 4 pairs whose sum is less than 5: (2, 2), (2, 1), (3, 1) and (2, 1).
Input: arr[] = [2, 1, 8, 3, 4, 7, 6, 5], target = 7
Output: 6
Explanation: There are 6 pairs whose sum is less than 7: (2, 1), (2, 3), (2, 4), (1, 3), (1, 4) and (1, 5).
Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 104
1 <= target <= 104
"""

def countPairs(self, arr, target):
        arr.sort()
    
        # Initialize pointers and the count variable
        left = 0
        right = len(arr) - 1
        count = 0
    
        # Use two pointers to find valid pairs
        while left < right:
            # Calculate the sum of the current pair
            current_sum = arr[left] + arr[right]
    
            if current_sum < target:
                # If the sum is less than the target, all pairs from left to right-1 are valid
                count += (right - left)
                # Move the left pointer forward to check for other pairs
                left += 1
            else:
                # If the sum is greater than or equal to the target, move the right pointer backward
                right -= 1
    
        return count
