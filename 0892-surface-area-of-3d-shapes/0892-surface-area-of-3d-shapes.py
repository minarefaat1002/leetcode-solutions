class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        totalArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                totalArea += max(0,grid[i][j]-grid[i][j+1]) if j<len(grid[0])-1 else grid[i][j]
                totalArea += max(0,grid[i][j]-grid[i][j-1]) if j > 0 else grid[i][j]
                totalArea += max(0,grid[i][j]-grid[i+1][j])  if i < len(grid) - 1 else grid[i][j]
                totalArea += max(0,grid[i][j]-grid[i-1][j]) if i > 0 else grid[i][j]
                totalArea += 2 if grid[i][j] > 0 else 0
        return totalArea 
