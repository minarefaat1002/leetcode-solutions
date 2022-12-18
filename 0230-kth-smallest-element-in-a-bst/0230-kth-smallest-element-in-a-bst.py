# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            nonlocal k
            if not root:
                return 0
            left = dfs(root.left)
            if left:
                return left
            k-=1
            if k == 0:
                return root.val
            right = dfs(root.right)
            return right
        
        return dfs(root)