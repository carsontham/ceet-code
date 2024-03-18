class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        store = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        
        for i in s:
            if i in store:
                stack.append(i)
            else:
                if len(stack) == 0 or store[stack.pop()] != i:
                    return False
        
        return not stack