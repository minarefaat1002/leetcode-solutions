class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1]*len(s) for _ in range(len(s))]
        def dfs(i,j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if i == j:
                dp[i][j] = 1
                return 1
            elif s[i] == s[j]:
                dp[i][j] = 2 + dfs(i+1,j-1)
                return dp[i][j]
            dp[i][j] = max(dfs(i+1,j),dfs(i,j-1))
            return dp[i][j]
        dfs(0,len(s)-1)
        return dp[0][len(s)-1]