class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        visited = [False]*n
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        def dfs(node,destination):
            if destination == node:
                return True
            visited[node] = True
            for node in graph[node]:
                if not visited[node]:
                    if dfs(node,destination):
                        return True
        return dfs(source,destination)