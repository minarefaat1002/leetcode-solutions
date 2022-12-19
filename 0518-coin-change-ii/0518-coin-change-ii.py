class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(len(coins)+1)] for j in range(amount+1)]
        for j in range(len(coins)+1):
            dp[0][j] = 1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if i - coins[j-1] >=0:
                    dp[i][j] = dp[i-coins[j-1]][j] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]