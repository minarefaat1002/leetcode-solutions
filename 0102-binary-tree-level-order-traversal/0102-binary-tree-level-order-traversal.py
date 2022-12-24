# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        res = []
        queue = []
        temp = []
        queue.append(root)
        res.append([root.val])
        while len(queue):
            for i in range(len(queue)):
                poped = queue.pop(0)
                if  poped.left:
                    queue.append(poped.left) 
                    temp.append(poped.left.val)
                if  poped.right:
                    queue.append(poped.right)
                    temp.append(poped.right.val)
            if temp:
                res.append(temp) 
            temp = []
        return res