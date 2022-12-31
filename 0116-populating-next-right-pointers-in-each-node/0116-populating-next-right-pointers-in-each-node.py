"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        stack.append(root)
        while stack and stack[0]:
            iterations = len(stack)
            for i in range(iterations):
                left = stack.pop(0)
                right = stack[0] if i < iterations-1 else None
                left.next = right
                stack.append(left.left)
                stack.append(left.right)
        return root