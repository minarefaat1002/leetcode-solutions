class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        def dfs(prevr,prevc,r,c):
            found = False
            if (r,c) in visited:
                return True
            visited.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for d in directions:
                newR = r + d[0]
                newC = c + d[1]
                if (prevr != newR or prevc != newC) and newR >= 0 and newC >= 0 and newR <len(grid) and newC < len(grid[0]) and grid[r][c] == grid[newR][newC]:
                    found = found or dfs(r,c,newR,newC)
            return found
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if (i,j) not in visited and dfs(-1,-1,i,j):
                    return True 
        return False 
    
