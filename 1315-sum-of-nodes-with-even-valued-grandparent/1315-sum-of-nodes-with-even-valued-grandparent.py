# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        Sum = [0]
        def dfs(root,parent,grandParent):
            if not root:
                return None
            if grandParent and grandParent.val % 2 == 0:
                Sum[0] += root.val
            dfs(root.left,root,parent)
            dfs(root.right,root,parent)
        dfs(root,None,None)
        return Sum[0]