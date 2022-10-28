# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(cloned):
            if not cloned:
                return
            if target.val == cloned.val:
                return cloned
            left = dfs(cloned.left)
            if left:
                return left
            right = dfs(cloned.right)
            if right:
                return right
        return dfs(cloned)