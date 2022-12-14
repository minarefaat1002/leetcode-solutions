# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head = ListNode(0,None)
        # temp = head
        # while l1 and l2:
        #     newNode = ListNode(0,None)
        #     if l1.val < l2.val:
        #         newNode.val = l1.val
        #         l1 = l1.next
        #     else:
        #         newNode.val = l2.val
        #         l2 = l2.next
        #     temp.next = newNode
        #     temp = temp.next
        # if l1:
        #     temp.next = l1
        # if l2:
        #     temp.next = l2
        # return head.next
        # the above solution has time complexity of O(n) and space complexity of O(n)
        dummy = ListNode(0,None)
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next
        # the above solution has time complexity of O(n) and constant space complexity