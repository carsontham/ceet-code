# Qns : Product of Array Except Self https://leetcode.com/problems/product-of-array-except-self/

# Approach:
1) Use dictionary to store frequencies of each element
2) Create a new array of size = len(array) + 1
3) Based on the frequency, append to the index position in a new array
4) From here, all elements are stored in nested arrays in their corresponding index position.
E.g.                arr = [ [], [4,27], [2], [1] ]
        #index position      0   1       2    3

5) Iterate through the array backwards and append to result[], return result[] when len = k

---

# Solution:
```
def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # approach is to get prefix and suffix and then multiply them

        # first initialize the answer array 
        answer = [1] * len(nums)

        # reason for prefix = 1 is because index 0 has no prior numbers
        # so in the answer array initially, it will be stored as 1
        # same reasoning for postfix
        prefix = 1

        # iterate through nums array, set the current index = prefix
        # then multiply cur prefix with cur number
        # so the next iteration will have the updated prefix
        for index in range(len(nums)):
            answer[index] = prefix
            prefix *= nums[index]
        
        # iterate the array backwards 
        # and multiply the postfix with the num in the index
        # this will result in the answer array
        postfix = 1
        for index in range(len(nums)-1, -1, -1):
            answer[index] *= postfix
            postfix *= nums[index]
        
        return answer
```
---

# Time Complexity
Worst case : O(N)
Two seperate iterations through the loop to get prefix and postfix

# Space Complexity
Worst case : O(1) excluding output array
since the pre and post are calculated into the answers array, there is no extra memory used