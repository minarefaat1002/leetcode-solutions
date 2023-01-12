# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(0,None)
        new = newList
        cur = head
        while cur:
            temp = cur.next
            repeated = False
            while temp and temp.val == cur.val:
                temp = temp.next
                repeated = True
            if repeated:
                new.next = temp
                cur = temp
            else:
                new.next = cur
                new = new.next
                cur = cur.next
        return newList.next               
                
            