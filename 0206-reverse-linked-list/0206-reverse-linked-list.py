# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None 
        cur = head 
        nextt = head.next
        temp = head 
        while cur:
            cur.next = prev
            prev = cur
            cur = nextt
            nextt = nextt.next if nextt else None
        return prev