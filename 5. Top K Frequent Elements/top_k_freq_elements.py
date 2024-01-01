class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # creates a dictionary to store the frequency of each num
        # key = num, value = frequency
        # e.g. [1,1,1,2,2,4,27]
        # freq = { 1:3, 2:2, 4:1, 27:1 }
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # using list comprehension to create an array with size up to length of array + 1
        # reason for + 1 is because we are not using index 0
        # without +1, array will cause index out of bounds
        arr = [[] for i in range(len(nums) +1) ]

        # iterate through dictionary, append number to the index position equivalent to its frequency 
        # e.g.      arr = [ [], [4,27], [2], [1] ]
        #index position      0   1       2    3

        for num, freq in freq.items():
            arr[freq].append(num)
        
        # initialize the result array to return
        result = []

        # iterate through the arr backwards that stores the frequencies
        # top K elements, meaning we want K numbers that are more frequent
        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                result.append(num)

            # once len of result = k, we have the k most frequent elements
            if len(result) == k:
                return result  
