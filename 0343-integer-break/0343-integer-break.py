class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,len(dp)):
            for j in range(1,i):
                dp[i] = max(dp[i],dp[j]*dp[i-j],j*(i-j),j*dp[i-j])
        return dp[-1]