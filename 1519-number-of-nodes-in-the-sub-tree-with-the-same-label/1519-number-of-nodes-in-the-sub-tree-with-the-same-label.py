class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = {}
        res = [1]*len(labels)
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [False]*n
        
        def dfs(vertex):
            if visited[vertex]:
                return {}
            visited[vertex] = True        
            counter = Counter(labels[vertex])
            for child in graph[vertex]:
                childCounter = dfs(child)
                for char in childCounter:
                    counter[char] = counter.get(char,0) + childCounter[char]
            res[vertex] = counter[labels[vertex]]
            return counter
        dfs(0)
        return res