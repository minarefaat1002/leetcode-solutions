class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if 1 in (grid[0][0],grid[-1][-1]):
            return -1
        q = deque([[0,0,1]])
        visited = set()
        directions = [[1,1],[-1,-1],[0,1],[1,0],[-1,0],[0,-1],[1,-1],[-1,1]]
        visited.add((0,0))
        while q:
            (i,j,length) = q.popleft()
            if i == -1 or j == -1 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 1:
                continue
            if i == len(grid) - 1 and j == len(grid[0])-1:
                return length
            for d in directions:
                newI = i + d[0]
                newJ = j + d[1]
                if (newI,newJ) not in visited:
                    q.append([newI,newJ,length+1])
                    visited.add((newI,newJ))
        return -1