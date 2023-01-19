# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # arr = []
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     arr.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # newRoot = TreeNode(0,None,None)
        # temp = newRoot
        # for i in range(len(arr)):
        #     temp.right = TreeNode(arr[i],None,None)
        #     temp = temp.right
        # return newRoot.right
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            root.left = None
            self.cur.right = root
            self.cur = self.cur.right
            dfs(root.right)
        ans = self.cur = TreeNode(0)
        dfs(root)
        return ans.right