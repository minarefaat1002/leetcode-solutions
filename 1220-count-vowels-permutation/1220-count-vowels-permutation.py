class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[],[1,1,1,1,1]]
        mod = 10**9 + 7
        for i in range(2,n+1):
            dp.append([0,0,0,0,0])
            dp[i][0] = dp[i-1][1] + dp[i-1][4] + dp[i-1][2]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = dp[i-1][1] + dp[i-1][3]
            dp[i][3] = dp[i-1][2]
            dp[i][4] = dp[i-1][3] + dp[i-1][2]
        return sum(dp[n]) % mod
    