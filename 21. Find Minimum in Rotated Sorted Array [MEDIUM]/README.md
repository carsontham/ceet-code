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
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            
            else:
                right = mid
        
        return nums[left]

```
---

# Time Complexity
Time complexity will be O(log n).
We used divide and conquer strategy.

# Space Complexity
Space complexity is O(1). we store only additional left and right