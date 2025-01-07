"""
You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes. 

Examples :

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 2 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.
Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.
Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 4.
Constraints:
-105 <= target <=105
 2 <= arr.size() <= 105
-105 <= arr[i] <= 105
"""

def countPairs (self, arr, target) : 
        count = 0
        left = 0
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                # Count pairs with the same left and right values
                left_val = arr[left]
                right_val = arr[right]
                if left_val == right_val:
                    # Number of elements between left and right
                    num_elements = right - left + 1
                    count += (num_elements * (num_elements - 1)) // 2
                    break
                else:
                    left_count = 1
                    right_count = 1
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left += 1
                        left_count += 1
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right -= 1
                        right_count += 1
                    count += left_count * right_count
                    left += 1
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return count
