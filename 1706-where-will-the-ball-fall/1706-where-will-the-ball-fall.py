class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = [-1]*len(grid[0])
        for j in range(len(grid[0])):
            flag = True
            newJ = j
            for i in range(len(grid)):
                if (newJ == 0 and grid[i][newJ]== -1) or (newJ==len(grid[0])-1 and grid[i][newJ]==1) or (newJ<len(grid[0])-1 and grid[i][newJ] == 1 and grid[i][newJ+1] == -1) or (newJ > 0 and grid[i][newJ]==-1 and grid[i][newJ-1]==1 ):
                    res[j] = -1
                    flag = False
                    break
                newJ = newJ + grid[i][newJ]
                i+=1
            if flag:
                res[j] = newJ
        return res