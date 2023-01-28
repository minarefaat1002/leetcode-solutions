class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0 or (i,j) in visited:
                return
            grid[i][j] = 0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        count = 0 
        visited = set()   
        for i in range(len(grid)):
                if grid[i][0] == 1 and (i,0) not in visited:
                    dfs(i,0)
                if grid[i][-1] == 1 and (i,len(grid[0])-1) not in visited:
                    dfs(i,len(grid[0])-1)
        for j in range(len(grid[0])):
            if grid[0][j] == 1 and (0,j) not in visited:
                dfs(0,j)
            if grid[-1][j] == 1 and (len(grid)-1,j) not in visited:
                dfs(len(grid)-1,j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
        return count