# Qns : Longest Repeating Character Replacement https://leetcode.com/problems/longest-repeating-character-replacement/

# Approach:
1) Use sliding window technique. Use dict to keep track of the frequency count.
2) iterate through the array and increment maxFreq
3) use a while loop to check if the current window (right-left + 1) - maxFreq is more than K
4) if yes, decrease the sliding window length + decrement count
5) then check for the maxFreq and after the for loop, return result

---

# Solution:
```
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        left = 0
        maxFreq = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFreq = max(maxFreq, count[s[right]])

            while (right-left+1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result
```
---

# Time Complexity
Time complexity is O(n). Iterate once through the array. 

# Space Complexity
Space complexity is O(n). Worse case when all characters are unique.