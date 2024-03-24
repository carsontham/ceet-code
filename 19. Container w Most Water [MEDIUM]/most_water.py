class Solution:
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