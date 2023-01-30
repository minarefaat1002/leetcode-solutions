class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNode = [False]*len(graph)
        visited = [False]*(len(graph))
        res = []
        def dfs(vertex):
            if safeNode[vertex]:
                return True
            if visited[vertex]:
                return False
            visited[vertex] = True
            isSafe = True
            for neighbor in graph[vertex]:
                isSafe = isSafe and dfs(neighbor)
            safeNode[vertex] = isSafe
            return isSafe
        for i in range(len(graph)):
            if not visited[i]:
                dfs(i)
        for i,safe in enumerate(safeNode):
            if safe:
                res.append(i)
        return res
