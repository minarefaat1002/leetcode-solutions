# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent = [-1]
        def findHeight(root,val,height):
            if not root:
                return 0
            if root.val == val:
                return height
            parent[0] = root.val
            left = findHeight(root.left,val,height+1)
            if left:
                return left
            parent[0] = root.val
            right = findHeight(root.right,val,height+1)
            return right
        parent = [-1]
        xHeight = findHeight(root,x,0)
        xParent = parent[0]
        parent = [-1]
        yHeight = findHeight(root,y,0)
        yParent = parent[0]
        return xParent != yParent and xHeight == yHeight