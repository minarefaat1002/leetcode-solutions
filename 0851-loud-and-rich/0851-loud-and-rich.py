class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def buildGraph():
            for i in range(len(richer)):
                graph[richer[i][1]].append(richer[i][0])
        def dfs(vertex):
            if visited[vertex]:
                return result[vertex]
            visited[vertex] = True
            Min = [quiet[vertex],vertex]
            for neighbor in graph[vertex]:
                d = dfs(neighbor)
                if Min[0] > d[0]:
                    Min[0] = d[0]
                    Min[1] = d[1]
            result[vertex] = Min
            return Min
        graph = collections.defaultdict(list)
        result = [0]*len(quiet)
        visited = [False]*len(quiet)
        buildGraph()
        for i in range(len(visited)):
            if not visited[i]:
                dfs(i)
        return [b for a,b in result]