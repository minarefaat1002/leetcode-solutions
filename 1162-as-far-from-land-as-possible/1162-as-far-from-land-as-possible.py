class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append([i,j,0])
                    visited.add((i,j))
        Max = -1
        while q:
            x,y,moves = q.popleft()
            if grid[x][y] == 0:
                Max = max(Max,moves)
            for d in directions:
                dx = d[0]
                dy = d[1]
                newX = x + dx
                newY = y + dy
                if newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid[0]) and (newX,newY) not in visited:
                    q.append([newX,newY,moves+1])
                    visited.add((newX,newY))
        return Max