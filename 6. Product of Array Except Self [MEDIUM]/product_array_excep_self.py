class Solution(object):
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