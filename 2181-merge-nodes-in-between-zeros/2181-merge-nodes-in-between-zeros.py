# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        Sum = 0
        dummy = ListNode(0,None)
        cur = dummy
        Sum = 0
        while temp:
            if temp.val == 0:
                temp1 = temp
                temp = temp.next
                while temp and temp.val != 0:
                    Sum+=temp.val
                    temp = temp.next
                if temp == None:
                    cur.next = temp1 if temp1.val != 0 else None
                elif temp.val == 0:
                    cur.next = ListNode(Sum,None)
                    cur = cur.next
                    Sum = 0
            else:
                cur.next = ListNode(temp.val,None)
                cur = cur.next
        return dummy.next
    
                    