class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[1,0,0] for _ in range(n+1)]
        dp[1][0] = 1
        for i in range(2,n+1):
            for j in range(3):
                dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]
                dp[i][1] = dp[i-2][0] + dp[i-1][2]
                dp[i][2] = dp[i-2][0] + dp[i-1][1]
        return dp[-1][0]%MOD