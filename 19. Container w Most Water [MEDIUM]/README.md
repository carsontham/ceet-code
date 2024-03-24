# Qns : Container with Most Water https://leetcode.com/problems/container-with-most-water/

# Approach:
1) Use two pointers, left and right. Left starts at 0, right starts at last index (-1)
2) Use a while loop left < right: Compute the curWater and max()
3) if left pointer has shorter height than right pointer, shift left += 1, else, right -= 1
4) eventually the max can be found.
---

# Solution:
```
def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxWater = 0
        
        while left < right:
            curWater = min(height[left], height[right]) * (right-left)
            maxWater = max(maxWater, curWater)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater
```
---

# Time Complexity
Time complexity will be O(n).
We have to loop through the entire array to check the different combinations.

# Space Complexity
Space complexity is O(1). We only store maxWater, left and right.