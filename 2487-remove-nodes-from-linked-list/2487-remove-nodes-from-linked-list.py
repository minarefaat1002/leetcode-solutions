# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self,head):
        prev,curr = None , head
        while curr:
            nxt=curr.next
            curr.next = prev
            prev = curr
            curr=nxt
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(float('inf'),None)
        rear = front
        while head:
            while head.val > rear.val:
                rear = rear.next
            temp = head.next
            head.next = rear
            rear = head
            head = temp
        return self.reverseLinkedList(rear).next
