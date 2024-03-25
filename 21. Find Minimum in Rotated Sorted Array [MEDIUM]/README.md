# Qns : Find Minimum in Rotated Sorted Array https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

# Approach:
1) Use two pointers, left and right
2) use a while loop left < right: 
3) if mid > right, this means that there is smaller numbers on the right side. Thus, we should move left pointer there
4) move left = mid + 1
5) Otherwise, the smaller number is earlier in front. Move the right pointer = mid.
6) return the nums[left] for smallest number
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