# Qns : Balanced Binary Tree https://leetcode.com/problems/balanced-binary-tree/

# Approach

1. Solve the problem bottom-up. Meaning we will check the child nodes first to see if they are balanced.
2. Use depth-first-search (DFS) and check if the height between left and right node is <=1. The DFS function will also return an array [Boolean, height], where height = max(left, right) + 1
3. If there is a False returned, it means that the tree is not balanced.

# Solution:

```
def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return [True, 0]
            left = dfs(node.left)
            right = dfs(node.right)

            # returns a Boolean + check if abs is less than or equal 1
            isBalanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [isBalanced, 1+max(left[1],right[1])]

        return dfs(root)[0]
```

---

# Time Complexity

Time complexity is O(n) since each node is visited once.

# Space Complexity

Space complexity is O(h), which is the height of the tree.
