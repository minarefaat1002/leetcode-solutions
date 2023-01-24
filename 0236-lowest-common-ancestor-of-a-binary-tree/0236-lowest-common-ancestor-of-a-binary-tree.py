# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            return right if left ==None else left 
        return dfs(root)
            
            
            