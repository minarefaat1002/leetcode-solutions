class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        visited = set()
        def dfs(i,j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return False
            if grid[i][j] == 1 or (i,j) in visited:
                return True
            visited.add((i,j))
            d1 = dfs(i+1,j) 
            d2 = dfs(i,j+1) 
            d3 = dfs(i-1,j) 
            d4 = dfs(i,j-1)
            return d1 and d2 and d3 and d4
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i,j) not in visited and dfs(i,j):
                    count += 1
        return count 
