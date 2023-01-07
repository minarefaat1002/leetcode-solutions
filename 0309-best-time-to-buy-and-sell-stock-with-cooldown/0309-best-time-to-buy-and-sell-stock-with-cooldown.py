class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0=>noStock       1 => inHand     2===> sell
        dp = [[0,0,0] for i in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1,len(prices)):
            price = prices[i]
            dp[i][0] = max(dp[i-1][0],dp[i-1][2])
            dp[i][1] = max(dp[i-1][0]-price,dp[i-1][1])
            dp[i][2] = dp[i-1][1] + price
        return max(dp[-1][2],dp[-1][0])