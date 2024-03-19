# Qns : Two Sum II https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Approach:
1) Since it is a sorted array, use Two Pointers
2) Left = 0, right = len(array)-1
3) check if the curNum is larger or smaller than the target
4) either increment left pointer or decrement right pointer
5) return the index of l and r  


---

# Solution:
```
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            cur = numbers[left] + numbers[right]
            
            if cur > target:
                right -= 1

            elif cur < target:
                left += 1
            else:
                return [left+1, right+1] 
```
---

# Time Complexity
Time complexity is O(n) since we have to loop the array once

# Space Complexity
Space complexity is O(1) since we store only left and right.
