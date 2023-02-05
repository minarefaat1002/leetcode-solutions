class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        i = n - 1
        j = n - 1
        dp = [0]*n
        count = 0
        Max = -1
        while i >= 0:
            num = prizePositions[i]
            count += 1
            while prizePositions[j] - prizePositions[i] > k:
                j-=1
                count-=1
            Max = max(Max,count)
            dp[i] = Max
            i-=1
        Max = -1
        j = 0
        res = 0
        count = 0
        for i in range(n):
            count += 1
            while prizePositions[i] - prizePositions[j] > k:
                j+=1
                count -= 1
            Max = max(Max,count)
            if i < n-1:
                res = max(Max+dp[i+1],res)
            else:
                res = max(res,Max,dp[-1])
        return res
            
            
            
                
                