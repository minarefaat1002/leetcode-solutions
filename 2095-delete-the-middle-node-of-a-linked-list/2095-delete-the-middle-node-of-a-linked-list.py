# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        count = 0
        temp = head  # 2 -> 3 -> 5->6 ->2 ====> count = 5 ===> odd # 2=>3=>5=>6 ===> count = 2 
        while(temp!=None): 
            count+=1
            temp = temp.next
        middle = count//2
        temp = head
        for i in range(middle-1):
            temp=temp.next
        temp.next = temp.next.next
        return head