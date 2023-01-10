class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = {}
        res = 0
        for row in grid:
            count[tuple(row)] = count.get(tuple(row),0) + 1
        for j in range(len(grid[0])):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][j])
            res += count.get(tuple(col),0)
        return res