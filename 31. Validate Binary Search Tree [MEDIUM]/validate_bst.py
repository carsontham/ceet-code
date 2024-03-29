# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower, upper, node):
            if not node:
                return True
            
            if not( node.val < upper and node.val > lower):
                return False
            
            else:
                return dfs(lower, node.val, node.left) and dfs(node.val, upper, node.right)
        
        return dfs(float('-inf'), float('inf'), root)

