class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 0 => red 1 == blue
        visited = [[False,False] for _ in range(n)]
        res = [float('inf')]*n
        res[0] = 0
        graphRed = collections.defaultdict(list)
        graphBlue = collections.defaultdict(list)
        for edge in redEdges:
            graphRed[edge[0]].append(edge[1])
        for edge in blueEdges:
            graphBlue[edge[0]].append(edge[1])
        graph = [graphRed,graphBlue]
        q = deque()
        q.append([0,0,0]) # vertex , color , length
        q.append([0,1,0])
        visited[0][0] = True
        visited[0][1] = True
        while q:
            vertex,color,length = q.popleft()
            res[vertex] = min(res[vertex],length)
            for neighbor in graph[1-color][vertex]:
                if not visited[neighbor][1-color]:
                    visited[neighbor][1-color] = True
                    q.append([neighbor,1-color,length+1])
        for i in range(n):
            if not visited[i][0] and not visited[i][1]:
                res[i] = -1
        return res