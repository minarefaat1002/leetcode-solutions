# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int):
        def dfs(root):
            if not root:
                root = TreeNode(val)
            if val > root.val and not root.right:
                root.right = TreeNode(val)
            elif val < root.val and not root.left:
                root.left = TreeNode(val)
            if val > root.val:
                dfs(root.right)
            elif val < root.val:
                dfs(root.left)
            return root
        return dfs(root)
