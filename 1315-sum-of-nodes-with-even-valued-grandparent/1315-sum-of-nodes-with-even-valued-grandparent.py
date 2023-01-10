# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root,parent,grandParent):
            return ((root.val if grandParent and grandParent.val%2 == 0 else 0)+ dfs(root.left,root,parent) + dfs(root.right,root,parent)) if root else 0
        return dfs(root,None,None)