class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create an empty set
        unique = set()

        # iterate through the list and append to set if not already in set
        # if already in set, return True
        for num in nums:
            if num in unique:
                return True
            else:
                unique.add(num)
        
        return False