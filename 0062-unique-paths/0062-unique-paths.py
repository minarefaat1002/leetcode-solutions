class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [ [ 0 for i in range(n) ] for j in range(m) ]
        def backTracking(curRow , curCol,m,n) -> int:
            if curRow == m or curCol ==n:
                return 0
            if curRow ==m-1 and curCol ==n-1:
                return 1
            if memo[curRow][curCol] !=0:
                return memo[curRow][curCol]
            memo[curRow][curCol] = backTracking(curRow , curCol+1,m,n) + backTracking(curRow+1,curCol,m,n)
            return memo[curRow][curCol]
        return backTracking(0,0,m,n)