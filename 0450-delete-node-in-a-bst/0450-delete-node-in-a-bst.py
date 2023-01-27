# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successor(root):
            cur = root.left
            while cur.right:
                cur = cur.right
            return cur.val
        def delete(root,key):
            if not root:
                return None
            if key > root.val:
                root.right = delete(root.right,key)
            elif key < root.val:
                root.left = delete(root.left,key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    root.val = successor(root)
                    root.left = delete(root.left,root.val)
            return root
        root = delete(root,key)
        return root
