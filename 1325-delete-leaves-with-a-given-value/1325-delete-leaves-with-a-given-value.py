# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            if dfs(root.left):
                root.left = None
            if dfs(root.right):
                root.right = None
            if root.val == target and not root.left and not root.right:
                return True
            return False
        if dfs(root):
            return None
        return root