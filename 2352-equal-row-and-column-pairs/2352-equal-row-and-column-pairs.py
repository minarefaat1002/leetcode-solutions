class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = Counter(tuple(row) for row in grid)
        res = 0
        for j in range(len(grid[0])):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][j])
            res += count.get(tuple(col),0)
        return res