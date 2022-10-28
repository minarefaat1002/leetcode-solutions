class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        r = 0
        Max = float('-inf')
        timeSum = 0
        while r < len(colors):
            if colors[l] == colors[r]:
                Max = max(Max,neededTime[r])
                r+=1
            else:
                l=r
                timeSum += Max
                Max = 0
        return sum(neededTime)-timeSum-Max