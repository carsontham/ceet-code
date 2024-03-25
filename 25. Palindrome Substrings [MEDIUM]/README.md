# Qns : Palindrom Substring https://leetcode.com/problems/palindromic-substrings/

# Approach:
1) iterate through the string. During each iteration, use a while loop to check if the left and right are palindrome. If yes, increment left and right.
2) however, this is only for odd numbers. We need to check even number palindrome too.
3) Thus, initialize left = i, right = i+1 to have even number palindrome.
4) If both left and right are palindrome, increment result. Lastly, return the result. 
---

# Solution:
```
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        
        return result
```
---

# Time Complexity
Time complexity is O(n^2). Within each iteration, there may be additional N palindrome.

# Space Complexity
Space complexity is O(1). Only kept pointers to left, right, result and i.