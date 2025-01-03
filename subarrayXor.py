'''
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

Examples: 

Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.
Input: arr[] = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].
Constraints:

1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤105
0 ≤ k ≤ 105
'''
def subarrayXor(self, arr, k):
        xor_sum = 0
        freq = {0: 1}  # To handle cases where the XOR itself is k
        count = 0
    
        # Traverse the array
        for num in arr:
            # Update the cumulative XOR
            xor_sum ^= num
    
            # Calculate the required XOR value for the subarray
            required_xor = xor_sum ^ k
    
            # Check if the required XOR exists in the hashmap
            if required_xor in freq:
                count += freq[required_xor]
    
            # Update the frequency of the current XOR value
            freq[xor_sum] = freq.get(xor_sum, 0) + 1
    
        return count
