# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        def dfs(root,isLeft):
            if not root:
                return 0
            if not root.left and not root.right:
                if isLeft:
                    return root.val
                else:
                    return 0
            return dfs(root.left,True) + dfs(root.right,False)
        return dfs(root,False)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        Sum = [0]
        if not root:
            return 0 
        if not root.left and not root.right:
            return 0
        Sum =[0]
        def dfs(root,isLeft):
            if not root:
                return
            if not root.left and not root.right:
                if isLeft:
                    Sum[0]+=root.val
                    return
                else:
                    return
            dfs(root.left,True)
            dfs(root.right,False)
        dfs(root,False)
        this is another solution
"""