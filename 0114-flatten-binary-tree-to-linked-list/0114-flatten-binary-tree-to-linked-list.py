# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.cur = TreeNode(0)
        def dfs(root):
            if not root:
                return None
            left = root.left
            right = root.right
            root.left = None
            self.cur.right = root
            self.cur = self.cur.right
            dfs(left)
            dfs(right)
        dfs(root)
        return self.cur.right