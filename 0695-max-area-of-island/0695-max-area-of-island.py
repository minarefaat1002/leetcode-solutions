class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        area = 0 
        def dfs(r,c):
            if r < 0 or c < 0 or r>= len(grid) or c>= len(grid[0]) or grid[r][c] == 0 or (r,c) in visit:
                return 0 
            visit.add((r,c))
            return 1+ dfs(r,c-1) + dfs(r,c+1) + dfs(r-1,c) + dfs(r+1 ,c )
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visit:
                    area = max(area,dfs(i,j))
        return area 