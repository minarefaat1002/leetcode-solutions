class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        score = 0
        score += (2**(len(grid[0])-1))*len(grid)
        for j in range(1,len(grid[0])):
            onesCount = 0
            for i in range(len(grid)):
                if grid[i][0] == 0:
                    grid[i][j] = 1 - grid[i][j]
                if grid[i][j] == 1:
                    onesCount+=1
            score += (2**(len(grid[0]) - j-1))*max(onesCount,len(grid)-onesCount)
        return score