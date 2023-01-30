class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        target = (1<<len(graph)) -1
        q = deque()
        visited = set()
        for i in range(len(graph)):
            mask = 1 << i
            q.append([i,mask,0]) # val , mask , length
            visited.add((i,mask))
        while q:
            val , mask,length = q.popleft()
            for temp in graph[val]:
                newMask = mask | (1<<temp)
                if newMask == target:
                    return length+1
                elif (temp,newMask) in visited:
                    continue
                visited.add((temp,newMask))
                q.append([temp,newMask,length+1])
        return 0 