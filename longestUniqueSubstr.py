"""
Given a string s, find the length of the longest substring with all distinct characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.
Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.
Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.
Constraints:
1<= s.size()<=3*10^4
All the characters are in lowercase.
"""
def longestUniqueSubstr(self, s):
        char_set = set()  # To store characters in the current window
        max_length = 0  # To store the maximum length of distinct substring
        left = 0  # Left pointer of the sliding window
    
        for right in range(len(s)):  # Right pointer of the sliding window
            # If the character at `right` is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
    
            # Add the current character to the set
            char_set.add(s[right])
    
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
    
        return max_length  
