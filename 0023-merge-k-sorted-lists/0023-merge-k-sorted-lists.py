# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        counter = 0
        head = point = ListNode(0)
        arr = []
        for l in lists:
            if l:
                heapq.heappush(arr,(l.val,counter, l))
                counter+=1
        while arr:
            val,counter, node = heapq.heappop(arr)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(arr,(node.val,counter, node))
                counter+=1
        return head.next