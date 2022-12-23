"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # if not node:
        #     return None
        # newNode = Node(node.val,None)
        # hashMap = {}
        # visited = [False]*101
        # hashMap[newNode.val] = newNode
        # def dfs(newNode,node):
        #     if visited[node.val]:
        #         return
        #     visited[node.val] = True
        #     for neighbor in node.neighbors:
        #         ne = Node(neighbor.val,None) if neighbor.val not in hashMap else hashMap[neighbor.val]
        #         hashMap[ne.val] = ne
        #         newNode.neighbors.append(ne)
        #         dfs(ne,neighbor)
        #     return newNode
        # dfs(newNode,node)
        # return newNode  
        def dfs(node):
            clone = Node(node.val)
            hashMap[node.val] = clone
            for neighbor in node.neighbors:
                if neighbor.val not in hashMap:
                    dfs(neighbor)
                clone.neighbors.append(hashMap[neighbor.val])
            return clone
        if not node:
            return None
        hashMap = {}
        return dfs(node)