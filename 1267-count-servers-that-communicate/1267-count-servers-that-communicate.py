class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        onesInRows = {}
        onesInCols = {}
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    onesInRows[i] = onesInRows.get(i,0) + 1
                    onesInCols[j] = onesInCols.get(j,0) + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and onesInRows[i] + onesInCols[j] > 2:
                    res +=1
        return res