# Qns : Invert Binary Tree https://leetcode.com/problems/invert-binary-tree/

# Approach: using Depth-First-Search
1) use a temp to hold left child node. swap left = right, right = temp
2) then self.invert(left), self.invert(right)
3) return root

# Solution:
```
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```
---

# Time Complexity
Time complexity is O(n), traverse each node once.

# Space Complexity
Space complexity is O(h), height of binary tree.