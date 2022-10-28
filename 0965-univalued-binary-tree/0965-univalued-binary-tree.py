# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        pivot = root.val
        def dfs(root,pivot):
            if not root:
                return True
            if root.val == pivot and dfs(root.left,pivot) and dfs(root.right,pivot):
                return True
            else:
                return False
        return dfs(root,pivot)