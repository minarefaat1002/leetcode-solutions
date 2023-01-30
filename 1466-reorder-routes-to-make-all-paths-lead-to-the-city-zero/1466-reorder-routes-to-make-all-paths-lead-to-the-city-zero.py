class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        directions = set()
        visited = [False]*n
        for edge in connections:
            directions.add((edge[0],edge[1]))
        def dfs(vertex):
            if len(graph[vertex]) == 1 and vertex != 0:
                return 0
            visited[vertex] = True
            Sum = 0
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    visited[vertex] = True
                    Sum+= dfs(neighbor) + (1 if (vertex,neighbor) in directions else 0)
            return Sum
        graph = collections.defaultdict(list)
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        return dfs(0)