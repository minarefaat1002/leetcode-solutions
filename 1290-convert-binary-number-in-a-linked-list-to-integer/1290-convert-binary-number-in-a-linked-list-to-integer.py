# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res =0
        counter =0
        temp = head
        while temp:
            counter +=1
            temp = temp.next
        for i in range(counter-1,-1,-1):
            res += head.val * (2**i)
            head = head.next
        return res