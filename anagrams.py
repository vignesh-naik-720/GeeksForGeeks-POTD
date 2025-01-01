'''
Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

Note: The final output will be in lexicographic order.

Examples:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.
Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]
Explanation: 
Group 1: "abc", "bac", and "cab" are anagrams.
Group 2: "listen", "silent", and "enlist" are anagrams.
Group 3: "rat", "tar", and "art" are anagrams.
Constraints:
1<= arr.size() <=100
1<= arr[i].size() <=10
'''

def anagrams(arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        anagram_dict = {}   #To store the list of anagrams

        for word in arr:    #iterate through each word in arr

            key = ''.join(sorted(word)) #create the key which is sorted form of the word for eg key for cat is act.
            
            if key in anagram_dict: #if key is in the dictionary 
                anagram_dict[key].append(word)  #append the word to the anagrams list
            else:   #if key is not present
                anagram_dict[key] = [word]  #create a new key and create a list with word as its first value.

        return list(anagram_dict.values()) 

print(anagrams(["act", "god", "cat", "dog", "tac"]))
