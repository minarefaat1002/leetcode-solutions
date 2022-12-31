# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy =None
        dummy = head
        while head.next:
            if head.val != head.next.val:
                head = head.next
            else:
                head.next = head.next.next
        return dummy
            