# Qns : Evaluate Reverse Polish Notation https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Approach
1) How RPN work is that each time u come across an operator like +, -, * or /, it will perform the operation on the last two digits
2) How to solve this: use if elif else to check if cur token is an operator. If yes, perform stack.pop() and stack.pop() to get the last two digits. Then append the digit to the stack again


# Solution:
```
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack[-1]
```
---

# Time Complexity
Time complexity is O(n) since we iterate through all elements in array.

# Space Complexity
Space complexity is O(1) since we only will be left with one item in the array at the end.