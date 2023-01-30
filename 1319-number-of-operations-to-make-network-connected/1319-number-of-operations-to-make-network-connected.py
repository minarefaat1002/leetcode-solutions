class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(v):
            if visited[v]:
                return 
            visited[v] = True
            for neighbor in graph[v]:
                dfs(neighbor)
        graph = collections.defaultdict(list)
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        visited = [False]*n
        components = 0
        for v in range(n):
            if not visited[v]:
                dfs(v)
                components+=1
        return (components-1) if len(connections) >= n-1 else -1