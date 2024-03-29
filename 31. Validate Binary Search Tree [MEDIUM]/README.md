# Qns : Validate Binary Search Tree https://leetcode.com/problems/validate-binary-search-tree/

# Approach: using Depth-First-Search
1) create a dfs() method that takes in lower and upper bound, and a node.
2) in the dfs() method, check node value is within bounds (> lower, < upper)
3) recursively call itself, left node will have same lower bound but new upper bound and vice versa
4) return dfs() starts with float('-inf) and float('inf')

# Solution:
```
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower, upper, node):
            if not node:
                return True
            
            if not( node.val < upper and node.val > lower):
                return False
            
            else:
                return dfs(lower, node.val, node.left) and dfs(node.val, upper, node.right)
        
        return dfs(float('-inf'), float('inf'), root)
```
---

# Time Complexity
Time complexity is O(n), traverse each node once.

# Space Complexity
Space complexity is O(h), height of binary tree.