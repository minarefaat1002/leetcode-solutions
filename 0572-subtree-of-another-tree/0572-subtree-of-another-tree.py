# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not subRoot: return True
            if not root: return False   # and subRoot but look at the previous condition 
            if self.sameTree(root,subRoot):
                return True
            else:
                return ( self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        def sameTree(self,root,subRoot):
            if not subRoot and not root: # if both are None
                return True
            if subRoot and root and subRoot.val == root.val: # to make sure that both of them is not empty
                return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))
            return False   # if one of the trees is empty and  the other is not empty 
# time complexity is O(n*m) where n is the no. of nodes in the root tree and m is the no. of nodes in the subRoot tree