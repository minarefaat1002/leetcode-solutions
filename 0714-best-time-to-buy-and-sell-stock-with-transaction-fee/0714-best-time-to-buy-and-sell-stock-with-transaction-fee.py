class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0,0] for i in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1,len(prices)):
            price = prices[i]
            dp[i][0] = max(dp[i-1][1] - price,dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + price - fee,dp[i-1][1])
        return dp[-1][1]