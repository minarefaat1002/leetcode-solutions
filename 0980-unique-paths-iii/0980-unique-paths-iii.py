class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        counter=[0]
        startr = 0 
        startc = 0
        obstacles = [0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==-1:
                    obstacles[0]+=1
                if grid[i][j] ==1:
                    startr = i
                    startc = j
        hashset =set()
        def dfs(n,i,j):
            if (i,j) in hashset:
                return
            if i<0 or i==len(grid) or j<0 or j==len(grid[0]) or grid[i][j] == -1:
                return
            if grid[i][j]==2 and n==len(grid)*len(grid[0])-obstacles[0]:
                counter[0]+=1
                return
            elif grid[i][j] ==2:
                return
            hashset.add((i,j))
            dfs(n+1,i+1,j)
            dfs(n+1,i,j+1)
            dfs(n+1,i-1,j)
            dfs(n+1,i,j-1)
            hashset.remove((i,j))
        dfs(1,startr,startc)
        return counter[0]