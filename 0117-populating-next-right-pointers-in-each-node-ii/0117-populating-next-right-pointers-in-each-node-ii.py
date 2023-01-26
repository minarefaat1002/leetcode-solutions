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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            length = len(q)
            for i in range(length-1):
                popped = q.popleft()
                popped.next = q[0]
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            popped = q.popleft()
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
        return root