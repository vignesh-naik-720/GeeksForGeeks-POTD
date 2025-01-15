"""
Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = 15 is [-5, 8, -14, 2, 4] of length 5.
Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].
Constraints:
1 ≤ arr.size() ≤ 10^5
-10^4 ≤ arr[i] ≤ 10^4
-10^9 ≤ k ≤ 10^9
"""
def longestSubarray(self, arr, k):  
        prefix_sum = {}
        current_sum = 0
        max_length = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            # Check if the sum of the subarray from the start equals k
            if current_sum == k:
                max_length = i + 1
            # Check if there is a prefix_sum that satisfies the condition
            if (current_sum - k) in prefix_sum:
                max_length = max(max_length, i - prefix_sum[current_sum - k])
            # Store current_sum in the dictionary if it is not already stored
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = i
        return max_length
