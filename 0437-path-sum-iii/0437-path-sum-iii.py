# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashSums = {0:1}
        count = [0]
        def dfs(root,Sum):
            if not root:
                return
            Sum += root.val
            count[0] += hashSums.get(Sum - targetSum,0)
            hashSums[Sum] = hashSums.get(Sum,0) + 1
            dfs(root.left,Sum)
            dfs(root.right,Sum)
            hashSums[Sum] -= 1
        dfs(root,0)
        return count[0]