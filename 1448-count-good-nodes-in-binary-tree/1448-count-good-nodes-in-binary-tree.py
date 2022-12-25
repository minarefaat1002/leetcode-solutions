# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def dfs(root,Max):
            if root.val>=Max:
                count[0]+=1
            Max = max(Max,root.val)
            if root.left:
                dfs(root.left,Max)
            if root.right:
                dfs(root.right,Max)
        dfs(root,float('-inf'))
        return count[0]