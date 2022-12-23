class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visit = set()
        counter  = 0 
        def dfs(i,j):
            if i<0 or j <0 or i>=len(grid1) or j >=len(grid1[0]) or (i,j) in visit or grid2[i][j] == 0:
                return True 
            visit.add((i,j))
            res = True 
            if grid1[i][j]== 0:
                res = False
            res = dfs(i-1,j) and res 
            res = dfs(i+1,j) and res 
            res = dfs(i,j-1) and res 
            res = dfs(i,j+1) and res 
            return res 
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and (i,j) not in visit and dfs(i,j):
                    counter+=1
        return counter 