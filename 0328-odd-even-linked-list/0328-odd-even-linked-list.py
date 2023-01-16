# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = ListNode(0)
        even = ListNode(0) 
        temp = head 
        temp1 = odd
        temp2 = even
        i = 1
        last = None
        while temp:
            if i%2 == 1:
                temp1.next = temp
                temp1 = temp1.next
                last = temp1
            else:
                temp2.next = temp
                temp2 = temp2.next
            temp = temp.next
            i+=1
        temp1.next = None
        temp2.next = None
        last.next = even.next
        return odd.next
        