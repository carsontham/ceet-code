# Qns : Product of Array Except Self https://leetcode.com/problems/product-of-array-except-self/

# Approach:

To solve this, use PREFIX and POSTFIX.
This will store the answer of all products before element [i].

create an array of size = len of given array
loop through array once, and assign the prefix to the answer array.

then loop through array from back, multiply postfix to answer array. 
return results.

---

# Solution:
```
def productExceptSelf(self, nums: List[int]) -> List[int]:
        answerArray = [0]*len(nums)

        prefix = 1

        for index in range(len(nums)):
            answerArray[index] = prefix
            prefix *= nums[index]
        
        postfix = 1
        for index in range(len(nums)-1 , -1, -1):
            answerArray[index] *= postfix
            postfix *= nums[index]

        return answerArray
```
---

# Time Complexity
Time complexity is O(n) since only use two for loops = O(2n)

# Space Complexity
Space complexity is O(1) since the variables used to store pre and post is fixed. No additional arrays were required to be created. Excluding the final array, the algo will be considerd O(1)
