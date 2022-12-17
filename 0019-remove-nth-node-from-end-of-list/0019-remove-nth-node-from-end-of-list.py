# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head 
        counter = 0
        while temp !=None :
            counter +=1
            temp = temp.next
        temp = head 
        if counter ==n:
            return head.next
        while temp !=None:
            if counter-1 == n:
                temp.next = temp.next.next
                break
            temp = temp.next
            counter-=1
        return head 