# Qns : Group Anagram https://leetcode.com/problems/group-anagrams/

# Approach:
Use a dictionary, keys will be unique signature of the words based on ASCII. For Values, it will be a list of each anagram. 

---

# Solution:
```
from collections import defaultdict

def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return [strs]
            
        ## using python libraries to create a dictionary, with value of type arrays
        answerMap = defaultdict(list)

        # similarly, initialize the unique key signature based on ASCII
        for word in strs:
            key_signature = [0] * 26
            
            for char in word:
                key_signature[ord(char) - ord('a')] += 1
            
            # reason for casting the array into tuple is because tuples are immutable
            # in python dictionaries, Keys must be immutable type
            # but this seems take slightly more memory space
            # however, execution time seems to be faster too
            answerMap[tuple(key_signature)].append(word)
        
        return answerMap.values()
```
---

# Time Complexity
Worst case : O(N * K)
For each word in strs[], it will be O(n).
For each character in each word, worst case will be K, where K is the number of characters in a longest word.
Thus time complexity = O(n*K) 

# Space Complexity
Worst case : O(n)
In the dictionary, ultimately it will be n number of anagrams being stored. 
Thus space complexity = O(n)