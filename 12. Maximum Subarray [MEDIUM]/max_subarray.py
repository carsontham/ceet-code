class Solution:
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
                