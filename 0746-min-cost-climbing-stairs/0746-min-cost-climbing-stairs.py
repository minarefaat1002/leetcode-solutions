class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        prevprev = 0
        for i in range(2,len(cost)):
            temp = prev
            prev = min(cost[i-1]+prev,cost[i-2]+prevprev)
            prevprev = temp 
        return min(prev+cost[-1] , prevprev+cost[-2])
