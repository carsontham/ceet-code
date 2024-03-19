# Qns : Maximum Subarray https://leetcode.com/problems/maximum-subarray/

# Approach:
1) Can be solved linearly (one loop)
2) first initialize maxSum and curSum, then iterate through the array. 
3) if curSum is less than 0, means somewhere they added a negative number that is not worth keeping. thus throw it away.
4) Add current number to curSum. Check max() during each iteration
---

# Solution:
```
def maxSubArray(self, nums: List[int]) -> int:
        # initialize a current max sum and cur sum
        maxSum = nums[0]
        curSum = 0

        # iterate through the array
        for i in nums:
            # if anytime the curSum is less than 0, it means the sum is not worth to keep since we want max sum
            if curSum < 0:
                # set curSum to 0
                curSum = 0
            # add the current number to curSum
            curSum += i
            #use max() to always get the maxSum 
            maxSum = max(maxSum, curSum)
        
        return maxSum
```
---

# Time Complexity
Worst case : O(N)
Loop through the array only once 

# Space Complexity
Worst case : O(1)
is O(1) bcos always have to store 2 variables - maxSum and curSum 
