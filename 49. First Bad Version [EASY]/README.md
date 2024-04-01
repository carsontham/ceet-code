# Qns : First Bad Version https://leetcode.com/problems/first-bad-version/

# Approach
1) Binary search approach

# Solution:
```
def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid) :
                right = mid
            else:
                left = mid + 1
        
        return right
```
---

# Time Complexity
Time complexity is O(log n), divide and conquer algo

# Space Complexity
Space complexity is O(1), only store pointers.