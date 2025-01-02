'''
Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.

Examples:

Input: arr = [10, 2, -2, -20, 10], k = -10
Output: 3
Explaination: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.
Input: arr = [9, 4, 20, 3, 10, 5], k = 33
Output: 2
Explaination: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.
Input: arr = [1, 3, 5], k = 0
Output: 0
Explaination: No subarray with 0 sum.
Constraints:

1 ≤ arr.size() ≤ 105
-103 ≤ arr[i] ≤ 103
-107 ≤ k ≤ 107
'''
def countSubarrays(self, arr, k):
        # code here
        prefix_sum = 0
        count = 0
        prefix_map = {0: 1} 

        for num in arr:
            prefix_sum += num  # Update the prefix sum
            
            # Check if (prefix_sum - k) exists in the map
            if (prefix_sum - k) in prefix_map:
                count += prefix_map[prefix_sum - k]  # Add how many times it occurred
            
            # Update the map with the current prefix_sum
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        
        return count
