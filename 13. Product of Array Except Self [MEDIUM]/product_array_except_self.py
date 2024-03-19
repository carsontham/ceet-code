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