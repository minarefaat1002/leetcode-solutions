class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        Set = set()
        for edge in edges:
            Set.add(edge[1])
        res = []
        for i in range(n):
            if i not in Set:
                res.append(i)
        return res