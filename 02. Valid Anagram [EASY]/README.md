# Qns : Valid Anagram https://leetcode.com/problems/valid-anagram/

# Approach:
Use a dictionary to store character and it's frequenceies as Key-Pair Values. 
Loop through first string, store all char in dictionary.
Then loop through second string, subtract from the frequencies in the dictionary.
Lastly, check if there is any letter's frequency != 0.

---

# Solution:
```
def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # check if length of s and t are the same
        if len(s) != len(t):
            return False
        
        # anagram basically means that no. of different characters are the same
        # use a dictionary to store the frequencies of characters

        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                return False
        
        for v in freq.values():
            if v != 0:
                return False
        
        return True
```
---

# Time Complexity
Worst case : O(n)
Have to loop through the entire array, thus O(n).

# Space Complexity
Worst case : O(n)
Have to loop through the entire array to check the frequencies, thus O(n).