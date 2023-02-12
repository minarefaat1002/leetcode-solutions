class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(list)
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        res = [0]
        def dfs(root,parent):
            Sum = 0
            for neighbour in graph[root]:
                if neighbour == parent:
                    continue
                d = dfs(neighbour,root)
                Sum += d
                res[0] += math.ceil(d/seats)
            return 1 + Sum
        dfs(0,-1)
        return res[0]