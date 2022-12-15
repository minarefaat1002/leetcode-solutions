class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(node,temp):
            if node == len(graph)-1:
                res.append(temp.copy())
                return
            for node in graph[node]:
                temp.append(node)
                dfs(node,temp)
                temp.pop()
        dfs(0,[0])
        return res
            