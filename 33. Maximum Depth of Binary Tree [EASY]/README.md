# Qns : Max Depth of Binary Tree https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Approach
1) Use DFS recursively. Check if root is NONE. If no, return 1 + max() of root left and right

# Solution:
```
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right) )
        
```
---

# Time Complexity
Time complexity is O(n), height of tree.

# Space Complexity
Space complexity is O(h), height of tree due to recursion call stack.