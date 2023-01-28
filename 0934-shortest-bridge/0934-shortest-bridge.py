class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def findFirstIsland(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] ==1:
                        dfs(i,j)
                        return
        def dfs(i,j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0 or (i,j) in visited:
                return 
            q.append([i,j,0])
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        visited = set()
        q = deque()
        findFirstIsland(grid)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            x,y,moves = q.popleft()
            for d in directions:
                dx = d[0]
                dy = d[1]
                newX = x + dx
                newY = y + dy
                if newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid[0]) and (newX,newY) not in visited:
                    if grid[newX][newY] == 1:
                        return moves
                    q.append([newX,newY,moves+1])
                    visited.add((newX,newY))
            