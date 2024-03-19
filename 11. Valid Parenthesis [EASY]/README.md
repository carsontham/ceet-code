# Qns : Valid Parenthesis https://leetcode.com/problems/valid-parentheses/ 

# Approach:
1) Use a map to store the brackets, initialize empty stack
2) Use for loop to check if the char is in stack
3) If yes, add to stack. If no, check if last item store[stack.pop()] == current bracket
4) Return not stack (if empty or len = 0)
---

# Solution:
```
def isValid(self, s: str) -> bool:
        
        stack = []
        store = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        
        for i in s:
            # char is in store, append to stack
            if i in store:
                stack.append(i)
            else:
                # this else check means the bracket is a right bracket. 
                # Fails if stack is empty. 
                # Fails if the last element in stack does not match the current right bracket.
                if len(stack) == 0 or store[stack.pop()] != i:
                    return False
        
        return not stack
```
---

# Time Complexity
Worst case : O(N)
Have to loop through the entire string.

# Space Complexity
Worst case : O(n)
Have to store the map of brackets + stack memory (but will ultimately be zero after the qns)