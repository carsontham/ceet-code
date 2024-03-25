# Qns : Longest Substring Without Repeating Characters 
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Approach:
1) Use sliding window technique. Use dict to keep track of the frequency count.
2) iterate through the array, check if the current char exist in dict. 
3) if no, then add to dict, update maxLength using max()
4) if yes, move the sliding window. use while loop to minus count from dict + increase left until reach the same char. 
5) Once reach same char, left += 1 again for left pointer to be the start of the new substring
6) FYI, SOLVED IT ON MY OWN!!!!!! 25 MARCH 24 10:46PM :D

---

# Solution:
```
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        maxLength = 0
        left = 0

        for right in range(len(s)):
            if count.get(s[right], 0) == 0:
                count[s[right]] = 1
                size = right - left + 1
                maxLength = max(maxLength, size)
            
            else:
                while s[left] != s[right]:
                    count[s[left]] -= 1
                    left += 1
                left += 1

        return maxLength    
```
---

# Time Complexity
Time complexity is O(n). Iterate once through the array. 

# Space Complexity
Space complexity is O(n). Worse case when all characters are unique.