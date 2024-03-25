class Solution:
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
                size = right - left + 1
                maxLength = max(maxLength, size)

        return maxLength    
            