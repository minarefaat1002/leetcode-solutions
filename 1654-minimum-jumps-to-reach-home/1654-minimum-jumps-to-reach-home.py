class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited = set()
        q = deque()
        q.append([0,0,False]) # pos , length,backward
        visited.add((0,0))
        visited.add((0,1))
        for f in forbidden:
            visited.add((f,0)) # 0 forward
            visited.add((f,1)) # 1 backward
        while q:
            pos,length,backward = q.popleft()
            if pos == x:
                return length
            if pos+a >= 0 and ((pos+a,0) not in visited) and pos+a < 10000:
                visited.add((pos+a,0))
                q.append([pos+a,length+1,False])
            if pos-b>=0 and (not backward) and ((pos-b,1) not in visited):
                visited.add((pos-b,1))
                q.append([pos-b,length+1,True])
        return -1