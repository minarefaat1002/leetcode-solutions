class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[float('inf')] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    left = ans[i][j-1] if j > 0 else float('inf')
                    up = ans[i-1][j] if i > 0 else float('inf')
                    ans[i][j] = min(left,up) + 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    right = ans[i][j+1] if j < m-1 else float('inf')
                    down = ans[i+1][j] if i < n-1 else float('inf')
                    ans[i][j] = min(ans[i][j],min(right,down) + 1)
        return ans 
    