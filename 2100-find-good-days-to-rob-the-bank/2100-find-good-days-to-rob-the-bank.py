class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:

        dp1 = [1]*len(security)
        dp2 = [1]*len(security)
        res = []
        for i in range(1,len(security)):
            dp1[i] += dp1[i-1] if security[i] <= security[i-1] else 0
        for i in range(len(security)-2,-1,-1):
            dp2[i] += dp2[i+1] if security[i] <= security[i+1] else 0
        for i in range(time,len(security)-time):
            if  dp1[i] >= time + 1 and dp2[i] >= time+1:
                res.append(i)
        return res
    