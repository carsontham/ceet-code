class Solution:
    def longestPalindrome(self, s: str) -> int:

        tracker = {}

        # store char counts into dict 
        for char in s:
            if char in tracker:
                tracker[char] += 1
            else:
                tracker[char] = 1
        

        # to fulfil palindrome - all char must be % 2 except one char (which acts as the mid)
        result = 0

        oddFlag = False
        for value in tracker.values():
            # if value is even number, means we can use all letters 
            # thus increment values to result
            if value % 2 == 0:
                result += value
            else:
                # means the value is odd number
                # we can use all the odd number - 1
                result += value - 1
                oddFlag = True # set the oddFlag = True, this means an odd did exist
        
        if oddFlag:
            return result + 1

        return result




        