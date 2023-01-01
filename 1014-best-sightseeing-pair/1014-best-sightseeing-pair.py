class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        Max = values[0]
        res = float('-inf')
        for i in range(1,len(values)):
            res = max(res,Max + values[i] - i)
            Max = max(Max,i+values[i])
        return res