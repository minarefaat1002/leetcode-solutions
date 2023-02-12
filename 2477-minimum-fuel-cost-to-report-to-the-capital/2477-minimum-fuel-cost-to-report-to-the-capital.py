class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(list)
        visited = [False]*(len(roads)+1)
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        res = [0]
        def dfs(root):
            if len(graph[root]) == 1 and root!=0:
                return 1
            if visited[root]:
                return 0
            visited[root] = True
            Sum = 0
            for neighbour in graph[root]:
                d = dfs(neighbour)
                Sum += d
                res[0] += math.ceil(d/seats)
            return 1 + Sum
        dfs(0)
        return res[0]