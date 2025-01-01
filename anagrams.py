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
