# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        head1 = head
        dp = {}
        def dfs(head,root):
            if not head:
                return True
            if not root:
                return False
            if (root,head) in dp:
                return dp[(root,head)]
            if head.val == root.val:
                dp[(root,head)] = dfs(head.next,root.left) or dfs(head.next,root.right) or dfs(head1,root.left) or dfs(head1,root.right)
                return dp[(root,head)]
            else:
                dp[(root,head)] = dfs(head1,root.left) or dfs(head1,root.right)
                return dp[(root,head)]
        return dfs(head,root)