# Qns : Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Approach
1) Unds the pattern in postorder and inorder traversals.
2) For postorder, the root node will be the last item in postorder list.
3) For inorder, the root node will be the middle note. Items on the left will be belong in left subtree
4) This is kinda tough. to revisit again.

# Solution:
```
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = { v:i for i,v in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            root = TreeNode(postorder.pop())
            index = inorder_index[root.val]

            root.right = helper(index+1, right)
            root.left = helper(left, index -1)

            return root
        
        return helper(0, len(inorder) - 1)        
```
---

# Time Complexity
Time complexity is O(n), all nodes of tree.

# Space Complexity
Space complexity is O(n), construct an entire tree.