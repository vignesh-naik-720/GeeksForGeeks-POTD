# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 07:10:30 2025

@author: Vignesh
"""
"""
Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.
Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.
Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 103
0 <= target <= 109
"""

def subarraySum(self, arr, target):
        n = len(arr)
        start = 0
        curr_sum = 0
    
        for end in range(n):
            # Add the current element to the current sum
            curr_sum += arr[end]
    
            # Shrink the window from the left if the current sum exceeds the target
            while curr_sum > target and start <= end:
                curr_sum -= arr[start]
                start += 1
    
            # Check if the current sum equals the target
            if curr_sum == target:
                return [start + 1, end + 1]  # Return 1-based indices
    
        # If no subarray with the given sum is found, return [-1]
        return [-1]