class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse = True)
        ans = 0
        for j in range(len(grid[0])):
            Max = float('-inf')
            for i in range(len(grid)):
                Max = max(Max,grid[i][j])
            ans+=Max
        return ans
            