# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        def dfs(root,level):
            if not root:
                return 
            if len(arr)<level:
                arr.append([])
                arr[level-1].append(root.val)
            else:
                arr[level-1].append(root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        dfs(root,1)
        for i in range(len(arr)):
            if i%2 == 1:
                arr[i] = arr[i][::-1]
        return arr