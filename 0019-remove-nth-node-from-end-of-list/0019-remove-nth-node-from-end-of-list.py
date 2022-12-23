# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def dfs(head):
            if not head:
                return 0
            cur = dfs(head.next) + 1
            if cur == n+1:
                head.next = head.next.next
            return cur
        dummy = ListNode(0,head)
        dfs(dummy)
        return dummy.next
'''
another solution by we can use two pointers and keep the distance between them as n.
'''