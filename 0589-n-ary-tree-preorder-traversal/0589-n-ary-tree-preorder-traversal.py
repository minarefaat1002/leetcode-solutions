"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if not node.children:
                continue
            for i in range(len(node.children)-1,-1,-1):
                stack.append(node.children[i])
        return res