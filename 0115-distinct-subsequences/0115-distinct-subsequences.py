class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # i ===> t and j =====>s
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == len(t):
                return 1
            elif j == len(s):
                return 0
            if t[i] == s[j]:
                dp[(i,j)] = dfs(i+1,j+1) + dfs(i,j+1)
                return dp[(i,j)]
            else:
                dp[(i,j)] = dfs(i,j+1)
                return dp[(i,j)]
        return dfs(0,0)