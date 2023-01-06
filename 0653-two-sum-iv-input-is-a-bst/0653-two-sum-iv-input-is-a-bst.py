# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()
        def dfs(root,k):
            if not root:
                return
            if k-root.val in hashset:
                return True
            else:
                hashset.add(root.val)
            if dfs(root.left,k) or dfs(root.right,k):
                return True
        return dfs(root,k)