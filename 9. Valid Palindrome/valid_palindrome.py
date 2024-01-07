class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string += char

        new_string = new_string.lower()
        
        #two pointer approach
        left = 0
        right = len(new_string) - 1

        while left < right:
            if new_string[left] == new_string[right]:
                left += 1
                right -= 1
            else:
                return False

        print(left, right)
        return True

