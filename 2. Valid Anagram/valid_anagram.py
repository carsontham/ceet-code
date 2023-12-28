class Solution(object):
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
