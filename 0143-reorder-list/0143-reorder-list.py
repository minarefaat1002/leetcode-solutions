# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head1 = head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        def reverse(node):
            if not node.next:
                return node
            head = reverse(node.next)
            node.next.next = node
            node.next = None
            return head
        head2 = reverse(slow)
        dummy = ListNode(0,None)
        temp = dummy
        while head1 and head2:
            temp.next = head1
            temp = temp.next
            head1 = head1.next
            temp.next = head2
            temp = temp.next
            head2 = head2.next
        if head1 == head2:
            temp.next = head1
            temp = temp.next
        temp.next = None
        head = dummy.next
        