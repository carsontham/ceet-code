# Qns : Construct Binary Tree from Preorder and Inorder Traversal 
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Approach
1) Unds the pattern in preorder and inorder traversals.
2) For preorder, the root node will always be the first item in preorder list.
3) For inorder, the root node will be the middle note. Items on the left will be belong in left subtree, while items on the right will belong in the right subtree.
4) Thus, recursively build the left subtree - pass in preorder of all left subtrees using [1:mid+1]. Pass inorder up till [:mid] onwards which are the elements in the left subtree.
5) Recursively build right subtree - pass in preorder starting from mid+1, inorder from mid+1 onwards.
6) finally, return root.

# Solution:
```
    if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree( preorder[1:mid+1], inorder[:mid] )
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        
```
---

# Time Complexity
Time complexity is O(n), all nodes of tree.

# Space Complexity
Space complexity is O(n), construct an entire tree.