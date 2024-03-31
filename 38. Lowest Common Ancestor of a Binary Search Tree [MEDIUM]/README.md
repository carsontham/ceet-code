# Qns : Lowest Common Ancestor of a Binary Search Tree 
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Approach
1) Since it is a BST, all values are sorted nicely in the tree. meaning left < root < right
2) thus, we simply check if both p and q nodes are both bigger / smaller than current root node.
3) if yes, shift the cur pointer to left/right. 
4) when we reach the point whereby either p or q is larger or smaller then cur root, we have reached last interception point (aka intersection). We can then simply return the intersection.


# Solution:
```
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            else:
                return cur
               
```
---

# Time Complexity
Time complexity is O(log n), since we keep searching in one subtree, worst case it's height of tree.

# Space Complexity
Space complexity is O(1), no usage of any data structure.