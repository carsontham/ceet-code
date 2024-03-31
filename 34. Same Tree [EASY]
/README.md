# Qns : Same Tree https://leetcode.com/problems/same-tree/

# Approach
1) Use DFS recursively. 
2) Check if p and q are None. if both yes, return True
3) Check if either p or q are None. If yes, return False
4) Check if p = q, if true, continue self dfs.

# Solution:
```
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
```
---

# Time Complexity
Time complexity is O(n), all nodes of tree.

# Space Complexity
Space complexity is O(h), height of tree due to recursion call stack.