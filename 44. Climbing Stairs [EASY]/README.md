# Qns : Climbing Stairs https://leetcode.com/problems/climbing-stairs/

# Approach
1) This is dynamic programming. Smth like fibonacci sequence.
2) Essentially the answer = prev + prev-1. Thus we use one,two = 1,1
3) iterate and add one, two = one+two, one. Lastly return one

# Solution:
```
def climbStairs(self, n: int) -> int:
        one, two = 1,1

        for i in range(n-1):
            one, two = one+two, one

        return one
```
---

# Time Complexity
Time complexity is O(n), have to iterate the entire array.

# Space Complexity
Space complexity is O(1), store only values of one and two.