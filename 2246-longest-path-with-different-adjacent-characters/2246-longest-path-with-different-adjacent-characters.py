class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = {}
        if len(parent) == 1:
            return 1
        for i in range(1,len(parent)):
            p = parent[i]
            if i not in graph:
                graph[i] = []
            if p not in graph:
                graph[p] = []
            graph[i].append(p)
            graph[p].append(i)
        visited = [False]*len(s)
        ans = [float('-inf')]
        def dfs(vertex):
            if visited[vertex]:
                return 0
            visited[vertex] = True 
            maxChildPath1 = 0
            maxChildPath2 = 0
            for child in graph[vertex]:
                curChildPath = dfs(child)
                if  s[vertex] != s[child]:
                    if curChildPath >= maxChildPath1:
                        maxChildPath2 = maxChildPath1
                        maxChildPath1 = curChildPath
                    elif curChildPath >= maxChildPath2:
                        maxChildPath2 = curChildPath
            ans[0] = max(ans[0],1 + maxChildPath1 + maxChildPath2)
            return 1 + max(maxChildPath1,maxChildPath2)
        dfs(0)
        return ans[0]