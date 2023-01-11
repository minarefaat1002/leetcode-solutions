class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {}
        Sum = [0]
        graph[edges[0][0]] = [edges[0][1]]
        used = [False]*n
        used[edges[0][0]] = True
        used[edges[0][1]] = True
        for edge in edges[1:]:
            if used[edge[0]]:
                if edge[0] not in graph:
                    graph[edge[0]] = []
                graph[edge[0]].append(edge[1])
                used[edge[1]] = True
            elif used[edge[1]]:
                if edge[1] not in graph:
                    graph[edge[1]] = []
                graph[edge[1]].append(edge[0])
                used[edge[0]] = True
        visited = [False]*n
        def dfs(vertex):
            visited[vertex] = True
            if vertex not in graph:
                if hasApple[vertex]:
                    return True
                return False
            hasAple = False
            for child in graph[vertex]:
                df = dfs(child)
                if df:
                    Sum[0]+=2
                hasAple = hasAple or df
            return hasAple or hasApple[vertex]
        for i in range(n):
            if not visited[i]:
                dfs(i)
        return Sum[0]