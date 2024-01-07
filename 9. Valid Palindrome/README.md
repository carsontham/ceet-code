# Qns : Valid Palindrome https://leetcode.com/problems/valid-palindrome/

# Approach:
1) Process the string by checking if each char is .alnum(), if yes, add them to a new string
2) then convert the string to lowercase using .lower()
3) Lastly use two pointer approach, check left and right 
---

# Solution:
```
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
```
---

# Time Complexity
Worst case : O(N)
Reason is due to the processing of data, have to loop through every single char

# Space Complexity
Worst case : O(n)
We create additional string in memory.
