# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # to handle [] case
            return None
        if not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head 
        head.next  = None
        return newHead
    #recursive : T O(n) , M O(n)
    '''
     # this solution is  T O(n) and M O(1)
          prev,curr = None , head
          while curr:
                nxt=curr.next
                curr.next = prev
                prev = curr
                curr=nxt
          return prev
    '''