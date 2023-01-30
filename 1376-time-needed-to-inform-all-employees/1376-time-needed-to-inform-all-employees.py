class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(head):
            if graph[head] == []:
                return 0
            Max = -1
            for neighbor in graph[head]:
                Max = max(Max,dfs(neighbor))
            return informTime[head] + Max
        graph = collections.defaultdict(list)
        for t,f in enumerate(manager):
            if t != headID:
                graph[f].append(t)
        return dfs(headID)