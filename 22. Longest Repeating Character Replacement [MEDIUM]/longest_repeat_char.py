class Solution:
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