class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j] > prices[i]:
        #             maxProfit = max(maxProfit,prices[j]-prices[i])
        # return maxProfit
        # the above solution has time complexity of O(n^2)
        minPrice = float('inf')
        maxProfit = 0 
        for price in prices:
            minPrice = min(minPrice,price)
            maxProfit = max(maxProfit,price-minPrice)
        # the above solution has time complexity of O(n)
        return maxProfit
  