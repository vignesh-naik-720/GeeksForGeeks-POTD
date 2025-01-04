"""
Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Two triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2
Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 
Constraints:
3 ≤ arr.size() ≤ 103
-105 ≤ arr[i], target ≤ 105

"""
def countTriplets(self, arr, target):
        n = len(arr) 
        count = 0 
        for i in range(n - 2): 
            # Create a dictionary to store the frequency of elements
            seen = {}
            current_target = target - arr[i] 
            for j in range(i + 1, n): 
                if current_target - arr[j] in seen: 
                    count += seen[current_target - arr[j]]  # Increment count by the dictionary value
                if arr[j] in seen: 
                    seen[arr[j]] += 1  # Increment the count of the current element
                else:
                    seen[arr[j]] = 1  # Initialize count for the current element
        return count
