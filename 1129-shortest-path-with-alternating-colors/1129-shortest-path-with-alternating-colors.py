class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # -1 => red 1 == blue
        visitedFromRed = [False]*n
        visitedFromBlue = [False]*n
        res = [float('inf')]*n
        res[0] = 0
        graphRed = collections.defaultdict(list)
        graphBlue = collections.defaultdict(list)
        for edge in redEdges:
            graphRed[edge[0]].append(edge[1])
        for edge in blueEdges:
            graphBlue[edge[0]].append(edge[1])
        q = deque()
        q.append([0,-1,0]) # vertex , color , length
        q.append([0,1,0])
        visitedFromRed[0] = True
        visitedFromBlue[0] = True
        while q:
            vertex,color,length = q.popleft()
            res[vertex] = min(res[vertex],length)
            if color == -1:
                for neighbor in graphBlue[vertex]:
                    if not visitedFromBlue[neighbor]:
                        visitedFromBlue[neighbor] = True
                        q.append([neighbor,1,length+1])
            else:
                for neighbor in graphRed[vertex]:
                    if not visitedFromRed[neighbor]:
                        visitedFromRed[neighbor] = True
                        q.append([neighbor,-1,length+1])
        for i in range(n):
            if not visitedFromRed[i] and not visitedFromBlue[i]:
                res[i] = -1
        return res