# Qns : Subtree of Another Tree https://leetcode.com/problems/subtree-of-another-tree/

# Approach
1) Similar approach to same tree problem.
2) check if root or subRoot is none - return True. either is none - return False
3) check if root = subroot value and isSameTree returns True
4) otherwise, move down left and right nodes again.
5) Utilize is SameTree code

# Solution:
```
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)      
```
---

# Time Complexity
Time complexity is O(n), visit all nodes of tree in worst case scenario.

# Space Complexity
Space complexity is O(h), height of tree in call stack.