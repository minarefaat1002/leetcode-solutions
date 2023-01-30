class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        Max = [-1]
        def dfs(head,time):
            if graph[head] == []:
                Max[0] = max(Max[0],time)
            for neighbor in graph[head]:
                dfs(neighbor,time+informTime[head])
        graph = collections.defaultdict(list)
        for t,f in enumerate(manager):
            if t != headID:
                graph[f].append(t)
        dfs(headID,0)
        return Max[0]