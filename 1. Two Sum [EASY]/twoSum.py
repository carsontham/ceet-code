class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        store = {}

        # loop through the array to find the other number
        for index in range(len(nums)):
            # determine the other number 
            otherNum = target-nums[index]

            # check if other number already exists in the dictionary
            if otherNum in store: # check if other num exists is in existing keys
                return [index, store[otherNum]] # if exists, returns the two indexes 
            else:
                # insert the cur value as key, cur index as value into the dictionary
                store[nums[index]] = index
