"""
Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]
Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.
Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: Window 1 of size k = 2 is 4 1. Number of distinct elements in this window are 2. 
Window 2 of size k = 2 is 1 1. Number of distinct elements in this window is 1. 
Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]
Constraints:
1 <= k <= arr.size() <= 10^5
1 <= arr[i] <= 10^5
"""
def countDistinct(self, arr, k):
        # Result array to store counts of distinct elements
        result = []
        # Hash map to store frequency of elements in the current window
        freq_map = {}
        
        # Traverse the array
        for i in range(len(arr)):
            # Add the current element to the hash map
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
            
            # If the current index is greater than or equal to k,
            # remove the element that slides out of the window
            if i >= k:
                # Get the element that is sliding out
                out_element = arr[i - k]
                # Decrease its frequency in the map
                freq_map[out_element] -= 1
                # If the frequency becomes 0, remove the element from the map
                if freq_map[out_element] == 0:
                    del freq_map[out_element]
            
            # Once the first window of size k is formed, record the result
            if i >= k - 1:
                result.append(len(freq_map))
        
        return result
