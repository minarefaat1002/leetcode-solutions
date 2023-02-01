class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        def dfs(i, j, grid):
            if i == len(grid):
                return j
            if grid[i][j] == 1:
                if j >= len(grid[0]) - 1 or grid[i][j+1] == -1:
                    return -1
                else:
                    return dfs(i + 1, j + 1, grid)
            if grid[i][j] == -1:
                if j <= 0 or grid[i][j-1] == 1:
                    return -1
                else:
                    return dfs(i + 1, j - 1, grid)
        ans = [None] * len(grid[0])
        for j in range(len(grid[0])):
            ans[j] = dfs(0, j, grid)
        return ans