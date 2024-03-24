# Qns : Rotate Array https://leetcode.com/problems/rotate-array/

# Approach:
1) First rotate the entire array using two pointers, left=0 and right= len-1
2) then rotate the first k elements
3) rotate the remaining elements 
---

# Solution:
```
def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        left, right = 0, len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1

        left, right = 0, k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1
        
        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1
```
---

# Time Complexity
Time complexity will be O(n).
We have to loop through the entire array to rotate.

# Space Complexity
Space complexity is O(1). we store only additional left and right