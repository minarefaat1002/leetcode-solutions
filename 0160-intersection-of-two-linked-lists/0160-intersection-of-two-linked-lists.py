# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # we can solve it using hashset but space complexity is O(N)
        # tempA = headA
        # count1 = 0
        # count2 = 0
        # tempB = headB
        # while tempA:
        #     count1+=1
        #     tempA = tempA.next
        # while tempB:
        #     count2+=1
        #     tempB = tempB.next
        # tempA = headA
        # tempB = headB
        # if count2 > count1:
        #     for i in range(count2-count1):
        #         tempB = tempB.next
        # if count1 > count2:
        #     for i in range(count1-count2):
        #         tempA = tempA.next
        # while tempA and tempB:
        #     if tempA == tempB:
        #         return tempA
        #     else:
        #         tempA = tempA.next
        #         tempB = tempB.next
        # return None
        # the above solution has time complexity of (O(m+n)) 
        l1, l2 = headA, headB    
        while l1 != l2: # when they are equal that means intersection so that we return l1 
            l1 = l1.next if l1 else headB 
            l2 = l2.next if l2 else headA
        return l1
        # this solution has time complexity of O(n+m) and spce complexity of O(1) and it's more readable than the previous solution 