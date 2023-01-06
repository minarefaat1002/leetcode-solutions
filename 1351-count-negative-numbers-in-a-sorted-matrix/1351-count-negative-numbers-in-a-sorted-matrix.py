class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # count = 0 
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] < 0 :
        #             count += 1
        # return count 
        i = len(grid)-1
        j = 0
        count = 0
        while i >= 0 and j<len(grid[0]):
            if grid[i][j] < 0:
                count += len(grid[0]) - j
                i-=1
            else:
                j+=1
        return count
