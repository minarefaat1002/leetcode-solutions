# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        def construct(Min,Max):
            if  self.i < len(preorder) and preorder[self.i] > Min and preorder[self.i] < Max:
                root = TreeNode(preorder[self.i],None,None)
                self.i+=1
            else:
                return None
            root.left = construct(Min,root.val)
            root.right = construct(root.val,Max)
            return root
        return construct(float('-inf'),float('inf'))