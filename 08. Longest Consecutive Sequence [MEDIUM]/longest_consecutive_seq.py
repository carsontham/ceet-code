class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # use a set to remove duplicates 
        numSet = set(nums)

        # initialized longest as 0
        longest_seq = 0

        # loop through the original array
        for num in numSet:
            # if there is no left number, it is start of a sequence
            if (num-1) not in numSet:

                # now check if there is a next number in the numSet
                # if yes, increase length by 1
                length = 0
                while (num+length) in numSet:
                    length += 1
                
                # get the longest sequence
                longest_seq = max(longest_seq, length)

        return longest_seq

                