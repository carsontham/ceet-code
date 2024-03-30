
# Tree Traversals (Preorder, Postorder, Inorder)

# inorder -> left -> root -> right
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# postoder -> left -> right -> root
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root: return []
    return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


# preorder -> root -> left -> right
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root: return []
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)