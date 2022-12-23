"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        newNode = Node(node.val,None)
        hashMap = {}
        hashMap[newNode.val] = newNode
        def dfs(newNode,node):
            for neighbor in node.neighbors:
                if neighbor.val in hashMap:
                    ne = hashMap[neighbor.val]
                    newNode.neighbors.append(ne)
                else:
                    ne = Node(neighbor.val,None)
                    hashMap[ne.val] = ne
                    newNode.neighbors.append(ne)
                    dfs(ne,neighbor)
            return newNode
        dfs(newNode,node)
        return newNode    