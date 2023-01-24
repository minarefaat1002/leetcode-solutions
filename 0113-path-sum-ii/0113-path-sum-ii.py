# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        arr = []
        def dfs(root,temp,Sum):
            if not root:
                return
            if not root.left and not root.right and root.val + Sum == targetSum:
                temp.append(root.val)
                arr.append(temp.copy())
                temp.pop()
            temp.append(root.val)
            dfs(root.left,temp,Sum+root.val)
            dfs(root.right,temp,Sum+root.val)
            temp.pop()
        dfs(root,[],0)
        return arr