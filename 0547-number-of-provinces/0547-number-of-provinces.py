class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {}
        def buildGraph(isConnected):
            for i in range(len(isConnected)):
                vertex = i + 1
                for j in range(len(isConnected)):
                    neighbor = j + 1
                    if isConnected[i][j] == 1:
                        if vertex not in graph:
                            graph[vertex] = []
                        if vertex != neighbor:
                            graph[vertex].append(neighbor)
        buildGraph(isConnected)
        visited = [False]*(len(isConnected)+1)
        count = 0
        def dfs(vertex):
            if visited[vertex]:
                return 
            visited[vertex] = True
            if len(graph[vertex]) == 0:
                return
            for neighbor in graph[vertex]:
                dfs(neighbor)
        for i in range(1,len(isConnected)+1):
            if not visited[i]:
                dfs(i)
                count += 1
        return count