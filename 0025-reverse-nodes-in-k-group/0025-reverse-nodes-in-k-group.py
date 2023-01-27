# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            if not node.next:
                return node
            head = reverse(node.next)
            node.next.next = node
            node.next = None
            return head 
        temp = head
        newHead = endOfLastPortion = ListNode(0,None)
        while temp:
            i = 1
            start = temp
            end = temp
            while i < k and end.next:
                i+=1
                end = end.next
            if i < k:
                endOfLastPortion.next = start
                return newHead.next
            temp = end.next
            end.next = None
            h = reverse(start)
            endOfLastPortion.next = h
            endOfLastPortion = start
        return newHead.next