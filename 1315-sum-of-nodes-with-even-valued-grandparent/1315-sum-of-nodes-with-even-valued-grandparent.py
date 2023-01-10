# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode,parent = None,grandParent = None) -> int:
            return ((root.val if grandParent and grandParent.val%2 == 0 else 0)+ self.sumEvenGrandparent(root.left,root,parent) + self.sumEvenGrandparent(root.right,root,parent)) if root else 0
