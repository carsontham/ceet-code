# Qns : Kth Smallest Element in a BST https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Approach
1) Uses inorder traversal and simply return the k-1 element

# Solution:
```
 def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorderTraversal(root):
            if not root: return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

        arr = inorderTraversal(root)
        return arr[k-1]             
```
---

# Time Complexity
Time complexity is O(n), traverse all nodes

# Space Complexity
Space complexity is O(n), have to store n nodes.