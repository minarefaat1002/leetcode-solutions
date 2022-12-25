class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4,n+1):
            dp[i] = i
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i] , 1 + dp[i-j*j])
                j+=1
        return dp[n]