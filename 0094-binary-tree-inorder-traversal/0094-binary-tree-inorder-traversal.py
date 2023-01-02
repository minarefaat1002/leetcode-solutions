# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

        # if not root:
        #     return root
        # def back(root,res):
        #     if not root:
        #         return False
        #     back(root.left,res)
        #     res.append(root.val)
        #     back(root.right,res)
        #     return res
        # return back(root,[])