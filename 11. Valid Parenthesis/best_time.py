class Solution:
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
                # this else check means the bracket is a right bracket )}]. 
                # Fails if stack is empty. 
                # Fails if the last element in stack does not match the current right bracket.
                if len(stack) == 0 or store[stack.pop()] != i:
                    return False
        
        return not stack