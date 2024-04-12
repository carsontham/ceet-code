# Qns : Longest Palindrome https://leetcode.com/problems/longest-palindrome/

# Approach
1) Store all char frequency in a dictionary. 
2) Iterate through the values, if values % 2, this means it is even number and will definitely work in a palindrome. Thus, we can safely all the value to our result.
3) If it is an odd value, we can use minus 1 from the value to make it even. E.g. 3-1 = 2. We can use length 2 and add to our result. Use a flag to mark it that an odd value exist.
4) Lastly, if oddFlag is True, return result + 1 (bcos in palindrome we allow one char to be odd since it is in the middle of the string). Else, return the result.

# Solution:
```
def longestPalindrome(self, s: str) -> int:

        tracker = {}

        # store char counts into dict 
        for char in s:
            if char in tracker:
                tracker[char] += 1
            else:
                tracker[char] = 1
        

        # to fulfil palindrome - all char must be % 2 except one char (which acts as the mid)
        result = 0

        oddFlag = False
        for value in tracker.values():
            # if value is even number, means we can use all letters 
            # thus increment values to result
            if value % 2 == 0:
                result += value
            else:
                # means the value is odd number
                # we can use all the odd number - 1
                result += value - 1
                oddFlag = True # set the oddFlag = True, this means an odd did exist
        
        if oddFlag:
            return result + 1

        return result        
```
---

# Time Complexity
Time complexity is O(m*n) since we iterate through all elements in grid.

# Space Complexity
Space complexity is O(1), we only have to really use the minutes counter.